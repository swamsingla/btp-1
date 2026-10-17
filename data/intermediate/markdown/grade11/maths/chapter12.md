<!-- page 1 of 40 -->

11076CH13

Chapter

12

# LIMITS AND DERIVATIVES

With the Calculus as a key, Mathematics can be successfully applied to the explanation of the course of Nature – WHITEHEAD

## 12.1 Introduction

This chapter is an introduction to Calculus. Calculus is that branch of mathematics which mainly deals with the study of change in the value of a function as the points in the domain change. First, we give an intuitive idea of derivative (without actually defining it). Then we give a naive definition of limit and study some algebra of limits. Then we come back to a definition of derivative and study some algebra of derivatives. We also obtain derivatives of certain standard functions.

![Image block](doc:ef55644/tier:standard/page:1/block:8)

## 12.2 Intuitive Idea of Derivatives

Sir Issac Newton (1642-1727)

Physical experiments have confirmed that the body dropped from a tall cliff covers a distance of  $4.9t^{2}$  metres in t seconds,

i.e., distance $s$ in metres covered by the body as a function of time $t$ in seconds is given by $s = 4.9t^2$.

The adjoining Table 13.1 gives the distance travelled in metres at various intervals of time in seconds of a body dropped from a tall cliff.

The objective is to find the velocity of the body at time $t = 2$ seconds from this data. One way to approach this problem is to find the average velocity for various intervals of time ending at $t = 2$ seconds and hope that these throw some light on the velocity at $t = 2$ seconds.

Average velocity between  $t = t_{1}$  and  $t = t_{2}$  equals distance travelled between  $t = t_{1}$  and  $t = t_{2}$  seconds divided by  $(t_{2} - t_{1})$ . Hence the average velocity in the first two seconds

Reprint 2025-26

<!-- page 2 of 40 -->

218

MATHEMATICS

$$
\begin{array}{l} = \frac {\text {Distance travelled between} t _ {2} = 2 \text {and} t _ {1} = 0}{\text {Time interval} (t _ {2} - t _ {1})} \\ = \frac {(1 9 . 6 - 0) m}{(2 - 0) s} = 9. 8 m / s. \end{array}
$$

Similarly, the average velocity between $t = 1$ and $t = 2$ is

$$
\frac {(1 9 . 6 - 4 . 9) m}{(2 - 1) s} = 1 4. 7 \text {m / s}
$$

Likewise we compute the average velocity between  $t = t_{1}$  and t = 2 for various  $t_{1}$ . The following Table 13.2 gives the average velocity (v),  $t = t_{1}$  seconds and t = 2 seconds.

Table 12.1

| t | s |
| --- | --- |
| 0 | 0 |
| 1 | 4.9 |
| 1.5 | 11.025 |
| 1.8 | 15.876 |
| 1.9 | 17.689 |
| 1.95 | 18.63225 |
| 2 | 19.6 |
| 2.05 | 20.59225 |
| 2.1 | 21.609 |
| 2.2 | 23.716 |
| 2.5 | 30.625 |
| 3 | 44.1 |
| 4 | 78.4 |

Table 12.2

| $t_{1}$ | 0 | 1 | 1.5 | 1.8 | 1.9 | 1.95 | 1.99 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| v | 9.8 | 14.7 | 17.15 | 18.62 | 19.11 | 19.355 | 19.551 |

From Table 12.2, we observe that the average velocity is gradually increasing. As we make the time intervals ending at t = 2 smaller, we see that we get a better idea of the velocity at t = 2. Hoping that nothing really dramatic happens between 1.99 seconds and 2 seconds, we conclude that the average velocity at t = 2 seconds is just above 19.551m/s.

This conclusion is somewhat strengthened by the following set of computation. Compute the average velocities for various time intervals starting at t = 2 seconds. As before the average velocity v between t = 2 seconds and  $t = t_{2}$  seconds is

Distance travelled between 2 seconds and $t_2$ seconds

$$
t _ {2} - 2
$$

= Distance travelled in  $t_{2}$  seconds – Distance travelled in 2 seconds

$$
t _ {2} - 2
$$

Reprint 2025-26

<!-- page 3 of 40 -->

LIMITS AND DERIVATIVES

219

$$
= \frac {\text {Distance travelled in} t _ {2} \text {seconds} - 1 9 . 6}{t _ {2} - 2}
$$

The following Table 12.3 gives the average velocity v in metres per second between t = 2 seconds and  $t_{2}$  seconds.

Table 12.3

| $t_{2}$ | 4 | 3 | 2.5 | 2.2 | 2.1 | 2.05 | 2.01 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| v | 29.4 | 24.5 | 22.05 | 20.58 | 20.09 | 19.845 | 19.649 |

Here again we note that if we take smaller time intervals starting at $t = 2$, we get better idea of the velocity at $t = 2$.

In the first set of computations, what we have done is to find average velocities in increasing time intervals ending at t=2 and then hope that nothing dramatic happens just before t=2. In the second set of computations, we have found the average velocities decreasing in time intervals ending at t=2 and then hope that nothing dramatic happens just after t=2. Purely on the physical grounds, both these sequences of average velocities must approach a common limit. We can safely conclude that the velocity of the body at t=2 is between 19.551m/s and 19.649 m/s. Technically, we say that the instantaneous velocity at t=2 is between 19.551 m/s and 19.649 m/s. As is well-known, velocity is the rate of change of displacement. Hence what we have accomplished is the following. From the given data of distance covered at various time

change of the distance at a given instant of time. We say that the derivative of the distance function $s = 4.9t^2$ at $t = 2$ is between 19.551 and 19.649.

An alternate way of viewing this limiting process is shown in Fig 12.1. This is a plot of distance s of the body from the top of the cliff versus the time t elapsed. In the limit as the sequence of time intervals  $h_{1}, h_{2}, \ldots$ , approaches zero, the sequence of average velocities approaches the same limit as does the sequence of ratios

![Chart block](doc:ef55644/tier:standard/page:3/block:11)

Fig 12.1

Reprint 2025-26

<!-- page 4 of 40 -->

220

MATHEMATICS

$$
\left| \frac {\mathrm{C} _ {1} \mathrm{B} _ {1}}{\mathrm{AC} _ {1}}, \frac {\mathrm{C} _ {2} \mathrm{B} _ {2}}{\mathrm{AC} _ {2}}, \frac {\mathrm{C} _ {3} \mathrm{B} _ {3}}{\mathrm{AC} _ {3}}, \dots \right|
$$

where  $C_{1}B_{1}=s_{1}-s_{0}$  is the distance travelled by the body in the time interval  $h_{1}=AC_{1}$ , etc. From the Fig 12.1 it is safe to conclude that this latter sequence approaches the slope of the tangent to the curve at point A. In other words, the instantaneous velocity  $v(t)$  of a body at time t=2 is equal to the slope of the tangent of the curve  $s=4.9t^{2}$  at t=2.

## 12.3 Limits

The above discussion clearly points towards the fact that we need to understand limiting process in greater clarity. We study a few illustrative examples to gain some familiarity with the concept of limits.

Consider the function $f(x) = x^2$. Observe that as $x$ takes values very close to 0, the value of $f(x)$ also moves towards 0 (See Fig 2.10 Chapter 2). We say

$$
\lim _ {x \to 0} f (x) = 0
$$

(to be read as limit of $f(x)$ as $x$ tends to zero equals zero). The limit of $f(x)$ as $x$ tends to zero is to be thought of as the value $f(x)$ should assume at $x = 0$.

In general as $x \to a, f(x) \to l$, then $l$ is called limit of the function $f(x)$ which is symbolically written as $\lim_{x \to a} f(x) = l$.

Consider the following function $g(x) = |x|, x \neq 0$. Observe that $g(0)$ is not defined.

Computing the value of $g(x)$ for values of $x$ very near to 0, we see that the value of $g(x)$ moves towards 0. So, $\lim_{x \to 0} g(x) = 0$. This is intuitively clear from the graph of $y = |x|$ for $x \neq 0$. (See Fig 2.13, Chapter 2).

Consider the following function.

$$
h (x) = \frac {x ^ {2} - 4}{x - 2}, x \neq 2.
$$

Compute the value of  $h(x)$  for values of x very near to 2 (but not at 2). Convince yourself that all these values are near to 4. This is somewhat strengthened by considering the graph of the function  $y = h(x)$  given here (Fig 12.2).

![Image block](doc:ef55644/tier:standard/page:4/block:16)

Fig 12.2

Reprint 2025-26

<!-- page 5 of 40 -->

LIMITS AND DERIVATIVES

221

In all these illustrations the value which the function should assume at a given point $x = a$ did not really depend on how is $x$ tending to $a$. Note that there are essentially two ways $x$ could approach a number $a$ either from left or from right, i.e., all the values of $x$ near $a$ could be less than $a$ or could be greater than $a$. This naturally leads to two limits - the right hand limit and the left hand limit. Right hand limit of a function $f(x)$ is that value of $f(x)$ which is dictated by the values of $f(x)$ when $x$ tends to $a$ from the right. Similarly, the left hand limit. To illustrate this, consider the function

$$
f (x) = \left\{ \begin{array}{l l} 1, & x \leq 0 \\ 2, & x > 0 \end{array} \right.
$$

Graph of this function is shown in the Fig 12.3. It is clear that the value of $f$ at 0 dictated by values of $f(x)$ with $x \leq 0$ equals 1, i.e., the left hand limit of $f(x)$ at 0 is

$$
\lim _ {x \to \bar {0}} f (x) = 1.
$$

Similarly, the value of $f$ at 0 dictated by values of $f(x)$ with $x > 0$ equals 2, i.e., the right hand limit of $f(x)$ at 0 is

![Image block](doc:ef55644/tier:standard/page:5/block:8)

$$
\lim _ {x \to 0 ^ {+}} f (x) = 2.
$$

Fig 12.3

In this case the right and left hand limits are different, and hence we say that the limit of $f(x)$ as $x$ tends to zero does not exist (even though the function is defined at 0).

## Summary

We say $\lim_{x\to a^{-}}f(x)$ is the expected value of $f$ at $x = a$ given the values of $f$ near $x$ to the left of $a$. This value is called the left hand limit of $f$ at $a$.

We say $\lim_{x\to a^{+}}f(x)$ is the expected value of $f$ at $x = a$ given the values of $f$ near $x$ to the right of $a$. This value is called the right hand limit of $f(x)$ at $a$.

If the right and left hand limits coincide, we call that common value as the limit of $f(x)$ at $x = a$ and denote it by $\lim_{x\to a}f(x)$.

Illustration 1 Consider the function $f(x) = x + 10$. We want to find the limit of this function at $x = 5$. Let us compute the value of the function $f(x)$ for $x$ very near to 5. Some of the points near and to the left of 5 are 4.9, 4.95, 4.99, 4.995, ..., etc. Values of the function at these points are tabulated below. Similarly, the real number 5.001,

Reprint 2025-26

<!-- page 6 of 40 -->

222

MATHEMATICS

5.01, 5.1 are also points near and to the right of 5. Values of the function at these points are also given in the Table 12.4.

Table 12.4

| x | 4.9 | 4.95 | 4.99 | 4.995 | 5.001 | 5.01 | 5.1 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| f(x) | 14.9 | 14.95 | 14.99 | 14.995 | 15.001 | 15.01 | 15.1 |

From the Table 12.4, we deduce that value of $f(x)$ at $x = 5$ should be greater than 14.995 and less than 15.001 assuming nothing dramatic happens between $x = 4.995$ and 5.001. It is reasonable to assume that the value of the $f(x)$ at $x = 5$ as dictated by the numbers to the left of 5 is 15, i.e.,

$$
\lim _ {x \to 5 ^ {-}} f (x) = 1 5.
$$

Similarly, when $x$ approaches 5 from the right, $f(x)$ should be taking value 15, i.e.,

$$
\lim _ {x \to 5 ^ {+}} f (x) = 1 5.
$$

Hence, it is likely that the left hand limit of $f(x)$ and the right hand limit of $f(x)$ are both equal to 15. Thus,

$$
\lim _ {x \to 5 ^ {-}} f (x) = \lim _ {x \to 5 ^ {+}} f (x) = \lim _ {x \to 5} f (x) = 1 5.
$$

This conclusion about the limit being equal to 15 is somewhat strengthened by seeing the graph of this function which is given in Fig 2.16, Chapter 2. In this figure, we note that as x approaches 5 from either right or left, the graph of the function  $f(x) = x + 10$  approaches the point (5, 15).

We observe that the value of the function at $x = 5$ also happens to be equal to 15.

Illustration 2 Consider the function $f(x) = x^3$. Let us try to find the limit of this function at $x = 1$. Proceeding as in the previous case, we tabulate the value of $f(x)$ at $x$ near 1. This is given in the Table 12.5.

Table 12.5

| x | 0.9 | 0.99 | 0.999 | 1.001 | 1.01 | 1.1 |
| --- | --- | --- | --- | --- | --- | --- |
| f(x) | 0.729 | 0.970299 | 0.997002999 | 1.003003001 | 1.030301 | 1.331 |

From this table, we deduce that value of $f(x)$ at $x = 1$ should be greater than 0.997002999 and less than 1.003003001 assuming nothing dramatic happens between

Reprint 2025-26

<!-- page 7 of 40 -->

LIMITS AND DERIVATIVES

223

$x = 0.999$ and 1.001. It is reasonable to assume that the value of the $f(x)$ at $x = 1$ as dictated by the numbers to the left of 1 is 1, i.e.,

$$
\lim _ {x \to^ {- 1} ^ {-}} f (x) = 1.
$$

Similarly, when $x$ approaches 1 from the right, $f(x)$ should be taking value 1, i.e.,

$$
\lim _ {x \to^ {+}} f (x) = 1.
$$

Hence, it is likely that the left hand limit of $f(x)$ and the right hand limit of $f(x)$ are both equal to 1. Thus,

$$
\lim _ {x \to 1 ^ {-}} f (x) = \lim _ {x \to 1 ^ {+}} f (x) = \lim _ {x \to 1} f (x) = 1.
$$

This conclusion about the limit being equal to 1 is somewhat strengthened by seeing the graph of this function which is given in Fig 2.11, Chapter 2. In this figure, we note that as x approaches 1 from either right or left, the graph of the function  $f(x) = x^{3}$  approaches the point (1, 1).

We observe, again, that the value of the function at $x = 1$ also happens to be equal to 1.

Illustration 3 Consider the function $f(x) = 3x$. Let us try to find the limit of this function at $x = 2$. The following Table 12.6 is now self-explanatory.

Table 12.6

| x | 1.9 | 1.95 | 1.99 | 1.999 | 2.001 | 2.01 | 2.1 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| f(x) | 5.7 | 5.85 | 5.97 | 5.997 | 6.003 | 6.03 | 6.3 |

As before we observe that as $x$ approaches 2 from either left or right, the value of $f(x)$ seem to approach 6. We record this as

$$
\lim _ {x \to 2 ^ {-}} f (x) = \lim _ {x \to 2 ^ {+}} f (x) = \lim _ {x \to 2} f (x) = 6
$$

Its graph shown in Fig 12.4 strengthens this fact.

Here again we note that the value of the function at $x = 2$ coincides with the limit at $x = 2$.

Illustration 4 Consider the constant function $f(x) = 3$. Let us try to find its limit at $x = 2$. This function being the constant function takes the same

![Image block](doc:ef55644/tier:standard/page:7/block:19)

Fig 12.4

Reprint 2025-26

<!-- page 8 of 40 -->

224

MATHEMATICS

value (3, in this case) everywhere, i.e., its value at points close to 2 is 3. Hence

$$
\lim _ {x \to 2} f (x) = \lim _ {x \to 2 ^ {+}} f (x) = \lim _ {x \to 2} f (x) = 3
$$

Graph of $f(x) = 3$ is anyway the line parallel to $x$-axis passing through (0, 3) and is shown in Fig 2.9, Chapter 2. From this also it is clear that the required limit is 3. In fact, it is easily observed that $\lim_{x \to a} f(x) = 3$ for any real number $a$.

Illustration 5 Consider the function $f(x) = x^{2} + x$. We want to find $\lim_{x\to 1}f(x)$. We tabulate the values of $f(x)$ near $x = 1$ in Table 12.7.

Table 12.7

| x | 0.9 | 0.99 | 0.999 | 1.01 | 1.1 | 1.2 |
| --- | --- | --- | --- | --- | --- | --- |
| f(x) | 1.71 | 1.9701 | 1.997001 | 2.0301 | 2.31 | 2.64 |

From this it is reasonable to deduce that

$$
\lim _ {x \to 1 ^ {-}} f (x) = \lim _ {x \to 1 ^ {+}} f (x) = \lim _ {x \to 1} f (x) = 2.
$$

From the graph of  $f(x) = x^{2} + x$  shown in the Fig 12.5, it is clear that as x approaches 1, the graph approaches (1, 2).

Here, again we observe that the

$$
\lim _ {x \to 1} f (x) = f (1)
$$

![Image block](doc:ef55644/tier:standard/page:8/block:14)

Now, convince yourself of the following three facts:

Y' Fig 12.5

$$
\lim _ {x \to 1} x ^ {2} = 1, \lim _ {x \to 1} x = 1 \text {and} \lim _ {x \to 1} x + 1 = 2
$$

Then

$$
\lim _ {x \to 1} x ^ {2} + \lim _ {x \to 1} x = 1 + 1 = 2 = \lim _ {x \to 1} \left[ x ^ {2} + x \right].
$$

Also

$$
\lim _ {x \rightarrow 1} x. \lim _ {x \rightarrow 1} (x + 1) = 1. 2 = 2 = \lim _ {x \rightarrow 1} [ x (x + 1) ] = \lim _ {x \rightarrow 1} [ x ^ {2} + x ].
$$

Reprint 2025-26

<!-- page 9 of 40 -->

LIMITS AND DERIVATIVES

225

Illustration 6 Consider the function $f(x) = \sin x$. We are interested in $\lim_{x\to \frac{\pi}{2}}\sin x$, where the angle is measured in radians.

Here, we tabulate the (approximate) value of $f(x)$ near $\frac{\pi}{2}$ (Table 12.8). From this, we may deduce that

$$
\lim _ {x \to \frac {\pi}{2} ^ {-}} f (x) = \lim _ {x \to \frac {\pi}{2} ^ {+}} f (x) = \lim _ {x \to \frac {\pi}{2}} f (x) = 1.
$$

Further, this is supported by the graph of $f(x) = \sin x$ which is given in the Fig 3.8 (Chapter 3). In this case too, we observe that $\lim_{x\to 0}\sin x = 1$.

$$
x \rightarrow \frac {\pi}{2}
$$

Table 12.8

| x | $\frac{\pi}{2} - 0.1$ | $\frac{\pi}{2} - 0.01$ | $\frac{\pi}{2} + 0.01$ | $\frac{\pi}{2} + 0.1$ |
| --- | --- | --- | --- | --- |
| f(x) | 0.9950 | 0.9999 | 0.9999 | 0.9950 |

Illustration 7 Consider the function $f(x) = x + \cos x$. We want to find the $\lim_{x\to 0}f(x)$. Here we tabulate the (approximate) value of $f(x)$ near 0 (Table 12.9).

Table 12.9

| x | -0.1 | -0.01 | -0.001 | 0.001 | 0.01 | 0.1 |
| --- | --- | --- | --- | --- | --- | --- |
| f(x) | 0.9850 | 0.98995 | 0.9989995 | 1.0009995 | 1.00995 | 1.0950 |

From the Table 13.9, we may deduce that

$$
\lim _ {x \to 0 ^ {-}} f (x) = \lim _ {x \to 0 ^ {+}} f (x) = \lim _ {x \to 0} f (x) = 1
$$

In this case too, we observe that $\lim_{x\to 0}f(x) = f(0) = 1$.

Now, can you convince yourself that

$$
\lim _ {x \to 0} [ x + \cos x ] = \lim _ {x \to 0} x + \lim _ {x \to 0} \cos x \text {is indeed true?}
$$

Reprint 2025-26

<!-- page 10 of 40 -->

226

MATHEMATICS

Illustration 8 Consider the function $f(x) = \frac{1}{x^2}$ for $x > 0$. We want to know $\lim_{x \to 0^+} f(x)$.

Here, observe that the domain of the function is given to be all positive real numbers. Hence, when we tabulate the values of $f(x)$, it does not make sense to talk of $x$ approaching 0 from the left. Below we tabulate the values of the function for positive $x$ close to 0 (in this table $n$ denotes any positive integer).

From the Table 12.10 given below, we see that as $x$ tends to 0, $f(x)$ becomes larger and larger. What we mean here is that the value of $f(x)$ may be made larger than any given number.

Table 12.10

| x | 1 | 0.1 | 0.01 | $10^{-n}$ |
| --- | --- | --- | --- | --- |
| f(x) | 1 | 100 | 10000 | $10^{2n}$ |

Mathematically, we say

$$
\lim _ {x \to 0} f (x) = + \infty
$$

We also remark that we will not come across such limits in this course.

Illustration 9 We want to find $\lim_{x\to 0}f(x)$, where

$$
f (x) = \left\{ \begin{array}{l l} x - 2, & x <   0 \\ 0, & x = 0 \\ x + 2, & x > 0 \end{array} \right.
$$

As usual we make a table of $x$ near 0 with $f(x)$. Observe that for negative values of $x$ we need to evaluate $x - 2$ and for positive values, we need to evaluate $x + 2$.

Table 12.11

| x | -0.1 | -0.01 | -0.001 | 0.001 | 0.01 | 0.1 |
| --- | --- | --- | --- | --- | --- | --- |
| f(x) | -2.1 | -2.01 | -2.001 | 2.001 | 2.01 | 2.1 |

From the first three entries of the Table 12.11, we deduce that the value of the function is decreasing to -2 and hence.

$$
\lim _ {x \to 0 ^ {-}} f (x) = - 2
$$

Reprint 2025-26

<!-- page 11 of 40 -->

LIMITS AND DERIVATIVES

227

From the last three entires of the table we deduce that the value of the function is increasing from 2 and hence Y

$$
\lim _ {x \to 0 ^ {+}} f (x) = 2
$$

Since the left and right hand limits at 0 do not coincide, we say that the limit of the function at 0 does not exist.

Graph of this function is given in the Fig12.6. Here, we remark that the value of the function at $x = 0$ is well defined and is, indeed, equal to 0, but the limit of the function at $x = 0$ is not even defined.

![Image block](doc:ef55644/tier:standard/page:11/block:7)

Fig 12.6

Illustration 10 As a final illustration, we find $\lim_{x\to 1}f(x)$, where

$$
f (x) = \left\{ \begin{array}{c c} x + 2 & x \neq 1 \\ 0 & x = 1 \end{array} \right.
$$

Table 12.12

| x | 0.9 | 0.99 | 0.999 | 1.001 | 1.01 | 1.1 |
| --- | --- | --- | --- | --- | --- | --- |
| f(x) | 2.9 | 2.99 | 2.999 | 3.001 | 3.01 | 3.1 |

As usual we tabulate the values of $f(x)$ for $x$ near 1. From the values of $f(x)$ for $x$ less than 1, it seems that the function should take value 3 at $x = 1$, i.e.,

$$
\lim _ {x \to 1 ^ {-}} f (x) = 3.
$$

Similarly, the value of $f(x)$ should be 3 as dictated by values of $f(x)$ at $x$ greater than 1. i.e.

$$
\lim _ {x \to 1 ^ {+}} f (x) = 3.
$$

But then the left and right hand limits coincide and hence

$$
\lim _ {x \to 1 ^ {-}} f (x) = \lim _ {x \to 1 ^ {+}} f (x) = \lim _ {x \to 1} f (x) = 3.
$$

Graph of function given in Fig 12.7 strengthens our deduction about the limit. Here, we

![Image block](doc:ef55644/tier:standard/page:11/block:20)

Fig 12.7

Reprint 2025-26

<!-- page 12 of 40 -->

228

MATHEMATICS

note that in general, at a given point the value of the function and its limit may be different (even when both are defined).

12.3.1 Algebra of limits In the above illustrations, we have observed that the limiting process respects addition, subtraction, multiplication and division as long as the limits and functions under consideration are well defined. This is not a coincidence. In fact, below we formalise these as a theorem without proof.

Theorem 1 Let $f$ and $g$ be two functions such that both $\lim_{x\to a}f(x)$ and $\lim_{x\to a}g(x)$ exist. Then

(i) Limit of sum of two functions is sum of the limits of the functions, i.e.,

$$
\lim _ {x \to a} [ f (x) + g (x) ] = \lim _ {x \to a} f (x) + \lim _ {x \to a} g (x).
$$

(ii) Limit of difference of two functions is difference of the limits of the functions, i.e.,

$$
\lim _ {x \to a} [ f (x) - g (x) ] = \lim _ {x \to a} f (x) - \lim _ {x \to a} g (x).
$$

(iii) Limit of product of two functions is product of the limits of the functions, i.e.,

$$
\lim _ {x \to a} [ f (x). g (x) ] = \lim _ {x \to a} f (x). \lim _ {x \to a} g (x).
$$

(iv) Limit of quotient of two functions is quotient of the limits of the functions (whenever the denominator is non zero), i.e.,

$$
\lim _ {x \to a} \frac {f (x)}{g (x)} = \frac {\lim _ {x \to a} f (x)}{\lim _ {x \to a} g (x)}
$$

Note In particular as a special case of (iii), when $g$ is the constant function such that $g(x) = \lambda$, for some real number $\lambda$, we have

$$
\lim _ {x \to a} \left[ (\lambda . f) (x) \right] = \lambda . \lim _ {x \to a} f (x).
$$

In the next two subsections, we illustrate how to exploit this theorem to evaluate limits of special types of functions.

12.3.2 Limits of polynomials and rational functions A function $f$ is said to be a polynomial function of degree $n f(x) = a_0 + a_1 x + a_2 x^2 + \ldots + a_n x^n$, where $a_1 s$ are real numbers such that $a_n \neq 0$ for some natural number $n$.

We know that $\lim_{x\to a}x = a$ . Hence

Reprint 2025-26

<!-- page 13 of 40 -->

LIMITS AND DERIVATIVES

229

$$
\lim _ {x \to a} x ^ {2} = \lim _ {x \to a} (x. x) = \lim _ {x \to a} x. \lim _ {x \to a} x = a. a = a ^ {2}
$$

An easy exercise in induction on $n$ tells us that

$$
\lim _ {x \to a} x ^ {n} = a ^ {n}
$$

Now, let $f(x) = a_0 + a_1x + a_2x^2 + \ldots + a_nx^n$ be a polynomial function. Thinking of each of $a_0, a_1x, a_2x^2, \ldots, a_nx^n$ as a function, we have

$$
\begin{array}{r l} \lim _ {x \to a} f (x) & = \lim _ {x \to a} \left[ a _ {0} + a _ {1} x + a _ {2} x ^ {2} + \dots + a _ {n} x ^ {n} \right] \\ & = \lim _ {x \to a} a _ {0} + \lim _ {x \to a} a _ {1} x + \lim _ {x \to a} a _ {2} x ^ {2} + \dots + \lim _ {x \to a} a _ {n} x ^ {n} \\ & = a _ {0} + a _ {1} \lim _ {x \to a} x + a _ {2} \lim _ {x \to a} x ^ {2} + \dots + a _ {n} \lim _ {x \to a} x ^ {n} \\ & = a _ {0} + a _ {1} a + a _ {2} a ^ {2} + \dots + a _ {n} a ^ {n} \\ & = f (a) \end{array}
$$

(Make sure that you understand the justification for each step in the above!)

A function $f$ is said to be a rational function, if $f(x) = \frac{g(x)}{h(x)}$, where $g(x)$ and $h(x)$ are polynomials such that $h(x) \neq 0$. Then

$$
\lim _ {x \to a} f (x) = \lim _ {x \to a} \frac {g (x)}{h (x)} = \frac {\lim _ {x \to a} g (x)}{\lim _ {x \to a} h (x)} = \frac {g (a)}{h (a)}
$$

However, if $h(a) = 0$, there are two scenarios - (i) when $g(a) \neq 0$ and (ii) when $g(a) = 0$. In the former case we say that the limit does not exist. In the latter case we can write $g(x) = (x - a)^k g_1(x)$, where $k$ is the maximum of powers of $(x - a)$ in $g(x)$. Similarly, $h(x) = (x - a)^l h_1(x)$ as $h(a) = 0$. Now, if $k > l$, we have

$$
\lim _ {x \to a} f (x) = \frac {\lim _ {x \to a} g (x)}{\lim _ {x \to a} h (x)} = \frac {\lim _ {x \to a} (x - a) ^ {k} g _ {1} (x)}{\lim _ {x \to a} (x - a) ^ {l} h _ {1} (x)}
$$

Reprint 2025-26

<!-- page 14 of 40 -->

230

MATHEMATICS

$$
= \frac {\lim _ {x \to a} (x - a) ^ {(k - l)} g _ {1} (x)}{\lim _ {x \to a} h _ {1} (x)} = \frac {0 . g _ {1} (a)}{h _ {1} (a)} = 0
$$

If $k < l$, the limit is not defined.

Example 1 Find the limits: (i) $\lim_{x\to 1}\left[x^3 -x^2 +1\right]$ (ii) $\lim_{x\to 3}\left[x(x + 1)\right]$

(iii) $\lim_{x\to -1}\left[1 + x + x^2 +\dots +x^{10}\right].$

Solution The required limits are all limits of some polynomial functions. Hence the limits are the values of the function at the prescribed points. We have

(i) $\lim_{x\to 1}[x^3 -x^2 +1] = 1^3 -1^2 +1 = 1$

(ii) $\lim_{x\to 3}\left[x(x + 1)\right] = 3(3 + 1) = 3(4) = 12$

(iii) $\lim_{x\to -1}\left[1 + x + x^2 +\dots +x^{10}\right] = 1 + (-1) + (-1)^2 +\dots +(-1)^{10}$

$$
= 1 - 1 + 1 \dots + 1 = 1.
$$

Example 2 Find the limits:

$$
\lim _ {x \to 1} \left[ \frac {x ^ {2} + 1}{x + 1 0 0} \right]\tag{i}
$$

$$
\lim _ {x \to 2} \left[ \frac {x ^ {3} - 4 x ^ {2} + 4 x}{x ^ {2} - 4} \right]\tag{iii}
$$

$$
\lim _ {x \to 2} \left[ \frac {x ^ {2} - 4}{x ^ {3} - 4 x ^ {2} + 4 x} \right]
$$

$$
\lim _ {x \to 2} \left[ \frac {x ^ {3} - 2 x ^ {2}}{x ^ {2} - 5 x + 6} \right]
$$

(v) $\lim_{x\to 1}\left[\frac{x - 2}{x^2 - x} -\frac{1}{x^3 - 3x^2 + 2x}\right].$

Solution All the functions under consideration are rational functions. Hence, we first evaluate these functions at the prescribed points. If this is of the form $\frac{0}{0}$, we try to rewrite the function cancelling the factors which are causing the limit to be of the form $\frac{0}{0}$.

Reprint 2025-26

<!-- page 15 of 40 -->

LIMITS AND DERIVATIVES

231

(i) We have $\lim_{x\to 1}\frac{x^2 + 1}{x + 100} = \frac{1^2 + 1}{1 + 100} = \frac{2}{101}$

(ii) Evaluating the function at 2, it is of the form $\frac{0}{0}$.

Hence $\lim_{x\to 2}\frac{x^3 - 4x^2 + 4x}{x^2 - 4} = \lim_{x\to 2}\frac{x(x - 2)^2}{(x + 2)(x - 2)}$ $= \lim_{x\to 2}\frac{x(x - 2)}{(x + 2)}$ as $x\neq 2$ $= \frac{2(2 - 2)}{2 + 2} = \frac{0}{4} = 0.$

(iii) Evaluating the function at 2, we get it of the form $\frac{0}{0}$

Hence $\lim_{x\to 2}\frac{x^2 - 4}{x^3 - 4x^2 + 4x} = \lim_{x\to 2}\frac{(x + 2)(x - 2)}{x(x - 2)^2}$

$$
= \lim _ {x \to 2} \frac {(x + 2)}{x (x - 2)} = \frac {2 + 2}{2 (2 - 2)} = \frac {4}{0}
$$

which is not defined.

(iv) Evaluating the function at 2, we get it of the form $\frac{0}{0}$.

Hence

$$
\begin{array}{r l} \lim _ {x \to 2} \frac {x ^ {3} - 2 x ^ {2}}{x ^ {2} - 5 x + 6} & = \lim _ {x \to 2} \frac {x ^ {2} (x - 2)}{(x - 2) (x - 3)} \\ & = \lim _ {x \to 2} \frac {x ^ {2}}{(x - 3)} = \frac {(2) ^ {2}}{2 - 3} = \frac {4}{- 1} = - 4. \end{array}
$$

Reprint 2025-26

<!-- page 16 of 40 -->

232

MATHEMATICS

(v) First, we rewrite the function as a rational function.

$$
\begin{array}{r l} \left[ \frac {x - 2}{x ^ {2} - x} - \frac {1}{x ^ {3} - 3 x ^ {2} + 2 x} \right] & = \left[ \frac {x - 2}{x (x - 1)} - \frac {1}{x (x ^ {2} - 3 x + 2)} \right] \\ & = \left[ \frac {x - 2}{x (x - 1)} - \frac {1}{x (x - 1) (x - 2)} \right] \\ & = \left[ \frac {x ^ {2} - 4 x + 4 - 1}{x (x - 1) (x - 2)} \right] \\ & = \frac {x ^ {2} - 4 x + 3}{x (x - 1) (x - 2)} \end{array}
$$

Evaluating the function at 1, we get it of the form $\frac{0}{0}$.

Hence

$$
\lim _ {x \to 1} \left[ \frac {x ^ {2} - 2}{x ^ {2} - x} - \frac {1}{x ^ {3} - 3 x ^ {2} + 2 x} \right] = \lim _ {x \to 1} \frac {x ^ {2} - 4 x + 3}{x (x - 1) (x - 2)}
$$

$$
= \lim _ {x \to 1} \frac {(x - 3) (x - 1)}{x (x - 1) (x - 2)}
$$

$$
= \lim _ {x \to 1} \frac {x - 3}{x (x - 2)} = \frac {1 - 3}{1 (1 - 2)} = 2.
$$

We remark that we could cancel the term $(x - 1)$ in the above evaluation because $x \neq 1$.

Evaluation of an important limit which will be used in the sequel is given as a theorem below.

Theorem 2 For any positive integer $n$,

$$
\varliminf_ {x \to a} \frac {x ^ {n} - a ^ {n}}{x - a} = n a ^ {n - 1}.
$$

Remark The expression in the above theorem for the limit is true even if n is any rational number and a is positive.

Reprint 2025-26

<!-- page 17 of 40 -->

LIMITS AND DERIVATIVES

233

Proof Dividing $(x^{n} - a^{n})$ by $(x - a)$, we see that

$$
x ^ {n} - a ^ {n} = (x - a) \left(x ^ {n - 1} + x ^ {n - 2} a + x ^ {n - 3} a ^ {2} + \dots + x a ^ {n - 2} + a ^ {n - 1}\right)
$$

Thus, $\lim_{x\to a}\frac{x^n - a^n}{x - a} = \lim_{x\to a}(x^{n - 1} + x^{n - 2}a + x^{n - 3}a^2 +\dots +x a^{n - 2} + a^{n - 1})$ $= a^{n - 1} + a a^{n - 2} + \ldots +a^{n - 2}(a) + a^{n - 1}$ $= a^{n - 1} + a^{n - 1} + \dots +a^{n - 1} + a^{n - 1}$ (n terms) $= na^{n - 1}$

Example 3 Evaluate:

(i) $\lim_{x\to 1}\frac{x^{15} - 1}{x^{10} - 1}$

(ii) $\lim_{x\to 0}\frac{\sqrt{1 + x} - 1}{x}$

Solution (i) We have

$$
\begin{array}{r l} \lim _ {x \to 1} \frac {x ^ {1 5} - 1}{x ^ {1 0} - 1} = & \lim _ {x \to 1} \left[ \frac {x ^ {1 5} - 1}{x - 1} \div \frac {x ^ {1 0} - 1}{x - 1} \right] \\ = & \lim _ {x \to 1} \left[ \frac {x ^ {1 5} - 1}{x - 1} \right] \div \lim _ {x \to 1} \left[ \frac {x ^ {1 0} - 1}{x - 1} \right] \\ = & 1 5 (1) ^ {1 4} \div 1 0 (1) ^ {9} \text {(by the theorem above)} \end{array}
$$

$$
1 5 \div 1 0 = \frac {3}{2}
$$

(ii) Put $y = 1 + x$, so that $y \to 1$ as $x \to 0$.

Then

$$
\begin{array}{r l} \lim _ {x \to 0} \frac {\sqrt {1 + x} - 1}{x} & = \lim _ {y \to 1} \frac {\sqrt {y} - 1}{y - 1} \\ & = \lim _ {y \to 1} \frac {y ^ {\frac {1}{2}} - 1 ^ {\frac {1}{2}}}{y - 1} \\ & = \frac {1}{2} (1) ^ {\frac {1}{2} - 1} \text {(by the remark above)} = \frac {1}{2} \end{array}
$$

Reprint 2025-26

<!-- page 18 of 40 -->

234

MATHEMATICS

## 12.4 Limits of Trigonometric Functions

The following facts (stated as theorems) about functions in general come in handy in calculating limits of some trigonometric functions.

Theorem 3 Let $f$ and $g$ be two real valued functions with the same domain such that $f(x) \leq g(x)$ for all $x$ in the domain of definition, For some $a$, if both $\lim_{x \to a} f(x)$ and $\lim_{x \to a} g(x)$ exist, then $\lim_{x \to a} f(x) \leq \lim_{x \to a} g(x)$. This is illustrated in Fig 12.8.

![Image block](doc:ef55644/tier:standard/page:18/block:6)

Fig 12.8

Theorem 4 (Sandwich Theorem) Let $f, g$ and $h$ be real functions such that $f(x) \leq g(x) \leq h(x)$ for all $x$ in the common domain of definition. For some real number $a$, if $\lim_{x \to a} f(x) = l = \lim_{x \to a} h(x)$, then $\lim_{x \to a} g(x) = l$. This is illustrated in Fig 12.9.

![Image block](doc:ef55644/tier:standard/page:18/block:9)

Fig 12.9

Given below is a beautiful geometric proof of the following important inequality relating trigonometric functions.

$$
\boxed {\cos x <   \frac {\sin x}{x} <   1 \quad \text {for} 0 <   | x | <   \frac {\pi}{2}}\tag{*}
$$

Reprint 2025-26

<!-- page 19 of 40 -->

LIMITS AND DERIVATIVES

235

Proof We know that $\sin (-x) = -\sin x$ and $\cos (-x) = \cos x$. Hence, it is sufficient

to prove the inequality for $0 < x < \frac{\pi}{2}$.

In the Fig 12.10, O is the centre of the unit circle such that the angle AOC is $x$ radians and $0 < x < \frac{\pi}{2}$. Line segments B A and CD are perpendiculars to OA. Further, join AC. Then

![Image block](doc:ef55644/tier:standard/page:19/block:6)

Area of $\Delta$OAC $<$ Area of sector OAC $<$ Area of $\Delta$ OAB.

Fig 12.10

i.e., $\frac{1}{2}\mathrm{OA.CD} < \frac{x}{2\pi}.\pi .(\mathrm{OA})^2 < \frac{1}{2}\mathrm{OA.AB}$

i.e., CD < x . OA < AB.

From $\Delta$ OCD,

$\sin x = \frac{\mathrm{CD}}{\mathrm{OA}}$ (since $\mathrm{OC} = \mathrm{OA}$) and hence $\mathrm{CD} = \mathrm{OA}\sin x$. Also $\tan x = \frac{\mathrm{AB}}{\mathrm{OA}}$ and hence $\mathrm{AB} = \mathrm{OA}$. $\tan x$. Thus $\mathrm{OA}\sin x < \mathrm{OA}$. $x < \mathrm{OA}$. $\tan x$.

Since length OA is positive, we have $\sin x < x < \tan x$.

Since $0 < x < \frac{\pi}{2}$, $\sin x$ is positive and thus by dividing throughout by $\sin x$, we have $1 < \frac{x}{\sin x} < \frac{1}{\cos x}$. Taking reciprocals throughout, we have $\cos x < \frac{\sin x}{x} < 1$

which complete the proof.

Theorem 5 The following are two important limits.
(i)  $\lim_{x\to0}\frac{\sin x}{x}=1$ .
(ii)  $\lim_{x\to0}\frac{1-\cos x}{x}=0$ .

Proof (i) The inequality in (\*) says that the function $\frac{\sin x}{x}$ is sandwiched between the function $\cos x$ and the constant function which takes value 1.

Reprint 2025-26

<!-- page 20 of 40 -->

236

MATHEMATICS

Further, since $\lim_{x\to 0}\cos x = 1$, we see that the proof of (i) of the theorem is complete by sandwich theorem.

To prove (ii), we recall the trigonometric identity $1 - \cos x = 2\sin^2\left(\frac{x}{2}\right)$. Then

$$
\begin{array}{r l} \lim _ {x \to 0} \frac {1 - \cos x}{x} & = \lim _ {x \to 0} \frac {2 \sin^ {2} \left(\frac {x}{2}\right)}{x} = \lim _ {x \to 0} \frac {\sin \left(\frac {x}{2}\right)}{\frac {x}{2}}. \sin \left(\frac {x}{2}\right) \\ & = \lim _ {x \to 0} \frac {\sin \left(\frac {x}{2}\right)}{\frac {x}{2}}. \lim _ {x \to 0} \sin \left(\frac {x}{2}\right) = 1. 0 = 0 \end{array}
$$

Observe that we have implicitly used the fact that $x \to 0$ is equivalent to $\frac{x}{2} \to 0$. This may be justified by putting $y = \frac{x}{2}$.

Example 4 Evaluate: (i) $\lim_{x\to 0}\frac{\sin 4x}{\sin 2x}$ (ii) $\lim_{x\to 0}\frac{\tan x}{x}$

Solution (i) $\lim_{x\to 0}\frac{\sin 4x}{\sin 2x} = \lim_{x\to 0}\left[\frac{\sin 4x}{4x}.\frac{2x}{\sin 2x}.2\right]$ $= 2.\lim_{x\to 0}\left[\frac{\sin 4x}{4x}\right] \div \left[\frac{\sin 2x}{2x}\right]$ $= 2.\lim_{4x\to 0}\left[\frac{\sin 4x}{4x}\right] \div \lim_{2x\to 0}\left[\frac{\sin 2x}{2x}\right]$ $= 2.1.1 = 2$ (as $x\to 0,4x\to 0$ and $2x\to 0$)

Reprint 2025-26

<!-- page 21 of 40 -->

LIMITS AND DERIVATIVES

237

(ii) We have $\lim_{x\to 0}\frac{\tan x}{x} = \lim_{x\to 0}\frac{\sin x}{x\cos x} = \lim_{x\to 0}\frac{\sin x}{x}.\lim_{x\to 0}\frac{1}{\cos x} = 1.1 = 1$

A general rule that needs to be kept in mind while evaluating limits is the following.

Say, given that the limit $\lim_{x\to a}\frac{f(x)}{g(x)}$ exists and we want to evaluate this. First we check

the value of $f(a)$ and $g(a)$. If both are 0, then we see if we can get the factor which is causing the terms to vanish, i.e., see if we can write $f(x) = f_{1}(x)f_{2}(x)$ so that $f_{1}(a) = 0$ and $f_{2}(a)\neq 0$. Similarly, we write $g(x) = g_{1}(x)g_{2}(x)$, where $g_{1}(a) = 0$ and $g_{2}(a)\neq 0$. Cancel out the common factors from $f(x)$ and $g(x)$ (if possible) and write

$\frac{f(x)}{g(x)} = \frac{p(x)}{q(x)},$ where $q(x)\neq 0.$

Then

$$
\lim _ {x \to a} \frac {f (x)}{g (x)} = \frac {p (a)}{q (a)}
$$

## EXERCISE 12.1

Evaluate the following limits in Exercises 1 to 22.

1. $\lim_{x\to 3}x + 3$

2. $\lim_{x\to \pi}\left(x - \frac{22}{7}\right)$

$$
\lim _ {r \to 1} \pi r ^ {2}
$$

4. $\lim_{x\to 4}\frac{4x + 3}{x - 2}$ 5. $\lim_{x\to -1}\frac{x^{10} + x^5 + 1}{x - 1}$ 6. $\lim_{x\to 0}\frac{(x + 1)^{5} - 1}{x}$

7. $\lim_{x\to 2}\frac{3x^2 - x - 10}{x^2 - 4}$

8. $\lim_{x\to 3}\frac{x^4 - 81}{2x^2 - 5x - 3}$

9. $\lim_{x\to 0}\frac{ax + b}{cx + 1}$

10. $\lim_{z\to 1}\frac{z^{\frac{1}{3}} - 1}{z^{\frac{1}{6}} - 1}$

11. $\lim_{x\to 1}\frac{ax^2 + bx + c}{cx^2 + bx + a},a + b + c\neq 0$

12. $\lim_{x\to -2}\frac{\frac{1}{x} + \frac{1}{2}}{x + 2}$ 13. $\lim_{x\to 0}\frac{\sin ax}{bx}$ 14. $\lim_{x\to 0}\frac{\sin ax}{\sin bx}, a, b \neq 0$

Reprint 2025-26

<!-- page 22 of 40 -->

238

MATHEMATICS

15. $\lim_{x\to \pi}\frac{\sin(\pi - x)}{\pi(\pi - x)}$ 16. $\lim_{x\to 0}\frac{\cos x}{\pi - x}$ 17. $\lim_{x\to 0}\frac{\cos 2x - 1}{\cos x - 1}$

18. $\lim_{x\to 0}\frac{ax + x\cos x}{b\sin x}$ 19. $\lim_{x\to 0}x\sec x$

20. $\lim_{x\to 0}\frac{\sin ax + bx}{ax + \sin bx} a,b,a + b\neq 0,$ 21. $\lim_{x\to 0}(\sec x - \cot x)$

22. $\lim_{x\to \frac{\pi}{2}}\frac{\tan 2x}{x - \frac{\pi}{2}}$

23. Find $\lim_{x\to 0}f(x)$ and $\lim_{x\to 1}f(x)$, where $f(x) = \begin{cases} 2x + 3, & x\leq 0 \\ 3(x + 1), & x > 0 \end{cases}$

24. Find $\lim_{x\to 1}f(x)$, where $f(x) = \left\{ \begin{array}{ll}x^{2} - 1, & x\leq 1\\ -x^{2} - 1, & x > 1 \end{array} \right.$

25. Evaluate $\lim_{x\to 0}f(x)$, where $f(x) = \begin{cases} \frac{|x|}{x}, & x\neq 0\\ 0, & x = 0 \end{cases}$

26. Find $\lim_{x\to 0}f(x)$, where $f(x) = \begin{cases} \frac{x}{|x|}, & x\neq 0\\ 0, & x = 0 \end{cases}$

27. Find $\lim_{x\to 5}f(x)$, where $f(x) = |x| - 5$

28. Suppose  $f(x) = \begin{cases} a + bx, & x < 1 \\ 4, & x = 1 \\ b - ax, & x > 1 \end{cases}$

and if $\lim_{x\to 1}f(x) = f(1)$ what are possible values of $a$ and $b?$

Reprint 2025-26

<!-- page 23 of 40 -->

LIMITS AND DERIVATIVES

239

29. Let $a_1, a_2, \ldots, a_n$ be fixed real numbers and define a function

$$
f (x) = \left(x - a _ {1}\right) \left(x - a _ {2}\right)... \left(x - a _ {n}\right).
$$

What is $\lim_{x\to a_1}f(x)$? For some $a\neq a_1$, $a_2$, ..., $a_n$, compute $\lim_{x\to a}f(x)$.

30. If $f(x) = \begin{cases} |x| + 1, & x < 0 \\ 0, & x = 0 \\ |x| - 1, & x > 0 \end{cases}$

For what value (s) of $a$ does $\lim_{x\to a}f(x)$ exists?

31. If the function $f(x)$ satisfies $\lim_{x\to 1}\frac{f(x) - 2}{x^2 - 1} = \pi$, evaluate $\lim_{x\to 1}f(x)$

32. If $f(x) = \begin{cases} mx^2 + n, & x < 0 \\ nx + m, & 0 \leq x \leq 1 \\ nx^3 + m, & x > 1 \end{cases}$. For what integers $m$ and $n$ does both $\lim_{x \to 0} f(x)$

and $\lim_{x\to 1}f(x)$ exist?

## 12.5 Derivatives

We have seen in the Section 13.2, that by knowing the position of a body at various time intervals it is possible to find the rate at which the position of the body is changing. It is of very general interest to know a certain parameter at various instants of time and try to finding the rate at which it is changing. There are several real life situations where such a process needs to be carried out. For instance, people maintaining a reservoir need to know when will a reservoir overflow knowing the depth of the water at several instances of time, Rocket Scientists need to compute the precise velocity with which the satellite needs to be shot out from the rocket knowing the height of the rocket at various times. Financial institutions need to predict the changes in the value of a particular stock knowing its present value. In these, and many such cases it is desirable to know how a particular parameter is changing with respect to some other parameter. The heart of the matter is derivative of a function at a given point in its domain of definition.

Reprint 2025-26

<!-- page 24 of 40 -->

240

MATHEMATICS

Definition 1 Suppose $f$ is a real valued function and $a$ is a point in its domain of definition. The derivative of $f$ at $a$ is defined by

$$
\lim _ {h \to 0} \frac {f (a + h) - f (a)}{h}
$$

provided this limit exists. Derivative of $f(x)$ at $a$ is denoted by $f'(a)$.

Observe that $f'(a)$ quantifies the change in $f(x)$ at $a$ with respect to $x$.

Example 5 Find the derivative at $x = 2$ of the function $f(x) = 3x$.

Solution We have

$$
\begin{array}{r l} f ^ {\prime} (2) & = \lim _ {h \to 0} \frac {f (2 + h) - f (2)}{h} = \lim _ {h \to 0} \frac {3 (2 + h) - 3 (2)}{h} \\ & = \lim _ {h \to 0} \frac {6 + 3 h - 6}{h} = \lim _ {h \to 0} \frac {3 h}{h} = \lim _ {h \to 0} 3 = 3. \end{array}
$$

The derivative of the function $3x$ at $x = 2$ is 3.

Example 6 Find the derivative of the function $f(x) = 2x^{2} + 3x - 5$ at $x = -1$. Also prove that $f'(0) + 3f'(-1) = 0$.

Solution We first find the derivatives of $f(x)$ at $x = -1$ and at $x = 0$. We have

$$
\begin{array}{l} f ^ {\prime} (- 1) = \lim _ {h \to 0} \frac {f (- 1 + h) - f (- 1)}{h} \\ = \lim _ {h \to 0} \frac {\left[ 2 (- 1 + h) ^ {2} + 3 (- 1 + h) - 5 \right] - \left[ 2 (- 1) ^ {2} + 3 (- 1) - 5 \right]}{h} \\ = \lim _ {h \to 0} \frac {2 h ^ {2} - h}{h} = \lim _ {h \to 0} (2 h - 1) = 2 (0) - 1 = - 1 \\ f ^ {\prime} (0) = \lim _ {h \to 0} \frac {f (0 + h) - f (0)}{h} \\ = \lim _ {h \to 0} \frac {\left[ 2 (0 + h) ^ {2} + 3 (0 + h) - 5 \right] - \left[ 2 (0) ^ {2} + 3 (0) - 5 \right]}{h} \end{array}
$$

and

Reprint 2025-26

<!-- page 25 of 40 -->

LIMITS AND DERIVATIVES

241

$$
= \lim _ {h \to 0} \frac {2 h ^ {2} + 3 h}{h} = \lim _ {h \to 0} (2 h + 3) = 2 (0) + 3 = 3
$$

Clearly  $f'(0)+3f'(-1)=0$

Remark At this stage note that evaluating derivative at a point involves effective use of various rules, limits are subjected to. The following illustrates this.

Example 7 Find the derivative of $\sin x$ at $x = 0$.

Solution Let $f(x) = \sin x$. Then

$$
\begin{array}{r l} f ^ {\prime} (0) & = \lim _ {h \to 0} \frac {f (0 + h) - f (0)}{h} \\ & = \lim _ {h \to 0} \frac {\sin (0 + h) - \sin (0)}{h} = \lim _ {h \to 0} \frac {\sin h}{h} = 1 \end{array}
$$

Example 8 Find the derivative of $f(x) = 3$ at $x = 0$ and at $x = 3$.

Solution Since the derivative measures the change in function, intuitively it is clear that the derivative of the constant function must be zero at every point. This is indeed, supported by the following computation.

Similarly

$$
\begin{array}{l} f ^ {\prime} (0) = \lim _ {h \to 0} \frac {f (0 + h) - f (0)}{h} = \lim _ {h \to 0} \frac {3 - 3}{h} = \lim _ {h \to 0} \frac {0}{h} = 0. \\ f ^ {\prime} (3) = \lim _ {h \to 0} \frac {f (3 + h) - f (3)}{h} = \lim _ {h \to 0} \frac {3 - 3}{h} = 0. \end{array}
$$

We now present a geometric interpretation of derivative of a function at a point. Let  $y = f(x)$  be a function and let  $P = (a, f(a))$  and  $Q = (a + h, f(a + h))$  be two points close to each other on the graph of this function. The Fig 12.11 is now self explanatory.

![Chart block](doc:ef55644/tier:standard/page:25/block:14)

Fig 12.11

Reprint 2025-26

<!-- page 26 of 40 -->

242

MATHEMATICS

We know that  $f'(a)=\lim_{h\to0}\frac{f(a+h)-f(a)}{h}$

From the triangle PQR, it is clear that the ratio whose limit we are taking is precisely equal to $\tan (\mathrm{QPR})$ which is the slope of the chord PQ. In the limiting process, as $h$ tends to 0, the point Q tends to P and we have

$$
\lim _ {h \to 0} \frac {f (a + h) - f (a)}{h} = \lim _ {\mathrm{Q} \to \mathrm{P}} \frac {\mathrm{QR}}{\mathrm{PR}}
$$

This is equivalent to the fact that the chord PQ tends to the tangent at P of the curve $y = f(x)$. Thus the limit turns out to be equal to the slope of the tangent. Hence

$$
f ^ {\prime} (a) = \tan \psi .
$$

For a given function $f$ we can find the derivative at every point. If the derivative exists at every point, it defines a new function called the derivative of $f$. Formally, we define derivative of a function as follows.

Definition 2 Suppose $f$ is a real valued function, the function defined by

$$
\lim _ {h \to 0} \frac {f (x + h) - f (x)}{h}
$$

wherever the limit exists is defined to be the derivative of $f$ at $x$ and is denoted by $f'(x)$. This definition of derivative is also called the first principle of derivative.

Thus

$$
f ^ {\prime} (x) = \lim _ {h \to 0} \frac {f (x + h) - f (x)}{h}
$$

Clearly the domain of definition of $f'(x)$ is wherever the above limit exists. There are different notations for derivative of a function. Sometimes $f'(x)$ is denoted by $\frac{d}{dx}\big(f(x)\big)$ or if $y = f(x)$, it is denoted by $\frac{dy}{dx}$. This is referred to as derivative of $f(x)$ or $y$ with respect to $x$. It is also denoted by D ($f(x)$). Further, derivative of $f$ at $x = a$ is also denoted by $\frac{d}{dx}f(x)\bigg|_a$ or $\frac{df}{dx}\bigg|_a$ or even $\left(\frac{df}{dx}\right)_{x=a}$.

Example 9 Find the derivative of $f(x) = 10x$.

Solution Since  $f'(x) = \lim_{h \to 0} \frac{f(x + h) - f(x)}{h}$

Reprint 2025-26

<!-- page 27 of 40 -->

LIMITS AND DERIVATIVES

243

$$
\begin{array}{l} = \lim _ {h \to 0} \frac {1 0 (x + h) - 1 0 (x)}{h} \\ = \lim _ {h \to 0} \frac {1 0 h}{h} = \lim _ {h \to 0} (1 0) = 1 0. \end{array}
$$

Example 10 Find the derivative of $f(x) = x^2$.

Solution We have, $f'(x) = \lim_{h \to 0} \frac{f(x + h) - f(x)}{h}$

$= \lim_{h \to 0} \frac{(x + h)^2 - (x)^2}{h} = \lim_{h \to 0} (h + 2x) = 2x$

Example 11 Find the derivative of the constant function $f(x) = a$ for a fixed real number $a$.

Solution We have, $f'(x) = \lim_{h \to 0} \frac{f(x + h) - f(x)}{h}$

$= \lim_{h \to 0} \frac{a - a}{h} = \lim_{h \to 0} \frac{0}{h} = 0 \text{ as } h \neq 0$

Example 12 Find the derivative of $f(x) = \frac{1}{x}$

Solution We have $f'(x) = \lim_{h \to 0} \frac{f(x + h) - f(x)}{h}$

$= \lim_{h \to 0} \frac{\frac{1}{(x + h)} - \frac{1}{x}}{h}$

$= \lim_{h \to 0} \frac{1}{h} \left[ \frac{x - (x + h)}{x(x + h)} \right]$

$= \lim_{h \to 0} \frac{1}{h} \left[ \frac{-h}{x(x + h)} \right] \quad = \lim_{h \to 0} \frac{-1}{x(x + h)} = -\frac{1}{x^2}$

Reprint 2025-26

<!-- page 28 of 40 -->

244

MATHEMATICS

12.5.1 Algebra of derivative of functions Since the very definition of derivatives involve limits in a rather direct fashion, we expect the rules for derivatives to follow closely that of limits. We collect these in the following theorem.

Theorem 5 Let $f$ and $g$ be two functions such that their derivatives are defined in a common domain. Then

(i) Derivative of sum of two functions is sum of the derivatives of the functions.

$$
\frac {d}{d x} \Big [ f (x) + g (x) \Big ] = \frac {d}{d x} f (x) + \frac {d}{d x} g (x).
$$

(ii) Derivative of difference of two functions is difference of the derivatives of the functions.

$$
\frac {d}{d x} \Big [ f (x) - g (x) \Big ] = \frac {d}{d x} f (x) - \frac {d}{d x} g (x).
$$

(iii) Derivative of product of two functions is given by the following product rule.

$$
\left| \frac {d}{d x} \left[ f (x) \cdot g (x) \right] = \frac {d}{d x} f (x) \cdot g (x) + f (x) \cdot \frac {d}{d x} g (x) \right|
$$

(iv) Derivative of quotient of two functions is given by the following quotient rule (whenever the denominator is non-zero).

$$
\frac {d}{d x} \left(\frac {f (x)}{g (x)}\right) = \frac {\frac {d}{d x} f (x) \cdot g (x) - f (x) \frac {d}{d x} g (x)}{\left(g (x)\right) ^ {2}}
$$

The proofs of these follow essentially from the analogous theorem for limits. We will not prove these here. As in the case of limits this theorem tells us how to compute derivatives of special types of functions. The last two statements in the theorem may be restated in the following fashion which aids in recalling them easily:

Let $u = f(x)$ and $v = g(x)$. Then

$$
\left(u v\right) ^ {\prime} = u ^ {\prime} v + u v ^ {\prime}
$$

This is referred to a Leibnitz rule for differentiating product of functions or the product rule. Similarly, the quotient rule is

Reprint 2025-26

<!-- page 29 of 40 -->

LIMITS AND DERIVATIVES

245

$$
\left(\frac {u}{v}\right) ^ {\prime} = \frac {u ^ {\prime} v - u v ^ {\prime}}{v ^ {2}}
$$

Now, let us tackle derivatives of some standard functions.

It is easy to see that the derivative of the function $f(x) = x$ is the constant

function 1. This is because $f'(x) = \lim_{h \to 0} \frac{f(x + h) - f(x)}{h} = \lim_{h \to 0} \frac{x + h - x}{h}$
$= \lim_{h \to 0} 1 = 1$.

We use this and the above theorem to compute the derivative of $f(x) = 10x = x + \dots + x$ (ten terms). By (i) of the above theorem

$$
\begin{array}{r l} \frac {d f (x)}{d x} & = \frac {d}{d x} (x + \dots + x) (\text {ten terms}) \\ & = \frac {d}{d x} x + \dots + \frac {d}{d x} x (\text {ten terms}) \\ & = 1 + \dots + 1 (\text {ten terms}) = 1 0. \end{array}
$$

We note that this limit may be evaluated using product rule too. Write $f(x) = 10x = uv$, where $u$ is the constant function taking value 10 everywhere and $v(x) = x$. Here, $f(x) = 10x = uv$ we know that the derivative of $u$ equals 0. Also derivative of $v(x) = x$ equals 1. Thus by the product rule we have

$$
f ^ {\prime} (x) = (1 0 x) ^ {\prime} = (u v) ^ {\prime} = u ^ {\prime} v + u v ^ {\prime} = 0. x + 1 0. 1 = 1 0
$$

On similar lines the derivative of $f(x) = x^2$ may be evaluated. We have $f(x) = x^2 = x$. $x$ and hence

$$
\begin{array}{r l} \frac {d f}{d x} = & \frac {d}{d x} (x. x) = \frac {d}{d x} (x). x + x. \frac {d}{d x} (x) \\ = & 1. x + x. 1 = 2 x. \end{array}
$$

More generally, we have the following theorem.

Theorem 6 Derivative of $f(x) = x^n$ is $nx^{n-1}$ for any positive integer $n$.

Proof By definition of the derivative function, we have

$$
f ^ {\prime} (x) = \lim _ {h \to 0} \frac {f (x + h) - f (x)}{h} = \lim _ {h \to 0} \frac {(x + h) ^ {n} - x ^ {n}}{h}.
$$

Reprint 2025-26

<!-- page 30 of 40 -->

246

MATHEMATICS

Binomial theorem tells that $(x + h)^n = \left(nC_0\right)x^n + \left(nC_1\right)x^{n-1}h + \ldots + \left(nC_n\right)h^n$ and hence $(x + h)^n - x^n = h(nx^{n-1} + \ldots + h^{n-1})$. Thus

$$
\begin{array}{r l} \frac {d f (x)}{d x} & = \lim _ {h \to 0} \frac {(x + h) ^ {n} - x ^ {n}}{h} \\ & = \lim _ {h \to 0} \frac {h (n x ^ {n - 1} + \dots + h ^ {n - 1})}{h} \\ & = \lim _ {h \to 0} (n x ^ {n - 1} + \dots + h ^ {n - 1}) = n x ^ {n - 1}. \end{array}
$$

Alternatively, we may also prove this by induction on n and the product rule as follows. The result is true for n = 1, which has been proved earlier. We have

$$
\begin{array}{r l} \frac {d}{d x} \Big (x ^ {n} \Big) & = \frac {d}{d x} \Big (x. x ^ {n - 1} \Big) \\ & = \frac {d}{d x} \Big (x \Big). \Big (x ^ {n - 1} \Big) + x. \frac {d}{d x} \Big (x ^ {n - 1} \Big) (\text {by product rule}) \\ & = 1. x ^ {n - 1} + x. \Big ((n - 1) x ^ {n - 2} \Big) (\text {by induction hypothesis}) \\ & = x ^ {n - 1} + (n - 1) x ^ {n - 1} = n x ^ {n - 1}. \end{array}
$$

Remark The above theorem is true for all powers of $x$, i.e., $n$ can be any real number (but we will not prove it here).

12.5.2 Derivative of polynomials and trigonometric functions We start with the following theorem which tells us the derivative of a polynomial function.

Theorem 7 Let $f(x) = a_{n}x^{n} + a_{n - 1}x^{n - 1} + \dots +a_{1}x + a_{0}$ be a polynomial function, where $a_{i}s$ are all real numbers and $a_{n}\neq 0$. Then, the derivative function is given by

$$
\frac {d f (x)}{d x} = n a _ {n} x ^ {n - 1} + (n - 1) a _ {n - 1} x ^ {x - 2} + \dots + 2 a _ {2} x + a _ {1}.
$$

Proof of this theorem is just putting together part (i) of Theorem 5 and Theorem 6. Example 13 Compute the derivative of $6x^{100} - x^{55} + x$.

Solution A direct application of the above theorem tells that the derivative of the above function is $600x^{99} - 55x^{54} + 1$.

Reprint 2025-26

<!-- page 31 of 40 -->

LIMITS AND DERIVATIVES

247

Example 14 Find the derivative of $f(x) = 1 + x + x^{2} + x^{3} + \ldots + x^{50}$ at $x = 1$.

Solution A direct application of the above Theorem 6 tells that the derivative of the above function is $1 + 2x + 3x^{2} + \ldots + 50x^{49}$. At $x = 1$ the value of this function equals

$$
1 + 2 (1) + 3 (1) ^ {2} + \dots + 5 0 (1) ^ {4 9} = 1 + 2 + 3 + \dots + 5 0 = \frac {(5 0) (5 1)}{2} = 1 2 7 5.
$$

Example 15 Find the derivative of $f(x) = \frac{x + 1}{x}$

Solution Clearly this function is defined everywhere except at $x = 0$. We use the quotient rule with $u = x + 1$ and $v = x$. Hence $u' = 1$ and $v' = 1$. Therefore

$$
\frac {d f (x)}{d x} = \frac {d}{d x} \left(\frac {x + 1}{x}\right) = \frac {d}{d x} \left(\frac {u}{v}\right) = \frac {u ^ {\prime} v - u v ^ {\prime}}{v ^ {2}} = \frac {1 (x) - (x + 1) 1}{x ^ {2}} = - \frac {1}{x ^ {2}}
$$

Example 16 Compute the derivative of $\sin x$.

Solution Let $f(x) = \sin x$. Then

$$
\begin{array}{l} \frac {d f (x)}{d x} = \lim _ {h \to 0} \frac {f (x + h) - f (x)}{h} = \lim _ {h \to 0} \frac {\sin (x + h) - \sin (x)}{h} \\ = \lim _ {h \to 0} \frac {2 \cos \left(\frac {2 x + h}{2}\right) \sin \left(\frac {h}{2}\right)}{h} (\text {using formula for} \sin A - \sin B) \\ = \lim _ {h \to 0} \cos \left(x + \frac {h}{2}\right). \lim _ {h \to 0} \frac {\sin \frac {h}{2}}{\frac {h}{2}} = \cos x. 1 = \cos x. \end{array}
$$

Example 17 Compute the derivative of tan $x$.

Solution Let $f(x) = \tan x$. Then

$$
\begin{array}{r l} \frac {d f (x)}{d x} & = \lim _ {h \to 0} \frac {f (x + h) - f (x)}{h} = \lim _ {h \to 0} \frac {\tan (x + h) - \tan (x)}{h} \\ & = \lim _ {h \to 0} \frac {1}{h} \left[ \frac {\sin (x + h)}{\cos (x + h)} - \frac {\sin x}{\cos x} \right] \end{array}
$$

Reprint 2025-26

<!-- page 32 of 40 -->

248

MATHEMATICS

$$
\begin{array}{l} = \lim _ {h \to 0} \left[ \frac {\sin (x + h) \cos x - \cos (x + h) \sin x}{h \cos (x + h) \cos x} \right] \\ = \lim _ {h \to 0} \frac {\sin (x + h - x)}{h \cos (x + h) \cos x} (\text {using formula for} \sin (\mathrm{A} + \mathrm{B})) \\ = \lim _ {h \to 0} \frac {\sin h}{h}. \lim _ {h \to 0} \frac {1}{\cos (x + h) \cos x} \\ = 1. \frac {1}{\cos^ {2} x} = \sec^ {2} x. \end{array}
$$

Example 18 Compute the derivative of $f(x) = \sin^2 x$.

Solution We use the Leibnitz product rule to evaluate this.

$$
\begin{array}{r l} \frac {d f (x)}{d x} & = \frac {d}{d x} (\sin x \sin x) \\ & = (\sin x) ^ {\prime} \sin x + \sin x (\sin x) ^ {\prime} \\ & = (\cos x) \sin x + \sin x (\cos x) \\ & = 2 \sin x \cos x = \sin 2 x. \end{array}
$$

## EXERCISE 12.2

1. Find the derivative of $x^{2} - 2$ at $x = 10$.

2. Find the derivative of $x$ at $x = 1$.

3. Find the derivative of $99x$ at $x = 100$.

4. Find the derivative of the following functions from first principle.
(i)  $x^{3}-27$ 
(ii)  $(x-1)(x-2)$ 
(iii)  $\frac{1}{x^{2}}$ 
(iv)  $\frac{x+1}{x-1}$

5. For the function

$$
f (x) = \frac {x ^ {1 0 0}}{1 0 0} + \frac {x ^ {9 9}}{9 9} + \dots + \frac {x ^ {2}}{2} + x + 1.
$$

Reprint 2025-26

<!-- page 33 of 40 -->

LIMITS AND DERIVATIVES

249

Prove that $f'(1) = 100f'(0)$,

6. Find the derivative of $x^n + ax^{n-1} + a^2 x^{n-2} + \ldots + a^{n-1}x + a^n$ for some fixed real number $a$.

7. For some constants $a$ and $b$, find the derivative of (i) $\left(x - a\right)\left(x - b\right)$ (ii) $\left(ax^2 + b\right)^2$ (iii) $\frac{x - a}{x - b}$

8. Find the derivative of $\frac{x^n - a^n}{x - a}$ for some constant $a$.

9. Find the derivative of
(i)  $2x - \frac{3}{4}$ 
(ii)  $(5x^{3} + 3x - 1)(x - 1)$ 
(iii)  $x^{-3}(5 + 3x)$ 
(iv)  $x^{5}(3 - 6x^{-9})$ 
(v)  $x^{-4}(3 - 4x^{-5})$ 
(vi)  $\frac{2}{x + 1} - \frac{x^{2}}{3x - 1}$

10. Find the derivative of $\cos x$ from first principle.

11. Find the derivative of the following functions:
(i)  $\sin x \cos x$  (ii)  $\sec x$  (iii)  $5 \sec x + 4 \cos x$ 
(iv)  $\csc x$  (v)  $3 \cot x + 5 \csc x$ 
(vi)  $5 \sin x - 6 \cos x + 7$  (vii)  $2 \tan x - 7 \sec x$

## Miscellaneous Examples

Example 19 Find the derivative of $f$ from the first principle, where $f$ is given by (i) $f(x) = \frac{2x + 3}{x - 2}$ (ii) $f(x) = x + \frac{1}{x}$

Solution (i) Note that function is not defined at $x = 2$. But, we have

$$
f ^ {\prime} (x) = \lim _ {h \rightarrow 0} \frac {f (x + h) - f (x)}{h} = \lim _ {h \rightarrow 0} \frac {\frac {2 (x + h) + 3}{x + h - 2} - \frac {2 x + 3}{x - 2}}{h}
$$

Reprint 2025-26

<!-- page 34 of 40 -->

250

MATHEMATICS

$$
\begin{array}{l} = \lim _ {h \to 0} \frac {(2 x + 2 h + 3) (x - 2) - (2 x + 3) (x + h - 2)}{h (x - 2) (x + h - 2)} \\ = \lim _ {h \to 0} \frac {(2 x + 3) (x - 2) + 2 h (x - 2) - (2 x + 3) (x - 2) - h (2 x + 3)}{h (x - 2) (x + h - 2)} \\ = \lim _ {h \to 0} \frac {- 7}{(x - 2) (x + h - 2)} = - \frac {7}{(x - 2) ^ {2}} \end{array}
$$

Again, note that the function $f'$ is also not defined at $x = 2$.

(ii) The function is not defined at $x = 0$. But, we have

$$
\begin{array}{l} f ^ {\prime} (x) = \lim _ {h \to 0} \frac {f (x + h) - f (x)}{h} = \lim _ {h \to 0} \frac {\left(x + h + \frac {1}{x + h}\right) - \left(x + \frac {1}{x}\right)}{h} \\ = \lim _ {h \to 0} \frac {1}{h} \left[ h + \frac {1}{x + h} - \frac {1}{x} \right] \\ = \lim _ {h \to 0} \frac {1}{h} \left[ h + \frac {x - x - h}{x (x + h)} \right] = \lim _ {h \to 0} \frac {1}{h} \left[ h \left(1 - \frac {1}{x (x + h)}\right) \right] \\ = \lim _ {h \to 0} \left[ 1 - \frac {1}{x (x + h)} \right] = 1 - \frac {1}{x ^ {2}} \end{array}
$$

Again, note that the function $f'$ is not defined at $x = 0$.

Example 20 Find the derivative of $f(x)$ from the first principle, where $f(x)$ is

(i) $\sin x + \cos x$

(ii) $x\sin x$

$$
\begin{array}{l} \text {Solution (i) we have} f ^ {\prime} (x) = \frac {f (x + h) - f (x)}{h} \\ \quad = \lim _ {h \to 0} \frac {\sin (x + h) + \cos (x + h) - \sin x - \cos x}{h} \\ \quad = \lim _ {h \to 0} \frac {\sin x \cos h + \cos x \sin h + \cos x \cos h - \sin x \sin h - \sin x - \cos x}{h} \end{array}
$$

Reprint 2025-26

<!-- page 35 of 40 -->

LIMITS AND DERIVATIVES

251

$$
\begin{array}{l} = \lim _ {h \to 0} \frac {\sin h (\cos x - \sin x) + \sin x (\cos h - 1) + \cos x (\cos h - 1)}{h} \\ = \lim _ {h \to 0} \frac {\sin h}{h} (\cos x - \sin x) + \lim _ {h \to 0} \sin x \frac {(\cos h - 1)}{h} + \lim _ {h \to 0} \cos x \frac {(\cos h - 1)}{h} \\ = \cos x - \sin x \end{array}\tag{ii}
$$

$$
\begin{array}{l} f ^ {\prime} (x) = \lim _ {h \to 0} \frac {f (x + h) - f (x)}{h} = \lim _ {h \to 0} \frac {(x + h) \sin (x + h) - x \sin x}{h} \\ = \lim _ {h \to 0} \frac {(x + h) (\sin x \cos h + \sin h \cos x) - x \sin x}{h} \\ = \lim _ {h \to 0} \frac {x \sin x (\cos h - 1) + x \cos x \sin h + h (\sin x \cos h + \sin h \cos x)}{h} \\ = \lim _ {h \to 0} \frac {x \sin x (\cos h - 1)}{h} + \lim _ {h \to 0} x \cos x \frac {\sin h}{h} + \lim _ {h \to 0} (\sin x \cos h + \sin h \cos x) \\ = x \cos x + \sin x \end{array}
$$

Example 21 Compute derivative of

$$
(\mathrm{i}) f (x) = \sin 2 x
$$

$$
g (x) = \cot x
$$

Solution (i) Recall the trigonometric formula $\sin 2x = 2\sin x\cos x$. Thus

$$
\begin{array}{r l} \frac {d f (x)}{d x} & = \frac {d}{d x} \big (2 \sin x \cos x \big) = 2 \frac {d}{d x} \big (\sin x \cos x \big) \\ & = 2 \Big [ \big (\sin x \big) ^ {\prime} \cos x + \sin x \big (\cos x \big) ^ {\prime} \Big ] \\ & = 2 \Big [ \big (\cos x \big) \cos x + \sin x \big (- \sin x \big) \Big ] \\ & = 2 \Big (\cos^ {2} x - \sin^ {2} x \Big) \end{array}
$$

(ii) By definition, $\mathrm{g}(x) = \cot x = \frac{\cos x}{\sin x}$. We use the quotient rule on this function wherever it is defined. $\frac{dg}{dx} = \frac{d}{dx} (\cot x) = \frac{d}{dx}\left(\frac{\cos x}{\sin x}\right)$

Reprint 2025-26

<!-- page 36 of 40 -->

(i)

(ii)

252

MATHEMATICS

$$
\begin{array}{l} = \frac {(\cos x) ^ {\prime} (\sin x) - (\cos x) (\sin x) ^ {\prime}}{(\sin x) ^ {2}} \\ = \frac {(- \sin x) (\sin x) - (\cos x) (\cos x)}{(\sin x) ^ {2}} \\ = - \frac {\sin^ {2} x + \cos^ {2} x}{\sin^ {2} x} = - \sec^ {2} x \end{array}
$$

Alternatively, this may be computed by noting that  $\cot x = \frac{1}{\tan x}$ . Here, we use the fact that the derivative of  $\tan x$  is  $sec^{2}x$  which we saw in Example 17 and also that the derivative of the constant function is 0.

$$
\left| \begin{array}{l} \frac {d g}{d x} = \frac {d}{d x} (\cot x) = \frac {d}{d x} \left(\frac {1}{\tan x}\right) \\ = \frac {(1) ^ {\prime} (\tan x) - (1) (\tan x) ^ {\prime}}{(\tan x) ^ {2}} \\ = \frac {(0) (\tan x) - (\sec x) ^ {2}}{(\tan x) ^ {2}} \\ = \frac {- \sec^ {2} x}{\tan^ {2} x} = - \sec^ {2} x \end{array} \right|
$$

Example 22 Find the derivative of

$$
\frac {x ^ {5} - \cos x}{\sin x}
$$

$$
\frac {x + \cos x}{\tan x}
$$

Solution (i) Let $h(x) = \frac{x^5 - \cos x}{\sin x}$. We use the quotient rule on this function wherever it is defined.

$$
h ^ {\prime} (x) = \frac {(x ^ {5} - \cos x) ^ {\prime} \sin x - (x ^ {5} - \cos x) (\sin x) ^ {\prime}}{(\sin x) ^ {2}}
$$

Reprint 2025-26

<!-- page 37 of 40 -->

LIMITS AND DERIVATIVES

253

$$
\begin{array}{l} = \frac {(5 x ^ {4} + \sin x) \sin x - (x ^ {5} - \cos x) \cos x}{\sin^ {2} x} \\ = \frac {- x ^ {5} \cos x + 5 x ^ {4} \sin x + 1}{(\sin x) ^ {2}} \end{array}
$$

(ii) We use quotient rule on the function $\frac{x + \cos x}{\tan x}$ wherever it is defined.

$$
\begin{array}{r l} h ^ {\prime} (x) & = \frac {(x + \cos x) ^ {\prime} \tan x - (x + \cos x) (\tan x) ^ {\prime}}{(\tan x) ^ {2}} \\ & = \frac {(1 - \sin x) \tan x - (x + \cos x) \sec^ {2} x}{(\tan x) ^ {2}} \end{array}
$$

Miscellaneous Exercise on Chapter 12

1. Find the derivative of the following functions from first principle:
(i) -x (ii)  $(-x)^{-1}$  (iii)  $\sin(x+1)$  (iv)  $\cos\left(x-\frac{\pi}{8}\right)$

Find the derivative of the following functions (it is to be understood that $a, b, c, d, p, q, r$ and $s$ are fixed non-zero constants and $m$ and $n$ are integers):
2. $(x + a)$
3. $(px + q)\left(\frac{r}{x} + s\right)$
4. $(ax + b)(cx + d)^2$
5. $\frac{ax + b}{cx + d}$
6. $\frac{1 + \frac{1}{x}}{1 - \frac{1}{x}}$
7. $\frac{1}{ax^2 + bx + c}$
8. $\frac{ax + b}{px^2 + qx + r}$
9. $\frac{px^2 + qx + r}{ax + b}$
10. $\frac{a}{x^4} - \frac{b}{x^2} + \cos x$
11. $4\sqrt{x} - 2$
12. $(ax + b)^n$
13. $(ax + b)^n(cx + d)^m$
14. $\sin (x + a)$
15. $\csc x \cot x$
16. $\frac{\cos x}{1 + \sin x}$

Reprint 2025-26

<!-- page 38 of 40 -->

254

MATHEMATICS

17. $\frac{\sin x + \cos x}{\sin x - \cos x}$ 18. $\frac{\sec x - 1}{\sec x + 1}$ 19. $\sin^n x$

20. $\frac{a + b\sin x}{c + d\cos x}$ 21. $\frac{\sin(x + a)}{\cos x}$ 22. $x^4 (5\sin x - 3\cos x)$

23. $\left(x^{2} + 1\right)\cos x$ 24. $\left(ax^{2} + \sin x\right)\left(p + q\cos x\right)$

25. $(x + \cos x)(x - \tan x)$ 26. $\frac{4x + 5\sin x}{3x + 7\cos x}$ 27. $\frac{x^2\cos\left(\frac{\pi}{4}\right)}{\sin x}$

28. $\frac{x}{1 + \tan x}$ 29. $(x + \sec x)(x - \tan x)$ 30. $\frac{x}{\sin^n x}$

## Summary

The expected value of the function as dictated by the points to the left of a point defines the left hand limit of the function at that point. Similarly the right hand limit.

Limit of a function at a point is the common value of the left and right hand limits, if they coincide.

For a function $f$ and a real number $a$, $\lim_{x \to a} f(x)$ and $f(a)$ may not be same (In fact, one may be defined and not the other one).

For functions $f$ and $g$ the following holds:

$$
\lim _ {x \to a} \big [ f (x) \pm g (x) \big ] = \lim _ {x \to a} f (x) \pm \lim _ {x \to a} g (x)
$$

$$
\lim _ {x \to a} \big [ f (x). g (x) \big ] = \lim _ {x \to a} f (x). \lim _ {x \to a} g (x)
$$

$$
\varliminf_ {x \to a} \left[ \frac {f (x)}{g (x)} \right] = \frac {\lim _ {x \to a} f (x)}{\lim _ {x \to a} g (x)}
$$

$\diamond$ Following are some of the standard limits $\lim_{x\to a}\frac{x^n - a^n}{x - a} = na^{n - 1}$

Reprint 2025-26

<!-- page 39 of 40 -->

LIMITS AND DERIVATIVES

255

$$
\lim _ {x \to 0} \frac {\sin x}{x} = 1
$$

$$
\lim _ {x \to 0} \frac {1 - \cos x}{x} = 0
$$

The derivative of a function $f$ at $a$ is defined by

$$
f ^ {\prime} (a) = \lim _ {h \to 0} \frac {f (a + h) - f (a)}{h}
$$

Derivative of a function $f$ at any point $x$ is defined by

$$
f ^ {\prime} (x) = \frac {d f (x)}{d x} = \lim _ {h \to 0} \frac {f (x + h) - f (x)}{h}
$$

For functions $u$ and $v$ the following holds:

$$
(u \pm v) ^ {\prime} = u ^ {\prime} \pm v ^ {\prime}
$$

$$
(u v) ^ {\prime} = u ^ {\prime} v + u v ^ {\prime}
$$

$\left(\frac{u}{v}\right)^{\prime}=\frac{u^{\prime}v-uv^{\prime}}{v^{2}}$ provided all are defined.

◆ Following are some of the standard derivatives.

$$
\frac {d}{d x} (x ^ {n}) = n x ^ {n - 1}
$$

$$
\frac {d}{d x} (\sin x) = \cos x
$$

$$
\frac {d}{d x} (\cos x) = - \sin x
$$

## Historical Note

In the history of mathematics two names are prominent to share the credit for inventing calculus, Issac Newton (1642 - 1727) and G.W. Leibnitz (1646 - 1717). Both of them independently invented calculus around the seventeenth century. After the advent of calculus many mathematicians contributed for further development of calculus. The rigorous concept is mainly attributed to the great

Reprint 2025-26

<!-- page 40 of 40 -->

256

MATHEMATICS

mathematicians, A.L. Cauchy, J.L. Lagrange and Karl Weierstrass. Cauchy gave the foundation of calculus as we have now generally accepted in our textbooks. Cauchy used D'Alembert's limit concept to define the derivative of a function. Starting with definition of a limit, Cauchy gave examples such as the limit of

$\frac{\sin \alpha}{\alpha}$ for $\alpha = 0$. He wrote $\frac{\Delta y}{\Delta x} = \frac{f(x + i) - f(x)}{i}$, and called the limit for $i \to 0$, the "function derive'e, $y'$ for $f'(x)$".

Before 1900, it was thought that calculus is quite difficult to teach. So calculus became beyond the reach of youngsters. But just in 1900, John Perry and others in England started propagating the view that essential ideas and methods of calculus were simple and could be taught even in schools. F.L. Griffin, pioneered the teaching of calculus to first year students. This was regarded as one of the most daring act in those days.

Today not only the mathematics but many other subjects such as Physics, Chemistry, Economics and Biological Sciences are enjoying the fruits of calculus.

Reprint 2025-26