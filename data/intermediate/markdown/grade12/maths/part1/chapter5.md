<!-- page 1 of 43 -->

The image provided is a QR code. As per the instructions, I am to process text and non-text content in standard OCR text. However, since there is no textual content to extract or convert from it, and since you do not use text for OCR content, the correct OCR output is an empty string.

Chapter

12079CHOS

5

# CONTINUITY AND DIFFERENTIABILITY

The whole of science is nothing more than a refinement of everyday thinking." — ALBERT EINSTEIN

## 5.1 Introduction

This chapter is essentially a continuation of our study of differentiation of functions in Class XI. We had learnt to differentiate certain functions like polynomial functions and trigonometric functions. In this chapter, we introduce the very important concepts of continuity, differentiability and relations between them. We will also learn differentiation of inverse trigonometric functions. Further, we introduce a new class of functions called exponential and logarithmic functions. These functions lead to powerful techniques of differentiation. We illustrate certain geometrically obvious conditions through differential calculus. In the process, we will learn some fundamental theorems in this area.

## 5.2 Continuity

![Image block](doc:8b97716/tier:standard/page:1/block:10)

Sir Issac Newton (1642-1727)

We start the section with two informal examples to get a feel of continuity. Consider the function

$$
f (x) = \left\{ \begin{array}{l} 1, \text {if} x \leq 0 \\ 2, \text {if} x > 0 \end{array} \right.
$$

This function is of course defined at every point of the real line. Graph of this function is given in the Fig 5.1. One can deduce from the graph that the value of the function at nearby points on $x$-axis remain close to each other except at $x = 0$. At the points near and to the left of 0, i.e., at points like -0.1, -0.01, -0.001, the value of the function is 1. At the points near and to the right of 0, i.e., at points like 0.1, 0.01,

![Image block](doc:8b97716/tier:standard/page:1/block:15)

Fig 5.1

Reprint 2025-26

<!-- page 2 of 43 -->

CONTINUITY AND DIFFERENTIABILITY

105

0.001, the value of the function is 2. Using the language of left and right hand limits, we may say that the left (respectively right) hand limit of $f$ at 0 is 1 (respectively 2). In particular the left and right hand limits do not coincide. We also observe that the value of the function at $x = 0$ coincides with the left hand limit. Note that when we try to draw the graph, we cannot draw it in one stroke, i.e., without lifting pen from the plane of the paper, we can not draw the graph of this function. In fact, we need to lift the pen when we come to 0 from left. This is one instance of function being not continuous at $x = 0$.

Now, consider the function defined as

$$
f (x) = \left\{ \begin{array}{l} 1, \text {if} x \neq 0 \\ 2, \text {if} x = 0 \end{array} \right.
$$

This function is also defined at every point. Left and the right hand limits at $x = 0$

are both equal to 1. But the value of the function at $x = 0$ equals 2 which does not coincide with the common value of the left and right hand limits. Again, we note that we cannot draw the graph of the function without lifting the pen. This is yet another instance of a function being not continuous at $x = 0$.

![Image block](doc:8b97716/tier:standard/page:2/block:8)

Naively, we may say that a function is continuous at a fixed point if we can draw the graph of the function around that point without lifting the pen from the plane of the paper.

Fig 5.2

Mathematically, it may be phrased precisely as follows:

Definition 1 Suppose $f$ is a real function on a subset of the real numbers and let $c$ be a point in the domain of $f$. Then $f$ is continuous at $c$ if

$$
\lim _ {x \to c} f (x) = f (c)
$$

More elaborately, if the left hand limit, right hand limit and the value of the function at $x = c$ exist and equal to each other, then $f$ is said to be continuous at $x = c$. Recall that if the right hand and left hand limits at $x = c$ coincide, then we say that the common value is the limit of the function at $x = c$. Hence we may also rephrase the definition of continuity as follows: a function is continuous at $x = c$ if the function is defined at $x = c$ and if the value of the function at $x = c$ equals the limit of the function at $x = c$. If $f$ is not continuous at $c$, we say $f$ is discontinuous at $c$ and $c$ is called a point of discontinuity of $f$.

Reprint 2025-26

<!-- page 3 of 43 -->

106

MATHEMATICS

Example 1 Check the continuity of the function $f$ given by $f(x) = 2x + 3$ at $x = 1$.

Solution First note that the function is defined at the given point $x = 1$ and its value is 5. Then find the limit of the function at $x = 1$. Clearly

$$
\lim _ {x \to 1} f (x) = \lim _ {x \to 1} (2 x + 3) = 2 (1) + 3 = 5
$$

Thus

$$
\lim _ {x \to 1} f (x) = 5 = f (1)
$$

Hence, $f$ is continuous at $x = 1$.

Example 2 Examine whether the function $f$ given by $f(x) = x^2$ is continuous at $x = 0$.

Solution First note that the function is defined at the given point $x = 0$ and its value is 0. Then find the limit of the function at $x = 0$. Clearly

$$
\lim _ {x \to 0} f (x) = \lim _ {x \to 0} x ^ {2} = 0 ^ {2} = 0
$$

Thus

$$
\lim _ {x \to 0} f (x) = 0 = f (0)
$$

Hence, $f$ is continuous at $x = 0$.

Example 3 Discuss the continuity of the function $f$ given by $f(x) = |x|$ at $x = 0$.

Solution By definition

$$
f (x) = \left\{ \begin{array}{l} - x, \text {if} x <   0 \\ x, \text {if} x \geq 0 \end{array} \right.
$$

Clearly the function is defined at 0 and $f(0) = 0$. Left hand limit of $f$ at 0 is

$$
\lim _ {x \to 0 ^ {-}} f (x) = \lim _ {x \to 0 ^ {-}} (- x) = 0
$$

Similarly, the right hand limit of $f$ at 0 is

$$
\lim _ {x \to 0 ^ {+}} f (x) = \lim _ {x \to 0 ^ {+}} x = 0
$$

Thus, the left hand limit, right hand limit and the value of the function coincide at $x = 0$. Hence, $f$ is continuous at $x = 0$.

Example 4 Show that the function $f$ given by

$$
f (x) = \left\{ \begin{array}{l l} x ^ {3} + 3, & \text {if} x \neq 0 \\ 1, & \text {if} x = 0 \end{array} \right.
$$

is not continuous at $x = 0$.

Reprint 2025-26

<!-- page 4 of 43 -->

CONTINUITY AND DIFFERENTIABILITY

107

Solution The function is defined at $x = 0$ and its value at $x = 0$ is 1. When $x \neq 0$, the function is given by a polynomial. Hence,

$$
\lim _ {x \to 0} f (x) = \lim _ {x \to 0} (x ^ {3} + 3) = 0 ^ {3} + 3 = 3
$$

Since the limit of $f$ at $x = 0$ does not coincide with $f(0)$, the function is not continuous at $x = 0$. It may be noted that $x = 0$ is the only point of discontinuity for this function.

Example 5 Check the points where the constant function $f(x) = k$ is continuous.

Solution The function is defined at all real numbers and by definition, its value at any real number equals $k$. Let $c$ be any real number. Then

$$
\lim _ {x \to c} f (x) = \lim _ {x \to c} k = k
$$

Since $f(c) = k = \lim_{x\to c}f(x)$ for any real number $c$, the function $f$ is continuous at every real number.

Example 6 Prove that the identity function on real numbers given by $f(x) = x$ is continuous at every real number.

Solution The function is clearly defined at every point and $f(c) = c$ for every real number $c$. Also,

$$
\lim _ {x \to c} f (x) = \lim _ {x \to c} x = c
$$

Thus, $\lim_{x\to c}f(x) = c = f(c)$ and hence the function is continuous at every real number.

Having defined continuity of a function at a given point, now we make a natural extension of this definition to discuss continuity of a function.

Definition 2 A real function $f$ is said to be continuous if it is continuous at every point in the domain of $f$.

This definition requires a bit of elaboration. Suppose f is a function defined on a closed interval  $[a, b]$ , then for f to be continuous, it needs to be continuous at every point in  $[a, b]$  including the end points a and b. Continuity of fat a means

$$
\lim _ {x \to a ^ {+}} f (x) = f (a)
$$

and continuity of $f$ at $b$ means

$$
\lim _ {x \to b ^ {-}} f (x) = f (b)
$$

Observe that  $\lim_{x\to a^{-}}f(x)$  and  $\lim_{x\to b^{+}}f(x)$  do not make sense. As a consequence of this definition, if f is defined only at one point, it is continuous there, i.e., if the domain of f is a singleton, f is a continuous function.

Reprint 2025-26

<!-- page 5 of 43 -->

(Why?)

108

MATHEMATICS

Example 7 Is the function defined by $f(x) = |x|$, a continuous function? Solution We may rewrite $f$ as

$$
f (x) = \left\{ \begin{array}{l} - x, \text {if} x <   0 \\ x, \text {if} x \geq 0 \end{array} \right.
$$

By Example 3, we know that $f$ is continuous at $x = 0$.

Let $c$ be a real number such that $c < 0$. Then $f(c) = -c$. Also

$$
\lim _ {x \to c} f (x) = \lim _ {x \to c} (- x) = - c
$$

Since $\lim_{x\to c}f(x) = f(c)$, $f$ is continuous at all negative real numbers.

Now, let $c$ be a real number such that $c > 0$. Then $f(c) = c$. Also

$$
\lim _ {x \to c} f (x) = \lim _ {x \to c} x = c
$$

Since  $\lim_{x\to c}f(x)=f(c)$ , f is continuous at all positive real numbers. Hence, f is continuous at all points.

Example 8 Discuss the continuity of the function $f$ given by $f(x) = x^{3} + x^{2} - 1$.

Solution Clearly $f$ is defined at every real number $c$ and its value at $c$ is $c^3 + c^2 - 1$. We also know that

$$
\lim _ {x \to c} f (x) = \lim _ {x \to c} \left(x ^ {3} + x ^ {2} - 1\right) = c ^ {3} + c ^ {2} - 1
$$

Thus $\lim_{x\to c}f(x) = f(c)$, and hence $f$ is continuous at every real number. This means $f$ is a continuous function.

Example 9 Discuss the continuity of the function $f$ defined by $f(x) = \frac{1}{x}, x \neq 0$.

Solution Fix any non zero real number $c$, we have

$$
\varlimsup_ {x \to c} f (x) = \lim _ {x \to c} \frac {1}{x} = \frac {1}{c}
$$

Also, since for $c \neq 0$, $f(c) = \frac{1}{c}$, we have $\lim_{x \to c} f(x) = f(c)$ and hence, $f$ is continuous at every point in the domain of $f$. Thus $f$ is a continuous function.

Reprint 2025-26

<!-- page 6 of 43 -->

CONTINUITY AND DIFFERENTIABILITY

109

We take this opportunity to explain the concept of infinity. This we do by analysing the function  $f(x)=\frac{1}{x}$  near x=0. To carry out this analysis we follow the usual trick of finding the value of the function at real numbers close to 0. Essentially we are trying to find the right hand limit of f at 0. We tabulate this in the following (Table 5.1).

Table 5.1

| x | 1 | 0.3 | 0.2 | $0.1 = 10^{-1}$ | $0.01 = 10^{-2}$ | $0.001 = 10^{-3}$ | $10^{-n}$ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| f(x) | 1 | 3.333... | 5 | 10 | $100 = 10^{2}$ | $1000 = 10^{3}$ | $10^{n}$ |

We observe that as x gets closer to 0 from the right, the value of  $f(x)$  shoots up higher. This may be rephrased as: the value of  $f(x)$  may be made larger than any given number by choosing a positive real number very close to 0. In symbols, we write

$$
\lim _ {x \to 0 ^ {+}} f (x) = + \infty
$$

(to be read as: the right hand limit of  $f(x)$  at 0 is plus infinity). We wish to emphasise that  $+\infty$  is NOT a real number and hence the right hand limit of fat 0 does not exist (as a real number).

Similarly, the left hand limit of $f$ at 0 may be found. The following table is self explanatory.

Table 5.2

| x | -1 | -0.3 | -0.2 | $-10^{-1}$ | $-10^{-2}$ | $-10^{-3}$ | $-10^{-n}$ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| f(x) | -1 | -3.333... | -5 | -10 | $-10^{2}$ | $-10^{3}$ | $-10^{n}$ |

From the Table 5.2, we deduce that the value of  $f(x)$  may be made smaller than any given number by choosing a negative real number very close to 0. In symbols, we write

$$
\lim _ {x \to 0 ^ {-}} f (x) = - \infty
$$

(to be read as: the left hand limit of $f(x)$ at 0 is minus infinity). Again, we wish to emphasise that $-\infty$ is NOT a real number and hence the left hand limit of $f$ at 0 does not exist (as a real number). The graph of the reciprocal function given in Fig 5.3 is a geometric representation of the above mentioned facts.

![Image block](doc:8b97716/tier:standard/page:6/block:15)

Fig 5.3

Reprint 2025-26

<!-- page 7 of 43 -->

110

MATHEMATICS

Example 10 Discuss the continuity of the function $f$ defined by

$$
f (x) = \left\{ \begin{array}{l} x + 2, \text {if} x \leq 1 \\ x - 2, \text {if} x > 1 \end{array} \right.
$$

Solution The function $f$ is defined at all points of the real line.

Case 1 If $c < 1$, then $f(c) = c + 2$. Therefore, $\lim_{x \to c} f(x) = \lim_{x \to c} (x + 2) = c + 2$

Thus, $f$ is continuous at all real numbers less than 1.

Case 2 If $c > 1$, then $f(c) = c - 2$. Therefore,

$$
\lim _ {x \to c} f (x) = \lim _ {x \to c} (x - 2) = c - 2 = f (c)
$$

Thus, $f$ is continuous at all points $x > 1$.

Case 3 If $c = 1$, then the left hand limit of $f$ at $x = 1$ is

$$
\lim _ {x \to 1 ^ {-}} f (x) = \lim _ {x \to 1 ^ {-}} (x + 2) = 1 + 2 = 3
$$

The right hand limit of $f$ at $x = 1$ is

$$
\lim _ {x \to 1 ^ {+}} f (x) = \lim _ {x \to 1 ^ {+}} (x - 2) = 1 - 2 = - 1
$$

![Image block](doc:8b97716/tier:standard/page:7/block:15)

Since the left and right hand limits of $f$ at $x = 1$ do not coincide, $f$ is not continuous at $x = 1$. Hence

Fig 5.4

$x = 1$ is the only point of discontinuity of $f$. The graph of the function is given in Fig 5.4.

Example 11 Find all the points of discontinuity of the function $f$ defined by

$$
f (x) = \left\{ \begin{array}{c} x + 2, \text {if} x <   1 \\ 0, \text {if} x = 1 \\ x - 2, \text {if} x > 1 \end{array} \right.
$$

Solution As in the previous example we find that f is continuous at all real numbers  $x \neq 1$ . The left hand limit of f at x = 1 is

$$
\lim _ {x \to 1 ^ {-}} f (x) = \lim _ {x \to 1 ^ {-}} (x + 2) = 1 + 2 = 3
$$

The right hand limit of $f$ at $x = 1$ is

$$
\lim _ {x \to 1 ^ {+}} f (x) = \lim _ {x \to 1 ^ {+}} (x - 2) = 1 - 2 = - 1
$$

Since, the left and right hand limits of $f$ at $x = 1$ do not coincide, $f$ is not continuous at $x = 1$. Hence $x = 1$ is the only point of discontinuity of $f$. The graph of the function is given in the Fig 5.5.

![Image block](doc:8b97716/tier:standard/page:7/block:26)

Fig 5.5

Reprint 2025-26

<!-- page 8 of 43 -->

CONTINUITY AND DIFFERENTIABILITY

111

Example 12 Discuss the continuity of the function defined by

$$
f (x) = \left\{ \begin{array}{c} x + 2, \text {if} x <   0 \\ - x + 2, \text {if} x > 0 \end{array} \right.
$$

Solution Observe that the function is defined at all real numbers except at 0. Domain of definition of this function is Y

$D_{1} \cup D_{2}$  where  $D_{1} = \{x \in R : x < 0\}$  and  $D_{2} = \{x \in R : x > 0\}$

$$
c \in \mathrm{D} _ {1}
$$

$$
\varliminf_ {x \to c} f (x) = \varliminf_ {x \to c} (x + 2)
$$

$$
= c + 2 = f (c)
$$

$$
\mathrm{D} _ {1}
$$

$$
c \in \mathrm{D} _ {2}
$$

$$
\lim _ {x \to c} f (x) = \lim _ {x \to c} (- x + 2)
$$

$= -c + 2 = f(c)$ and hence $f$ is continuous in $\mathrm{D}_2$. Since $f$ is continuous at all points in the domain of $f$, we deduce that $f$ is continuous. Graph of this function is given in the Fig 5.6. Note that to graph this function we need to lift the pen from the plane

![Image block](doc:8b97716/tier:standard/page:8/block:14)

Fig 5.6

of the paper, but we need to do that only for those points where the function is not defined.

Example 13 Discuss the continuity of the function $f$ given by

$$
f (x) = \left\{ \begin{array}{l l} x, & \text {if} x \geq 0 \\ x ^ {2}, & \text {if} x <   0 \end{array} \right.
$$

Solution Clearly the function is defined at every real number. Graph of the function is given in Fig 5.7. By inspection, it seems prudent to partition the domain of definition of f into three disjoint subsets of the real line.

![Image block](doc:8b97716/tier:standard/page:8/block:20)

Let $D_{1} = \{x \in R : x < 0\}, D_{2} = \{0\}$ and $D_{3} = \{x \in R : x > 0\}$

Fig 5.7

Case 1 At any point in $\mathrm{D}_1$, we have $f(x) = x^2$ and it is easy to see that it is continuous there (see Example 2).

Case 2 At any point in $\mathrm{D}_3$, we have $f(x) = x$ and it is easy to see that it is continuous there (see Example 6).

Reprint 2025-26

<!-- page 9 of 43 -->

112

MATHEMATICS

Case 3 Now we analyse the function at $x = 0$. The value of the function at 0 is $f(0) = 0$. The left hand limit of $f$ at 0 is

$$
\lim _ {x \to 0 ^ {-}} f (x) = \lim _ {x \to 0 ^ {-}} x ^ {2} = 0 ^ {2} = 0
$$

The right hand limit of $fat$ 0 is

$$
\lim _ {x \to 0 ^ {+}} f (x) = \lim _ {x \to 0 ^ {+}} x = 0
$$

Thus $\lim_{x\to 0}f(x) = 0 = f(0)$ and hence $f$ is continuous at 0. This means that $f$ is continuous at every point in its domain and hence, $f$ is a continuous function. Example 14 Show that every polynomial function is continuous.

Solution Recall that a function $p$ is a polynomial function if it is defined by $p(x) = a_0 + a_1 x + \ldots + a_n x^n$ for some natural number $n$, $a_n \neq 0$ and $a_i \in \mathbf{R}$. Clearly this function is defined for every real number. For a fixed real number $c$, we have

$$
\lim _ {x \to c} p (x) = p (c)
$$

By definition, $p$ is continuous at $c$. Since $c$ is any real number, $p$ is continuous at every real number and hence $p$ is a continuous function.

Example 15 Find all the points of discontinuity of the greatest integer function defined by $f(x) = [x]$, where $[x]$ denotes the greatest integer less than or equal to $x$.

Solution First observe that $f$ is defined for all real numbers. Graph of the function is given in Fig 5.8. From the graph it looks like that $f$ is discontinuous at every integral point. Below we explore, if this is true.

![Image block](doc:8b97716/tier:standard/page:9/block:13)

Fig 5.8

Reprint 2025-26

<!-- page 10 of 43 -->

CONTINUITY AND DIFFERENTIABILITY

113

Case 1 Let $c$ be a real number which is not equal to any integer. It is evident from the graph that for all real numbers close to $c$ the value of the function is equal to $[c]$; i.e., $\lim_{x \to c} f(x) = \lim_{x \to c} [x] = [c]$. Also $f(c) = [c]$ and hence the function is continuous at all real numbers not equal to integers.

Case 2 Let $c$ be an integer. Then we can find a sufficiently small real number $r > 0$ such that $[c - r] = c - 1$ whereas $[c + r] = c$.

This, in terms of limits mean that

$$
\lim _ {x \to c ^ {-}} f (x) = c - 1, \lim _ {x \to c ^ {+}} f (x) = c
$$

Since these limits cannot be equal to each other for any $c$, the function is discontinuous at every integral point.

## 5.2.1 Algebra of continuous functions

In the previous class, after having understood the concept of limits, we learnt some algebra of limits. Analogously, now we will study some algebra of continuous functions. Since continuity of a function at a point is entirely dictated by the limit of the function at that point, it is reasonable to expect results analogous to the case of limits.

Theorem 1 Suppose $f$ and $g$ be two real functions continuous at a real number $c$. Then

(1) $f + g$ is continuous at $x = c$.

(2) $f - g$ is continuous at $x = c$.

(3) $f.g$ is continuous at $x = c$.

(4) $\left(\frac{f}{g}\right)$ is continuous at $x = c$, (provided $g(c) \neq 0$).

Proof We are investigating continuity of $(f + g)$ at $x = c$. Clearly it is defined at $x = c$. We have

$$
\begin{array}{r l r} \lim _ {x \to c} (f + g) (x) & = \lim _ {x \to c} [ f (x) + g (x) ] & \text {(by definition of} f + g \text {)} \\ & = \lim _ {x \to c} f (x) + \lim _ {x \to c} g (x) & \text {(by the theorem on limits)} \\ & = f (c) + g (c) & \text {(as} f \text {and} g \text {are continuous)} \\ & = (f + g) (c) & \text {(by definition of} f + g \text {)} \end{array}
$$

Hence, $f + g$ is continuous at $x = c$.

Proofs for the remaining parts are similar and left as an exercise to the reader.

Reprint 2025-26

<!-- page 11 of 43 -->

114

MATHEMATICS

Remarks

(i) As a special case of (3) above, if $f$ is a constant function, i.e., $f(x) = \lambda$ for some real number $\lambda$, then the function $(\lambda . g)$ defined by $(\lambda . g)(x) = \lambda . g(x)$ is also continuous. In particular if $\lambda = -1$, the continuity of $f$ implies continuity of $-f$.

(ii) As a special case of (4) above, if $f$ is the constant function $f(x) = \lambda$, then the function $\frac{\lambda}{g}$ defined by $\frac{\lambda}{g}(x) = \frac{\lambda}{g(x)}$ is also continuous wherever $g(x) \neq 0$. In particular, the continuity of $g$ implies continuity of $\frac{1}{g}$.

The above theorem can be exploited to generate many continuous functions. They also aid in deciding if certain functions are continuous or not. The following examples illustrate this:

Example 16 Prove that every rational function is continuous.

Solution Recall that every rational function $f$ is given by

$$
f (x) = \frac {p (x)}{q (x)}, q (x) \neq 0
$$

where p and q are polynomial functions. The domain of f is all real numbers except points at which q is zero. Since polynomial functions are continuous (Example 14), f is continuous by (4) of Theorem 1.

Example 17 Discuss the continuity of sine function.

Solution To see this we use the following facts

$$
\lim _ {x \to 0} \sin x = 0
$$

We have not proved it, but is intuitively clear from the graph of $\sin x$ near 0.

Now, observe that $f(x) = \sin x$ is defined for every real number. Let $c$ be a real number. Put $x = c + h$. If $x \to c$ we know that $h \to 0$. Therefore

$$
\begin{array}{r l} \underset {x \to c} {\lim} f (x) & = \underset {x \to c} {\lim} \sin x \\ & = \underset {h \to 0} {\lim} \sin (c + h) \\ & = \underset {h \to 0} {\lim} [ \sin c \cos h + \cos c \sin h ] \\ & = \underset {h \to 0} {\lim} [ \sin c \cos h ] + \underset {h \to 0} {\lim} [ \cos c \sin h ] \\ & = \sin c + 0 = \sin c = f (c) \end{array}
$$

Thus $\lim_{x\to c}f(x) = f(c)$ and hence $f$ is a continuous function.

Reprint 2025-26

<!-- page 12 of 43 -->

CONTINUITY AND DIFFERENTIABILITY

115

Remark A similar proof may be given for the continuity of cosine function.

Example 18 Prove that the function defined by $f(x) = \tan x$ is a continuous function.

Solution The function $f(x) = \tan x = \frac{\sin x}{\cos x}$. This is defined for all real numbers such

that $\cos x \neq 0$, i.e., $x \neq (2n + 1)\frac{\pi}{2}$. We have just proved that both sine and cosine functions are continuous. Thus $\tan x$ being a quotient of two continuous functions is continuous wherever it is defined.

An interesting fact is the behaviour of continuous functions with respect to composition of functions. Recall that if $f$ and $g$ are two real functions, then

$$
\left(f \circ g\right) (x) = f (g (x))
$$

is defined whenever the range of $g$ is a subset of domain of $f$. The following theorem (stated without proof) captures the continuity of composite functions.

Theorem 2 Suppose $f$ and $g$ are real valued functions such that $(f \circ g)$ is defined at $c$. If $g$ is continuous at $c$ and if $f$ is continuous at $g(c)$, then $(f \circ g)$ is continuous at $c$.

The following examples illustrate this theorem.

Example 19 Show that the function defined by $f(x) = \sin (x^2)$ is a continuous function.

Solution Observe that the function is defined for every real number. The function $f$ may be thought of as a composition $g \circ h$ of the two functions $g$ and $h$, where $g(x) = \sin x$ and $h(x) = x^2$. Since both $g$ and $h$ are continuous functions, by Theorem 2, it can be deduced that $f$ is a continuous function.

Example 20 Show that the function $f$ defined by

$$
f (x) = | 1 - x + | x | |
$$

where $x$ is any real number, is a continuous function.

Solution Define $g$ by $g(x) = 1 - x + |x|$ and $h$ by $h(x) = |x|$ for all real $x$. Then

$$
\begin{array}{r l} (h \circ g) (x) & = h (g (x)) \\ & = h (1 - x + | x |) \\ & = | 1 - x + | x | | = f (x) \end{array}
$$

In Example 7, we have seen that $h$ is a continuous function. Hence $g$ being a sum of a polynomial function and the modulus function is continuous. But then $f$ being a composite of two continuous functions is continuous.

Reprint 2025-26

<!-- page 13 of 43 -->

116

MATHEMATICS

## EXERCISE 5.1

1. Prove that the function $f(x) = 5x - 3$ is continuous at $x = 0$, at $x = -3$ and at $x = 5$.

2. Examine the continuity of the function $f(x) = 2x^{2} - 1$ at $x = 3$.

3. Examine the following functions for continuity.

(a) $f(x) = x - 5$ (b) $f(x) = \frac{1}{x - 5}, x \neq 5$

(c) $f(x) = \frac{x^2 - 25}{x + 5}, x \neq -5$ (d) $f(x) = |x - 5|$

4. Prove that the function $f(x) = x^n$ is continuous at $x = n$, where $n$ is a positive integer.

5. Is the function $f$ defined by

$$
f (x) = \left\{ \begin{array}{l} x, \text {if} x \leq 1 \\ 5, \text {if} x > 1 \end{array} \right.
$$

continuous at $x = 0$? At $x = 1$? At $x = 2$?

Find all points of discontinuity of $f$, where $f$ is defined by

6.  $f(x)=\left\{\begin{aligned}&2x+3,\text{ if }x\leq2\\ &2x-3,\text{ if }x>2\end{aligned}\right.$

$$
\int | x | + 3, \text {if} x \leq - 3
$$

$$
f (x) = \left\{ \begin{array}{l} - 2 x, \text {if} - 3 <   x <   3 \\ 6 x + 2, \text {if} x \geq 3 \end{array} \right.
$$

8. $f(x) = \left\{ \begin{array}{ll}\frac{|x|}{x}, & \text{if} x\neq 0\\ 0, & \text{if} x = 0 \end{array} \right.$

9. $f(x) = \begin{cases} \frac{x}{|x|}, & \text{if } x < 0 \\ -1, & \text{if } x \geq 0 \end{cases}$

10.  $f(x)=\begin{cases}x+1,&\text{if }x\geq1\\x^{2}+1,&\text{if }x<1\end{cases}$

11. $f(x) = \begin{cases} x^3 - 3, & \text{if } x \leq 2 \\ x^2 + 1, & \text{if } x > 2 \end{cases}$

12. $f(x) = \begin{cases} x^{10} - 1, & \text{if } x \leq 1 \\ x^2, & \text{if } x > 1 \end{cases}$

13. Is the function defined by

$$
f (x) = \left\{ \begin{array}{l l} x + 5, & \text {if} x \leq 1 \\ x - 5, & \text {if} x > 1 \end{array} \right.
$$

a continuous function?

Reprint 2025-26

<!-- page 14 of 43 -->

CONTINUITY AND DIFFERENTIABILITY

117

Discuss the continuity of the function $f$, where $f$ is defined by

14.

$$
f (x) = \left\{ \begin{array}{l l} 3, & \text {if} 0 \leq x \leq 1 \\ 4, & \text {if} 1 <   x <   3 \\ 5, & \text {if} 3 \leq x \leq 1 0 \end{array} \right.
$$

15.

$$
f (x) = \left\{ \begin{array}{l} 2 x, \text {if} x <   0 \\ 0, \text {if} 0 \leq x \leq 1 \\ 4 x, \text {if} x > 1 \end{array} \right.
$$

16.  $f(x)=\begin{cases}-2,\text{ if }x\leq-1\\2x,\text{ if }-1<x\leq1\\2,\text{ if }x>1\end{cases}$

17. Find the relationship between $a$ and $b$ so that the function $f$ defined by

$$
f (x) = \left\{ \begin{array}{l l} a x + 1, & \text {if} x \leq 3 \\ b x + 3, & \text {if} x > 3 \end{array} \right.
$$

is continuous at $x = 3$.

18. For what value of $\lambda$ is the function defined by

$$
f (x) = \left\{ \begin{array}{l l} \lambda \left(x ^ {2} - 2 x\right), & \text {if} x \leq 0 \\ 4 x + 1, & \text {if} x > 0 \end{array} \right.
$$

continuous at $x = 0$? What about continuity at $x = 1$?

19. Show that the function defined by  $g(x) = x - [x]$  is discontinuous at all integral points. Here [x] denotes the greatest integer less than or equal to x.

20. Is the function defined by $f(x) = x^{2} - \sin x + 5$ continuous at $x = \pi$?

21. Discuss the continuity of the following functions:
(a)  $f(x) = \sin x + \cos x$  (b)  $f(x) = \sin x - \cos x$ 
(c)  $f(x) = \sin x \cdot \cos x$

22. Discuss the continuity of the cosine, cosecant, secant and cotangent functions.

23. Find all points of discontinuity of $f$, where

$$
f (x) = \left\{ \begin{array}{l l} \frac {\sin x}{x}, & \text {if} x <   0 \\ x + 1, & \text {if} x \geq 0 \end{array} \right.
$$

24. Determine if $f$ defined by

$$
f (x) = \left\{ \begin{array}{l l} x ^ {2} \sin \frac {1}{x}, & \text {if} x \neq 0 \\ 0, & \text {if} x = 0 \end{array} \right.
$$

is a continuous function?

Reprint 2025-26

<!-- page 15 of 43 -->

118

MATHEMATICS

25. Examine the continuity of $f$, where $f$ is defined by

$$
f (x) = \left\{ \begin{array}{l l} \sin x - \cos x, & \text {if} x \neq 0 \\ - 1, & \text {if} x = 0 \end{array} \right.
$$

Find the values of $k$ so that the function $f$ is continuous at the indicated point in Exercises 26 to 29.

$$
f (x) = \left\{ \begin{array}{l l} \frac {k \cos x}{\pi - 2 x}, & \text {if} x \neq \frac {\pi}{2} \\ 3, & \text {if} x = \frac {\pi}{2} \end{array} \quad \text {at} x = \frac {\pi}{2} \right.
$$

27. $f(x) = \begin{cases} kx^2, & \text{if } x \leq 2 \\ 3, & \text{if } x > 2 \end{cases}$

$$
\text {at} x = 2
$$

28. $f(x) = \left\{ \begin{array}{ll}kx + 1, & \text{if } x \leq \pi \\ \cos x, & \text{if } x > \pi \end{array} \right|$

$$
\text {at} x = \pi
$$

29.  $f(x)=\left\{\begin{aligned}&kx+1,&if x\leq5\\ &3x-5,&if x>5\end{aligned}\right.$

$$
\text {at} x = 5
$$

30. Find the values of $a$ and $b$ such that the function defined by

$$
f (x) = \left\{ \begin{array}{l l} 5, & \text {if} x \leq 2 \\ a x + b, & \text {if} 2 <   x <   1 0 \\ 2 1, & \text {if} x \geq 1 0 \end{array} \right.
$$

is a continuous function.

31. Show that the function defined by $f(x) = \cos (x^2)$ is a continuous function.

32. Show that the function defined by $f(x) = |\cos x|$ is a continuous function.

33. Examine that $\sin |x|$ is a continuous function.

34. Find all the points of discontinuity of $f$ defined by $f(x) = |x| - |x + 1|$.

## 5.3. Differentiability

Recall the following facts from previous class. We had defined the derivative of a real function as follows:

Suppose $f$ is a real function and $c$ is a point in its domain. The derivative of $fat$ is defined by

$$
\lim _ {h \to 0} \frac {f (c + h) - f (c)}{h}
$$

Reprint 2025-26

<!-- page 16 of 43 -->

CONTINUITY AND DIFFERENTIABILITY

119

provided this limit exists. Derivative of $f$ at $c$ is denoted by $f'(c)$ or $\frac{d}{dx}(f(x))|_c$. The function defined by

$$
f ^ {\prime} (x) = \lim _ {h \to 0} \frac {f (x + h) - f (x)}{h}
$$

wherever the limit exists is defined to be the derivative of $f$. The derivative of $f$ is denoted by $f'(x)$ or $\frac{d}{dx}(f(x))$ or if $y = f(x)$ by $\frac{dy}{dx}$ or $y'$. The process of finding derivative of a function is called differentiation. We also use the phrase differentiate $f(x)$ with respect to $x$ to mean find $f'(x)$.

The following rules were established as a part of algebra of derivatives:

(1) $(u\pm v)^{\prime} = u^{\prime}\pm v^{\prime}$

(2) $(uv)' = u'v + uv'$ (Leibnitz or product rule)

(3) $\left(\frac{u}{v}\right)' = \frac{u'v - uv'}{v^2}$, wherever $v \neq 0$ (Quotient rule).

The following table gives a list of derivatives of certain standard functions:

Table 5.3

| $f(x)$ | $x^{n}$ | $\sin x$ | $\cos x$ | $\tan x$ |
| --- | --- | --- | --- | --- |
| $f'(x)$ | $nx^{n-1}$ | $\cos x$ | $-\sin x$ | $\sec^{2} x$ |

Whenever we defined derivative, we had put a caution provided the limit exists. Now the natural question is; what if it doesn't? The question is quite pertinent and so is its answer. If $\lim_{h\to 0}\frac{f(c + h) - f(c)}{h}$ does not exist, we say that $f$ is not differentiable at $c$. In other words, we say that a function $f$ is differentiable at a point $c$ in its domain if both $\lim_{h\to 0^{-}}\frac{f(c + h) - f(c)}{h}$ and $\lim_{h\to 0^{+}}\frac{f(c + h) - f(c)}{h}$ are finite and equal. A function is said to be differentiable in an interval $[a,b]$ if it is differentiable at every point of $[a,b]$. As in case of continuity, at the end points $a$ and $b$, we take the right hand limit and left hand limit, which are nothing but left hand derivative and right hand derivative of the function at $a$ and $b$ respectively. Similarly, a function is said to be differentiable in an interval $(a,b)$ if it is differentiable at every point of $(a,b)$.

Reprint 2025-26

<!-- page 17 of 43 -->

120

MATHEMATICS

Theorem 3 If a function $f$ is differentiable at a point $c$, then it is also continuous at that point.

Proof Since $f$ is differentiable at $c$, we have

$$
\lim _ {x \to c} \frac {f (x) - f (c)}{x - c} = f ^ {\prime} (c)
$$

But for $x \neq c$, we have

$$
f (x) - f (c) = \frac {f (x) - f (c)}{x - c}. (x - c)
$$

Therefore

$$
\lim _ {x \to c} [ f (x) - f (c) ] = \lim _ {x \to c} \left[ \frac {f (x) - f (c)}{x - c}. (x - c) \right]
$$

or

or

$$
\begin{array}{r l} \lim _ {x \to c} [ f (x) ] - \lim _ {x \to c} [ f (c) ] & = \lim _ {x \to c} \left[ \frac {f (x) - f (c)}{x - c} \right]. \lim _ {x \to c} [ (x - c) ] \\ & = f ^ {\prime} (c). 0 = 0 \\ \lim _ {x \to c} f (x) & = f (c) \end{array}
$$

Hence $f$ is continuous at $x = c$.

Corollary 1 Every differentiable function is continuous.

We remark that the converse of the above statement is not true. Indeed we have seen that the function defined by $f(x) = |x|$ is a continuous function. Consider the left hand limit

$$
\lim _ {h \to 0 ^ {-}} \frac {f (0 + h) - f (0)}{h} = \frac {- h}{h} = - 1
$$

The right hand limit

$$
\lim _ {h \to 0 ^ {+}} \frac {f (0 + h) - f (0)}{h} = \frac {h}{h} = 1
$$

Since the above left and right hand limits at 0 are not equal, $\lim_{h\to 0}\frac{f(0 + h) - f(0)}{h}$ does not exist and hence $f$ is not differentiable at 0. Thus $f$ is not a differentiable function.

## 5.3.1 Derivatives of composite functions

To study derivative of composite functions, we start with an illustrative example. Say, we want to find the derivative of $f$, where

$$
f (x) = (2 x + 1) ^ {3}
$$

Reprint 2025-26

<!-- page 18 of 43 -->

CONTINUITY AND DIFFERENTIABILITY

121

One way is to expand  $(2x + 1)^{3}$  using binomial theorem and find the derivative as a polynomial function as illustrated below.

$$
\left| \begin{array}{l} \frac {d}{d x} f (x) = \frac {d}{d x} \left[ (2 x + 1) ^ {3} \right] \\ = \frac {d}{d x} (8 x ^ {3} + 1 2 x ^ {2} + 6 x + 1) \\ = 2 4 x ^ {2} + 2 4 x + 6 \\ = 6 (2 x + 1) ^ {2} \\ f (x) = (h \circ g) (x) \end{array} \right.
$$

Now, observe that

where $g(x) = 2x + 1$ and $h(x) = x^3$. Put $t = g(x) = 2x + 1$. Then $f(x) = h(t) = t^3$. Thus

$$
\frac {d f}{d x} = 6 (2 x + 1) ^ {2} = 3 (2 x + 1) ^ {2}. 2 = 3 t ^ {2}. 2 = \frac {d h}{d t} \cdot \frac {d t}{d x}
$$

The advantage with such observation is that it simplifies the calculation in finding the derivative of, say,  $(2x + 1)^{100}$ . We may formalise this observation in the following theorem called the chain rule.

Theorem 4 (Chain Rule) Let $f$ be a real valued function which is a composite of two

functions $u$ and $v$; i.e., $f = v$ or $u$. Suppose $t = u(x)$ and if both $\frac{dt}{dx}$ and $\frac{dv}{dt}$ exist, we have

$$
\frac {d f}{d x} = \frac {d v}{d t} \cdot \frac {d t}{d x}
$$

We skip the proof of this theorem. Chain rule may be extended as follows. Suppose $f$ is a real valued function which is a composite of three functions $u, v$ and $w$; i.e.,

$f = (w \circ u) \circ v$. If $t = v(x)$ and $s = u(t)$, then

$$
\frac {d f}{d x} = \frac {d (w o u)}{d t} \cdot \frac {d t}{d x} = \frac {d w}{d s} \cdot \frac {d s}{d t} \cdot \frac {d t}{d x}
$$

provided all the derivatives in the statement exist. Reader is invited to formulate chain rule for composite of more functions.

Example 21 Find the derivative of the function given by $f(x) = \sin (x^2)$.

Solution Observe that the given function is a composite of two functions. Indeed, if $t = u(x) = x^2$ and $v(t) = \sin t$, then

$$
f (x) = (v \text {o} u) (x) = v (u (x)) = v (x ^ {2}) = \sin x ^ {2}
$$

Reprint 2025-26

<!-- page 19 of 43 -->

122

MATHEMATICS

Put $t = u(x) = x^2$. Observe that $\frac{dv}{dt} = \cos t$ and $\frac{dt}{dx} = 2x$ exist. Hence, by chain rule

$$
\frac {d f}{d x} = \frac {d v}{d t} \cdot \frac {d t}{d x} = \cos t \cdot 2 x
$$

It is normal practice to express the final result only in terms of $x$. Thus

$$
\frac {d f}{d x} = \cos t \cdot 2 x = 2 x \cos x ^ {2}
$$

## EXERCISE 5.2

Differentiate the functions with respect to $x$ in Exercises 1 to 8.

1. $\sin (x^2 + 5)$ 2. $\cos (\sin x)$ 3. $\sin (ax + b)$

4. $\sec (\tan (\sqrt{x}))$

5. $\frac{\sin(ax + b)}{\cos(cx + d)}$

6. $\cos x^3\cdot \sin^2 (x^5)$

7. $2\sqrt{\cot(x^2)}$ 8. $\cos (\sqrt{x})$

9. Prove that the function $f$ given by

$$
f (x) = | x - 1 |, x \in \mathbf {R}
$$

is not differentiable at $x = 1$.

10. Prove that the greatest integer function defined by

$$
f (x) = [ x ], 0 <   x <   3
$$

is not differentiable at $x = 1$ and $x = 2$.

## 5.3.2 Derivatives of implicit functions

Until now we have been differentiating various functions given in the form  $y = f(x)$ . But it is not necessary that functions are always expressed in this form. For example, consider one of the following relationships between x and y:

$$
x - y - \pi = 0
$$

$$
x + \sin x y - y = 0
$$

In the first case, we can solve for y and rewrite the relationship as  $y = x - \pi$ . In the second case, it does not seem that there is an easy way to solve for y. Nevertheless, there is no doubt about the dependence of y on x in either of the cases. When a relationship between x and y is expressed in a way that it is easy to solve for y and write  $y = f(x)$ , we say that y is given as an explicit function of x. In the latter case it

Reprint 2025-26

<!-- page 20 of 43 -->

CONTINUITY AND DIFFERENTIABILITY

123

is implicit that y is a function of x and we say that the relationship of the second type, above, gives function implicitly. In this subsection, we learn to differentiate implicit functions.

Example 22 Find $\frac{dy}{dx}$ if $x - y = \pi$.

Solution One way is to solve for $y$ and rewrite the above as

$$
y = x - \pi
$$

But then

$$
\frac {d y}{d x} = 1
$$

Alternatively, directly differentiating the relationship w.r.t., $x$, we have

$$
\frac {d}{d x} (x - y) = \frac {d \pi}{d x}
$$

Recall that $\frac{d\pi}{dx}$ means to differentiate the constant function taking value $\pi$ everywhere w.r.t., $x$. Thus

$$
\frac {d}{d x} (x) - \frac {d}{d x} (y) = 0
$$

which implies that

$$
\frac {d y}{d x} = \frac {d x}{d x} = 1
$$

Example 23 Find $\frac{dy}{dx}$, if $y + \sin y = \cos x$.

Solution We differentiate the relationship directly with respect to $x$, i.e.,

$$
\frac {d y}{d x} + \frac {d}{d x} (\sin y) = \frac {d}{d x} (\cos x)
$$

which implies using chain rule

$$
\frac {d y}{d x} + \cos y \cdot \frac {d y}{d x} = - \sin x
$$

This gives

$$
\frac {d y}{d x} = - \frac {\sin x}{1 + \cos y}
$$

where

$$
y \neq (2 n + 1) \pi
$$

Reprint 2025-26

<!-- page 21 of 43 -->

124

MATHEMATICS

## 5.3.3 Derivatives of inverse trigonometric functions

We remark that inverse trigonometric functions are continuous functions, but we will not prove this. Now we use chain rule to find derivatives of these functions.

Example 24 Find the derivative of $f$ given by $f(x) = \sin^{-1}x$ assuming it exists.

Solution Let $y = \sin^{-1}x$. Then, $x = \sin y$.

Differentiating both sides w.r.t. $x$, we get

$$
1 = \cos y \frac {d y}{d x}
$$

which implies that

$$
\frac {d y}{d x} = \frac {1}{\cos y} = \frac {1}{\cos \left(\sin^ {- 1} x\right)}
$$

Observe that this is defined only for $\cos y \neq 0$, i.e., $\sin^{-1} x \neq -\frac{\pi}{2}, \frac{\pi}{2}$, i.e., $x \neq -1, 1$, i.e., $x \in (-1, 1)$.

To make this result a bit more attractive, we carry out the following manipulation. Recall that for $x \in (-1, 1)$, $\sin (\sin^{-1} x) = x$ and hence

$$
\cos^ {2} y = 1 - (\sin y) ^ {2} = 1 - (\sin (\sin^ {- 1} x)) ^ {2} = 1 - x ^ {2}
$$

Also, since $y \in \left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$, cos $y$ is positive and hence $\cos y = \sqrt{1 - x^2}$

Thus, for $x\in (-1,1)$

$$
\frac {d y}{d x} = \frac {1}{\cos y} = \frac {1}{\sqrt {1 - x ^ {2}}}
$$

| $f(x)$ | $\sin^{-1} x$ | $\cos^{-1} x$ | $\tan^{-1} x$ |
| --- | --- | --- | --- |
| $f^{1}(x)$ | $\frac{1}{\sqrt{1-x^{2}}}$ | $\frac{-1}{\sqrt{1-x^{2}}}$ | $\frac{1}{1+x^{2}}$ |
| Domain off | (-1, 1) | (-1, 1) | R |

Reprint 2025-26

<!-- page 22 of 43 -->

CONTINUITY AND DIFFERENTIABILITY

125

## EXERCISE 5.3

Find $\frac{dy}{dx}$ in the following:

1. $2x + 3y = \sin x$

2. $2x + 3y = \sin y$

3. $ax + by^{2} = \cos y$

4. $xy + y^{2} = \tan x + y$ 5. $x^{2} + xy + y^{2} = 100$ 6. $x^{3} + x^{2}y + xy^{2} + y^{3} = 81$

7. $\sin^2 y + \cos xy = \kappa$ 8. $\sin^2 x + \cos^2 y = 1$ 9. $y = \sin^{-1}\left(\frac{2x}{1 + x^2}\right)$

10.  $y = \tan^{-1}\left(\frac{3x - x^{3}}{1 - 3x^{2}}\right), -\frac{1}{\sqrt{3}} < x < \frac{1}{\sqrt{3}}$

11. $y = \cos^{-1}\left(\frac{1 - x^2}{1 + x^2}\right), 0 < x < 1$

12. $y = \sin^{-1}\left(\frac{1 - x^2}{1 + x^2}\right), 0 < x < 1$

13. $y = \cos^{-1}\left(\frac{2x}{1 + x^2}\right), - 1 <   x <   1$

14. $y = \sin^{-1}\left(2x\sqrt{1 - x^2}\right), - \frac{1}{\sqrt{2}} <  x <   \frac{1}{\sqrt{2}}$

15. $y = \sec^{-1}\left(\frac{1}{2x^2 - 1}\right), 0 < x < \frac{1}{\sqrt{2}}$

## 5.4 Exponential and Logarithmic Functions

Till now we have learnt some aspects of different classes of functions like polynomial functions, rational functions and trigonometric functions. In this section, we shall learn about a new class of (related) functions called exponential functions and logarithmic functions. It needs to be emphasized that many statements made in this section are motivational and precise proofs of these are well beyond the scope of this text.

The Fig 5.9 gives a sketch of $y = f_{1}(x) = x$, $y = f_{2}(x) = x^{2}$, $y = f_{3}(x) = x^{3}$ and $y = f_{4}(x) = x^{4}$. Observe that the curves get steeper as the power of $x$ increases. Steeper the curve, faster is the rate of growth. What this means is that for a fixed increment in the value of $x (> 1)$, the increment in the value of $y = f_{n}(x)$ increases as $n$ increases for $n = 1, 2, 3, 4$. It is conceivable that such a statement is true for all positive values of $n$,

Reprint 2025-26

<!-- page 23 of 43 -->

126

MATHEMATICS

where $f_n(x) = x^n$. Essentially, this means that the graph of $y = f_n(x)$ leans more towards the $y$-axis as $n$ increases. For example, consider $f_{10}(x) = x^{10}$ and $f_{15}(x) = x^{15}$. If $x$ increases from 1 to 2, $f_{10}$ increases from 1 to $2^{10}$ whereas $f_{15}$ increases from 1 to $2^{15}$. Thus, for the same increment in $x, f_{15}$ grow faster than $f_{10}$.

Upshot of the above discussion is that the growth of polynomial functions is dependent on the degree of the polynomial function - higher the degree, greater is the growth. The next natural question is:

![Image block](doc:8b97716/tier:standard/page:23/block:5)

Fig 5.9

Is there a function which grows faster than any polynomial function. The answer is in affirmative and an example of such a function is

$$
y = f (x) = 1 0 ^ {x}.
$$

Our claim is that this function $f$ grows faster than $f_{n}(x) = x^{n}$ for any positive integer $n$. For example, we can prove that $10^{x}$ grows faster than $f_{100}(x) = x^{100}$. For large values of $x$ like $x = 10^{3}$, note that $f_{100}(x) = (10^{3})^{100} = 10^{300}$ whereas $f(10^{3}) = 10^{10^{3}} = 10^{1000}$. Clearly $f(x)$ is much greater than $f_{100}(x)$. It is not difficult to prove that for all $x > 10^{3}, f(x) > f_{100}(x)$. But we will not attempt to give a proof of this here. Similarly, by choosing large values of $x$, one can verify that $f(x)$ grows faster than $f_{n}(x)$ for any positive integer $n$.

Definition 3 The exponential function with positive base $b > 1$ is the function

$$
y = f (x) = b ^ {x}
$$

The graph of $y = 10^{x}$ is given in the Fig 5.9.

It is advised that the reader plots this graph for particular values of $b$ like 2, 3 and 4. Following are some of the salient features of the exponential functions:

(1) Domain of the exponential function is $\mathbf{R}$, the set of all real numbers.

(2) Range of the exponential function is the set of all positive real numbers.

(3) The point  $(0, 1)$  is always on the graph of the exponential function (this is a restatement of the fact that  $b^{0} = 1$  for any real b > 1).

(4) Exponential function is ever increasing; i.e., as we move from left to right, the graph rises above.

Reprint 2025-26

<!-- page 24 of 43 -->

CONTINUITY AND DIFFERENTIABILITY

127

(5) For very large negative values of x, the exponential function is very close to 0. In other words, in the second quadrant, the graph approaches x-axis (but never meets it).

Exponential function with base 10 is called the common exponential function. In the Appendix A.1.4 of Class XI, it was observed that the sum of the series

$$
1 + \frac {1}{1 !} + \frac {1}{2 !} + \dots
$$

is a number between 2 and 3 and is denoted by $e$. Using this $e$ as the base we obtain an extremely important exponential function $y = e^x$.

This is called natural exponential function.

It would be interesting to know if the inverse of the exponential function exists and has nice interpretation. This search motivates the following definition.

Definition 4 Let $b > 1$ be a real number. Then we say logarithm of $a$ to base $b$ is $x$ if $b^x = a$.

Logarithm of $a$ to base $b$ is denoted by $\log_b a$. Thus $\log_b a = x$ if $b^x = a$. Let us work with a few explicit examples to get a feel for this. We know $2^3 = 8$. In terms of logarithms, we may rewrite this as $\log_2 8 = 3$. Similarly, $10^4 = 10000$ is equivalent to saying $\log_{10} 10000 = 4$. Also, $625 = 5^4 = 25^2$ is equivalent to saying $\log_5 625 = 4$ or $\log_{25} 625 = 2$.

On a slightly more mature note, fixing a base b > 1, we may look at logarithm as a function from positive real numbers to all real numbers. This function, called the logarithmic function, is defined by

$$
\begin{array}{c} \log_ {b}: \mathbf {R} ^ {+} \to \mathbf {R} \\ x \to \log_ {b} x = y \quad \text {if} b ^ {y} = x \end{array}
$$

As before if the base b = 10, we say it is common logarithms and if b = e, then we say it is natural logarithms. Often natural logarithm is denoted by ln. In this chapter, log x denotes the logarithm function to base e, i.e., ln x will be written as simply log x. The Fig 5.10 gives the plots of logarithm function to base 2, e and 10.

Some of the important observations about the logarithm function to any base b > 1 are listed below:

![Image block](doc:8b97716/tier:standard/page:24/block:15)

Fig 5.10

Reprint 2025-26

<!-- page 25 of 43 -->

128

MATHEMATICS

(1) We cannot make a meaningful definition of logarithm of non-positive numbers and hence the domain of log function is  $R^{+}$ .

(2) The range of log function is the set of all real numbers.

(3) The point $(1,0)$ is always on the graph of the log function.

(4) The log function is ever increasing, i.e., as we move from left to right the graph rises above.

(5) For x very near to zero, the value of  $\log x$  can be made lesser than any given real number. In other words in the fourth quadrant the graph approaches y-axis (but never meets it).

(6) Fig 5.11 gives the plot of $y = e^x$ and $y = ln x$. It is of interest to observe that the two curves are the mirror

![Image block](doc:8b97716/tier:standard/page:25/block:9)

Fig 5.11

images of each other reflected in the line $y = x$,

Two properties of 'log' functions are proved below:

(1) There is a standard change of base rule to obtain $\log_a p$ in terms of $\log_b p$. Let $\log_a p = \alpha$, $\log_b p = \beta$ and $\log_b a = \gamma$. This means $a^\alpha = p$, $b^\beta = p$ and $b^\gamma = a$. Substituting the third equation in the first one, we have

$$
(b ^ {\gamma}) ^ {\alpha} = b ^ {\gamma \alpha} = p
$$

Using this in the second equation, we get

$$
b ^ {\beta} = p = b ^ {\gamma \alpha}
$$

which implies $\beta = \alpha \gamma$ or $\alpha = \frac{\beta}{\gamma}$. But then

$$
\log_ {a} p = \frac {\log_ {b} p}{\log_ {b} a}
$$

(2) Another interesting property of the log function is its effect on products. Let $\log_b pq = \alpha$. Then $b^\alpha = pq$. If $\log_b p = \beta$ and $\log_b q = \gamma$, then $b^\beta = p$ and $b^\gamma = q$. But then $b^\alpha = pq = b^\beta b^\gamma = b^{\beta + \gamma}$ which implies $\alpha = \beta + \gamma$, i.e.,

$$
\log_ {b} p q = \log_ {b} p + \log_ {b} q
$$

Reprint 2025-26

<!-- page 26 of 43 -->

CONTINUITY AND DIFFERENTIABILITY

129

A particularly interesting and important consequence of this is when p = q. In this case the above may be rewritten as

$$
\log_ {b} p ^ {2} = \log_ {b} p + \log_ {b} p = 2 \log p
$$

An easy generalisation of this (left as an exercise!) is

$$
\log_ {b} p ^ {n} = n \log p
$$

for any positive integer $n$. In fact this is true for any real number $n$, but we will not attempt to prove this. On the similar lines the reader is invited to verify

$$
\log_ {b} \frac {x}{y} = \log_ {b} x - \log_ {b} y
$$

Example 25 Is it true that $x = e^{\log x}$ for all real $x$?

Solution First, observe that the domain of log function is set of all positive real numbers. So the above equation is not true for non-positive real numbers. Now, let  $y = e^{\log x}$ . If y > 0, we may take logarithm which gives us  $\log y = \log (e^{\log x}) = \log x$ .  $\log e = \log x$ . Thus y = x. Hence  $x = e^{\log x}$  is true only for positive values of x.

One of the striking properties of the natural exponential function in differential calculus is that it doesn't change during the process of differentiation. This is captured in the following theorem whose proof we skip.

Theorem 5\*

(1) The derivative of $e^x$ w.r.t., $x$ is $e^x$; i.e., $\frac{d}{dx}(e^x) = e^x$.

(2) The derivative of $\log x$ w.r.t., $x$ is $\frac{1}{x}$; i.e., $\frac{d}{dx} (\log x) = \frac{1}{x}$.

Example 26 Differentiate the following w.r.t. $x$:

(i) $e^{-x}$ (ii) $\sin (\log x), x > 0$ (iii) $\cos^{-1}(e^x)$ (iv) $e^{\cos x}$

Solution

(i) Let $y = e^{-x}$. Using chain rule, we have

$$
\frac {d y}{d x} = e ^ {- x} \cdot \frac {d}{d x} (- x) = - e ^ {- x}
$$

(ii) Let $y = \sin (\log x)$. Using chain rule, we have

$$
\frac {d y}{d x} = \cos (\log x) \cdot \frac {d}{d x} (\log x) = \frac {\cos (\log x)}{x}
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">\* Please see supplementary material on Page 222.</span></small>

Reprint 2025-26

<!-- page 27 of 43 -->

130

MATHEMATICS

(iii) Let $y = \cos^{-1}(e^x)$. Using chain rule, we have

$$
\frac {d y}{d x} = \frac {- 1}{\sqrt {1 - \left(e ^ {x}\right) ^ {2}}} \cdot \frac {d}{d x} \left(e ^ {x}\right) = \frac {- e ^ {x}}{\sqrt {1 - e ^ {2 x}}}
$$

(iv) Let $y = e^{\cos x}$. Using chain rule, we have

$$
\frac {d y}{d x} = e ^ {\cos x} \cdot (- \sin x) = - (\sin x) e ^ {\cos x}
$$

## EXERCISE 5.4

Differentiate the following w.r.t. $x$:

1. $\frac{e^x}{\sin x}$ 2. $e^{\sin^{-1}x}$ 3. $e^{x^3}$

4. $\sin (\tan^{-1}e^{-x})$ 5. $\log (\cos e^x)$ 6. $e^{x} + e^{x^{2}} + \dots +e^{x^{5}}$

7. $\sqrt{e^{\sqrt{x}}}$, $x > 0$ 8. $\log (\log x)$, $x > 1$ 9. $\frac{\cos x}{\log x}$, $x > 0$

10. $\cos (\log x + e^x), x > 0$

## 5.5. Logarithmic Differentiation

In this section, we will learn to differentiate certain special class of functions given in the form

$$
y = f (x) = [ u (x) ] ^ {v (x)}
$$

By taking logarithm (to base $e$) the above may be rewritten as

$\log y = v(x)\log [u(x)]$

Using chain rule we may differentiate this to get

$$
\frac {1}{y} \cdot \frac {d y}{d x} = v (x) \cdot \frac {1}{u (x)} \cdot u ^ {\prime} (x) + v ^ {\prime} (x) \cdot \log [ u (x) ]
$$

which implies that

$$
\frac {d y}{d x} = y \left[ \frac {v (x)}{u (x)} \cdot u ^ {\prime} (x) + v ^ {\prime} (x) \cdot \log [ u (x) ] \right]
$$

The main point to be noted in this method is that  $f(x)$  and  $u(x)$  must always be positive as otherwise their logarithms are not defined. This process of differentiation is known as logarithms differentiation and is illustrated by the following examples:

Reprint 2025-26

<!-- page 28 of 43 -->

CONTINUITY AND DIFFERENTIABILITY

131

Example 27 Differentiate $\sqrt{\frac{(x - 3)(x^2 + 4)}{3x^2 + 4x + 5}}$ w.r.t. $x$.

Solution Let  $y=\sqrt{\frac{(x-3)(x^{2}+4)}{(3x^{2}+4x+5)}}$

Taking logarithm on both sides, we have

$$
\log y = \frac {1}{2} \left[ \log (x - 3) + \log (x ^ {2} + 4) - \log (3 x ^ {2} + 4 x + 5) \right]
$$

Now, differentiating both sides w.r.t. $x$, we get

$$
\frac {1}{y} \cdot \frac {d y}{d x} = \frac {1}{2} \left[ \frac {1}{(x - 3)} + \frac {2 x}{x ^ {2} + 4} - \frac {6 x + 4}{3 x ^ {2} + 4 x + 5} \right]
$$

or

$$
\begin{array}{r l} \frac {d y}{d x} & = \frac {y}{2} \left[ \frac {1}{(x - 3)} + \frac {2 x}{x ^ {2} + 4} - \frac {6 x + 4}{3 x ^ {2} + 4 x + 5} \right] \\ & = \frac {1}{2} \sqrt {\frac {(x - 3) (x ^ {2} + 4)}{3 x ^ {2} + 4 x + 5}} \left[ \frac {1}{(x - 3)} + \frac {2 x}{x ^ {2} + 4} - \frac {6 x + 4}{3 x ^ {2} + 4 x + 5} \right] \end{array}
$$

Example 28 Differentiate $a^x$ w.r.t. $x$, where $a$ is a positive constant.

Solution Let $y = a^x$. Then

$\log y = x\log a$

Differentiating both sides w.r.t. $x$, we have

$$
\frac {1}{y} \frac {d y}{d x} = \log a
$$

or

$$
\frac {d y}{d x} = y \log a
$$

Thus

$$
\frac {d}{d x} (a ^ {x}) = a ^ {x} \log a
$$

Alternatively

$$
\begin{array}{r l} \frac {d}{d x} (a ^ {x}) & = \frac {d}{d x} (e ^ {x \log a}) = e ^ {x \log a} \frac {d}{d x} (x \log a) \\ & = e ^ {x \log a}. \log a = a ^ {x} \log a. \end{array}
$$

Reprint 2025-26

<!-- page 29 of 43 -->

132

MATHEMATICS

Example 29 Differentiate $x^{\sin x}, x > 0$ w.r.t. $x$.

Solution Let $y = x^{\sin x}$. Taking logarithm on both sides, we have

$$
\log y = \sin x \log x
$$

Therefore

$$
\frac {1}{y} \cdot \frac {d y}{d x} = \sin x \frac {d}{d x} (\log x) + \log x \frac {d}{d x} (\sin x)
$$

or

$$
\frac {1}{y} \frac {d y}{d x} = (\sin x) \frac {1}{x} + \log x \cos x
$$

or

$$
\frac {d y}{d x} = y \left[ \frac {\sin x}{x} + \cos x \log x \right]
$$

$$
\begin{array}{l} = x ^ {\sin x} \left[ \frac {\sin x}{x} + \cos x \log x \right] \\ = x ^ {\sin x - 1} \cdot \sin x + x ^ {\sin x} \cdot \cos x \log x \end{array}
$$

Example 30 Find $\frac{dy}{dx}$, if $y^{x} + x^{y} + x^{x} = a^{b}$.

Solution Given that $y^{x} + x^{y} + x^{z} = a^{b}$.

Putting $u = y^{x}$, $v = x^{y}$ and $w = x^{x}$, we get $u + v + w = a^{b}$

Therefore

$$
\frac {d u}{d x} + \frac {d v}{d x} + \frac {d w}{d x} = 0\tag{... (1}
$$

Now, $u = y^{x}$. Taking logarithm on both sides, we have

$$
\log u = x \log y
$$

Differentiating both sides w.r.t. $x$, we have

$$
\begin{array}{r l} \frac {1}{u} \cdot \frac {d u}{d x} & = x \frac {d}{d x} (\log y) + \log y \frac {d}{d x} (x) \\ & = x \frac {1}{y} \cdot \frac {d y}{d x} + \log y \cdot 1 \end{array}
$$

So

$$
\frac {d u}{d x} = u \left(\frac {x}{y} \frac {d y}{d x} + \log y\right) = y ^ {x} \left[ \frac {x}{y} \frac {d y}{d x} + \log y \right]\tag{... (2}
$$

Also $v = x^{y}$

Reprint 2025-26

<!-- page 30 of 43 -->

... (3)

CONTINUITY AND DIFFERENTIABILITY

133

Taking logarithm on both sides, we have

$$
\log v = y \log x
$$

Differentiating both sides w.r.t. $x$, we have

$$
\left| \begin{array}{l} \frac {1}{v} \cdot \frac {d v}{d x} = y \frac {d}{d x} (\log x) + \log x \frac {d y}{d x} \\ = y \cdot \frac {1}{x} + \log x \cdot \frac {d y}{d x} \end{array} \right|
$$

So

$$
\begin{array}{r l} \frac {d v}{d x} & = v \left[ \frac {y}{x} + \log x \frac {d y}{d x} \right] \\ & = x ^ {y} \left[ \frac {y}{x} + \log x \frac {d y}{d x} \right] \end{array}
$$

Again

$$
w = x ^ {x}
$$

Taking logarithm on both sides, we have

$$
\log w = x \log x.
$$

Differentiating both sides w.r.t. $x$, we have

$$
\frac {1}{w} \cdot \frac {d w}{d x} = x \frac {d}{d x} (\log x) + \log x \cdot \frac {d}{d x} (x)\tag{©}
$$

$$
= x \cdot \frac {1}{x} + \log x \cdot 1
$$

i.e.

$$
\begin{array}{r l} \frac {d w}{d x} & = w (1 + \log x) \\ & = x ^ {x} (1 + \log x) \end{array}\tag{... (4}
$$

From (1), (2), (3), (4), we have

$$
y ^ {x} \left(\frac {x}{y} \frac {d y}{d x} + \log y\right) + x ^ {y} \left(\frac {y}{x} + \log x \frac {d y}{d x}\right) + x ^ {x} (1 + \log x) = 0
$$

or

$$
(x \cdot y ^ {x - 1} + x ^ {y} \cdot \log x) \frac {d y}{d x} = - x ^ {x} (1 + \log x) - y \cdot x ^ {y - 1} - y ^ {x} \log y
$$

Therefore

$$
\frac {d y}{d x} = \frac {- \left[ y ^ {x} \log y + y . x ^ {y - 1} + x ^ {x} (1 + \log x) \right]}{x . y ^ {x - 1} + x ^ {y} \log x}
$$

Reprint 2025-26

<!-- page 31 of 43 -->

134

MATHEMATICS

## EXERCISE 5.5

Differentiate the functions given in Exercises 1 to 11 w.r.t. $x$.

1. $\cos x.\cos 2x.\cos 3x$

2.  $\sqrt{\frac{(x-1)(x-2)}{(x-3)(x-4)(x-5)}}$

3. $(\log x)^{\cos x}$

4. $x^{x} - 2^{\sin x}$

5. $(x + 3)^2\cdot (x + 4)^3\cdot (x + 5)^4$

6. $\left(x + \frac{1}{x}\right)^x + x^{\left(1 + \frac{1}{x}\right)}$

7. $(\log x)^x + x^{\log x}$

8. $(\sin x)^{x} + \sin^{-1}\sqrt{x}$

9. $x^{\sin x} + (\sin x)^{\cos x}$ 10. $x^{x\cos x} + \frac{x^2 + 1}{x^2 - 1}$

11. $(x\cos x)^{x} + (x\sin x)^{\frac{1}{x}}$

Find $\frac{dy}{dx}$ of the functions given in Exercises 12 to 15.

12. $x^{y} + y^{x} = 1$

13. $y^{x} = x^{y}$

14. $(\cos x)^{y} = (\cos y)^{x}$

15. $xy = e^{(x - y)}$

16. Find the derivative of the function given by $f(x) = (1 + x)(1 + x^2)(1 + x^4)(1 + x^8)$ and hence find $f'(1)$.

17. Differentiate $(x^{2} - 5x + 8)(x^{3} + 7x + 9)$ in three ways mentioned below:

(i) by using product rule

(ii) by expanding the product to obtain a single polynomial.

(iii) by logarithmic differentiation.

Do they all give the same answer?

18. If $u, v$ and $w$ are functions of $x$, then show that

$$
\frac {d}{d x} (u. v. w) = \frac {d u}{d x} v. w + u. \frac {d v}{d x}. w + u. v \frac {d w}{d x}
$$

in two ways - first by repeated application of product rule, second by logarithmic differentiation.

## 5.6 Derivatives of Functions in Parametric Forms

Sometimes the relation between two variables is neither explicit nor implicit, but some link of a third variable with each of the two variables, separately, establishes a relation between the first two variables. In such a situation, we say that the relation between

Reprint 2025-26

<!-- page 32 of 43 -->

CONTINUITY AND DIFFERENTIABILITY

135

them is expressed via a third variable. The third variable is called the parameter. More precisely, a relation expressed between two variables $x$ and $y$ in the form $x = f(t), y = g(t)$ is said to be parametric form with $t$ as a parameter.

In order to find derivative of function in such form, we have by chain rule.

$$
\frac {d y}{d t} = \frac {d y}{d x} \cdot \frac {d x}{d t}
$$

or

$$
\frac {d y}{d x} = \frac {\frac {d y}{d t}}{\frac {d x}{d t}} \left(\text {whenever} \frac {d x}{d t} \neq 0\right)
$$

Thus

$$
\frac {d y}{d x} = \frac {g ^ {\prime} (t)}{f ^ {\prime} (t)} \left(\text {as} \frac {d y}{d t} = g ^ {\prime} (t) \text {and} \frac {d x}{d t} = f ^ {\prime} (t)\right) [ \text {provided} f ^ {\prime} (t) \neq 0 ]
$$

Example 31 Find $\frac{dy}{dx}$, if $x = a\cos \theta, y = a\sin \theta$.

Solution Given that

$$
x = a \cos \theta , y = a \sin \theta
$$

Therefore

$$
\frac {d x}{d \theta} = - a \sin \theta , \frac {d y}{d \theta} = a \cos \theta
$$

Hence

$$
\frac {d y}{d x} = \frac {\frac {d y}{d \theta}}{\frac {d x}{d \theta}} = \frac {a \cos \theta}{- a \sin \theta} = - \cot \theta
$$

Example 32 Find $\frac{dy}{dx}$, if $x = at^2$, $y = 2at$.

Solution Given that $x = at^2$, $y = 2at$

So

$$
\frac {d x}{d t} = 2 a t \quad \text {and} \quad \frac {d y}{d t} = 2 a
$$

Therefore

$$
\frac {d y}{d x} = \frac {\frac {d y}{d t}}{\frac {d x}{d t}} = \frac {2 a}{2 a t} = \frac {1}{t}
$$

Reprint 2025-26

<!-- page 33 of 43 -->

136

MATHEMATICS

Example 33 Find $\frac{dy}{dx}$, if $x = a (\theta + \sin \theta)$, $y = a (1 - \cos \theta)$.

Solution We have $\frac{dx}{d\theta} = a(1 + \cos \theta),\frac{dy}{d\theta} = a(\sin \theta)$

Therefore

$$
\frac {d y}{d x} = \frac {\frac {d y}{d \theta}}{\frac {d x}{d \theta}} = \frac {a \sin \theta}{a (1 + \cos \theta)} = \tan \frac {\theta}{2}\left. \right\}
$$

Note It may be noted here that $\frac{dy}{dx}$ is expressed in terms of parameter only without directly involving the main variables $x$ and $y$.

Example 34 Find $\frac{dy}{dx}$, if $x^{\frac{2}{3}} + y^{\frac{2}{3}} = a^{\frac{2}{3}}$.

Solution Let $x = a\cos^3\theta, y = a\sin^3\theta$. Then

$$
\begin{array}{r l} x ^ {\frac {2}{3}} + y ^ {\frac {2}{3}} & = (a \cos^ {3} \theta) ^ {\frac {2}{3}} + (a \sin^ {3} \theta) ^ {\frac {2}{3}} \\ & = a ^ {\frac {2}{3}} (\cos^ {2} \theta + (\sin^ {2} \theta) = a ^ {\frac {2}{3}} \end{array}
$$

Hence, $x = a\cos^3\theta$, $y = a\sin^3\theta$ is parametric equation of $x^{\frac{2}{3}} + y^{\frac{2}{3}} = a^{\frac{2}{3}}$

Now

$$
\frac {d x}{d \theta} = - 3 a \cos^ {2} \theta \sin \theta \text {and} \frac {d y}{d \theta} = 3 a \sin^ {2} \theta \cos \theta
$$

Therefore

$$
\frac {d y}{d x} = \frac {\frac {d y}{d \theta}}{\frac {d x}{d \theta}} = \frac {3 a \sin^ {2} \theta \cos \theta}{- 3 a \cos^ {2} \theta \sin \theta} = - \tan \theta = - \sqrt [ 3 ]{\frac {y}{x}}
$$

Reprint 2025-26

<!-- page 34 of 43 -->

CONTINUITY AND DIFFERENTIABILITY

137

## EXERCISE 5.6

If $x$ and $y$ are connected parametrically by the equations given in Exercises 1 to 10, without eliminating the parameter, Find $\frac{dy}{dx}$.

1. $x = 2at^{2},y = at^{4}$

2. $x = a\cos \theta ,y = b\cos \theta$

3. $x = \sin t, y = \cos 2t$

4. $x = 4t, y = \frac{4}{t}$

5. $x = \cos \theta -\cos 2\theta ,y = \sin \theta -\sin 2\theta$

6. $x = a(\theta -\sin \theta),y = a(1 + \cos \theta)$ 7. $x = \frac{\sin^3t}{\sqrt{\cos 2t}},y = \frac{\cos^3t}{\sqrt{\cos 2t}}$

8. $x = a\left(\cos t + \log \tan \frac{t}{2}\right)y = a\sin t$ 9. $x = a\sec \theta, y = b\tan \theta$

10. $x = a(\cos \theta +\theta \sin \theta),y = a(\sin \theta -\theta \cos \theta)$

11. If $x = \sqrt{a^{\sin^{-1}t}}$, $y = \sqrt{a^{\cos^{-1}t}}$, show that $\frac{dy}{dx} = -\frac{y}{x}$

## 5.7 Second Order Derivative

Let $y = f(x)$. Then

$$
\frac {d y}{d x} = f ^ {\prime} (x)\tag{... (1}
$$

If $f'(x)$ is differentiable, we may differentiate (1) again w.r.t. $x$. Then, the left hand side becomes $\frac{d}{dx}\left(\frac{dy}{dx}\right)$ which is called the second order derivative of $y$ w.r.t. $x$ and is denoted by $\frac{d^2y}{dx^2}$. The second order derivative of $f(x)$ is denoted by $f''(x)$. It is also denoted by $D^2y$ or $y''$ or $y_2$ if $y = f(x)$. We remark that higher order derivatives may be defined similarly.

Reprint 2025-26

<!-- page 35 of 43 -->

138

MATHEMATICS

Example 35 Find $\frac{d^2y}{dx^2}$, if $y = x^3 + \tan x$.

Solution Given that $y = x^{3} + \tan x$. Then

$$
\frac {d y}{d x} = 3 x ^ {2} + \sec^ {2} x
$$

Therefore

$$
\begin{array}{r l} \frac {d ^ {2} y}{d x ^ {2}} & = \frac {d}{d x} \left(3 x ^ {2} + \sec^ {2} x\right) \\ & = 6 x + 2 \sec x. \sec x \tan x = 6 x + 2 \sec^ {2} x \tan x \end{array}
$$

Example 36 If $y = A \sin x + B \cos x$, then prove that $\frac{d^2y}{dx^2} + y = 0$.

Solution We have

$$
\frac {d y}{d x} = \mathrm{A} \cos x - \mathrm{B} \sin x
$$

and

$$
\frac {d ^ {2} y}{d x ^ {2}} = \frac {d}{d x} (\mathrm{A} \cos x - \mathrm{B} \sin x)
$$

$$
= - \mathrm{A} \sin x - \mathrm{B} \cos x = - y
$$

Hence

$$
\frac {d ^ {2} y}{d x ^ {2}} + y = 0
$$

Example 37 If $y = 3e^{2x} + 2e^{3x}$, prove that $\frac{d^2y}{dx^2} - 5\frac{dy}{dx} + 6y = 0$.

Solution Given that $y = 3e^{2x} + 2e^{3x}$. Then

$$
\frac {d y}{d x} = 6 e ^ {2 x} + 6 e ^ {3 x} = 6 (e ^ {2 x} + e ^ {3 x})
$$

Therefore

$$
\frac {d ^ {2} y}{d x ^ {2}} = 1 2 e ^ {2 x} + 1 8 e ^ {3 x} = 6 \left(2 e ^ {2 x} + 3 e ^ {3 x}\right)
$$

Hence

$$
\begin{array}{r l} \frac {d ^ {2} y}{d x ^ {2}} - 5 \frac {d y}{d x} + 6 y & = 6 (2 e ^ {2 x} + 3 e ^ {3 x}) \\ & - 3 0 (e ^ {2 x} + e ^ {3 x}) + 6 (3 e ^ {2 x} + 2 e ^ {3 x}) = 0 \end{array}
$$

Reprint 2025-26

<!-- page 36 of 43 -->

CONTINUITY AND DIFFERENTIABILITY

139

Example 38 If $y = \sin^{-1} x$, show that $(1 - x^2) \frac{d^2y}{dx^2} - x \frac{dy}{dx} = 0$.

Solution We have $y = \sin^{-1}x$. Then

$$
\frac {d y}{d x} = \frac {1}{\sqrt {\left(1 - x ^ {2}\right)}}
$$

or

$$
\sqrt {(1 - x ^ {2})} \frac {d y}{d x} = 1
$$

So

$$
\frac {d}{d x} \Bigg (\sqrt {(1 - x ^ {2})} \cdot \frac {d y}{d x} \Bigg) = 0
$$

or

$$
\sqrt {(1 - x ^ {2})} \cdot \frac {d ^ {2} y}{d x ^ {2}} + \frac {d y}{d x} \cdot \frac {d}{d x} \Big (\sqrt {(1 - x ^ {2})} \Big) = 0
$$

or

$$
\sqrt {(1 - x ^ {2})} \cdot \frac {d ^ {2} y}{d x ^ {2}} - \frac {d y}{d x} \cdot \frac {2 x}{2 \sqrt {1 - x ^ {2}}} = 0
$$

Hence

$$
(1 - x ^ {2}) \frac {d ^ {2} y}{d x ^ {2}} - x \frac {d y}{d x} = 0
$$

Alternatively, Given that $y = \sin^{-1}x$, we have

$$
y _ {1} = \frac {1}{\sqrt {1 - x ^ {2}}}, \text { i.e., } (1 - x ^ {2}) y _ {1} ^ {2} = 1
$$

So

$$
(1 - x ^ {2}). 2 y _ {1} y _ {2} + y _ {1} ^ {2} (0 - 2 x) = 0
$$

Hence

$$
(1 - x ^ {2}) y _ {2} - x y _ {1} = 0
$$

## EXERCISE 5.7

Find the second order derivatives of the functions given in Exercises 1 to 10.

1. $x^{2} + 3x + 2$ 2. $x^{20}$ 3. $x.\cos x$

4. $\log x$ 5. $x^{3}\log x$ 6. $e^{x}\sin 5x$

7. $e^{6x}\cos 3x$ 8. $\tan^{-1}x$ 9. log (log x)

10. $\sin (\log x)$  
11. If $y = 5\cos x - 3\sin x$ , prove that $\frac{d^2y}{dx^2} +y = 0$

Reprint 2025-26

<!-- page 37 of 43 -->

140

MATHEMATICS

12. If $y = \cos^{-1}x$, Find $\frac{d^2y}{dx^2}$ in terms of $y$ alone.

13. If $y = 3\cos (\log x) + 4\sin (\log x)$, show that $x^{2}y_{2} + xy_{1} + y = 0$

14. If $y = \mathrm{A}e^{mx} + \mathrm{Be}^{nx}$, show that $\frac{d^2y}{dx^2} - (m + n)\frac{dy}{dx} + mny = 0$

15. If $y = 500e^{7x} + 600e^{-7x}$, show that $\frac{d^2y}{dx^2} = 49y$

16. If $e^y (x + 1) = 1$, show that $\frac{d^2y}{dx^2} = \left(\frac{dy}{dx}\right)^2$

17. If $y = (\tan^{-1}x)^2$, show that $(x^{2} + 1)^{2}y_{2} + 2x(x^{2} + 1)y_{1} = 2$

## Miscellaneous Examples

Example 39 Differentiate w.r.t. $x$, the following function:

(i) $\sqrt{3x + 2} +\frac{1}{\sqrt{2x^2 + 4}}$ (ii) $\log_7(\log x)$

Solution

(i) Let $y = \sqrt{3x + 2} + \frac{1}{\sqrt{2x^2 + 4}} = (3x + 2)^{\frac{1}{2}} + (2x^2 + 4)^{-\frac{1}{2}}$

Note that this function is defined at all real numbers $x > -\frac{2}{3}$. Therefore

$$
\begin{array}{r l} \frac {d y}{d x} & = \frac {1}{2} (3 x + 2) ^ {\frac {1}{2} - 1} \cdot \frac {d}{d x} (3 x + 2) + \left(- \frac {1}{2}\right) (2 x ^ {2} + 4) ^ {- \frac {1}{2} - 1} \cdot \frac {d}{d x} (2 x ^ {2} + 4) \\ & = \frac {1}{2} (3 x + 2) ^ {- \frac {1}{2}} \cdot (3) - \left(\frac {1}{2}\right) (2 x ^ {2} + 4) ^ {- \frac {3}{2}} \cdot 4 x \\ & = \frac {3}{2 \sqrt {3 x + 2}} - \frac {2 x}{(2 x ^ {2} + 4) ^ {\frac {3}{2}}} \end{array}
$$

This is defined for all real numbers $x > -\frac{2}{3}$.

Reprint 2025-26

<!-- page 38 of 43 -->

CONTINUITY AND DIFFERENTIABILITY

141

(ii) Let $y = \log_7(\log x) = \frac{\log(\log x)}{\log 7}$ (by change of base formula).

The function is defined for all real numbers $x > 1$. Therefore

$$
\left| \begin{array}{l} \frac {d y}{d x} = \frac {1}{\log 7} \frac {d}{d x} (\log (\log x)) \\ = \frac {1}{\log 7} \frac {1}{\log x} \cdot \frac {d}{d x} (\log x) \\ = \frac {1}{x \log 7 \log x} \end{array} \right|
$$

Example 40 Differentiate the following w.r.t. $x$.

(i) $\cos^{-1}(\sin x)$

$$
\tan^ {- 1} \left(\frac {\sin x}{1 + \cos x}\right)
$$

(iii)  $\sin^{-1}\left(\frac{2^{x+1}}{1+4^{x}}\right)$

Solution

(i) Let $f(x) = \cos^{-1}(\sin x)$. Observe that this function is defined for all real numbers. We may rewrite this function as

$$
\begin{array}{r l} f (x) & = \cos^ {- 1} (\sin x) \\ & = \cos^ {- 1} \left[ \cos \left(\frac {\pi}{2} - x\right) \right] \\ & = \frac {\pi}{2} - x \end{array}
$$

Thus $f'(x) = -1$.

(ii) Let $f(x) = \tan^{-1}\left(\frac{\sin x}{1 + \cos x}\right)$. Observe that this function is defined for all real numbers, where $\cos x \neq -1$; i.e., at all odd multiplies of $\pi$. We may rewrite this function as

$$
\begin{array}{r l} f (x) & = \tan^ {- 1} \left(\frac {\sin x}{1 + \cos x}\right) \\ & = \tan^ {- 1} \left[ \frac {2 \sin \left(\frac {x}{2}\right) \cos \left(\frac {x}{2}\right)}{2 \cos^ {2} \frac {x}{2}} \right] \end{array}
$$

Reprint 2025-26

<!-- page 39 of 43 -->

142

MATHEMATICS

$$
= \tan^ {- 1} \left[ \tan \left(\frac {x}{2}\right) \right] = \frac {x}{2}
$$

Observe that we could cancel $\cos\left(\frac{x}{2}\right)$ in both numerator and denominator as it is not equal to zero. Thus $f'(x) = \frac{1}{2}$. Let $f(x) = \sin^{-1}\left(\frac{2^{x+1}}{1+4^x}\right)$. To find the domain of this function we need to find all $x$ such that $-1 \leq \frac{2^{x+1}}{1+4^x} \leq 1$. Since the quantity in the middle is always positive, we need to find all $x$ such that $\frac{2^{x+1}}{1+4^x} \leq 1$, i.e., all $x$ such that $2^{x+1} \leq 1+4^x$. We may rewrite this as $2 \leq \frac{1}{2^x} + 2^x$ which is true for all $x$. Hence the function is defined at every real number. By putting $2^x = \tan \theta$, this function may be rewritten as

$$
\begin{array}{r l} f (x) & = \sin^ {- 1} \left[ \frac {2 ^ {x + 1}}{1 + 4 ^ {x}} \right] \\ & = \sin^ {- 1} \left[ \frac {2 ^ {x} \cdot 2}{1 + (2 ^ {x}) ^ {2}} \right] \\ & = \sin^ {- 1} \left[ \frac {2 \tan \theta}{1 + \tan^ {2} \theta} \right] \\ & = \sin^ {- 1} [ \sin 2 \theta ] \\ & = 2 \theta = 2 \tan^ {- 1} (2 ^ {x}) \end{array}
$$

Thus

$$
\begin{array}{r l} f ^ {\prime} (x) & = 2 \cdot \frac {1}{1 + \left(2 ^ {x}\right) ^ {2}} \cdot \frac {d}{d x} (2 ^ {x}) \\ & = \frac {2}{1 + 4 ^ {x}} \cdot (2 ^ {x}) \log 2 \\ & = \frac {2 ^ {x + 1} \log 2}{1 + 4 ^ {x}} \end{array}
$$

Reprint 2025-26

<!-- page 40 of 43 -->

CONTINUITY AND DIFFERENTIABILITY

143

Example 41 Find $f'(x)$ if $f(x) = (\sin x)^{\sin x}$ for all $0 < x < \pi$.

Solution The function  $y = (\sin x)^{\sin x}$  is defined for all positive real numbers. Taking logarithms, we have

$$
\log y = \log (\sin x) ^ {\sin x} = \sin x \log (\sin x)
$$

Then

$$
\begin{array}{r l} \frac {1}{y} \frac {d y}{d x} & = \frac {d}{d x} (\sin x \log (\sin x)) \\ & = \cos x \log (\sin x) + \sin x. \frac {1}{\sin x} \cdot \frac {d}{d x} (\sin x) \\ & = \cos x \log (\sin x) + \cos x \\ & = (1 + \log (\sin x)) \cos x \end{array}
$$

Thus

$$
\frac {d y}{d x} = y ((1 + \log (\sin x)) \cos x) = (1 + \log (\sin x)) (\sin x) ^ {\sin x} \cos x
$$

Example 42 For a positive constant $a$ find $\frac{dy}{dx}$, where

$$
\left| y = a ^ {t + \frac {1}{t}}, \text {and} x = \left(t + \frac {1}{t}\right) ^ {a} \right|
$$

Solution Observe that both $y$ and $x$ are defined for all real $t \neq 0$. Clearly

$$
\frac {d y}{d t} = \frac {d}{d t} \left(a ^ {t + \frac {1}{t}}\right) = a ^ {t + \frac {1}{t}} \frac {d}{d t} \left(t + \frac {1}{t}\right) \cdot \log a
$$

$$
= a ^ {t + \frac {1}{t}} \left(1 - \frac {1}{t ^ {2}}\right) \log a \Bigg |
$$

Similarly

$$
\left| \frac {d x}{d t} = a \left[ t + \frac {1}{t} \right] ^ {a - 1} \cdot \frac {d}{d t} \left(t + \frac {1}{t}\right) \right|
$$

$$
= a \left[ t + \frac {1}{t} \right] ^ {a - 1} \cdot \left(1 - \frac {1}{t ^ {2}}\right)
$$

$\frac{dx}{dt} \neq 0$ only if $t \neq \pm 1$. Thus for $t \neq \pm 1$,

Reprint 2025-26

<!-- page 41 of 43 -->

144

MATHEMATICS

$$
\frac {d y}{d x} = \frac {\frac {d y}{d t}}{\frac {d x}{d t}} = \frac {a ^ {t + \frac {1}{t}} \left(1 - \frac {1}{t ^ {2}}\right) \log a}{a \left[ t + \frac {1}{t} \right] ^ {a - 1} \cdot \left(1 - \frac {1}{t ^ {2}}\right)}
$$

$$
= \frac {a ^ {t + \frac {1}{t}} \log a}{a \left(t + \frac {1}{t}\right) ^ {a - 1}}
$$

Example 43 Differentiate $\sin^2 x$ w.r.t. $e^{\cos x}$.

Solution Let $u(x) = \sin^2 x$ and $v(x) = e^{\cos x}$. We want to find $\frac{du}{dv} = \frac{du / dx}{dv / dx}$. Clearly

$\frac{du}{dx} = 2 \sin x \cos x$ and $\frac{dv}{dx} = e^{\cos x}(-\sin x) = -(\sin x)e^{\cos x}$

Thus

$$
\frac {d u}{d v} = \frac {2 \sin x \cos x}{- \sin x e ^ {\cos x}} = - \frac {2 \cos x}{e ^ {\cos x}}
$$

## Miscellaneous Exercise on Chapter 5

Differentiate w.r.t. $x$ the function in Exercises 1 to 11.

1. $(3x^{2} - 9x + 5)^{9}$

2. $\sin^3 x + \cos^6 x$

3. $(5x)^{3}\cos 2x$

4. $\sin^{-1}(x\sqrt{x}), 0 \leq x \leq 1$

5. $\frac{\cos^{-1}\frac{x}{2}}{\sqrt{2x + 7}}, - 2 <   x <   2$

6. $\cot^{-1}\left[\frac{\sqrt{1 + \sin x} + \sqrt{1 - \sin x}}{\sqrt{1 + \sin x} - \sqrt{1 - \sin x}}\right], 0 < x < \frac{\pi}{2}$

7.  $(\log x)^{\log x}, x > 1$

8. $\cos (a\cos x + b\sin x)$, for some constant $a$ and $b$.

9. $(\sin x - \cos x)^{(\sin x - \cos x)}, \frac{\pi}{4} < x < \frac{3\pi}{4}$

10. $x^{x} + x^{a} + a^{x} + a^{a}$, for some fixed $a > 0$ and $x > 0$

Reprint 2025-26

<!-- page 42 of 43 -->

CONTINUITY AND DIFFERENTIABILITY

145

11. $x^{x^2 -3} + (x - 3)^{x^2}$ , for $x > 3$

12. Find $\frac{dy}{dx}$, if $y = 12(1 - \cos t)$, $x = 10(t - \sin t)$, $-\frac{\pi}{2} < t < \frac{\pi}{2}$

13. Find $\frac{dy}{dx}$, if $y = \sin^{-1}x + \sin^{-1}\sqrt{1 - x^2}$, $0 < x < 1$

14. If $x\sqrt{1 + y} + y\sqrt{1 + x} = 0$, for, $-1 < x < 1$, prove that

$$
\frac {d y}{d x} = - \frac {1}{(1 + x) ^ {2}}
$$

15. If $(x - a)^2 + (y - b)^2 = c^2$, for some $c > 0$, prove that

$$
\left[ 1 + \left(\frac {d y}{d x}\right) ^ {2} \right] ^ {\frac {3}{2}}
$$

$$
\frac {d ^ {2} y}{d x ^ {2}}
$$

is a constant independent of $a$ and $b$.

16. If $\cos y = x\cos (a + y)$, with $\cos a \neq \pm 1$, prove that $\frac{dy}{dx} = \frac{\cos^2(a + y)}{\sin a}$.

17. If $x = a$ ($\cos t + t \sin t$) and $y = a$ ($\sin t - t \cos t$), find $\frac{d^2y}{dx^2}$.

18. If $f(x) = |x|^3$, show that $f''(x)$ exists for all real $x$ and find it.

19. Using the fact that  $\sin(A+B)=\sin A\cos B+\cos A\sin B$  and the differentiation, obtain the sum formula for cosines.

20. Does there exist a function which is continuous everywhere but not differentiable at exactly two points? Justify your answer.

21. If  $y=\begin{vmatrix}f(x)&g(x)&h(x)\\l&a&m&n\\a&b&c\end{vmatrix}$ , prove that  $\frac{dy}{dx}=\begin{vmatrix}f'(x)&g'(x)&h'(x)\\l&a&m&n\\a&b&c\end{vmatrix}$

22. If $y = e^{a\cos^{-1}x}, -1 \leq x \leq 1$, show that $(1 - x^2)\frac{d^2y}{dx^2} - x\frac{dy}{dx} - a^2y = 0$.

Reprint 2025-26

<!-- page 43 of 43 -->

146

MATHEMATICS

## Summary

A real valued function is continuous at a point in its domain if the limit of the function at that point equals the value of the function at that point. A function is continuous if it is continuous on the whole of its domain.

Sum, difference, product and quotient of continuous functions are continuous. i.e., if $f$ and $g$ are continuous functions, then

$(f \pm g)(x) = f(x) \pm g(x)$ is continuous.

$(f.g)(x) = f(x).g(x)$ is continuous.

$\left(\frac{f}{g}\right)(x) = \frac{f(x)}{g(x)}$ (wherever $g(x)\neq 0$) is continuous.

Every differentiable function is continuous, but the converse is not true.

Chain rule is rule to differentiate composites of functions. If $f = v$ or $u$, $t = u(x)$ and if both $\frac{dt}{dx}$ and $\frac{dv}{dt}$ exist then

$$
\frac {d f}{d x} = \frac {d v}{d t} \cdot \frac {d t}{d x}
$$

◆ Following are some of the standard derivatives (in appropriate domains):

$$
\frac {d}{d x} (\sin^ {- 1} x) = \frac {1}{\sqrt {1 - x ^ {2}}}
$$

$$
\frac {d}{d x} \left(\cos^ {- 1} x\right) = - \frac {1}{\sqrt {1 - x ^ {2}}}
$$

$$
\frac {d}{d x} \big (\tan^ {- 1} x \big) = \frac {1}{1 + x ^ {2}}
$$

$$
\frac {d}{d x} \left(e ^ {x}\right) = e ^ {x}
$$

$$
\frac {d}{d x} (\log x) = \frac {1}{x}
$$

Logarithmic differentiation is a powerful technique to differentiate functions of the form $f(x) = [u(x)]^{\nu (x)}$. Here both $f(x)$ and $u(x)$ need to be positive for this technique to make sense.

Reprint 2025-26