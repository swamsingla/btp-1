---
{
  "concept": "Cube Roots",
  "slug": "cube-roots",
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
    "completion_tokens": 948,
    "prompt_tokens": 5269,
    "total_tokens": 6217,
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
  "generated_at": "2026-10-12T21:13:15",
  "source_grade": 8,
  "grade_delta": 0,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g8_maths_part1_chapter1_018",
      "chapter": "chapter1",
      "section": "1.2 Cubic Numbers"
    }
  ],
  "citation_check": {
    "cited": [
      "1"
    ],
    "invented_citations": [],
    "unused_sources": [],
    "explanatory_paragraphs_without_a_citation": 0,
    "words": 635,
    "target_words": [
      950,
      1300
    ],
    "untraceable_sections": 0,
    "ok": true,
    "short": [
      "length: 635 words, under 950"
    ],
    "structural_problems": [
      "notation: '\\sqrt[3]{n^3} = n' writes \\sqrt with no {...} argument -- it parses but renders wrongly",
      "notation: '\\sqrt[3]{64} = \\sqrt[3]{2^3 \\times 2^3} = 2 \\times' writes \\sqrt with no {...} argument -- it parses but renders wrongly",
      "notation: '\\sqrt[3]{729} = 9' writes \\sqrt with no {...} argument -- it parses but renders wrongly",
      "notation: '\\sqrt[3]{y}' writes \\sqrt with no {...} argument -- it parses but renders wrongly",
      "notation: '\\sqrt[3]{n^3} = n' writes \\sqrt with no {...} argument -- it parses but renders wrongly"
    ]
  },
  "terms": [
    "perfect cube",
    "cube",
    "cube root",
    "prime factorisation",
    "prime factors",
    "triplet",
    "exponent"
  ]
}
---

# Cube Roots

A cube root is the inverse operation of finding a perfect cube. If a number multiplied by itself three times gives a specific value, that original number is the cube root. For example, because $2 \times 2 \times 2 = 8$, we know that 2 is the cube root of 8. Understanding cube roots is essential for solving problems involving three-dimensional volumes, as it allows you to find the edge length of a cube when you know its total volume.

## Finding Cube Roots by Prime Factorisation

To determine the cube root of a perfect cube using prime factorisation, you must break the number down into its prime factors. A number is a perfect cube if all of its prime factors can be grouped into sets of three identical numbers, or triplets. If the prime factors cannot be divided into three equal groups, then the number is not a perfect cube. This method relies on the fundamental property that the cube root of a number raised to the third power is the number itself, so $\sqrt[3]{n^3} = n$.

For instance, consider the number 3375. Its prime factorisation is $3 \times 3 \times 3 \times 5 \times 5 \times 5$. Since these factors can be arranged into two groups of three, we can see that $3375 = (3 \times 5)^3 = 15^3$. Therefore, the cube root of 3375 is 15. In contrast, if we take the number 500, its prime factorisation is $2 \times 2 \times 5 \times 5 \times 5$. Because the factors of 2 cannot be split into three identical groups, 500 is not a perfect cube.

## How Cubes and Prime Factors Relate

When you calculate the cube of any number, each of its prime factors appears exactly three times in the result. This consistent pattern makes prime factorisation a reliable tool for finding cube roots. If you know the prime factorisation of a number, you can simply divide the exponents of each prime factor by three to find the cube root. This works because taking the cube root is the exact opposite of cubing a number.

For example, if you want to find the cube root of 64, you first find its prime factorisation, which is $2 \times 2 \times 2 \times 2 \times 2 \times 2$. Since there are six factors of 2, you can group them into two triplets: $(2 \times 2 \times 2) \times (2 \times 2 \times 2)$. This simplifies to $2^3 \times 2^3$, which means $\sqrt[3]{64} = \sqrt[3]{2^3 \times 2^3} = 2 \times 2 = 4$.

## Worked Example

Let us apply this rule to find the cube root of 729. First, we find the prime factorisation of 729. Dividing 729 by 3 repeatedly, we get $3 \times 3 \times 3 \times 3 \times 3 \times 3$. This gives us six factors of 3, which can be grouped into two triplets of $3 \times 3 \times 3$. Therefore, the prime factorisation is $3^3 \times 3^3$. Taking the cube root of each triplet, we get $3 \times 3$, which equals 9. Thus, $\sqrt[3]{729} = 9$.

## Key points

*   A perfect cube is a number obtained by multiplying a number by itself three times, written as $n^3$.
*   The cube root of a number $y$ is the number $x$ such that $x^3 = y$, denoted as $\sqrt[3]{y}$.
*   A number is a perfect cube if its prime factorisation can be split into three identical groups.
*   If the prime factors of a number cannot be divided into three equal groups, the number is not a perfect cube.
*   The cube root of a number raised to the third power is the number itself, so $\sqrt[3]{n^3} = n$.