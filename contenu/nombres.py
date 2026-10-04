"""Domaine « Nombres et calculs » (programme de Seconde générale, 2019).
Chaque exercice : (notion, titre, difficulté 1-3, énoncé, correction)."""

DOMAINE = "Nombres et calculs"

CHAPITRES = [
    # ------------------------------------------------------------------ 1
    dict(
        nom="Ensembles de nombres et intervalles",
        notions=["Ensembles de nombres", "Intervalles", "Valeur absolue et distance"],
        recap=r"""## Ensembles de nombres
- $\mathbb{N}$ : entiers naturels $0,1,2,\dots$
- $\mathbb{Z}$ : entiers relatifs $\dots,-2,-1,0,1,2,\dots$
- $\mathbb{D}$ : nombres décimaux (écriture avec un nombre fini de décimales)
- $\mathbb{Q}$ : rationnels, de la forme $\dfrac{a}{b}$ avec $a\in\mathbb{Z}$ et $b\in\mathbb{Z}^*$
- $\mathbb{R}$ : réels, tous les points de la droite numérique
> $\mathbb{N}\subset\mathbb{Z}\subset\mathbb{D}\subset\mathbb{Q}\subset\mathbb{R}$
$\sqrt{2}$ et $\pi$ sont des réels **irrationnels** (non rationnels). $\dfrac{1}{3}$ est rationnel mais pas décimal.

## Intervalles
- $[a\,;b]$ : $a\le x\le b$ (crochets fermés : bornes incluses)
- $]a\,;b[$ : $a<x<b$ (crochets ouverts : bornes exclues)
- $[a\,;+\infty[$ : $x\ge a$ ; $]-\infty\,;b[$ : $x<b$. On ne met **jamais** un crochet fermé sur $\infty$.
- **Réunion** $A\cup B$ : les $x$ dans $A$ **ou** dans $B$. **Intersection** $A\cap B$ : les $x$ dans $A$ **et** dans $B$.

## Valeur absolue et distance
> $|x-a|$ est la distance entre les points d'abscisses $x$ et $a$ sur une droite graduée.
- $|x-a|=r \iff x=a-r$ ou $x=a+r$
- $|x-a|\le r \iff a-r\le x\le a+r$, c'est-à-dire $x\in[a-r\,;a+r]$
- $|x-a|\ge r \iff x\le a-r$ ou $x\ge a+r$
- $|x|=x$ si $x\ge0$, $|x|=-x$ si $x\le0$""",
        exos=[
            ("Ensembles de nombres", "Plus petit ensemble", 1,
             r"""Pour chaque nombre, donner le plus petit ensemble parmi $\mathbb{N},\mathbb{Z},\mathbb{D},\mathbb{Q},\mathbb{R}$ auquel il appartient :
$-7$ ; $\dfrac{3}{4}$ ; $\dfrac{1}{3}$ ; $\sqrt{9}$ ; $\sqrt{5}$ ; $0{,}25$ ; $\dfrac{12}{4}$.""",
             r"""$-7\in\mathbb{Z}$ ; $\dfrac34=0{,}75\in\mathbb{D}$ ; $\dfrac13\in\mathbb{Q}$ (écriture décimale infinie) ; $\sqrt9=3\in\mathbb{N}$ ; $\sqrt5\in\mathbb{R}$ ; $0{,}25\in\mathbb{D}$ ; $\dfrac{12}{4}=3\in\mathbb{N}$."""),
            ("Intervalles", "Inégalités et intervalles", 1,
             r"""Écrire sous forme d'intervalle ou de réunion d'intervalles :
1. $x\ge3$  2. $-2<x\le5$  3. $x<-1$ ou $x\ge4$  4. $x\neq2$""",
             r"""1. $[3\,;+\infty[$
2. $]-2\,;5]$
3. $]-\infty\,;-1[\,\cup\,[4\,;+\infty[$
4. $]-\infty\,;2[\,\cup\,]2\,;+\infty[$"""),
            ("Intervalles", "Intersection et réunion", 2,
             r"""On pose $A=[-3\,;4[$ et $B=]1\,;7]$.
1. Déterminer $A\cap B$ et $A\cup B$.
2. Les nombres $3{,}5$ et $4$ appartiennent-ils à $A\cap B$ ? à $A\cup B$ ?""",
             r"""1. $A\cap B=]1\,;4[$ et $A\cup B=[-3\,;7]$.
2. $3{,}5\in A\cap B$ (donc aussi dans $A\cup B$). $4\notin A$ donc $4\notin A\cap B$, mais $4\in B$ donc $4\in A\cup B$."""),
            ("Valeur absolue et distance", "Équations et inéquations avec valeur absolue", 2,
             r"""Résoudre dans $\mathbb{R}$ :
1. $|x-3|=5$  2. $|x-3|<2$  3. $|x+1|\ge3$""",
             r"""1. $x-3=5$ ou $x-3=-5$ : $S=\{-2\,;8\}$.
2. $|x-3|<2\iff 1<x<5$ : $S=]1\,;5[$.
3. $|x+1|=|x-(-1)|\ge3\iff x\le-4$ ou $x\ge2$ : $S=]-\infty\,;-4]\cup[2\,;+\infty[$."""),
            ("Valeur absolue et distance", "Distances sur une droite graduée", 2,
             r"""Sur une droite graduée, $A$ a pour abscisse $-2$ et $B$ pour abscisse $5$.
1. Calculer la distance $AB$.
2. Déterminer les points $M$ tels que $AM=3$.
3. Déterminer l'ensemble des points $M$ tels que $AM\le3$.""",
             r"""1. $AB=|5-(-2)|=7$.
2. $|x+2|=3\iff x=1$ ou $x=-5$.
3. $|x+2|\le3\iff-5\le x\le1$ : les points d'abscisse dans $[-5\,;1]$."""),
            ("Ensembles de nombres", "Irrationalité de racine de 2", 3,
             r"""Montrer par l'absurde que $\sqrt2$ n'est pas un nombre rationnel.""",
             r"""Supposons $\sqrt2=\dfrac pq$ avec $p,q$ entiers positifs et la fraction irréductible.
Alors $2q^2=p^2$, donc $p^2$ est pair, donc $p$ est pair : $p=2k$.
Alors $2q^2=4k^2$, soit $q^2=2k^2$, donc $q^2$ est pair, donc $q$ est pair.
$p$ et $q$ sont tous deux pairs : la fraction n'est pas irréductible. Contradiction. Donc $\sqrt2\notin\mathbb{Q}$."""),
        ],
    ),
    # ------------------------------------------------------------------ 2
    dict(
        nom="Calcul numérique",
        notions=["Fractions", "Puissances", "Racines carrées"],
        recap=r"""## Fractions
- $\dfrac ab+\dfrac cb=\dfrac{a+c}{b}$ ; pour des dénominateurs différents, on réduit au même dénominateur.
- $\dfrac ab\times\dfrac cd=\dfrac{ac}{bd}$ ; $\dfrac ab\div\dfrac cd=\dfrac ab\times\dfrac dc$ (on multiplie par l'**inverse**).
- On simplifie en divisant numérateur et dénominateur par leur PGCD.

## Puissances
> $a^m\times a^n=a^{m+n}$ ; $\dfrac{a^m}{a^n}=a^{m-n}$ ; $(a^m)^n=a^{mn}$ ; $(ab)^n=a^nb^n$ ; $a^{-n}=\dfrac1{a^n}$ ; $a^0=1$
- Notation scientifique : $a\times10^n$ avec $1\le a<10$ et $n\in\mathbb{Z}$.

## Racines carrées
Pour $a\ge0$, $\sqrt a$ est le nombre **positif** dont le carré est $a$.
> $(\sqrt a)^2=a$ ; $\sqrt{a^2}=|a|$ ; $\sqrt{ab}=\sqrt a\sqrt b$ ; $\sqrt{\dfrac ab}=\dfrac{\sqrt a}{\sqrt b}$ ($a,b\ge0$, $b\ne0$)
- Attention : $\sqrt{a+b}\neq\sqrt a+\sqrt b$ en général.
- Simplifier : $\sqrt{50}=\sqrt{25\times2}=5\sqrt2$.
- Rendre un dénominateur rationnel : $\dfrac{1}{\sqrt a-\sqrt b}=\dfrac{\sqrt a+\sqrt b}{a-b}$ (expression conjuguée).""",
        exos=[
            ("Fractions", "Opérations sur les fractions", 1,
             r"""Calculer et donner le résultat sous forme de fraction irréductible :
$A=\dfrac23+\dfrac56$ ; $B=\dfrac34\times\dfrac89$ ; $C=\dfrac56\div\dfrac{10}3$ ; $D=\dfrac12-\dfrac13+\dfrac14$""",
             r"""$A=\dfrac46+\dfrac56=\dfrac96=\dfrac32$.
$B=\dfrac{24}{36}=\dfrac23$.
$C=\dfrac56\times\dfrac3{10}=\dfrac{15}{60}=\dfrac14$.
$D=\dfrac6{12}-\dfrac4{12}+\dfrac3{12}=\dfrac5{12}$."""),
            ("Fractions", "Fraction de fractions", 2,
             r"""Calculer $A=\dfrac{\dfrac23-\dfrac14}{\dfrac56+\dfrac12}$ et donner le résultat sous forme irréductible.""",
             r"""Numérateur : $\dfrac8{12}-\dfrac3{12}=\dfrac5{12}$. Dénominateur : $\dfrac56+\dfrac36=\dfrac86=\dfrac43$.
$A=\dfrac5{12}\times\dfrac34=\dfrac{15}{48}=\dfrac5{16}$."""),
            ("Puissances", "Règles de calcul sur les puissances", 1,
             r"""Simplifier :
$A=\dfrac{2^5\times2^{-3}}{2^4}$ ; $B=(3^2)^3\times3^{-4}$ ; $C=\dfrac{10^{-3}\times5\times10^5}{2\times10^{-1}}$""",
             r"""$A=\dfrac{2^{2}}{2^4}=2^{-2}=\dfrac14$.
$B=3^6\times3^{-4}=3^2=9$.
$C=\dfrac{5\times10^2}{2\times10^{-1}}=2{,}5\times10^3=2500$."""),
            ("Puissances", "Notation scientifique : la lumière du Soleil", 2,
             r"""La lumière se déplace à $3\times10^8$ m/s. La distance Terre-Soleil est d'environ $1{,}5\times10^{11}$ m.
1. Calculer le temps mis par la lumière du Soleil pour atteindre la Terre, en secondes puis en minutes et secondes.
2. Calculer $\dfrac{3\times10^{8}\times2{,}4\times10^{-3}}{6\times10^{2}}$ et donner l'écriture scientifique du résultat.""",
             r"""1. $t=\dfrac{1{,}5\times10^{11}}{3\times10^8}=0{,}5\times10^3=500$ s, soit $8$ min $20$ s.
2. $\dfrac{7{,}2\times10^{5}}{6\times10^2}=1{,}2\times10^3$."""),
            ("Racines carrées", "Simplifier des racines", 2,
             r"""Écrire sous la forme $a\sqrt b$ avec $b$ entier le plus petit possible :
$\sqrt{50}$ ; $\sqrt{75}$ ; $\sqrt{18}+\sqrt{32}$ ; $3\sqrt{12}-\sqrt{27}$""",
             r"""$\sqrt{50}=5\sqrt2$ ; $\sqrt{75}=5\sqrt3$ ; $\sqrt{18}+\sqrt{32}=3\sqrt2+4\sqrt2=7\sqrt2$ ;
$3\sqrt{12}-\sqrt{27}=6\sqrt3-3\sqrt3=3\sqrt3$."""),
            ("Racines carrées", "Expressions conjuguées", 2,
             r"""1. Calculer $(3+\sqrt2)(3-\sqrt2)$ et $(\sqrt5+2)^2$.
2. Rendre rationnel le dénominateur de $\dfrac1{\sqrt3-1}$.""",
             r"""1. $(3+\sqrt2)(3-\sqrt2)=9-2=7$ ; $(\sqrt5+2)^2=5+4\sqrt5+4=9+4\sqrt5$.
2. $\dfrac1{\sqrt3-1}=\dfrac{\sqrt3+1}{(\sqrt3-1)(\sqrt3+1)}=\dfrac{\sqrt3+1}{2}$."""),
            ("Racines carrées", "Comparer des nombres avec des racines", 3,
             r"""Comparer $\sqrt3+\sqrt5$ et $\sqrt8$ (sans calculatrice).""",
             r"""Les deux nombres sont positifs : on compare leurs carrés.
$(\sqrt3+\sqrt5)^2=3+2\sqrt{15}+5=8+2\sqrt{15}>8=(\sqrt8)^2$. Donc $\sqrt3+\sqrt5>\sqrt8$."""),
        ],
    ),
    # ------------------------------------------------------------------ 3
    dict(
        nom="Arithmétique",
        notions=["Multiples et diviseurs", "Nombres premiers et PGCD"],
        recap=r"""## Multiples et diviseurs
> $a$ est un multiple de $b$ (ou $b$ divise $a$) s'il existe un entier $k$ tel que $a=kb$.
- Un entier pair s'écrit $2k$, un entier impair $2k+1$ ($k$ entier).
- Critères de divisibilité : par **2** (chiffre des unités pair), **3** (somme des chiffres divisible par 3), **4** (deux derniers chiffres), **5** (finit par 0 ou 5), **9** (somme des chiffres divisible par 9), **10** (finit par 0).

## Nombres premiers
> Un entier $n\ge2$ est premier s'il n'a que deux diviseurs : $1$ et $n$.
- Tout entier $\ge2$ se décompose de façon unique en produit de facteurs premiers : $360=2^3\times3^2\times5$.
- Pour tester si $n$ est premier, il suffit de tester les nombres premiers $p$ avec $p\le\sqrt n$.

## PGCD et PPCM
- Le **PGCD** de $a$ et $b$ est leur plus grand diviseur commun ; le **PPCM** est leur plus petit multiple commun non nul.
- Avec les décompositions : PGCD = facteurs communs aux plus petits exposants ; PPCM = tous les facteurs aux plus grands exposants.
- Une fraction est irréductible quand son numérateur et son dénominateur ont pour PGCD $1$.""",
        exos=[
            ("Multiples et diviseurs", "Critères de divisibilité", 1,
             r"""Le nombre $4\,572$ est-il divisible par $2$ ? $3$ ? $4$ ? $5$ ? $9$ ? Justifier.""",
             r"""Il finit par $2$ : divisible par $2$. Somme des chiffres $4+5+7+2=18$ : divisible par $3$ et par $9$. Les deux derniers chiffres $72=4\times18$ : divisible par $4$. Il ne finit ni par $0$ ni par $5$ : pas divisible par $5$."""),
            ("Nombres premiers et PGCD", "Décomposition en facteurs premiers", 2,
             r"""1. Décomposer $360$ et $1\,260$ en produit de facteurs premiers.
2. Combien $360$ a-t-il de diviseurs ?""",
             r"""1. $360=2^3\times3^2\times5$ ; $1\,260=2^2\times3^2\times5\times7$.
2. $(3+1)(2+1)(1+1)=24$ diviseurs."""),
            ("Nombres premiers et PGCD", "Un nombre est-il premier ?", 2,
             r"""Les nombres $247$ et $211$ sont-ils premiers ?""",
             r"""$247=13\times19$ : non premier.
$\sqrt{211}\approx14{,}5$ : on teste $2,3,5,7,11,13$. $211$ est impair, $2+1+1=4$ (pas multiple de 3), ne finit pas par 0 ou 5, $7\times30=210$, $11\times19=209$, $13\times16=208$ : aucun ne divise $211$. Donc $211$ est premier."""),
            ("Nombres premiers et PGCD", "PGCD et découpe de plaque", 2,
             r"""Une plaque rectangulaire mesure $84$ cm sur $126$ cm. On veut la découper en carrés identiques, sans perte, les plus grands possible.
Quelle est la longueur du côté d'un carré ? Combien de carrés obtient-on ?""",
             r"""$84=2^2\times3\times7$ et $126=2\times3^2\times7$, donc $\text{PGCD}(84,126)=2\times3\times7=42$.
Côté : $42$ cm. Nombre de carrés : $\dfrac{84}{42}\times\dfrac{126}{42}=2\times3=6$."""),
            ("Nombres premiers et PGCD", "Fraction irréductible", 2,
             r"""Rendre irréductible la fraction $\dfrac{252}{378}$.""",
             r"""$252=2^2\times3^2\times7$, $378=2\times3^3\times7$, $\text{PGCD}=2\times3^2\times7=126$.
$\dfrac{252}{378}=\dfrac{2\times126}{3\times126}=\dfrac23$."""),
            ("Multiples et diviseurs", "Carré d'un entier impair", 2,
             r"""Démontrer que le carré d'un entier impair est impair.""",
             r"""Soit $n=2k+1$ un entier impair. $n^2=4k^2+4k+1=2(2k^2+2k)+1$, de la forme $2m+1$ avec $m=2k^2+2k$ entier : $n^2$ est impair."""),
            ("Multiples et diviseurs", "Deux feux qui clignotent", 3,
             r"""Deux feux clignotent : l'un toutes les $12$ s, l'autre toutes les $18$ s. À $t=0$ ils clignotent ensemble.
1. Au bout de combien de secondes clignotent-ils de nouveau ensemble ?
2. Combien de fois clignotent-ils ensemble pendant les $5$ minutes suivantes ?""",
             r"""1. On cherche le PPCM de $12=2^2\times3$ et $18=2\times3^2$ : $2^2\times3^2=36$ s.
2. $5$ min $=300$ s et $300\div36\approx8{,}3$ : multiples $36,72,\dots,288$, soit $8$ fois."""),
        ],
    ),
    # ------------------------------------------------------------------ 4
    dict(
        nom="Proportions et pourcentages",
        notions=["Proportions et pourcentages", "Évolutions et coefficient multiplicateur", "Évolutions successives et réciproques"],
        recap=r"""## Proportion
> Si une population de $n_A$ éléments est incluse dans une population de $n$ éléments, la proportion est $p=\dfrac{n_A}{n}$ ($\times100$ pour un pourcentage).
- Proportion de proportion : on **multiplie** les proportions. $40\,\%$ de $55\,\%$ donne $0{,}40\times0{,}55=22\,\%$.

## Évolution et coefficient multiplicateur
> Taux d'évolution : $t=\dfrac{V_f-V_i}{V_i}$. Coefficient multiplicateur : $CM=\dfrac{V_f}{V_i}=1+t$.
- Augmenter de $15\,\%$ : multiplier par $1{,}15$. Diminuer de $15\,\%$ : multiplier par $0{,}85$.
- Retrouver la valeur initiale : $V_i=\dfrac{V_f}{CM}$.

## Évolutions successives et réciproques
- Les coefficients multiplicateurs se **multiplient** : $CM_{global}=CM_1\times CM_2$. Les taux ne s'additionnent pas.
- Évolution réciproque : $CM'=\dfrac1{CM}$. Une hausse de $25\,\%$ est annulée par une baisse de $20\,\%$ (et non $25\,\%$).
- Taux moyen sur $n$ périodes : $CM_{moyen}=\sqrt[n]{CM_{global}}$.""",
        exos=[
            ("Proportions et pourcentages", "Pourcentage de pourcentage", 1,
             r"""Dans un lycée de $800$ élèves, $55\,\%$ sont des filles. Parmi les filles, $40\,\%$ sont en Seconde.
Quel pourcentage des élèves du lycée sont des filles de Seconde ? Combien cela fait-il d'élèves ?""",
             r"""$0{,}55\times0{,}40=0{,}22$ : $22\,\%$ des élèves, soit $0{,}22\times800=176$ élèves."""),
            ("Évolutions et coefficient multiplicateur", "Calculer un taux d'évolution", 1,
             r"""1. Un prix passe de $45$ € à $54$ €. Quel est le taux d'évolution ?
2. Une population passe de $12\,500$ à $11\,875$ habitants. Quel est le taux d'évolution ? le coefficient multiplicateur ?""",
             r"""1. $\dfrac{54-45}{45}=0{,}2$ : hausse de $20\,\%$.
2. $\dfrac{11\,875-12\,500}{12\,500}=-0{,}05$ : baisse de $5\,\%$ ; $CM=0{,}95$."""),
            ("Évolutions successives et réciproques", "Baisse puis hausse", 2,
             r"""Un article coûte $80$ €. Son prix baisse de $15\,\%$, puis augmente de $15\,\%$.
1. Calculer le prix après la baisse.
2. Calculer le prix final.
3. Le prix final est-il égal au prix initial ? Expliquer.""",
             r"""1. $80\times0{,}85=68$ €.
2. $68\times1{,}15=78{,}2$ €.
3. Non : $0{,}85\times1{,}15=0{,}9775\neq1$. La hausse s'applique à un prix plus petit, donc elle ne compense pas la baisse."""),
            ("Évolutions successives et réciproques", "Évolutions successives", 2,
             r"""Calculer le taux d'évolution global :
1. une hausse de $20\,\%$ puis une hausse de $30\,\%$ ;
2. une baisse de $10\,\%$ puis une baisse de $20\,\%$.""",
             r"""1. $1{,}2\times1{,}3=1{,}56$ : hausse globale de $56\,\%$ (et non $50\,\%$).
2. $0{,}9\times0{,}8=0{,}72$ : baisse globale de $28\,\%$."""),
            ("Évolutions successives et réciproques", "Évolution réciproque", 2,
             r"""1. Un prix a augmenté de $25\,\%$. Quel pourcentage de baisse permet de revenir au prix initial ?
2. Un prix a baissé de $40\,\%$. Quel pourcentage de hausse permet de revenir au prix initial ?""",
             r"""1. $CM=1{,}25$, réciproque $\dfrac1{1{,}25}=0{,}8$ : baisse de $20\,\%$.
2. $CM=0{,}6$, réciproque $\dfrac1{0{,}6}=\dfrac53\approx1{,}667$ : hausse d'environ $66{,}7\,\%$."""),
            ("Évolutions et coefficient multiplicateur", "Retrouver la valeur initiale", 2,
             r"""1. Après une réduction de $30\,\%$, un manteau coûte $77$ €. Quel était son prix initial ?
2. Après une hausse de $8\,\%$, un loyer est de $540$ €. Quel était-il avant la hausse ?""",
             r"""1. $V_i=\dfrac{77}{0{,}7}=110$ €.
2. $V_i=\dfrac{540}{1{,}08}=500$ €."""),
            ("Évolutions successives et réciproques", "Taux annuel moyen", 3,
             r"""1. Un prix augmente de $10\,\%$ par an pendant $3$ ans. Quel est le taux d'évolution global ?
2. Une quantité augmente de $21\,\%$ en deux ans. Quel est le taux annuel moyen (supposé constant) ?""",
             r"""1. $1{,}1^3=1{,}331$ : hausse globale de $33{,}1\,\%$.
2. $CM^2=1{,}21$ donc $CM=\sqrt{1{,}21}=1{,}1$ : $10\,\%$ par an."""),
        ],
    ),
    # ------------------------------------------------------------------ 5
    dict(
        nom="Calcul littéral",
        notions=["Développer et réduire", "Identités remarquables", "Factoriser"],
        recap=r"""## Développer
> Distributivité : $k(a+b)=ka+kb$ et $(a+b)(c+d)=ac+ad+bc+bd$.
Développer, c'est transformer un produit en somme ; **réduire**, c'est regrouper les termes semblables.

## Identités remarquables
> $(a+b)^2=a^2+2ab+b^2$
> $(a-b)^2=a^2-2ab+b^2$
> $(a+b)(a-b)=a^2-b^2$
- Utile pour le calcul mental : $101^2=(100+1)^2=10\,201$.

## Factoriser
Factoriser, c'est transformer une somme en produit. Méthodes :
- **Facteur commun** : $6x^2-9x=3x(2x-3)$ ; $(x+1)(x-2)+3(x+1)=(x+1)(x+1)$
- **Identité remarquable** (dans l'autre sens) : $x^2-9=(x-3)(x+3)$ ; $4x^2+12x+9=(2x+3)^2$
- Pour montrer une égalité, on développe les deux membres, ou on part d'un membre pour arriver à l'autre.""",
        exos=[
            ("Développer et réduire", "Développer et réduire", 1,
             r"""Développer et réduire : $A=(2x+3)(x-5)$ ; $B=(x+4)^2$ ; $C=(3x-1)(2x+4)$ ; $D=(x-2)(x^2+3x-1)$.""",
             r"""$A=2x^2-10x+3x-15=2x^2-7x-15$.
$B=x^2+8x+16$.
$C=6x^2+12x-2x-4=6x^2+10x-4$.
$D=x^3+3x^2-x-2x^2-6x+2=x^3+x^2-7x+2$."""),
            ("Identités remarquables", "Identités remarquables", 1,
             r"""Développer : $(3x-2)^2$ ; $(5x+1)(5x-1)$ ; $(2x+\sqrt3)(2x-\sqrt3)$.
Calculer sans calculatrice : $101^2$ et $99\times101$.""",
             r"""$(3x-2)^2=9x^2-12x+4$ ; $(5x+1)(5x-1)=25x^2-1$ ; $(2x+\sqrt3)(2x-\sqrt3)=4x^2-3$.
$101^2=(100+1)^2=10\,201$ ; $99\times101=(100-1)(100+1)=9\,999$."""),
            ("Factoriser", "Factoriser avec un facteur commun", 2,
             r"""Factoriser : $A=6x^2-9x$ ; $B=(x+1)(x-2)+3(x+1)$ ; $C=(2x-1)^2-(2x-1)(x+3)$.""",
             r"""$A=3x(2x-3)$.
$B=(x+1)[(x-2)+3]=(x+1)(x+1)=(x+1)^2$.
$C=(2x-1)[(2x-1)-(x+3)]=(2x-1)(x-4)$."""),
            ("Factoriser", "Factoriser avec une identité remarquable", 2,
             r"""Factoriser : $A=x^2-9$ ; $B=4x^2+12x+9$ ; $C=25-(x+1)^2$ ; $D=x^2-10x+25$.""",
             r"""$A=(x-3)(x+3)$ ; $B=(2x+3)^2$ ; $C=[5-(x+1)][5+(x+1)]=(4-x)(6+x)$ ; $D=(x-5)^2$."""),
            ("Développer et réduire", "Démontrer une égalité", 2,
             r"""Montrer que, pour tout réel $x$, $(x+3)^2-(x-1)^2=8(x+1)$.""",
             r"""$(x+3)^2-(x-1)^2=(x^2+6x+9)-(x^2-2x+1)=8x+8=8(x+1)$."""),
            ("Factoriser", "Forme canonique et factorisation", 3,
             r"""1. Montrer que $x^2-6x+5=(x-3)^2-4$.
2. En déduire une factorisation de $x^2-6x+5$.""",
             r"""1. $(x-3)^2-4=x^2-6x+9-4=x^2-6x+5$.
2. $(x-3)^2-2^2=(x-3-2)(x-3+2)=(x-5)(x-1)$."""),
            ("Développer et réduire", "Programme de calcul", 2,
             r"""Programme de calcul : choisir un nombre $x$, lui ajouter $3$, élever le résultat au carré, puis soustraire $9$.
Montrer que le résultat est $x(x+6)$. Quel nombre faut-il choisir pour obtenir $0$ ?""",
             r"""Résultat : $(x+3)^2-9=x^2+6x+9-9=x^2+6x=x(x+6)$.
Il vaut $0$ si $x=0$ ou $x=-6$."""),
        ],
    ),
    # ------------------------------------------------------------------ 6
    dict(
        nom="Équations",
        notions=["Équations du premier degré", "Équations produit et quotient", "Mise en équation"],
        recap=r"""## Équations du premier degré
Résoudre $ax+b=cx+d$ : regrouper les $x$ d'un côté, les nombres de l'autre, puis diviser.
- On peut ajouter, soustraire, multiplier ou diviser par un nombre **non nul** les deux membres.
- Avec des fractions, on multiplie par le dénominateur commun.

## Équations produit nul
> Un produit de facteurs est nul si et seulement si l'un des facteurs est nul : $AB=0\iff A=0$ ou $B=0$.
- Pour résoudre une équation de degré supérieur, on se ramène à $0$ et on **factorise**.
- $x^2=a$ : si $a>0$, deux solutions $\sqrt a$ et $-\sqrt a$ ; si $a=0$, une solution $0$ ; si $a<0$, aucune solution.

## Équations avec quotient
> $\dfrac AB=0\iff A=0$ et $B\ne0$.
On commence toujours par chercher les **valeurs interdites** (dénominateur nul).

## Mettre un problème en équation
1. Choisir l'inconnue et la nommer. 2. Traduire l'énoncé par une équation. 3. Résoudre. 4. Vérifier et répondre par une phrase.""",
        exos=[
            ("Équations du premier degré", "Équations du premier degré", 1,
             r"""Résoudre dans $\mathbb{R}$ :
1. $3x-7=2x+5$  2. $\dfrac x2+1=\dfrac{2x-1}3$  3. $5(x-2)-3=2(x+1)+x$""",
             r"""1. $x=12$.
2. On multiplie par $6$ : $3x+6=4x-2$ donc $x=8$.
3. $5x-13=3x+2$ donc $2x=15$, $x=7{,}5$."""),
            ("Équations produit et quotient", "Équations produit nul", 2,
             r"""Résoudre dans $\mathbb{R}$ :
1. $(2x-1)(x+4)=0$  2. $x^2-9=0$  3. $x^2=-4$  4. $x^2+5x=0$""",
             r"""1. $S=\left\{\dfrac12\,;-4\right\}$.
2. $(x-3)(x+3)=0$ : $S=\{-3\,;3\}$.
3. Un carré n'est jamais négatif : $S=\varnothing$.
4. $x(x+5)=0$ : $S=\{-5\,;0\}$."""),
            ("Équations produit et quotient", "Factoriser pour résoudre", 3,
             r"""Résoudre dans $\mathbb{R}$ :
1. $(x+1)(x-2)+3(x+1)=0$  2. $4x^2-12x+9=0$  3. $(x-3)^2=(2x+1)^2$""",
             r"""1. $(x+1)(x+1)=0$ donc $x=-1$.
2. $(2x-3)^2=0$ donc $x=\dfrac32$.
3. $(x-3)^2-(2x+1)^2=0\iff[(x-3)-(2x+1)][(x-3)+(2x+1)]=0\iff(-x-4)(3x-2)=0$.
$S=\left\{-4\,;\dfrac23\right\}$."""),
            ("Équations produit et quotient", "Équations avec quotient", 2,
             r"""Résoudre dans $\mathbb{R}$ (en précisant les valeurs interdites) :
1. $\dfrac{x-3}{x+2}=0$  2. $\dfrac{2x+1}{x-1}=3$  3. $\dfrac1x+1=\dfrac3x$""",
             r"""1. Valeur interdite $-2$. $x-3=0$ : $S=\{3\}$.
2. Valeur interdite $1$. $2x+1=3(x-1)\iff x=4$ : $S=\{4\}$.
3. Valeur interdite $0$. $1+x=3$ donc $x=2$ : $S=\{2\}$."""),
            ("Mise en équation", "Âge du père et du fils", 1,
             r"""Un père a $40$ ans et son fils $12$ ans. Dans combien d'années l'âge du père sera-t-il le double de celui du fils ?""",
             r"""Soit $x$ le nombre d'années. $40+x=2(12+x)\iff40+x=24+2x\iff x=16$.
Dans $16$ ans : le père aura $56$ ans, le fils $28$ ans."""),
            ("Mise en équation", "Dimensions d'un rectangle", 2,
             r"""Un rectangle a un périmètre de $34$ cm. Sa longueur dépasse sa largeur de $5$ cm. Quelles sont ses dimensions ? Quelle est son aire ?""",
             r"""Largeur $\ell$, longueur $\ell+5$ : $2(\ell+\ell+5)=34\iff2\ell+5=17\iff\ell=6$.
Dimensions : $6$ cm sur $11$ cm ; aire $66$ cm$^2$."""),
            ("Mise en équation", "Location de voiture", 2,
             r"""Deux tarifs de location : A : $30$ € fixes plus $0{,}40$ € par km ; B : $0{,}70$ € par km.
Pour quelle distance les deux tarifs sont-ils égaux ?""",
             r"""$30+0{,}4x=0{,}7x\iff30=0{,}3x\iff x=100$. Les tarifs sont égaux pour $100$ km."""),
        ],
    ),
    # ------------------------------------------------------------------ 7
    dict(
        nom="Inéquations et signe",
        notions=["Inéquations du premier degré", "Tableaux de signes"],
        recap=r"""## Inéquations du premier degré
On résout comme une équation, avec une règle supplémentaire :
> Multiplier ou diviser par un nombre **négatif** change le sens de l'inégalité.
La solution s'écrit sous forme d'intervalle. Exemple : $-2x+3\le7\iff x\ge-2$, $S=[-2\,;+\infty[$.

## Signe de $ax+b$ ($a\ne0$)
> $ax+b$ s'annule en $x=-\dfrac ba$. Il est du signe de $a$ après ce zéro, de signe contraire avant.
Si $a>0$ : $-$ puis $+$ ; si $a<0$ : $+$ puis $-$.

## Inéquations produit ou quotient
1. Mettre l'inéquation sous la forme « expression $\ge0$ » (ou $>$, $\le$, $<$ ) avec un produit ou un quotient de facteurs.
2. Dresser un **tableau de signes** avec une ligne par facteur et une ligne pour le produit (règle des signes).
3. Lire les solutions. Pour un quotient, la valeur qui annule le dénominateur est exclue (double barre).
- $x^2\le a$ (avec $a>0$) $\iff-\sqrt a\le x\le\sqrt a$ ; $x^2\ge a\iff x\le-\sqrt a$ ou $x\ge\sqrt a$.""",
        exos=[
            ("Inéquations du premier degré", "Inéquations du premier degré", 1,
             r"""Résoudre et donner l'ensemble des solutions sous forme d'intervalle :
1. $-2x+3\le7$  2. $3x-5>x+7$  3. $\dfrac{x+1}2\ge\dfrac{2x-3}3$""",
             r"""1. $-2x\le4\iff x\ge-2$ : $S=[-2\,;+\infty[$.
2. $2x>12\iff x>6$ : $S=]6\,;+\infty[$.
3. $3(x+1)\ge2(2x-3)\iff3x+3\ge4x-6\iff9\ge x$ : $S=]-\infty\,;9]$."""),
            ("Tableaux de signes", "Signe d'une expression affine", 1,
             r"""Dresser le tableau de signes de $2x-6$ puis de $-3x+9$.""",
             r"""$2x-6$ s'annule en $3$ : négatif pour $x<3$, positif pour $x>3$.
$-3x+9$ s'annule en $3$ : positif pour $x<3$, négatif pour $x>3$ (coefficient $-3<0$)."""),
            ("Tableaux de signes", "Inéquation produit", 2,
             r"""Résoudre $(x-2)(x+3)\ge0$.""",
             r"""Zéros : $-3$ et $2$.
$x<-3$ : $(-)(-)=+$ ; $-3<x<2$ : $(-)(+)=-$ ; $x>2$ : $(+)(+)=+$.
$S=]-\infty\,;-3]\cup[2\,;+\infty[$."""),
            ("Tableaux de signes", "Inéquation quotient", 2,
             r"""Résoudre $\dfrac{2x-1}{x+3}<0$.""",
             r"""Valeur interdite $-3$ ; le numérateur s'annule en $\dfrac12$.
$x<-3$ : $\dfrac{-}{-}=+$ ; $-3<x<\dfrac12$ : $\dfrac{-}{+}=-$ ; $x>\dfrac12$ : $+$.
$S=\left]-3\,;\dfrac12\right[$."""),
            ("Tableaux de signes", "Inéquations avec un carré", 2,
             r"""Résoudre : 1. $x^2-4\le0$  2. $x^2>9$""",
             r"""1. $(x-2)(x+2)\le0$ : $S=[-2\,;2]$.
2. $x^2-9>0\iff(x-3)(x+3)>0$ : $S=]-\infty\,;-3[\cup]3\,;+\infty[$."""),
            ("Tableaux de signes", "Produit à coefficient négatif", 3,
             r"""Résoudre $(3x+1)(2-x)>0$.""",
             r"""Zéros : $-\dfrac13$ et $2$.
$x<-\dfrac13$ : $(-)(+)=-$ ; $-\dfrac13<x<2$ : $(+)(+)=+$ ; $x>2$ : $(+)(-)=-$.
$S=\left]-\dfrac13\,;2\right[$."""),
            ("Inéquations du premier degré", "Abonnement à une salle de sport", 2,
             r"""Une salle propose un abonnement de $120$ € puis $5$ € par séance, ou $9$ € la séance sans abonnement.
À partir de combien de séances l'abonnement est-il plus avantageux ?""",
             r"""Pour $n$ séances : $120+5n<9n\iff120<4n\iff n>30$. L'abonnement est plus avantageux dès $31$ séances."""),
        ],
    ),
]
