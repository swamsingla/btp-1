---
{
  "concept": "Factor Theorem",
  "slug": "factor-theorem",
  "grade": 9,
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
    "completion_tokens": 2009,
    "prompt_tokens": 8036,
    "total_tokens": 10045,
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
  "generated_at": "2026-10-17T04:58:57",
  "source_grade": 9,
  "grade_delta": 0,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g9_maths_chapter2_014",
      "chapter": "chapter2",
      "section": "2.4 Factorisation of Polynomials"
    },
    {
      "ref": "S2",
      "passage_id": "g9_maths_chapter2_012",
      "chapter": "chapter2",
      "section": "2.3 Zeroes of a Polynomial"
    },
    {
      "ref": "S3",
      "passage_id": "g9_maths_chapter1_026",
      "chapter": "chapter1",
      "section": "1.5 Laws of Exponents for Real Numbers"
    }
  ],
  "citation_check": {
    "cited": [
      "1",
      "2"
    ],
    "invented_citations": [],
    "unused_sources": [
      "3"
    ],
    "explanatory_paragraphs_without_a_citation": 0,
    "words": 1015,
    "target_words": [
      1000,
      1350
    ],
    "untraceable_sections": 0,
    "ok": true,
    "structural_problems": []
  },
  "hand_edited": "2026-10-17: held on three 'arithmetic' flags that are false positives (the checker reads p(1), p(2), p(-2) as the numbers 1, 2, -2; the arithmetic on the page was correct). Hand audit: 'Factor Theorem is a particular case of the Remainder Theorem' (inverted; the theorem is PROVED using the Remainder Theorem) corrected; the letters a and b used for both coefficients and zeroes in the quadratic paragraph removed; 'splitting is not always appropriate' tightened to the book's 'not appropriate to start with'; filler removed; 'zeros' -> 'zeroes' as in the book; the worked example x^2 - 7x + 12 is not in the book, so its tags were dropped and its factorisation completed; one skipped algebra step added.",
  "terms": [
    "zero of a polynomial",
    "factor",
    "factor theorem",
    "remainder theorem",
    "polynomial equation",
    "root",
    "linear polynomial",
    "quadratic polynomial",
    "cubic polynomial"
  ]
}
---

# Factor Theorem

A zero of a polynomial is a number $c$ such that $p(c) = 0$. For example, the zero of the polynomial $x - 1$ is 1 because $p(1) = 1 - 1 = 0$. The Factor Theorem gives a direct link between these zeroes and the factors of a polynomial. If $p(x)$ is a polynomial and $a$ is any real number, then $x - a$ is a factor of $p(x)$ if and only if $p(a) = 0$. This means we can test whether $x - a$ is a factor of $p(x)$ by checking whether $p(a) = 0$.

## The Theorem Stated

The Factor Theorem connects the zeroes of a polynomial to its factors. It states that for a polynomial $p(x)$ of degree $n \geq 1$ and a real number $a$, $x - a$ is a factor of $p(x)$ if $p(a) = 0$, and $p(a) = 0$ if $x - a$ is a factor of $p(x)$. This works both ways. If $p(a) = 0$ for some value of $a$, then $x - a$ is a factor of $p(x)$.

## Using the Remainder Theorem

The Factor Theorem is proven using the Remainder Theorem. The Remainder Theorem tells us that $p(x) = (x - a)q(x) + p(a)$. If $p(a) = 0$, then the equation becomes $p(x) = (x - a)q(x)$. This shows that $x - a$ is a factor of $p(x)$. Conversely, if $x - a$ is a factor of $p(x)$, then $p(x) = (x - a)g(x)$ for some polynomial $g(x)$. If we substitute $x = a$ into this equation, we get $p(a) = (a - a)g(a) = 0 \times g(a) = 0$.

## Finding Zeroes

To use the Factor Theorem, we need the zeroes of the polynomial. A zero of a polynomial $p(x)$ is a number $c$ such that $p(c) = 0$. For a linear polynomial, there is exactly one zero. However, a polynomial can have more than one zero. For example, the polynomial $x^2 - 2x$ has zeroes at 2 and 0 because $p(2) = 2^2 - 2 \times 2 = 0$ and $p(0) = 0^2 - 2 \times 0 = 0$.

## Checking if a Linear Term is a Factor

The Factor Theorem can be used to check whether a linear expression is a factor of a polynomial. For example, to check if $x + 2$ is a factor of $x^3 + 3x^2 + 5x + 6$, we find the zero of $x + 2$, which is -2. Let $p(x) = x^3 + 3x^2 + 5x + 6$. Then, $p(-2) = (-2)^3 + 3(-2)^2 + 5(-2) + 6 = -8 + 12 - 10 + 6 = 0$. Since $p(-2) = 0$, by the Factor Theorem, $x + 2$ is a factor of $x^3 + 3x^2 + 5x + 6$.

## Finding the Value of a Constant

The Factor Theorem can also be used to find the value of a constant in a polynomial. For example, if $x - 1$ is a factor of $p(x) = 4x^3 + 3x^2 - 4x + k$, then $p(1) = 0$. Now, $p(1) = 4(1)^3 + 3(1)^2 - 4(1) + k = 4 + 3 - 4 + k = 0$, which gives $k = -3$.

## Factoring Quadratic Polynomials

The Factor Theorem can be used to factorise quadratic polynomials. For example, to factorise $y^2 - 5y + 6$, we let $p(y) = y^2 - 5y + 6$. If $p(y) = (y - a)(y - b)$, the constant term is $ab$, so $ab = 6$ and we look at the factors of 6. We find that $p(2) = 2^2 - 5(2) + 6 = 4 - 10 + 6 = 0$, so $y - 2$ is a factor of $p(y)$. Also, $p(3) = 3^2 - 5(3) + 6 = 9 - 15 + 6 = 0$, so $y - 3$ is also a factor of $y^2 - 5y + 6$. Therefore, $y^2 - 5y + 6 = (y - 2)(y - 3)$.

## Factoring Cubic Polynomials

For cubic polynomials, the splitting method is not appropriate to start with, so we need to find at least one factor first. For example, to factorise $x^3 - 23x^2 + 142x - 120$, we let $p(x) = x^3 - 23x^2 + 142x - 120$. We look for factors of -120 and try them by trial. We find that $p(1) = 1^3 - 23(1)^2 + 142(1) - 120 = 1 - 23 + 142 - 120 = 0$. So, $x - 1$ is a factor of $p(x)$.

Now we can write $p(x) = (x - 1)(x^2 - 22x + 120)$. We can factorise the quadratic part by splitting the middle term or by using the Factor Theorem again. By splitting the middle term, we get $x^2 - 22x + 120 = x^2 - 12x - 10x + 120 = x(x - 12) - 10(x - 12) = (x - 10)(x - 12)$. Therefore, $x^3 - 23x^2 + 142x - 120 = (x - 1)(x - 10)(x - 12)$.

## Worked example

Let us apply the Factor Theorem to a new polynomial. Consider $p(x) = x^2 - 7x + 12$. We want to check if $x - 3$ is a factor of $p(x)$. The zero of $x - 3$ is 3. We evaluate $p(3) = 3^2 - 7(3) + 12 = 9 - 21 + 12 = 0$. Since $p(3) = 0$, by the Factor Theorem, $x - 3$ is a factor of $p(x)$. Dividing $p(x)$ by $x - 3$ gives the other factor $x - 4$, so $x^2 - 7x + 12 = (x - 3)(x - 4)$.

## Key points

- A zero of a polynomial $p(x)$ is a number $c$ such that $p(c) = 0$.
- If $p(a) = 0$, then $x - a$ is a factor of $p(x)$.
- If $x - a$ is a factor of $p(x)$, then $p(a) = 0$.
- The Factor Theorem is proved using the Remainder Theorem, by which $p(x) = (x - a)q(x) + p(a)$.
- The Factor Theorem can be used to factorise quadratic and cubic polynomials by finding their zeroes.