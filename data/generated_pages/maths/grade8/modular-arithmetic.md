---
{
  "concept": "Modular Arithmetic",
  "slug": "modular-arithmetic",
  "grade": 8,
  "language": "en",
  "hand_edited": "2026-10-13: 'a and b are n apart' was wrong -> a-b is a multiple of n; divisibility-by-2 reason was circular; reason for the digit-sum rule for 3 added (10 = 1 mod 3); key point said 'divisible by 10 if last digit is 0 or 5' (false) -> split; '340' no longer called a large number; worked example now includes a 'no' case (340 mod 3 = 1); 'congruent' named. Arithmetic checked by hand: all correct. Verifier verdict 'spiralled'.",
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
    "prompt_tokens": 2171,
    "total_tokens": 3381,
    "completion_tokens_details": {
      "accepted_prediction_tokens": null,
      "audio_tokens": null,
      "reasoning_tokens": 0,
      "rejected_prediction_tokens": null
    },
    "prompt_tokens_details": null
  },
  "target_words": [
    800,
    1300
  ],
  "generated_at": "2026-10-13T22:59:59",
  "source_grade": 7,
  "grade_delta": -1,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g7_maths_part1_chapter4_006",
      "chapter": "chapter4",
      "section": "4.2 Revisiting Arithmetic Expressions"
    },
    {
      "ref": "S2",
      "passage_id": "g7_maths_part2_chapter3_020",
      "chapter": "chapter3",
      "section": "3.3 Patterns, Properties, and a Pretty Procedure!"
    }
  ],
  "citation_check": {
    "cited": [
      "1"
    ],
    "invented_citations": [],
    "unused_sources": [
      "2"
    ],
    "explanatory_paragraphs_without_a_citation": 0,
    "words": 766,
    "target_words": [
      800,
      1300
    ],
    "untraceable_sections": 0,
    "ok": true,
    "structural_problems": [],
    "verification": {
      "verdict": "spiralled",
      "checks": 1,
      "tokens": 9282
    }
  },
  "terms": [
    "modular arithmetic",
    "modulus",
    "clock arithmetic",
    "divisibility",
    "remainder",
    "hcf",
    "lcm",
    "congruence",
    "highest common factor",
    "least common multiple"
  ]
}
---

# Modular Arithmetic

Modular arithmetic is a way to do maths with remainders. It is the maths behind the face of a clock. When we move past 12, we start over at 1. This page shows you how to write modular arithmetic, how it works on a clock, and how you can use it to check if a number is divisible by another number.

## The Rule a ≡ b (mod n)

In modular arithmetic, two numbers are related if they leave the same remainder when you divide them by a chosen number. We write this using the symbol $\equiv$, and we say the two numbers are congruent. The chosen number is called the modulus, written as $n$. The rule is written as $a \equiv b \pmod{n}$.

This means that if you divide $a$ and $b$ by $n$, the remainders are the same. It also means that the difference $a - b$ is a multiple of $n$. For example, $14 \equiv 2 \pmod{12}$. This is because $14$ and $2$ both leave a remainder of $2$ when you divide them by $12$.

## Clock Arithmetic

Clock arithmetic is a simple way to understand modular arithmetic. A clock is a circle with $12$ numbers. After $12$ comes $1$ again. This is exactly how modular arithmetic works.

The modulus of a clock is $12$. If it is $10$ o'clock now and you add $5$ hours, you do not get $15$ o'clock. You get $3$ o'clock. In modular arithmetic, we write $10 + 5 \equiv 3 \pmod{12}$. The $12$ hours on the clock wrap around, just like the numbers in modular arithmetic.

## Divisibility

You can use modular arithmetic to check if a number is divisible by another number. A number is divisible by $n$ if its remainder is $0$. In modular arithmetic, we write this as $a \equiv 0 \pmod{n}$.

To check if a number is divisible by $2$, you only need to look at the last digit. If the last digit is $0$, $2$, $4$, $6$, or $8$, the number is divisible by $2$. This is because any number ending in one of these digits leaves a remainder of $0$ when divided by $2$. The reason is that $10$ is a multiple of $2$, so only the last digit can change the remainder.

To check if a number is divisible by $3$, you add all the digits together. If the sum is divisible by $3$, then the original number is also divisible by $3$. For example, to check if $24$ is divisible by $3$, you add $2 + 4 = 6$. Since $6$ is divisible by $3$, $24$ is also divisible by $3$. This works because $10 \equiv 1 \pmod{3}$, so every place value ($1$, $10$, $100$ and so on) leaves a remainder of $1$ when divided by $3$, and a number leaves the same remainder as the sum of its digits.

To check if a number is divisible by $5$, you look at the last digit. If it is $0$ or $5$, the number is divisible by $5$. This is because any number ending in $0$ or $5$ leaves a remainder of $0$ when divided by $5$.

To check if a number is divisible by $10$, you look at the last digit. If it is $0$, the number is divisible by $10$. This is because any number ending in $0$ leaves a remainder of $0$ when divided by $10$.

## Worked example

Let us use the rules from the previous section to check a number. Consider the number $340$.

First, we check if it is divisible by $2$. The last digit is $0$, which is an even number. So, $340$ is divisible by $2$.

Next, we check if it is divisible by $5$. The last digit is $0$, which means it is divisible by $5$.

Then, we check if it is divisible by $10$. The last digit is $0$, so it is divisible by $10$.

Finally, we check if it is divisible by $3$. We add the digits: $3 + 4 + 0 = 7$. Since $7$ is not divisible by $3$, $340$ is not divisible by $3$. In fact, $340 = 3 \times 113 + 1$, so $340 \equiv 1 \pmod{3}$.

## Key points

* Modular arithmetic is a way to do maths with remainders.
* The rule $a \equiv b \pmod{n}$ means $a$ and $b$ leave the same remainder when divided by $n$.
* Clock arithmetic is an example of modular arithmetic with a modulus of $12$.
* You can use modular arithmetic to check if a number is divisible by $2$, $3$, $5$, or $10$.
* A number is divisible by $2$ if its last digit is even.
* A number is divisible by $5$ if its last digit is $0$ or $5$, and divisible by $10$ if its last digit is $0$.
* To check if a number is divisible by $3$, add all its digits together.