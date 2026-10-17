# Inverse Trigonometric Functions

You have already studied the basic trigonometric functions, such as sine, cosine, and tangent. These functions take an angle as input and give you a ratio as output. Sometimes, you need to reverse this process. You might know the ratio and need to find the original angle. This is exactly what inverse trigonometric functions do. They are the inverses of the standard trigonometric functions, allowing you to find an angle when you know its sine, cosine, or tangent value.

## Principal Value Branches

To make inverse trigonometric functions well-defined, we work within the principal value branches of the corresponding inverse trigonometric functions [S1]. These results are valid within these principal value branches and wherever they are defined [S1]. Some results may not be valid for all values of the domains of inverse trigonometric functions; in fact, they will be valid only for some values of $x$ for which inverse trigonometric functions are defined [S1].

For the inverse sine function, denoted as $\sin^{-1} x$, the principal value branch corresponds to the interval $\left[ \frac{-\pi}{2}, \frac{\pi}{2} \right]$, where we have $\sin^{-1} (\sin x) = x$ [S1].

## Basic Definitions

The inverse trigonometric functions are defined by their relationship with the standard trigonometric functions. If $y = \sin^{-1} x$, then $x = \sin y$, and if $x = \sin y$, then $y = \sin^{-1} x$ [S1]. For suitable values of domain, similar results follow for the remaining trigonometric functions [S1].

This definition leads to two fundamental identities. The first is that applying the sine function to its inverse returns the original input. Specifically, $\sin \left( \sin^{-1} x \right) = x$, provided $x$ is in the domain $[-1, 1]$ [S1]. The second identity is that applying the inverse sine function to the sine of an angle returns the angle itself, but only if that angle is within the principal value branch. Thus, $\sin^{-1} (\sin x) = x$, provided $x \in \left[ \frac{-\pi}{2}, \frac{\pi}{2} \right]$ [S1].

## Properties and Identities

Working with inverse trigonometric functions involves using specific algebraic identities and substitutions. These identities are extremely useful for simplifying complex expressions.

Consider the substitution $x = \sin \theta$, which gives $\sin^{-1} x = \theta$ [S1]. We have:
$$
\sin^{-1} \left( 2x \sqrt{1 - x^2} \right) = \sin^{-1} \left( 2 \sin \theta \sqrt{1 - \sin^2 \theta} \right) = \sin^{-1} (2 \sin \theta \cos \theta) = \sin^{-1} (\sin 2\theta) = 2\theta = 2 \sin^{-1} x
$$
This identity is valid for $x$ in the range $\left[ -\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}} \right]$ [S1].

Similarly, if we use the substitution $x = \cos \theta$, we can derive another useful identity:
$$
\sin^{-1} \left( 2x \sqrt{1 - x^2} \right) = 2 \cos^{-1} x
$$
This version is valid for $x$ in the range $\left[ \frac{1}{\sqrt{2}}, 1 \right]$ [S1].

Another common technique is simplifying expressions involving $\tan^{-1}$ by using half-angle substitutions. For instance, the expression $\tan^{-1} \left( \frac{\cos x}{1 - \sin x} \right)$, where $x$ is in the range $\left( -\frac{3\pi}{2}, \frac{\pi}{2} \right)$, can be simplified by expressing the numerator and denominator in terms of $\frac{x}{2}$ [S1]. This yields:
$$
\tan^{-1} \left[ \frac{1 + \tan \frac{x}{2}}{1 - \tan \frac{x}{2}} \right] = \frac{\pi}{4} + \frac{x}{2}
$$
This demonstrates how algebraic manipulation combined with trigonometric identities can reduce a complex inverse trigonometric expression to a simple linear form [S1].

## Derivatives

The study of calculus introduces the concept of the derivative, which measures the rate of change of a function. The inverse trigonometric functions are continuous, and we can find their derivatives using the chain rule [S2].

To find the derivative of $f(x) = \sin^{-1} x$, we start by letting $y = \sin^{-1} x$. This implies $x = \sin y$ [S2]. Differentiating both sides with respect to $x$ gives:
$$
1 = \cos y \frac{dy}{dx}
$$
Solving for $\frac{dy}{dx}$ yields:
$$
\frac{dy}{dx} = \frac{1}{\cos y}
$$
Since $y = \sin^{-1} x$, we can rewrite this as $\frac{d}{dx} \left( \sin^{-1} x \right) = \frac{1}{\cos \left( \sin^{-1} x \right)}$ [S2].

This expression is only defined when $\cos y \neq 0$. This occurs when $\sin^{-1} x \neq -\frac{\pi}{2}$ and $\sin^{-1} x \neq \frac{\pi}{2}$, which corresponds to $x$ being in the open interval $(-1, 1)$ [S2].

To make this derivative more practical, we use the Pythagorean identity $\cos^2 y = 1 - \sin^2 y$. Substituting $x = \sin y$ gives $\cos^2 y = 1 - x^2$ [S2]. Since $y$ is restricted to $\left( -\frac{\pi}{2}, \frac{\pi}{2} \right)$, $\cos y$ is always positive, so $\cos y = \sqrt{1 - x^2}$ [S2].

Therefore, the derivative of the inverse sine function is:
$$
\frac{d}{dx} \left( \sin^{-1} x \right) = \frac{1}{\sqrt{1 - x^2}}
$$
for $x \in (-1, 1)$ [S2].

Similarly, we can find the derivatives of the inverse cosine and inverse tangent functions. The derivative of $\cos^{-1} x$ is $\frac{-1}{\sqrt{1 - x^2}}$ for $x \in (-1, 1)$, and the derivative of $\tan^{-1} x$ is $\frac{1}{1 + x^2}$ for $x \in \mathbb{R}$ [S2].

## Worked example

Let us apply the derivative rule for the inverse sine function to a specific problem. Suppose we want to find the derivative of $f(x) = \sin^{-1} (2x)$ with respect to $x$.

We use the chain rule. Let $u = 2x$. Then $f(x) = \sin^{-1} u$. The derivative of $\sin^{-1} u$ with respect to $u$ is $\frac{1}{\sqrt{1 - u^2}}$. The derivative of $u$ with respect to $x$ is $2$.

Applying the chain rule, we get:
$$
\frac{df}{dx} = \frac{d}{du} \left( \sin^{-1} u \right) \cdot \frac{du}{dx} = \frac{1}{\sqrt{1 - u^2}} \cdot 2 = \frac{2}{\sqrt{1 - (2x)^2}}
$$
Simplifying the denominator, we have:
$$
\frac{df}{dx} = \frac{2}{\sqrt{1 - 4x^2}}
$$
This derivative is valid as long as the denominator is not zero, which means $4x^2 < 1$, or $x \in \left( -\frac{1}{2}, \frac{1}{2} \right)$.

## Key points

*   Inverse trigonometric functions, such as $\sin^{-1} x$, $\cos^{-1} x$, and $\tan^{-1} x$, are used to find an angle when the trigonometric ratio is known.
*   Inverse trigonometric functions are defined within their principal value branches, where their properties and identities are valid [S1].
*   For $\sin^{-1} x$, the principal value branch is $\left[ \frac{-\pi}{2}, \frac{\pi}{2} \right]$ [S1].
*   The fundamental identity $\sin \left( \sin^{-1} x \right) = x$ holds true for $x \in [-1, 1]$ [S1].
*   The derivative of $\sin^{-1} x$ is $\frac{1}{\sqrt{1 - x^2}}$, defined for $x \in (-1, 1)$ [S2].
*   The derivative of $\cos^{-1} x$ is $\frac{-1}{\sqrt{1 - x^2}}$, defined for $x \in (-1, 1)$ [S2].
*   The derivative of $\tan^{-1} x$ is $\frac{1}{1 + x^2}$, defined for all real numbers $x \in \mathbb{R}$ [S2].
<!-- TERMS: inverse trigonometric functions, principal value branch, sin inverse, cos inverse, tan inverse, domain, range, chain rule, derivative, continuous functions, identity, Pythagorean identity, chain rule, differentiation -->
