---
{
  "concept": "Estimation and Approximation",
  "slug": "estimation",
  "grade": 6,
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
    "completion_tokens": 1264,
    "prompt_tokens": 4116,
    "total_tokens": 5380,
    "completion_tokens_details": null,
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cached_tokens": 4096
    }
  },
  "target_words": [
    700,
    1250
  ],
  "generated_at": "2026-10-02T19:34:12",
  "source_grade": 7,
  "grade_delta": 1,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g7_maths_part1_chapter1_011",
      "chapter": "chapter1",
      "section": "1.4 Exact and Approximate Values"
    }
  ],
  "citation_check": {
    "cited": [
      "1"
    ],
    "invented_citations": [],
    "unused_sources": [],
    "explanatory_paragraphs_without_a_citation": 1,
    "words": 670,
    "target_words": [
      700,
      1250
    ],
    "untraceable_sections": 0,
    "ok": true,
    "structural_problems": [
      "length: 670 words, under 900"
    ]
  },
  "terms": [
    "estimation",
    "approximation",
    "rounding up",
    "rounding down",
    "nearest thousand",
    "nearest lakh",
    "nearest crore",
    "exact value",
    "actual number"
  ],
  "hand_edited": "2026-10-02: five errors corrected by hand. (1) 29,05,32,481 was rounded to the nearest ten lakh as 29,00,00,000 (should be 29,10,00,000) and to the nearest crore as 30,00,00,000 (should be 29,00,00,000). (2) The page said Roxie's 8,00,000 was closer to the sum 8,82,810; Estu's 9,00,000 is closer. (3) It said Estu's 9,00,000 was closer to the difference 9,73,108; Roxie's 10,00,000 is closer. (4) Rounding a pen's price from 340 to 350 was called 'rounding down'; that is rounding up. (5) 'are shown in a table' referred to a table the page does not contain. Two non-sequitur justifications were also replaced with the actual comparison. Not regenerated; still 670 words against a 900 floor. Grade 6 word band recalibrated from 900-1250 to 700-1250 on 2026-10-02 after two full runs showed the model never reaches 900 for these concepts (see the comment on GRADE_WORDS in build_context.py); this page kept its text and had its recorded band updated to the new standard."
}
---

# Estimation and Approximation

Estimation is a quick way to find a value that is close enough to the real answer. We do this by rounding numbers to make them easier to work with. It helps us check if our final answer makes sense. For example, if you need to buy sweets for a school with 732 people, you do not need the exact number. You can estimate and order 750 sweets instead of 700 to make sure everyone gets one.

## Rounding Up and Rounding Down

Sometimes we round a number up, and sometimes we round it down. Rounding up means the estimated number is more than the actual number. If a school has 732 people including students, teachers, and staff, the principal might order 750 sweets instead of 700 sweets. This is because 732 is closer to 750 than to 700.

Other times, it is better to round down. Rounding down means the estimated number is less than the actual number. If the cost of an item is ₹470, the shopkeeper may say that the cost is around ₹450 instead of saying it is around ₹500.

## Nearest Neighbours

With large numbers, it is useful to know the nearest thousand, lakh, or crore. Take the number 6,72,85,183. Its nearest thousand is 6,72,85,000. Its nearest ten thousand is 6,72,90,000. Its nearest lakh is 6,73,00,000. Its nearest ten lakh is 6,70,00,000. Its nearest crore is 7,00,00,000. Each of these is a different neighbour of the same number, and which one you want depends on how rough an answer is good enough.

You can find the nearest neighbours for other large numbers too. For the number 3,87,69,957, the nearest thousand is 3,87,70,000, and the nearest lakh is 3,88,00,000. For the number 29,05,32,481, the nearest ten lakh is 29,10,00,000, because 5,32,481 is more than half of ten lakh, and the nearest crore is 29,00,00,000, because 5,32,481 is far less than half of a crore.

## Checking Your Answer

Estimation helps us check if our final answer is reasonable. Let us look at two friends, Roxie and Estu, estimating the sum of 4,63,128 and 4,19,682. Roxie says the sum is near 8,00,000 and is more than 8,00,000. Estu says the sum is near 9,00,000 and is less than 9,00,000. The exact sum is 8,82,810, so both of them are right. But Estu's estimate is the closer one: 8,82,810 is only 17,190 away from 9,00,000, while it is 82,810 away from 8,00,000. Rounding each number to the nearest lakh shows why Estu did well. 4,63,128 rounds to 5,00,000 and 4,19,682 rounds to 4,00,000, and 5,00,000 plus 4,00,000 is 9,00,000.

Now let us look at the difference of 14,63,128 and 4,90,020. Roxie says the difference is near 10,00,000 and is less than 10,00,000. Estu says the difference is near 9,00,000 and is more than 9,00,000. The exact difference is 9,73,108, so again both are right. This time it is Roxie who is closer: 9,73,108 is 26,892 away from 10,00,000, while it is 73,108 away from 9,00,000. Rounding to the nearest lakh shows why. 14,63,128 rounds to 15,00,000 and 4,90,020 rounds to 5,00,000, and 15,00,000 minus 5,00,000 is 10,00,000.

Notice that being "near" a round number is not the same as being the closest estimate. Both friends gave true statements each time, but which one was nearer changed from the first problem to the second.

## Worked example

Imagine you are at a shop and you want to buy a notebook for ₹470 and a pen for ₹340. You do not need the exact total to check if you have enough money. Round the price of the notebook down to ₹450, and round the price of the pen up to ₹350. Adding the rounded prices gives ₹800, so you need about ₹800 to buy both items. The exact total is ₹810, so the estimate is very close. Here one price was rounded down and the other up, which is perfectly allowed — you choose whichever neighbour is nearer to each price.

## Key points

*   Estimation is a quick way to find a value that is close enough to the real answer.
*   Rounding up means the estimated number is more than the actual number.
*   Rounding down means the estimated number is less than the actual number.
*   With large numbers, it is useful to know the nearest thousand, lakh, or crore.
*   Estimation helps us check if our final answer is reasonable and makes sense.