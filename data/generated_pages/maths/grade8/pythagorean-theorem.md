---
{
  "concept": "Pythagorean Theorem",
  "slug": "pythagorean-theorem",
  "grade": 8,
  "language": "en",
  "prior_knowledge_fix": "2026-10-13: removed or rewrote an unsupported claim about what the student has already studied; edited directly in the tagged copy and the published copy",
  "subject": "maths",
  "area": "Geometry",
  "model": "sarvam-105b",
  "settings": {
    "temperature": 0.3,
    "max_tokens": 8000,
    "reasoning_effort": "none"
  },
  "usage": {
    "completion_tokens": 1347,
    "prompt_tokens": 6044,
    "total_tokens": 7391,
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
  "generated_at": "2026-10-12T21:48:44",
  "source_grade": 8,
  "grade_delta": 0,
  "hand_edited": "2026-10-12: line-by-line hand audit against the textbook, edited directly: removed the claim that the theorem tests for right angles (that is the converse), removed unsourced claims about irrationality and trigonometry attributed to the theorem and replaced them with the textbook's bounds on root 2, added the Baudhayana attribution and the Lilavati source, the stem-is-vertical assumption.",
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g8_maths_part2_chapter2_021",
      "chapter": "chapter2",
      "section": "2.7 Further Applications of the Baudhāyana-Pythagoras Theorem"
    },
    {
      "ref": "S2",
      "passage_id": "g8_maths_part2_chapter2_011",
      "chapter": "chapter2",
      "section": "2.4 Combining Two Different Squares"
    },
    {
      "ref": "S3",
      "passage_id": "g8_maths_part2_chapter2_004",
      "chapter": "chapter2",
      "section": "2.3 Hypotenuse of an Isosceles Right Triangle"
    }
  ],
  "citation_check": {
    "cited": [
      "1",
      "2",
      "3"
    ],
    "invented_citations": [],
    "unused_sources": [],
    "explanatory_paragraphs_without_a_citation": 1,
    "words": 960,
    "target_words": [
      950,
      1300
    ],
    "untraceable_sections": 0,
    "ok": true,
    "structural_problems": [],
    "verification": {
      "verdict": "ok",
      "checks": 1,
      "tokens": 1806
    }
  },
  "terms": [
    "hypotenuse",
    "right-angled triangle",
    "pythagorean theorem",
    "isosceles right triangle",
    "square root",
    "area of a square"
  ]
}
---

# Pythagorean Theorem

The Pythagorean theorem is one of the most important rules in geometry. It tells us exactly how the three sides of a right-angled triangle are related. This rule is so useful that we can use it to solve everyday puzzles, like finding the depth of a lake.

## The Rule for Right-Angled Triangles

A right-angled triangle is a triangle that has one angle exactly equal to 90 degrees. The side opposite this right angle is the longest side. This longest side is called the hypotenuse. The other two sides are called the shorter sides or legs. The Pythagorean theorem says that if the lengths of the two shorter sides are $a$ and $b$, and the length of the hypotenuse is $c$, then $a^2 + b^2 = c^2$. 

This means that if you square the lengths of the two shorter sides, and add those results together, you get the square of the hypotenuse. For example, if a triangle has shorter sides of 3 cm and 4 cm, you can find the hypotenuse. You calculate $3^2 + 4^2 = 9 + 16 = 25$. Since $25 = 5^2$, the hypotenuse must be exactly 5 cm. 

The theorem is also called Baudhāyana's theorem, after the Indian mathematician Baudhāyana, who stated it in this general form. It is named after Pythagoras (c. 500 BCE) too, who studied it a couple of hundred years after Baudhāyana, and it is often called the Baudhāyana-Pythagoras theorem.

## A Real-World Puzzle

You can use this theorem to solve problems that look impossible at first. This one comes from Bhāskarāchārya's Līlāvatī. Imagine a lotus flower growing in a lake. The tip of its stem sticks 1 unit above the water. A gentle breeze sways the flower, and the tip touches the water 3 units away from where it started. How deep is the lake?

To solve this, we need to find the length of the stem underwater. Let us call this length $x$. The total length of the stem is $x + 1$. We assume the stem was standing straight up before the breeze, so it forms a right angle with the water. This creates a right triangle. The two shorter sides of this triangle are 3 and $x$. The hypotenuse is the total length of the stem, which is $x + 1$. 

Using the theorem, we set up the equation $3^2 + x^2 = (x + 1)^2$. This simplifies to $9 + x^2 = x^2 + 2x + 1$. If we subtract $x^2$ from both sides, we get $9 = 2x + 1$. Solving this gives $x = 4$. So, the depth of the lake is 4 units.

## Combining Different Squares

The theorem is not just a random rule; it has a deep connection to area. Take two identical squares of side $a$. Cut each along a diagonal, and the four triangles can be rearranged to form one larger square. The side of this new square is the diagonal of the old squares. The Pythagorean theorem explains why this works: the diagonal $d$ satisfies $d^2 = a^2 + a^2 = 2a^2$, which is exactly the total area of the two old squares.

But what if you want to combine two squares of completely different sizes? The theorem provides the answer. If you draw a right-angled triangle using the side lengths of the two smaller squares, the hypotenuse of that triangle will be the side length of a new, larger square. The area of this new square is exactly equal to the sum of the areas of the two smaller squares. 

For instance, if you have two squares with sides of length 3 and 4, the theorem guarantees that a square built on the hypotenuse of a 3-4-5 triangle will have an area of $3^2 + 4^2 = 25$. You can actually prove this by cutting the two smaller squares into pieces and rearranging them to cover the larger square perfectly.

## Special Cases and Triangles

The theorem also helps us understand triangles that are not just any right-angled triangle. For example, consider an isosceles right-angled triangle. This means the two shorter sides are exactly the same length. If each of these sides is 1 unit, the theorem tells us that the hypotenuse squared equals $1^2 + 1^2 = 2$. Therefore, the hypotenuse is $\sqrt{2}$ units long. 

We cannot write $\sqrt{2}$ exactly as a short decimal, but we can trap it between bounds. Since $1^2 = 1$ and $2^2 = 4$, we get $1 < \sqrt{2} < 2$. Since $1.41^2 = 1.9881$ and $1.42^2 = 2.0164$, we get $1.41 < \sqrt{2} < 1.42$. Since $1.414^2 = 1.999396$ and $1.415^2 = 2.002225$, we get $1.414 < \sqrt{2} < 1.415$.

## Worked example

Let us apply the rule to find the missing side of a right-angled triangle. Suppose you have a triangle where one shorter side is 6 cm and the hypotenuse is 10 cm. You need to find the length of the other shorter side.

Let us call the unknown side $a$. The known shorter side is $b = 6$, and the hypotenuse is $c = 10$. We use the formula $a^2 + b^2 = c^2$. Substituting the known values, we get $a^2 + 6^2 = 10^2$. This simplifies to $a^2 + 36 = 100$. Subtracting 36 from both sides gives $a^2 = 64$. Taking the square root of 64, we find that $a = 8$. So, the missing side is exactly 8 cm long.

## Key points
*   The Pythagorean theorem applies only to right-angled triangles, where $a^2 + b^2 = c^2$.
*   The side $c$ is always the hypotenuse, which is the side opposite the right angle.
*   You can use the theorem to find a missing side length if you know the other two side lengths.
*   The theorem connects the areas of squares drawn on the sides of a right triangle.
*   The hypotenuse of a right triangle whose two shorter sides are both 1 unit long is $\sqrt{2}$ units, and $1.414 < \sqrt{2} < 1.415$.