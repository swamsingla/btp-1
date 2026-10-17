---
{
  "concept": "Exponents and Powers",
  "slug": "exponents-and-powers",
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
    "completion_tokens": 1031,
    "prompt_tokens": 6743,
    "total_tokens": 7774,
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
  "generated_at": "2026-10-12T21:14:49",
  "source_grade": 8,
  "grade_delta": 0,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g8_maths_part1_chapter2_015",
      "chapter": "chapter2",
      "section": "2.3 The Other Side of Powers"
    },
    {
      "ref": "S2",
      "passage_id": "g8_maths_part1_chapter2_019",
      "chapter": "chapter2",
      "section": "2.4 Powers of 10"
    },
    {
      "ref": "S3",
      "passage_id": "g8_maths_part2_chapter2_019",
      "chapter": "chapter2",
      "section": "2.6 A Long-Standing Open Problem"
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
    "words": 580,
    "target_words": [
      950,
      1300
    ],
    "untraceable_sections": 0,
    "ok": true,
    "short": [
      "length: 580 words, under 950"
    ],
    "structural_problems": [],
    "verification": {
      "verdict": "spiralled",
      "checks": 1,
      "tokens": 9251
    }
  },
  "terms": [
    "exponent",
    "power",
    "base",
    "scientific notation",
    "coefficient",
    "reciprocal",
    "counting numbers",
    "integers",
    "standard form",
    "indian numerals"
  ],
  "hand_edited": "2026-10-12: second line-by-line audit against the textbook, edited directly: exact base/exponent definition, power-of-a-power rule, zero exponent derived from the division rule, 1 <= x < 10, Mumbai exponent example. 2026-10-12: hand audit: Sun-Saturn distance had an extra 00 group (was 10^14 m, textbook is 1.4335 x 10^12 m); exponent/digits sentence was inexact."
}
---

# Exponents and Powers

Exponents and powers are a way of writing repeated multiplication in a shorter form. Instead of writing $2 \times 2 \times 2 \times 2$, we can write $2^4$. This notation is very useful in everyday life, from measuring the vast distances between planets in our solar system to understanding the mass of the Earth. This page will explain how to use exponents, the rules that govern them, and how to write very large numbers using powers of 10.

## Understanding $a^n$ and the Laws of Exponents

We write $n^a$ for $n$ multiplied by itself $a$ times. For example, $2^4 = 2 \times 2 \times 2 \times 2 = 16$. Here $2$ is the base and $4$ is the exponent, also called the power. When we multiply powers with the same base, we add their exponents. This is written as $n^a \times n^b = n^{a+b}$, where $n \neq 0$ and $a$ and $b$ are counting numbers. Raising a power to a power multiplies the exponents: $(n^a)^b = n^{a \times b}$.

Similarly, when we divide powers with the same base, we subtract their exponents. This gives us the rule $n^a \div n^b = n^{a-b}$. For example, if we start with a line of length $2^4$ units and halve it three times, we get $2^4 \div 2^3 = 2^{4-3} = 2^1 = 2$ units.

## Zero and Negative Exponents

We can also find the value of powers when the exponent is zero or negative. When the top and bottom exponents are the same, the division rule gives $2^0 = 2^{a-a} = 2^a \div 2^a = 1$. Therefore, $2^0 = 1$, and in general $x^0 = 1$ for any $x \neq 0$.

When the exponent is negative, the power represents a fraction. For example, if we halve a line of length $2^4$ units five times, we get $2^4 \div 2^5 = 2^{(4-5)} = 2^{-1}$ units. When expanded, this equals $\frac{1}{2^1} = \frac{1}{2}$. Similarly, $10^{-3} = \frac{1}{10^3}$ and $7^{-2} = \frac{1}{7^2}$. In general, $n^{-a} = \frac{1}{n^a}$ and $n^a = \frac{1}{n^{-a}}$, where $n \neq 0$.

## Writing Large Numbers with Powers of 10

Writing very large numbers can be difficult and lead to mistakes. For example, the distance between the Sun and Saturn is $14,33,50,00,00,000$ metres, and the Sun is $30,00,00,00,00,00,00,00,00,000$ metres from the centre of our Milky Way galaxy. To make these numbers easier to read and compare, we can use scientific notation.

In scientific notation, we write a number as $x \times 10^y$, where $1 \leq x < 10$ and $y$ is an integer. For example, $80,00,000$ can be written as $8 \times 10^6$. The exponent is very important because it tells us how large the number is: $8 \times 10^6$ has 7 digits, one more than the exponent. Changing the 2 in $2 \times 10^7$ to a 3 raises the number by one-half, but changing the 7 to an 8 makes it 10 times larger.

## Worked example

Let us apply the rules of exponents to simplify an expression. Consider the expression $2^{-4} \times 2^7$. Using the rule for multiplying powers with the same base, we add the exponents: $2^{-4} \times 2^7 = 2^{-4+7} = 2^3 = 8$.

## Key points
- Exponents represent repeated multiplication, such as $2^4 = 2 \times 2 \times 2 \times 2 = 16$.
- When multiplying powers with the same base, add the exponents: $n^a \times n^b = n^{a+b}$.
- When dividing powers with the same base, subtract the exponents: $n^a \div n^b = n^{a-b}$.
- To raise a power to a power, multiply the exponents: $(n^a)^b = n^{a \times b}$.
- Any non-zero number raised to the power of zero equals $1$: $n^0 = 1$.
- A negative exponent indicates the reciprocal: $n^{-a} = \frac{1}{n^a}$.
- Scientific notation writes numbers as $x \times 10^y$, where $1 \leq x < 10$ and $y$ is an integer.