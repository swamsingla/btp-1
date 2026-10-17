# Factorisation of Algebraic Expressions

Factorisation is the process of breaking down an algebraic expression into smaller pieces, called factors, that multiply together to give the original expression. An algebraic identity is an algebraic equation that is true for all values of the variables occurring in it [S1]. Identities are useful tools for factorisation, because each one shows a pattern that expressions can be matched to [S1]. Once you know the common patterns, factorising becomes quicker and less a matter of guessing.

## Taking Out Common Factors

The most basic way to factorise an expression is by taking out the Highest Common Factor, or HCF. The HCF is the largest expression that divides evenly into every term. When you take out the HCF, you are reversing the distributive law of multiplication over addition.

To do this, look at all the terms in the expression and find the HCF of their numerical coefficients and of their variable parts. Then divide every term by this HCF and write the result inside brackets.

**Worked example**
Let us factorise the expression $6x^2 + 15x$. First, we look at the coefficients, $6$ and $15$. The HCF of $6$ and $15$ is $3$. Next, we look at the variables. Both terms contain $x$, and the lowest power of $x$ is $x^1$, or just $x$. So the HCF of the entire expression is $3x$.

Now we divide each term by $3x$:
$\frac{6x^2}{3x} = 2x$
$\frac{15x}{3x} = 5$

We then write the HCF outside the brackets and the remaining terms inside the brackets:
$6x^2 + 15x = 3x(2x + 5)$

## Grouping Terms

Sometimes an expression does not have a single factor that is common to all its terms. In such cases, we can group the terms into pairs and factorise each group separately. This method is called grouping.

To use this method, arrange the terms so that the first two terms have a common factor, and the last two terms also have a common factor. Then take out the HCF from each pair. If the expression inside the brackets is the same for both pairs, you can take it out as a common factor to get the final answer.

**Worked example**
Consider the expression $ax + ay + bx + by$. If we group the first two terms and the last two terms, we get:
$a(x + y) + b(x + y)$

Now we notice that $(x + y)$ is a common factor in both terms. We take it out:
$a(x + y) + b(x + y) = (x + y)(a + b)$

## Using Identities

Algebraic identities are equations that hold true for all values of the variables [S1]. You can use them to factorise expressions that fit their patterns, by writing the expanded form of the identity as its factorised form [S1].

The three identities used most for factorisation are:
1. $x^2 - y^2 = (x + y)(x - y)$ [S1]
2. $(x + y)^2 = x^2 + 2xy + y^2$ [S1]
3. $(x - y)^2 = x^2 - 2xy + y^2$ [S1]

To factorise with one of these, match the given expression with the expanded form in the identity, such as $x^2 - y^2$ or $x^2 + 2xy + y^2$. Once you identify the values of $x$ and $y$, you can write the factorised form directly.

**Worked example 1: difference of two squares**
Let us factorise $x^2 - 49$. This matches $x^2 - y^2$. Here $x^2$ is already a square, and $49 = 7^2$, so $y = 7$. Substituting into the identity, we get:
$x^2 - 49 = (x + 7)(x - 7)$

**Worked example 2: a perfect square with plus sign**
Let us factorise $x^2 + 10x + 25$. We see that $25 = 5^2$ and $10x = 2 \times x \times 5$. So the expression has the form $x^2 + 2xy + y^2$ with $y = 5$:
$x^2 + 10x + 25 = (x + 5)^2$

**Worked example 3: a perfect square with minus sign**
Let us factorise $4a^2 - 12a + 9$. We see that $4a^2 = (2a)^2$, $9 = 3^2$ and $12a = 2 \times 2a \times 3$. So the expression has the form $x^2 - 2xy + y^2$ with $x = 2a$ and $y = 3$:
$4a^2 - 12a + 9 = (2a - 3)^2$

## Factorising Trinomials

Some expressions have three terms, like $x^2 + 7x + 12$. To factorise these, you can use the identity $(x + a)(x + b) = x^2 + (a + b)x + ab$ [S1].

In this identity, the middle coefficient is the sum of $a$ and $b$, and the last term is the product of $a$ and $b$ [S1]. So to factorise, you look for two numbers whose sum is the middle coefficient and whose product is the last term.

**Worked example**
Let us factorise $x^2 + 7x + 12$. We need two numbers that add up to $7$ and multiply to $12$. The numbers $3$ and $4$ fit, since $3 + 4 = 7$ and $3 \times 4 = 12$.

So $a = 3$ and $b = 4$. Using the identity, we get:
$x^2 + 7x + 12 = (x + 3)(x + 4)$

You can check the answer by multiplying the brackets back: $(x + 3)(x + 4) = x^2 + 4x + 3x + 12 = x^2 + 7x + 12$.

## Key points
- Factorisation is the reverse of expansion: we break an expression down into its factors.
- The HCF is the largest factor common to all terms in an expression.
- Grouping terms is useful when there is no single common factor for the entire expression.
- Algebraic identities give a direct method for factorising expressions that fit their patterns [S1].
- The identity $x^2 - y^2 = (x + y)(x - y)$ is used for a difference of two squares [S1].

<!-- TERMS: factorisation, algebraic expressions, highest common factor, grouping terms, algebraic identities, trinomials -->
