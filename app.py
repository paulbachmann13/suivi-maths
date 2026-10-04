import os
import sqlite3
import subprocess
import tempfile
from datetime import date

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

SCHEMA = """
CREATE TABLE IF NOT EXISTS chapitre (
    id INTEGER PRIMARY KEY, nom TEXT NOT NULL UNIQUE, ordre INTEGER DEFAULT 0);
CREATE TABLE IF NOT EXISTS notion (
    id INTEGER PRIMARY KEY, chapitre_id INTEGER NOT NULL REFERENCES chapitre(id),
    nom TEXT NOT NULL, UNIQUE(chapitre_id, nom));
CREATE TABLE IF NOT EXISTS exercice (
    id INTEGER PRIMARY KEY, notion_id INTEGER NOT NULL REFERENCES notion(id),
    titre TEXT NOT NULL, enonce TEXT NOT NULL, correction TEXT DEFAULT '',
    difficulte INTEGER DEFAULT 1, source TEXT DEFAULT '');
CREATE TABLE IF NOT EXISTS fiche (
    id INTEGER PRIMARY KEY, titre TEXT NOT NULL, date TEXT NOT NULL,
    statut TEXT DEFAULT 'brouillon');
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


@app.context_processor
def inject():
    return {"RESULTATS": RESULTATS}


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
    sql = ("SELECT e.*, n.nom AS notion, c.nom AS chapitre, "
           "(SELECT COUNT(*) FROM fiche_exo fe WHERE fe.exercice_id = e.id) AS nb_fiches "
           "FROM exercice e JOIN notion n ON n.id = e.notion_id "
           "JOIN chapitre c ON c.id = n.chapitre_id ")
    args = []
    if notion:
        sql += "WHERE n.id = ? "
        args.append(notion)
    sql += "ORDER BY c.ordre, c.nom, n.nom, e.difficulte, e.id"
    return render_template("exos.html", exos=db().execute(sql, args).fetchall(),
                           groupes=notions_groupees(), notion=notion)


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
        fid = conn.execute("INSERT INTO fiche (titre, date) VALUES (?,?)",
                           (request.form["titre"].strip() or "Fiche d'exercices",
                            request.form.get("date") or date.today().isoformat())).lastrowid
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
        conn.execute("UPDATE fiche SET statut=? WHERE id=?", (request.form["statut"], fiche_id))
        conn.commit()
        flash("Fiche enregistrée.")
        return redirect(url_for("fiche_detail", fiche_id=fiche_id))
    return render_template("fiche_detail.html", fiche=fiche, lignes=lignes)


@app.post("/fiches/<int:fiche_id>/delete")
def fiche_delete(fiche_id):
    db().execute("DELETE FROM fiche WHERE id = ?", (fiche_id,))
    db().commit()
    return redirect(url_for("fiches"))


@app.route("/fiches/<int:fiche_id>/print")
def fiche_print(fiche_id):
    fiche, lignes = charger_fiche(fiche_id)
    return render_template("print.html", fiche=fiche, lignes=lignes,
                           corrige=request.args.get("corrige") == "1")


@app.route("/fiches/<int:fiche_id>/pdf")
def fiche_pdf(fiche_id):
    corrige = request.args.get("corrige") == "1"
    browser = next((b for b in BROWSERS if os.path.exists(b)), None)
    if not browser:
        flash("Edge/Chrome introuvable : utilise la page d'impression (Ctrl+P).")
        return redirect(url_for("fiche_detail", fiche_id=fiche_id))
    fiche, _ = charger_fiche(fiche_id)
    nom = f"{fiche['date']}_{'corrige' if corrige else 'enonces'}_{fiche_id}.pdf"
    out = os.path.join(BASE, "pdf", nom)
    url = request.host_url + f"fiches/{fiche_id}/print" + ("?corrige=1" if corrige else "")
    with tempfile.TemporaryDirectory() as profile:
        subprocess.run([browser, "--headless=new", "--disable-gpu", f"--user-data-dir={profile}",
                        "--no-pdf-header-footer", "--virtual-time-budget=8000",
                        f"--print-to-pdf={out}", url],
                       check=False, timeout=60, capture_output=True)
    if not os.path.exists(out):
        flash("Échec de la génération PDF.")
        return redirect(url_for("fiche_detail", fiche_id=fiche_id))
    return send_file(out, mimetype="application/pdf", download_name=nom)


if __name__ == "__main__":
    init_db()
    app.run(debug=False, port=5000, threaded=True)
