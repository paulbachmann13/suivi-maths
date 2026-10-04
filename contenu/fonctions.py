"""Domaine « Fonctions » (programme de Seconde générale, 2019)."""

DOMAINE = "Fonctions"

CHAPITRES = [
    # ------------------------------------------------------------------ 8
    dict(
        nom="Généralités sur les fonctions",
        notions=["Image et antécédent", "Ensemble de définition", "Courbe représentative"],
        recap=r"""## Vocabulaire
> Une fonction $f$ associe à chaque réel $x$ de son **ensemble de définition** $D_f$ un unique réel noté $f(x)$.
- $f(x)$ est l'**image** de $x$. Si $f(a)=b$, alors $a$ est **un antécédent** de $b$ (il peut y en avoir plusieurs, ou aucun).
- Ensemble de définition : on exclut les valeurs qui annulent un dénominateur ($\dfrac1{x-2}$ : $x\ne2$) et celles qui rendent négatif ce qu'il y a sous une racine ($\sqrt{x-3}$ : $x\ge3$).

## Courbe représentative
> La courbe $\mathcal{C}_f$ est l'ensemble des points $M(x\,;f(x))$ avec $x\in D_f$. Un point $M(a\,;b)$ est sur $\mathcal{C}_f$ si et seulement si $f(a)=b$.
- **Lecture de l'image** de $a$ : on part de $a$ sur l'axe des abscisses, on monte (ou descend) jusqu'à la courbe, on lit l'ordonnée.
- **Lecture des antécédents** de $b$ : on part de $b$ sur l'axe des ordonnées, on trace l'horizontale $y=b$, on lit les abscisses des points d'intersection avec la courbe.
- Pour tracer une courbe : tableau de valeurs, placer les points, les relier avec soin.

## Méthodes
- Calculer une image : on remplace $x$.
- Trouver les antécédents de $b$ : on résout l'équation $f(x)=b$.""",
        exos=[
            ("Image et antécédent", "Image et antécédents", 1,
             r"""Soit $g(x)=x^2-4x$.
1. Calculer $g(0)$ et $g(3)$.
2. Déterminer les antécédents de $0$ par $g$.""",
             r"""1. $g(0)=0$ ; $g(3)=9-12=-3$.
2. $x^2-4x=0\iff x(x-4)=0$, donc $x=0$ ou $x=4$."""),
            ("Image et antécédent", "Calculs d'images avec un quotient", 2,
             r"""Soit $f(x)=\dfrac{2x-1}{x+3}$.
1. Quelle est la valeur interdite ? En déduire l'ensemble de définition.
2. Calculer $f(0)$, $f(1)$ et $f(-1)$.
3. Déterminer l'antécédent de $2$.""",
             r"""1. $x+3=0\iff x=-3$ : $D_f=\mathbb{R}\setminus\{-3\}$.
2. $f(0)=-\dfrac13$ ; $f(1)=\dfrac14$ ; $f(-1)=\dfrac{-3}{2}=-\dfrac32$.
3. $\dfrac{2x-1}{x+3}=2\iff2x-1=2x+6\iff-1=6$ : impossible, $2$ n'a pas d'antécédent."""),
            ("Ensemble de définition", "Ensemble de définition", 2,
             r"""Déterminer l'ensemble de définition de :
$f(x)=\sqrt{2x-6}$ ; $g(x)=\dfrac1{x^2-4}$ ; $h(x)=\dfrac{\sqrt{x+1}}{x-2}$.""",
             r"""$f$ : $2x-6\ge0\iff x\ge3$, $D_f=[3\,;+\infty[$.
$g$ : $x^2-4=0\iff x=\pm2$, $D_g=\mathbb{R}\setminus\{-2\,;2\}$.
$h$ : il faut $x+1\ge0$ et $x\ne2$ : $D_h=[-1\,;2[\,\cup\,]2\,;+\infty[$."""),
            ("Courbe représentative", "Un point est-il sur la courbe ?", 1,
             r"""Soit $f(x)=-x^2+2x+3$. Les points $A(2\,;3)$, $B(-1\,;0)$ et $C(3\,;-1)$ appartiennent-ils à la courbe de $f$ ?
Donner les coordonnées du point de la courbe d'abscisse $1$.""",
             r"""$f(2)=-4+4+3=3$ : $A\in\mathcal{C}_f$. $f(-1)=-1-2+3=0$ : $B\in\mathcal{C}_f$. $f(3)=-9+6+3=0\neq-1$ : $C\notin\mathcal{C}_f$.
$f(1)=-1+2+3=4$ : le point est $(1\,;4)$."""),
            ("Courbe représentative", "Tableau de valeurs et tracé", 1,
             r"""Soit $f(x)=x^2-2x-1$ définie sur $[-2\,;4]$.
Compléter un tableau de valeurs pour $x=-2,-1,0,1,2,3,4$, puis tracer la courbe. Quel semble être le minimum de $f$ ?""",
             r"""$f(-2)=7$ ; $f(-1)=2$ ; $f(0)=-1$ ; $f(1)=-2$ ; $f(2)=-1$ ; $f(3)=2$ ; $f(4)=7$.
La courbe est une parabole symétrique par rapport à la droite $x=1$. Le minimum semble être $-2$, atteint en $x=1$."""),
            ("Image et antécédent", "Aire d'un rectangle de périmètre fixé", 3,
             r"""Un rectangle $ABCD$ a pour périmètre $20$ cm. On pose $AB=x$.
1. Exprimer $BC$ en fonction de $x$. Quel est l'ensemble de définition de l'aire $A(x)$ ?
2. Montrer que $A(x)=x(10-x)$. Calculer $A(3)$.
3. Déterminer les antécédents de $21$ par $A$.""",
             r"""1. Demi-périmètre $10$ donc $BC=10-x$ ; $x\in]0\,;10[$ (ou $[0\,;10]$).
2. $A(x)=x(10-x)$ ; $A(3)=3\times7=21$.
3. $x(10-x)=21\iff x^2-10x+21=0\iff(x-3)(x-7)=0$ : $x=3$ ou $x=7$ (le rectangle $3\times7$ ou $7\times3$)."""),
        ],
    ),
    # ------------------------------------------------------------------ 9
    dict(
        nom="Variations et extremums",
        notions=["Sens de variation", "Tableau de variations", "Extremums"],
        recap=r"""## Sens de variation
Soit $f$ définie sur un intervalle $I$.
> $f$ est **croissante** sur $I$ si, pour tous $a<b$ dans $I$, $f(a)\le f(b)$ (elle conserve l'ordre).
> $f$ est **décroissante** sur $I$ si, pour tous $a<b$ dans $I$, $f(a)\ge f(b)$ (elle inverse l'ordre).
- Si $f$ est croissante, sa courbe « monte » ; si elle est décroissante, la courbe « descend ».

## Tableau de variations
Une flèche montante ($\nearrow$) pour une fonction croissante, descendante ($\searrow$) pour une fonction décroissante, avec les valeurs de $f$ aux extrémités des flèches.
- Pour comparer deux images, on regarde si les deux nombres sont dans un même intervalle où $f$ est monotone.

## Extremums
> $f$ admet un **maximum** $M$ sur $I$ atteint en $a$ si $f(x)\le M$ pour tout $x\in I$ et $f(a)=M$. Même idée à l'envers pour un **minimum**.
- Un extremum est une valeur de $f(x)$ (une ordonnée) et non la valeur de $x$ où il est atteint.
- Astuce : $(x-a)^2\ge0$, donc $(x-a)^2+k\ge k$ : minimum $k$ atteint en $x=a$.""",
        exos=[
            ("Tableau de variations", "Lire un tableau de variations", 2,
             r"""Une fonction $f$ est définie sur $[-4\,;5]$ avec : $f(-4)=1$, $f(-1)=4$, $f(2)=-3$, $f(5)=2$. Elle est croissante sur $[-4\,;-1]$, décroissante sur $[-1\,;2]$, croissante sur $[2\,;5]$.
1. Dresser le tableau de variations.
2. Quels sont le maximum et le minimum de $f$ ? En quelles valeurs sont-ils atteints ?
3. Comparer $f(0)$ et $f(1)$, puis $f(3)$ et $f(4)$.
4. Combien l'équation $f(x)=0$ a-t-elle de solutions ? Et $f(x)=5$ ?""",
             r"""2. Maximum $4$ atteint en $x=-1$ ; minimum $-3$ atteint en $x=2$.
3. $0<1$ dans $[-1\,;2]$ où $f$ décroît : $f(0)>f(1)$. $3<4$ dans $[2\,;5]$ où $f$ croît : $f(3)<f(4)$.
4. Sur $[-4\,;-1]$ : $f$ va de $1$ à $4$, jamais $0$. Sur $[-1\,;2]$ : de $4$ à $-3$, une solution. Sur $[2\,;5]$ : de $-3$ à $2$, une solution. Donc $2$ solutions. $f(x)=5$ : le maximum est $4$, aucune solution."""),
            ("Tableau de variations", "Dresser un tableau", 1,
             r"""Une fonction $g$ est définie sur $[-2\,;6]$, croissante sur $[-2\,;1]$, décroissante sur $[1\,;6]$, avec $g(-2)=-1$, $g(1)=3$, $g(6)=0$.
1. Dresser son tableau de variations.
2. Donner ses extremums.
3. Comparer $g(2)$ et $g(5)$.""",
             r"""1. $g$ passe de $-1$ en $x=-2$ à $3$ en $x=1$ ($\nearrow$) puis à $0$ en $x=6$ ($\searrow$).
2. Maximum $3$ (en $x=1$) ; minimum $-1$ (en $x=-2$).
3. $2<5$ dans $[1\,;6]$ où $g$ décroît : $g(2)>g(5)$."""),
            ("Sens de variation", "Comparer des images", 2,
             r"""Dans chaque cas, comparer les images ou dire si c'est impossible :
1. $f$ croissante sur $[0\,;5]$ : $f(1)$ et $f(4)$.
2. $g$ décroissante sur $\mathbb{R}$ : $g(-2)$ et $g(3)$.
3. $h$ croissante sur $[-3\,;2]$ et décroissante sur $[2\,;6]$ : $h(0)$ et $h(1)$ ; $h(3)$ et $h(5)$ ; $h(1)$ et $h(5)$.""",
             r"""1. $f(1)<f(4)$.  2. $g(-2)>g(3)$.
3. $h(0)<h(1)$ (même intervalle de croissance) ; $h(3)>h(5)$ (décroissance sur $[2\,;6]$) ; $h(1)$ et $h(5)$ sont dans des intervalles différents : on ne peut pas conclure avec ces seules informations."""),
            ("Extremums", "Extremums par un carré", 2,
             r"""Déterminer l'extremum de chaque fonction et la valeur de $x$ où il est atteint :
$f(x)=(x-2)^2+1$ ; $g(x)=5-(x+1)^2$ ; $h(x)=x^2-6x+5$ (on pourra écrire $h(x)=(x-3)^2-4$).""",
             r"""$f(x)\ge1$ car $(x-2)^2\ge0$ : minimum $1$ en $x=2$.
$g(x)\le5$ car $(x+1)^2\ge0$ : maximum $5$ en $x=-1$.
$h(x)=(x-3)^2-4\ge-4$ : minimum $-4$ en $x=3$."""),
            ("Extremums", "Aire maximale", 3,
             r"""Reprenons $A(x)=x(10-x)$ sur $[0\,;10]$ (aire d'un rectangle de périmètre $20$ cm).
1. Montrer que $A(x)=25-(x-5)^2$.
2. En déduire la valeur maximale de l'aire et les dimensions du rectangle correspondant.""",
             r"""1. $25-(x-5)^2=25-x^2+10x-25=10x-x^2=x(10-x)$.
2. $(x-5)^2\ge0$ donc $A(x)\le25$, avec égalité pour $x=5$. L'aire maximale est $25$ cm$^2$ : c'est un carré de côté $5$ cm."""),
            ("Sens de variation", "Démontrer un sens de variation", 3,
             r"""1. Démontrer que $f(x)=3x+2$ est croissante sur $\mathbb{R}$.
2. Démontrer que la fonction carré est croissante sur $[0\,;+\infty[$.""",
             r"""1. Soit $a<b$. $f(b)-f(a)=3(b-a)>0$, donc $f(a)<f(b)$.
2. Soit $0\le a<b$. $b^2-a^2=(b-a)(b+a)$. Or $b-a>0$ et $b+a>0$ (car $b>a\ge0$), donc $b^2-a^2>0$ : $a^2<b^2$."""),
        ],
    ),
    # ------------------------------------------------------------------ 10
    dict(
        nom="Fonctions de référence",
        notions=["Fonctions carré et cube", "Fonction inverse", "Fonction racine carrée"],
        recap=r"""## Fonction carré : $x\mapsto x^2$
- Définie sur $\mathbb{R}$, **décroissante** sur $]-\infty\,;0]$, **croissante** sur $[0\,;+\infty[$, minimum $0$ en $0$.
- Courbe : une parabole symétrique par rapport à l'axe des ordonnées.
> $x^2=a$ : $a>0$ deux solutions $\pm\sqrt a$ ; $a=0$ une solution ; $a<0$ aucune.

## Fonction cube : $x\mapsto x^3$
- Définie sur $\mathbb{R}$, **croissante** sur $\mathbb{R}$. Courbe symétrique par rapport à l'origine.

## Fonction inverse : $x\mapsto\dfrac1x$
- Définie sur $\mathbb{R}^*$, **décroissante** sur $]-\infty\,;0[$ et sur $]0\,;+\infty[$ (mais pas sur $\mathbb{R}^*$ tout entier).
- Courbe : une hyperbole. $\dfrac1x>0\iff x>0$.

## Fonction racine carrée : $x\mapsto\sqrt x$
- Définie sur $[0\,;+\infty[$, **croissante**, minimum $0$ en $0$.

## Positions relatives
> Sur $]0\,;1[$ : $x^3<x^2<x<\sqrt x$. Sur $]1\,;+\infty[$ : $\sqrt x<x<x^2<x^3$.
- Une fonction croissante conserve l'ordre, une fonction décroissante l'inverse : pour encadrer $f(x)$ on utilise le sens de variation.""",
        exos=[
            ("Fonctions carré et cube", "Équations avec un carré", 1,
             r"""Résoudre dans $\mathbb{R}$ : $x^2=16$ ; $x^2=7$ ; $x^2=-3$ ; $(x-1)^2=25$.""",
             r"""$x=\pm4$ ; $x=\pm\sqrt7$ ; aucune solution ; $x-1=5$ ou $x-1=-5$ donc $S=\{-4\,;6\}$."""),
            ("Fonctions carré et cube", "Inéquations avec un carré", 2,
             r"""Résoudre dans $\mathbb{R}$ : $x^2\le9$ ; $x^2>2$ ; $(x+1)^2<4$.""",
             r"""$S_1=[-3\,;3]$ ; $S_2=]-\infty\,;-\sqrt2[\,\cup\,]\sqrt2\,;+\infty[$.
$(x+1)^2<4\iff-2<x+1<2\iff-3<x<1$ : $S_3=]-3\,;1[$."""),
            ("Fonctions carré et cube", "Encadrer avec les fonctions de référence", 2,
             r"""1. Sachant que $-3\le x\le-1$, encadrer $x^2$.
2. Sachant que $-2\le x\le3$, encadrer $x^2$ (attention !).
3. Sachant que $2<x<5$, encadrer $x^3$, $\dfrac1x$ et $\sqrt x$.""",
             r"""1. Le carré est décroissant sur $]-\infty\,;0]$ : $1\le x^2\le9$.
2. Le carré n'est pas monotone sur $[-2\,;3]$ : le minimum est $0$ (en $x=0$) et le maximum $9$ : $0\le x^2\le9$ (et non $4\le x^2\le9$).
3. $8<x^3<125$ ; l'inverse est décroissant sur $]0\,;+\infty[$ : $\dfrac15<\dfrac1x<\dfrac12$ ; $\sqrt2<\sqrt x<\sqrt5$."""),
            ("Fonction inverse", "Équations et inéquations avec l'inverse", 3,
             r"""Résoudre dans $\mathbb{R}^*$ : 1. $\dfrac1x=4$  2. $\dfrac1x\ge2$  3. $\dfrac1x<-\dfrac12$""",
             r"""1. $x=\dfrac14$.
2. Il faut $x>0$ (sinon $\dfrac1x<0$). Alors $1\ge2x\iff x\le\dfrac12$ : $S=\left]0\,;\dfrac12\right]$.
3. Il faut $x<0$. En multipliant par $x<0$, le sens change : $1>-\dfrac x2\iff x>-2$. Donc $S=]-2\,;0[$.
(Vérification : $x=-1$ donne $-1<-0{,}5$ vrai ; $x=-3$ donne $-\dfrac13<-\dfrac12$ faux.)"""),
            ("Fonction racine carrée", "Équations et inéquations avec racine", 2,
             r"""Résoudre : 1. $\sqrt x=3$  2. $\sqrt x=-2$  3. $\sqrt{x+1}=2$  4. $\sqrt x\le2$  5. $\sqrt{2x-1}>3$""",
             r"""1. $x=9$.  2. Une racine est positive : aucune solution.  3. $x+1=4$ donc $x=3$.
4. $0\le x\le4$ : $S=[0\,;4]$.
5. Domaine $x\ge\dfrac12$ ; $2x-1>9\iff x>5$ : $S=]5\,;+\infty[$."""),
            ("Fonctions carré et cube", "Position relative de deux courbes de référence", 3,
             r"""Étudier la position relative des courbes des fonctions $x\mapsto x^2$ et $x\mapsto x$. Où se coupent-elles ?""",
             r"""$x^2-x=x(x-1)$. Zéros $0$ et $1$.
- $x<0$ ou $x>1$ : $x(x-1)>0$, la parabole est au-dessus de la droite.
- $0<x<1$ : $x(x-1)<0$, la parabole est en dessous.
Les courbes se coupent en $(0\,;0)$ et $(1\,;1)$."""),
            ("Fonctions carré et cube", "Parité (approfondissement)", 3,
             r"""Une fonction est **paire** si $f(-x)=f(x)$, **impaire** si $f(-x)=-f(x)$ pour tout $x$ de $D_f$ (symétrique par rapport à $0$).
Étudier la parité de $f(x)=x^3+x$, $g(x)=x^2-3$ et $k(x)=x^2+x$.""",
             r"""$f(-x)=-x^3-x=-f(x)$ : $f$ est impaire.
$g(-x)=x^2-3=g(x)$ : $g$ est paire.
$k(1)=2$ et $k(-1)=0$ : $k(-1)\ne k(1)$ et $k(-1)\ne-k(1)$, donc $k$ n'est ni paire ni impaire."""),
        ],
    ),
    # ------------------------------------------------------------------ 11
    dict(
        nom="Fonctions affines",
        notions=["Expression et représentation", "Variations et signe"],
        recap=r"""## Définition
> Une fonction affine est de la forme $f(x)=ax+b$ ($a,b$ réels). Sa courbe est une **droite**.
- $a$ est le **coefficient directeur** (la pente) ; $b$ est l'**ordonnée à l'origine** ($f(0)=b$).
- Si $b=0$, $f(x)=ax$ est **linéaire** (proportionnalité).
- Pour $x_1\ne x_2$ : $a=\dfrac{f(x_2)-f(x_1)}{x_2-x_1}$ (taux d'accroissement, constant).
- Pour la tracer : deux points suffisent (par exemple $x=0$ et $x=1$).

## Variations
- $a>0$ : $f$ est **croissante** ; $a<0$ : $f$ est **décroissante** ; $a=0$ : $f$ est **constante**.

## Signe de $ax+b$
> $ax+b=0\iff x=-\dfrac ba$. Pour $a>0$ : négatif puis positif ; pour $a<0$ : positif puis négatif.

## Reconnaître une situation affine
Un tableau de valeurs correspond à une fonction affine si le taux $\dfrac{\Delta y}{\Delta x}$ est constant. Exemple : prise en charge de $2{,}50$ € plus $1{,}20$ € par km : $f(x)=1{,}2x+2{,}5$.""",
        exos=[
            ("Expression et représentation", "Fonction affine : calculs", 1,
             r"""Soit $f(x)=2x-3$.
1. Calculer l'image de $4$.
2. Quel est l'antécédent de $7$ ?
3. Tracer la représentation graphique de $f$.""",
             r"""1. $f(4)=5$.
2. $2x-3=7\iff x=5$.
3. Droite passant par $(0\,;-3)$ et $(2\,;1)$."""),
            ("Expression et représentation", "Fonction affine à partir de deux valeurs", 2,
             r"""Déterminer l'expression de la fonction affine :
1. $f$ telle que $f(1)=2$ et $f(3)=8$ ;
2. $g$ telle que $g(-2)=5$ et $g(4)=-7$.""",
             r"""1. $a=\dfrac{8-2}{3-1}=3$ ; $3\times1+b=2$ donc $b=-1$ : $f(x)=3x-1$.
2. $a=\dfrac{-7-5}{4-(-2)}=-2$ ; $-2\times(-2)+b=5$ donc $b=1$ : $g(x)=-2x+1$."""),
            ("Expression et représentation", "Intersection de deux droites", 2,
             r"""Soit $f(x)=-x+2$ et $g(x)=0{,}5x-1$.
1. Tracer leurs représentations dans un même repère.
2. Déterminer par le calcul les coordonnées de leur point d'intersection.""",
             r"""2. $-x+2=0{,}5x-1\iff3=1{,}5x\iff x=2$, puis $f(2)=0$. Intersection : $(2\,;0)$."""),
            ("Variations et signe", "Variations et signe", 1,
             r"""Pour $f(x)=-3x+6$ et $g(x)=4x+10$ : donner le sens de variation, dresser le tableau de signes, puis résoudre $f(x)>0$ et $g(x)\le0$.""",
             r"""$f$ : $a=-3<0$, décroissante ; $f(x)=0\iff x=2$ ; positive pour $x<2$. $f(x)>0\iff x<2$ : $S=]-\infty\,;2[$.
$g$ : $a=4>0$, croissante ; $g(x)=0\iff x=-2{,}5$ ; négative pour $x<-2{,}5$. $g(x)\le0\iff x\le-2{,}5$ : $S=]-\infty\,;-2{,}5]$."""),
            ("Expression et représentation", "Course de taxi", 2,
             r"""Une course de taxi coûte $2{,}50$ € de prise en charge plus $1{,}20$ € par km. Soit $f(x)$ le prix pour $x$ km.
1. Donner l'expression de $f$. Quel est le prix d'une course de $7$ km ?
2. Avec $20$ €, quelle distance entière peut-on parcourir au maximum ?""",
             r"""1. $f(x)=1{,}2x+2{,}5$ ; $f(7)=8{,}4+2{,}5=10{,}9$ €.
2. $1{,}2x+2{,}5\le20\iff x\le14{,}58\ldots$ : $14$ km ($f(14)=19{,}3$ €, alors que $f(15)=20{,}5$ € dépasse $20$ €)."""),
            ("Variations et signe", "Comparer deux tarifs", 2,
             r"""Un musée propose : tarif A : $15$ € d'abonnement puis $2$ € par entrée ; tarif B : $4$ € par entrée.
1. Exprimer les prix $f(x)$ (tarif A) et $g(x)$ (tarif B) pour $x$ entrées.
2. À partir de combien d'entrées le tarif A est-il avantageux ?""",
             r"""1. $f(x)=2x+15$ ; $g(x)=4x$.
2. $2x+15<4x\iff x>7{,}5$ : à partir de $8$ entrées."""),
            ("Expression et représentation", "Reconnaître une fonction affine", 2,
             r"""Parmi ces deux tableaux de valeurs, lequel correspond à une fonction affine ? Donner son expression.
$x$ : $0,1,2,3$ ; $f(x)$ : $4,7,10,13$.   $x$ : $0,1,2,3$ ; $g(x)$ : $1,2,4,8$.""",
             r"""$f$ : les accroissements sont $3,3,3$, constants : $f(x)=3x+4$.
$g$ : les accroissements sont $1,2,4$, non constants : $g$ n'est pas affine."""),
        ],
    ),
    # ------------------------------------------------------------------ 12
    dict(
        nom="Résolutions graphiques et algébriques",
        notions=["Équations et courbes", "Inéquations et position relative"],
        recap=r"""## Équations et courbes
> Résoudre $f(x)=k$ : chercher les abscisses des points de $\mathcal{C}_f$ d'ordonnée $k$ (intersection avec la droite horizontale $y=k$).
> Résoudre $f(x)=g(x)$ : chercher les abscisses des points d'intersection de $\mathcal{C}_f$ et $\mathcal{C}_g$.
- Par le calcul : on se ramène à $f(x)-g(x)=0$ puis on factorise.

## Inéquations et position relative
> $f(x)<g(x)$ : les $x$ pour lesquels $\mathcal{C}_f$ est **en dessous** de $\mathcal{C}_g$.
- Algébriquement : on étudie le signe de $f(x)-g(x)$ (tableau de signes).
- Une lecture graphique donne des valeurs approchées ; le calcul donne les valeurs exactes.

## Nombre de solutions de $f(x)=k$
Selon la valeur de $k$, l'équation $x^2=k$ a $2$, $1$ ou $0$ solutions ; $\dfrac1x=k$ a une solution si $k\ne0$ et aucune si $k=0$ ; $\sqrt x=k$ a une solution si $k\ge0$.""",
        exos=[
            ("Équations et courbes", "Parabole et droite", 2,
             r"""Soit $f(x)=x^2$ et $g(x)=x+2$.
1. Résoudre $f(x)=g(x)$. Donner les points d'intersection des courbes.
2. Résoudre $f(x)\le g(x)$.""",
             r"""1. $x^2-x-2=0\iff(x-2)(x+1)=0$ : $x=2$ ou $x=-1$. Points $(2\,;4)$ et $(-1\,;1)$.
2. $x^2-x-2=(x-2)(x+1)\le0\iff x\in[-1\,;2]$."""),
            ("Équations et courbes", "Une droite tangente à la parabole", 2,
             r"""Soit $f(x)=x^2$ et $g(x)=2x-1$. Résoudre $f(x)=g(x)$ puis $f(x)\ge g(x)$. Que peut-on dire des deux courbes ?""",
             r"""$x^2-2x+1=(x-1)^2=0\iff x=1$ : un seul point commun $(1\,;1)$.
$(x-1)^2\ge0$ pour tout $x$ : $f(x)\ge g(x)$ sur $\mathbb{R}$. La droite touche la parabole en un seul point et reste en dessous : elle lui est tangente."""),
            ("Inéquations et position relative", "Inverse et identité", 3,
             r"""Soit $f(x)=\dfrac1x$ et $g(x)=x$. Résoudre $f(x)=g(x)$ puis $f(x)<g(x)$.""",
             r"""Valeur interdite $0$. $\dfrac1x=x\iff x^2=1\iff x=\pm1$.
$\dfrac1x-x=\dfrac{1-x^2}{x}=\dfrac{(1-x)(1+x)}{x}$ : tableau de signes avec zéros $-1$, $1$ et valeur interdite $0$.
$\dfrac{(1-x)(1+x)}{x}<0$ pour $-1<x<0$ et pour $x>1$. Donc $S=]-1\,;0[\,\cup\,]1\,;+\infty[$."""),
            ("Équations et courbes", "Combien de solutions ?", 2,
             r"""Discuter, selon la valeur du réel $k$, le nombre de solutions de : 1. $x^2=k$  2. $\dfrac1x=k$  3. $\sqrt x=k$""",
             r"""1. $k>0$ : $2$ solutions ; $k=0$ : $1$ ; $k<0$ : $0$.
2. $k\ne0$ : $1$ solution ($x=\dfrac1k$) ; $k=0$ : aucune.
3. $k\ge0$ : $1$ solution ($x=k^2$) ; $k<0$ : aucune."""),
            ("Inéquations et position relative", "Coût, recette et bénéfice", 2,
             r"""Une entreprise a un coût de fabrication $C(x)=2x+50$ et une recette $R(x)=7x$ pour $x$ objets vendus.
1. Exprimer le bénéfice $B(x)=R(x)-C(x)$.
2. À partir de combien d'objets l'entreprise réalise-t-elle un bénéfice ?
3. Interpréter graphiquement.""",
             r"""1. $B(x)=5x-50$.
2. $B(x)>0\iff x>10$ : dès $11$ objets (à $10$ objets, le bénéfice est nul).
3. Les droites des fonctions $C$ et $R$ se coupent au point $(10\,;70)$ ; pour $x>10$, la droite de $R$ est au-dessus de celle de $C$."""),
        ],
    ),
]
