<!-- page 1 of 8 -->

The image provided is a QR code. As per the instructions, I am to process text and non-textual graphical content that can be extracted from it. Therefore, no textual content can be extracted or converted according to the given instructions.

Chapter

12080CH08

8

# APPLICATION OF INTEGRALS

One should study Mathematics because it is only through Mathematics that nature can be conceived in harmonious form. – BIRKHOFF

## 8.1 Introduction

In geometry, we have learnt formulae to calculate areas of various geometrical figures including triangles, rectangles, trapezias and circles. Such formulae are fundamental in the applications of mathematics to many real life problems. The formulae of elementary geometry allow us to calculate areas of many simple figures. However, they are inadequate for calculating the areas enclosed by curves. For that we shall need some concepts of Integral Calculus.

In the previous chapter, we have studied to find the area bounded by the curve  $y = f(x)$ , the ordinates x = a, x = b and x-axis, while calculating definite integral as the limit of a sum. Here, in this chapter, we shall study a specific application of integrals to find the area under simple curves, area between lines and arcs of circles, parabolas and ellipses (standard forms only). We shall also deal with finding the area bounded by the above said curves.

## 8.2 Area under Simple Curves

![Image block](doc:bd56cce/tier:standard/page:1/block:11)

A.L. Cauchy (1789-1857)

In the previous chapter, we have studied definite integral as the limit of a sum and how to evaluate definite integral using Fundamental Theorem of Calculus. Now, we consider the easy and intuitive way of finding the area bounded by the curve  $y = f(x)$ , x-axis and the ordinates x = a and x = b. From Fig 8.1, we can think of area under the curve as composed of large number of very thin vertical strips. Consider an arbitrary strip of height y and width dx, then dA (area of the elementary strip) = ydx, where,  $y = f(x)$ .

![Chart block](doc:bd56cce/tier:standard/page:1/block:14)

Reprint 2025-26

<!-- page 2 of 8 -->

APPLICATION OF INTEGRALS

293

This area is called the elementary area which is located at an arbitrary position within the region which is specified by some value of $x$ between $a$ and $b$. We can think of the total area $A$ of the region between $x$-axis, ordinates $x = a$, $x = b$ and the curve $y = f(x)$ as the result of adding up the elementary areas of thin strips across the region

PQRSTP. Symbolically, we express

$$
\mathrm{A} = \int_ {a} ^ {b} d \mathrm{A} = \int_ {a} ^ {b} y d x = \int_ {a} ^ {b} f (x) d x
$$

The area A of the region bounded by the curve $x = g(y)$, $y$-axis and the lines $y = c$, $y = d$ is given by

$$
\mathrm{A} = \int_ {c} ^ {d} x d y = \int_ {c} ^ {d} g (y) d y
$$

![Image block](doc:bd56cce/tier:standard/page:2/block:8)

Here, we consider horizontal strips as shown in the Fig 8.2

Fig 8.2

Remark If the position of the curve under consideration is below the $x$-axis, then since $f(x) < 0$ from $x = a$ to $x = b$, as shown in Fig 8.3, the area bounded by the curve, $x$-axis and the ordinates $x = a$, $x = b$ come out to be negative. But, it is only the numerical value of the area which is taken into consideration. Thus, if the area is negative, we take its absolute value, i.e., $\left|\int_{a}^{b} f(x) dx\right|$.

![Image block](doc:bd56cce/tier:standard/page:2/block:12)

Generally, it may happen that some portion of the curve is above $x$-axis and some is below the $x$-axis as shown in the Fig 8.4. Here, $\mathrm{A}_1 < 0$ and $\mathrm{A}_2 > 0$. Therefore, the area $A$ bounded by the curve $y = f(x)$, $x$-axis and the ordinates $x = a$ and $x = b$ is given by $\mathrm{A} = |\mathrm{A}_1| + \mathrm{A}_2$.

Reprint 2025-26

<!-- page 3 of 8 -->

294

MATHEMATICS

![Image block](doc:bd56cce/tier:standard/page:3/block:3)

Fig 8.4

Example 1 Find the area enclosed by the circle $x^{2} + y^{2} = a^{2}$.

Solution From Fig 8.5, the whole area enclosed by the given circle

$= 4$ (area of the region AOBA bounded by the curve, $x$-axis and the ordinates $x = 0$ and $x = a$) [as the circle is symmetrical about both $x$-axis and $y$-axis]

$= 4\int_{0}^{a}ydx$ (taking vertical strips)

$$
= 4 \int_ {0} ^ {a} \sqrt {a ^ {2} - x ^ {2}} d x
$$

![Image block](doc:bd56cce/tier:standard/page:3/block:10)

Fig 8.5

Since $x^{2} + y^{2} = a^{2}$ gives $y = \pm \sqrt{a^2 - x^2}$

As the region AOBA lies in the first quadrant, $y$ is taken as positive. Integrating, we get the whole area enclosed by the given circle

$$
\begin{array}{l} = 4 \left[ \frac {x}{2} \sqrt {a ^ {2} - x ^ {2}} + \frac {a ^ {2}}{2} \sin^ {- 1} \frac {x}{a} \right] _ {0} ^ {a} \\ = 4 \left[ \left(\frac {a}{2} \times 0 + \frac {a ^ {2}}{2} \sin^ {- 1} 1\right) - 0 \right] = 4 \left(\frac {a ^ {2}}{2}\right) \left(\frac {\pi}{2}\right) = \pi a ^ {2} \end{array}
$$

Reprint 2025-26

<!-- page 4 of 8 -->

APPLICATION OF INTEGRALS

295

Alternatively, considering horizontal strips as shown in Fig 8.6, the whole area of the

region enclosed by circle

$$
\begin{array}{l} = 4 \int_ {0} ^ {a} x d y = 4 \int_ {0} ^ {a} \sqrt {a ^ {2} - y ^ {2}} d y \\ = 4 \left[ \frac {y}{2} \sqrt {a ^ {2} - y ^ {2}} + \frac {a ^ {2}}{2} \sin^ {- 1} \frac {y}{a} \right] _ {0} ^ {a} \\ = 4 \left[ \left(\frac {a}{2} \times 0 + \frac {a ^ {2}}{2} \sin^ {- 1} 1\right) - 0 \right] \\ = 4 \frac {a ^ {2}}{2} \frac {\pi}{2} = \pi a ^ {2} \end{array}
$$

(Why?)

![Image block](doc:bd56cce/tier:standard/page:4/block:7)

Fig 8.6

Example 2 Find the area enclosed by the ellipse $\frac{x^2}{a^2} +\frac{y^2}{b^2} = 1$

Solution From Fig 8.7, the area of the region ABA'B'A bounded by the ellipse

$$
= 4 \binom{\text {area of the region AOBA in the first quadrant bounded}}{\text {by the curve, $x - axis$ and the ordinates $x = 0, x = a$}}
$$

(as the ellipse is symmetrical about both $x$-axis and $y$-axis)

$= 4\int_{0}^{a}ydx$ (taking vertical strips)

Now $\frac{x^2}{a^2} +\frac{y^2}{b^2} = 1$ gives $y = \pm \frac{b}{a}\sqrt{a^2 - x^2}$, but as the region AOBA lies in the first quadrant, $y$ is taken as positive. So, the required area is

$$
\begin{array}{l} = 4 \int_ {0} ^ {a} \frac {b}{a} \sqrt {a ^ {2} - x ^ {2}} d x \\ = \frac {4 b}{a} \left[ \frac {x}{2} \sqrt {a ^ {2} - x ^ {2}} + \frac {a ^ {2}}{2} \sin^ {- 1} \frac {x}{a} \right] _ {0} ^ {a} \\ = \frac {4 b}{a} \left[ \left(\frac {a}{2} \times 0 + \frac {a ^ {2}}{2} \sin^ {- 1} 1\right) - 0 \right] \\ = \frac {4 b}{a} \frac {a ^ {2}}{2} \frac {\pi}{2} = \pi a b \end{array}
$$

(Why?)

![Image block](doc:bd56cce/tier:standard/page:4/block:17)

Fig 8.7

Reprint 2025-26

<!-- page 5 of 8 -->

296

MATHEMATICS

Alternatively, considering horizontal strips as shown in the Fig 8.8, the area of the ellipse is

$$
\begin{array}{l} = 4 \int_ {0} ^ {b} x d y = 4 \frac {a}{b} \int_ {0} ^ {b} \sqrt {b ^ {2} - y ^ {2}} d y (\text {Why?}) \\ = \frac {4 a}{b} \left[ \frac {y}{2} \sqrt {b ^ {2} - y ^ {2}} + \frac {b ^ {2}}{2} \sin^ {- 1} \frac {y}{b} \right] _ {0} ^ {b} \\ = \frac {4 a}{b} \left[ \left(\frac {b}{2} \times 0 + \frac {b ^ {2}}{2} \sin^ {- 1} 1\right) - 0 \right] \\ = \frac {4 a}{b} \frac {b ^ {2}}{2} \frac {\pi}{2} = \pi a b \end{array}
$$

![Image block](doc:bd56cce/tier:standard/page:5/block:5)

Fig 8.8

## EXERCISE 8.1

1. Find the area of the region bounded by the ellipse $\frac{x^2}{16} +\frac{y^2}{9} = 1$.

2. Find the area of the region bounded by the ellipse  $\frac{x^{2}}{4}+\frac{y^{2}}{9}=1$ .
Choose the correct answer in the following Exercises 3 and 4.

3. Area lying in the first quadrant and bounded by the circle $x^{2} + y^{2} = 4$ and the lines $x = 0$ and $x = 2$ is (A) $\pi$ (B) $\frac{\pi}{2}$ (C) $\frac{\pi}{3}$ (D) $\frac{\pi}{4}$

4. Area of the region bounded by the curve $y^{2} = 4x$, $y$-axis and the line $y = 3$ is (A) 2 (B) $\frac{9}{4}$ (C) $\frac{9}{3}$ (D) $\frac{9}{2}$

## Miscellaneous Examples

Example 3 Find the area of the region bounded by the line $y = 3x + 2$, the $x$-axis and the ordinates $x = -1$ and $x = 1$.

Reprint 2025-26

<!-- page 6 of 8 -->

APPLICATION OF INTEGRALS

297

Solution As shown in the Fig 8.9, the line $y = 3x + 2$ meets $x$-axis at $x = \frac{-2}{3}$ and its graph lies below $x$-axis for $x \in \left(-1, \frac{-2}{3}\right)$ and above $x$-axis for $x \in \left(\frac{-2}{3}, 1\right)$.

The required area = Area of the region ACBA + Area of the region ADEA

![Image block](doc:bd56cce/tier:standard/page:6/block:5)

$$
\begin{array}{l} = \left| \int_ {- 1} ^ {\frac {- 2}{3}} (3 x + 2) d x \right| + \int_ {\frac {- 2}{3}} ^ {1} (3 x + 2) d x \\ = \left| \left[ \frac {3 x ^ {2}}{2} + 2 x \right] _ {- 1} ^ {\frac {- 2}{3}} \right| + \left[ \frac {3 x ^ {2}}{2} + 2 x \right] _ {\frac {- 2}{3}} ^ {1} = \frac {1}{6} + \frac {2 5}{6} = \frac {1 3}{3} \end{array}
$$

Example 4 Find the area bounded by the curve $y = \cos x$ between $x = 0$ and $x = 2\pi$.

Solution From the Fig 8.10, the required area = area of the region OABO + area of the region BCDB + area of the region DEFD.

Fig 8.9

![Image block](doc:bd56cce/tier:standard/page:6/block:10)

Fig 8.10

Thus, we have the required area

$$
\begin{array}{l} = \int_ {0} ^ {\frac {\pi}{2}} \cos x d x + \left| \int_ {\frac {\pi}{2}} ^ {\frac {3 \pi}{2}} \cos x d x \right| + \int_ {\frac {3 \pi}{2}} ^ {2 \pi} \cos x d x \\ = \left[ \sin x \right] _ {0} ^ {\frac {\pi}{2}} + \left| \left[ \sin x \right] _ {\frac {\pi}{2}} ^ {\frac {3 \pi}{2}} \right| + \left[ \sin x \right] _ {\frac {3 \pi}{2}} ^ {2 \pi} \\ = 1 + 2 + 1 = 4 \end{array}
$$

Reprint 2025-26

<!-- page 7 of 8 -->

298

MATHEMATICS

## Miscellaneous Exercise on Chapter 8

1. Find the area under the given curves and given lines:
(i)  $y = x^{2}, x = 1, x = 2$  and x-axis
(ii)  $y = x^{4}, x = 1, x = 5$  and x-axis

2. Sketch the graph of $y = |x + 3|$ and evaluate $\int_{-6}^{0}|x + 3|dx$.

3. Find the area bounded by the curve $y = \sin x$ between $x = 0$ and $x = 2\pi$. Choose the correct answer in the following Exercises from 4 to 5.

4. Area bounded by the curve $y = x^3$, the $x$-axis and the ordinates $x = -2$ and $x = 1$ is (A) - 9 (B) $\frac{-15}{4}$ (C) $\frac{15}{4}$ (D) $\frac{17}{4}$

5. The area bounded by the curve $y = x|x|$, $x$-axis and the ordinates $x = -1$ and $x = 1$ is given by
(A) 0 (B) $\frac{1}{3}$ (C) $\frac{2}{3}$ (D) $\frac{4}{3}$

[Hint: $y = x^{2}$ if $x > 0$ and $y = -x^{2}$ if $x < 0$].]

## Summary

The area of the region bounded by the curve $y = f(x)$, $x$-axis and the lines $x = a$ and $x = b$ ($b > a$) is given by the formula: $\text{Area} = \int_{a}^{b} y dx = \int_{a}^{b} f(x) dx$.

The area of the region bounded by the curve $x = \phi(y)$, $y$-axis and the lines $y = c, y = d$ is given by the formula: $\text{Area} = \int_{c}^{d} x dy = \int_{c}^{d} \phi(y) dy$.

## Historical Note

The origin of the Integral Calculus goes back to the early period of development of Mathematics and it is related to the method of exhaustion developed by the mathematicians of ancient Greece. This method arose in the solution of problems on calculating areas of plane figures, surface areas and volumes of solid bodies etc. In this sense, the method of exhaustion can be regarded as an early method

Reprint 2025-26

<!-- page 8 of 8 -->

APPLICATION OF INTEGRALS

299

of integration. The greatest development of method of exhaustion in the early period was obtained in the works of Eudoxus (440 B.C.) and Archimedes (300 B.C.)

Systematic approach to the theory of Calculus began in the 17th century. In 1665, Newton began his work on the Calculus described by him as the theory of fluxions and used his theory in finding the tangent and radius of curvature at any point on a curve. Newton introduced the basic notion of inverse function called the anti derivative (indefinite integral) or the inverse method of tangents.

During 1684-86, Leibnitz published an article in the Acta Eruditorum which he called Calculas summatorius, since it was connected with the summation of a number of infinitely small areas, whose sum, he indicated by the symbol ‘∫’. In 1696, he followed a suggestion made by J. Bernoulli and changed this article to Calculus integrali. This corresponded to Newton’s inverse method of tangents.

Both Newton and Leibnitz adopted quite independent lines of approach which was radically different. However, respective theories accomplished results that were practically identical. Leibnitz used the notion of definite integral and what is quite certain is that he first clearly appreciated tie up between the antiderivative and the definite integral.

Conclusively, the fundamental concepts and theory of Integral Calculus and primarily its relationships with Differential Calculus were developed in the work of P.de Fermat, I. Newton and G. Leibnitz at the end of 17th century. However, this justification by the concept of limit was only developed in the works of A.L. Cauchy in the early 19th century. Lastly, it is worth mentioning the following quotation by Lie Sophie's:

“It may be said that the conceptions of differential quotient and integral which in their origin certainly go back to Archimedes were introduced in Science by the investigations of Kepler, Descartes, Cavalieri, Fermat and Wallis .... The discovery that differentiation and integration are inverse operations belongs to Newton and Leibnitz”.

Reprint 2025-26