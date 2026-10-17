# Factor Theorem

A zero of a polynomial is a number $c$ such that $p(c) = 0$ [S2]. For example, the zero of the polynomial $x - 1$ is 1 because $p(1) = 1 - 1 = 0$ [S2]. The Factor Theorem gives a direct link between these zeroes and the factors of a polynomial. If $p(x)$ is a polynomial and $a$ is any real number, then $x - a$ is a factor of $p(x)$ if and only if $p(a) = 0$ [S1]. This means we can test whether $x - a$ is a factor of $p(x)$ by checking whether $p(a) = 0$.

## The Theorem Stated

The Factor Theorem connects the zeroes of a polynomial to its factors. It states that for a polynomial $p(x)$ of degree $n \geq 1$ and a real number $a$, $x - a$ is a factor of $p(x)$ if $p(a) = 0$, and $p(a) = 0$ if $x - a$ is a factor of $p(x)$ [S1]. This works both ways. If $p(a) = 0$ for some value of $a$, then $x - a$ is a factor of $p(x)$.

## Using the Remainder Theorem

The Factor Theorem is proven using the Remainder Theorem. The Remainder Theorem tells us that $p(x) = (x - a)q(x) + p(a)$ [S1]. If $p(a) = 0$, then the equation becomes $p(x) = (x - a)q(x)$. This shows that $x - a$ is a factor of $p(x)$ [S1]. Conversely, if $x - a$ is a factor of $p(x)$, then $p(x) = (x - a)g(x)$ for some polynomial $g(x)$ [S1]. If we substitute $x = a$ into this equation, we get $p(a) = (a - a)g(a) = 0 \times g(a) = 0$ [S1].

## Finding Zeroes

To use the Factor Theorem, we need the zeroes of the polynomial. A zero of a polynomial $p(x)$ is a number $c$ such that $p(c) = 0$ [S2]. For a linear polynomial, there is exactly one zero [S2]. However, a polynomial can have more than one zero [S2]. For example, the polynomial $x^2 - 2x$ has zeroes at 2 and 0 because $p(2) = 2^2 - 2 \times 2 = 0$ and $p(0) = 0^2 - 2 \times 0 = 0$ [S2].

## Checking if a Linear Term is a Factor

The Factor Theorem can be used to check whether a linear expression is a factor of a polynomial. For example, to check if $x + 2$ is a factor of $x^3 + 3x^2 + 5x + 6$, we find the zero of $x + 2$, which is -2 [S1]. Let $p(x) = x^3 + 3x^2 + 5x + 6$. Then, $p(-2) = (-2)^3 + 3(-2)^2 + 5(-2) + 6 = -8 + 12 - 10 + 6 = 0$ [S1]. Since $p(-2) = 0$, by the Factor Theorem, $x + 2$ is a factor of $x^3 + 3x^2 + 5x + 6$ [S1].

## Finding the Value of a Constant

The Factor Theorem can also be used to find the value of a constant in a polynomial. For example, if $x - 1$ is a factor of $p(x) = 4x^3 + 3x^2 - 4x + k$, then $p(1) = 0$ [S1]. Now, $p(1) = 4(1)^3 + 3(1)^2 - 4(1) + k = 4 + 3 - 4 + k = 0$, which gives $k = -3$ [S1].

## Factoring Quadratic Polynomials

The Factor Theorem can be used to factorise quadratic polynomials. For example, to factorise $y^2 - 5y + 6$, we let $p(y) = y^2 - 5y + 6$ [S1]. If $p(y) = (y - a)(y - b)$, the constant term is $ab$, so $ab = 6$ and we look at the factors of 6 [S1]. We find that $p(2) = 2^2 - 5(2) + 6 = 4 - 10 + 6 = 0$, so $y - 2$ is a factor of $p(y)$ [S1]. Also, $p(3) = 3^2 - 5(3) + 6 = 9 - 15 + 6 = 0$, so $y - 3$ is also a factor of $y^2 - 5y + 6$ [S1]. Therefore, $y^2 - 5y + 6 = (y - 2)(y - 3)$ [S1].

## Factoring Cubic Polynomials

For cubic polynomials, the splitting method is not appropriate to start with, so we need to find at least one factor first [S1]. For example, to factorise $x^3 - 23x^2 + 142x - 120$, we let $p(x) = x^3 - 23x^2 + 142x - 120$ [S1]. We look for factors of -120 and try them by trial [S1]. We find that $p(1) = 1^3 - 23(1)^2 + 142(1) - 120 = 1 - 23 + 142 - 120 = 0$ [S1]. So, $x - 1$ is a factor of $p(x)$ [S1].

Now we can write $p(x) = (x - 1)(x^2 - 22x + 120)$ [S1]. We can factorise the quadratic part by splitting the middle term or by using the Factor Theorem again [S1]. By splitting the middle term, we get $x^2 - 22x + 120 = x^2 - 12x - 10x + 120 = x(x - 12) - 10(x - 12) = (x - 10)(x - 12)$ [S1]. Therefore, $x^3 - 23x^2 + 142x - 120 = (x - 1)(x - 10)(x - 12)$ [S1].

## Worked example

Let us apply the Factor Theorem to a new polynomial. Consider $p(x) = x^2 - 7x + 12$. We want to check if $x - 3$ is a factor of $p(x)$. The zero of $x - 3$ is 3. We evaluate $p(3) = 3^2 - 7(3) + 12 = 9 - 21 + 12 = 0$. Since $p(3) = 0$, by the Factor Theorem, $x - 3$ is a factor of $p(x)$ [S1]. Dividing $p(x)$ by $x - 3$ gives the other factor $x - 4$, so $x^2 - 7x + 12 = (x - 3)(x - 4)$.

## Key points

- A zero of a polynomial $p(x)$ is a number $c$ such that $p(c) = 0$ [S2].
- If $p(a) = 0$, then $x - a$ is a factor of $p(x)$ [S1].
- If $x - a$ is a factor of $p(x)$, then $p(a) = 0$ [S1].
- The Factor Theorem is proved using the Remainder Theorem, by which $p(x) = (x - a)q(x) + p(a)$ [S1].
- The Factor Theorem can be used to factorise quadratic and cubic polynomials by finding their zeroes [S1].

<!-- TERMS: zero of a polynomial, factor, Factor Theorem, Remainder Theorem, polynomial equation, root, linear polynomial, quadratic polynomial, cubic polynomial -->