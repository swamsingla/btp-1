<!-- page 1 of 38 -->

The image provided is a QR code. As per the instructions, I am to process text and non-textual content that can be extracted from it. Therefore, no textual content can be output for OCR.

12080CH09

Chapter

9

# DIFFERENTIAL EQUATIONS

He who seeks for methods without having a definite problem in mind seeks for the most part in vain. – D. HILBERT

## 9.1 Introduction

In Class XI and in Chapter 5 of the present book, we discussed how to differentiate a given function $f$ with respect to an independent variable, i.e., how to find $f'(x)$ for a given function $f$ at each $x$ in its domain of definition. Further, in the chapter on Integral Calculus, we discussed how to find a function $f$ whose derivative is the function $g$, which may also be formulated as follows:

For a given function $g$, find a function $f$ such that

$$
\frac {d y}{d x} = g (x), \text {where} y = f (x)\tag{... (1}
$$

![Image block](doc:26f26d5/tier:standard/page:1/block:11)

Henri Poincare (1854-1912)

An equation of the form (1) is known as a differential equation. A formal definition will be given later.

These equations arise in a variety of applications, may it be in Physics, Chemistry, Biology, Anthropology, Geology, Economics etc. Hence, an indepth study of differential equations has assumed prime importance in all modern scientific investigations.

In this chapter, we will study some basic concepts related to differential equation, general and particular solutions of a differential equation, formation of differential equations, some methods to solve a first order - first degree differential equation and some applications of differential equations in different areas.

## 9.2 Basic Concepts

We are already familiar with the equations of the type:

$$
x ^ {2} - 3 x + 3 = 0\tag{... (1}
$$

$$
\sin x + \cos x = 0\tag{... (2}
$$

$$
x + y = 7\tag{... (3}
$$

Reprint 2025-26

<!-- page 2 of 38 -->

DIFFERENTIAL EQUATIONS

301

Let us consider the equation:

$$
x \frac {d y}{d x} + y = 0\tag{... (4}
$$

We see that equations (1), (2) and (3) involve independent and/or dependent variable (variables) only but equation (4) involves variables as well as derivative of the dependent variable $y$ with respect to the independent variable $x$. Such an equation is called a differential equation.

In general, an equation involving derivative (derivatives) of the dependent variable with respect to independent variable (variables) is called a differential equation.

A differential equation involving derivatives of the dependent variable with respect to only one independent variable is called an ordinary differential equation, e.g.,

$$
2 \frac {d ^ {2} y}{d x ^ {2}} + \left(\frac {d y}{d x}\right) ^ {3} = 0 \text {is an ordinary differential equation}\tag{.... (5}
$$

Of course, there are differential equations involving derivatives with respect to more than one independent variables, called partial differential equations but at this stage we shall confine ourselves to the study of ordinary differential equations only. Now onward, we will use the term ‘differential equation’ for ‘ordinary differential equation’.

## Note

1. We shall prefer to use the following notations for derivatives:

$$
\frac {d y}{d x} = y ^ {\prime}, \frac {d ^ {2} y}{d x ^ {2}} = y ^ {\prime \prime}, \frac {d ^ {3} y}{d x ^ {3}} = y ^ {\prime \prime \prime}
$$

2. For derivatives of higher order, it will be inconvenient to use so many dashes

as supersuffix therefore, we use the notation $y_{n}$ for $n$th order derivative $\frac{d^n y}{dx^n}$.

## 9.2.1. Order of a differential equation

Order of a differential equation is defined as the order of the highest order derivative of the dependent variable with respect to the independent variable involved in the given differential equation.

Consider the following differential equations:

$$
\frac {d y}{d x} = e ^ {x}\tag{... (6}
$$

Reprint 2025-26

<!-- page 3 of 38 -->

302

MATHEMATICS

$$
\frac {d ^ {2} y}{d x ^ {2}} + y = 0\tag{... (7}
$$

$$
\left(\frac {d ^ {3} y}{d x ^ {3}}\right) + x ^ {2} \left(\frac {d ^ {2} y}{d x ^ {2}}\right) ^ {3} = 0\tag{... (8}
$$

The equations (6), (7) and (8) involve the highest derivative of first, second and third order respectively. Therefore, the order of these equations are 1, 2 and 3 respectively.

## 9.2.2 Degree of a differential equation

To study the degree of a differential equation, the key point is that the differential equation must be a polynomial equation in derivatives, i.e., $y', y'', y'''$ etc. Consider the following differential equations:

$$
\frac {d ^ {3} y}{d x ^ {3}} + 2 \left(\frac {d ^ {2} y}{d x ^ {2}}\right) ^ {2} - \frac {d y}{d x} + y = 0\tag{... (9}
$$

$$
\left(\frac {d y}{d x}\right) ^ {2} + \left(\frac {d y}{d x}\right) - \sin^ {2} y = 0\tag{... (10}
$$

$$
\frac {d y}{d x} + \sin \left(\frac {d y}{d x}\right) = 0\tag{... (11}
$$

We observe that equation (9) is a polynomial equation in  $y'''$ ,  $y''$  and  $y'$ , equation (10) is a polynomial equation in  $y'$  (not a polynomial in y though). Degree of such differential equations can be defined. But equation (11) is not a polynomial equation in  $y'$  and degree of such a differential equation can not be defined.

By the degree of a differential equation, when it is a polynomial equation in derivatives, we mean the highest power (positive integral index) of the highest order derivative involved in the given differential equation.

In view of the above definition, one may observe that differential equations (6), (7), (8) and (9) each are of degree one, equation (10) is of degree two while the degree of differential equation (11) is not defined.

Note Order and degree (if defined) of a differential equation are always positive integers.

Reprint 2025-26

<!-- page 4 of 38 -->

DIFFERENTIAL EQUATIONS

303

Example 1 Find the order and degree, if defined, of each of the following differential equations:
(i)  $\frac{dy}{dx}-\cos x=0$ 
(ii)  $xy\frac{d^{2}y}{dx^{2}}+x\left(\frac{dy}{dx}\right)^{2}-y\frac{dy}{dx}=0$

(iii) $y^{\prime \prime \prime} + y^{2} + e^{y^{\prime}} = 0$

## Solution

(i) The highest order derivative present in the differential equation is  $\frac{dy}{dx}$ , so its order is one. It is a polynomial equation in  $y'$  and the highest power raised to  $\frac{dy}{dx}$  is one, so its degree is one.

(ii) The highest order derivative present in the given differential equation is $\frac{d^2y}{dx^2}$, so its order is two. It is a polynomial equation in $\frac{d^2y}{dx^2}$ and $\frac{dy}{dx}$ and the highest power raised to $\frac{d^2y}{dx^2}$ is one, so its degree is one.

(iii) The highest order derivative present in the differential equation is $y''$, so its order is three. The given differential equation is not a polynomial equation in its derivatives and so its degree is not defined.

## EXERCISE 9.1

Determine order and degree (if defined) of differential equations given in Exercises 1 to 10.

1. $\frac{d^{4}y}{dx^{4}}+\sin(y^{\prime\prime})=0$ 2. $y^{\prime}+5y=0$ 3. $\left(\frac{ds}{dt}\right)^{4}+3s\frac{d^{2}s}{dt^{2}}=0$

4. $\left(\frac{d^{2}y}{dx^{2}}\right)^{2}+\cos\left(\frac{dy}{dx}\right)=0$ 5. $\frac{d^{2}y}{dx^{2}}=\cos3x+\sin3x$

6. $(y^{\prime\prime})^{2}+(y^{\prime\prime})^{3}+(y^{\prime})^{4}+y^{5}=0$ 7. $y^{\prime\prime\prime}+2y^{\prime\prime}+y^{\prime}=0$

Reprint 2025-26

<!-- page 5 of 38 -->

304

MATHEMATICS

8. $y^{\prime} + y = e^{x}$ 9. $y'' + (y')^{2} + 2y = 0$ 10. $y'' + 2y' + \sin y = 0$

11. The degree of the differential equation $\left(\frac{d^2y}{dx^2}\right)^3 +\left(\frac{dy}{dx}\right)^2 +\sin \left(\frac{dy}{dx}\right) + 1 = 0$ is (A) 3 (B) 2 (C) 1 (D) not defined

12. The order of the differential equation $2x^{2}\frac{d^{2}y}{dx^{2}} - 3\frac{dy}{dx} + y = 0$ is (A) 2 (B) 1 (C) 0 (D) not defined

## 9.3. General and Particular Solutions of a Differential Equation

In earlier Classes, we have solved the equations of the type:

$$
x ^ {2} + 1 = 0\tag{... (1}
$$

$$
\sin^ {2} x - \cos x = 0\tag{... (2}
$$

Solution of equations (1) and (2) are numbers, real or complex, that will satisfy the given equation i.e., when that number is substituted for the unknown x in the given equation, L.H.S. becomes equal to the R.H.S..

Now consider the differential equation $\frac{d^2y}{dx^2} + y = 0$

... (3)

In contrast to the first two equations, the solution of this differential equation is a function $\phi$ that will satisfy it i.e., when the function $\phi$ is substituted for the unknown $y$ (dependent variable) in the given differential equation, L.H.S. becomes equal to R.H.S..

The curve $y = \phi(x)$ is called the solution curve (integral curve) of the given differential equation. Consider the function given by

$$
y = \phi (x) = a \sin (x + b),\tag{... (4}
$$

where $a, b \in \mathbf{R}$. When this function and its derivative are substituted in equation (3), L.H.S. = R.H.S.. So it is a solution of the differential equation (3).

Let $a$ and $b$ be given some particular values say $a = 2$ and $b = \frac{\pi}{4}$, then we get a

function

$$
y = \phi_ {1} (x) = 2 \sin \left(x + \frac {\pi}{4}\right)\tag{... (5}
$$

When this function and its derivative are substituted in equation (3) again L.H.S. = R.H.S.. Therefore  $\phi_{1}$  is also a solution of equation (3).

Reprint 2025-26

<!-- page 6 of 38 -->

DIFFERENTIAL EQUATIONS

305

Function  $\phi$  consists of two arbitrary constants (parameters) a, b and it is called general solution of the given differential equation. Whereas function  $\phi_{1}$  contains no arbitrary constants but only the particular values of the parameters a and b and hence is called a particular solution of the given differential equation.

The solution which contains arbitrary constants is called the general solution (primitive) of the differential equation.

The solution free from arbitrary constants i.e., the solution obtained from the general solution by giving particular values to the arbitrary constants is called a particular solution of the differential equation.

Example 2 Verify that the function $y = e^{-3x}$ is a solution of the differential equation

$$
\frac {d ^ {2} y}{d x ^ {2}} + \frac {d y}{d x} - 6 y = 0
$$

Solution Given function is $y = e^{-3x}$. Differentiating both sides of equation with respect to $x$, we get

$$
\frac {d y}{d x} = - 3 e ^ {- 3 x}\tag{... (1}
$$

Now, differentiating (1) with respect to $x$, we have

$$
\frac {d ^ {2} y}{d x ^ {2}} = 9 e ^ {- 3 x}
$$

Substituting the values of $\frac{d^2y}{dx^2},\frac{dy}{dx}$ and $y$ in the given differential equation, we get L.H.S. $= 9e^{-3x} + (-3e^{-3x}) - 6.e^{-3x} = 9e^{-3x} - 9e^{-3x} = 0 = \mathrm{R.H.S.}$.

Therefore, the given function is a solution of the given differential equation.

Example 3 Verify that the function $y = a \cos x + b \sin x$, where, $a, b \in \mathbf{R}$ is a solution of the differential equation $\frac{d^2y}{dx^2} + y = 0$

Solution The given function is

$$
y = a \cos x + b \sin x\tag{... (1}
$$

Differentiating both sides of equation (1) with respect to $x$, successively, we get

$$
\frac {d y}{d x} = - a \sin x + b \cos x
$$

$$
\frac {d ^ {2} y}{d x ^ {2}} = - a \cos x - b \sin x
$$

Reprint 2025-26

<!-- page 7 of 38 -->

306

MATHEMATICS

Substituting the values of $\frac{d^2y}{dx^2}$ and $y$ in the given differential equation, we get

L.H.S. $= (-a\cos x - b\sin x) + (a\cos x + b\sin x) = 0 = \mathrm{R.H.S}.$

Therefore, the given function is a solution of the given differential equation.

## EXERCISE 9.2

In each of the Exercises 1 to 10 verify that the given functions (explicit or implicit) is a solution of the corresponding differential equation:

1. $y = e^{x} + 1$

: $y'' - y' = 0$

2. $y = x^{2} + 2x + C$

$y^{\prime} - 2x - 2 = 0$

3. $y = \cos x + C$

$: y^{\prime} + \sin x = 0$

4. $y = \sqrt{1 + x^2}$

$:y^{\prime} = \frac{xy}{1 + x^{2}}$

5. $y = Ax$

: $xy' = y (x \neq 0)$

6. $y = x\sin x$ : $xy^{\prime} = y + x\sqrt{x^{2} - y^{2}}$ ($x \neq 0$ and $x > y$ or $x < -y$)

7. $xy = \log y + C$

$$
y ^ {\prime} = \frac {y ^ {2}}{1 - x y} (x y \neq 1)
$$

8. $y - \cos y = x$

$$
(y \sin y + \cos y + x) y ^ {\prime} = y
$$

9. $x + y = \tan^{-1}y$

$$
y ^ {2} y ^ {\prime} + y ^ {2} + 1 = 0
$$

10. $y = \sqrt{a^2 - x^2} x\in (-a,a):x + y\frac{dy}{dx} = 0(y\neq 0)$

11. The number of arbitrary constants in the general solution of a differential equation of fourth order are:
(A) 0 (B) 2 (C) 3 (D) 4

12. The number of arbitrary constants in the particular solution of a differential equation of third order are:
(A) 3 (B) 2 (C) 1 (D) 0

9.4. Methods of Solving First Order, First Degree Differential Equations In this section we shall discuss three methods of solving first order first degree differential equations.

## 9.4.1 Differential equations with variables separable

A first order-first degree differential equation is of the form

$$
\frac {d y}{d x} = \mathrm{F} (x, y)
$$

Reprint 2025-26

<!-- page 8 of 38 -->

DIFFERENTIAL EQUATIONS

307

If $F(x, y)$ can be expressed as a product $g(x) h(y)$, where, $g(x)$ is a function of $x$ and $h(y)$ is a function of $y$, then the differential equation (1) is said to be of variable separable type. The differential equation (1) then has the form

$$
\frac {d y}{d x} = h (y) \cdot g (x)\tag{... (2}
$$

If $h(y) \neq 0$, separating the variables, (2) can be rewritten as

$$
\frac {1}{h (y)} d y = g (x) d x\tag{... (3}
$$

Integrating both sides of (3), we get

$$
\int \frac {1}{h (y)} d y = \int g (x) d x\tag{... (4}
$$

Thus, (4) provides the solutions of given differential equation in the form

$$
\mathrm{H} (y) = \mathrm{G} (x) + \mathrm{C}
$$

Here, H (y) and G (x) are the anti derivatives of  $\frac{1}{h(y)}$  and  $g(x)$  respectively and C is the arbitrary constant.

Example 4 Find the general solution of the differential equation $\frac{dy}{dx} = \frac{x + 1}{2 - y}$, $(y \neq 2)$

Solution We have

$$
\frac {d y}{d x} = \frac {x + 1}{2 - y}\tag{... (1}
$$

Separating the variables in equation (1), we get

$$
(2 - y) d y = (x + 1) d x\tag{... (2}
$$

Integrating both sides of equation (2), we get

$$
\left| \int (2 - y) d y = \int (x + 1) d x \right|
$$

or

$$
2 y - \frac {y ^ {2}}{2} = \frac {x ^ {2}}{2} + x + \mathrm{C} _ {1}
$$

or

$$
\left| x ^ {2} + y ^ {2} + 2 x - 4 y + 2 \mathrm{C} _ {1} = 0 \right|
$$

or

$$
x ^ {2} + y ^ {2} + 2 x - 4 y + \mathrm{C} = 0, \text {where} \mathrm{C} = 2 \mathrm{C} _ {1}
$$

which is the general solution of equation (1).

Reprint 2025-26

<!-- page 9 of 38 -->

308

MATHEMATICS

Example 5 Find the general solution of the differential equation $\frac{dy}{dx} = \frac{1 + y^2}{1 + x^2}$.

Solution Since  $1 + y^{2} \neq 0$ , therefore separating the variables, the given differential equation can be written as

$$
\frac {d y}{1 + y ^ {2}} = \frac {d x}{1 + x ^ {2}}\tag{... (1}
$$

Integrating both sides of equation (1), we get

$$
\int \frac {d y}{1 + y ^ {2}} = \int \frac {d x}{1 + x ^ {2}}
$$

or

$$
\tan^ {- 1} y = \tan^ {- 1} x + C
$$

which is the general solution of equation (1).

Example 6 Find the particular solution of the differential equation $\frac{dy}{dx} = -4xy^2$ given that $y = 1$, when $x = 0$.

Solution If $y \neq 0$, the given differential equation can be written as

$$
\frac {d y}{y ^ {2}} = - 4 x d x\tag{... (1}
$$

Integrating both sides of equation (1), we get

$$
\int \frac {d y}{y ^ {2}} = - 4 \int x d x
$$

or

$$
- \frac {1}{y} = - 2 x ^ {2} + C
$$

or

$$
y = \frac {1}{2 x ^ {2} - \mathrm{C}}\tag{... (2}
$$

Substituting $y = 1$ and $x = 0$ in equation (2), we get, $C = -1$.

Now substituting the value of C in equation (2), we get the particular solution of the given differential equation as  $y=\frac{1}{2x^{2}+1}$ .

Example 7 Find the equation of the curve passing through the point (1, 1) whose differential equation is $x \, dy = (2x^2 + 1) \, dx$ ($x \neq 0$).

Reprint 2025-26

<!-- page 10 of 38 -->

DIFFERENTIAL EQUATIONS

309

Solution The given differential equation can be expressed as

$$
d y ^ {*} = \left(\frac {2 x ^ {2} + 1}{x}\right) d x ^ {*}
$$

or

$$
d y = \left(2 x + \frac {1}{x}\right) d x\tag{... (1}
$$

Integrating both sides of equation (1), we get

$$
\int d y = \int \left(2 x + \frac {1}{x}\right) d x
$$

or

$$
y = x ^ {2} + \log | x | + C\tag{... (2}
$$

Equation (2) represents the family of solution curves of the given differential equation but we are interested in finding the equation of a particular member of the family which passes through the point  $(1, 1)$ . Therefore substituting x = 1, y = 1 in equation (2), we get C = 0.

Now substituting the value of C in equation (2) we get the equation of the required curve as $y = x^{2} + \log |x|$.

Example 8 Find the equation of a curve passing through the point $(-2, 3)$, given that the slope of the tangent to the curve at any point $(x, y)$ is $\frac{2x}{y^2}$.

Solution We know that the slope of the tangent to a curve is given by $\frac{dy}{dx}$.

SO,

$$
\frac {d y}{d x} = \frac {2 x}{y ^ {2}}\tag{... (1}
$$

Separating the variables, equation (1) can be written as

$$
y ^ {2} d y = 2 x d x\tag{... (2}
$$

Integrating both sides of equation (2), we get

$$
\int y ^ {2} d y = \int 2 x d x
$$

or

$$
\frac {y ^ {3}}{3} = x ^ {2} + C\tag{... (3}
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">\* The notation $\frac{dy}{dx}$ due to Leibnitz is extremely flexible and useful in many calculation and formal transformations, where, we can deal with symbols $dy$ and $dx$ exactly as if they were ordinary numbers. By treating $dx$ and $dy$ like separate entities, we can give neater expressions to many calculations.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">Refer: Introduction to Calculus and Analysis, volume-I page 172, By Richard Courant, Fritz John Spinger – Verlog New York.</span></small>

Reprint 2025-26

<!-- page 11 of 38 -->

310

MATHEMATICS

Substituting $x = -2$, $y = 3$ in equation (3), we get $C = 5$.

Substituting the value of C in equation (3), we get the equation of the required curve as

$$
\frac {y ^ {3}}{3} = x ^ {2} + 5 \quad \text {or} \quad y = (3 x ^ {2} + 1 5) ^ {\frac {1}{3}}
$$

Example 9 In a bank, principal increases continuously at the rate of 5% per year. In how many years Rs 1000 double itself?

Solution Let $P$ be the principal at any time $t$. According to the given problem,

$$
\frac {d p}{d t} = \left(\frac {5}{1 0 0}\right) \times \mathrm{P}
$$

or

$$
\frac {d p}{d t} = \frac {\mathrm{P}}{2 0}\tag{... (1}
$$

separating the variables in equation (1), we get

$$
\frac {d p}{\mathrm{P}} = \frac {d t}{2 0}\tag{... (2}
$$

Integrating both sides of equation (2), we get

$$
\log \mathrm{P} = \frac {t}{2 0} + \mathrm{C}_1
$$

or

$$
\mathrm{P} = e ^ {\frac {t}{2 0}} \cdot e ^ {\mathrm{C} _ {1}}
$$

or

$$
\mathrm{P} = \mathrm{C} e ^ {\frac {t}{2 0}} \text {(where} e ^ {\mathrm{C} _ {1}} = \mathrm{C})\tag{... (3}
$$

Now

$$
\mathrm{P} = 1 0 0 0, \text {when} t = 0
$$

Substituting the values of P and t in (3), we get C = 1000. Therefore, equation (3), gives

$$
\mathrm{P} = 1 0 0 0 e ^ {\frac {t}{2 0}}
$$

Let $t$ years be the time required to double the principal. Then

$$
2 0 0 0 = 1 0 0 0 e ^ {\frac {t}{2 0}} \Rightarrow t = 2 0 \log_ {e} 2
$$

## EXERCISE 9.3

For each of the differential equations in Exercises 1 to 10, find the general solution:

$$
\frac {d y}{d x} = \frac {1 - \cos x}{1 + \cos x}
$$

$$
\frac {d y}{d x} = \sqrt {4 - y ^ {2}} (- 2 <   y <   2) \tag {2}
$$

Reprint 2025-26

<!-- page 12 of 38 -->

DIFFERENTIAL EQUATIONS

311

3. $\frac{dy}{dx} + y = 1 (y \neq 1)$ 4. $\sec^2 x \tan y dx + \sec^2 y \tan x dy = 0$

5. $(e^{x} + e^{-x})dy - (e^{x} - e^{-x})dx = 0$ 6. $\frac{dy}{dx} = (1 + x^2)(1 + y^2)$

7. $y\log ydx - xdy = 0$ 8. $x^{5}\frac{dy}{dx} = -y^{5}$

9. $\frac{dy}{dx} = \sin^{-1}x$ 10. $e^{x}\tan y dx + (1 - e^{x})\sec^{2}y dy = 0$

For each of the differential equations in Exercises 11 to 14, find a particular solution satisfying the given condition:

11. $(x^{3} + x^{2} + x + 1)\frac{dy}{dx} = 2x^{2} + x; y = 1$ when $x = 0$

12. $x(x^{2} - 1)\frac{dy}{dx} = 1; y = 0$ when $x = 2$

13.  $\cos\left(\frac{dy}{dx}\right)=a\quad(a\in\mathbf{R});y=1$  when x=0

14. $\frac{dy}{dx} = y\tan x;y = 1$ when $x = 0$

15. Find the equation of a curve passing through the point  $(0, 0)$  and whose differential equation is  $y' = e^{x} \sin x$ .

16. For the differential equation $xy \frac{dy}{dx} = (x + 2)(y + 2)$, find the solution curve passing through the point (1, -1).

17. Find the equation of a curve passing through the point $(0, -2)$ given that at any point $(x, y)$ on the curve, the product of the slope of its tangent and $y$ coordinate of the point is equal to the $x$ coordinate of the point.

18. At any point $(x, y)$ of a curve, the slope of the tangent is twice the slope of the line segment joining the point of contact to the point $(-4, -3)$. Find the equation of the curve given that it passes through $(-2, 1)$.

19. The volume of spherical balloon being inflated changes at a constant rate. If initially its radius is 3 units and after 3 seconds it is 6 units. Find the radius of balloon after t seconds.

Reprint 2025-26

<!-- page 13 of 38 -->

312

MATHEMATICS

20. In a bank, principal increases continuously at the rate of $r\%$ per year. Find the value of $r$ if Rs 100 double itself in 10 years ($\log_e 2 = 0.6931$).

21. In a bank, principal increases continuously at the rate of 5% per year. An amount of Rs 1000 is deposited with this bank, how much will it worth after 10 years ( $e^{0.5} = 1.648$ ).

22. In a culture, the bacteria count is 1,00,000. The number is increased by 10% in 2 hours. In how many hours will the count reach 2,00,000, if the rate of growth of bacteria is proportional to the number present?

23. The general solution of the differential equation $\frac{dy}{dx} = e^{x + y}$ is (A) $e^x + e^{-y} = C$ (B) $e^x + e^y = C$ (C) $e^{-x} + e^y = C$ (D) $e^{-x} + e^{-y} = C$

## 9.4.2 Homogeneous differential equations

Consider the following functions in $x$ and $y$

$$
\mathrm{F} _ {1} (x, y) = y ^ {2} + 2 x y, \quad \mathrm{F} _ {2} (x, y) = 2 x - 3 y,
$$

$$
\mathrm{F} _ {3} (x, y) = \cos \left(\frac {y}{x}\right), \quad \mathrm{F} _ {4} (x, y) = \sin x + \cos y
$$

If we replace $x$ and $y$ by $\lambda x$ and $\lambda y$ respectively in the above functions, for any nonzero constant $\lambda$, we get

$$
\mathrm{F} _ {1} (\lambda x, \lambda y) = \lambda^ {2} (y ^ {2} + 2 x y) = \lambda^ {2} \mathrm{F} _ {1} (x, y)
$$

$$
\mathrm{F} _ {2} (\lambda x, \lambda y) = \lambda (2 x - 3 y) = \lambda \mathrm{F} _ {2} (x, y)
$$

$$
\mathrm{F} _ {3} (\lambda x, \lambda y) = \cos \left(\frac {\lambda y}{\lambda x}\right) = \cos \left(\frac {y}{x}\right) = \lambda^ {0} \mathrm{F} _ {3} (x, y)
$$

$$
\mathrm{F} _ {4} (\lambda x, \lambda y) = \sin \lambda x + \cos \lambda y \neq \lambda^ {n} \mathrm{F} _ {4} (x, y), \text {for any} n \in \mathbf {N}
$$

Here, we observe that the functions  $F_{1}$ ,  $F_{2}$ ,  $F_{3}$  can be written in the form  $\mathrm{F}(\lambda x, \lambda y) = \lambda^{n} \mathrm{~F}(x, y)$  but  $F_{4}$  can not be written in this form. This leads to the following definition:

A function  $\mathrm{F}(x, y)$  is said to be homogeneous function of degree n if  $\mathrm{F}(\lambda x, \lambda y) = \lambda^{n} \mathrm{~F}(x, y)$  for any nonzero constant  $\lambda$ .

We note that in the above examples, $\mathrm{F}_1, \mathrm{F}_2, \mathrm{F}_3$ are homogeneous functions of degree 2, 1, 0 respectively but $\mathrm{F}_4$ is not a homogeneous function.

Reprint 2025-26

<!-- page 14 of 38 -->

DIFFERENTIAL EQUATIONS

313

We also observe that

$$
\mathrm{F} _ {1} (x, y) = x ^ {2} \left(\frac {y ^ {2}}{x ^ {2}} + \frac {2 y}{x}\right) = x ^ {2} h _ {1} \left(\frac {y}{x}\right)
$$

or

$$
\mathrm{F} _ {1} (x, y) = y ^ {2} \left(1 + \frac {2 x}{y}\right) = y ^ {2} h _ {2} \left(\frac {x}{y}\right)
$$

$$
\mathrm{F} _ {2} (x, y) = x ^ {1} \left(2 - \frac {3 y}{x}\right) = x ^ {1} h _ {3} \left(\frac {y}{x}\right)
$$

or

$$
\mathrm{F} _ {2} (x, y) = y ^ {1} \left(2 \frac {x}{y} - 3\right) = y ^ {1} h _ {4} \left(\frac {x}{y}\right)
$$

$$
\mathrm{F} _ {3} (x, y) = x ^ {0} \cos \left(\frac {y}{x}\right) = x ^ {0} h _ {5} \left(\frac {y}{x}\right)
$$

$$
\mathrm{F} _ {4} (x, y) \neq x ^ {n} h _ {6} \left(\frac {y}{x}\right), \text {for any} n \in \mathbf {N}
$$

or

$$
\mathrm{F} _ {4} (x, y) \neq y ^ {n} h _ {7} \left(\frac {x}{y}\right), \text {for any} n \in \mathbf {N}
$$

Therefore, a function $\mathrm{F}(x,y)$ is a homogeneous function of degree $n$ if

$$
\mathrm{F} (x, y) = x ^ {n} g \left(\frac {y}{x}\right) \quad \text {or} \quad y ^ {n} h \left(\frac {x}{y}\right)
$$

A differential equation of the form $\frac{dy}{dx} = F(x, y)$ is said to be homogenous if $F(x, y)$ is a homogenous function of degree zero.

To solve a homogeneous differential equation of the type

$$
\frac {d y}{d x} = \mathrm{F} (x, y) = g \left(\frac {y}{x}\right)\tag{... (1}
$$

We make the substitution

$$
y = v. x\tag{... (2}
$$

Differentiating equation (2) with respect to $x$, we get

$$
\frac {d y}{d x} = v + x \frac {d v}{d x}\tag{... (3}
$$

Substituting the value of $\frac{dy}{dx}$ from equation (3) in equation (1), we get

Reprint 2025-26

<!-- page 15 of 38 -->

314

MATHEMATICS

$$
v + x \frac {d v}{d x} = g (v)
$$

or

$$
x \frac {d v}{d x} = g (v) - v\tag{... (4}
$$

Separating the variables in equation (4), we get

$$
\frac {d v}{g (v) - v} = \frac {d x}{x}\tag{... (5}
$$

Integrating both sides of equation (5), we get

$$
\int \frac {d v}{g (v) - v} = \int \frac {1}{x} d x + C\tag{6}
$$

Equation (6) gives general solution (primitive) of the differential equation (1) when we replace v by  $\frac{y}{x}$ .

Note If the homogeneous differential equation is in the form $\frac{dx}{dy} = F(x, y)$ where, $F(x, y)$ is homogenous function of degree zero, then we make substitution $\frac{x}{y} = v$ i.e., $x = vy$ and we proceed further to find the general solution as discussed above by writing $\frac{dx}{dy} = F(x, y) = h\left(\frac{x}{y}\right)$.

Example 10 Show that the differential equation $(x - y)\frac{dy}{dx} = x + 2y$ is homogeneous and solve it.

Solution The given differential equation can be expressed as

$$
\frac {d y}{d x} = \frac {x + 2 y}{x - y}\tag{... (1}
$$

Let

$$
\mathrm{F} (x, y) = \frac {x + 2 y}{x - y}
$$

Now

$$
\mathrm{F} (\lambda x, \lambda y) = \frac {\lambda (x + 2 y)}{\lambda (x - y)} = \lambda^ {0} \cdot f (x, y)
$$

Reprint 2025-26

<!-- page 16 of 38 -->

DIFFERENTIAL EQUATIONS

315

Therefore, $\mathrm{F}(x,y)$ is a homogenous function of degree zero. So, the given differential equation is a homogenous differential equation.

Alternatively,

$$
\frac {d y}{d x} = \left(\frac {1 + \frac {2 y}{x}}{1 - \frac {y}{x}}\right) = g \left(\frac {y}{x}\right)\tag{... (2}
$$

R.H.S. of differential equation (2) is of the form $g\left(\frac{y}{x}\right)$ and so it is a homogeneous function of degree zero. Therefore, equation (1) is a homogeneous differential equation. To solve it we make the substitution

$$
y = v x\tag{... (3}
$$

Differentiating equation (3) with respect to, $x$ we get

$$
\frac {d y}{d x} = v + x \frac {d v}{d x}\tag{... (4}
$$

Substituting the value of $y$ and $\frac{dy}{dx}$ in equation (1) we get

$$
v + x \frac {d v}{d x} = \frac {1 + 2 v}{1 - v}
$$

or

$$
x \frac {d v}{d x} = \frac {1 + 2 v}{1 - v} - v\tag{or}
$$

$$
x \frac {d v}{d x} = \frac {v ^ {2} + v + 1}{1 - v}
$$

or

$$
\frac {v - 1}{v ^ {2} + v + 1} d v = \frac {- d x}{x}
$$

Integrating both sides of equation (5), we get

$$
\int \frac {v - 1}{v ^ {2} + v + 1} d v = - \int \frac {d x}{x}
$$

or

$$
\frac {1}{2} \int \frac {2 v + 1 - 3}{v ^ {2} + v + 1} d v = - \log | x | + C _ {1}
$$

Reprint 2025-26

<!-- page 17 of 38 -->

316

MATHEMATICS

or

$$
\frac {1}{2} \int \frac {2 v + 1}{v ^ {2} + v + 1} d v - \frac {3}{2} \int \frac {1}{v ^ {2} + v + 1} d v = - \log | x | + C _ {1}
$$

or

$$
\frac {1}{2} \log \left| v ^ {2} + v + 1 \right| - \frac {3}{2} \int \frac {1}{\left(v + \frac {1}{2}\right) ^ {2} + \left(\frac {\sqrt {3}}{2}\right) ^ {2}} d v = - \log | x | + C _ {1}
$$

or

$$
\frac {1}{2} \log \left| v ^ {2} + v + 1 \right| - \frac {3}{2}. \frac {2}{\sqrt {3}} \tan^ {- 1} \left(\frac {2 v + 1}{\sqrt {3}}\right) = - \log | x | + C _ {1}
$$

or

$$
\frac {1}{2} \log \left| v ^ {2} + v + 1 \right| + \frac {1}{2} \log x ^ {2} = \sqrt {3} \tan^ {- 1} \left(\frac {2 v + 1}{\sqrt {3}}\right) + C _ {1}\tag{Why?}
$$

Replacing $v$ by $\frac{y}{x}$, we get

or

$$
\frac {1}{2} \log \left| \frac {y ^ {2}}{x ^ {2}} + \frac {y}{x} + 1 \right| + \frac {1}{2} \log x ^ {2} = \sqrt {3} \tan^ {- 1} \left(\frac {2 y + x}{\sqrt {3} x}\right) + C _ {1}
$$

or

$$
\frac {1}{2} \log \left| \left(\frac {y ^ {2}}{x ^ {2}} + \frac {y}{x} + 1\right) x ^ {2} \right| = \sqrt {3} \tan^ {- 1} \left(\frac {2 y + x}{\sqrt {3} x}\right) + C _ {1}
$$

or

$$
\log \left| (y ^ {2} + x y + x ^ {2}) \right| = 2 \sqrt {3} \tan^ {- 1} \left(\frac {2 y + x}{\sqrt {3} x}\right) + 2 C _ {1}
$$

or

$$
\log \left| (x ^ {2} + x y + y ^ {2}) \right| = 2 \sqrt {3} \tan^ {- 1} \left(\frac {x + 2 y}{\sqrt {3} x}\right) + C
$$

which is the general solution of the differential equation (1)

Example 11 Show that the differential equation $x \cos \left( \frac{y}{x} \right) \frac{dy}{dx} = y \cos \left( \frac{y}{x} \right) + x$ is homogeneous and solve it.

Solution The given differential equation can be written as

$$
\frac {d y}{d x} = \frac {y \cos \left(\frac {y}{x}\right) + x}{x \cos \left(\frac {y}{x}\right)}\tag{... (1}
$$

Reprint 2025-26

<!-- page 18 of 38 -->

DIFFERENTIAL EQUATIONS

317

It is a differential equation of the form $\frac{dy}{dx} = \mathrm{F}(x,y)$.

Here

$$
\mathrm{F} (x, y) = \frac {y \cos \left(\frac {y}{x}\right) + x}{x \cos \left(\frac {y}{x}\right)}
$$

Replacing $x$ by $\lambda x$ and $y$ by $\lambda y$, we get

$$
\mathrm{F} (\lambda x, \lambda y) = \frac {\lambda [ y \cos \left(\frac {y}{x}\right) + x ]}{\lambda \left(x \cos \frac {y}{x}\right)} = \lambda^ {0} [ \mathrm{F} (x, y) ]
$$

Thus, $\mathrm{F}(x,y)$ is a homogeneous function of degree zero.

Therefore, the given differential equation is a homogeneous differential equation. To solve it we make the substitution

$$
y = v x\tag{... (2}
$$

Differentiating equation (2) with respect to $x$, we get

$$
\frac {d y}{d x} = v + x \frac {d v}{d x}\tag{... (3}
$$

Substituting the value of $y$ and $\frac{dy}{dx}$ in equation (1), we get

$$
v + x \frac {d v}{d x} = \frac {v \cos v + 1}{\cos v}
$$

or

$$
x \frac {d v}{d x} = \frac {v \cos v + 1}{\cos v} - v
$$

or

$$
\boxed {x \frac {d v}{d x} = \frac {1}{\cos v}}
$$

or

$$
\cos v d v = \frac {d x}{x}
$$

Therefore

$$
\int \cos v d v = \int \frac {1}{x} d x
$$

Reprint 2025-26

<!-- page 19 of 38 -->

318

MATHEMATICS

or

$$
\sin v = \log | x | + \log | C |
$$

or

$$
\sin v = \log | C x |
$$

Replacing $v$ by $\frac{y}{x}$, we get

$$
\sin \left(\frac {y}{x}\right) = \log | C x |
$$

which is the general solution of the differential equation (1).

Example 12 Show that the differential equation $2y e^{\frac{x}{y}} dx + \left( y - 2x e^{\frac{x}{y}} \right) dy = 0$ is homogeneous and find its particular solution, given that, $x = 0$ when $y = 1$.

Solution The given differential equation can be written as

$$
\frac {d x}{d y} = \frac {2 x e ^ {\frac {x}{y}} - y}{2 y e ^ {\frac {x}{y}}}\tag{... (1}
$$

Let

$$
\mathrm{F} (x, y) = \frac {2 x e ^ {y} - y}{2 y e ^ {\frac {x}{y}}}\left. \right\}
$$

Then

$$
\mathrm{F} (\lambda x, \lambda y) = \frac {\lambda \left(2 x e ^ {\frac {x}{y}} - y\right)}{\lambda \left(2 y e ^ {\frac {x}{y}}\right)} = \lambda^ {0} [ \mathrm{F} (x, y) ]
$$

Thus, $\mathrm{F}(x,y)$ is a homogeneous function of degree zero. Therefore, the given differential equation is a homogeneous differential equation.

To solve it, we make the substitution

$$
x = v y\tag{... (2}
$$

Differentiating equation (2) with respect to $y$, we get

$$
\frac {d x}{d y} = v + y \frac {d v}{d y}\left. \right|
$$

Reprint 2025-26

<!-- page 20 of 38 -->

DIFFERENTIAL EQUATIONS

319

Substituting the value of $x$ and $\frac{dx}{dy}$ in equation (1), we get

$$
v + y \frac {d v}{d y} = \frac {2 v e ^ {v} - 1}{2 e ^ {v}}\tag{or}
$$

$$
y \frac {d v}{d y} = \frac {2 v e ^ {v} - 1}{2 e ^ {v}} - v\tag{or}
$$

$$
y \frac {d v}{d y} = - \frac {1}{2 e ^ {v}}\tag{or}
$$

$$
\left| 2 e ^ {v} d v = \frac {- d y}{y} \right|\tag{or}
$$

$$
\int 2 e ^ {v} \cdot d v = - \int \frac {d y}{y}
$$

or

$$
2 e ^ {v} = - \log | y | + C
$$

and replacing $v$ by $\frac{x}{y}$, we get

$$
2 e ^ {\frac {x}{y}} + \log | y | = C\tag{... (3}
$$

Substituting $x = 0$ and $y = 1$ in equation (3), we get

$$
2 e ^ {0} + \log | 1 | = \mathrm{C} \Rightarrow \mathrm{C} = 2
$$

Substituting the value of $C$ in equation (3), we get

$$
2 e ^ {\frac {x}{y}} + \log | y | = 2
$$

which is the particular solution of the given differential equation.

Example 13 Show that the family of curves for which the slope of the tangent at any point $(x, y)$ on it is $\frac{x^2 + y^2}{2xy}$, is given by $x^2 - y^2 = cx$.

Solution We know that the slope of the tangent at any point on a curve is $\frac{dy}{dx}$.

Therefore,

$$
\frac {d y}{d x} = \frac {x ^ {2} + y ^ {2}}{2 x y}
$$

Reprint 2025-26

<!-- page 21 of 38 -->

320

MATHEMATICS

or

$$
\frac {d y}{d x} = \frac {1 + \frac {y ^ {2}}{x ^ {2}}}{\frac {2 y}{x}}\tag{... (1}
$$

Clearly, (1) is a homogenous differential equation. To solve it we make substitution

$$
y = v x
$$

Differentiating $y = vx$ with respect to $x$, we get

$$
\frac {d y}{d x} = v + x \frac {d v}{d x}
$$

or

$$
\left| v + x \frac {d v}{d x} = \frac {1 + v ^ {2}}{2 v} \right|
$$

or

$$
x \frac {d v}{d x} = \frac {1 - v ^ {2}}{2 v}
$$

$$
\frac {2 v}{1 - v ^ {2}} d v = \frac {d x}{x}
$$

or

$$
\frac {2 v}{v ^ {2} - 1} d v = - \frac {d x}{x}
$$

Therefore

$$
\int \frac {2 v}{v ^ {2} - 1} d v = - \int \frac {1}{x} d x
$$

or

$$
\log | v ^ {2} - 1 | = - \log | x | + \log | C _ {1} |
$$

or

$$
\log | (v ^ {2} - 1) (x) | = \log | C _ {1} |
$$

or

$$
(v ^ {2} - 1) x = \pm C _ {1}
$$

Replacing $v$ by $\frac{y}{x}$, we get

$$
\left(\frac {y ^ {2}}{x ^ {2}} - 1\right) x = \pm \mathrm{C} _ {1}\left. \right\vert
$$

or

$$
(y ^ {2} - x ^ {2}) = \pm \mathrm{C} _ {1} x \text {or} x ^ {2} - y ^ {2} = \mathrm{C} x
$$

Reprint 2025-26

<!-- page 22 of 38 -->

DIFFERENTIAL EQUATIONS

321

## EXERCISE 9.4

In each of the Exercises 1 to 10, show that the given differential equation is homogeneous and solve each of them.

1. $(x^{2} + xy)dy = (x^{2} + y^{2})dx$

2. $y^{\prime} = \frac{x + y}{x}$

3. $(x - y)dy - (x + y)dx = 0$

4. $(x^{2} - y^{2})dx + 2xydy = 0$

5. $x^{2}\frac{dy}{dx} = x^{2} - 2y^{2} + xy$

6. $x dy - y dx = \sqrt{x^2 + y^2} dx$

7. $\left\{x\cos \left(\frac{y}{x}\right) + y\sin \left(\frac{y}{x}\right)\right\} y dx = \left\{y\sin \left(\frac{y}{x}\right) - x\cos \left(\frac{y}{x}\right)\right\} x dy$

8. $x\frac{dy}{dx} - y + x\sin \left(\frac{y}{x}\right) = 0$

$$
y d x + x \log \left(\frac {y}{x}\right) d y - 2 x d y = 0
$$

10. $\left(1 + e^{\frac{x}{y}}\right)dx + e^{\frac{x}{y}}\left(1 - \frac{x}{y}\right)dy = 0$

For each of the differential equations in Exercises from 11 to 15, find the particular solution satisfying the given condition:

11. $(x + y)dy + (x - y)dx = 0;y = 1$ when $x = 1$

12. $x^{2}dy + (xy + y^{2})dx = 0;y = 1$ when $x = 1$

13. $\left[x\sin^2\left(\frac{y}{x}\right) - y\right]dx + xdy = 0; y = \frac{\pi}{4}$ when $x = 1$

14. $\frac{dy}{dx} -\frac{y}{x} +\sec \left(\frac{y}{x}\right) = 0;$ $y = 0$ when $x = 1$

15. $2xy + y^{2} - 2x^{2}\frac{dy}{dx} = 0$ ; $y = 2$ when $x = 1$

16. A homogeneous differential equation of the from $\frac{dx}{dy} = h\left(\frac{x}{y}\right)$ can be solved by making the substitution.
(A) $y = vx$ (B) $v = yx$ (C) $x = vy$ (D) $x = v$

Reprint 2025-26

<!-- page 23 of 38 -->

322

MATHEMATICS

17. Which of the following is a homogeneous differential equation?

(A) $(4x + 6y + 5)dy - (3y + 2x + 4)dx = 0$

(B) $(xy)dx - (x^{3} + y^{3})dy = 0$

(C) $(x^{3} + 2y^{2})dx + 2xydy = 0$

(D) $y^{2} \, dx + (x^{2} - xy - y^{2}) \, dy = 0$

## 9.4.3 Linear differential equations

A differential equation of the from

$$
\frac {d y}{d x} + \mathrm{Py} = \mathrm{Q}
$$

where, P and Q are constants or functions of $x$ only, is known as a first order linear differential equation. Some examples of the first order linear differential equation are

$$
\frac {d y}{d x} + y = \sin x
$$

$$
\frac {d y}{d x} + \left(\frac {1}{x}\right) y = e ^ {x}
$$

$$
\frac {d y}{d x} + \left(\frac {y}{x \log x}\right) = \frac {1}{x}\left. \right\vert
$$

Another form of first order linear differential equation is

$$
\frac {d x}{d y} + \mathrm{P} _ {1} x = \mathrm{Q} _ {1}
$$

where,  $P_{1}$  and  $Q_{1}$  are constants or functions of y only. Some examples of this type of differential equation are

$$
\frac {d x}{d y} + x = \cos y
$$

$$
\frac {d x}{d y} + \frac {- 2 x}{y} = y ^ {2} e ^ {- y}
$$

To solve the first order linear differential equation of the type

$$
\frac {d y}{d x} + \mathrm{Py} = \mathrm{Q}\tag{... (1}
$$

Multiply both sides of the equation by a function of $x$ say $g(x)$ to get

$$
g (x) \frac {d y}{d x} + \mathrm{P}. (g (x)) y = \mathrm{Q}. g (x)\tag{... (2}
$$

Reprint 2025-26

<!-- page 24 of 38 -->

DIFFERENTIAL EQUATIONS

323

Choose $g(x)$ in such a way that R.H.S. becomes a derivative of $y \cdot g(x)$.

$$
g (x) \frac {d y}{d x} + \mathrm{P}. g (x) y = \frac {d}{d x} [ y. g (x) ]\tag{i.e.}
$$

or

$$
g (x) \frac {d y}{d x} + \mathrm{P}. g (x) y = g (x) \frac {d y}{d x} + y g ^ {\prime} (x)
$$

⇒

$$
\mathrm{P}. g (x) = g ^ {\prime} (x)
$$

or

$$
\mathrm{P} = \frac {g ^ {\prime} (x)}{g (x)}
$$

Integrating both sides with respect to $x$, we get

$$
\int \mathrm{P} d x = \int \frac {g ^ {\prime} (x)}{g (x)} d x
$$

or

$$
\int \mathrm{P} \cdot d x = \log (g (x))
$$

or

$$
\mathrm{g} (x) = e ^ {\int \mathrm{P} d x}
$$

On multiplying the equation (1) by $g(x) = e^{\int \mathrm{P}dx}$, the L.H.S. becomes the derivative of some function of $x$ and $y$. This function $g(x) = e^{\int \mathrm{P}dx}$ is called Integrating Factor (I.F.) of the given differential equation.

Substituting the value of $g(x)$ in equation (2), we get

$$
e ^ {\int \mathrm{P} d x} \frac {d y}{d x} + \mathrm{P} e ^ {\int \mathrm{P} d x} y = \mathrm{Q} \cdot e ^ {\int \mathrm{P} d x}
$$

or

$$
\frac {d}{d x} \left(y e ^ {\int \mathrm{P} d x}\right) = Q e ^ {\int \mathrm{P} d x}
$$

Integrating both sides with respect to $x$, we get

$$
y \cdot e ^ {\int \mathrm{P} d x} = \int \left(\mathrm{Q}, e ^ {\int \mathrm{P} d x}\right) d x
$$

or

$$
y = e ^ {- \int P d x} \cdot \int \left(Q. e ^ {\int P d x}\right) d x + C
$$

which is the general solution of the differential equation.

Reprint 2025-26

<!-- page 25 of 38 -->

324

MATHEMATICS

## Steps involved to solve first order linear differential equation:

(i) Write the given differential equation in the form $\frac{dy}{dx} +\mathrm{Py} = \mathrm{Q}$ where P, Q are constants or functions of $x$ only.

(ii) Find the Integrating Factor (I.F) = $e^{\int \mathrm{P}_{dx}}$.

(iii) Write the solution of the given differential equation as

$$
y \left(\mathrm{I.F}\right) = \int \left(\mathrm{Q} \times \mathrm{I.F}\right) d x + \mathrm{C}
$$

In case, the first order linear differential equation is in the form $\frac{dx}{dy} + P_1x = Q_1$,

where,  $P_{1}$  and  $Q_{1}$  are constants or functions of y only. Then I.F =  $e^{P_{1}dy}$  and the solution of the differential equation is given by

$$
x. (\mathrm{I.F}) = \int \left(\mathrm{Q} _ {1} \times \mathrm{I.F}\right) d y + \mathrm{C}
$$

Example 14 Find the general solution of the differential equation $\frac{dy}{dx} - y = \cos x$.

Solution Given differential equation is of the form

$$
\frac {d y}{d x} + \mathrm{P} y = \mathrm{Q}, \text {where} \mathrm{P} = - 1 \text {and} \mathrm{Q} = \cos x
$$

Therefore

$$
\mathrm{I.F} = e ^ {\int - 1 d x} = e ^ {- x}
$$

Multiplying both sides of equation by I.F, we get

$$
e ^ {- x} \frac {d y}{d x} - e ^ {- x} y = e ^ {- x} \cos x
$$

or

$$
\frac {d y}{d x} \left(y e ^ {- x}\right) = e ^ {- x} \cos x
$$

On integrating both sides with respect to $x$, we get

... (1)

Let

$$
\begin{array}{r l} y e ^ {- x} & = \int e ^ {- x} \cos x d x + C \\ I & = \int e ^ {- x} \cos x d x \\ & = \cos x \left(\frac {e ^ {- x}}{- 1}\right) - \int (- \sin x) (- e ^ {- x}) d x \end{array}
$$

Reprint 2025-26

<!-- page 26 of 38 -->

DIFFERENTIAL EQUATIONS

325

$$
\begin{array}{l} = - \cos x e ^ {- x} - \int \sin x e ^ {- x} d x \\ = - \cos x e ^ {- x} - \left[ \sin x (- e ^ {- x}) - \int \cos x (- e ^ {- x}) d x \right] \\ = - \cos x e ^ {- x} + \sin x e ^ {- x} - \int \cos x e ^ {- x} d x \end{array}\tag{or}
$$

or

$$
\begin{array}{c} \mathrm{I} = - e ^ {- x} \cos x + \sin x e ^ {- x} - \mathrm{I} \\ 2 \mathrm{I} = (\sin x - \cos x) e ^ {- x} \end{array}\tag{or}
$$

$$
\mathrm{I} = \frac {(\sin x - \cos x) e ^ {- x}}{2}
$$

Substituting the value of I in equation (1), we get

$$
y e ^ {- x} = \left(\frac {\sin x - \cos x}{2}\right) e ^ {- x} + C
$$

or

$$
y = \left(\frac {\sin x - \cos x}{2}\right) + C e ^ {x}
$$

which is the general solution of the given differential equation.

Example 15 Find the general solution of the differential equation $x\frac{dy}{dx} + 2y = x^2 (x \neq 0)$. Solution The given differential equation is

$$
x \frac {d y}{d x} + 2 y = x ^ {2}\tag{... (1}
$$

Dividing both sides of equation (1) by $x$, we get

$$
\frac {d y}{d x} + \frac {2}{x} y = x
$$

which is a linear differential equation of the type $\frac{dy}{dx} +\mathrm{Py} = \mathrm{Q}$, where $\mathrm{P} = \frac{2}{x}$ and $\mathrm{Q} = x$.

So

$$
\mathrm{I.F} = e ^ {\int \frac {2}{x} d x} = e ^ {2 \log x} = e ^ {\log x ^ {2}} = x ^ {2} [ a s e ^ {\log f (x)} = f (x) ]
$$

Therefore, solution of the given equation is given by

$$
y \cdot x ^ {2} = \int (x) \left(x ^ {2}\right) d x + C = \int x ^ {3} d x + C
$$

or

$$
y = \frac {x ^ {2}}{4} + C x ^ {- 2}
$$

which is the general solution of the given differential equation.

Reprint 2025-26

<!-- page 27 of 38 -->

326

MATHEMATICS

Example 16 Find the general solution of the differential equation $y \, dx - (x + 2y^2) \, dy = 0$. Solution The given differential equation can be written as

$$
\frac {d x}{d y} - \frac {x}{y} = 2 y
$$

This is a linear differential equation of the type $\frac{dx}{dy} + P_1x = Q_1$, where $P_1 = -\frac{1}{y}$ and $Q_1 = 2y$. Therefore $I.F = e^{\int -\frac{1}{y} dy} = e^{-\log y} = e^{\log (y)^{-1}} = \frac{1}{y}$

Hence, the solution of the given differential equation is

$$
x \frac {1}{y} = \int (2 y) \left(\frac {1}{y}\right) d y + C
$$

or

$$
\frac {x}{y} = \int (2 d y) + C
$$

or

$$
\frac {x}{y} = 2 y + \mathrm{C}
$$

or

$$
x = 2 y ^ {2} + C y
$$

which is a general solution of the given differential equation.

Example 17 Find the particular solution of the differential equation

$$
\frac {d y}{d x} + y \cot x = 2 x + x ^ {2} \cot x (x \neq 0)
$$

given that $y = 0$ when $x = \frac{\pi}{2}$.

Solution The given equation is a linear differential equation of the type $\frac{dy}{dx} + Py = Q$, where $P = \cot x$ and $Q = 2x + x^2 \cot x$. Therefore

$$
\mathrm{I.F} = e ^ {\int \cot x d x} = e ^ {\log \sin x} = \sin x
$$

Hence, the solution of the differential equation is given by

$y.\sin x = \int (2x + x^{2}\cot x)\sin xdx + C$

Reprint 2025-26

<!-- page 28 of 38 -->

DIFFERENTIAL EQUATIONS

327

or

$$
y \sin x = \int 2 x \sin x d x + \int x ^ {2} \cos x d x + C\tag{or}
$$

$$
\left| y \sin x = \sin x \left(\frac {2 x ^ {2}}{2}\right) - \int \cos x \left(\frac {2 x ^ {2}}{2}\right) d x + \int x ^ {2} \cos x d x + C \right|\tag{or}
$$

$$
y \sin x = x ^ {2} \sin x - \int x ^ {2} \cos x d x + \int x ^ {2} \cos x d x + C\tag{or}
$$

$$
y \sin x = x ^ {2} \sin x + C\tag{... (1}
$$

Substituting $y = 0$ and $x = \frac{\pi}{2}$ in equation (1), we get

$$
0 = \left(\frac {\pi}{2}\right) ^ {2} \sin \left(\frac {\pi}{2}\right) + C
$$

or

$$
\mathrm{C} = \frac {- \pi^ {2}}{4}
$$

Substituting the value of $C$ in equation (1), we get

$$
y \sin x = x ^ {2} \sin x - \frac {\pi^ {2}}{4}
$$

or

$$
y = x ^ {2} - \frac {\pi^ {2}}{4 \sin x} (\sin x \neq 0)
$$

which is the particular solution of the given differential equation.

Example 18 Find the equation of a curve passing through the point  $(0, 1)$ . If the slope of the tangent to the curve at any point  $(x, y)$  is equal to the sum of the x coordinate (abscissa) and the product of the x coordinate and y coordinate (ordinate) of that point.

Solution We know that the slope of the tangent to the curve is $\frac{dy}{dx}$.

Therefore,

$$
\frac {d y}{d x} = x + x y
$$

or

$$
\frac {d y}{d x} - x y = x\tag{... (1}
$$

This is a linear differential equation of the type $\frac{dy}{dx} +\mathrm{Py} = \mathrm{Q}$, where $\mathrm{P} = -x$ and $\mathrm{Q} = x$.

Therefore,

$$
\mathrm{I.F} = e ^ {\int - x d x} = e ^ {\frac {- x ^ {2}}{2}}
$$

Reprint 2025-26

<!-- page 29 of 38 -->

328

MATHEMATICS

Hence, the solution of equation is given by

$$
y \cdot e ^ {\frac {- x ^ {2}}{2}} = \int (x) \left(e ^ {\frac {- x ^ {2}}{2}}\right) d x + C\tag{... (2}
$$

Let

$$
\mathrm{I} = \int (x) e ^ {\frac {- x ^ {2}}{2}} d x
$$

Let $\frac{-x^2}{2} = t$, then $-x dx = dt$ or $x dx = -dt$.

Therefore,

$$
\mathrm{I} = - \int e ^ {t} d t = - e ^ {t} = - e ^ {\frac {- x ^ {2}}{2}}
$$

Substituting the value of I in equation (2), we get

$$
y e ^ {\frac {- x ^ {2}}{2}} = - e ^ {\frac {- x ^ {2}}{2} + C}
$$

or

$$
y = - 1 + \mathrm{C} e ^ {\frac {x ^ {2}}{2}}\tag{3}
$$

Now (3) represents the equation of family of curves. But we are interested in finding a particular member of the family passing through $(0,1)$. Substituting $x = 0$ and $y = 1$ in equation (3) we get

$$
1 = - 1 + \mathrm{C}. e ^ {0} \text {or} \mathrm{C} = 2
$$

Substituting the value of $C$ in equation (3), we get

$$
y = - 1 + 2 e ^ {\frac {x ^ {2}}{2}}
$$

which is the equation of the required curve.

## EXERCISE 9.5

For each of the differential equations given in Exercises 1 to 12, find the general solution:

1. $\frac{dy}{dx} + 2y = \sin x$

2.

$$
\frac {d y}{d x} + 3 y = e ^ {- 2 x}
$$

$$
\frac {d y}{d x} + \frac {y}{x} = x ^ {2}
$$

4.  $\frac{dy}{dx} + (\sec x)y = \tan x\left(0 \leq x < \frac{\pi}{2}\right)$

5.

$$
\cos^ {2} x \frac {d y}{d x} + y = \tan x \left(0 \leq x <   \frac {\pi}{2}\right)
$$

6. $x\frac{dy}{dx} + 2y = x^2 \log x$  
7. $x \log x \frac{dy}{dx} + y = \frac{2}{x} \log x$

8. $(1 + x^{2})dy + 2xydx = \cot x dx (x\neq 0)$

Reprint 2025-26

<!-- page 30 of 38 -->

DIFFERENTIAL EQUATIONS

329

9. $x\frac{dy}{dx} + y - x + xy \cot x = 0 (x \neq 0)$ 10. $(x + y)\frac{dy}{dx} = 1$

11. $y \, dx + (x - y^2) \, dy = 0$  
12. $(x + 3y^2)\frac{dy}{dx} = y \, (y > 0)$.

For each of the differential equations given in Exercises 13 to 15, find a particular solution satisfying the given condition:

13. $\frac{dy}{dx} + 2y \tan x = \sin x; y = 0$ when $x = \frac{\pi}{3}$

14. $(1 + x^{2})\frac{dy}{dx} + 2xy = \frac{1}{1 + x^{2}}; y = 0$ when $x = 1$

15. $\frac{dy}{dx} - 3y\cot x = \sin 2x; y = 2$ when $x = \frac{\pi}{2}$

16. Find the equation of a curve passing through the origin given that the slope of the tangent to the curve at any point $(x, y)$ is equal to the sum of the coordinates of the point.

17. Find the equation of a curve passing through the point  $(0, 2)$  given that the sum of the coordinates of any point on the curve exceeds the magnitude of the slope of the tangent to the curve at that point by 5.

18. The Integrating Factor of the differential equation $x\frac{dy}{dx} - y = 2x^2$ is (A) $e^{-x}$ (B) $e^{-y}$ (C) $\frac{1}{x}$ (D) $x$

19. The Integrating Factor of the differential equation
 $(1-y^{2})\frac{dx}{dy}+yx=ay(-1<y<1)$  is
(A)  $\frac{1}{y^{2}-1}$  (B)  $\frac{1}{\sqrt{y^{2}-1}}$  (C)  $\frac{1}{1-y^{2}}$  (D)  $\frac{1}{\sqrt{1-y^{2}}}$

## Miscellaneous Examples

Example 19 Verify that the function $y = c_{1}e^{ax}\cos bx + c_{2}e^{ax}\sin bx$, where $c_{1}, c_{2}$ are arbitrary constants is a solution of the differential equation

$$
\frac {d ^ {2} y}{d x ^ {2}} - 2 a \frac {d y}{d x} + \left(a ^ {2} + b ^ {2}\right) y = 0
$$

Reprint 2025-26

<!-- page 31 of 38 -->

330

MATHEMATICS

Solution The given function is

$$
y = e ^ {a x} \left[ c _ {1} \cos b x + c _ {2} \sin b x \right]\tag{... (1}
$$

Differentiating both sides of equation (1) with respect to $x$, we get

$$
\frac {d y}{d x} = e ^ {a x} \left[ - b c _ {1} \sin b x + b c _ {2} \cos b x \right] + \left[ c _ {1} \cos b x + c _ {2} \sin b x \right] e ^ {a x} \cdot a
$$

or

$$
\frac {d y}{d x} = e ^ {a x} [ (b c _ {2} + a c _ {1}) \cos b x + (a c _ {2} - b c _ {1}) \sin b x ]\tag{... (2}
$$

Differentiating both sides of equation (2) with respect to $x$, we get

$$
\begin{array}{r l} \frac {d ^ {2} y}{d x ^ {2}} & = e ^ {a x} [ (b c _ {2} + a c _ {1}) (- b \sin b x) + (a c _ {2} - b c _ {1}) (b \cos b x) ] \\ & \quad + [ (b c _ {2} + a c _ {1}) \cos b x + (a c _ {2} - b c _ {1}) \sin b x ] e ^ {a x}. a \\ & = e ^ {a x} [ (a ^ {2} c _ {2} - 2 a b c _ {1} - b ^ {2} c _ {2}) \sin b x + (a ^ {2} c _ {1} + 2 a b c _ {2} - b ^ {2} c _ {1}) \cos b x ] \end{array}
$$

Substituting the values of $\frac{d^2y}{dx^2},\frac{dy}{dx}$ and $y$ in the given differential equation, we get

$$
\begin{array}{r l} \text {L.H.S.} & = e ^ {a x} [ a ^ {2} c _ {2} - 2 a b c _ {1} - b ^ {2} c _ {2}) \sin b x + (a ^ {2} c _ {1} + 2 a b c _ {2} - b ^ {2} c _ {1}) \cos b x ] \\ & \quad - 2 a e ^ {a x} [ (b c _ {2} + a c _ {1}) \cos b x + (a c _ {2} - b c _ {1}) \sin b x ] \\ & \quad + (a ^ {2} + b ^ {2}) e ^ {a x} [ c _ {1} \cos b x + c _ {2} \sin b x ] \\ & = e ^ {a x} \left[ \begin{array}{l} (a ^ {2} c _ {2} - 2 a b c _ {1} - b ^ {2} c _ {2} - 2 a ^ {2} c _ {2} + 2 a b c _ {1} + a ^ {2} c _ {2} + b ^ {2} c _ {2}) \sin b x \\ + (a ^ {2} c _ {1} + 2 a b c _ {2} - b ^ {2} c _ {1} - 2 a b c _ {2} - 2 a ^ {2} c _ {1} + a ^ {2} c _ {1} + b ^ {2} c _ {1}) \cos b x \end{array} \right] \\ & = e ^ {a x} [ 0 \times \sin b x + 0 \cos b x ] = e ^ {a x} \times 0 = 0 = \text {R.H.S.} \end{array}
$$

Hence, the given function is a solution of the given differential equation.

Example 20 Find the particular solution of the differential equation $\log \left(\frac{dy}{dx}\right) = 3x + 4y$ given that $y = 0$ when $x = 0$.

Solution The given differential equation can be written as

$$
\frac {d y}{d x} = e ^ {(3 x + 4 y)}
$$

Reprint 2025-26

<!-- page 32 of 38 -->

DIFFERENTIAL EQUATIONS

331

or

$$
\frac {d y}{d x} = e ^ {3 x}. e ^ {4 y}\tag{... (1}
$$

Separating the variables, we get

$$
\frac {d y}{e ^ {4 y}} = e ^ {3 x} d x
$$

Therefore

$$
\int e ^ {- 4 y} d y = \int e ^ {3 x} d x
$$

or

$$
\frac {e ^ {- 4 y}}{- 4} = \frac {e ^ {3 x}}{3} + C
$$

or

$$
4 e ^ {3 x} + 3 e ^ {- 4 y} + 1 2 \mathrm{C} = 0\tag{... (2}
$$

Substituting $x = 0$ and $y = 0$ in (2), we get

$$
4 + 3 + 1 2 \mathrm{C} = 0 \text {or} \mathrm{C} = \frac {- 7}{1 2}
$$

Substituting the value of $C$ in equation (2), we get

$$
4 e ^ {3 x} + 3 e ^ {- 4 y} - 7 = 0,
$$

which is a particular solution of the given differential equation.

Example 21 Solve the differential equation

$$
(x d y - y d x) y \sin \left(\frac {y}{x}\right) = (y d x + x d y) x \cos \left(\frac {y}{x}\right).
$$

Solution The given differential equation can be written as

$$
\left[ x y \sin \left(\frac {y}{x}\right) - x ^ {2} \cos \left(\frac {y}{x}\right) \right] d y = \left[ x y \cos \left(\frac {y}{x}\right) + y ^ {2} \sin \left(\frac {y}{x}\right) \right] d x
$$

or

$$
\frac {d y}{d x} = \frac {x y \cos \left(\frac {y}{x}\right) + y ^ {2} \sin \left(\frac {y}{x}\right)}{x y \sin \left(\frac {y}{x}\right) - x ^ {2} \cos \left(\frac {y}{x}\right)}
$$

Dividing numerator and denominator on RHS by $x^2$, we get

$$
\frac {d y}{d x} = \frac {\frac {y}{x} \cos \left(\frac {y}{x}\right) + \left(\frac {y ^ {2}}{x ^ {2}}\right) \sin \left(\frac {y}{x}\right)}{\frac {y}{x} \sin \left(\frac {y}{x}\right) - \cos \left(\frac {y}{x}\right)}\tag{... (1}
$$

Reprint 2025-26

<!-- page 33 of 38 -->

332

MATHEMATICS

Clearly, equation (1) is a homogeneous differential equation of the form $\frac{dy}{dx} = g\left(\frac{y}{x}\right)$. To solve it, we make the substitution

$$
y = v x\tag{... (2}
$$

or

$$
\frac {d y}{d x} = v + x \frac {d v}{d x}
$$

or

$$
\left| v + x \frac {d v}{d x} = \frac {v \cos v + v ^ {2} \sin v}{v \sin v - \cos v} \right|
$$

(using (1) and (2))

or

$$
x \frac {d v}{d x} = \frac {2 v \cos v}{v \sin v - \cos v}
$$

or

$$
\left(\frac {v \sin v - \cos v}{v \cos v}\right) d v = \frac {2 d x}{x}
$$

Therefore

$$
\int \left(\frac {v \sin v - \cos v}{v \cos v}\right) d v = 2 \int \frac {1}{x} d x
$$

or

$$
\int \tan v d v - \int \frac {1}{v} d v = 2 \int \frac {1}{x} d x
$$

or

$$
\log | \sec v | - \log | v | = 2 \log | x | + \log | C _ {1} |
$$

or

$$
\log \left| \frac {\sec v}{v x ^ {2}} \right| = \log \left| C _ {1} \right|
$$

or

$$
\frac {\sec v}{v x ^ {2}} = \pm C _ {1}\tag{... (3}
$$

Replacing $v$ by $\frac{y}{x}$ in equation (3), we get

$$
\frac {\sec \left(\frac {y}{x}\right)}{\left(\frac {y}{x}\right) (x ^ {2})} = \mathrm{C} \text {where,} \mathrm{C} = \pm \mathrm{C} _ {1}
$$

or

$$
\sec \left(\frac {y}{x}\right) = \mathrm{C} x y
$$

which is the general solution of the given differential equation.

Reprint 2025-26

<!-- page 34 of 38 -->

DIFFERENTIAL EQUATIONS

333

Example 22 Solve the differential equation

$$
(\tan^ {- 1} y - x) d y = (1 + y ^ {2}) d x.
$$

Solution The given differential equation can be written as

$$
\frac {d x}{d y} + \frac {x}{1 + y ^ {2}} = \frac {\tan^ {- 1} y}{1 + y ^ {2}}\tag{... (1}
$$

Now (1) is a linear differential equation of the form $\frac{dx}{dy} +\mathrm{P}_1x = \mathrm{Q}_1,$

where,  $P_{1}=\frac{1}{1+y^{2}}$  and  $Q_{1}=\frac{\tan^{-1}y}{1+y^{2}}$ .

Therefore, $\mathrm{I.F} = e^{\int \frac{1}{1 + y^2}dy} = e^{\tan^{-1}y}$

Thus, the solution of the given differential equation is

$$
x e ^ {\tan^ {- 1} y} = \int \left(\frac {\tan^ {- 1} y}{1 + y ^ {2}}\right) e ^ {\tan^ {- 1} y} d y + C\tag{... (2}
$$

Let

$$
\mathrm{I} = \int \left(\frac {\tan^ {- 1} y}{1 + y ^ {2}}\right) e ^ {\tan^ {- 1} y} d y
$$

Substituting $\tan^{-1}y = t$ so that $\left(\frac{1}{1 + y^2}\right)dy = dt$, we get

$$
\mathrm{I} = \int t e ^ {t} d t = t e ^ {t} - \int 1 . e ^ {t} d t = t e ^ {t} - e ^ {t} = e ^ {t} (t - 1)
$$

or

$$
\mathrm{I} = e ^ {\tan^ {- 1} y (\tan^ {- 1} y - 1)}
$$

Substituting the value of I in equation (2), we get

$$
x. e ^ {\tan^ {- 1} y} = e ^ {\tan^ {- 1} y} (\tan^ {- 1} y - 1) + C
$$

or

$$
x = (\tan^ {- 1} y - 1) + C e ^ {- \tan^ {- 1} y}
$$

which is the general solution of the given differential equation.

## Miscellaneous Exercise on Chapter 9

1. For each of the differential equations given below, indicate its order and degree (if defined).

Reprint 2025-26

<!-- page 35 of 38 -->

334

MATHEMATICS

(i) $\frac{d^2y}{dx^2} + 5x\left(\frac{dy}{dx}\right)^2 - 6y = \log x$ (ii) $\left(\frac{dy}{dx}\right)^3 - 4\left(\frac{dy}{dx}\right)^2 + 7y = \sin x$

(iii) $\frac{d^4y}{dx^4} -\sin \left(\frac{d^3y}{dx^3}\right) = 0$

2. For each of the exercises given below, verify that the given function (implicit or explicit) is a solution of the corresponding differential equation.

$$
\text {(i)} x y = a e ^ {x} + b e ^ {- x} + x ^ {2}: x \frac {d ^ {2} y}{d x ^ {2}} + 2 \frac {d y}{d x} - x y + x ^ {2} - 2 = 0
$$

$$
\text {(ii)} y = e ^ {x} (a \cos x + b \sin x): \frac {d ^ {2} y}{d x ^ {2}} - 2 \frac {d y}{d x} + 2 y = 0
$$

$$
\frac {d ^ {2} y}{d x ^ {2}} + 9 y - 6 \cos 3 x = 0
$$

$$
x ^ {2} = 2 y ^ {2} \log y
$$

$$
(x ^ {2} + y ^ {2}) \frac {d y}{d x} - x y = 0
$$

3. Prove that $x^{2} - y^{2} = c(x^{2} + y^{2})^{2}$ is the general solution of differential equation $(x^{3} - 3xy^{2})dx = (y^{3} - 3x^{2}y)dy$, where $c$ is a parameter.

4. Find the general solution of the differential equation $\frac{dy}{dx} + \sqrt{\frac{1 - y^2}{1 - x^2}} = 0$.

5. Show that the general solution of the differential equation  $\frac{dy}{dx} + \frac{y^{2} + y + 1}{x^{2} + x + 1} = 0$  is given by  $(x + y + 1) = A(1 - x - y - 2xy)$ , where A is parameter.

6. Find the equation of the curve passing through the point $\left(0, \frac{\pi}{4}\right)$ whose differential equation is $\sin x \cos y dx + \cos x \sin y dy = 0$.

7. Find the particular solution of the differential equation $(1 + e^{2x})dy + (1 + y^2)e^xdx = 0$ , given that $y = 1$ when $x = 0$

8. Solve the differential equation $y e^{\frac{x}{y}} dx = \left( x e^{\frac{x}{y}} + y^{2} \right) dy (y \neq 0)$.

Reprint 2025-26

<!-- page 36 of 38 -->

DIFFERENTIAL EQUATIONS

335

9. Find a particular solution of the differential equation $(x - y)(dx + dy) = dx - dy$, given that $y = -1$, when $x = 0$. (Hint: put $x - y = t$)

10. Solve the differential equation $\left[\frac{e^{-2\sqrt{x}}}{\sqrt{x}} -\frac{y}{\sqrt{x}}\right]\frac{dx}{dy} = 1 (x\neq 0)$.

11. Find a particular solution of the differential equation $\frac{dy}{dx} + y\cot x = 4x \sec x (x \neq 0)$, given that $y = 0$ when $x = \frac{\pi}{2}$.

12. Find a particular solution of the differential equation $(x + 1)\frac{dy}{dx} = 2e^{-y} - 1$, given that $y = 0$ when $x = 0$.

13. The general solution of the differential equation $\frac{y dx - x dy}{y} = 0$ is (A) $xy = C$ (B) $x = Cy^2$ (C) $y = Cx$ (D) $y = Cx^2$

14. The general solution of a differential equation of the type $\frac{dx}{dy} + \mathrm{P}_1x = \mathrm{Q}_1$ is (A) $y e^{\int \mathrm{P}_1 dy} = \int \left( \mathrm{Q}_1 e^{\int \mathrm{P}_1 dy} \right) dy + \mathrm{C}$ (B) $y \cdot e^{\int \mathrm{P}_1 dx} = \int \left( \mathrm{Q}_1 e^{\int \mathrm{P}_1 dx} \right) dx + \mathrm{C}$ (C) $x e^{\int \mathrm{P}_1 dy} = \int \left( \mathrm{Q}_1 e^{\int \mathrm{P}_1 dy} \right) dy + \mathrm{C}$ (D) $x e^{\int \mathrm{P}_1 dx} = \int \left( \mathrm{Q}_1 e^{\int \mathrm{P}_1 dx} \right) dx + \mathrm{C}$

15. The general solution of the differential equation $e^x dy + (y e^x + 2x) dx = 0$ is  
(A) $x e^y + x^2 = C$  
(B) $x e^y + y^2 = C$  
(C) $y e^x + x^2 = C$  
(D) $y e^y + x^2 = C$

Reprint 2025-26

<!-- page 37 of 38 -->

336

MATHEMATICS

## Summary

An equation involving derivatives of the dependent variable with respect to independent variable (variables) is known as a differential equation.

Order of a differential equation is the order of the highest order derivative occurring in the differential equation.

\- Degree of a differential equation is defined if it is a polynomial equation in its derivatives.

Degree (when defined) of a differential equation is the highest power (positive integer only) of the highest order derivative in it.

A function which satisfies the given differential equation is called its solution. The solution which contains as many arbitrary constants as the order of the differential equation is called a general solution and the solution free from arbitrary constants is called particular solution.

Variable separable method is used to solve such an equation in which variables can be separated completely i.e. terms containing y should remain with dy and terms containing x should remain with dx.

A differential equation which can be expressed in the form $\frac{dy}{dx} = f(x,y)$ or $\frac{dx}{dy} = g(x,y)$ where, $f(x,y)$ and $g(x,y)$ are homogenous functions of degree zero is called a homogeneous differential equation.

A differential equation of the form $\frac{dy}{dx} + Py = Q$, where P and Q are constants or functions of $x$ only is called a first order linear differential equation.

## Historical Note

One of the principal languages of Science is that of differential equations. Interestingly, the date of birth of differential equations is taken to be November, 11, 1675, when Gottfried Wilhelm Freiherr Leibnitz (1646 - 1716) first put in black and white the identity $\int y dy = \frac{1}{2} y^2$, thereby introducing both the symbols $\int$ and $dy$. Leibnitz was actually interested in the problem of finding a curve whose tangents were prescribed. This led him to discover the 'method of separation of variables' 1691. A year later he formulated the 'method of solving the homogeneous

Reprint 2025-26

<!-- page 38 of 38 -->

DIFFERENTIAL EQUATIONS

337

differential equations of the first order'. He went further in a very short time to the discovery of the 'method of solving a linear differential equation of the first-order'. How surprising is it that all these methods came from a single man and that too within 25 years of the birth of differential equations!

In the old days, what we now call the ‘solution’ of a differential equation, was used to be referred to as ‘integral’ of the differential equation, the word being coined by James Bernoulli (1654 - 1705) in 1690. The word ‘solution was first used by Joseph Louis Lagrange (1736 - 1813) in 1774, which was almost hundred years since the birth of differential equations. It was Jules Henri Poincare (1854 - 1912) who strongly advocated the use of the word ‘solution’ and thus the word ‘solution’ has found its deserved place in modern terminology. The name of the ‘method of separation of variables’ is due to John Bernoulli (1667 - 1748), a younger brother of James Bernoulli.

Application to geometric problems were also considered. It was again John Bernoulli who first brought into light the intricate nature of differential equations. In a letter to Leibnitz, dated May 20, 1715, he revealed the solutions of the differential equation

$$
x ^ {2} y ^ {\prime \prime} = 2 y,
$$

which led to three types of curves, viz., parabolas, hyperbolas and a class of cubic curves. This shows how varied the solutions of such innocent looking differential equation can be. From the second half of the twentieth century attention has been drawn to the investigation of this complicated nature of the solutions of differential equations, under the heading ‘qualitative analysis of differential equations’. Now-a-days, this has acquired prime importance being absolutely necessary in almost all investigations.

Reprint 2025-26