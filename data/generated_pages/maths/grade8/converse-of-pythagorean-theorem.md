---
{
  "concept": "Converse of Pythagorean Theorem",
  "slug": "converse-of-pythagorean-theorem",
  "grade": 8,
  "language": "en",
  "hand_edited": "2026-10-13: line-by-line hand audit against the source passages, edited directly (tagged copy; published body rebuilt from it): the source (Grade 9 mid-point theorem and congruence criteria) never mentions the Pythagorean Theorem, so every [S1] tag on the page was false and was removed; the page also said the hypotenuse is 'the side opposite the right angle' while using that to prove the triangle has a right angle (circular); replaced the redundant 'Why the Hypotenuse Matters' section with the standard proof of the converse using the SSS congruence rule, which the source does state [S2]; added a non-right example; removed the claim that carpenters and builders 'use this rule' as a sourced fact",
  "subject": "maths",
  "area": "Geometry",
  "model": "sarvam-105b",
  "settings": {
    "temperature": 0.3,
    "max_tokens": 8000,
    "reasoning_effort": "none"
  },
  "usage": {
    "completion_tokens": 1051,
    "prompt_tokens": 5029,
    "total_tokens": 6080,
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
  "generated_at": "2026-10-13T02:07:22",
  "source_grade": 9,
  "grade_delta": 1,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g9_maths_chapter8_009",
      "chapter": "chapter8",
      "section": "8.2 The Mid-point Theorem"
    },
    {
      "ref": "S2",
      "passage_id": "g9_maths_chapter7_017",
      "chapter": "chapter7",
      "section": "7.5 Some More Criteria for Congruence of Triangles"
    },
    {
      "ref": "S3",
      "passage_id": "g9_maths_chapter9_014",
      "chapter": "chapter9",
      "section": "9.4 Angle Subtended by an Arc of a Circle"
    }
  ],
  "citation_check": {
    "cited": [
      "1"
    ],
    "invented_citations": [],
    "unused_sources": [
      "2",
      "3"
    ],
    "explanatory_paragraphs_without_a_citation": 0,
    "words": 690,
    "target_words": [
      950,
      1300
    ],
    "untraceable_sections": 0,
    "ok": true,
    "short": [
      "length: 690 words, under 950"
    ],
    "structural_problems": [],
    "verification": {
      "verdict": "ok",
      "checks": 1,
      "tokens": 1189
    }
  },
  "terms": [
    "converse of pythagorean theorem",
    "hypotenuse",
    "right-angled triangle",
    "base",
    "perpendicular",
    "square of a number"
  ]
}
---

# Converse of Pythagorean Theorem

You may already know the Pythagorean Theorem. It tells you that if a triangle is right-angled, with the longest side $c$ opposite the right angle and the other two sides $a$ and $b$, then $a^2 + b^2 = c^2$. The converse of the Pythagorean Theorem turns this statement around. It says that if you measure the sides of a triangle and find that $a^2 + b^2 = c^2$, where $c$ is the longest side, then the triangle is right-angled. This is useful in everyday life. For example, a carpenter or builder can measure the three sides of a triangular frame and check this equation to find out whether a corner is a perfect right angle.

## What the Converse States

The converse of the Pythagorean Theorem is a rule about triangles. It tells you how to identify a right-angled triangle just by measuring its sides. Suppose a triangle has sides $a$, $b$ and $c$, and $c$ is the longest side. If $a^2 + b^2 = c^2$, then the triangle is right-angled, and the right angle is the angle opposite the side $c$. In a right-angled triangle, the longest side, opposite the right angle, is called the hypotenuse.

## Why the Converse Is True

Take a triangle ABC with sides $a$, $b$ and $c$ such that $a^2 + b^2 = c^2$. Now draw a different triangle PQR that has a right angle at Q, with the two sides next to the right angle equal to $a$ and $b$. By the Pythagorean Theorem, the hypotenuse PR of this right-angled triangle satisfies $PR^2 = a^2 + b^2$. But $a^2 + b^2 = c^2$, so $PR^2 = c^2$, which means $PR = c$.

Now the two triangles have all three sides equal in pairs: $a$ and $a$, $b$ and $b$, $c$ and $c$. If three sides of one triangle are equal to the three sides of another triangle, then the two triangles are congruent. So triangle ABC is congruent to triangle PQR, and the angle of triangle ABC opposite the side $c$ is equal to the right angle at Q. Hence triangle ABC is right-angled.

## How to Use the Rule

You can use the converse to check whether a triangle is right-angled. First, identify the longest side. This is your $c$. The other two sides are $a$ and $b$. Next, square the lengths of $a$ and $b$ and add these two squares together. Then square the length of $c$. If the two results are equal, the triangle is right-angled. If they are not equal, the triangle is not right-angled. It is important to choose the longest side as $c$, because the check is made against the longest side.

## Worked Example

Imagine a carpenter is building a triangular frame for a window. The lengths of the sides are $6$ cm, $8$ cm and $10$ cm. The carpenter wants to know whether the corner opposite the longest side is a perfect right angle.

The longest side is $10$ cm, so $c = 10$. The other two sides are $6$ cm and $8$ cm, so $a = 6$ and $b = 8$.
- $a^2 = 6 \times 6 = 36$
- $b^2 = 8 \times 8 = 64$
- $a^2 + b^2 = 36 + 64 = 100$
- $c^2 = 10 \times 10 = 100$

Since $a^2 + b^2 = c^2$, the triangle is right-angled.

Now consider a triangle with sides $5$ cm, $6$ cm and $8$ cm. The longest side is $8$ cm, so $c = 8$. Then $5^2 + 6^2 = 25 + 36 = 61$, while $8^2 = 64$. Since $61 \neq 64$, this triangle is not right-angled.

## Key points
- The converse of the Pythagorean Theorem states that if $a^2 + b^2 = c^2$, where $c$ is the longest side, then the triangle is right-angled.
- The right angle is opposite the longest side, which is the hypotenuse.
- To check a triangle, square the two shorter sides, add them, and compare the sum with the square of the longest side.
- If the sum is not equal to the square of the longest side, the triangle is not right-angled.
- The converse can be proved using the rule that two triangles with three pairs of equal sides are congruent.
