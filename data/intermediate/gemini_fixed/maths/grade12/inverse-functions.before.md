# Inverse Functions

An inverse function is a special operation that undoes the action of a given function. If a function $f$ takes an input $x$ and produces an output $y$, then its inverse $f^{-1}$ takes $y$ and returns the original $x$. This concept is fundamental in mathematics because it allows us to solve equations and understand the symmetry of mathematical relationships. For a function to have an inverse, it must possess two crucial properties: it must be one-one, meaning distinct inputs always produce distinct outputs, and it must be onto, meaning every element in the target set is covered by the function's output [S3].

## The Bijective Requirement

The existence of an inverse function is strictly tied to the concept of a bijective function. A function is bijective if and only if it is both one-one and onto [S3]. If a function fails to be one-one, it is called many-one, and if it fails to be onto, there are elements in the codomain that are never reached. 

Consider the function $f: \mathbf{R} \to \mathbf{R}$ defined by $f(x) = x^2$. This function is not one-one because $f(-1) = 1 = f(1)$. Because it is not one-one, it cannot have a true inverse over the real numbers. To see why, imagine trying to reverse the process: if you are given the number $1$ as an input to the inverse, you would not know whether to return $-1$ or $1$. Since the inverse would not be a function—it would map one input to multiple outputs—it does not exist in the standard sense [S3].

## Finding the Inverse

To find the inverse of a bijective function, we follow a straightforward algebraic process. We start by writing the function as $y = f(x)$. Then, we swap the roles of $x$ and $y$ to get $x = f(y)$. Finally, we solve this new equation for $y$ to find the expression for $f^{-1}(x)$ [S3].

For example, let's find the inverse of the linear function $f(x) = 2x + 3$. First, we write $y = 2x + 3$. Next, we swap $x$ and $y$ to get $x = 2y + 3$. Solving for $y$, we subtract $3$ from both sides to get $x - 3 = 2y$, and then divide by $2$ to find $y = \frac{x - 3}{2}$. Therefore, the inverse function is $f^{-1}(x) = \frac{x - 3}{2}$ [S3].

## Domain and Range

When finding an inverse function, the domain and range of the original function are swapped. The domain of the original function $f$ becomes the range of the inverse function $f^{-1}$, and the range of $f$ becomes the domain of $f^{-1}$ [S3].

Let's look at another example. Suppose we have the function $f(x) = 2x + 3$, where the domain is all real numbers $\mathbf{R}$. The range of this function is also all real numbers $\mathbf{R}$, because as $x$ varies over all real numbers, $2x + 3$ will also vary over all real numbers. When we find the inverse function $f^{-1}(x) = \frac{x - 3}{2}$, its domain is also all real numbers $\mathbf{R}$, and its range is all real numbers $\mathbf{R}$. This is because the input $x$ in $f^{-1}$ can be any real number, and the output $y$ will also be any real number.

## Worked Example

Let's find the inverse of the function $f(x) = 4x - 7$. First, we write $y = 4x - 7$. Next, we swap $x$ and $y$ to get $x = 4y - 7$. Solving for $y$, we add $7$ to both sides to get $x + 7 = 4y$, and then divide by $4$ to find $y = \frac{x + 7}{4}$. Therefore, the inverse function is $f^{-1}(x) = \frac{x + 7}{4}$.

To check our answer, we can compose the functions. We know that $f(f^{-1}(x)) = x$. Substituting $f^{-1}(x)$ into $f$, we get $f\left(\frac{x + 7}{4}\right) = 4\left(\frac{x + 7}{4}\right) - 7 = x + 7 - 7 = x$. This confirms that our inverse function is correct.

## Key points

- An inverse function $f^{-1}$ exists if and only if the original function $f$ is bijective, meaning it is both one-one and onto [S3].
- To find the inverse, write $y = f(x)$, swap $x$ and $y$, and solve for $y$ [S3].
- The domain of the original function becomes the range of the inverse, and the range of the original function becomes the domain of the inverse [S3].
- If a function is not one-one, such as $f(x) = x^2$, it does not have an inverse because the reverse operation is not unique [S3].
- The composition of a function and its inverse yields the identity function, i.e., $f(f^{-1}(x)) = x$ [S3].

<!-- TERMS: inverse function, bijective function, one-one, onto, domain, range, codomain, many-one -->