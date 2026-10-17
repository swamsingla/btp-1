---
{
  "concept": "Square Roots",
  "slug": "square-roots",
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
    "completion_tokens": 1404,
    "prompt_tokens": 5808,
    "total_tokens": 7212,
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
  "generated_at": "2026-10-12T21:11:25",
  "source_grade": 8,
  "grade_delta": 0,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g8_maths_part1_chapter1_010",
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
    "words": 791,
    "target_words": [
      950,
      1300
    ],
    "untraceable_sections": 0,
    "ok": true,
    "short": [
      "length: 791 words, under 950"
    ],
    "structural_problems": [],
    "verification": {
      "verdict": "spiralled",
      "checks": 1,
      "tokens": 9496
    }
  },
  "terms": [
    "square root",
    "perfect square",
    "prime factorisation",
    "square numbers",
    "long division"
  ],
  "hand_edited": "2026-10-12: second line-by-line audit against the textbook, edited directly: added the check 44 x 44 = 1936 and the estimation of the root of 250. 2026-10-12: hand audit: section heading said long division but the section teaches estimation."
}
---

# Square Roots

Square roots are the inverse operation of squaring a number. If you know the area of a square, finding the square root gives you the length of its side. This is a very useful skill when you are working with geometry, measuring areas, or solving equations.

## What is a Square Root?

A square root of a number is a value that, when multiplied by itself, gives the original number. For example, the area of a square is 49 sq. cm. The length of its side is 7 cm because $7 \times 7 = 49$. We call 7 the square root of 49. In general, if $y = x^{2}$, then $x$ is the square root of $y$.

Every perfect square has two integer square roots. One is positive and the other is negative. For example, $8^{2} = 64$ and $(-8)^{2} = 64$. The square root of a number is denoted by the symbol $\sqrt{}$. Thus, $\sqrt{64} = \pm 8$ and $\sqrt{100} = \pm 10$. Note that $\sqrt{8^2} = \pm 8$ and $\sqrt{10^2} = \pm 10$. In general, $\sqrt{n^2} = \pm n$. In this chapter, we shall only consider the positive square root.

## Finding Square Roots by Prime Factorisation

We know that a perfect square is obtained by multiplying an integer by itself. Looking at a number's prime factorisation can help us determine whether it is a perfect square. If we can divide the prime factors of a number into two equal groups, then the product of the prime factors in either group combine to form the square root.

We can write the prime factors in pairs. If all the prime factors can be paired up perfectly, the number is a perfect square.

Consider the number 324. Its prime factorisation is $2 \times 2 \times 3 \times 3 \times 3 \times 3$. We can group these factors into pairs. This gives $324 = (2 \times 3 \times 3) \times (2 \times 3 \times 3)$. This shows that 324 is a perfect square. Therefore, $324 = (2 \times 3 \times 3)^{2} = 18^{2}$. The square root of 324 is 18.

Now consider the number 156. The prime factorisation of 156 is $2 \times 2 \times 3 \times 13$. We cannot pair up these factors perfectly. Therefore, 156 is not a perfect square.

## Finding Square Roots by Estimation

For larger numbers, prime factorisation can be difficult. We can estimate the square root by looking at the closest perfect squares we are familiar with. For example, to find $\sqrt{1936}$, we can reason as follows. First, 1936 is between 1600 ($40^{2}$) and 2500 ($50^{2}$). So, 40 is less than $\sqrt{1936}$ which is less than 50.

Second, the last digit of 1936 is 6. So, the last digit of the square root must either be 4 or 6. It can be 44 or 46.

Third, we can calculate $45^{2}$ to compare it with 1936. We can write $45^{2}$ as $(40 + 5)(40 + 5) = 40^{2} + 2 \times 40 \times 5 + 5^{2} = 1600 + 400 + 25 = 2025$.

Fourth, 2025 is greater than 1936. So, 40 is less than $\sqrt{1936}$ which is less than 45.

From the observation in the second point, we can guess and then verify that $\sqrt{1936}$ is 44. Check: $44 \times 44 = 1936$.

## When the Number Is Not a Perfect Square

Suppose we want $\sqrt{250}$. Since 250 is not a perfect square, we can only estimate. We know that $100 < 250 < 400$, and $\sqrt{100} = 10$ and $\sqrt{400} = 20$, so $10 < \sqrt{250} < 20$. To get closer, we use $15^{2} = 225$ and $16^{2} = 256$. Therefore $15 < \sqrt{250} < 16$. Since 256 is much closer to 250 than 225 is, $\sqrt{250}$ is approximately 16, though a little less than 16.

## Worked example

Let us find the square root of 1156 using prime factorisation. First, we find the prime factors of 1156. We can divide 1156 by 2 to get 578. Dividing by 2 again gives 289. The number 289 is $17 \times 17$. So, the prime factorisation of 1156 is $2 \times 2 \times 17 \times 17$.

We can pair up these factors. This gives $1156 = (2 \times 17) \times (2 \times 17)$. This shows that 1156 is a perfect square. Therefore, $1156 = 34^{2}$. The square root of 1156 is 34.

## Key points
* A square root of a number is a value that, when multiplied by itself, gives the original number.
* The square root of a number is denoted by the symbol $\sqrt{}$.
* A perfect square is a number whose prime factors can be grouped into two equal groups.
* If a number ends with 2, 3, 7, or 8, then we can definitely say that it is not a square.
* We can estimate the square root of a larger perfect square by looking at the closest perfect squares we are familiar with.