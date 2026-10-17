---
{
  "concept": "LCM and GCD (HCF)",
  "slug": "lcm-and-gcd",
  "grade": 7,
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
    "completion_tokens": 1219,
    "prompt_tokens": 4416,
    "total_tokens": 5635,
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
  "generated_at": "2026-10-11T17:31:44",
  "source_grade": 7,
  "grade_delta": 0,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g7_maths_part2_chapter3_015",
      "chapter": "chapter3",
      "section": "3.2 Least, but not Last!"
    }
  ],
  "citation_check": {
    "cited": [
      "1"
    ],
    "invented_citations": [],
    "unused_sources": [],
    "explanatory_paragraphs_without_a_citation": 5,
    "words": 847,
    "target_words": [
      700,
      1250
    ],
    "untraceable_sections": 1,
    "ok": true,
    "structural_problems": [],
    "verification": {
      "verdict": "spiralled",
      "checks": 1,
      "tokens": 9444
    }
  },
  "terms": [
    "least common multiple",
    "highest common factor",
    "common multiple",
    "prime factorisation",
    "subpart"
  ]
}
---

# LCM and GCD (HCF)

Finding the Least Common Multiple (LCM) and the Greatest Common Divisor, also called the Highest Common Factor (HCF), helps us solve everyday problems where we need to find matching sizes or times. Imagine two friends making decorative torans out of cloth strips. One friend uses strips of 6 cm and the other uses strips of 8 cm. If they both want to make a toran of the exact same length, they need to find a length that works for both. This length must be a multiple of 6 and a multiple of 8 at the same time. The smallest such length is the Lowest Common Multiple (LCM).

## Understanding Common Multiples and the LCM

A multiple of a number is the product of that number and an integer. For example, 6, 12, 18, and 24 are all multiples of 6. Similarly, 8, 16, 24, and 32 are all multiples of 8. When a number appears in both lists of multiples, it is called a common multiple. The Lowest Common Multiple (LCM) of two or more given numbers is the lowest (or smallest or least) of their common multiples.

Consider Anshu, who makes torans using 6 cm strips, and Guna, who uses 8 cm strips. Anshu’s toran lengths could be 6, 12, 18, 24, 30, and so on. Guna’s toran lengths could be 8, 16, 24, 32, 40, and so on. By looking at these lists, we can see that 24 and 48 are common multiples of 6 and 8. Since 24 is the smallest among them, 24 is the length of the shortest toran that both can stitch.

## Finding the LCM Using Prime Factorisation

Listing multiples works well for small numbers, but it becomes difficult for larger numbers. Prime factorisation can simplify the process of finding the LCM. We begin by comparing the prime factorisations of the numbers we are working with.

Every factor of a number is formed by taking a subpart of its prime factorisation. We can use this fact to build the LCM. A common multiple must contain the prime factors of the original numbers as subparts. For example, to find a common multiple of 14 and 35, we need a number that contains $2 \times 7$ as a subpart and $5 \times 7$ as a subpart.

To build the LCM, we identify all the prime factors and find the maximum number of times each of them occurs in either of the factorisations. We then multiply these together to get the LCM.

## Example: Finding the LCM of 96 and 360

Let us apply this rule to find the LCM of 96 and 360. First, we find the prime factorisation of each number.

$96 = 2 \times 2 \times 2 \times 2 \times 2 \times 3$

$360 = 2 \times 2 \times 2 \times 3 \times 3 \times 5$

To build the LCM, we look at each prime factor and choose the highest power that appears in either factorisation. The prime factor 2 occurs three times in 360 and five times in 96, so we choose five occurrences of 2. The prime factor 3 occurs twice in 360 and once in 96, so we choose two occurrences of 3. The prime factor 5 occurs once in 360 and not at all in 96, so we choose one occurrence of 5.

Thus, the LCM of 96 and 360 is $2 \times 2 \times 2 \times 2 \times 2 \times 3 \times 3 \times 5 = 1440$.

## Understanding the HCF

While the LCM is the smallest number that is a multiple of the given numbers, the HCF is the largest number that divides each of the given numbers exactly. The process of finding the HCF by listing out all the factors may get tedious for larger numbers. Prime factorisation can simplify the process of finding the HCF as well.

To find the HCF using prime factorisation, we identify the common prime factors of the given numbers and multiply them together. This gives us the highest number that divides both numbers without leaving a remainder.

## Worked Example

Let us find the HCF of 14 and 35 using prime factorisation.

$14 = 2 \times 7$

$35 = 5 \times 7$

The only common prime factor is 7. Therefore, the HCF of 14 and 35 is 7.

## Key points

* The Lowest Common Multiple (LCM) of two or more given numbers is the lowest of their common multiples.
* A common multiple of two numbers must contain the prime factors of each number as a subpart.
* To find the LCM using prime factorisation, identify all prime factors and choose the maximum number of times each occurs in either factorisation.
* The Highest Common Factor (HCF) is the largest number that divides each of the given numbers exactly.
* Prime factorisation simplifies the process of finding both the LCM and the HCF, especially for larger numbers.