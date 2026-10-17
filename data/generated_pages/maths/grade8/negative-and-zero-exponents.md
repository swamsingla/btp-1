---
{
  "concept": "Negative and Zero Exponents",
  "slug": "negative-and-zero-exponents",
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
    "completion_tokens": 973,
    "prompt_tokens": 6611,
    "total_tokens": 7584,
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
  "generated_at": "2026-10-12T21:14:46",
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
      "passage_id": "g8_maths_part1_chapter2_005",
      "chapter": "chapter2",
      "section": "2.2 Exponential Notation and Operations"
    },
    {
      "ref": "S3",
      "passage_id": "g8_maths_part1_chapter2_015",
      "chapter": "chapter2",
      "section": "2.3 The Other Side of Powers"
    }
  ],
  "citation_check": {
    "cited": [
      "2",
      "3"
    ],
    "invented_citations": [],
    "unused_sources": [
      "1"
    ],
    "explanatory_paragraphs_without_a_citation": 0,
    "words": 518,
    "target_words": [
      950,
      1300
    ],
    "untraceable_sections": 0,
    "ok": true,
    "short": [
      "length: 518 words, under 950"
    ],
    "structural_problems": [],
    "verification": {
      "verdict": "spiralled",
      "checks": 1,
      "tokens": 9176
    }
  },
  "terms": [
    "exponents",
    "powers",
    "base",
    "exponent",
    "standard form",
    "scientific notation",
    "laws of exponents"
  ],
  "hand_edited": "2026-10-12: second line-by-line audit against the textbook, edited directly: said the paper thickness doubles each fold, gave the 7-fold result in standard form, added the reverse rule. 2026-10-12: hand audit: 'In Grade 8 maths, you have already learned' read as a self-reference; reworded."
}
---

# Negative and Zero Exponents

Earlier in this chapter you learned about powers and exponents. You know that $5^4$ means 5 multiplied by itself 4 times, which equals 625. You also know how to use the laws of exponents to multiply and divide powers when the exponents are counting numbers. However, what happens when you need to divide a smaller power by a larger power, or when you divide a number by itself? This page explores the answers to these questions, introducing you to zero and negative exponents.

## The Rule for Zero Exponents

You already know that $x^a \times x^b = x^{a+b}$ and $x^a \div x^b = x^{a-b}$. But what happens when the exponents are equal? If you divide $2^4$ by $2^4$, you get 1, because the top and bottom cancel out. Using the law of exponents, $2^4 \div 2^4 = 2^{4-4} = 2^0$. This means that $2^0$ must equal 1. This rule holds true for any non-zero base $x$ and any counting number $a$, so $x^a \div x^a = x^0 = 1$, where $x \neq 0$.

## The Rule for Negative Exponents

What happens if you divide $2^4$ by $2^5$? If you expand it out, you get $\frac{2 \times 2 \times 2 \times 2}{2 \times 2 \times 2 \times 2 \times 2}$, which simplifies to $\frac{1}{2}$, or $\frac{1}{2^1}$. Using the law of exponents, $2^4 \div 2^5 = 2^{4-5} = 2^{-1}$. Therefore, $2^{-1} = \frac{1}{2}$. The same logic applies to any negative exponent: $10^{-3} = \frac{1}{10^3}$, $7^{-2} = \frac{1}{7^2}$, and $2^{-6} = \frac{1}{2^6}$. In general, for any non-zero base $n$ and positive integer $a$, $n^{-a} = \frac{1}{n^a}$. The rule also works in reverse: $10^3 = \frac{1}{10^{-3}}$ and $7^2 = \frac{1}{7^{-2}}$.

## Standard Form and Scientific Notation

As numbers get very large or very small, writing them out in full becomes difficult. For example, the initial thickness of a sheet of paper might be $0.001$ cm. The thickness doubles with each fold, so if you fold it 7 times, the thickness becomes $0.001 \times 2^7 = 0.128$ cm. Standard form, or scientific notation, helps us write these numbers easily. We write $0.001$ as $1 \times 10^{-3}$. This is because $10^{-3} = \frac{1}{10^3} = \frac{1}{1000} = 0.001$. So, the thickness after 7 folds is $1 \times 10^{-3} \times 2^7$ cm, which is $1.28 \times 10^{-1}$ cm in standard form.

## Worked Example

Let's apply these rules to a problem. Suppose we need to simplify the expression $2^3 \times 2^{-5}$. Using the law of exponents, we add the exponents: $2^{3 + (-5)} = 2^{-2}$. Since we have a negative exponent, we convert it to a positive exponent by taking the reciprocal: $2^{-2} = \frac{1}{2^2} = \frac{1}{4}$.

## Key points
- Any non-zero number raised to the power of zero equals 1: $x^0 = 1$, where $x \neq 0$.
- A negative exponent means the reciprocal of the base raised to the positive exponent: $n^{-a} = \frac{1}{n^a}$, where $n \neq 0$.
- Standard form uses powers of 10 to write very large or very small numbers easily.
- The laws of exponents still apply when using zero and negative exponents.