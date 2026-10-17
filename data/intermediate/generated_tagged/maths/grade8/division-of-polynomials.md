# Division of Algebraic Expressions

Algebraic expressions can be added, subtracted, multiplied and divided. Dividing one algebraic expression by another means finding the expression that, when multiplied by the divisor, gives the dividend back. This skill helps us simplify expressions and solve equations more easily. In this page, the divisor is never zero.

## Dividing a Polynomial by a Monomial

To divide a polynomial by a monomial, divide each term of the polynomial by the monomial separately, and then add the results.

For example, to divide $12x^3 - 6x^2$ by $3x$, divide $12x^3$ by $3x$ to get $4x^2$, and divide $-6x^2$ by $3x$ to get $-2x$. The result is $4x^2 - 2x$.

You can check the answer by multiplying it by the divisor: $3x \times (4x^2 - 2x) = 12x^3 - 6x^2$, which is the original polynomial.

## Dividing a Polynomial by Another Polynomial

When the divisor has more than one term, you can use the long division method, which is very similar to the long division you learned with numbers. First write both polynomials with their terms in decreasing powers of $x$. Then repeat these steps: divide the first term of the dividend by the first term of the divisor, multiply the result by the divisor, and subtract it from the dividend. Continue with what is left until the remainder is $0$ or has a lower power of $x$ than the divisor.

For instance, let us divide $x^2 + 5x + 6$ by $x + 2$.
- Divide $x^2$ by $x$ to get $x$.
- Multiply $x$ by $x + 2$ to get $x^2 + 2x$. Subtracting this from the dividend leaves $3x + 6$.
- Divide $3x$ by $x$ to get $3$.
- Multiply $3$ by $x + 2$ to get $3x + 6$. Subtracting leaves a remainder of $0$.

So the quotient is $x + 3$ and the remainder is $0$.

Sometimes the remainder is not zero. Let us divide $x^2 + 3x + 5$ by $x + 1$. Divide $x^2$ by $x$ to get $x$, then $x \times (x + 1) = x^2 + x$, and subtracting leaves $2x + 5$. Divide $2x$ by $x$ to get $2$, then $2 \times (x + 1) = 2x + 2$, and subtracting leaves $3$. The quotient is $x + 2$ and the remainder is $3$. The remainder $3$ has no $x$ in it, so we cannot divide any further.

To check a division, use this relation:
$$ \text{dividend} = \text{divisor} \times \text{quotient} + \text{remainder} $$
Here $(x + 1)(x + 2) + 3 = x^2 + 3x + 2 + 3 = x^2 + 3x + 5$, which is the dividend.

## Using Identities to Divide

Sometimes division is easier if you factorise the dividend first. You can use algebraic identities to do this. For example, the identity $x^2 - y^2 = (x + y)(x - y)$ is useful for a difference of two squares [S1].

Let us divide $x^2 - 9$ by $x + 3$. Since $9 = 3^2$, the identity gives $x^2 - 9 = (x + 3)(x - 3)$. Then
$$ \frac{x^2 - 9}{x + 3} = \frac{(x + 3)(x - 3)}{x + 3} = x - 3 $$
The common factor $x + 3$ cancels, so the quotient is $x - 3$.

The identity $(x + y)^2 = x^2 + 2xy + y^2$ [S1] works in the same way. Since $x^2 + 10x + 25 = (x + 5)^2$, dividing $x^2 + 10x + 25$ by $x + 5$ gives $x + 5$.

## Worked Example

Let us divide $10x^2 - 5x$ by $5x$.

First, split the polynomial into two terms: $\frac{10x^2}{5x}$ and $\frac{-5x}{5x}$.

Next, divide the first term: $\frac{10x^2}{5x} = 2x$.

Then, divide the second term: $\frac{-5x}{5x} = -1$.

Combine the results to get the final answer: $2x - 1$.

Check: $5x \times (2x - 1) = 10x^2 - 5x$, which is the original polynomial.

## Key points

*   To divide a polynomial by a monomial, divide each term of the polynomial by the monomial.
*   To divide a polynomial by another polynomial, use the long division method.
*   Factorising using algebraic identities can simplify the division process [S1].
*   Always check your answer: dividend = divisor × quotient + remainder.
*   This topic builds on the factorisation of algebraic expressions, which uses algebraic identities [S1].

<!-- TERMS: polynomial, monomial, binomial, factorisation, algebraic identity, dividend, divisor, quotient, remainder, long division -->
