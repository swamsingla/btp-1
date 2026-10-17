# Factorisation of Polynomials

Factorising a polynomial means writing it as a product of simpler polynomials, called its factors. On this page we use the Factor Theorem, and the method of splitting the middle term, to factorise polynomials of degree 2 and 3.

## The Factor Theorem

If $p(x)$ is a polynomial of degree $n \geq 1$ and $a$ is any real number, then (i) $x - a$ is a factor of $p(x)$ if $p(a) = 0$, and (ii) $p(a) = 0$ if $x - a$ is a factor of $p(x)$ [S1]. This is the Factor Theorem.

The proof uses the Remainder Theorem, by which $p(x) = (x - a)q(x) + p(a)$ [S1]. If $p(a) = 0$, then $p(x) = (x - a)q(x)$, which shows that $x - a$ is a factor of $p(x)$ [S1]. Conversely, if $x - a$ is a factor of $p(x)$, then $p(x) = (x - a)g(x)$ for some polynomial $g(x)$, and so $p(a) = (a - a)g(a) = 0$ [S1].

## Testing Whether a Linear Expression Is a Factor

To examine whether $x + 2$ is a factor of $x^3 + 3x^2 + 5x + 6$, note that the zero of $x + 2$ is $-2$ [S1]. Let $p(x) = x^3 + 3x^2 + 5x + 6$. Then $p(-2) = (-2)^3 + 3(-2)^2 + 5(-2) + 6 = -8 + 12 - 10 + 6 = 0$ [S1]. So, by the Factor Theorem, $x + 2$ is a factor of $x^3 + 3x^2 + 5x + 6$ [S1].

The same test works for $2x + 4$: with $s(x) = 2x + 4$ we get $s(-2) = 2(-2) + 4 = 0$, so $x + 2$ is a factor of $2x + 4$ [S1]. We can also see this without the Factor Theorem, since $2x + 4 = 2(x + 2)$ [S1].

## Finding the Value of a Constant

If $x - 1$ is a factor of $p(x) = 4x^3 + 3x^2 - 4x + k$, then $p(1) = 0$ [S1]. Now $p(1) = 4(1)^3 + 3(1)^2 - 4(1) + k = 4 + 3 - 4 + k$, and setting this equal to 0 gives $k = -3$ [S1].

## Splitting the Middle Term

A quadratic polynomial like $x^2 + lx + m$ can be factorised by splitting the middle term $lx$ as $ax + bx$ so that $ab = m$. Then $x^2 + lx + m = (x + a)(x + b)$ [S1]. We now factorise quadratic polynomials of the type $ax^2 + bx + c$, where $a \neq 0$ and $a$, $b$, $c$ are constants [S1].

Let the factors be $(px + q)$ and $(rx + s)$. Then $ax^2 + bx + c = (px + q)(rx + s) = prx^2 + (ps + qr)x + qs$ [S1]. Comparing the coefficients of $x^2$ gives $a = pr$, comparing the coefficients of $x$ gives $b = ps + qr$, and comparing the constant terms gives $c = qs$ [S1]. So $b$ is the sum of two numbers $ps$ and $qr$ whose product is $(ps)(qr) = (pr)(qs) = ac$ [S1]. Therefore, to factorise $ax^2 + bx + c$, we write $b$ as the sum of two numbers whose product is $ac$ [S1].

For example, to factorise $6x^2 + 17x + 5$ by splitting the middle term, we look for two numbers whose sum is 17 and whose product is $6 \times 5 = 30$ [S1]. Some pairs of factors of 30 are 1 and 30, 2 and 15, 3 and 10, 5 and 6. Of these, 2 and 15 give the sum 17 [S1]. So $6x^2 + 17x + 5 = 6x^2 + 2x + 15x + 5 = 2x(3x + 1) + 5(3x + 1) = (3x + 1)(2x + 5)$ [S1].

The Factor Theorem gives the same answer. Write $6x^2 + 17x + 5 = 6\left(x^2 + \frac{17}{6}x + \frac{5}{6}\right) = 6p(x)$, say. If $a$ and $b$ are the zeroes of $p(x)$, then $6x^2 + 17x + 5 = 6(x - a)(x - b)$ and $ab = \frac{5}{6}$ [S1]. By trial, $p\left(-\frac{1}{3}\right) = 0$, so $x + \frac{1}{3}$ is a factor of $p(x)$, and similarly $x + \frac{5}{2}$ is a factor of $p(x)$ [S1]. Therefore $6x^2 + 17x + 5 = 6\left(x + \frac{1}{3}\right)\left(x + \frac{5}{2}\right) = 6\left(\frac{3x + 1}{3}\right)\left(\frac{2x + 5}{2}\right) = (3x + 1)(2x + 5)$ [S1]. For this example the splitting method appears more efficient [S1].

## Using the Factor Theorem for a Quadratic

Now factorise $y^2 - 5y + 6$ by using the Factor Theorem. Let $p(y) = y^2 - 5y + 6$. If $p(y) = (y - a)(y - b)$, the constant term is $ab$, so $ab = 6$, and we look at the factors of 6 [S1]. We find $p(2) = 2^2 - (5 \times 2) + 6 = 0$, so $y - 2$ is a factor of $p(y)$ [S1]. Also $p(3) = 3^2 - (5 \times 3) + 6 = 0$, so $y - 3$ is also a factor [S1]. Therefore $y^2 - 5y + 6 = (y - 2)(y - 3)$ [S1]. This polynomial can also be factorised by splitting the middle term $-5y$ [S1].

## Factorising Cubic Polynomials

For cubic polynomials, the splitting method is not appropriate to start with, and we need to find at least one factor first [S1].

Consider $p(x) = x^3 - 23x^2 + 142x - 120$. We look for the factors of $-120$, such as $\pm 1, \pm 2, \pm 3, \pm 4, \pm 5, \pm 6, \pm 8, \pm 10, \pm 12, \pm 15, \pm 20, \pm 24, \pm 30, \pm 60$ [S1]. By trial, $p(1) = 1 - 23 + 142 - 120 = 0$, so $x - 1$ is a factor of $p(x)$ [S1]. Then $x^3 - 23x^2 + 142x - 120 = x^3 - x^2 - 22x^2 + 22x + 120x - 120 = x^2(x - 1) - 22x(x - 1) + 120(x - 1) = (x - 1)(x^2 - 22x + 120)$, taking $(x - 1)$ common [S1]. We could also have got this by dividing $p(x)$ by $x - 1$ [S1].

The quadratic $x^2 - 22x + 120$ can be factorised by splitting the middle term or by using the Factor Theorem [S1]. By splitting the middle term, $x^2 - 22x + 120 = x^2 - 12x - 10x + 120 = x(x - 12) - 10(x - 12) = (x - 12)(x - 10)$ [S1]. Therefore $x^3 - 23x^2 + 142x - 120 = (x - 1)(x - 10)(x - 12)$ [S1].

## Worked Example

Factorise $x^3 - 2x^2 - 5x + 6$. The factors of the constant term 6 are $\pm 1, \pm 2, \pm 3, \pm 6$. Let $p(x) = x^3 - 2x^2 - 5x + 6$. Trying $x = 1$ gives $p(1) = 1 - 2 - 5 + 6 = 0$, so by the Factor Theorem $x - 1$ is a factor [S1]. Dividing by $x - 1$, we get $x^3 - 2x^2 - 5x + 6 = (x - 1)(x^2 - x - 6)$.

To factorise $x^2 - x - 6$ by splitting the middle term, we need two numbers whose sum is $-1$ and whose product is $-6$. These are $-3$ and $2$. So $x^2 - x - 6 = x^2 + 2x - 3x - 6 = x(x + 2) - 3(x + 2) = (x - 3)(x + 2)$. The complete factorisation is $x^3 - 2x^2 - 5x + 6 = (x - 1)(x - 3)(x + 2)$.

## Key points

*   If $p(x)$ has degree $n \geq 1$, then $x - a$ is a factor of $p(x)$ if and only if $p(a) = 0$ [S1].
*   The Factor Theorem can be used to find an unknown constant in a polynomial when a linear factor is given [S1].
*   To factorise $ax^2 + bx + c$ by splitting the middle term, write $b$ as the sum of two numbers whose product is $ac$ [S1].
*   The Factor Theorem can also be used to factorise quadratic polynomials, by finding their zeroes [S1].
*   For a cubic polynomial, the splitting method is not appropriate to start with, so we first find one factor and then factorise the remaining quadratic [S1].

<!-- TERMS: polynomial, factor, zero, Factor Theorem, Remainder Theorem, middle term, cubic polynomial, quadratic polynomial, constant term -->
