---
{
  "concept": "Cube Numbers",
  "slug": "cube-numbers",
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
    "completion_tokens": 819,
    "prompt_tokens": 5693,
    "total_tokens": 6512,
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
  "generated_at": "2026-10-12T21:52:56",
  "source_grade": 8,
  "grade_delta": 0,
  "hand_edited": "2026-10-12: this page was held back by the automated checks (no key-points section, no [S#] citations). Published after a line-by-line hand audit against the textbook, edited directly: added the key points, the triplet form for 3375, the cube-roots notation and the odd-number pattern, natural number in place of integer, the taxicab story detail.",
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g8_maths_part1_chapter1_014",
      "chapter": "chapter1",
      "section": "1.2 Cubic Numbers"
    },
    {
      "ref": "S2",
      "passage_id": "g8_maths_part2_chapter2_019",
      "chapter": "chapter2",
      "section": "2.6 A Long-Standing Open Problem"
    }
  ],
  "citation_check": {
    "cited": [],
    "invented_citations": [],
    "unused_sources": [
      "1",
      "2"
    ],
    "explanatory_paragraphs_without_a_citation": 3,
    "words": 527,
    "target_words": [
      950,
      1300
    ],
    "untraceable_sections": 3,
    "ok": false,
    "structural_problems": [
      "sections: no 'key points' section",
      "notation: 'x = \\sqrt[3]{y}' writes \\sqrt with no {...} argument -- it parses but renders wrongly",
      "notation: '\\sqrt[3]{8} = 2' writes \\sqrt with no {...} argument -- it parses but renders wrongly"
    ]
  },
  "terms": [
    "perfect cube",
    "cube root",
    "prime factorisation",
    "taxicab number",
    "exponent"
  ]
}
---

# Cube Numbers

A cube number is the result of multiplying a number by itself three times. For example, $2 \times 2 \times 2 = 8$. We write this as $2^3$, where 2 is the base and 3 is the exponent. These are called perfect cubes. Understanding cube numbers is useful when you are calculating the volume of a three-dimensional object, like a box or a room.

## What is a Perfect Cube?

A perfect cube is a number that can be written as $n \times n \times n$, or $n^3$, for some natural number $n$. The numbers 1, 8, 27, 64, and 125 are perfect cubes because they are the results of $1^3$, $2^3$, $3^3$, $4^3$, and $5^3$. If you try to find a number between 8 and 27 that is a perfect cube, you will not find one. This is because $2^3 = 8$ and $3^3 = 27$, leaving no natural number $n$ to produce a number in between.

Cubes also come from consecutive odd numbers: $1 = 1^3$, $3 + 5 = 8 = 2^3$, $7 + 9 + 11 = 27 = 3^3$, and $13 + 15 + 17 + 19 = 64 = 4^3$.

## The Cube Root

The cube root of a number is the value that, when multiplied by itself three times, gives the original number. If $y = x^3$, then $x$ is the cube root of $y$. We denote this by $x = \sqrt[3]{y}$. For instance, since $8 = 2^3$, the cube root of 8 is 2. This means $\sqrt[3]{8} = 2$. In the same way $\sqrt[3]{27} = 3$ and $\sqrt[3]{1000} = 10$, and in general $\sqrt[3]{n^3} = n$.

## Prime Factorisation of Cubes

You can check if a number is a perfect cube by looking at its prime factors. A number is a perfect cube if all its prime factors can be grouped into sets of three identical numbers. For example, consider the number 3375. Its prime factorisation is $3 \times 3 \times 3 \times 5 \times 5 \times 5$. Since the factors can be split into three groups of $(3 \times 5)$, we know that 3375 is a perfect cube. It can be written as $(3 \times 5)^3 = 15^3$. Grouped as triplets, $3375 = (3 \times 3 \times 3) \times (5 \times 5 \times 5) = 3^3 \times 5^3$, so the cube root of 3375 is $3 \times 5 = 15$.

## Worked Example

Let's check if 500 is a perfect cube using prime factorisation. First, we find the prime factors of 500. They are $2 \times 2 \times 5 \times 5 \times 5$. To be a perfect cube, the factors must be split into three identical groups. Here, we have two 2s and three 5s. Since the factors cannot be split into three identical groups, 500 is not a perfect cube.

## Taxicab Numbers

A taxicab number is a special number that can be expressed as the sum of two perfect cubes in two different ways. The smallest taxicab number is 1729. This number is famous because of a story involving the mathematicians Srinivasa Ramanujan and G. H. Hardy. Hardy had ridden in a taxicab numbered 1729 and remarked that it was a rather dull number. Ramanujan immediately replied that it was very interesting because it is the smallest number that can be written as the sum of two cubes in two different ways.

The two ways to express 1729 as a sum of two cubes are:
$$1729 = 1^3 + 12^3$$
$$1729 = 9^3 + 10^3$$

Because of this story, 1729 has since been known as the Hardy-Ramanujan Number. The next two taxicab numbers after 1729 are 4104 and 13832.

## Key points

*   A cube number is obtained by multiplying a natural number by itself three times: $n^3 = n \times n \times n$. These numbers are called perfect cubes.
*   If $y = x^3$, then $x$ is the cube root of $y$, written $x = \sqrt[3]{y}$.
*   A number is a perfect cube if its prime factors can be grouped into triplets of identical factors. The cube root is the product of one factor from each triplet.
*   1729 is the smallest number that is a sum of two cubes in two different ways: $1^3 + 12^3 = 9^3 + 10^3$.