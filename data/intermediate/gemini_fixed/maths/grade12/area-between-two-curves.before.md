# Area Between Two Curves

In everyday life, you might need to measure the space between two boundaries, like the area of a park between a river and a road. [S3] In mathematics, we often need to find the space enclosed between two different curves on a graph. This is a direct extension of the area under a single curve that you may already know. [S3] Instead of just measuring the space from one curve down to the x-axis, we measure the vertical distance between two functions. [S3] This concept is fundamental because it allows us to calculate the exact space between two non-linear boundaries, such as the area between two different hills or the space between a parabola and a straight line.

## The Basic Concept of Elementary Strips

To understand how to measure the space between two curves, we must first look at how we measure the area under a single curve. [S1] In the previous chapter, we studied definite integrals as the limit of a sum. [S3] We can think of the area under a curve as being made up of a large number of very thin vertical strips. [S1] Consider an arbitrary strip of height $y$ and width $dx$, then the elementary area $dA$ is equal to $ydx$, where $y = f(x)$. [S1] We can think of the total area $A$ of the region between the x-axis, the ordinates $x = a$, $x = b$ and the curve $y = f(x)$ as the result of adding up the elementary areas of thin strips across the region. [S1] Symbolically, we express this as $A = \int_a^b y dx = \int_a^b f(x) dx$.

## The Area Function

The area of a region under a curve depends on the limits of integration. [S2] Let $x$ be a given point in the interval $[a, b]$. [S2] Then $\int_a^x f(x) dx$ represents the area of the region bounded by the curve $y = f(x)$, the x-axis, and the ordinate $x = a$ up to the point $x$. [S2] The area of this shaded region depends upon the value of $x$. [S2] In other words, the area of this shaded region is a function of $x$. [S2] We denote this function of $x$ by $A(x)$. [S2] We call the function $A(x)$ as Area function and is given by $A(x) = \int_a^x f(x) dx$. [S2] This function is useful because it allows us to calculate the area between two curves by finding the difference in the area functions of the two curves at the limits of integration.

## Calculating the Area Between Two Curves

When we have two curves, $y = f(x)$ and $y = g(x)$, the area between them can be found by subtracting the area under the lower curve from the area under the upper curve. [S1] The area $A$ bounded by the curve $y = f(x)$, the curve $y = g(x)$, and the ordinates $x = a$ and $x = b$ is given by the definite integral of the difference of the two functions. [S1] Symbolically, we express this as $A = \int_a^b [f(x) - g(x)] dx$. [S1] This formula holds true as long as $f(x) \geq g(x)$ for all $x$ in the interval $[a, b]$. [S1] If the position of the curve under consideration is below the x-axis, then since $f(x) < 0$ from $x = a$ to $x = b$, the area bounded by the curve, x-axis and the ordinates $x = a$, $x = b$ come out to be negative. [S1] But, it is only the numerical value of the area which is taken into consideration. [S1] Thus, if the area is negative, we take its absolute value, i.e., $\left|\int_a^b f(x) dx\right|$.

## Handling Negative Areas

Generally, it may happen that some portion of the curve is above the x-axis and some is below the x-axis. [S1] Here, $A_1 < 0$ and $A_2 > 0$. [S1] Therefore, the area $A$ bounded by the curve $y = f(x)$, x-axis and the ordinates $x = a$ and $x = b$ is given by $A = |A_1| + A_2$. [S1] This means that if the two curves cross the x-axis, we must split the integral into parts where the function is positive and parts where the function is negative. [S1] We then take the absolute value of the negative parts to ensure that we are measuring the actual geometric area, not just the signed area.

## Worked example

Let's apply the rule for finding the area between two curves to a specific problem. [S1] Consider the curves $y = x^2$ and $y = x$. [S1] We want to find the area enclosed by these two curves. [S1] First, we need to find the points of intersection by setting the two equations equal to each other: $x^2 = x$. [S1] This gives us $x^2 - x = 0$, which factors to $x(x - 1) = 0$. [S1] So, the points of intersection are at $x = 0$ and $x = 1$. [S1] Now, we need to determine which curve is on top in the interval $[0, 1]$. [S1] We can test a point, say $x = 0.5$. [S1] For $y = x^2$, $y = 0.25$. [S1] For $y = x$, $y = 0.5$. [S1] So, $y = x$ is the upper curve and $y = x^2$ is the lower curve. [S1] Now, we can apply the formula for the area between two curves: $A = \int_0^1 [f(x) - g(x)] dx = \int_0^1 [x - x^2] dx$. [S1] Integrating, we get $A = \left[\frac{x^2}{2} - \frac{x^3}{3}\right]_0^1 = \left(\frac{1^2}{2} - \frac{1^3}{3}\right) - (0 - 0) = \frac{1}{2} - \frac{1}{3} = \frac{1}{6}$. [S1] So, the area enclosed by the curves $y = x^2$ and $y = x$ is $\frac{1}{6}$ square units.

## Key points

- The area between two curves $y = f(x)$ and $y = g(x)$ from $x = a$ to $x = b$ is given by the definite integral of their difference: $A = \int_a^b [f(x) - g(x)] dx$. [S1]
- The area function $A(x) = \int_a^x f(x) dx$ is a function of $x$ that represents the area under the curve $y = f(x)$ from $a$ to $x$. [S2]
- If the area is negative, we take its absolute value, i.e., $\left|\int_a^b f(x) dx\right|$. [S1]
- If the two curves cross the x-axis, we must split the integral into parts where the function is positive and parts where the function is negative, and then take the absolute value of the negative parts. [S1]
- The area between two curves is a direct extension of the area under a single curve, and it is a fundamental application of definite integrals in calculus. [S3]

<!-- TERMS: definite integral, area function, elementary area, ordinates, limits of integration, points of intersection, upper curve, lower curve, absolute value -->