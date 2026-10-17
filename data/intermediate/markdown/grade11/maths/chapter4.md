<!-- page 1 of 13 -->

The image provided is a QR code. As per the instructions, I am to process text and non-textual content that can be extracted from it. Therefore, no textual content can be extracted or converted according to the given instructions.

11076CHOS

Chapter

4

# COMPLEX NUMBERS AND QUADRATIC EQUATIONS

◆ Mathematics is the Queen of Sciences and Arithmetic is the Queen of Mathematics. – GAUSS ◆

## 4.1 Introduction

In earlier classes, we have studied linear equations in one and two variables and quadratic equations in one variable. We have seen that the equation  $x^{2} + 1 = 0$  has no real solution as  $x^{2} + 1 = 0$  gives  $x^{2} = -1$  and square of every real number is non-negative. So, we need to extend the real number system to a larger system so that we can find the solution of the equation  $x^{2} = -1$ . In fact, the main objective is to solve the equation  $ax^{2} + bx + c = 0$ , where  $D = b^{2} - 4ac < 0$ , which is not possible in the system of real numbers.

![Image block](doc:a0f0ab4/tier:standard/page:1/block:9)

W. R. Hamilton (1805-1865)

## 4.2 Complex Numbers

Let us denote $\sqrt{-1}$ by the symbol $i$. Then, we have $i^2 = -1$. This means that $i$ is a solution of the equation $x^2 + 1 = 0$.

A number of the form $a + ib$, where $a$ and $b$ are real numbers, is defined to be a

complex number. For example,  $2 + i3$ ,  $(-1) + i\sqrt{3}$ ,  $4 + i\left(\frac{-1}{11}\right)$  are complex numbers.

For the complex number  $z = a + ib$ , a is called the real part, denoted by Re z and b is called the imaginary part denoted by Im z of the complex number z. For example, if  $z = 2 + i5$ , then Re z = 2 and Im z = 5.

Two complex numbers $z_{1} = a + ib$ and $z_{2} = c + id$ are equal if $a = c$ and $b = d$.

Reprint 2025-26

<!-- page 2 of 13 -->

COMPLEX NUMBERS AND QUADRATIC EQUATIONS

77

Example 1 If  $4x + i(3x - y) = 3 + i(-6)$ , where x and y are real numbers, then find the values of x and y.

Solution We have

$$
4 x + i (3 x - y) = 3 + i (- 6)\tag{... (1}
$$

Equating the real and the imaginary parts of (1), we get

$$
4 x = 3, 3 x - y = - 6,
$$

which, on solving simultaneously, give $x = \frac{3}{4}$ and $y = \frac{33}{4}$.

## 4.3 Algebra of Complex Numbers

In this Section, we shall develop the algebra of complex numbers.

4.3.1 Addition of two complex numbers Let $z_{1} = a + ib$ and $z_{2} = c + id$ be any two complex numbers. Then, the sum $z_{1} + z_{2}$ is defined as follows:

$z_{1} + z_{2} = (a + c) + i(b + d)$, which is again a complex number.

For example, $(2 + i3) + (-6 + i5) = (2 - 6) + i(3 + 5) = -4 + i8$

The addition of complex numbers satisfy the following properties:

(i) The closure law The sum of two complex numbers is a complex number, i.e., $z_{1} + z_{2}$ is a complex number for all complex numbers $z_{1}$ and $z_{2}$.

(ii) The commutative law For any two complex numbers  $z_{1}$  and  $z_{2}$ ,  $z_{1} + z_{2} = z_{2} + z_{1}$

(iii) The associative law For any three complex numbers  $z_{1}, z_{2}, z_{3}, (z_{1} + z_{2}) + z_{3} = z_{1} + (z_{2} + z_{3})$ .

(iv) The existence of additive identity There exists the complex number $0 + i0$ (denoted as 0), called the additive identity or the zero complex number, such that, for every complex number $z, z + 0 = z$.

(v) The existence of additive inverse To every complex number $z = a + ib$, we have the complex number $-a + i(-b)$ (denoted as $-z$), called the additive inverse or negative of $z$. We observe that $z + (-z) = 0$ (the additive identity).

4.3.2 Difference of two complex numbers Given any two complex numbers $z_{1}$ and $z_{2}$, the difference $z_{1} - z_{2}$ is defined as follows:

$$
z _ {1} - z _ {2} = z _ {1} + (- z _ {2}).
$$

For example,

$$
(6 + 3 i) - (2 - i) = (6 + 3 i) + (- 2 + i) = 4 + 4 i
$$

and

$$
(2 - i) - (6 + 3 i) = (2 - i) + (- 6 - 3 i) = - 4 - 4 i
$$

Reprint 2025-26

<!-- page 3 of 13 -->

78

MATHEMATICS

4.3.3 Multiplication of two complex numbers Let $z_{1} = a + ib$ and $z_{2} = c + id$ be any two complex numbers. Then, the product $z_{1}z_{2}$ is defined as follows:

$$
z _ {1} z _ {2} = (a c - b d) + i (a d + b c)
$$

For example, $(3 + i5)(2 + i6) = (3\times 2 - 5\times 6) + i(3\times 6 + 5\times 2) = -24 + i28$

The multiplication of complex numbers possesses the following properties, which we state without proofs.

(i) The closure law The product of two complex numbers is a complex number, the product $z_{1}z_{2}$ is a complex number for all complex numbers $z_{1}$ and $z_{2}$.

(ii) The commutative law For any two complex numbers $z_{1}$ and $z_{2}$,

$$
z _ {1} z _ {2} = z _ {2} z _ {1}
$$

(iii) The associative law For any three complex numbers $z_{1}, z_{2}, z_{3}$,

$$
(z _ {1} z _ {2}) z _ {3} = z _ {1} (z _ {2} z _ {3}).
$$

(iv) The existence of multiplicative identity There exists the complex number $1 + i0$ (denoted as 1), called the multiplicative identity such that $z.1 = z$, for every complex number $z$.

(v) The existence of multiplicative inverse For every non-zero complex number $z = a + ib$ or $a + bi (a \neq 0, b \neq 0)$, we have the complex number $\frac{a}{a^2 + b^2} + i\frac{-b}{a^2 + b^2}$ (denoted by $\frac{1}{z}$ or $z^{-1}$), called the multiplicative inverse of $z$ such that

$z.\frac{1}{z}=1$  (the multiplicative identity).

(vi) The distributive law For any three complex numbers $z_{1}, z_{2}, z_{3}$,

(a) $z_{1}(z_{2} + z_{3}) = z_{1}z_{2} + z_{1}z_{3}$

(b) $(z_{1} + z_{2})z_{3} = z_{1}z_{3} + z_{2}z_{3}$

4.3.4 Division of two complex numbers Given any two complex numbers $z_{1}$ and $z_{2}$,

where $z_{2} \neq 0$, the quotient $\frac{z_1}{z_2}$ is defined by

$$
\frac {z _ {1}}{z _ {2}} = z _ {1} \frac {1}{z _ {2}}
$$

For example, let $z_{1} = 6 + 3i$ and $z_{2} = 2 - i$

Then

$$
\frac {z _ {1}}{z _ {2}} = \left((6 + 3 i) \times \frac {1}{2 - i}\right) = (6 + 3 i) \left(\frac {2}{2 ^ {2} + (- 1) ^ {2}} + i \frac {- (- 1)}{2 ^ {2} + (- 1) ^ {2}}\right)
$$

Reprint 2025-26

<!-- page 4 of 13 -->

COMPLEX NUMBERS AND QUADRATIC EQUATIONS

79

$$
= (6 + 3 i) \left(\frac {2 + i}{5}\right) = \frac {1}{5} [ 1 2 - 3 + i (6 + 6) ] = \frac {1}{5} (9 + 1 2 i)
$$

## 4.3.5 Power of $i$ we know that

$$
\left| i ^ {3} = i ^ {2} i = (- 1) i = - i, \quad i ^ {4} = \left(i ^ {2}\right) ^ {2} = (- 1) ^ {2} = 1 \right|
$$

$$
i ^ {5} = \left(i ^ {2}\right) ^ {2} i = (- 1) ^ {2} i = i, \quad i ^ {6} = \left(i ^ {2}\right) ^ {3} = (- 1) ^ {3} = - 1, \text {etc.}
$$

Also, we have

$$
i ^ {- 1} = \frac {1}{i} \times \frac {i}{i} = \frac {i}{- 1} = - i, \quad i ^ {- 2} = \frac {1}{i ^ {2}} = \frac {1}{- 1} = - 1,
$$

$$
i ^ {- 3} = \frac {1}{i ^ {3}} = \frac {1}{- i} \times \frac {i}{i} = \frac {i}{1} = i, \quad i ^ {- 4} = \frac {1}{i ^ {4}} = \frac {1}{1} = 1
$$

In general, for any integer $k$, $i^{4k} = 1$, $i^{4k + 1} = i$, $i^{4k + 2} = -1$, $i^{4k + 3} = -i$

## 4.3.6 The square roots of a negative real number

Note that $i^2 = -1$ and $(-i)^2 = i^2 = -1$

Therefore, the square roots of $-1$ are $i, -i$. However, by the symbol $\sqrt{-1}$, we would mean $i$ only.

Now, we can see that $i$ and $-i$ both are the solutions of the equation $x^{2} + 1 = 0$ or $x^{2} = -1$.

Similarly

$$
\left(\sqrt {3} i\right) ^ {2} = \left(\sqrt {3}\right) ^ {2} i ^ {2} = 3 (- 1) = - 3
$$

$$
\left(- \sqrt {3} i\right) ^ {2} = \left(- \sqrt {3}\right) ^ {2} i ^ {2} = - 3
$$

Therefore, the square roots of $-3$ are $\sqrt{3} i$ and $-\sqrt{3} i$.

Again, the symbol $\sqrt{-3}$ is meant to represent $\sqrt{3}i$ only, i.e., $\sqrt{-3} = \sqrt{3}i$.

Generally, if $a$ is a positive real number, $\sqrt{-a} = \sqrt{a}\sqrt{-1} = \sqrt{a} i$,

We already know that $\sqrt{a} \times \sqrt{b} = \sqrt{ab}$ for all positive real number $a$ and $b$. This result also holds true when either $a > 0$, $b < 0$ or $a < 0$, $b > 0$. What if $a < 0$, $b < 0$? Let us examine.

Note that

Reprint 2025-26

<!-- page 5 of 13 -->

80

MATHEMATICS

$i^2 = \sqrt{-1}\sqrt{-1} = \sqrt{(-1)(-1)}$ (by assuming $\sqrt{a}\times \sqrt{b} = \sqrt{ab}$ for all real numbers) $= \sqrt{1} = 1$ , which is a contradiction to the fact that $i^2 = -1$

Therefore, $\sqrt{a} \times \sqrt{b} \neq \sqrt{ab}$ if both $a$ and $b$ are negative real numbers.

Further, if any of $a$ and $b$ is zero, then, clearly, $\sqrt{a} \times \sqrt{b} = \sqrt{ab} = 0$.

4.3.7 Identities We prove the following identity

$\left(z_{1} + z_{2}\right)^{2} = z_{1}^{2} + z_{2}^{2} + 2z_{1}z_{2}$, for all complex numbers $z_{1}$ and $z_{2}$.

Proof We have, $(z_{1} + z_{2})^{2} = (z_{1} + z_{2})(z_{1} + z_{2}),$ $= (z_{1} + z_{2})z_{1} + (z_{1} + z_{2})z_{2}$ $= z_1^2 +z_2z_1 + z_1z_2 + z_2^2$ $= z_{1}^{2} + z_{1}z_{2} + z_{1}z_{2} + z_{2}^{2}$ $= z_{1}^{2} + 2z_{1}z_{2} + z_{2}^{2}$

(Distributive law)

(Distributive law)

(Commutative law of multiplication)

Similarly, we can prove the following identities:

(i) $\left(z_{1} - z_{2}\right)^{2} = z_{1}^{2} - 2z_{1}z_{2} + z_{2}^{2}$

(ii) $\left(z_{1} + z_{2}\right)^{3} = z_{1}^{3} + 3z_{1}^{2}z_{2} + 3z_{1}z_{2}^{2} + z_{2}^{3}$

(iii) $\left(z_{1} - z_{2}\right)^{3} = z_{1}^{3} - 3z_{1}^{2}z_{2} + 3z_{1}z_{2}^{2} - z_{2}^{3}$

(iv) $z_{1}^{2} - z_{2}^{2} = \left(z_{1} + z_{2}\right)\left(z_{1} - z_{2}\right)$

In fact, many other identities which are true for all real numbers, can be proved to be true for all complex numbers.

Example 2 Express the following in the form of $a + bi$:

$$
(- 5 i) \left(\frac {1}{8} i\right) \tag {i}
$$

$$
\left| (- i) (2 i) \left(- \frac {1}{8} i\right) ^ {3} \right|
$$

Solution (i) $(-5i)\left(\frac{1}{8} i\right) = \frac{-5}{8} i^2 = \frac{-5}{8} (-1) = \frac{5}{8} = \frac{5}{8} + i0$

(ii) $(-i)(2i)\left(-\frac{1}{8} i\right)^3 = 2 \times \frac{1}{8 \times 8 \times 8} \times i^5 = \frac{1}{256}\left(i^2\right)^2 i = \frac{1}{256} i.$

Reprint 2025-26

<!-- page 6 of 13 -->

COMPLEX NUMBERS AND QUADRATIC EQUATIONS

81

Example 3 Express $(5 - 3i)^{3}$ in the form $a + ib$.

Solution We have, $(5 - 3i)^{3} = 5^{3} - 3 \times 5^{2} \times (3i) + 3 \times 5(3i)^{2} - (3i)^{3}$ $= 125 - 225i - 135 + 27i = -10 - 198i.$

Example 4 Express $\left(-\sqrt{3} +\sqrt{-2}\right)\left(2\sqrt{3} -i\right)$ in the form of $a + ib$

Solution We have,

$$
\begin{array}{r l} \left(- \sqrt {3} + \sqrt {- 2}\right) \left(2 \sqrt {3} - i\right) & = \left(- \sqrt {3} + \sqrt {2}   i\right) \left(2 \sqrt {3} - i\right) \\ & = - 6 + \sqrt {3} i + 2 \sqrt {6} i - \sqrt {2}   i ^ {2} = \left(- 6 + \sqrt {2}\right) + \sqrt {3} \left(1 + 2 \sqrt {2}\right) i \end{array}
$$

## 4.4 The Modulus and the Conjugate of a Complex Number

Let $z = a + ib$ be a complex number. Then, the modulus of $z$, denoted by $|z|$, is defined to be the non-negative real number $\sqrt{a^2 + b^2}$, i.e., $|z| = \sqrt{a^2 + b^2}$ and the conjugate of $z$, denoted as $\bar{z}$, is the complex number $a - ib$, i.e., $\bar{z} = a - ib$.

For example,

$$
\left| 3 + i \right| = \sqrt {3 ^ {2} + 1 ^ {2}} = \sqrt {1 0}, \left| 2 - 5 i \right| = \sqrt {2 ^ {2} + (- 5) ^ {2}} = \sqrt {2 9},
$$

and

$$
\overline {{3 + i}} = 3 - i, \overline {{2 - 5 i}} = 2 + 5 i, \overline {{- 3 i - 5}} = 3 i - 5
$$

Observe that the multiplicative inverse of the non-zero complex number z is given by

$$
z ^ {- 1} = \frac {1}{a + i b} = \frac {a}{a ^ {2} + b ^ {2}} + i \frac {- b}{a ^ {2} + b ^ {2}} = \frac {a - i b}{a ^ {2} + b ^ {2}} = \frac {\bar {z}}{| z | ^ {2}}
$$

or

$$
z \overline {{z}} = \left| z \right| ^ {2}
$$

Furthermore, the following results can easily be derived.

For any two complex numbers $z_{1}$ and $z_{2}$, we have

(i)

$$
\left| \begin{array}{c c} z _ {1} & z _ {2} \end{array} \right| = \left| \begin{array}{c} z _ {1} \end{array} \right| \left| \begin{array}{c} z _ {2} \end{array} \right|\tag{ii}
$$

$$
\left| \frac {z _ {1}}{z _ {2}} \right| = \frac {\left| z _ {1} \right|}{\left| z _ {2} \right|} \text {provided} \left| z _ {2} \right| \neq 0
$$

(iii)

$$
\overline {{z _ {1} z _ {2}}} = \overline {{z _ {1}}} \overline {{z _ {2}}}
$$

(iv)

$$
\overline {{z _ {1} \pm z _ {2}}} = \overline {{z _ {1}}} \pm \overline {{z _ {2}}} (\mathrm{v}) \overline {{\left(\frac {z _ {1}}{z _ {2}}\right)}} = \frac {\overline {{z _ {1}}}}{\overline {{z _ {2}}}} \text {provided} z _ {2} \neq 0.
$$

Reprint 2025-26

<!-- page 7 of 13 -->

82

MATHEMATICS

Example 5 Find the multiplicative inverse of $2 - 3i$.

Solution Let $z = 2 - 3i$

Then  $\overline{z}=2+3i$  and  $\left|z\right|^{2}=2^{2}+(-3)^{2}=13$

Therefore, the multiplicative inverse of $2 - 3i$ is given by

$$
z ^ {- 1} = \frac {\bar {z}}{| z | ^ {2}} = \frac {2 + 3 i}{1 3} = \frac {2}{1 3} + \frac {3}{1 3} i
$$

The above working can be reproduced in the following manner also,

$$
z ^ {- 1} = \frac {1}{2 - 3 i} = \frac {2 + 3 i}{(2 - 3 i) (2 + 3 i)}
$$

$$
= \frac {2 + 3 i}{2 ^ {2} - (3 i) ^ {2}} = \frac {2 + 3 i}{1 3} = \frac {2}{1 3} + \frac {3}{1 3} i
$$

Example 6 Express the following in the form $a + ib$

(i)  $\frac{5+\sqrt{2}i}{1-\sqrt{2}i}$

(ii) $i^{-35}$

Solution (i) We have, $\frac{5 + \sqrt{2}i}{1 - \sqrt{2}i} = \frac{5 + \sqrt{2}i}{1 - \sqrt{2}i}\times \frac{1 + \sqrt{2}i}{1 + \sqrt{2}i} = \frac{5 + 5\sqrt{2}i + \sqrt{2}i - 2}{1 - (\sqrt{2}i)^2}$

$$
= \frac {3 + 6 \sqrt {2} i}{1 + 2} = \frac {3 (1 + 2 \sqrt {2} i)}{3} = 1 + 2 \sqrt {2} i.
$$

$$
i ^ {- 3 5} = \frac {1}{i ^ {3 5}} = \frac {1}{\left(i ^ {2}\right) ^ {1 7} i} = \frac {1}{- i} \times \frac {i}{i} = \frac {i}{- i ^ {2}} = i
$$

## EXERCISE 4.1

Express each of the complex number given in the Exercises 1 to 10 in the form $a + ib$.  
1. $(5i)\left(-\frac{3}{5}i\right)$  
2. $i^{9} + i^{19}$  
3. $i^{-39}$

Reprint 2025-26

<!-- page 8 of 13 -->

COMPLEX NUMBERS AND QUADRATIC EQUATIONS

83

4. $3(7 + i7) + i(7 + i7)$ 5. $(1 - i) - (-1 + i6)$  
6. $\left(\frac{1}{5} + i\frac{2}{5}\right) - \left(4 + i\frac{5}{2}\right)$ 7. $\left[\left(\frac{1}{3} + i\frac{7}{3}\right) + \left(4 + i\frac{1}{3}\right)\right] - \left(-\frac{4}{3} + i\right)$  
8. $(1 - i)^4$ 9. $\left(\frac{1}{3} + 3i\right)^3$ 10. $\left(-2 - \frac{1}{3}i\right)^3$

Find the multiplicative inverse of each of the complex numbers given in the Exercises 11 to 13.

11. $4 - 3i$ 12. $\sqrt{5} + 3i$ 13. $-i$

14. Express the following expression in the form of $a + ib$:

$$
\frac {\left(3 + i \sqrt {5}\right) \left(3 - i \sqrt {5}\right)}{\left(\sqrt {3} + \sqrt {2} i\right) - \left(\sqrt {3} - i \sqrt {2}\right)}
$$

## 4.5 Argand Plane and Polar Representation

We already know that corresponding to each ordered pair of real numbers $(x,y)$, we get a unique point in the XY-plane and vice-versa with reference to a set of mutually perpendicular lines known as the $x$-axis and the $y$-axis. The complex number $x + iy$ which corresponds to the ordered pair $(x,y)$ can be represented geometrically as the unique point $\mathrm{P}(x,y)$ in the XY-plane and vice-versa.

![Image block](doc:a0f0ab4/tier:standard/page:8/block:10)

Some complex numbers such as $2 + 4i, -2 + 3i, 0 + 1i, 2 + 0i, -5 - 2i$ and $1 - 2i$ which correspond to the ordered

Fig 4.1

pairs (2, 4), (-2, 3), (0, 1), (2, 0), (-5, -2), and (1, -2), respectively, have been represented geometrically by the points A, B, C, D, E, and F, respectively in the Fig 4.1.

The plane having a complex number assigned to each of its point is called the complex plane or the Argand plane.

Reprint 2025-26

<!-- page 9 of 13 -->

84

MATHEMATICS

Obviously, in the Argand plane, the modulus of the complex number

$x + iy = \sqrt{x^2 + y^2}$ is the distance between the point $\mathrm{P}(x,y)$ and the origin O (0, 0) (Fig 4.2). The points on the $x$-axis corresponds to the complex numbers of the form $a + i$ 0 and the points on the $y$-axis corresponds to the complex numbers of the form

![Image block](doc:a0f0ab4/tier:standard/page:9/block:5)

$0 + i b$. The $x$-axis and $y$-axis in the Argand plane are called, respectively, the real axis and the imaginary axis.

The representation of a complex number $z = x + iy$ and its conjugate $z = x - iy$ in the Argand plane are, respectively, the points $P(x, y)$ and $Q(x, -y)$.

Geometrically, the point $(x, -y)$ is the mirror image of the point $(x, y)$ on the real axis (Fig 4.3).

![Image block](doc:a0f0ab4/tier:standard/page:9/block:9)

Fig 4.3

Reprint 2025-26

<!-- page 10 of 13 -->

COMPLEX NUMBERS AND QUADRATIC EQUATIONS

85

## Miscellaneous Examples

Example 7 Find the conjugate of $\frac{(3 - 2i)(2 + 3i)}{(1 + 2i)(2 - i)}$.

Solution We have, $\frac{(3 - 2i)(2 + 3i)}{(1 + 2i)(2 - i)}$  
$= \frac{6 + 9i - 4i + 6}{2 - i + 4i + 2} = \frac{12 + 5i}{4 + 3i} \times \frac{4 - 3i}{4 - 3i}$  
$= \frac{48 - 36i + 20i + 15}{16 + 9} = \frac{63 - 16i}{25} = \frac{63}{25} - \frac{16}{25}i$

Therefore, conjugate of  $\frac{(3-2i)(2+3i)}{(1+2i)(2-i)}$  is  $\frac{63}{25}+\frac{16}{25}i$ .

Example 8 If $x + iy = \frac{a + ib}{a - ib}$, prove that $x^2 + y^2 = 1$.

Solution We have,

$$
x + i y = \frac {(a + i b) (a + i b)}{(a - i b) (a + i b)} = \frac {a ^ {2} - b ^ {2} + 2 a b i}{a ^ {2} + b ^ {2}} = \frac {a ^ {2} - b ^ {2}}{a ^ {2} + b ^ {2}} + \frac {2 a b}{a ^ {2} + b ^ {2}} i
$$

So that, $x - iy = \frac{a^2 - b^2}{a^2 + b^2} -\frac{2ab}{a^2 + b^2} i$

Therefore,

$$
x ^ {2} + y ^ {2} = (x + i y) (x - i y) = \frac {(a ^ {2} - b ^ {2}) ^ {2}}{(a ^ {2} + b ^ {2}) ^ {2}} + \frac {4 a ^ {2} b ^ {2}}{(a ^ {2} + b ^ {2}) ^ {2}} = \frac {(a ^ {2} + b ^ {2}) ^ {2}}{(a ^ {2} + b ^ {2}) ^ {2}} = 1
$$

## Miscellaneous Exercise on Chapter 4

1. Evaluate: $\left[i^{18} + \left(\frac{1}{i}\right)^{25}\right]^3$.

2. For any two complex numbers $z_{1}$ and $z_{2}$, prove that $\operatorname{Re}(z_1 z_2) = \operatorname{Re} z_1 \operatorname{Re} z_2 - \operatorname{Im} z_1 \operatorname{Im} z_2$.

Reprint 2025-26

<!-- page 11 of 13 -->

86

MATHEMATICS

3. Reduce $\left(\frac{1}{1 - 4i} -\frac{2}{1 + i}\right)\left(\frac{3 - 4i}{5 + i}\right)$ to the standard form.

4. If $x - iy = \sqrt{\frac{a - ib}{c - id}}$ prove that $\left(x^{2} + y^{2}\right)^{2} = \frac{a^{2} + b^{2}}{c^{2} + d^{2}}$.

5. If $z_{1} = 2 - i, z_{2} = 1 + i$, find $\left|\frac{z_1 + z_2 + 1}{z_1 - z_2 + 1}\right|$.

6. If $a + ib = \frac{(x + i)^2}{2x^2 + 1}$, prove that $a^2 + b^2 = \frac{(x^2 + 1)^2}{(2x^2 + 1)^2}$.

7. Let $z_{1} = 2 - i, z_{2} = -2 + i$. Find (i) $\operatorname{Re}\left(\frac{z_1 z_2}{\overline{z}_1}\right)$, (ii) $\operatorname{Im}\left(\frac{1}{z_1 \overline{z}_1}\right)$.

8. Find the real numbers $x$ and $y$ if $(x - iy)(3 + 5i)$ is the conjugate of $-6 - 24i$.

9. Find the modulus of $\frac{1 + i}{1 - i} = \frac{1 - i}{1 + i}$.

10. If $(x + iy)^3 = u + iv$, then show that $\frac{u}{x} + \frac{v}{y} = 4(x^2 - y^2)$.

11. If $\alpha$ and $\beta$ are different complex numbers with $|\beta| = 1$, then find $\left|\frac{\beta - \alpha}{1 - \overline{\alpha}\beta}\right|$.

12. Find the number of non-zero integral solutions of the equation $\left|1 - i\right|^x = 2^x$

13. If $(a + ib)(c + id)(e + if)(g + ih) = A + iB$, then show that $(a^2 + b^2)(c^2 + d^2)(e^2 + f^2)(g^2 + h^2) = A^2 + B^2$

14. If $\left(\frac{1 + i}{1 - i}\right)^m = 1$, then find the least positive integral value of $m$.

Reprint 2025-26

<!-- page 12 of 13 -->

COMPLEX NUMBERS AND QUADRATIC EQUATIONS

87

## Summary

A number of the form $a + ib$, where $a$ and $b$ are real numbers, is called a complex number, $a$ is called the real part and $b$ is called the imaginary part of the complex number.

Let $z_{1} = a + ib$ and $z_{2} = c + id$. Then

(i) $z_{1} + z_{2} = (a + c) + i(b + d)$

(ii) $z_{1}z_{2} = (ac - bd) + i(ad + bc)$

For any non-zero complex number $z = a + ib$ ($a \neq 0, b \neq 0$), there exists the complex number $\frac{a}{a^2 + b^2} + i\frac{-b}{a^2 + b^2}$, denoted by $\frac{1}{z}$ or $z^{-1}$, called the multiplicative inverse of $z$ such that $(a + ib) \frac{a}{a^2 + b^2} + i\frac{-b}{a^2 + b^2} = 1 + i0 = 1$

For any integer $k$, $i^{4k} = 1$, $i^{4k + 1} = i$, $i^{4k + 2} = -1$, $i^{4k + 3} = -i$

The conjugate of the complex number $z = a + ib$, denoted by $\overline{z}$, is given by $\overline{z} = a - ib$.

## Historical Note

The fact that square root of a negative number does not exist in the real number system was recognised by the Greeks. But the credit goes to the Indian mathematician Mahavira (850) who first stated this difficulty clearly. “He mentions in his work ‘Ganitasara Sangraha’ as in the nature of things a negative (quantity) is not a square (quantity)’, it has, therefore, no square root”. Bhaskara, another Indian mathematician, also writes in his work Bijaganita, written in 1150. “There is no square root of a negative quantity, for it is not a square.” Cardan (1545) considered the problem of solving

$$
x + y = 1 0, x y = 4 0.
$$

Reprint 2025-26

<!-- page 13 of 13 -->

88

MATHEMATICS

He obtained  $x = 5 + \sqrt{-15}$  and  $y = 5 - \sqrt{-15}$  as the solution of it, which was discarded by him by saying that these numbers are ‘useless’. Albert Girard (about 1625) accepted square root of negative numbers and said that this will enable us to get as many roots as the degree of the polynomial equation. Euler was the first to introduce the symbol i for  $\sqrt{-1}$  and W.R. Hamilton (about 1830) regarded the complex number  $a + ib$  as an ordered pair of real numbers  $(a, b)$  thus giving it a purely mathematical definition and avoiding use of the so called ‘imaginary numbers’.

Reprint 2025-26