---
{
  "concept": "Square Numbers",
  "slug": "square-numbers",
  "grade": 8,
  "language": "en",
  "subject": "maths",
  "area": "Number Theory",
  "model": "sarvam-105b",
  "settings": {
    "temperature": 0.3,
    "max_tokens": 8000,
    "reasoning_effort": "none"
  },
  "usage": {
    "completion_tokens": 1210,
    "prompt_tokens": 7036,
    "total_tokens": 8246,
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
  "generated_at": "2026-10-12T21:10:10",
  "source_grade": 8,
  "grade_delta": 0,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g8_maths_part1_chapter1_003",
      "chapter": "chapter1",
      "section": "1.1 Square Numbers"
    }
  ],
  "citation_check": {
    "cited": [
      "1"
    ],
    "invented_citations": [],
    "unused_sources": [],
    "explanatory_paragraphs_without_a_citation": 0,
    "words": 809,
    "target_words": [
      950,
      1300
    ],
    "untraceable_sections": 0,
    "ok": true,
    "structural_problems": [],
    "verification": {
      "verdict": "spiralled",
      "checks": 1,
      "tokens": 9411
    }
  },
  "terms": [
    "square numbers",
    "perfect squares",
    "units digit",
    "prime factorisation",
    "square root"
  ],
  "hand_edited": "2026-10-12: second line-by-line audit against the textbook, edited directly: natural number in the intro, rule for passing 0 added, why 11 cm fits. 2026-10-12: hand audit: rewrote the handkerchief worked example (the 144 comparison did not explain why 15 cm is impossible)."
}
---

# Square Numbers

Square numbers are the result of multiplying a natural number by itself. They represent the total number of small squares that would fit perfectly inside a larger square. Understanding square numbers is important because they appear everywhere in geometry, algebra, and even in everyday situations like calculating areas for a garden or a room.

## What Are Perfect Squares?

A perfect square is the square of a natural number. For any number $n$, we write $n \times n = n^2$, which is read as 'n squared'. For example, $5 \times 5 = 5^2 = 25$, so 25 is a perfect square. The squares of natural numbers, such as 1, 4, 9, 16, and 25, are all perfect squares. You can also find the square of a fraction or a decimal. For instance, the area of a square with a side length of $2.5$ units is $(2.5)^2 = 6.25$ square units.

## Properties of the Units Digit

When you look at the last digit of a perfect square, you will only ever find 0, 1, 4, 5, 6, or 9. A number that ends in 2, 3, 7, or 8 can never be a perfect square. However, just because a number ends in 1, 4, 5, 6, or 9 does not guarantee it is a square. For example, 26 ends in 6, but it is not a perfect square. The units digit is useful for quickly identifying numbers that are definitely not squares. If a number ends with 2, 3, 7, or 8, you can immediately say it is not a square.

## Squares and Odd Numbers

There is a special connection between square numbers and consecutive odd numbers. The sum of the first $n$ odd numbers is always $n^2$. For example, $1 + 3 + 5 + 7 + 9 = 25$, which is $5^2$. You can use this pattern to test if a number is a perfect square. Start with the number and repeatedly subtract consecutive odd numbers starting from 1. If you reach exactly 0, the number is a perfect square. If you pass 0 without landing on it, the number is not a perfect square. For example, starting with 25 and subtracting 1, 3, 5, 7, and 9 in order gives exactly 0, so 25 is a perfect square.

## Finding the Square Root

The square root of a number is the value that, when multiplied by itself, gives the original number. For example, since $7 \times 7 = 49$, the side length of a square with an area of 49 square centimetres is 7 cm. We call 7 the square root of 49. Every perfect square has two integer square roots, one positive and one negative. For instance, the square roots of 64 are +8 and -8, because both $8^2$ and $(-8)^2$ equal 64.

## Using Prime Factorisation

You can determine if a number is a perfect square by looking at its prime factorisation. If you can divide the prime factors of a number into two equal groups, then the product of the factors in either group will form the square root. For example, 324 can be written as $2 \times 2 \times 3 \times 3 \times 3 \times 3$. Grouping them gives $(2 \times 3 \times 3) \times (2 \times 3 \times 3)$, which is $18^2$. Therefore, $\sqrt{324} = 18$. On the other hand, 156 has the prime factorisation $2 \times 2 \times 3 \times 13$. Because the factors cannot be paired up evenly, 156 is not a perfect square.

## Worked example

Imagine you have a square piece of cloth with an area of $125 \, cm^2$. You want to know if you can cut out a square handkerchief with a side length of 15 cm. A handkerchief of side 15 cm would need an area of $15^2 = 225 \, cm^2$, which is more than 125 $cm^2$, so it cannot be cut. To find the largest handkerchief with a whole-number side, note that 125 is not a perfect square. The nearest perfect squares are $11^2 = 121$ and $12^2 = 144$. Since 144 is larger than 125, the side must be less than 12 cm, and since 121 is less than 125, a square of side 11 cm fits. So the largest square handkerchief with a whole-number side has a side length of 11 cm.

## Key points

*   A perfect square is a natural number that can be expressed as $n^2$ for some natural number $n$.
*   The units digit of a perfect square can only be 0, 1, 4, 5, 6, or 9.
*   A natural number is a perfect square if and only if it can be expressed as the sum of successive odd natural numbers starting from 1.
*   The square root of a perfect square $n^2$ is $\pm n$, though we usually consider only the positive root.
*   A number is a perfect square if and only if its prime factors can be divided into two equal groups.