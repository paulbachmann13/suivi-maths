"""Remplit la base avec les chapitres/notions de Seconde et quelques exercices de départ.
Ne fait rien si la base contient déjà des exercices."""
import sqlite3

from app import DB_PATH, init_db

PROGRAMME = {
    "Nombres et calculs": ["Pourcentages et évolutions", "Calcul littéral", "Équations", "Inéquations et intervalles"],
    "Fonctions": ["Généralités (image, antécédent)", "Fonctions affines", "Variations et tableaux"],
    "Géométrie": ["Repérage et vecteurs", "Droites (équations)"],
    "Statistiques et probabilités": ["Statistiques (moyenne, médiane, quartiles)", "Probabilités"],
}

# (notion, titre, difficulté, énoncé, correction)
EXOS = [
    ("Pourcentages et évolutions", "Baisse puis hausse", 2,
     "Un article coûte $80$ €. Son prix baisse de $15\\,\\%$, puis augmente de $15\\,\\%$.\n"
     "1. Calculer le prix après la baisse.\n2. Calculer le prix final.\n"
     "3. Le prix final est-il égal au prix initial ? Expliquer.",
     "1. $80\\times(1-0{,}15)=80\\times 0{,}85=68$ €.\n2. $68\\times 1{,}15=78{,}2$ €.\n"
     "3. Non : $0{,}85\\times1{,}15=0{,}9775\\neq 1$. La hausse de $15\\,\\%$ s'applique à un prix plus petit, "
     "donc elle ne compense pas la baisse."),
    ("Calcul littéral", "Développer", 1,
     "Développer et réduire : $A=(2x+3)(x-5)$ et $B=(x+4)^2$.",
     "$A=2x^2-10x+3x-15=2x^2-7x-15$.\n$B=x^2+8x+16$."),
    ("Calcul littéral", "Factoriser", 2,
     "Factoriser : $A=x^2-9$ ; $B=4x^2+12x$ ; $C=(x+1)(x-2)+3(x+1)$.",
     "$A=(x-3)(x+3)$.\n$B=4x(x+3)$.\n$C=(x+1)\\big[(x-2)+3\\big]=(x+1)(x+1)=(x+1)^2$."),
    ("Équations", "Équations du premier degré", 1,
     "Résoudre dans $\\mathbb{R}$ :\n1. $3x-7=2x+5$\n2. $\\dfrac{x}{2}+1=\\dfrac{2x-1}{3}$",
     "1. $3x-2x=5+7$ donc $x=12$.\n"
     "2. On multiplie par $6$ : $3x+6=4x-2$, d'où $x=8$.\n$S=\\{8\\}$."),
    ("Inéquations et intervalles", "Inéquation et intervalle", 2,
     "Résoudre $-2x+3\\le 7$ et donner l'ensemble des solutions sous forme d'intervalle.",
     "$-2x\\le 4$. On divise par $-2$ (négatif) donc le sens change : $x\\ge -2$.\n$S=[-2\\,;+\\infty[$."),
    ("Généralités (image, antécédent)", "Image et antécédents", 1,
     "Soit $g(x)=x^2-4x$.\n1. Calculer $g(0)$ et $g(3)$.\n2. Déterminer les antécédents de $0$ par $g$.",
     "1. $g(0)=0$ ; $g(3)=9-12=-3$.\n2. $x^2-4x=0\\iff x(x-4)=0$, donc $x=0$ ou $x=4$."),
    ("Fonctions affines", "Fonction affine : calculs", 1,
     "Soit $f(x)=2x-3$.\n1. Calculer l'image de $4$.\n2. Quel est l'antécédent de $7$ ?\n"
     "3. Tracer la représentation graphique de $f$.",
     "1. $f(4)=5$.\n2. $2x-3=7\\iff x=5$.\n"
     "3. Droite passant par $(0\\,;-3)$ et $(2\\,;1)$."),
    ("Fonctions affines", "Fonction affine à partir de deux points", 2,
     "Déterminer l'expression de la fonction affine $f$ telle que $f(1)=2$ et $f(3)=8$.",
     "$f(x)=ax+b$ avec $a=\\dfrac{8-2}{3-1}=3$. Puis $3\\times1+b=2$ donc $b=-1$.\n$f(x)=3x-1$."),
    ("Repérage et vecteurs", "Coordonnées de vecteurs", 2,
     "Dans un repère, on donne $A(1\\,;2)$, $B(4\\,;6)$ et $C(-1\\,;0)$.\n"
     "1. Calculer les coordonnées de $\\overrightarrow{AB}$ puis la distance $AB$.\n"
     "2. Déterminer $D$ pour que $ABCD$ soit un parallélogramme.\n3. Calculer les coordonnées du milieu de $[AC]$.",
     "1. $\\overrightarrow{AB}(3\\,;4)$ et $AB=\\sqrt{3^2+4^2}=5$.\n"
     "2. $ABCD$ parallélogramme $\\iff\\overrightarrow{AB}=\\overrightarrow{DC}$, donc $-1-x_D=3$ et $0-y_D=4$ : $D(-4\\,;-4)$.\n"
     "3. Milieu de $[AC]$ : $\\left(\\dfrac{1-1}{2}\\,;\\dfrac{2+0}{2}\\right)=(0\\,;1)$."),
    ("Statistiques (moyenne, médiane, quartiles)", "Série de notes", 1,
     "Notes : $12,\\ 15,\\ 15,\\ 10,\\ 18,\\ 20,\\ 15,\\ 14$.\n"
     "Calculer la moyenne, la médiane, $Q_1$ et $Q_3$.",
     "Série ordonnée : $10,12,14,15,15,15,18,20$ ($n=8$).\nMoyenne : $\\dfrac{119}{8}=14{,}875$.\n"
     "Médiane : $\\dfrac{15+15}{2}=15$.\n$Q_1$ : rang $2$ donc $12$ ; $Q_3$ : rang $6$ donc $15$."),
    ("Probabilités", "Lancer de dé", 2,
     "On lance un dé équilibré à $6$ faces. $A$ : « le nombre est pair » ; $B$ : « le nombre est multiple de $3$ ».\n"
     "Calculer $P(A)$, $P(B)$, $P(A\\cap B)$ puis $P(A\\cup B)$.",
     "$P(A)=\\dfrac12$, $P(B)=\\dfrac13$, $A\\cap B=\\{6\\}$ donc $P(A\\cap B)=\\dfrac16$.\n"
     "$P(A\\cup B)=\\dfrac12+\\dfrac13-\\dfrac16=\\dfrac23$."),
]


def main():
    init_db()
    c = sqlite3.connect(DB_PATH)
    if c.execute("SELECT COUNT(*) FROM exercice").fetchone()[0]:
        print("Base déjà remplie, rien à faire.")
        return
    notion_id = {}
    for i, (chap, notions) in enumerate(PROGRAMME.items(), 1):
        cid = c.execute("INSERT OR IGNORE INTO chapitre (nom, ordre) VALUES (?,?)", (chap, i)).lastrowid \
            or c.execute("SELECT id FROM chapitre WHERE nom=?", (chap,)).fetchone()[0]
        for n in notions:
            c.execute("INSERT OR IGNORE INTO notion (chapitre_id, nom) VALUES (?,?)", (cid, n))
            notion_id[n] = c.execute("SELECT id FROM notion WHERE chapitre_id=? AND nom=?", (cid, n)).fetchone()[0]
    for notion, titre, diff, enonce, corr in EXOS:
        c.execute("INSERT INTO exercice (notion_id, titre, enonce, correction, difficulte, source) VALUES (?,?,?,?,?,?)",
                  (notion_id[notion], titre, enonce, corr, diff, "Claude (programme Seconde)"))
    c.commit()
    print(f"{len(EXOS)} exercices ajoutés.")


if __name__ == "__main__":
    main()
