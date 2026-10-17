---
{
  "concept": "Operations on Integers",
  "slug": "integer-operations",
  "grade": 7,
  "language": "en",
  "subject": "maths",
  "area": "Number Systems",
  "model": "sarvam-105b",
  "settings": {
    "temperature": 0.3,
    "max_tokens": 8000,
    "reasoning_effort": "none"
  },
  "usage": {
    "completion_tokens": 1190,
    "prompt_tokens": 6253,
    "total_tokens": 7443,
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
  "generated_at": "2026-10-12T14:10:55",
  "source_grade": 7,
  "grade_delta": 0,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g7_maths_part2_chapter2_006",
      "chapter": "chapter2",
      "section": "2.2 Multiplication of Integers"
    },
    {
      "ref": "S2",
      "passage_id": "g7_maths_part2_chapter2_014",
      "chapter": "chapter2",
      "section": "2.2 Multiplication of Integers — Figure it Out"
    },
    {
      "ref": "S3",
      "passage_id": "g7_maths_part2_chapter2_015",
      "chapter": "chapter2",
      "section": "2.2 Multiplication of Integers — Figure it Out"
    },
    {
      "ref": "S4",
      "passage_id": "g7_maths_part2_chapter2_019",
      "chapter": "chapter2",
      "section": "2.2 Multiplication of Integers — Figure it Out"
    },
    {
      "ref": "S5",
      "passage_id": "g7_maths_part2_chapter2_038",
      "chapter": "chapter2",
      "section": "2.2 Multiplication of Integers — SUMMARY"
    }
  ],
  "citation_check": {
    "cited": [
      "1",
      "2",
      "3",
      "4"
    ],
    "invented_citations": [],
    "unused_sources": [
      "5"
    ],
    "explanatory_paragraphs_without_a_citation": 0,
    "words": 846,
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
      "tokens": 9369
    }
  },
  "terms": [
    "integers",
    "multiplier",
    "multiplicand",
    "product",
    "commutative property",
    "quotient",
    "dividend",
    "divisor",
    "zero pairs"
  ],
  "hand_edited": "2026-10-12: regenerated from the Grade 7 multiplication section with the Grade 6 page supplied as what the reader already knows; 0% of it repeats that page. Hand audit: 'in Grade 7, you will learn' removed (a page does not tell the reader which class they are in); the worked example was announced as division and multiplication and contains no division; the mining elevator was tagged to the wrong extract; the Key point on Brahmagupta's rules left out two debts; four non-terms removed from the declared terms. All products, quotients and the worked example checked."
}
---

# Operations on Integers

Operations on integers are the basic mathematical actions we perform using positive and negative whole numbers together with zero. You may already know how to add and subtract these numbers. This page shows how to multiply and divide them, using rules for the sign of the answer. Understanding these operations helps you calculate things like exam scores, bank balances, or the movement of a mining elevator.

## Multiplying Integers

When we multiply integers, we are essentially grouping a certain number of tokens together. We can use a bag to represent this. If the multiplier is positive, we place tokens into the bag. If the multiplier is negative, we remove tokens from the bag.

If we multiply a positive number by a negative number, like $4 \times (-2)$, we place 2 negatives into an empty bag 4 times. This gives us 8 negatives, or -8. Similarly, if we have $(-4) \times 2$, we remove 2 positives from the bag 4 times. Since the bag is empty, we must first put in zero pairs, and then remove the positives, leaving us with 8 negatives, which is -8.

What happens when both integers are negative? For $(-4) \times (-2)$, we remove 2 negatives from the bag 4 times. Again, we start with an empty bag and use zero pairs. After removing the negatives 4 times, we are left with 8 positives, or +8.

## Commutative Property of Multiplication

One important rule for multiplying integers is that the order of the numbers does not matter. This is called the commutative property. If you swap the multiplier and the multiplicand, the product remains exactly the same.

For example, $4 \times (-2)$ gives -8. If you swap them to get $(-2) \times 4$, the result is still -8. The magnitude of the product stays the same because it only depends on the sizes of the two numbers.

This rule holds true no matter what the signs are. If both numbers are positive or both are negative, swapping them still gives a positive product. If one number is positive and the other is negative, swapping them still gives a negative product.

In general, for any two integers $a$ and $b$, we can say that $a \times b = b \times a$.

## Brahmagupta's Rules

Long ago, a mathematician named Brahmagupta wrote down rules for multiplying and dividing positive and negative numbers. He used the words fortune (dhana) for positive values and debt (rṇa) for negative values.

His rules state:
- The product or quotient of two fortunes is a fortune.
- The product or quotient of two debts is a fortune.
- The product or quotient of a debt and a fortune is a debt.
- The product or quotient of a fortune and a debt is a debt.

These rules help us figure out the sign of our answer when we multiply or divide integers.

## Dividing Integers

Division of integers follows the exact same sign rules as multiplication. We can figure out a division problem by thinking about what we need to multiply to get our answer.

For example, if we have $(-100) \div 25$, we can ask ourselves what we need to multiply 25 by to get -100. We know that $25 \times (-4) = -100$. Therefore, $(-100) \div 25 = (-4)$.

If we divide two negative numbers, like $(-100) \div (-4)$, we ask what we need to multiply -4 by to get -100. We know that $(-4) \times 25 = -100$. Therefore, $(-100) \div (-4) = 25$.

## Worked example

Let us look at a real-world problem involving multiplication. Imagine an elevator in a mining shaft. The elevator's positions above the ground are represented as positive integers, and positions below the ground are represented as negative integers.

Suppose the elevator starts at ground level, which is 0. It moves down 3 levels, so it is at -3. Then, it makes 4 trips, and each trip moves it down 2 more levels. To find the final position, we calculate $4 \times (-2)$, which equals -8. We add this to the starting position: $(-3) + (-8) = -11$. The elevator is now 11 levels below the ground.

## Key points

- When multiplying integers, the product is positive when both numbers have the same sign, and negative when the signs are different.
- Multiplication is commutative, meaning $a \times b = b \times a$ for any two integers $a$ and $b$.
- Brahmagupta's rules state that multiplying or dividing two fortunes, or two debts, gives a fortune, while multiplying or dividing a fortune and a debt gives a debt.
- When dividing integers, the quotient is positive when both numbers have the same sign, and negative when the signs are different.
- Division can be understood by asking what number must be multiplied by the divisor to get the dividend.