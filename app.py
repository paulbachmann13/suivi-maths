import os
import re
import socket
import sqlite3
import sys
import threading
import unicodedata
import subprocess
import tempfile
from datetime import date

from markupsafe import Markup, escape
from flask import (Flask, abort, flash, g, redirect, render_template, request,
                   send_file, url_for)

BASE = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE, "data.db")
BROWSERS = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
]
RESULTATS = {"ok": "Réussi", "aide": "Avec aide", "ko": "Pas compris"}
SCORE = {"ok": 1.0, "aide": 0.5, "ko": 0.0}

PORT = int(os.environ.get("SUIVI_PORT", "5000"))
MODE_LAN = os.environ.get("SUIVI_LAN") == "1"

SCHEMA = """
CREATE TABLE IF NOT EXISTS chapitre (
    id INTEGER PRIMARY KEY, nom TEXT NOT NULL UNIQUE, ordre INTEGER DEFAULT 0,
    domaine TEXT DEFAULT '');
CREATE TABLE IF NOT EXISTS recap (
    chapitre_id INTEGER PRIMARY KEY REFERENCES chapitre(id), contenu TEXT NOT NULL DEFAULT '',
    rappel TEXT DEFAULT '');
CREATE TABLE IF NOT EXISTS notion (
    id INTEGER PRIMARY KEY, chapitre_id INTEGER NOT NULL REFERENCES chapitre(id),
    nom TEXT NOT NULL, UNIQUE(chapitre_id, nom));
CREATE TABLE IF NOT EXISTS exercice (
    id INTEGER PRIMARY KEY, notion_id INTEGER NOT NULL REFERENCES notion(id),
    titre TEXT NOT NULL, enonce TEXT NOT NULL, correction TEXT DEFAULT '',
    difficulte INTEGER DEFAULT 1, source TEXT DEFAULT '');
CREATE TABLE IF NOT EXISTS fiche (
    id INTEGER PRIMARY KEY, titre TEXT NOT NULL, date TEXT NOT NULL,
    statut TEXT DEFAULT 'brouillon', rappels INTEGER DEFAULT 1);
CREATE TABLE IF NOT EXISTS fiche_exo (
    fiche_id INTEGER NOT NULL REFERENCES fiche(id) ON DELETE CASCADE,
    exercice_id INTEGER NOT NULL REFERENCES exercice(id),
    ordre INTEGER DEFAULT 0, resultat TEXT, remarque TEXT DEFAULT '',
    PRIMARY KEY (fiche_id, exercice_id));
"""

app = Flask(__name__)
app.secret_key = "suivi-maths-local"


def db():
    if "db" not in g:
        g.db = sqlite3.connect(DB_PATH)
        g.db.row_factory = sqlite3.Row
        g.db.execute("PRAGMA foreign_keys = ON")
    return g.db


@app.teardown_appcontext
def close_db(_):
    conn = g.pop("db", None)
    if conn:
        conn.close()


def init_db():
    conn = sqlite3.connect(DB_PATH)
    conn.executescript(SCHEMA)
    if "domaine" not in [r[1] for r in conn.execute("PRAGMA table_info(chapitre)")]:
        conn.execute("ALTER TABLE chapitre ADD COLUMN domaine TEXT DEFAULT ''")
    if "rappel" not in [r[1] for r in conn.execute("PRAGMA table_info(recap)")]:
        conn.execute("ALTER TABLE recap ADD COLUMN rappel TEXT DEFAULT ''")
    if "rappels" not in [r[1] for r in conn.execute("PRAGMA table_info(fiche)")]:
        conn.execute("ALTER TABLE fiche ADD COLUMN rappels INTEGER DEFAULT 1")
    conn.commit()
    conn.close()


def notions_groupees():
    rows = db().execute(
        "SELECT n.id, n.nom, c.nom AS chapitre FROM notion n "
        "JOIN chapitre c ON c.id = n.chapitre_id ORDER BY c.ordre, c.nom, n.nom"
    ).fetchall()
    groupes = {}
    for r in rows:
        groupes.setdefault(r["chapitre"], []).append(r)
    return groupes


@app.template_filter("fmt")
def fmt(text):
    """Mini-mise en forme des recaps : '## titre', '- puce', '> encadré', '**gras**'."""
    html, in_list, in_code = [], False, False
    for raw in (text or "").split("\n"):
        if raw.strip().startswith("```"):
            if in_list:
                html.append("</ul>")
                in_list = False
            html.append("</code></pre>" if in_code else "<pre><code>")
            in_code = not in_code
            continue
        if in_code:
            html.append(str(escape(raw.rstrip())))
            continue
        line = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", str(escape(raw.rstrip())))
        line = re.sub(r"`([^`]+)`", r"<code>\1</code>", line)
        if line.startswith("- "):
            if not in_list:
                html.append("<ul>")
                in_list = True
            html.append(f"<li>{line[2:]}</li>")
            continue
        if in_list:
            html.append("</ul>")
            in_list = False
        if line.startswith("## "):
            html.append(f"<h3>{line[3:]}</h3>")
        elif line.startswith("&gt; "):
            html.append(f'<p class="box">{line[5:]}</p>')
        elif line.strip():
            html.append(f"<p>{line}</p>")
    if in_list:
        html.append("</ul>")
    return Markup("\n".join(html))


def _git(*args):
    try:
        r = subprocess.run(["git", *args], cwd=BASE, capture_output=True, text=True, timeout=5)
        return r.stdout.strip() if r.returncode == 0 else ""
    except (OSError, subprocess.SubprocessError):
        return ""


def numero_version():
    """Numéro de version = nombre de commits (augmente à chaque mise à jour du code)."""
    return _git("rev-list", "--count", "HEAD") or "?"


def libelle_version():
    date_commit = _git("log", "-1", "--format=%cd", "--date=format:%d/%m %H:%M")
    return f"v{numero_version()}" + (f" · {date_commit}" if date_commit else "")


VERSION_LANCEE = numero_version()
LIBELLE_VERSION = libelle_version()


@app.context_processor
def inject():
    return {"RESULTATS": RESULTATS, "version": LIBELLE_VERSION,
            "maj_dispo": numero_version() != VERSION_LANCEE}


@app.post("/redemarrer")
def redemarrer():
    """Relance l'appli (pour prendre en compte une mise à jour du code) puis recharge la page."""
    commande = f'title Suivi maths & timeout /t 2 /nobreak >nul & "{sys.executable}" app.py'
    flags = subprocess.CREATE_NEW_CONSOLE if os.name == "nt" else 0
    subprocess.Popen(commande, shell=True, cwd=BASE, creationflags=flags)
    threading.Timer(0.5, lambda: os._exit(0)).start()
    return render_template("redemarrage.html")


# ---------- Tableau de bord ----------

@app.route("/")
def index():
    rows = db().execute(
        "SELECT n.id AS notion_id, n.nom AS notion, c.nom AS chapitre, "
        "e.id AS exo_id, fe.resultat, f.date, f.id AS fid "
        "FROM notion n JOIN chapitre c ON c.id = n.chapitre_id "
        "LEFT JOIN exercice e ON e.notion_id = n.id "
        "LEFT JOIN fiche_exo fe ON fe.exercice_id = e.id AND fe.resultat IS NOT NULL "
        "LEFT JOIN fiche f ON f.id = fe.fiche_id "
        "ORDER BY c.ordre, c.nom, n.nom, f.date, f.id"
    ).fetchall()
    stats, dernier = {}, {}
    for r in rows:
        key = (r["chapitre"], r["notion_id"], r["notion"])
        stats.setdefault(key, set())
        if r["exo_id"] is not None:
            stats[key].add(r["exo_id"])
        if r["resultat"]:
            dernier[(r["notion_id"], r["exo_id"])] = r["resultat"]  # dernier résultat gagne
    chapitres = {}
    for (chap, nid, nom), exos in stats.items():
        res = [dernier[(nid, e)] for e in exos if (nid, e) in dernier]
        maitrise = round(100 * sum(SCORE[x] for x in res) / len(res)) if res else None
        chapitres.setdefault(chap, []).append(
            {"id": nid, "nom": nom, "total": len(exos), "faits": len(res), "maitrise": maitrise})
    return render_template("index.html", chapitres=chapitres)


# ---------- Exercices ----------

@app.route("/exos")
def exos():
    notion = request.args.get("notion", type=int)
    chapitre = request.args.get("chapitre", type=int)
    sql = ("SELECT e.*, n.nom AS notion, c.nom AS chapitre, "
           "(SELECT COUNT(*) FROM fiche_exo fe WHERE fe.exercice_id = e.id) AS nb_fiches "
           "FROM exercice e JOIN notion n ON n.id = e.notion_id "
           "JOIN chapitre c ON c.id = n.chapitre_id ")
    args = []
    if notion:
        sql += "WHERE n.id = ? "
        args.append(notion)
    elif chapitre:
        sql += "WHERE c.id = ? "
        args.append(chapitre)
    sql += "ORDER BY c.ordre, c.nom, n.nom, e.difficulte, e.id"
    return render_template("exos.html", exos=db().execute(sql, args).fetchall(),
                           groupes=notions_groupees(), notion=notion, chapitre=chapitre)


@app.route("/exos/new", methods=["GET", "POST"])
@app.route("/exos/<int:exo_id>/edit", methods=["GET", "POST"])
def exo_form(exo_id=None):
    exo = None
    if exo_id:
        exo = db().execute("SELECT * FROM exercice WHERE id = ?", (exo_id,)).fetchone()
        if not exo:
            abort(404)
    if request.method == "POST":
        f = request.form
        vals = (f["notion_id"], f["titre"].strip(), f["enonce"].strip(),
                f["correction"].strip(), int(f.get("difficulte", 1)), f["source"].strip())
        if exo:
            db().execute("UPDATE exercice SET notion_id=?, titre=?, enonce=?, correction=?, "
                         "difficulte=?, source=? WHERE id=?", vals + (exo_id,))
        else:
            db().execute("INSERT INTO exercice (notion_id, titre, enonce, correction, "
                         "difficulte, source) VALUES (?,?,?,?,?,?)", vals)
        db().commit()
        flash("Exercice enregistré.")
        return redirect(url_for("exos", notion=f["notion_id"]))
    return render_template("exo_form.html", exo=exo, groupes=notions_groupees(),
                           notion=request.args.get("notion", type=int))


@app.post("/exos/<int:exo_id>/delete")
def exo_delete(exo_id):
    if db().execute("SELECT 1 FROM fiche_exo WHERE exercice_id = ?", (exo_id,)).fetchone():
        flash("Impossible : cet exercice est utilisé dans une fiche.")
    else:
        db().execute("DELETE FROM exercice WHERE id = ?", (exo_id,))
        db().commit()
        flash("Exercice supprimé.")
    return redirect(url_for("exos"))


# ---------- Notions / chapitres ----------

@app.route("/notions", methods=["GET", "POST"])
def notions():
    if request.method == "POST":
        chap = request.form["chapitre"].strip()
        nom = request.form["notion"].strip()
        if chap and nom:
            conn = db()
            row = conn.execute("SELECT id FROM chapitre WHERE nom = ?", (chap,)).fetchone()
            if row:
                cid = row["id"]
            else:
                ordre = conn.execute("SELECT COALESCE(MAX(ordre),0)+1 FROM chapitre").fetchone()[0]
                cid = conn.execute("INSERT INTO chapitre (nom, ordre) VALUES (?,?)",
                                   (chap, ordre)).lastrowid
            conn.execute("INSERT OR IGNORE INTO notion (chapitre_id, nom) VALUES (?,?)", (cid, nom))
            conn.commit()
        return redirect(url_for("notions"))
    return render_template("notions.html", groupes=notions_groupees())


# ---------- Fiches recap (cours) ----------

def charger_recap(chap_id):
    chap = db().execute("SELECT * FROM chapitre WHERE id = ?", (chap_id,)).fetchone()
    if not chap:
        abort(404)
    row = db().execute("SELECT contenu FROM recap WHERE chapitre_id = ?", (chap_id,)).fetchone()
    return chap, (row["contenu"] if row else "")


@app.route("/recaps")
def recaps():
    rows = db().execute(
        "SELECT c.*, r.contenu IS NOT NULL AND r.contenu != '' AS a_recap, "
        "(SELECT COUNT(*) FROM exercice e JOIN notion n ON n.id = e.notion_id "
        " WHERE n.chapitre_id = c.id) AS nb_exos "
        "FROM chapitre c LEFT JOIN recap r ON r.chapitre_id = c.id ORDER BY c.ordre").fetchall()
    domaines = {}
    for r in rows:
        domaines.setdefault(r["domaine"] or "Autres", []).append(r)
    return render_template("recaps.html", domaines=domaines)


@app.route("/recaps/<int:chap_id>")
def recap_detail(chap_id):
    chap, contenu = charger_recap(chap_id)
    notions_ = db().execute("SELECT * FROM notion WHERE chapitre_id = ? ORDER BY id", (chap_id,)).fetchall()
    return render_template("recap_detail.html", chap=chap, contenu=contenu, notions=notions_)


@app.route("/recaps/<int:chap_id>/edit", methods=["GET", "POST"])
def recap_edit(chap_id):
    chap, contenu = charger_recap(chap_id)
    if request.method == "POST":
        db().execute("INSERT INTO recap (chapitre_id, contenu) VALUES (?,?) "
                     "ON CONFLICT(chapitre_id) DO UPDATE SET contenu = excluded.contenu",
                     (chap_id, request.form["contenu"].strip()))
        db().commit()
        flash("Fiche recap enregistrée.")
        return redirect(url_for("recap_detail", chap_id=chap_id))
    return render_template("recap_edit.html", chap=chap, contenu=contenu)


@app.route("/recaps/<int:chap_id>/print")
def recap_print(chap_id):
    chap, contenu = charger_recap(chap_id)
    return render_template("recap_print.html", chap=chap, contenu=contenu)


@app.route("/recaps/<int:chap_id>/pdf")
def recap_pdf(chap_id):
    chap, _ = charger_recap(chap_id)
    nom = f"recap_{chap_id:02d}_{re.sub(r'[^a-z0-9]+', '-', unicodedata.normalize('NFKD', chap['nom'].lower()).encode('ascii', 'ignore').decode()).strip('-')}.pdf"
    err = html_vers_pdf(f"recaps/{chap_id}/print", nom)
    if err:
        flash(err)
        return redirect(url_for("recap_detail", chap_id=chap_id))
    return send_file(os.path.join(BASE, "pdf", nom), mimetype="application/pdf", download_name=nom, as_attachment=True)


# ---------- Fiches ----------

@app.route("/fiches")
def fiches():
    rows = db().execute(
        "SELECT f.*, COUNT(fe.exercice_id) AS nb, "
        "SUM(fe.resultat IS NOT NULL) AS notes FROM fiche f "
        "LEFT JOIN fiche_exo fe ON fe.fiche_id = f.id GROUP BY f.id ORDER BY f.date DESC, f.id DESC"
    ).fetchall()
    return render_template("fiches.html", fiches=rows)


@app.route("/fiches/new", methods=["GET", "POST"])
def fiche_new():
    if request.method == "POST":
        ids = request.form.getlist("exo")
        if not ids:
            flash("Choisis au moins un exercice.")
            return redirect(url_for("fiche_new"))
        conn = db()
        fid = conn.execute("INSERT INTO fiche (titre, date, rappels) VALUES (?,?,?)",
                           (request.form["titre"].strip() or "Fiche d'exercices",
                            request.form.get("date") or date.today().isoformat(),
                            1 if request.form.get("rappels") else 0)).lastrowid
        for i, eid in enumerate(ids):
            conn.execute("INSERT INTO fiche_exo (fiche_id, exercice_id, ordre) VALUES (?,?,?)",
                         (fid, eid, i))
        conn.commit()
        return redirect(url_for("fiche_detail", fiche_id=fid))
    exos_ = db().execute(
        "SELECT e.id, e.titre, e.difficulte, e.notion_id, n.nom AS notion, c.nom AS chapitre, "
        "(SELECT group_concat(f.date) FROM fiche_exo fe JOIN fiche f ON f.id = fe.fiche_id "
        " WHERE fe.exercice_id = e.id) AS deja, "
        "(SELECT fe.resultat FROM fiche_exo fe JOIN fiche f ON f.id = fe.fiche_id "
        " WHERE fe.exercice_id = e.id AND fe.resultat IS NOT NULL "
        " ORDER BY f.date DESC, f.id DESC LIMIT 1) AS dernier "
        "FROM exercice e JOIN notion n ON n.id = e.notion_id JOIN chapitre c ON c.id = n.chapitre_id "
        "ORDER BY c.ordre, c.nom, n.nom, e.difficulte, e.id").fetchall()
    groupes = {}
    for e in exos_:
        groupes.setdefault((e["chapitre"], e["notion"]), []).append(e)
    return render_template("fiche_new.html", groupes=groupes, today=date.today().isoformat())


def charger_fiche(fiche_id):
    fiche = db().execute("SELECT * FROM fiche WHERE id = ?", (fiche_id,)).fetchone()
    if not fiche:
        abort(404)
    lignes = db().execute(
        "SELECT e.*, n.nom AS notion, fe.resultat, fe.remarque FROM fiche_exo fe "
        "JOIN exercice e ON e.id = fe.exercice_id JOIN notion n ON n.id = e.notion_id "
        "WHERE fe.fiche_id = ? ORDER BY fe.ordre", (fiche_id,)).fetchall()
    return fiche, lignes


@app.route("/fiches/<int:fiche_id>", methods=["GET", "POST"])
def fiche_detail(fiche_id):
    fiche, lignes = charger_fiche(fiche_id)
    if request.method == "POST":
        conn = db()
        for l in lignes:
            res = request.form.get(f"res_{l['id']}") or None
            conn.execute("UPDATE fiche_exo SET resultat=?, remarque=? WHERE fiche_id=? AND exercice_id=?",
                         (res, request.form.get(f"rem_{l['id']}", "").strip(), fiche_id, l["id"]))
        conn.execute("UPDATE fiche SET statut=?, rappels=? WHERE id=?",
                     (request.form["statut"], 1 if request.form.get("rappels") else 0, fiche_id))
        conn.commit()
        flash("Fiche enregistrée.")
        return redirect(url_for("fiche_detail", fiche_id=fiche_id))
    return render_template("fiche_detail.html", fiche=fiche, lignes=lignes)


@app.post("/fiches/<int:fiche_id>/delete")
def fiche_delete(fiche_id):
    db().execute("DELETE FROM fiche WHERE id = ?", (fiche_id,))
    db().commit()
    return redirect(url_for("fiches"))


def rappels_chapitres(chap_ids):
    """Un rappel par chapitre ; à défaut de rappel dédié, on reprend les encadrés du recap."""
    if not chap_ids:
        return []
    marques = ",".join("?" * len(chap_ids))
    rows = db().execute(
        f"SELECT c.nom, r.contenu, r.rappel FROM chapitre c LEFT JOIN recap r ON r.chapitre_id = c.id "
        f"WHERE c.id IN ({marques}) ORDER BY c.ordre", list(chap_ids)).fetchall()
    rappels = []
    for r in rows:
        lignes_box = [l for l in (r["contenu"] or "").splitlines() if l.startswith("> ")]
        texte = r["rappel"] or "\n".join(lignes_box)
        if texte.strip():
            rappels.append({"nom": r["nom"], "texte": texte})
    return rappels


@app.route("/fiches/<int:fiche_id>/print")
def fiche_print(fiche_id):
    fiche, lignes = charger_fiche(fiche_id)
    rappels = []
    if fiche["rappels"]:
        ids = [r[0] for r in db().execute(
            "SELECT DISTINCT n.chapitre_id FROM fiche_exo fe JOIN exercice e ON e.id = fe.exercice_id "
            "JOIN notion n ON n.id = e.notion_id WHERE fe.fiche_id = ?", (fiche_id,))]
        rappels = rappels_chapitres(ids)
    return render_template("print.html", fiche=fiche, lignes=lignes, rappels=rappels,
                           corrige=request.args.get("corrige") == "1")


@app.route("/exos/chapitre/<int:chap_id>/print")
def chapitre_print(chap_id):
    chap = db().execute("SELECT * FROM chapitre WHERE id = ?", (chap_id,)).fetchone()
    if not chap:
        abort(404)
    lignes = db().execute(
        "SELECT e.*, n.nom AS notion FROM exercice e JOIN notion n ON n.id = e.notion_id "
        "WHERE n.chapitre_id = ? ORDER BY e.difficulte, e.id", (chap_id,)).fetchall()
    fiche = {"titre": f"Exercices : {chap['nom']}", "date": date.today().isoformat()}
    rappels = rappels_chapitres([chap_id]) if request.args.get("rappels", "1") == "1" else []
    return render_template("print.html", fiche=fiche, lignes=lignes, rappels=rappels,
                           corrige=request.args.get("corrige") == "1")


@app.route("/exos/chapitre/<int:chap_id>/pdf")
def chapitre_pdf(chap_id):
    corrige = request.args.get("corrige") == "1"
    chap = db().execute("SELECT nom FROM chapitre WHERE id = ?", (chap_id,)).fetchone()
    if not chap:
        abort(404)
    slug = re.sub(r"[^a-z0-9]+", "-", unicodedata.normalize("NFKD", chap["nom"].lower())
                  .encode("ascii", "ignore").decode()).strip("-")
    nom = f"exos_{chap_id:02d}_{slug}{'_corrige' if corrige else ''}.pdf"
    q = "?" + "&".join(k + "=" + v for k, v in request.args.items() if k in ("corrige", "rappels"))
    err = html_vers_pdf(f"exos/chapitre/{chap_id}/print" + (q if len(q) > 1 else ""), nom)
    if err:
        flash(err)
        return redirect(url_for("exos", chapitre=chap_id))
    return send_file(os.path.join(BASE, "pdf", nom), mimetype="application/pdf", download_name=nom, as_attachment=True)


@app.route("/exos/notion/<int:notion_id>/print")
def notion_print(notion_id):
    notion = db().execute("SELECT * FROM notion WHERE id = ?", (notion_id,)).fetchone()
    if not notion:
        abort(404)
    lignes = db().execute(
        "SELECT e.*, n.nom AS notion FROM exercice e JOIN notion n ON n.id = e.notion_id "
        "WHERE n.id = ? ORDER BY e.difficulte, e.id", (notion_id,)).fetchall()
    fiche = {"titre": f"Exercices : {notion['nom']}", "date": date.today().isoformat()}
    rappels = rappels_chapitres([notion["chapitre_id"]]) if request.args.get("rappels", "1") == "1" else []
    return render_template("print.html", fiche=fiche, lignes=lignes, rappels=rappels,
                           corrige=request.args.get("corrige") == "1")


@app.route("/exos/notion/<int:notion_id>/pdf")
def notion_pdf(notion_id):
    corrige = request.args.get("corrige") == "1"
    notion = db().execute("SELECT nom FROM notion WHERE id = ?", (notion_id,)).fetchone()
    if not notion:
        abort(404)
    slug = re.sub(r"[^a-z0-9]+", "-", unicodedata.normalize("NFKD", notion["nom"].lower())
                  .encode("ascii", "ignore").decode()).strip("-")
    nom = f"exos_notion_{notion_id:02d}_{slug}{'_corrige' if corrige else ''}.pdf"
    q = "?" + "&".join(k + "=" + v for k, v in request.args.items() if k in ("corrige", "rappels"))
    err = html_vers_pdf(f"exos/notion/{notion_id}/print" + (q if len(q) > 1 else ""), nom)
    if err:
        flash(err)
        return redirect(url_for("exos", notion=notion_id))
    return send_file(os.path.join(BASE, "pdf", nom), mimetype="application/pdf", download_name=nom, as_attachment=True)


def html_vers_pdf(chemin, nom):
    """Imprime http://host/<chemin> en PDF avec Edge/Chrome. Renvoie un message d'erreur ou None."""
    browser = next((b for b in BROWSERS if os.path.exists(b)), None)
    if not browser:
        return "Edge/Chrome introuvable : utilise la page d'impression (Ctrl+P)."
    os.makedirs(os.path.join(BASE, "pdf"), exist_ok=True)
    out = os.path.join(BASE, "pdf", nom)
    if os.path.exists(out):
        os.remove(out)
    with tempfile.TemporaryDirectory() as profile:
        subprocess.run([browser, "--headless=new", "--disable-gpu", f"--user-data-dir={profile}",
                        "--no-pdf-header-footer", "--virtual-time-budget=8000",
                        f"--print-to-pdf={out}", f"http://127.0.0.1:{PORT}/" + chemin],
                       check=False, timeout=60, capture_output=True)
    return None if os.path.exists(out) else "Échec de la génération PDF."


@app.route("/fiches/<int:fiche_id>/pdf")
def fiche_pdf(fiche_id):
    corrige = request.args.get("corrige") == "1"
    fiche, _ = charger_fiche(fiche_id)
    nom = f"{fiche['date']}_{'corrige' if corrige else 'enonces'}_{fiche_id}.pdf"
    err = html_vers_pdf(f"fiches/{fiche_id}/print" + ("?corrige=1" if corrige else ""), nom)
    if err:
        flash(err)
        return redirect(url_for("fiche_detail", fiche_id=fiche_id))
    return send_file(os.path.join(BASE, "pdf", nom), mimetype="application/pdf", download_name=nom, as_attachment=True)


def ip_locale():
    """Adresse du PC sur le réseau local (celle à taper sur le téléphone)."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        sock.connect(("10.255.255.255", 1))
        return sock.getsockname()[0]
    except OSError:
        return None
    finally:
        sock.close()


@app.route("/telephone")
def telephone():
    ip = ip_locale() if MODE_LAN else None
    return render_template("telephone.html", url=f"http://{ip}:{PORT}" if ip else None, lan=MODE_LAN)


if __name__ == "__main__":
    init_db()
    if MODE_LAN:
        print()
        print(f"  Mode téléphone : ouvre http://{ip_locale()}:{PORT} sur ton téléphone (même Wi-Fi que le PC)")
        print()
    app.run(host="0.0.0.0" if MODE_LAN else "127.0.0.1", debug=False, port=PORT, threaded=True)
