"""Séries d'exercices supplémentaires (développer, factoriser, résoudre) et rappels de cours courts.
Fusionnés avec les chapitres de nombres.py."""

RAPPELS = {
    "Calcul littéral": r"""> **Distributivité** : $k(a+b)=ka+kb$ et $(a+b)(c+d)=ac+ad+bc+bd$
> $(a+b)^2=a^2+2ab+b^2$
> $(a-b)^2=a^2-2ab+b^2$
> $(a+b)(a-b)=a^2-b^2$
> **Facteur commun** : $ka+kb=k(a+b)$ ; le facteur peut être une parenthèse : $(x+1)(2x-3)+(x+1)(x+5)=(x+1)[(2x-3)+(x+5)]$
> **Attention aux signes** : $-(a-b)=b-a$, donc $5-x=-(x-5)$
Pour factoriser, on cherche d'abord un facteur commun, puis une identité remarquable (dans le sens $a^2-b^2=(a-b)(a+b)$, etc.).""",
    "Équations": r"""> **Produit nul** : $A\times B=0\iff A=0$ ou $B=0$
> $x^2=a$ : si $a>0$, $x=\sqrt a$ ou $x=-\sqrt a$ ; si $a<0$, aucune solution
Pour résoudre une équation du second degré simple : tout passer dans un membre, **factoriser**, puis utiliser le produit nul.
Ne jamais « diviser par $x-2$ » : on le met en facteur (on perdrait la solution $x=2$).""",
}

SUPPL = {
    "Calcul littéral": [
        ("Développer et réduire", "Série : développer (double distributivité)", 1,
         r"""Développer et réduire chaque expression :
$A(x)=(x+3)(x+5)$
$B(x)=(2x-1)(x+4)$
$C(x)=(3x-2)(2x-5)$
$D(x)=(4-x)(3x+2)$
$E(x)=(x+1)(x^2-x+1)$
$F(x)=2x(x-3)-(x+1)(x-2)$""",
         r"""$A=x^2+5x+3x+15=x^2+8x+15$.
$B=2x^2+8x-x-4=2x^2+7x-4$.
$C=6x^2-15x-4x+10=6x^2-19x+10$.
$D=12x+8-3x^2-2x=-3x^2+10x+8$.
$E=x^3-x^2+x+x^2-x+1=x^3+1$.
$F=2x^2-6x-(x^2-x-2)=2x^2-6x-x^2+x+2=x^2-5x+2$."""),
        ("Identités remarquables", "Série : développer avec les identités remarquables", 2,
         r"""Développer et réduire en utilisant les identités remarquables :
$A(x)=(x+7)^2$
$B(x)=(3x-4)^2$
$C(x)=(5x+2)(5x-2)$
$D(x)=(2x+3y)^2$
$E(x)=\left(\dfrac x2+3\right)^2$
$F(x)=(4-3x)^2$
$G(x)=-(x-4)^2+(x+2)(x-2)$""",
         r"""$A=x^2+14x+49$.
$B=9x^2-24x+16$.
$C=25x^2-4$.
$D=4x^2+12xy+9y^2$.
$E=\dfrac{x^2}4+3x+9$.
$F=16-24x+9x^2$.
$G=-(x^2-8x+16)+(x^2-4)=-x^2+8x-16+x^2-4=8x-20$."""),
        ("Factoriser", "Série : factoriser avec un facteur commun", 2,
         r"""Factoriser chaque expression (attention aux signes !) :
$A(x)=(3x+1)(x-2)+(3x+1)(2x+5)$
$B(x)=(x-4)(2x+1)-(x-4)(x+3)$
$C(x)=(2x-5)^2+(2x-5)(x+1)$
$D(x)=6x^2-4x$
$E(x)=(x-5)(2x-3)-(5-x)(10-x)$
$F(x)=(x+2)(3x-1)-(x+2)$""",
         r"""$A=(3x+1)[(x-2)+(2x+5)]=(3x+1)(3x+3)=3(3x+1)(x+1)$.
$B=(x-4)[(2x+1)-(x+3)]=(x-4)(x-2)$.
$C=(2x-5)[(2x-5)+(x+1)]=(2x-5)(3x-4)$.
$D=2x(3x-2)$.
$E$ : $5-x=-(x-5)$, donc $-(5-x)(10-x)=(x-5)(10-x)$ et $E=(x-5)[(2x-3)+(10-x)]=(x-5)(x+7)$.
$F=(x+2)(3x-1)-1\times(x+2)=(x+2)[(3x-1)-1]=(x+2)(3x-2)$."""),
        ("Factoriser", "Série : factoriser avec les identités remarquables", 2,
         r"""Factoriser chaque expression :
$A(x)=x^2-16$
$B(x)=9x^2-49$
$C(x)=x^2+6x+9$
$D(x)=4x^2-20x+25$
$E(x)=(x+3)^2-25$
$F(x)=(2x+1)^2-(x-4)^2$
$G(x)=x^2-2$""",
         r"""$A=(x-4)(x+4)$.
$B=(3x-7)(3x+7)$.
$C=(x+3)^2$.
$D=(2x-5)^2$.
$E=(x+3-5)(x+3+5)=(x-2)(x+8)$.
$F=[(2x+1)-(x-4)][(2x+1)+(x-4)]=(x+5)(3x-3)=3(x+5)(x-1)$.
$G=(x-\sqrt2)(x+\sqrt2)$."""),
        ("Factoriser", "Série : développer, factoriser, vérifier", 2,
         r"""Pour chacune des expressions suivantes :
1. la développer ; 2. la factoriser ; 3. développer l'expression factorisée pour vérifier qu'on retrouve bien le résultat du 1.
$A(x)=(3x-1)^2+(3x-1)(x+2)$
$B(x)=(x+4)(2x-3)-(x+4)(x-1)$
$C(x)=4x^2-9+(2x-3)(x+1)$
$D(x)=(x-2)^2-(2x+1)(x-2)$
$E(x)=x(x-3)-2(x-3)$
$F(x)=(5x-1)^2-(3x+2)^2$""",
         r"""$A$ : développée $12x^2-x-1$ ; factorisée $(3x-1)(4x+1)$ (vérif. : $12x^2+3x-4x-1$ ✔).
$B$ : développée $x^2+2x-8$ ; factorisée $(x+4)(x-2)$ (vérif. : $x^2-2x+4x-8$ ✔).
$C$ : développée $6x^2-x-12$ ; factorisée $(2x-3)(2x+3)+(2x-3)(x+1)=(2x-3)(3x+4)$ (vérif. : $6x^2+8x-9x-12$ ✔).
$D$ : développée $-x^2-x+6$ ; factorisée $(x-2)[(x-2)-(2x+1)]=(x-2)(-x-3)=-(x-2)(x+3)$ (vérif. : $-(x^2+x-6)$ ✔).
$E$ : développée $x^2-5x+6$ ; factorisée $(x-3)(x-2)$ (vérif. : $x^2-2x-3x+6$ ✔).
$F$ : développée $16x^2-22x-3$ ; factorisée $(5x-1-3x-2)(5x-1+3x+2)=(2x-3)(8x+1)$ (vérif. : $16x^2+2x-24x-3$ ✔)."""),
        ("Identités remarquables", "Calcul astucieux", 2,
         r"""Calculer de tête, en utilisant les identités remarquables :
1. $998^2$  2. $49\times51$  3. $2025^2-2024\times2026$  4. $102^2-98^2$  5. $7{,}5^2-2{,}5^2$""",
         r"""1. $(1000-2)^2=1\,000\,000-4\,000+4=996\,004$.
2. $(50-1)(50+1)=2\,500-1=2\,499$.
3. $2024\times2026=(2025-1)(2025+1)=2025^2-1$, donc le résultat est $1$.
4. $(102-98)(102+98)=4\times200=800$.
5. $(7{,}5-2{,}5)(7{,}5+2{,}5)=5\times10=50$."""),
        ("Factoriser", "Programme de calcul à factoriser", 2,
         r"""Programme de calcul : choisir un nombre $x$, le multiplier par $3$, ajouter $2$, élever au carré, puis soustraire $4$.
1. Quel résultat obtient-on avec $x=1$ ?
2. Exprimer le résultat en fonction de $x$ puis le factoriser.
3. Pour quels nombres $x$ le résultat est-il nul ?""",
         r"""1. $(3+2)^2-4=25-4=21$.
2. Résultat : $(3x+2)^2-4=(3x+2-2)(3x+2+2)=3x(3x+4)$ (avec $x=1$ : $3\times7=21$ ✔).
3. $3x(3x+4)=0\iff x=0$ ou $x=-\dfrac43$."""),
        ("Factoriser", "Aire d'un cadre", 3,
         r"""On retire d'un carré de côté $x+3$ (en cm, avec $x>0$) un carré de côté $2$.
1. Montrer que l'aire restante est $x^2+6x+5$.
2. La factoriser.
3. Pour quelle valeur de $x$ l'aire vaut-elle $21$ cm$^2$ ?""",
         r"""1. $(x+3)^2-2^2=x^2+6x+9-4=x^2+6x+5$.
2. $(x+3)^2-2^2=(x+3-2)(x+3+2)=(x+1)(x+5)$.
3. $(x+1)(x+5)=21\iff x^2+6x-16=0\iff(x+8)(x-2)=0$. Comme $x>0$ : $x=2$ (vérif. : $5^2-4=21$ ✔)."""),
    ],
    "Équations": [
        ("Équations produit et quotient", "Série : équations à factoriser", 2,
         r"""Résoudre dans $\mathbb{R}$ :
1. $3x(x+4)=(2x-1)(x+4)$
2. $(2x-1)(x+3)=-3$
3. $(4x+3)(x-5)=4x+3$
4. $x^2-25=(x-5)(2x+1)$
5. $(2x-1)^2-9=0$
6. $x^2-6x=-9$""",
         r"""1. $(x+4)[3x-(2x-1)]=(x+4)(x+1)=0$ : $S=\{-4\,;-1\}$.
2. $2x^2+5x-3=-3\iff2x^2+5x=0\iff x(2x+5)=0$ : $S=\left\{-\dfrac52\,;0\right\}$.
3. $(4x+3)(x-5)-(4x+3)=(4x+3)(x-6)=0$ : $S=\left\{-\dfrac34\,;6\right\}$.
4. $(x-5)(x+5)-(x-5)(2x+1)=(x-5)(4-x)=0$ : $S=\{4\,;5\}$.
5. $(2x-1-3)(2x-1+3)=(2x-4)(2x+2)=0$ : $S=\{-1\,;2\}$.
6. $x^2-6x+9=(x-3)^2=0$ : $S=\{3\}$."""),
        ("Équations produit et quotient", "Série : ne pas simplifier par x", 3,
         r"""Résoudre dans $\mathbb{R}$ (sans jamais « diviser par $x$ » ou par une expression qui dépend de $x$) :
1. $4x^2=9x$
2. $9x^2-1=0$
3. $x^2-4x+4=0$
4. $x^3=4x$
5. $(2x+3)^2=(x-1)^2$""",
         r"""1. $4x^2-9x=x(4x-9)=0$ : $S=\left\{0\,;\dfrac94\right\}$.
2. $(3x-1)(3x+1)=0$ : $S=\left\{-\dfrac13\,;\dfrac13\right\}$.
3. $(x-2)^2=0$ : $S=\{2\}$.
4. $x^3-4x=x(x^2-4)=x(x-2)(x+2)=0$ : $S=\{-2\,;0\,;2\}$.
5. $(2x+3)^2-(x-1)^2=[(2x+3)-(x-1)][(2x+3)+(x-1)]=(x+4)(3x+2)=0$ : $S=\left\{-4\,;-\dfrac23\right\}$."""),
    ],
}
