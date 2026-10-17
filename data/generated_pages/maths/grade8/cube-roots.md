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
    "completion_tokens": 925,
    "prompt_tokens": 5269,
    "total_tokens": 6194,
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
  "generated_at": "2026-10-12T21:13:22",
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
    "explanatory_paragraphs_without_a_citation": 1,
    "words": 615,
    "target_words": [
      950,
      1300
    ],
    "untraceable_sections": 0,
    "ok": true,
    "short": [
      "length: 615 words, under 950"
    ],
    "structural_problems": [],
    "verification": {
      "verdict": "spiralled",
      "checks": 1,
      "tokens": 9166
    }
  },
  "terms": [
    "cube roots",
    "perfect cubes",
    "prime factorisation",
    "triplets"
  ],
  "hand_edited": "2026-10-12: second line-by-line audit against the textbook, edited directly: proper definition and notation of the cube root, exact prime-factor definition, triplet wording for 3375, the cube's prime-factor observation. 2026-10-12: hand audit: worked example grouped 729 into two groups of three 3s (which gives a square, 27 x 27) and then wrote 9^3; regrouped into three groups of (3 x 3)."
}
---

# Cube Roots

If $y = x^3$, then $x$ is the cube root of $y$, written $x = \sqrt[3]{y}$. For example, $8 = 2 \times 2 \times 2 = 2^3$, so $\sqrt[3]{8} = 2$. In the same way $\sqrt[3]{27} = 3$, and in general $\sqrt[3]{n^3} = n$. Finding cube roots is the exact opposite of finding a perfect cube, and it is a useful skill for solving many types of maths problems.

## The Concept of Perfect Cubes

Before you can find a cube root, you need to know what a perfect cube is. A perfect cube is a number that you get by multiplying a number by itself three times. For instance, $1 = 1 \times 1 \times 1$, $8 = 2 \times 2 \times 2$, and $27 = 3 \times 3 \times 3$ are all perfect cubes. 

If a number is not a perfect cube, it does not have a whole number as its cube root. For example, 9 is not a perfect cube because $2 \times 2 \times 2 = 8$ and $3 \times 3 \times 3 = 27$. Therefore, 9 cannot be expressed as a number multiplied by itself three times.

## Prime Factorisation

To find the cube root of a larger number, you can use prime factorisation. This method involves breaking a number down into its prime factors. A prime factor is a prime number (one divisible only by 1 and itself) that divides the number. To find the cube root, you need to group these prime factors into sets of three identical numbers. If all the prime factors can be grouped into triplets, then the number is a perfect cube.

For example, let's check if 3375 is a perfect cube. First, we find its prime factors: $3375 = 3 \times 3 \times 3 \times 5 \times 5 \times 5$. We can group these factors into three identical groups of $(3 \times 5)$. This means $3375 = (3 \times 5) \times (3 \times 5) \times (3 \times 5) = 15 \times 15 \times 15 = 15^3$.

## Using Prime Factorisation to Find Cube Roots

Once you have the prime factorisation of a number, you can find its cube root by taking one factor from each triplet. In the case of 3375, the factors can also be grouped into triplets: $3375 = (3 \times 3 \times 3) \times (5 \times 5 \times 5) = 3^3 \times 5^3$. Taking one factor from each triplet gives us $3 \times 5 = 15$. Therefore, the cube root of 3375 is 15.

If a number cannot be grouped into triplets, then it is not a perfect cube. For example, let's check 500. Its prime factorisation is $500 = 2 \times 2 \times 5 \times 5 \times 5$. We have two 2s and three 5s. Since we cannot group the 2s into a triplet, 500 is not a perfect cube.

Observe that each prime factor of a number appears three times in the prime factorisation of its cube. For example, $15 = 3 \times 5$ and $15^3 = 3375 = 3^3 \times 5^3$.

## Worked example

Let's find the cube root of 729 using prime factorisation. First, we break down 729 into its prime factors. We can see that $729 = 3 \times 3 \times 3 \times 3 \times 3 \times 3$. We can group these factors into three identical groups of $(3 \times 3)$. This means $729 = (3 \times 3) \times (3 \times 3) \times (3 \times 3) = 9 \times 9 \times 9 = 9^3$. In triplets, $729 = (3 \times 3 \times 3) \times (3 \times 3 \times 3) = 3^3 \times 3^3$, and one factor from each triplet gives $3 \times 3 = 9$. Therefore, the cube root of 729 is 9.

## Key points
*   A perfect cube is a number that can be expressed as $n \times n \times n$ or $n^3$.
*   To find the cube root of a number, you can use prime factorisation.
*   Group the prime factors into sets of three identical numbers.
*   If all the prime factors can be grouped into triplets, then the number is a perfect cube.
*   The cube root is the product of one factor from each triplet.