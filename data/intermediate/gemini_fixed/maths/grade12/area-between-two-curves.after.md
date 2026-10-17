# Area under Simple Curves

In geometry, we have learnt formulae to calculate areas of various geometrical figures including triangles, rectangles, trapezias and circles. [S3] However, they are inadequate for calculating the areas enclosed by curves. [S3] For that, we shall need some concepts of Integral Calculus to find the area under simple curves, area between lines and arcs of circles, parabolas and ellipses. [S3] Finding the area bounded by these curves is a key application of definite integrals.

## The Basic Concept of Elementary Strips

To understand how to measure the area under a curve, we must first look at how we define it. [S1] In the previous chapter, we studied definite integrals as the limit of a sum. [S3] We can think of the area under a curve as being made up of a large number of very thin vertical strips. [S1] Consider an arbitrary strip of height $y$ and width $dx$, then the elementary area $dA$ is equal to $ydx$, where $y = f(x)$. [S1] We can think of the total area $A$ of the region between the x-axis, the ordinates $x = a$, $x = b$ and the curve $y = f(x)$ as the result of adding up the elementary areas of thin strips across the region. [S1] Symbolically, we express this as $A = \int_a^b y dx = \int_a^b f(x) dx$.

## The Area Function

The area of a region under a curve depends on the limits of integration. [S2] Let $x$ be a given point in the interval $[a, b]$. [S2] Then $\int_a^x f(x) dx$ represents the area of the region bounded by the curve $y = f(x)$, the x-axis, and the ordinate $x = a$ up to the point $x$. [S2] The area of this shaded region depends upon the value of $x$. [S2] In other words, the area of this shaded region is a function of $x$. [S2] We denote this function of $x$ by $A(x)$. [S2] We call the function $A(x)$ as Area function and is given by $A(x) = \int_a^x f(x) dx$. [S2]

## Area Bounded by a Curve Below the x-Axis

If the position of the curve under consideration is below the x-axis, then since $f(x) < 0$ from $x = a$ to $x = b$, the area bounded by the curve, x-axis and the ordinates $x = a$, $x = b$ comes out to be negative. [S1] But, it is only the numerical value of the area which is taken into consideration. [S1] Thus, if the area is negative, we take its absolute value, i.e., $\left|\int_a^b f(x) dx\right|$.

## Handling Negative Areas

Generally, it may happen that some portion of the curve is above the x-axis and some is below the x-axis. [S1] Here, $A_1 < 0$ and $A_2 > 0$. [S1] Therefore, the area $A$ bounded by the curve $y = f(x)$, x-axis and the ordinates $x = a$ and $x = b$ is given by $A = |A_1| + A_2$. [S1] This means that if the curve crosses the x-axis, we must split the integral into parts where the function is positive and parts where the function is negative. [S1] We then take the absolute value of the negative parts to ensure that we are measuring the actual geometric area, not just the signed area.

## Worked example

Let's apply the rule for finding the area under a simple curve to a specific problem. [S1] Find the area enclosed by the circle $x^{2} + y^{2} = a^{2}$. [S1]

Solution:
The whole area enclosed by the given circle is equal to 4 times the area of the region bounded by the curve, x-axis and the ordinates $x = 0$ and $x = a$ (as the circle is symmetrical about both x-axis and y-axis). [S1] Taking vertical strips, this is equal to $4\int_{0}^{a}ydx$. [S1] Since $x^{2} + y^{2} = a^{2}$ gives $y = \pm \sqrt{a^2 - x^2}$, and the region lies in the first quadrant, $y$ is taken as positive. [S1] Thus, the area is:
$$ 4 \int_ {0} ^ {a} \sqrt {a ^ {2} - x ^ {2}} d x $$ [S1]

Integrating, we get:
$$ 4 \left[ \frac {x}{2} \sqrt {a ^ {2} - x ^ {2}} + \frac {a ^ {2}}{2} \sin^ {- 1} \frac {x}{a} \right] _ {0} ^ {a} = 4 \left[ \left(\frac {a}{2} \times 0 + \frac {a ^ {2}}{2} \sin^ {- 1} 1\right) - 0 \right] = 4 \left(\frac {a ^ {2}}{2}\right) \left(\frac {\pi}{2}\right) = \pi a ^ {2} $$ [S1]

Alternatively, considering horizontal strips, the area is:
$$ 4 \int_ {0} ^ {a} x d y = 4 \int_ {0} ^ {a} \sqrt {a ^ {2} - y ^ {2}} d y = \pi a^2 $$ [S1]

## Key points

- The area $A$ of the region bounded by the curve $y = f(x)$, x-axis and the ordinates $x = a$, $x = b$ is given by $A = \int_a^b y dx = \int_a^b f(x) dx$. [S1]
- The area function $A(x) = \int_a^x f(x) dx$ is a function of $x$ that represents the area under the curve $y = f(x)$ from $a$ to $x$. [S2]
- If the position of the curve is below the x-axis, the area comes out to be negative, and we take its absolute value, i.e., $\left|\int_a^b f(x) dx\right|$. [S1]
- If some portion of the curve is above the x-axis and some is below, the total area is found by adding the absolute value of the negative area to the positive area: $A = |A_1| + A_2$. [S1]
- Finding the area under simple curves, such as circles, ellipses, and parabolas, is a key application of Integral Calculus. [S3]

<!-- TERMS: definite integral, area function, elementary area, ordinates, limits of integration, points of intersection, upper curve, lower curve, absolute value -->
