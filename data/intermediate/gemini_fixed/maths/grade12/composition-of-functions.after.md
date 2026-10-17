# Composition of Functions

When we combine two machines, the output of the first becomes the input of the second. In mathematics, functions work exactly like these machines. The operation of feeding the output of one function directly into the input of another is called the composition of functions. This concept is fundamental because it allows us to build complex operations from simpler, more manageable pieces. Understanding how to combine functions is essential for solving advanced problems in algebra and calculus.

## The Definition of Composition

Let $f: \mathrm{A} \rightarrow \mathrm{B}$ and $g: \mathrm{B} \rightarrow \mathrm{C}$ be two functions. Then the composition of $f$ and $g$, denoted by gof, is defined as the function gof: $\mathrm{A} \rightarrow \mathrm{C}$ given by

$$
g o f (x) = g (f (x)), \forall x \in \mathrm{A}.
$$

[S1]

For this composition to make sense, the output of the first function must fit perfectly into the input of the second. This means the range of the first function must be a subset of the domain of the second function. If we try to reverse the order, we get a different result. The composition of $g$ and $f$, denoted by $f \circ g$, is defined as

$$
\left(f \circ g\right) (x) = f (g (x))
$$

[S2]

whenever the range of $g$ is a subset of domain of $f$. [S2]

It is important to note that the order of composition matters. In general, gof is not equal to fog.

## Composition of Discrete Functions

To see how composition works with specific values, consider the following example. Let $f:\{2,3,4,5\}\to\{3,4,5,9\}$ and $g:\{3,4,5,9\}\to\{7,11,15\}$ be functions defined as $f(2)=3$, $f(3)=4$, $f(4)=f(5)=5$ and $g(3)=g(4)=7$ and $g(5)=g(9)=11$. We want to find gof.

Solution We have $gof(2) = g(f(2)) = g(3) = 7$, $gof(3) = g(f(3)) = g(4) = 7$, $gof(4) = g(f(4)) = g(5) = 11$ and $gof(5) = g(5) = 11$.

[S1]

Notice how we first apply $f$ to the input $x$, and then we take that result and apply $g$ to it. This step-by-step process is the core of function composition.

## Composition of Real-Valued Functions

Composition is not limited to discrete sets; it also applies to continuous real functions. Let $f: \mathbf{R} \to \mathbf{R}$ and $g: \mathbf{R} \to \mathbf{R}$ be given by $f(x) = \cos x$ and $g(x) = 3x^2$. We can find gof and fog to see if they are equal.

Solution We have  $gof(x) = g(f(x)) = g(\cos x) = 3 (\cos x)^{2} = 3 \cos^{2} x$ . Similarly,  $fog(x) = f(g(x)) = f(3x^{2}) = \cos(3x^{2})$ . Note that  $3\cos^{2} x \neq \cos 3x^{2}$ , for x = 0. Hence,  $gof \neq fog$ .

[S1]

At $x = 0$, $gof(0) = 3 \cos^{2}(0) = 3(1) = 3$. However, $fog(0) = \cos(3(0)^{2}) = \cos(0) = 1$. Since $3 \neq 1$, the two compositions are indeed different. This illustrates that composition is not commutative.

## Invertible Functions

A function is called invertible if we can reverse the process. This means there exists another function that undoes the original one. Let $f \colon \mathrm{X} \to \mathrm{Y}$ be a function. This function is defined to be invertible, if there exists a function $g \colon \mathrm{Y} \to \mathrm{X}$ such that $gof = \mathrm{I}_{\mathrm{X}}$ and $fog = \mathrm{I}_{\mathrm{Y}}$. [S1] The function $g$ is called the inverse of $f$ and is denoted by $f^{-1}$.

[S1]

In other words, if we apply $f$ and then $f^{-1}$, we get back to our original input. Similarly, if we apply $f^{-1}$ and then $f$, we also get back to our original input.

## One-One and Onto Functions

For a function to be invertible, it must possess two specific properties: it must be one-one and onto. A function $f: X \to Y$ is defined to be one-one (or injective), if the images of distinct elements of $X$ under $f$ are distinct, i.e., for every $x_1, x_2 \in \mathrm{X}, f(x_1) = f(x_2)$ implies $x_1 = x_2$. [S3] Otherwise, $f$ is called many-one. [S3]

[S3]

A function $f: X \to Y$ is said to be onto (or surjective), if every element of $Y$ is the image of some element of $X$ under $f$, i.e., for every $y \in Y$, there exists an element $x$ in $X$ such that $f(x) = y$. [S3]

[S3]

## The Connection Between Invertibility and One-One/Onto

There is a direct relationship between a function being invertible and it being one-one and onto. Thus, if f is invertible, then f must be one-one and onto and conversely, if f is one-one and onto, then f must be invertible. [S1] This fact significantly helps for proving a function f to be invertible by showing that f is one-one and onto, specially when the actual inverse of f is not to be determined. [S1]

[S1]

This means we do not always need to find the exact formula for the inverse function to prove that it exists. We can simply check the one-one and onto properties.

## Worked Example

Consider two functions defined as $f(x) = 2x + 1$ and $g(x) = x^2 - 4$. Let us find the composition gof.

Solution We apply $f$ first. $gof(x) = g(f(x)) = g(2x + 1)$. Now we substitute $2x + 1$ into $g$ in place of $x$. This gives $g(2x + 1) = (2x + 1)^2 - 4$. Expanding the square, we get $4x^2 + 4x + 1 - 4 = 4x^2 + 4x - 3$.

## Key points

- The composition of $f$ and $g$, denoted gof, is defined as $g(f(x))$.
- The order of composition matters, as gof is generally not equal to fog.
- A function is invertible if there exists a function $g$ such that $gof = \mathrm{I}_{\mathrm{X}}$ and $fog = \mathrm{I}_{\mathrm{Y}}$.
- A function is invertible if and only if it is both one-one and onto.

<!-- TERMS: composition of functions, invertible functions, one-one, onto, bijective, range, domain, identity function, associativity -->
