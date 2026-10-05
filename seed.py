"""Charge le programme de Seconde (chapitres, notions, fiches recap, exercices) dans la base.

Peut être relancé sans risque : ce qui existe déjà n'est pas dupliqué ni écrasé
(tes modifications de recaps et d'exercices sont conservées).
"""
import sqlite3

from app import DB_PATH, init_db
from contenu import algo_logique, fonctions, geometrie, nombres, stats_probas

MODULES = [nombres, fonctions, geometrie, stats_probas, algo_logique]
SOURCE = "Claude (programme Seconde 2019)"


def main():
    init_db()
    c = sqlite3.connect(DB_PATH)
    ordre = 0
    nb_exos = nb_recaps = 0
    for module in MODULES:
        for chap in module.CHAPITRES:
            ordre += 1
            row = c.execute("SELECT id FROM chapitre WHERE nom = ?", (chap["nom"],)).fetchone()
            if row:
                cid = row[0]
                c.execute("UPDATE chapitre SET ordre = ?, domaine = ? WHERE id = ?", (ordre, module.DOMAINE, cid))
            else:
                cid = c.execute("INSERT INTO chapitre (nom, ordre, domaine) VALUES (?,?,?)",
                                (chap["nom"], ordre, module.DOMAINE)).lastrowid
            notion_id = {}
            for nom in chap["notions"]:
                c.execute("INSERT OR IGNORE INTO notion (chapitre_id, nom) VALUES (?,?)", (cid, nom))
                notion_id[nom] = c.execute("SELECT id FROM notion WHERE chapitre_id = ? AND nom = ?",
                                           (cid, nom)).fetchone()[0]
            if c.execute("INSERT OR IGNORE INTO recap (chapitre_id, contenu) VALUES (?,?)",
                         (cid, chap["recap"].strip())).rowcount:
                nb_recaps += 1
            if chap.get("rappel"):
                c.execute("UPDATE recap SET rappel = ? WHERE chapitre_id = ? AND (rappel IS NULL OR rappel = '')",
                          (chap["rappel"].strip(), cid))
            for notion, titre, diff, enonce, corr in chap["exos"]:
                nid = notion_id[notion]
                if c.execute("SELECT 1 FROM exercice WHERE notion_id = ? AND titre = ?", (nid, titre)).fetchone():
                    continue
                c.execute("INSERT INTO exercice (notion_id, titre, enonce, correction, difficulte, source) "
                          "VALUES (?,?,?,?,?,?)", (nid, titre, enonce.strip(), corr.strip(), diff, SOURCE))
                nb_exos += 1
    c.commit()
    print(f"{nb_recaps} fiches recap et {nb_exos} exercices ajoutés.")


if __name__ == "__main__":
    main()
