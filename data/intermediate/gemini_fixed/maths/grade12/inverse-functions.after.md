# Inverse Functions

In mathematics, we study different types of functions, such as one-one and onto functions [S3]. For certain functions, we can define inverse functions, such as inverse trigonometric functions [S1]. For example, if $y = \sin^{-1}x$, then $x = \sin y$, and if $x = \sin y$, then $y = \sin^{-1}x$ [S1]. These inverse trigonometric functions are continuous functions [S2].

## The Bijective Requirement

The existence of an inverse function is strictly tied to the concept of a bijective function. A function $f: X \to Y$ is said to be bijective if it is both one-one and onto [S3]. 

A function $f: X \to Y$ is defined to be one-one (or injective) if the images of distinct elements of $X$ under $f$ are distinct, i.e., for every $x_1, x_2 \in X$, $f(x_1) = f(x_2)$ implies $x_1 = x_2$; otherwise, $f$ is called many-one [S3]. A function $f: X \to Y$ is said to be onto (or surjective) if every element of $Y$ is the image of some element of $X$ under $f$, which is true if and only if the range of $f = Y$ [S3]. If a function has $f(-1) = 1 = f(1)$, then it is not one-one [S3]. Furthermore, if an element like $-2$ in the co-domain $\mathbf{R}$ is not the image of any element $x$ in the domain $\mathbf{R}$, then the function is not onto [S3].

## Finding the Inverse

For inverse trigonometric functions, we can find the relationship between the function and its inverse. For example, if we have $y = \sin^{-1}x$, we can write this as $x = \sin y$, and vice versa [S1, S2]. This relationship is equivalent to:

$$
\sin \left(\sin^{-1} x\right) = x, x \in [-1, 1] \quad \text{and} \quad \sin^{-1} (\sin x) = x, x \in \left[-\frac{\pi}{2}, \frac{\pi}{2}\right]
$$

[S1]

For suitable values of the domain, similar results follow for the remaining trigonometric functions [S1].

## Domain and Range

The domains of inverse trigonometric functions are restricted to specific intervals where they are defined [S1]. Some properties of these functions are valid only within the principal value branches of the corresponding inverse trigonometric functions and wherever they are defined [S1]. 

Additionally, the domains of the derivatives of these functions are specified. For instance, the derivative of $f(x) = \sin^{-1}x$ is given by $f'(x) = \frac{1}{\sqrt{1-x^2}}$ for the domain $x \in (-1, 1)$ [S2]. The domains and derivatives of several inverse trigonometric functions are summarized below [S2]:

| $f(x)$ | $\sin^{-1} x$ | $\cos^{-1} x$ | $\tan^{-1} x$ |
| --- | --- | --- | --- |
| $f'(x)$ | $\frac{1}{\sqrt{1-x^{2}}}$ | $\frac{-1}{\sqrt{1-x^{2}}}$ | $\frac{1}{1+x^{2}}$ |
| Domain of $f$ | (-1, 1) | (-1, 1) | $\mathbf{R}$ |

## Worked Example

Let us write the expression $\cot^{-1}\left(\frac{1}{\sqrt{x^2 - 1}}\right)$ for $x > 1$ in its simplest form [S1].

To simplify this expression, we can let $x = \sec \theta$ [S1]. Using trigonometric identities, we have:

$$
\sqrt{x^2 - 1} = \sqrt{\sec^2\theta - 1} = \tan \theta
$$

[S1]

Substituting this back into our original expression, we get:

$$
\cot^{-1}\frac{1}{\sqrt{x^2 - 1}} = \cot^{-1}\left(\frac{1}{\tan \theta}\right) = \cot^{-1}(\cot \theta) = \theta
$$

[S1]

Since we defined $x = \sec \theta$, we can write $\theta = \sec^{-1}x$ [S1]. Therefore, the simplest form of the expression is:

$$
\sec^{-1}x
$$

[S1]

## Key points

- A function is bijective if and only if it is both one-one (injective) and onto (surjective) [S3].
- For the inverse sine function, the relation $y = \sin^{-1}x$ is equivalent to $x = \sin y$, which yields $\sin(\sin^{-1}x) = x$ for $x \in [-1, 1]$ and $\sin^{-1}(\sin x) = x$ for $x \in [-\frac{\pi}{2}, \frac{\pi}{2}]$ [S1].
- Inverse trigonometric functions are continuous, and their derivatives are defined on specific domains, such as $(-1, 1)$ for the derivative of $\sin^{-1}x$ and $\cos^{-1}x$, and $\mathbf{R}$ for the derivative of $\tan^{-1}x$ [S2].
- Expressions involving inverse trigonometric functions can be simplified using trigonometric substitutions, such as simplifying $\cot^{-1}\left(\frac{1}{\sqrt{x^2 - 1}}\right)$ for $x > 1$ to $\sec^{-1}x$ [S1].

<!-- TERMS: inverse function, bijective function, one-one, onto, domain, range, codomain, many-one -->
