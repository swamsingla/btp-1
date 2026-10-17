---
{
  "concept": "Algebraic Identities",
  "slug": "algebraic-identities",
  "grade": 8,
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
    "completion_tokens": 1150,
    "prompt_tokens": 6362,
    "total_tokens": 7512,
    "completion_tokens_details": {
      "accepted_prediction_tokens": null,
      "audio_tokens": null,
      "reasoning_tokens": 0,
      "rejected_prediction_tokens": null
    },
    "prompt_tokens_details": null
  },
  "target_words": [
    700,
    1250
  ],
  "generated_at": "2026-10-11T15:42:17",
  "source_grade": 8,
  "grade_delta": 0,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g8_maths_part1_chapter6_025",
      "chapter": "chapter6",
      "section": "6.3 Mind the Mistake, Mend the Mistake"
    },
    {
      "ref": "S2",
      "passage_id": "g8_maths_part1_chapter6_022",
      "chapter": "chapter6",
      "section": "6.2 Special Cases of the Distributive Property"
    }
  ],
  "citation_check": {
    "cited": [
      "1",
      "2"
    ],
    "invented_citations": [],
    "unused_sources": [],
    "explanatory_paragraphs_without_a_citation": 0,
    "words": 746,
    "target_words": [
      700,
      1250
    ],
    "untraceable_sections": 0,
    "ok": true,
    "structural_problems": [],
    "verification": {
      "verdict": "spiralled",
      "checks": 1,
      "tokens": 9361
    }
  },
  "terms": [
    "algebraic identity",
    "binomial",
    "trinomial",
    "expand",
    "simplify",
    "square of a sum",
    "square of a difference",
    "difference of squares",
    "quadratic expression"
  ],
  "hand_edited": "2026-10-12: moved from Grade 7 to Grade 8 — it was written from Grade 8 textbook text. Content unchanged apart from grade labels."
}
---

# Algebraic Identities

Algebraic identities are mathematical shortcuts that help us expand or simplify algebraic expressions quickly. Instead of multiplying out every term by hand, we can use standard patterns to find the answer in just a few steps. These patterns are very useful when you are calculating large numbers or simplifying complex expressions in algebra.

## The Square of a Sum: $(a + b)^2$

One of the most common patterns is the square of a sum. When you multiply a binomial by itself, you get a trinomial. The rule is that the square of a sum is equal to the square of the first term, plus twice the product of the two terms, plus the square of the second term. In symbols, this is written as $(a + b)^2 = a^2 + 2ab + b^2$.

Let us look at an example using numbers. Suppose we want to find the value of $65^2$. We can break 65 into $60 + 5$. Using the identity, we calculate $(60 + 5)^2 = 60^2 + 2(60 \times 5) + 5^2 = 3600 + 600 + 25 = 4225$. This method saves a lot of time compared to multiplying 65 by 65 directly.

## The Square of a Difference: $(a - b)^2$

Another useful pattern is the square of a difference. When you square a binomial where the second term is subtracted, the middle term becomes negative. The rule states that the square of a difference is equal to the square of the first term, minus twice the product of the two terms, plus the square of the second term. This is written as $(a - b)^2 = a^2 - 2ab + b^2$.

We can use this to calculate $55^2$ by writing it as $(60 - 5)^2$. Applying the identity, we get $60^2 - 2(60 \times 5) + 5^2 = 3600 - 600 + 25 = 3025$. Notice that the middle term is negative, which gives us the correct result.

## The Difference of Squares: $(a + b)(a - b)$

The third pattern is the difference of squares. When you multiply the sum and the difference of the same two terms, the middle terms cancel out. The result is simply the square of the first term minus the square of the second term. In symbols, this is $(a + b)(a - b) = a^2 - b^2$.

This identity is very handy for multiplying large numbers quickly. For example, to find the value of $98 \times 102$, we can write it as $(100 - 2)(100 + 2)$. Using the identity, we calculate $100^2 - 2^2 = 10000 - 4 = 9996$. This method is much faster than doing the long multiplication.

## Expanding Three Terms: $(a + b + c)^2$

Sometimes you need to square an expression with three terms. The rule for the square of a trinomial is to square each individual term and then add twice the product of each pair of terms. In symbols, this is $(a + b + c)^2 = a^2 + b^2 + c^2 + 2ab + 2bc + 2ca$.

## The Product of Binomials: $(x + a)(x + b)$

When you multiply two binomials with the same variable, you can expand the expression by multiplying each term in the first binomial by each term in the second binomial. The result is a quadratic expression. For example, $(x + 2)(x + 5)$ expands to $x^2 + 7x + 10$.

## Worked example

Let us apply the square of a sum identity to a simple algebraic expression. We want to expand $(3x + 4)^2$. Using the rule $(a + b)^2 = a^2 + 2ab + b^2$, we let $a = 3x$ and $b = 4$. The expansion is $(3x)^2 + 2(3x \times 4) + 4^2 = 9x^2 + 24x + 16$.

## Key points

*   An algebraic identity is a rule that holds true for all values of the variables.
*   The square of a sum is $(a + b)^2 = a^2 + 2ab + b^2$.
*   The square of a difference is $(a - b)^2 = a^2 - 2ab + b^2$.
*   The product of a sum and a difference is $(a + b)(a - b) = a^2 - b^2$.
*   Expanding $(x + a)(x + b)$ gives $x^2 + (a + b)x + ab$.