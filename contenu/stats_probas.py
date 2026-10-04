"""Domaine « Statistiques et probabilités » (programme de Seconde générale, 2019)."""

DOMAINE = "Statistiques et probabilités"

CHAPITRES = [
    # ------------------------------------------------------------------ 17
    dict(
        nom="Statistiques",
        notions=["Moyenne, médiane, quartiles", "Écart-type et dispersion", "Données groupées en classes"],
        recap=r"""## Indicateurs de position
> **Moyenne** : $\bar x=\dfrac{x_1n_1+x_2n_2+\dots+x_pn_p}{N}$ (avec les effectifs $n_i$ et $N=\sum n_i$).
- **Médiane** $M_e$ : valeur qui partage la série ordonnée en deux groupes de même effectif (au moins $50\,\%$ des valeurs $\le M_e$ et au moins $50\,\%$ $\ge M_e$). Si $N$ est pair, on prend la moyenne des deux valeurs centrales.
- **Quartiles** : $Q_1$ est la plus petite valeur telle qu'au moins $25\,\%$ des valeurs lui soient inférieures ou égales ; $Q_3$ la plus petite valeur telle qu'au moins $75\,\%$ des valeurs lui soient inférieures ou égales. (On repère le rang $\dfrac N4$ puis $\dfrac{3N}4$, arrondi à l'entier supérieur.)

## Indicateurs de dispersion
- **Étendue** : maximum $-$ minimum. **Écart interquartile** : $Q_3-Q_1$.
> **Variance** : $V=\dfrac{1}{N}\sum n_i(x_i-\bar x)^2$ ; **écart-type** : $\sigma=\sqrt V$.
- Plus $\sigma$ est grand, plus la série est dispersée autour de la moyenne.
- La médiane et l'écart interquartile sont peu sensibles aux valeurs extrêmes ; la moyenne et l'écart-type le sont davantage.

## Transformation affine
Si on remplace chaque valeur $x$ par $ax+b$ : la moyenne devient $a\bar x+b$ et l'écart-type devient $|a|\sigma$.

## Diagramme en boîte
Il résume la série par : minimum, $Q_1$, médiane, $Q_3$, maximum. Utile pour comparer deux séries.

## Données regroupées en classes
On estime la moyenne en utilisant le **centre** de chaque classe. La classe médiane est celle qui contient la médiane.""",
        exos=[
            ("Moyenne, médiane, quartiles", "Série de notes", 1,
             r"""Notes : $12,\ 15,\ 15,\ 10,\ 18,\ 20,\ 15,\ 14$. Calculer la moyenne, la médiane, $Q_1$ et $Q_3$.""",
             r"""Série ordonnée : $10,12,14,15,15,15,18,20$ ($N=8$).
Moyenne : $\dfrac{119}8=14{,}875$. Médiane : $\dfrac{15+15}2=15$.
$\dfrac N4=2$ : $Q_1$ est la $2^e$ valeur, $12$. $\dfrac{3N}4=6$ : $Q_3$ est la $6^e$ valeur, $15$."""),
            ("Moyenne, médiane, quartiles", "Série à effectifs", 2,
             r"""Notes d'un contrôle : valeur $8,10,12,14$ avec les effectifs $3,5,4,3$.
Calculer l'effectif total, la moyenne, la médiane, $Q_1$ et $Q_3$.""",
             r"""$N=15$. Moyenne : $\dfrac{8\times3+10\times5+12\times4+14\times3}{15}=\dfrac{164}{15}\approx10{,}93$.
Effectifs cumulés : $3$ ($8$), $8$ ($10$), $12$ ($12$), $15$ ($14$).
Médiane : $8^e$ valeur $=10$. $\dfrac N4=3{,}75$ : $4^e$ valeur, $Q_1=10$. $\dfrac{3N}4=11{,}25$ : $12^e$ valeur, $Q_3=12$."""),
            ("Écart-type et dispersion", "Calcul d'un écart-type", 2,
             r"""Calculer la variance puis l'écart-type de la série : $2,\ 4,\ 4,\ 4,\ 5,\ 5,\ 7,\ 9$.""",
             r"""Moyenne : $\dfrac{40}8=5$. Carrés des écarts : $9,1,1,1,0,0,4,16$, de somme $32$.
$V=\dfrac{32}8=4$ et $\sigma=\sqrt4=2$."""),
            ("Écart-type et dispersion", "Comparer deux séries", 2,
             r"""Deux classes ont la même moyenne $12$. Classe A : $\sigma=1{,}5$. Classe B : $\sigma=4$.
Les diagrammes en boîte : A (min $8$, $Q_1=11$, médiane $12$, $Q_3=13$, max $16$) ; B (min $2$, $Q_1=8$, médiane $12$, $Q_3=16$, max $20$).
Calculer les étendues et les écarts interquartiles. Que peut-on dire des deux classes ?""",
             r"""Étendues : A $=8$, B $=18$. Écarts interquartiles : A $=2$, B $=8$.
Même centre, mais les notes de la classe B sont beaucoup plus dispersées (écart-type plus grand) : classe plus hétérogène."""),
            ("Écart-type et dispersion", "Effet d'une transformation affine", 2,
             r"""Des notes sur $20$ ont pour moyenne $11{,}2$ et pour écart-type $2{,}5$.
1. On multiplie toutes les notes par $5$ (passage sur $100$). Moyenne et écart-type ?
2. Le professeur ajoute $2$ points à chaque note initiale. Moyenne et écart-type ?""",
             r"""1. Moyenne $56$, écart-type $12{,}5$.
2. Moyenne $13{,}2$, écart-type inchangé $2{,}5$ (ajouter une constante décale tout sans modifier la dispersion)."""),
            ("Données groupées en classes", "Données regroupées en classes", 2,
             r"""Les temps de trajet de $25$ personnes : $[0\,;10[$ : $4$ ; $[10\,;20[$ : $10$ ; $[20\,;30[$ : $6$ ; $[30\,;40[$ : $5$.
1. Estimer la moyenne. 2. Quelle est la classe modale ? la classe médiane ?""",
             r"""1. Centres $5,15,25,35$ : $\dfrac{4\times5+10\times15+6\times25+5\times35}{25}=\dfrac{495}{25}=19{,}8$ min.
2. Classe modale (effectif maximal) : $[10\,;20[$. La médiane est la $13^e$ valeur ; effectifs cumulés $4$, $14$ : classe médiane $[10\,;20[$."""),
            ("Moyenne, médiane, quartiles", "Problème de moyenne", 3,
             r"""La moyenne de $20$ élèves à un devoir est $11{,}5$.
1. Un élève ayant $6$ est remplacé par un élève ayant $15$. Nouvelle moyenne ?
2. Un $21^e$ élève passe le devoir : quelle note devrait-il avoir pour que la moyenne devienne $12$ ? Est-ce possible ?""",
             r"""Somme initiale $=20\times11{,}5=230$.
1. $\dfrac{230-6+15}{20}=\dfrac{239}{20}=11{,}95$.
2. $\dfrac{230+x}{21}=12\iff x=252-230=22$ : impossible, la note maximale est $20$."""),
        ],
    ),
    # ------------------------------------------------------------------ 18
    dict(
        nom="Probabilités",
        notions=["Vocabulaire et loi de probabilité", "Événements", "Tableaux et arbres"],
        recap=r"""## Vocabulaire
- **Expérience aléatoire** : on ne peut pas prévoir le résultat. **Issues** : résultats possibles. **Univers** $\Omega$ : ensemble des issues.
- **Événement** : partie de $\Omega$. Une **loi de probabilité** associe à chaque issue une probabilité (entre $0$ et $1$, de somme $1$).
> En situation d'**équiprobabilité** : $P(A)=\dfrac{\text{nombre d'issues favorables}}{\text{nombre d'issues possibles}}$.

## Événements
- **Contraire** $\bar A$ : $P(\bar A)=1-P(A)$.
- **Intersection** $A\cap B$ ($A$ et $B$) ; **réunion** $A\cup B$ ($A$ ou $B$, ou les deux).
> $P(A\cup B)=P(A)+P(B)-P(A\cap B)$
- $A$ et $B$ sont **incompatibles** si $A\cap B=\varnothing$ ; alors $P(A\cup B)=P(A)+P(B)$.

## Outils pour dénombrer
- **Tableau à double entrée** : pour deux lancers, deux caractères.
- **Arbre pondéré** : on multiplie les probabilités le long d'une branche, et on additionne les branches qui mènent à un même événement.
- **Tirage avec remise** : les tirages sont identiques à chaque fois ; **sans remise** : l'urne change.""",
        exos=[
            ("Événements", "Lancer de dé", 2,
             r"""On lance un dé équilibré à $6$ faces. $A$ : « le nombre est pair » ; $B$ : « le nombre est multiple de $3$ ».
Calculer $P(A)$, $P(B)$, $P(A\cap B)$ puis $P(A\cup B)$.""",
             r"""$P(A)=\dfrac12$, $P(B)=\dfrac13$, $A\cap B=\{6\}$ donc $P(A\cap B)=\dfrac16$.
$P(A\cup B)=\dfrac12+\dfrac13-\dfrac16=\dfrac23$."""),
            ("Vocabulaire et loi de probabilité", "Deux dés", 2,
             r"""On lance deux dés équilibrés à $6$ faces. Calculer la probabilité que : 1. la somme soit $7$ ; 2. la somme soit au moins $10$ ; 3. on obtienne un double ; 4. le produit soit pair.""",
             r"""$36$ issues équiprobables.
1. $6$ couples : $\dfrac6{36}=\dfrac16$.
2. $(4,6),(5,5),(6,4),(5,6),(6,5),(6,6)$ : $\dfrac6{36}=\dfrac16$.
3. $\dfrac6{36}=\dfrac16$.
4. Contraire : les deux nombres impairs, $3\times3=9$ couples. $1-\dfrac9{36}=\dfrac34$."""),
            ("Vocabulaire et loi de probabilité", "Tirage dans une urne", 2,
             r"""Une urne contient $3$ boules rouges, $5$ bleues et $2$ vertes. On tire une boule au hasard.
1. Calculer $P(R)$, $P(\text{non bleue})$ et $P(R\text{ ou }V)$.
2. On tire deux boules **avec remise**. Probabilité d'obtenir deux rouges ?
3. Même question **sans remise**.""",
             r"""1. $P(R)=\dfrac3{10}$ ; $P(\text{non bleue})=1-\dfrac5{10}=\dfrac12$ ; $P(R\text{ ou }V)=\dfrac5{10}=\dfrac12$.
2. $\dfrac3{10}\times\dfrac3{10}=\dfrac9{100}=0{,}09$.
3. $\dfrac3{10}\times\dfrac29=\dfrac6{90}=\dfrac1{15}$."""),
            ("Tableaux et arbres", "Tableau croisé", 2,
             r"""Dans un lycée de $200$ élèves : $70$ filles sont demi-pensionnaires (DP), $50$ filles sont externes, $40$ garçons sont DP et $40$ garçons sont externes. On choisit un élève au hasard.
1. Construire le tableau des effectifs.
2. Calculer $P(F)$, $P(DP)$, $P(F\cap DP)$ puis $P(F\cup DP)$.""",
             r"""Effectifs : filles $120$ (DP $70$, externes $50$) ; garçons $80$ (DP $40$, externes $40$) ; total DP $110$.
$P(F)=0{,}6$ ; $P(DP)=\dfrac{110}{200}=0{,}55$ ; $P(F\cap DP)=\dfrac{70}{200}=0{,}35$.
$P(F\cup DP)=0{,}6+0{,}55-0{,}35=0{,}8$ (contrôle : $1-P(\text{garçon externe})=1-0{,}2$)."""),
            ("Tableaux et arbres", "Arbre pondéré", 2,
             r"""Une pièce truquée donne Pile avec la probabilité $0{,}6$. On la lance deux fois.
Calculer la probabilité d'obtenir : deux Piles ; exactement un Pile ; au moins un Pile.""",
             r"""$P(PP)=0{,}6^2=0{,}36$. $P(\text{exactement un Pile})=2\times0{,}6\times0{,}4=0{,}48$.
$P(\text{au moins un Pile})=1-P(FF)=1-0{,}4^2=0{,}84$."""),
            ("Événements", "Jeu de 32 cartes", 2,
             r"""On tire une carte dans un jeu de $32$ cartes. Calculer la probabilité de : un roi ; un cœur ; le roi de cœur ; un roi **ou** un cœur ; ni un roi ni un cœur.""",
             r"""$P(\text{roi})=\dfrac4{32}=\dfrac18$ ; $P(\text{cœur})=\dfrac8{32}=\dfrac14$ ; $P(\text{roi de cœur})=\dfrac1{32}$.
$P(\text{roi ou cœur})=\dfrac4{32}+\dfrac8{32}-\dfrac1{32}=\dfrac{11}{32}$.
$P(\text{ni roi ni cœur})=1-\dfrac{11}{32}=\dfrac{21}{32}$."""),
            ("Événements", "Au moins un six", 3,
             r"""On lance $4$ fois un dé équilibré. Quelle est la probabilité d'obtenir au moins un $6$ ? (donner la valeur exacte puis arrondie au centième)""",
             r"""Contraire : aucun $6$ en $4$ lancers : $\left(\dfrac56\right)^4=\dfrac{625}{1296}$.
$P=1-\dfrac{625}{1296}=\dfrac{671}{1296}\approx0{,}52$."""),
            ("Vocabulaire et loi de probabilité", "Loi de probabilité à déterminer", 2,
             r"""Une roue porte les nombres $1,2,3,4$ avec les probabilités respectives $p,\ 2p,\ 3p,\ 4p$.
1. Déterminer $p$. 2. Calculer la probabilité d'obtenir un nombre pair, puis un nombre au moins égal à $3$.""",
             r"""1. $p+2p+3p+4p=10p=1$ donc $p=0{,}1$.
2. $P(\text{pair})=2p+4p=0{,}6$ ; $P(\ge3)=3p+4p=0{,}7$."""),
        ],
    ),
    # ------------------------------------------------------------------ 19
    dict(
        nom="Échantillonnage",
        notions=["Fluctuation d'échantillonnage", "Intervalle de fluctuation et prise de décision"],
        recap=r"""## Fluctuation d'échantillonnage
Quand on prélève un **échantillon** de taille $n$ dans une population où une proportion $p$ possède un caractère, la **fréquence observée** $f$ varie d'un échantillon à l'autre : c'est la fluctuation d'échantillonnage. Plus $n$ est grand, plus $f$ est proche de $p$.

## Intervalle de fluctuation
> Si $n\ge25$ et $0{,}2\le p\le0{,}8$, la fréquence observée $f$ appartient, dans environ $95\,\%$ des cas, à l'intervalle $\left[p-\dfrac1{\sqrt n}\,;\,p+\dfrac1{\sqrt n}\right]$.

## Prise de décision
On fait une **hypothèse** sur $p$ (par exemple « la pièce est équilibrée », $p=0{,}5$), on prélève un échantillon, puis :
- si $f$ est **dans** l'intervalle de fluctuation, on ne rejette pas l'hypothèse (elle est compatible avec l'observation) ;
- si $f$ est **hors** de l'intervalle, on rejette l'hypothèse, avec un risque d'erreur d'environ $5\,\%$.
- Ne pas rejeter une hypothèse ne prouve pas qu'elle est vraie.""",
        exos=[
            ("Fluctuation d'échantillonnage", "Calculer un intervalle de fluctuation", 1,
             r"""Pour $p=0{,}5$, donner l'intervalle de fluctuation à $95\,\%$ pour $n=100$ puis $n=400$. Que constate-t-on ?""",
             r"""$n=100$ : $\dfrac1{\sqrt{100}}=0{,}1$, intervalle $[0{,}4\,;0{,}6]$.
$n=400$ : $\dfrac1{20}=0{,}05$, intervalle $[0{,}45\,;0{,}55]$.
L'intervalle est deux fois plus étroit quand on multiplie la taille par $4$."""),
            ("Intervalle de fluctuation et prise de décision", "Une pièce est-elle équilibrée ?", 2,
             r"""On lance $200$ fois une pièce et on obtient $117$ Piles. Peut-on affirmer, au risque de $5\,\%$, que la pièce n'est pas équilibrée ?""",
             r"""Hypothèse $p=0{,}5$, $n=200$ : $\dfrac1{\sqrt{200}}\approx0{,}0707$. Intervalle $[0{,}429\,;0{,}571]$.
$f=\dfrac{117}{200}=0{,}585>0{,}571$ : $f$ est hors de l'intervalle, on rejette l'hypothèse : la pièce n'est probablement pas équilibrée (risque d'environ $5\,\%$ de se tromper)."""),
            ("Intervalle de fluctuation et prise de décision", "Un taux de réussite est-il cohérent ?", 2,
             r"""Un établissement annonce que $70\,\%$ de ses élèves réussissent un examen. Dans un échantillon de $300$ élèves, $197$ ont réussi. Ce résultat est-il compatible avec l'annonce ?""",
             r"""$p=0{,}7$, $n=300$ : $\dfrac1{\sqrt{300}}\approx0{,}0577$. Intervalle $[0{,}642\,;0{,}758]$.
$f=\dfrac{197}{300}\approx0{,}657$ appartient à l'intervalle : le résultat est compatible avec l'annonce."""),
            ("Fluctuation d'échantillonnage", "Conditions et taille d'échantillon", 3,
             r"""1. L'intervalle de fluctuation $\left[p-\dfrac1{\sqrt n};p+\dfrac1{\sqrt n}\right]$ peut-il être utilisé pour $p=0{,}1$ et $n=1000$ ? pour $p=0{,}5$ et $n=20$ ?
2. Quelle taille d'échantillon faut-il pour que l'amplitude de l'intervalle soit $0{,}02$ ?""",
             r"""1. Non dans les deux cas : $p=0{,}1\notin[0{,}2\,;0{,}8]$ ; $n=20<25$.
2. L'amplitude est $\dfrac2{\sqrt n}=0{,}02\iff\sqrt n=100\iff n=10\,000$."""),
        ],
    ),
]
