"""Domaine « Algorithmique et raisonnement » (programme de Seconde générale, 2019)."""

DOMAINE = "Algorithmique et raisonnement"

CHAPITRES = [
    # ------------------------------------------------------------------ 20
    dict(
        nom="Algorithmique et programmation",
        notions=["Variables et affectations", "Boucles et conditions", "Fonctions en Python"],
        recap=r"""## Variables et affectation
Une **variable** a un nom et une valeur. L'affectation `x = 5` met la valeur $5$ dans `x`. Les instructions s'exécutent **dans l'ordre**, de haut en bas.
- `y = 2*x - 3` calcule avec la valeur *actuelle* de `x`. `x = x + 1` augmente `x` de $1$.
- Opérations : `+  -  *  /  **` (puissance), `//` (quotient entier), `%` (reste).

## Instruction conditionnelle
`if condition:` … `elif autre_condition:` … `else:` … Comparaisons : `==  !=  <  <=  >  >=`. L'indentation (4 espaces) délimite le bloc.

## Boucles
- **Boucle bornée** : `for i in range(n):` répète $n$ fois ($i$ prend les valeurs $0$ à $n-1$) ; `range(a, b)` va de $a$ à $b-1$.
- **Boucle non bornée** : `while condition:` répète tant que la condition est vraie (attention à ce qu'elle finisse par devenir fausse).

## Fonctions
`def f(x):` … `return valeur`. Une fonction est appelée avec `f(4)`. `print(...)` affiche, `return` renvoie une valeur utilisable.
- Aléatoire : `import random` puis `random.randint(1, 6)` donne un entier entre $1$ et $6$ inclus.""",
        exos=[
            ("Variables et affectations", "Que fait ce programme ?", 1,
             r"""Qu'affiche le programme suivant ?
```
x = 5
y = 2*x - 3
x = y + 1
print(x, y)
```""",
             r"""`y` prend $2\times5-3=7$ ; puis `x` prend $7+1=8$. Le programme affiche `8 7`."""),
            ("Fonctions en Python", "Écrire une fonction", 1,
             r"""1. Écrire une fonction Python `f(x)` qui renvoie $3x^2-2x+1$.
2. Que renvoie `f(4)` ?""",
             r"""1.
```
def f(x):
    return 3*x**2 - 2*x + 1
```
2. $f(4)=3\times16-8+1=41$."""),
            ("Boucles et conditions", "Boucle for et somme", 2,
             r"""Quelle est la valeur de `s` à la fin ?
```
s = 0
for i in range(1, 11):
    s = s + i*i
```""",
             r"""`i` prend les valeurs $1$ à $10$ ; `s` est la somme des carrés : $1+4+9+\dots+100=385$."""),
            ("Boucles et conditions", "Boucle while : placement", 2,
             r"""On place $1000$ € à $3\,\%$ par an (intérêts composés). On veut savoir au bout de combien d'années le capital dépasse $1500$ €.
1. Compléter le programme.
```
c = 1000
n = 0
while ......:
    c = ......
    n = n + 1
print(n)
```
2. Que renvoie-t-il ?""",
             r"""1.
```
while c <= 1500:
    c = c * 1.03
    n = n + 1
```
2. $1{,}03^{13}\approx1{,}469<1{,}5$ et $1{,}03^{14}\approx1{,}513>1{,}5$ : le programme affiche `14` (capital $\approx1512{,}59$ €)."""),
            ("Boucles et conditions", "Condition : prix dégressif", 2,
             r"""```
def prix(n):
    if n >= 10:
        return 0.8 * 12 * n
    else:
        return 12 * n
```
1. Calculer `prix(5)`, `prix(10)` et `prix(12)`.
2. Pourquoi acheter $10$ articles coûte-t-il moins cher que d'en acheter $9$ ?""",
             r"""1. `prix(5)` $=60$ ; `prix(10)` $=0{,}8\times120=96$ ; `prix(12)` $=0{,}8\times144=115{,}2$.
2. `prix(9)` $=108>96$ : à partir de $10$ articles, la remise de $20\,\%$ s'applique à tout."""),
            ("Boucles et conditions", "Simulation d'un dé", 2,
             r"""```
import random
c = 0
for i in range(1000):
    if random.randint(1, 6) == 6:
        c = c + 1
print(c / 1000)
```
Que représente la valeur affichée ? Quelle valeur peut-on attendre ? Obtient-on toujours exactement la même ?""",
             r"""Le programme simule $1\,000$ lancers d'un dé et affiche la **fréquence** d'apparition du $6$. On attend une valeur proche de $\dfrac16\approx0{,}167$, mais pas exactement : à chaque exécution l'échantillon change (fluctuation d'échantillonnage)."""),
            ("Boucles et conditions", "Chercher un seuil", 3,
             r"""Écrire un programme qui renvoie le plus petit entier naturel $n$ tel que $n^2>500$. Quelle valeur obtient-on ?""",
             r"""```
n = 0
while n*n <= 500:
    n = n + 1
print(n)
```
$22^2=484\le500$ et $23^2=529>500$ : le programme affiche `23`."""),
        ],
    ),
    # ------------------------------------------------------------------ 21
    dict(
        nom="Logique et raisonnement",
        notions=["Implication et réciproque", "Contre-exemple et quantificateurs", "Types de raisonnement"],
        recap=r"""## Implication et équivalence
> « Si $P$ alors $Q$ » s'écrit $P\Rightarrow Q$. Sa **réciproque** est $Q\Rightarrow P$ : elle n'est pas toujours vraie.
- Si $P\Rightarrow Q$ et $Q\Rightarrow P$, on dit que $P$ et $Q$ sont **équivalentes** : $P\iff Q$.
- La **contraposée** de $P\Rightarrow Q$ est $\text{non }Q\Rightarrow\text{non }P$ : elle a toujours la même valeur de vérité que l'implication.

## Quantificateurs et contre-exemple
- « **Pour tout** $x$… » : pour montrer que c'est faux, il suffit d'un **contre-exemple**. Pour montrer que c'est vrai, un exemple ne suffit pas : il faut une démonstration.
- « **Il existe** $x$… » : pour montrer que c'est vrai, il suffit d'exhiber un exemple.

## Connecteurs et négation
- **et** (les deux), **ou** (inclusif : l'un, l'autre, ou les deux).
- Négation de « pour tout $x$, $P(x)$ » : « il existe $x$ tel que non $P(x)$ ».
- Négation de « $P$ et $Q$ » : « non $P$ ou non $Q$ ». Négation de « $P$ ou $Q$ » : « non $P$ et non $Q$ ».

## Types de raisonnement
- **Disjonction de cas** : on traite tous les cas possibles (par exemple $n$ pair ou impair).
- **Raisonnement par l'absurde** : on suppose le contraire de ce qu'on veut démontrer et on aboutit à une contradiction.
- **Raisonnement direct** : on enchaîne des déductions à partir des hypothèses.""",
        exos=[
            ("Implication et réciproque", "Écrire la réciproque", 1,
             r"""Écrire la réciproque de chaque implication, puis dire si l'implication et sa réciproque sont vraies :
1. Si un nombre est multiple de $6$, alors il est pair.
2. Si $ABCD$ est un losange, alors ses diagonales sont perpendiculaires.
3. Si $x=3$, alors $x^2=9$.""",
             r"""1. Vraie. Réciproque : « si un nombre est pair, il est multiple de $6$ » : fausse ($4$).
2. Vraie. Réciproque : « si les diagonales sont perpendiculaires, c'est un losange » : fausse (un cerf-volant).
3. Vraie. Réciproque : « si $x^2=9$ alors $x=3$ » : fausse ($x=-3$)."""),
            ("Contre-exemple et quantificateurs", "Vrai ou faux ?", 2,
             r"""Dire si les affirmations suivantes sont vraies ou fausses (justifier) :
1. Pour tout réel $x$, $x^2\ge x$.
2. Pour tout réel $x$, $x^2\ge0$.
3. Il existe un réel $x$ tel que $x^2=2$.
4. Pour tout entier naturel $n$, $n^2+n+11$ est un nombre premier.""",
             r"""1. Faux : $x=\dfrac12$ donne $\dfrac14<\dfrac12$.
2. Vrai : un carré est positif ou nul.
3. Vrai : $x=\sqrt2$.
4. Faux : pour $n=10$, $100+10+11=121=11^2$ n'est pas premier (alors que $n=0,\dots,9$ donnent des nombres premiers : un exemple ne prouve rien)."""),
            ("Types de raisonnement", "Disjonction de cas", 2,
             r"""Démontrer que, pour tout entier naturel $n$, $n(n+1)$ est pair.""",
             r"""Cas 1 : $n$ est pair, donc $n(n+1)$ est un multiple de $2$.
Cas 2 : $n$ est impair, donc $n+1$ est pair et $n(n+1)$ est pair.
Dans les deux cas, $n(n+1)$ est pair."""),
            ("Types de raisonnement", "Raisonnement par l'absurde", 3,
             r"""Montrer que $\dfrac13$ n'est pas un nombre décimal.""",
             r"""Supposons $\dfrac13=\dfrac a{10^k}$ avec $a$ entier et $k$ entier naturel. Alors $10^k=3a$, donc $3$ divise $10^k=2^k\times5^k$.
Or la décomposition en facteurs premiers de $10^k$ ne contient que $2$ et $5$ : contradiction. Donc $\dfrac13\notin\mathbb{D}$."""),
            ("Contre-exemple et quantificateurs", "Négation", 2,
             r"""Écrire la négation de chaque affirmation :
1. Tous les élèves de la classe ont plus de $15$ ans.
2. $x>3$ ou $x<-1$.
3. $x$ est pair et multiple de $3$.""",
             r"""1. Il existe un élève de la classe qui a $15$ ans ou moins.
2. $x\le3$ et $x\ge-1$, c'est-à-dire $-1\le x\le3$.
3. $x$ est impair ou $x$ n'est pas multiple de $3$."""),
            ("Implication et réciproque", "Implication ou équivalence ?", 2,
             r"""Compléter par $\Rightarrow$, $\Leftarrow$ ou $\iff$ :
1. $x=2$ … $x^2=4$   2. $x^2=4$ … $x=2$ ou $x=-2$   3. $x>3$ … $x>2$   4. $(x-1)(x+2)=0$ … $x=1$ ou $x=-2$""",
             r"""1. $\Rightarrow$ (la réciproque est fausse : $x=-2$).
2. $\iff$.
3. $\Rightarrow$ (si $x>3$ alors $x>2$ ; la réciproque est fausse : $x=2{,}5$).
4. $\iff$ (propriété du produit nul)."""),
        ],
    ),
]
