"""Domaine « Géométrie » (programme de Seconde générale, 2019)."""

DOMAINE = "Géométrie"

CHAPITRES = [
    # ------------------------------------------------------------------ 13
    dict(
        nom="Repérage et distances",
        notions=["Milieu et symétrique", "Distance entre deux points", "Nature d'une figure"],
        recap=r"""## Coordonnées dans un repère
Un repère $(O\,;I,J)$ permet de repérer un point par son abscisse et son ordonnée : $M(x\,;y)$.

## Milieu
> Le milieu $I$ de $[AB]$ a pour coordonnées $I\left(\dfrac{x_A+x_B}{2}\,;\dfrac{y_A+y_B}{2}\right)$.
- Symétrique de $A$ par rapport à $B$ : c'est le point $C$ tel que $B$ soit le milieu de $[AC]$, donc $x_C=2x_B-x_A$ et $y_C=2y_B-y_A$.

## Distance (repère orthonormé)
> $AB=\sqrt{(x_B-x_A)^2+(y_B-y_A)^2}$
- Cela vient du théorème de Pythagore. L'ordre de $A$ et $B$ n'a pas d'importance (les différences sont au carré).

## Nature d'une figure
- **Triangle** : on calcule les trois longueurs. Isocèle (deux côtés égaux), équilatéral (trois égaux), rectangle (réciproque de Pythagore : $AB^2+AC^2=BC^2$ avec $BC$ le plus grand côté).
- **Parallélogramme** : les diagonales ont le même milieu. **Rectangle** : parallélogramme avec diagonales de même longueur. **Losange** : parallélogramme avec deux côtés consécutifs égaux. **Carré** : rectangle et losange.
- **Cercle** de diamètre $[AB]$ : centre le milieu de $[AB]$, rayon $\dfrac{AB}{2}$.
- Pour comparer des distances, comparer plutôt les **carrés** (évite les racines).""",
        exos=[
            ("Milieu et symétrique", "Milieu et symétrique", 1,
             r"""Dans un repère, $A(-2\,;3)$ et $B(4\,;-1)$.
1. Calculer les coordonnées du milieu $I$ de $[AB]$.
2. Calculer les coordonnées du symétrique $C$ de $A$ par rapport à $B$.""",
             r"""1. $I\left(\dfrac{-2+4}2\,;\dfrac{3-1}2\right)=(1\,;1)$.
2. $x_C=2\times4-(-2)=10$ et $y_C=2\times(-1)-3=-5$ : $C(10\,;-5)$. Vérification : le milieu de $[AC]$ est $(4\,;-1)=B$."""),
            ("Distance entre deux points", "Calculer des distances", 1,
             r"""Dans un repère orthonormé, $A(1\,;2)$, $B(4\,;6)$ et $C(-1\,;0)$. Calculer $AB$, $BC$ et $AC$.""",
             r"""$AB=\sqrt{3^2+4^2}=5$ ; $BC=\sqrt{(-5)^2+(-6)^2}=\sqrt{61}$ ; $AC=\sqrt{(-2)^2+(-2)^2}=\sqrt8=2\sqrt2$."""),
            ("Nature d'une figure", "Nature d'un triangle", 2,
             r"""Dans un repère orthonormé, $A(0\,;0)$, $B(4\,;2)$ et $C(-1\,;2)$. Quelle est la nature du triangle $ABC$ ?""",
             r"""$AB^2=16+4=20$ ; $AC^2=1+4=5$ ; $BC^2=25+0=25$.
$AB^2+AC^2=25=BC^2$ : d'après la réciproque du théorème de Pythagore, $ABC$ est rectangle en $A$. Il n'est pas isocèle ($20\ne5$)."""),
            ("Nature d'une figure", "Nature d'un quadrilatère", 3,
             r"""Dans un repère orthonormé, $A(-3\,;-1)$, $B(2\,;0)$, $C(4\,;3)$ et $D(-1\,;2)$.
Montrer que $ABCD$ est un parallélogramme. Est-ce un rectangle ? un losange ?""",
             r"""Milieu de $[AC]$ : $\left(\dfrac12\,;1\right)$ ; milieu de $[BD]$ : $\left(\dfrac12\,;1\right)$. Mêmes milieux : $ABCD$ est un parallélogramme.
$AC^2=49+16=65$ ; $BD^2=9+4=13$ : diagonales de longueurs différentes, pas un rectangle.
$AB^2=25+1=26$ ; $BC^2=4+9=13$ : côtés consécutifs différents, pas un losange."""),
            ("Distance entre deux points", "Cercle de diamètre donné", 3,
             r"""Dans un repère orthonormé, $A(-1\,;2)$ et $B(5\,;-2)$. Soit $\mathcal{C}$ le cercle de diamètre $[AB]$.
1. Déterminer son centre et son rayon.
2. Les points $C(4\,;1)$ et $D(5\,;2)$ appartiennent-ils à $\mathcal{C}$ ?""",
             r"""1. Centre $\Omega(2\,;0)$ ; $AB^2=36+16=52$ donc $AB=2\sqrt{13}$ et rayon $\sqrt{13}$.
2. $\Omega C^2=4+1=5\neq13$ : $C\notin\mathcal{C}$. $\Omega D^2=9+4=13$ : $D\in\mathcal{C}$."""),
            ("Distance entre deux points", "Point équidistant de deux points", 3,
             r"""Dans un repère orthonormé, $A(1\,;3)$ et $B(5\,;1)$. Déterminer le point $M$ de l'axe des abscisses tel que $MA=MB$.""",
             r"""$M(x\,;0)$. $MA^2=(x-1)^2+9$ et $MB^2=(x-5)^2+1$.
$MA=MB\iff x^2-2x+10=x^2-10x+26\iff8x=16\iff x=2$. $M(2\,;0)$ ($MA^2=MB^2=10$)."""),
        ],
    ),
    # ------------------------------------------------------------------ 14
    dict(
        nom="Vecteurs",
        notions=["Coordonnées et opérations", "Relation de Chasles et parallélogramme", "Colinéarité"],
        recap=r"""## Vecteur
Un vecteur $\vec u$ est défini par une direction, un sens et une longueur (la **norme** $\|\vec u\|$). $\overrightarrow{AB}$ est le vecteur de translation qui amène $A$ en $B$.
> $\overrightarrow{AB}=\overrightarrow{CD}\iff ABDC$ est un parallélogramme (éventuellement aplati).

## Coordonnées
> $\overrightarrow{AB}\begin{pmatrix}x_B-x_A\\y_B-y_A\end{pmatrix}$ ; $\|\vec u\|=\sqrt{x^2+y^2}$ (repère orthonormé)
- $\vec u+\vec v$ : on additionne les coordonnées. $k\vec u$ : on multiplie chaque coordonnée par $k$.
- Deux vecteurs sont égaux si et seulement si leurs coordonnées sont égales.

## Relation de Chasles
> $\overrightarrow{AB}+\overrightarrow{BC}=\overrightarrow{AC}$ ; $\overrightarrow{AB}=-\overrightarrow{BA}$ ; $\overrightarrow{AA}=\vec0$
- Si $I$ est le milieu de $[AB]$ : $\overrightarrow{AI}=\overrightarrow{IB}$ et $\overrightarrow{IA}+\overrightarrow{IB}=\vec0$.

## Colinéarité
> $\vec u(x\,;y)$ et $\vec v(x'\,;y')$ sont **colinéaires** $\iff xy'-x'y=0$ (le déterminant est nul).
- Colinéaires : l'un est un multiple de l'autre ($\vec v=k\vec u$).
- $A,B,C$ sont **alignés** $\iff\overrightarrow{AB}$ et $\overrightarrow{AC}$ sont colinéaires.
- Les droites $(AB)$ et $(CD)$ sont **parallèles** $\iff\overrightarrow{AB}$ et $\overrightarrow{CD}$ sont colinéaires.""",
        exos=[
            ("Coordonnées et opérations", "Coordonnées de vecteurs", 2,
             r"""Dans un repère, $A(1\,;2)$, $B(4\,;6)$ et $C(-1\,;0)$.
1. Calculer les coordonnées de $\overrightarrow{AB}$ puis la distance $AB$ (repère orthonormé).
2. Déterminer $D$ pour que $ABCD$ soit un parallélogramme.
3. Calculer les coordonnées du milieu de $[AC]$.""",
             r"""1. $\overrightarrow{AB}(3\,;4)$ et $AB=\sqrt{9+16}=5$.
2. $ABCD$ parallélogramme $\iff\overrightarrow{AB}=\overrightarrow{DC}$ : $-1-x_D=3$ et $0-y_D=4$, donc $D(-4\,;-4)$.
3. Milieu de $[AC]$ : $\left(\dfrac{1-1}2\,;\dfrac{2+0}2\right)=(0\,;1)$."""),
            ("Coordonnées et opérations", "Opérations sur les vecteurs", 1,
             r"""Soit $\vec u(3\,;-2)$ et $\vec v(-1\,;4)$. Calculer les coordonnées de $\vec u+\vec v$ et $2\vec u-3\vec v$, puis la norme de $\vec u$ (repère orthonormé).""",
             r"""$\vec u+\vec v(2\,;2)$ ; $2\vec u-3\vec v(6+3\,;-4-12)=(9\,;-16)$ ; $\|\vec u\|=\sqrt{9+4}=\sqrt{13}$."""),
            ("Relation de Chasles et parallélogramme", "Simplifier avec Chasles", 2,
             r"""Simplifier : $\vec a=\overrightarrow{AB}+\overrightarrow{CD}+\overrightarrow{BC}+\overrightarrow{DA}$ ; $\vec b=\overrightarrow{AB}-\overrightarrow{CB}+\overrightarrow{CD}$ ; $\vec c=\overrightarrow{BM}+\overrightarrow{MA}$.""",
             r"""$\vec a=\overrightarrow{AB}+\overrightarrow{BC}+\overrightarrow{CD}+\overrightarrow{DA}=\overrightarrow{AA}=\vec0$.
$\vec b=\overrightarrow{AB}+\overrightarrow{BC}+\overrightarrow{CD}=\overrightarrow{AD}$ (car $-\overrightarrow{CB}=\overrightarrow{BC}$).
$\vec c=\overrightarrow{BA}$."""),
            ("Colinéarité", "Colinéarité de deux vecteurs", 2,
             r"""1. $\vec u(2\,;-3)$ et $\vec v(-4\,;6)$ sont-ils colinéaires ? $\vec w(1\,;5)$ et $\vec z(2\,;9)$ ?
2. Déterminer $m$ pour que $\vec u(m\,;4)$ et $\vec v(3\,;-2)$ soient colinéaires.""",
             r"""1. $2\times6-(-4)(-3)=12-12=0$ : colinéaires ($\vec v=-2\vec u$). $1\times9-2\times5=-1\neq0$ : non colinéaires.
2. $m\times(-2)-4\times3=0\iff m=-6$."""),
            ("Colinéarité", "Points alignés", 2,
             r"""Les points $A(1\,;1)$, $B(3\,;2)$ et $C(7\,;4)$ sont-ils alignés ? Et $A$, $B$ et $D(5\,;4)$ ?""",
             r"""$\overrightarrow{AB}(2\,;1)$, $\overrightarrow{AC}(6\,;3)$ : $2\times3-1\times6=0$, alignés.
$\overrightarrow{AD}(4\,;3)$ : $2\times3-1\times4=2\neq0$, non alignés."""),
            ("Relation de Chasles et parallélogramme", "Compléter un parallélogramme", 2,
             r"""Dans un repère, $A(-1\,;0)$, $B(2\,;1)$ et $C(3\,;4)$. Déterminer $D$ tel que $ABCD$ soit un parallélogramme et vérifier avec les milieux des diagonales.""",
             r"""$\overrightarrow{AB}(3\,;1)=\overrightarrow{DC}(3-x_D\,;4-y_D)$ : $D(0\,;3)$.
Milieu de $[AC]$ : $(1\,;2)$ ; milieu de $[BD]$ : $(1\,;2)$. ✔"""),
            ("Colinéarité", "Droites parallèles", 2,
             r"""Dans un repère, $A(-2\,;1)$, $B(1\,;3)$, $C(0\,;-2)$ et $D(6\,;2)$. Les droites $(AB)$ et $(CD)$ sont-elles parallèles ?""",
             r"""$\overrightarrow{AB}(3\,;2)$ et $\overrightarrow{CD}(6\,;4)$ : $3\times4-2\times6=0$, colinéaires, donc $(AB)\parallel(CD)$."""),
            ("Relation de Chasles et parallélogramme", "Démonstration vectorielle", 3,
             r"""Soit $ABC$ un triangle et $I$ le milieu de $[BC]$. Montrer que $\overrightarrow{AB}+\overrightarrow{AC}=2\overrightarrow{AI}$.""",
             r"""$\overrightarrow{AB}=\overrightarrow{AI}+\overrightarrow{IB}$ et $\overrightarrow{AC}=\overrightarrow{AI}+\overrightarrow{IC}$.
En additionnant : $\overrightarrow{AB}+\overrightarrow{AC}=2\overrightarrow{AI}+(\overrightarrow{IB}+\overrightarrow{IC})=2\overrightarrow{AI}$ car $I$ est le milieu de $[BC]$ donc $\overrightarrow{IB}+\overrightarrow{IC}=\vec0$."""),
        ],
    ),
    # ------------------------------------------------------------------ 15
    dict(
        nom="Droites et systèmes",
        notions=["Équations de droites", "Droites parallèles et sécantes", "Systèmes d'équations"],
        recap=r"""## Équation réduite
> Une droite non verticale a une équation de la forme $y=mx+p$ : $m$ est le **coefficient directeur**, $p$ l'**ordonnée à l'origine**.
- $m=\dfrac{y_B-y_A}{x_B-x_A}$ pour deux points $A,B$ de la droite avec $x_A\ne x_B$.
- Une droite verticale a pour équation $x=c$ (pas de coefficient directeur).
- $M(x_0\,;y_0)$ est sur la droite $\iff y_0=mx_0+p$.

## Équation cartésienne et vecteur directeur
> $ax+by+c=0$ (avec $(a\,;b)\ne(0\,;0)$) est une **équation cartésienne**. Le vecteur $\vec u(-b\,;a)$ est un **vecteur directeur**.

## Positions relatives
- Deux droites sont **parallèles** si elles ont le même coefficient directeur (ou des vecteurs directeurs colinéaires). Sinon elles sont **sécantes** en un point.

## Systèmes de deux équations
Résoudre un système, c'est trouver le couple $(x\,;y)$ vérifiant les deux équations. Géométriquement : l'intersection de deux droites.
- **Substitution** : exprimer une inconnue en fonction de l'autre.
- **Combinaison** : multiplier les équations pour éliminer une inconnue, puis additionner ou soustraire.
- Cas particuliers : droites parallèles distinctes, aucune solution ; droites confondues, une infinité.""",
        exos=[
            ("Équations de droites", "Équation réduite par deux points", 2,
             r"""Déterminer l'équation réduite de la droite $(AB)$ :
1. $A(1\,;2)$ et $B(3\,;8)$.
2. $A(-2\,;1)$ et $B(4\,;-2)$. Le point $C(6\,;-3)$ appartient-il à cette droite ?""",
             r"""1. $m=\dfrac{8-2}{3-1}=3$ ; $2=3\times1+p$ donc $p=-1$ : $y=3x-1$.
2. $m=\dfrac{-2-1}{4+2}=-\dfrac12$ ; $1=-\dfrac12\times(-2)+p$ donc $p=0$ : $y=-\dfrac12x$. Pour $x=6$ : $y=-3$ : $C$ appartient à la droite."""),
            ("Droites parallèles et sécantes", "Droite parallèle passant par un point", 2,
             r"""Soit $d$ la droite d'équation $y=2x-5$. Déterminer l'équation de la parallèle à $d$ passant par $A(1\,;4)$.""",
             r"""Même coefficient directeur $2$ : $y=2x+p$. $4=2\times1+p$ donc $p=2$ : $y=2x+2$."""),
            ("Équations de droites", "Droite verticale et équation cartésienne", 2,
             r"""1. Déterminer l'équation de la droite passant par $A(2\,;5)$ et $B(2\,;-1)$.
2. Déterminer une équation cartésienne de la droite passant par $(0\,;4)$ et $(3\,;0)$.""",
             r"""1. Même abscisse : droite verticale $x=2$.
2. $m=\dfrac{0-4}{3-0}=-\dfrac43$ : $y=-\dfrac43x+4$, soit $4x+3y-12=0$."""),
            ("Systèmes d'équations", "Résoudre un système", 2,
             r"""Résoudre : 1. $\begin{cases}y=2x-1\\3x+y=9\end{cases}$   2. $\begin{cases}3x-2y=4\\x+4y=6\end{cases}$""",
             r"""1. $3x+2x-1=9\iff x=2$, $y=3$ : $S=\{(2\,;3)\}$.
2. $x=6-4y$ : $18-12y-2y=4\iff y=1$, $x=2$ : $S=\{(2\,;1)\}$. Vérification : $3\times2-2=4$ ✔ ; $2+4=6$ ✔."""),
            ("Droites parallèles et sécantes", "Droites sécantes ou parallèles ?", 2,
             r"""1. Déterminer l'intersection de $d_1:y=-x+5$ et $d_2:y=2x-1$.
2. Les droites $d:y=3x+1$ et $d':6x-2y+5=0$ sont-elles parallèles ?""",
             r"""1. $-x+5=2x-1\iff x=2$, $y=3$ : intersection $(2\,;3)$.
2. $d'$ : $y=3x+\dfrac52$. Même coefficient directeur $3$, ordonnées à l'origine différentes : parallèles distinctes."""),
            ("Systèmes d'équations", "Problème : la boulangerie", 2,
             r"""Pour $3$ croissants et $2$ pains au chocolat, on paie $6{,}10$ €. Pour $2$ croissants et $4$ pains au chocolat, on paie $7{,}40$ €.
Quel est le prix d'un croissant ? d'un pain au chocolat ?""",
             r"""$\begin{cases}3c+2p=6{,}10\\2c+4p=7{,}40\end{cases}$. On double la première : $6c+4p=12{,}20$. On soustrait la seconde : $4c=4{,}80$ donc $c=1{,}20$ €, puis $p=\dfrac{6{,}10-3{,}60}{2}=1{,}25$ €."""),
            ("Équations de droites", "Équation cartésienne et vecteur directeur", 3,
             r"""Déterminer une équation cartésienne de la droite passant par $A(1\,;-2)$ et de vecteur directeur $\vec u(2\,;3)$.""",
             r"""Équation de la forme $ax+by+c=0$ avec $\vec u(-b\,;a)=(2\,;3)$ : $b=-2$ et $a=3$ : $3x-2y+c=0$.
$A$ appartient à la droite : $3\times1-2\times(-2)+c=0\iff c=-7$. Équation : $3x-2y-7=0$."""),
        ],
    ),
    # ------------------------------------------------------------------ 16
    dict(
        nom="Géométrie plane et espace",
        notions=["Pythagore et Thalès", "Trigonométrie du triangle rectangle", "Aires et volumes", "Projeté orthogonal"],
        recap=r"""## Théorème de Pythagore
> Dans un triangle $ABC$ rectangle en $A$ : $BC^2=AB^2+AC^2$. **Réciproque** : si $BC^2=AB^2+AC^2$, alors le triangle est rectangle en $A$.

## Théorème de Thalès
> Si $M\in(AB)$, $N\in(AC)$ et $(MN)\parallel(BC)$ : $\dfrac{AM}{AB}=\dfrac{AN}{AC}=\dfrac{MN}{BC}$.
- **Réciproque** : si $\dfrac{AM}{AB}=\dfrac{AN}{AC}$ avec les points alignés dans le même ordre, alors $(MN)\parallel(BC)$.

## Trigonométrie (triangle rectangle)
> $\cos\widehat{B}=\dfrac{\text{côté adjacent}}{\text{hypoténuse}}$ ; $\sin\widehat{B}=\dfrac{\text{côté opposé}}{\text{hypoténuse}}$ ; $\tan\widehat{B}=\dfrac{\text{côté opposé}}{\text{côté adjacent}}$
- Angles remarquables : $\sin30°=\dfrac12$, $\cos30°=\dfrac{\sqrt3}2$, $\sin45°=\cos45°=\dfrac{\sqrt2}2$, $\sin60°=\dfrac{\sqrt3}2$, $\cos60°=\dfrac12$.

## Aires et volumes
- Disque : $\pi r^2$ (périmètre $2\pi r$). Triangle : $\dfrac{b\times h}2$. Trapèze : $\dfrac{(B+b)h}2$.
- Cylindre : $\pi r^2h$. Cône et pyramide : $\dfrac13\times\text{aire de base}\times h$. Boule : $\dfrac43\pi r^3$ (aire de la sphère $4\pi r^2$).
- Agrandissement/réduction de rapport $k$ : longueurs $\times k$, aires $\times k^2$, volumes $\times k^3$.

## Projeté orthogonal
> Le projeté orthogonal $H$ d'un point $M$ sur une droite $d$ est le point de $d$ tel que $(MH)\perp d$. C'est le point de $d$ le plus proche de $M$.""",
        exos=[
            ("Pythagore et Thalès", "Pythagore", 1,
             r"""1. $ABC$ est rectangle en $A$ avec $AB=5$ et $AC=12$. Calculer $BC$.
2. Un triangle a pour côtés $7$, $24$ et $25$. Est-il rectangle ?""",
             r"""1. $BC^2=25+144=169$, $BC=13$.
2. $7^2+24^2=49+576=625=25^2$ : oui, d'après la réciproque de Pythagore (rectangle, hypoténuse $25$)."""),
            ("Pythagore et Thalès", "Théorème de Thalès", 2,
             r"""Dans le triangle $ABC$, $D\in[AB]$ et $E\in[AC]$ avec $(DE)\parallel(BC)$. On donne $AD=3$, $AB=7{,}5$, $AE=4$ et $BC=9$ (en cm). Calculer $AC$ et $DE$.""",
             r"""D'après Thalès : $\dfrac{AD}{AB}=\dfrac{AE}{AC}=\dfrac{DE}{BC}$, avec $\dfrac{AD}{AB}=\dfrac{3}{7{,}5}=0{,}4$.
$AC=\dfrac{4}{0{,}4}=10$ cm ; $DE=0{,}4\times9=3{,}6$ cm."""),
            ("Pythagore et Thalès", "Réciproque de Thalès", 2,
             r"""$M\in[AB]$ et $N\in[AC]$. On donne $AM=4$, $AB=10$, $AN=6$ et $AC=15$. Les droites $(MN)$ et $(BC)$ sont-elles parallèles ? Et si $AN=7$ ?""",
             r"""$\dfrac{AM}{AB}=0{,}4$ et $\dfrac{AN}{AC}=\dfrac6{15}=0{,}4$ : égaux, points alignés dans le même ordre : $(MN)\parallel(BC)$.
Avec $AN=7$ : $\dfrac7{15}\ne0{,}4$ : les droites ne sont pas parallèles."""),
            ("Trigonométrie du triangle rectangle", "Calculs avec sinus, cosinus et tangente", 2,
             r"""$ABC$ est rectangle en $A$.
1. $AB=6$ cm et $\widehat{C}=35°$ : calculer $BC$ et $AC$ (arrondir au dixième).
2. $AB=6$ et $AC=8$ : calculer l'angle $\widehat{B}$ au degré près.""",
             r"""1. $\sin\widehat C=\dfrac{AB}{BC}$ donc $BC=\dfrac6{\sin35°}\approx10{,}5$ cm. $\tan\widehat C=\dfrac{AB}{AC}$ donc $AC=\dfrac6{\tan35°}\approx8{,}6$ cm.
2. $\tan\widehat B=\dfrac{AC}{AB}=\dfrac86$ donc $\widehat B\approx53°$."""),
            ("Trigonométrie du triangle rectangle", "Valeurs remarquables", 3,
             r"""Soit $ABC$ un triangle équilatéral de côté $2$ et $H$ le pied de la hauteur issue de $A$.
1. Calculer $AH$ et l'aire de $ABC$.
2. En déduire $\sin60°$, $\cos60°$ et $\tan60°$.""",
             r"""1. $H$ est le milieu de $[BC]$, $BH=1$. $AH^2=4-1=3$, $AH=\sqrt3$. Aire $=\dfrac{2\times\sqrt3}2=\sqrt3$.
2. Dans $ABH$ rectangle en $H$ : $\sin60°=\dfrac{AH}{AB}=\dfrac{\sqrt3}2$ ; $\cos60°=\dfrac{BH}{AB}=\dfrac12$ ; $\tan60°=\sqrt3$."""),
            ("Aires et volumes", "Volumes usuels", 2,
             r"""Calculer le volume exact puis arrondi au dixième de :
1. un cylindre de rayon $4$ cm et de hauteur $10$ cm ;
2. un cône de même base et de même hauteur ;
3. une boule de rayon $3$ cm.""",
             r"""1. $\pi\times16\times10=160\pi\approx502{,}7$ cm$^3$.
2. $\dfrac13\times160\pi=\dfrac{160\pi}3\approx167{,}6$ cm$^3$.
3. $\dfrac43\pi\times27=36\pi\approx113{,}1$ cm$^3$."""),
            ("Aires et volumes", "Agrandissement et réduction", 2,
             r"""Un solide de volume $40$ cm$^3$ a une face d'aire $12$ cm$^2$. On l'agrandit avec un rapport $k=1{,}5$.
1. Quel est le nouveau volume ? la nouvelle aire de la face ?
2. Avec un rapport de réduction $k=0{,}5$, par combien le volume est-il multiplié ?""",
             r"""1. Volume : $40\times1{,}5^3=40\times3{,}375=135$ cm$^3$. Aire : $12\times1{,}5^2=27$ cm$^2$.
2. $0{,}5^3=\dfrac18$ : le volume est divisé par $8$."""),
            ("Projeté orthogonal", "Projeté orthogonal", 2,
             r"""1. Dans un repère orthonormé, donner le projeté orthogonal de $M(3\,;4)$ sur la droite d'équation $y=1$, puis la distance de $M$ à cette droite.
2. $ABC$ est un triangle, $H$ le projeté orthogonal de $A$ sur $(BC)$, avec $AB=13$, $BH=5$ et $AC=15$ ($H\in[BC]$). Calculer $AH$, $HC$, $BC$ et l'aire de $ABC$.""",
             r"""1. $H(3\,;1)$ ; distance $MH=3$.
2. $AH^2=13^2-5^2=144$, $AH=12$. $HC^2=15^2-12^2=81$, $HC=9$. $BC=5+9=14$. Aire $=\dfrac{14\times12}2=84$."""),
        ],
    ),
]
