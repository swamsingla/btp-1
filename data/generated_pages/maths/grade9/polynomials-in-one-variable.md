---
{
  "concept": "Polynomials in One Variable",
  "slug": "polynomials-in-one-variable",
  "grade": 9,
  "language": "en",
  "subject": "maths",
  "area": "Algebra",
  "hand_edited": "2026-10-17: held because the generated page had no citation tags (0 of 9 paragraphs cited), no key points and no worked example; its S3 source was a Chapter 4 passage on linear equations, unrelated to the page. The generated text was accurate but untraceable. Rewritten by hand from Section 2.2 with tags, adding linear polynomials, p(x) notation, the Example 1 degrees as the worked example, and key points. Unsupported lines removed: 'an algebraic expression is formed when we combine variables, constants and operations', and 'a term is each part separated by a plus or minus sign'.",
  "model": "sarvam-105b",
  "settings": {
    "temperature": 0.3,
    "max_tokens": 8000,
    "reasoning_effort": "none"
  },
  "usage": {
    "completion_tokens": 1298,
    "prompt_tokens": 6633,
    "total_tokens": 7931,
    "completion_tokens_details": {
      "accepted_prediction_tokens": null,
      "audio_tokens": null,
      "reasoning_tokens": 0,
      "rejected_prediction_tokens": null
    },
    "prompt_tokens_details": null
  },
  "target_words": [
    1000,
    1350
  ],
  "generated_at": "2026-10-17T04:58:27",
  "source_grade": 9,
  "grade_delta": 0,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g9_maths_chapter2_004",
      "chapter": "chapter2",
      "section": "2.2 Polynomials in One Variable"
    }
  ],
  "citation_check": {
    "cited": [
      "1"
    ],
    "invented_citations": [],
    "unused_sources": [],
    "explanatory_paragraphs_without_a_citation": 0,
    "words": 1067,
    "target_words": [
      1000,
      1350
    ],
    "untraceable_sections": 0,
    "ok": true,
    "structural_problems": []
  },
  "terms": [
    "variable",
    "constant",
    "polynomial",
    "term",
    "coefficient",
    "monomial",
    "binomial",
    "trinomial",
    "degree",
    "linear polynomial",
    "quadratic polynomial",
    "cubic polynomial",
    "constant polynomial",
    "zero polynomial"
  ]
}
---

# Polynomials in One Variable

A variable is denoted by a symbol that can take any real value, and we use letters such as $x$, $y$ and $z$ to denote variables. Expressions like $2x$, $3x$, $-x$ and $-\frac{1}{2}x$ are all of the form (a constant) $\times$ $x$. If we do not know what the constant is, we write it as $a$, $b$, $c$ and so on, so the expression will be $ax$, say. The values of constants remain the same throughout a particular situation, but the value of a variable can keep changing.

Consider a square of side $x$ units. Its perimeter is $4x$ units, so as the length of the side varies, the perimeter varies. Its area is $x \times x = x^2$ square units. Expressions such as $2x$, $x^2 + 2x$ and $x^3 - x^2 + 4x + 7$ have only whole numbers as the exponents of the variable, and expressions of this form are called polynomials in one variable.

## Definition and Terms

In the polynomial $x^3 - x^2 + 4x + 7$ the variable is $x$, so it is a polynomial in $x$. Similarly, $3y^2 + 5y$ is a polynomial in the variable $y$, and $t^2 + 4$ is a polynomial in the variable $t$. If the variable is $x$, we may denote the polynomial by $p(x)$, $q(x)$, $r(x)$ and so on, for example $p(x) = 2x^2 + 5x - 3$ and $q(x) = x^3 - 1$.

In the polynomial $x^2 + 2x$, the expressions $x^2$ and $2x$ are called the terms of the polynomial. The polynomial $3y^2 + 5y + 7$ has three terms, namely $3y^2$, $5y$ and $7$.

Each term of a polynomial has a coefficient. In $-x^3 + 4x^2 + 7x - 2$, the coefficient of $x^3$ is $-1$, the coefficient of $x^2$ is 4, the coefficient of $x$ is 7, and $-2$ is the coefficient of $x^0$, because $x^0 = 1$. In $x^2 - x + 7$, the coefficient of $x$ is $-1$.

## Types of Polynomials

A polynomial can have any finite number of terms. For instance, $x^{150} + x^{149} + \ldots + x^2 + x + 1$ is a polynomial with 151 terms. Polynomials are named by their number of terms:

*   A polynomial with only one term is called a monomial ("mono" means "one"). Examples are $2x$, $2$, $5x^3$, $-5x^2$, $y$ and $u^4$.
*   A polynomial with only two terms is called a binomial ("bi" means "two"). Examples are $x + 1$, $x^2 - x$, $y^9 + 1$ and $u^{15} - u^2$.
*   A polynomial with only three terms is called a trinomial ("tri" means "three"). Examples are $x + x^2 + \pi$, $u + u^2 - 2$, $\sqrt{2} + x - x^2$ and $y^4 + y + 5$.

## Degree of a Polynomial

The highest power of the variable in a polynomial is called the degree of the polynomial. In $p(x) = 3x^7 - 4x^6 + x + 9$ the term with the highest power of $x$ is $3x^7$, so the degree is 7. In $q(y) = 5y^6 - 4y^2 - 6$ the term with the highest power of $y$ is $5y^6$, so the degree is 6. The degree of a non-zero constant polynomial is zero.

A polynomial of degree one is called a linear polynomial, for example $4x + 5$, $2y$ and $3 - u$. A linear polynomial in $x$ can have at most two terms, and it is of the form $ax + b$, where $a$ and $b$ are constants and $a \neq 0$.

A polynomial of degree two is called a quadratic polynomial, for example $5 - y^2$, $4y + 5y^2$ and $6 - y - y^2$. A quadratic polynomial in $x$ has at most 3 terms, and it is of the form $ax^2 + bx + c$, where $a \neq 0$ and $a$, $b$, $c$ are constants.

A polynomial of degree three is called a cubic polynomial, for example $4x^3$, $2x^3 + 1$ and $2x^3 + 4x^2 + 6x + 7$. A cubic polynomial in one variable can have at most 4 terms, and it is of the form $ax^3 + bx^2 + cx + d$, where $a \neq 0$ and $a$, $b$, $c$, $d$ are constants.

## Constant and Zero Polynomials

The numbers 2, $-5$, 7 and so on are examples of constant polynomials. The constant polynomial 0 is called the zero polynomial. The degree of the zero polynomial is not defined.

## Expressions That Are Not Polynomials

Not every algebraic expression is a polynomial. We can write $x + \frac{1}{x} = x + x^{-1}$, and the exponent of the second term, $-1$, is not a whole number, so this expression is not a polynomial. Again, $\sqrt{x} + 3$ can be written as $x^{\frac{1}{2}} + 3$, where the exponent of $x$ is $\frac{1}{2}$, which is not a whole number, so it is not a polynomial either.

## General Form

A polynomial in one variable $x$ of degree $n$ is an expression of the form $a_n x^n + a_{n-1} x^{n-1} + \dots + a_1 x + a_0$, where $a_0, a_1, a_2, \ldots, a_n$ are constants and $a_n \neq 0$. If all the constants $a_0, a_1, \ldots, a_n$ are zero, we get the zero polynomial, which is denoted by 0.

## Worked Example

Find the degree of each of the polynomials $x^5 - x^4 + 3$, $2 - y^2 - y^3 + 2y^8$ and $2$.

*   In $x^5 - x^4 + 3$ the highest power of the variable is 5, so the degree is 5.
*   In $2 - y^2 - y^3 + 2y^8$ the highest power of the variable is 8, so the degree is 8.
*   The only term in $2$ is 2, which can be written as $2x^0$. The exponent of $x$ is 0, so the degree is 0.

## Key points

*   A polynomial in one variable is an expression in which the variable has only whole numbers as exponents.
*   The parts of a polynomial are called its terms, and each term has a coefficient.
*   Polynomials with one, two and three terms are called monomials, binomials and trinomials.
*   The degree of a polynomial is the highest power of the variable.
*   Polynomials of degree one, two and three are called linear, quadratic and cubic polynomials.
*   The degree of a non-zero constant polynomial is zero, and the degree of the zero polynomial is not defined.
