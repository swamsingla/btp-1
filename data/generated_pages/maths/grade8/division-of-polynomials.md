---
{
  "concept": "Division of Algebraic Expressions",
  "slug": "division-of-polynomials",
  "grade": 8,
  "language": "en",
  "hand_edited": "2026-10-13: line-by-line hand audit against the source passages, edited directly (tagged copy; published body rebuilt from it): the source (Grade 9 identities / zeroes-of-polynomial extracts) contains no division method, so the [S1]/[S2] tags on the monomial and long-division examples were false and removed; the long-division example never stated its quotient; the 'Using Identities' section showed a rewriting but no division; removed the pizza analogy; added a non-zero-remainder example, the dividend = divisor x quotient + remainder check, and two identity-based divisions. The division methods themselves are correct maths but unsourced; also removed unverified claims that the student has already studied or learned something that were copied from the Grade 9 source or unverified against the prerequisite graph",
  "subject": "maths",
  "area": "Algebra",
  "model": "sarvam-105b",
  "settings": {
    "temperature": 0.3,
    "max_tokens": 8000,
    "reasoning_effort": "none"
  },
  "usage": {
    "completion_tokens": 820,
    "prompt_tokens": 7101,
    "total_tokens": 7921,
    "completion_tokens_details": {
      "accepted_prediction_tokens": null,
      "audio_tokens": null,
      "reasoning_tokens": 0,
      "rejected_prediction_tokens": null
    },
    "prompt_tokens_details": null
  },
  "target_words": [
    950,
    1300
  ],
  "generated_at": "2026-10-13T02:06:59",
  "source_grade": 9,
  "grade_delta": 1,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g9_maths_chapter2_022",
      "chapter": "chapter2",
      "section": "2.5 Algebraic Identities"
    },
    {
      "ref": "S2",
      "passage_id": "g9_maths_chapter2_000",
      "chapter": "chapter2",
      "section": "2.1 Introduction"
    },
    {
      "ref": "S3",
      "passage_id": "g9_maths_chapter2_009",
      "chapter": "chapter2",
      "section": "2.3 Zeroes of a Polynomial"
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
    "explanatory_paragraphs_without_a_citation": 3,
    "words": 510,
    "target_words": [
      950,
      1300
    ],
    "untraceable_sections": 0,
    "ok": true,
    "short": [
      "length: 510 words, under 950"
    ],
    "structural_problems": [],
    "verification": {
      "verdict": "ok",
      "checks": 1,
      "tokens": 1364
    }
  },
  "terms": [
    "polynomial",
    "monomial",
    "binomial",
    "factorisation",
    "algebraic identity",
    "dividend",
    "divisor",
    "quotient",
    "remainder",
    "long division"
  ]
}
---

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

Sometimes division is easier if you factorise the dividend first. You can use algebraic identities to do this. For example, the identity $x^2 - y^2 = (x + y)(x - y)$ is useful for a difference of two squares.

Let us divide $x^2 - 9$ by $x + 3$. Since $9 = 3^2$, the identity gives $x^2 - 9 = (x + 3)(x - 3)$. Then
$$ \frac{x^2 - 9}{x + 3} = \frac{(x + 3)(x - 3)}{x + 3} = x - 3 $$
The common factor $x + 3$ cancels, so the quotient is $x - 3$.

The identity $(x + y)^2 = x^2 + 2xy + y^2$ works in the same way. Since $x^2 + 10x + 25 = (x + 5)^2$, dividing $x^2 + 10x + 25$ by $x + 5$ gives $x + 5$.

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
*   Factorising using algebraic identities can simplify the division process.
*   Always check your answer: dividend = divisor × quotient + remainder.
*   This topic builds on the factorisation of algebraic expressions, which uses algebraic identities.
