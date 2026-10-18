---
{
  "concept": "Relationship Between Zeroes and Coefficients",
  "slug": "zeroes-coefficients-relationship",
  "grade": 10,
  "language": "en",
  "subject": "maths",
  "area": "Algebra",
  "model": "sarvam-105b",
  "settings": {
    "temperature": 0.3,
    "max_tokens": 8000,
    "reasoning_effort": "none"
  },
  "usage": {
    "completion_tokens": 1661,
    "prompt_tokens": 7152,
    "total_tokens": 8813,
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
  "generated_at": "2026-10-17T22:04:27",
  "source_grade": 10,
  "grade_delta": 0,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g10_maths_chapter2_012",
      "chapter": "chapter2",
      "section": "2.3 Relationship between Zeroes and Coefficients of a Polynomial"
    },
    {
      "ref": "S2",
      "passage_id": "g10_maths_chapter2_003",
      "chapter": "chapter2",
      "section": "2.1 Introduction"
    }
  ],
  "citation_check": {
    "cited": [],
    "invented_citations": [],
    "unused_sources": [
      "1",
      "2"
    ],
    "explanatory_paragraphs_without_a_citation": 9,
    "words": 1004,
    "target_words": [
      1000,
      1350
    ],
    "untraceable_sections": 2,
    "ok": false,
    "structural_problems": []
  },
  "terms": [
    "polynomial",
    "zero",
    "linear polynomial",
    "quadratic polynomial",
    "cubic polynomial",
    "coefficient",
    "factor",
    "factorisation",
    "splitting the middle term",
    "constant term",
    "degree",
    "vieta's formulas",
    "sum of zeroes",
    "product of zeroes"
  ]
}
---

# Relationship Between Zeroes and Coefficients

In Grade 9, you learned how to find the zero of a linear polynomial and discovered that it is directly related to its coefficients. This chapter takes that idea a step further by exploring whether a similar connection exists for quadratic and cubic polynomials. Understanding this relationship allows you to find the zeroes of a polynomial without fully solving it, or even to construct a polynomial when you know its zeroes.

## Quadratic Polynomials

Let us begin with a quadratic polynomial, which is a polynomial of degree 2. A general quadratic polynomial is written as $p(x) = ax^{2} + bx + c$, where $a$, $b$, and $c$ are real numbers and $a \neq 0$. The zeroes of a quadratic polynomial are the values of $x$ that make the polynomial equal to zero.

To see the relationship between the zeroes and the coefficients, we can look at a specific example. Consider the quadratic polynomial $p(x) = 2x^{2} - 8x + 6$. We can factorise this by splitting the middle term. We need to split $-8x$ into a sum of two terms whose product is $12x^{2}$. This gives us $-6x - 2x$. Factoring by grouping, we get $2x(x - 3) - 2(x - 3)$, which simplifies to $2(x - 1)(x - 3)$. Setting $p(x) = 0$, we find that $x = 1$ or $x = 3$ are the zeroes.

Now, let us examine the sum and product of these zeroes. The sum of the zeroes is $1 + 3 = 4$. Notice that this is exactly $\frac{-(-8)}{2}$. In general, the sum of the zeroes is equal to the negative of the coefficient of $x$ divided by the coefficient of $x^{2}$. The product of the zeroes is $1 \times 3 = 3$, which is equal to $\frac{6}{2}$. In general, the product of the zeroes is equal to the constant term divided by the coefficient of $x^{2}$.

Let us consider another example, $p(x) = 3x^{2} + 5x - 2$. By splitting the middle term into $6x - x$, we can factorise it as $(3x - 1)(x + 2)$. The zeroes are $x = \frac{1}{3}$ and $x = -2$. The sum of the zeroes is $\frac{1}{3} + (-2) = -\frac{5}{3}$, which is equal to $\frac{-5}{3}$. The product of the zeroes is $\frac{1}{3} \times (-2) = -\frac{2}{3}$, which is equal to $\frac{-2}{3}$.

If $\alpha$ and $\beta$ are the zeroes of the quadratic polynomial $p(x) = ax^{2} + bx + c$, then $x - \alpha$ and $x - \beta$ are the factors of $p(x)$. Therefore, we can write $ax^{2} + bx + c = k(x - \alpha)(x - \beta)$, where $k$ is a constant. Expanding this, we get $k[x^{2} - (\alpha + \beta)x + \alpha\beta]$. Comparing the coefficients of $x^{2}$, $x$, and the constant terms on both sides, we get $a = k$, $b = -k(\alpha + \beta)$, and $c = k\alpha\beta$. This gives us the general formulas:
$$
\alpha + \beta = \frac{-b}{a},
$$
$$
\alpha\beta = \frac{c}{a}.
$$
These formulas are known as Vieta's formulas for quadratic polynomials.

## Cubic Polynomials

The same principle extends to cubic polynomials, which are polynomials of degree 3. A general cubic polynomial is written as $ax^{3} + bx^{2} + cx + d$, where $a$, $b$, $c$, and $d$ are real numbers and $a \neq 0$.

Let us consider the cubic polynomial $p(x) = 2x^{3} - 5x^{2} - 14x + 8$. The zeroes of this polynomial are $4$, $-2$, and $\frac{1}{2}$. The sum of the zeroes is $4 + (-2) + \frac{1}{2} = \frac{5}{2}$, which is equal to $\frac{-(-5)}{2}$. The product of the zeroes is $4 \times (-2) \times \frac{1}{2} = -4$, which is equal to $\frac{-8}{2}$.

However, there is one more relationship here. Consider the sum of the products of the zeroes taken two at a time. We have $\{4 \times (-2)\} + \{(-2) \times \frac{1}{2}\} + \{\frac{1}{2} \times 4\} = -8 - 1 + 2 = -7$, which is equal to $\frac{-14}{2}$.

In general, if $\alpha$, $\beta$, and $\gamma$ are the zeroes of the cubic polynomial $ax^{3} + bx^{2} + cx + d$, then the relationships are:
$$
\alpha + \beta + \gamma = \frac{-b}{a},
$$
$$
\alpha\beta + \beta\gamma + \gamma\alpha = \frac{c}{a},
$$
$$
\alpha\beta\gamma = \frac{-d}{a}.
$$

## Worked example

Let us apply these relationships to a new problem. Find the zeroes of the quadratic polynomial $x^{2} + 7x + 10$, and verify the relationship between the zeroes and the coefficients.

We can factorise the polynomial as $(x + 2)(x + 5)$. Setting $p(x) = 0$, we find that $x = -2$ or $x = -5$ are the zeroes. Now, let us verify the relationships. The sum of the zeroes is $-2 + (-5) = -7$, which is equal to $\frac{-7}{1}$. The product of the zeroes is $(-2) \times (-5) = 10$, which is equal to $\frac{10}{1}$. This confirms that the sum and product of the zeroes are related to the coefficients of the polynomial.

## Building a Polynomial from Its Zeroes

The relationships also work in reverse. Since $ax^{2} + bx + c = a\left[x^{2} - (\alpha + \beta)x + \alpha\beta\right]$, a quadratic polynomial with zeroes $\alpha$ and $\beta$ is
$$
k\left[x^{2} - (\text{sum of the zeroes})\,x + \text{product of the zeroes}\right]
$$
where $k$ is any non-zero real number.

Example: Find a quadratic polynomial whose zeroes have sum $-3$ and product $2$. Taking $k = 1$, the polynomial is $x^{2} - (-3)x + 2 = x^{2} + 3x + 2$. We can check this: $x^{2} + 3x + 2 = (x + 1)(x + 2)$, so the zeroes are $-1$ and $-2$. Their sum is $-3$ and their product is $2$, as required.

A quadratic polynomial has at most two zeroes, and a cubic polynomial has at most three. Because $k$ can be any non-zero number, more than one polynomial can have the same zeroes: for instance, $2x^{2} + 6x + 4$ has the same zeroes $-1$ and $-2$ as $x^{2} + 3x + 2$.

## Key points

*   For a quadratic polynomial $ax^{2} + bx + c$, the sum of the zeroes is $\frac{-b}{a}$ and the product of the zeroes is $\frac{c}{a}$.
*   For a cubic polynomial $ax^{3} + bx^{2} + cx + d$, the sum of the zeroes is $\frac{-b}{a}$, the sum of the products of the zeroes taken two at a time is $\frac{c}{a}$, and the product of the zeroes is $\frac{-d}{a}$.
*   These relationships are derived by comparing the coefficients of the polynomial with the expanded form of its factors.
*   The relationships between zeroes and coefficients are useful for constructing a polynomial when the zeroes are known.
*   The relationships for cubic polynomials are a natural extension of the quadratic case, but with an additional term for the sum of products of zeroes taken two at a time.