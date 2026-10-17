---
{
  "concept": "Properties of Triangles",
  "slug": "properties-of-triangles",
  "grade": 9,
  "language": "en",
  "subject": "maths",
  "area": "Geometry",
  "model": "sarvam-105b",
  "settings": {
    "temperature": 0.3,
    "max_tokens": 8000,
    "reasoning_effort": "none"
  },
  "usage": {
    "completion_tokens": 1192,
    "prompt_tokens": 6732,
    "total_tokens": 7924,
    "completion_tokens_details": {
      "accepted_prediction_tokens": null,
      "audio_tokens": null,
      "reasoning_tokens": 0,
      "rejected_prediction_tokens": null
    },
    "prompt_tokens_details": null
  },
  "target_words": [
    1000,
    1350
  ],
  "generated_at": "2026-10-17T14:34:32",
  "source_grade": 9,
  "grade_delta": 0,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g9_maths_chapter7_012",
      "chapter": "chapter7",
      "section": "7.4 Some Properties of a Triangle"
    },
    {
      "ref": "S2",
      "passage_id": "g9_maths_chapter7_016",
      "chapter": "chapter7",
      "section": "7.5 Some More Criteria for Congruence of Triangles"
    },
    {
      "ref": "S3",
      "passage_id": "g9_maths_chapter7_000",
      "chapter": "chapter7",
      "section": "7.1 Introduction"
    }
  ],
  "citation_check": {
    "cited": [
      "1",
      "3"
    ],
    "invented_citations": [],
    "unused_sources": [
      "2"
    ],
    "explanatory_paragraphs_without_a_citation": 3,
    "words": 887,
    "target_words": [
      1000,
      1350
    ],
    "untraceable_sections": 0,
    "ok": true,
    "structural_problems": [
      "repeats: 27% of this page is word for word the Grade 7 page"
    ]
  },
  "terms": [
    "triangle inequality",
    "isosceles triangle",
    "angle bisector",
    "perpendicular",
    "asa congruence rule",
    "sas congruence rule",
    "equilateral triangle",
    "vertices"
  ]
}
---

# Properties of Triangles

A triangle is the simplest closed figure made of straight lines, yet it hides some surprisingly strong rules. Instead of just naming its parts, this page asks what must be true once some sides or angles are known. We look at two ideas: which three lengths can form a triangle at all, and how equal sides force equal angles and the other way round. We also prove these facts using congruence, rather than only measuring examples.

## The Triangle Inequality

Not every set of three numbers can be the side lengths of a triangle. For three line segments to form a triangle, the sum of the lengths of any two sides must be greater than the length of the third side. This rule is called the triangle inequality.

Suppose you have three sticks and want a triangular frame. With sticks of 4 cm, 6 cm and 8 cm, we check all three pairs: $4 + 6 = 10 > 8$, $4 + 8 = 12 > 6$, and $6 + 8 = 14 > 4$. Every pair passes, so a triangle exists. With sticks of 2 cm, 3 cm and 10 cm, the pair $2 + 3 = 5$ is less than 10, so the two short sticks cannot reach across; no closed triangle is possible.

The same rule tells us how long a third side can be. If two sides of a triangle are 5 cm and 9 cm, the third side $x$ must satisfy $5 + 9 > x$, so $x < 14$. It must also satisfy $9 < 5 + x$, so $x > 4$. Therefore $4 < x < 14$. A third side of 4 cm would make the three points lie on one straight line, and a side of 14 cm would do the same, so neither forms a triangle.

## Angle-Side Relationships

A very important property of triangles connects the lengths of their sides to the sizes of their angles. If a triangle has two equal sides, then the angles opposite to those equal sides are also equal. This is known as the angle-side relationship. 

Let us say we have an isosceles triangle where two sides are equal. For example, if $\Delta$ ABC has $AB = AC$, then the angles opposite these sides, $\angle B$ and $\angle C$, must be equal. This result can be proved by drawing the bisector of $\angle A$ and letting it intersect the base $BC$ at a point $D$. In $\Delta$ BAD and $\Delta$ CAD, we have $AB = AC$, $\angle BAD = \angle CAD$, and $AD = AD$ (common). By the SAS congruence rule, $\Delta BAD \cong \Delta CAD$, which means $\angle ABD = \angle ACD$, so $\angle B = \angle C$.

This property also tells us something about equilateral triangles. Since all three sides are equal, all three angles must be equal. We know that the sum of the angles in any triangle is $180^{\circ}$. Therefore, if we divide $180^{\circ}$ by three, we find that each angle in an equilateral triangle measures exactly $60^{\circ}$.

## The Converse of the Angle-Side Relationship

Is the converse also true? That is: If two angles of any triangle are equal, can we conclude that the sides opposite to them are also equal? Yes, we can. 

Take a triangle $ABC$ in which $\angle B = \angle C$. Draw the bisector of $\angle A$ so that it meets $BC$ at $D$. Then $\angle BAD = \angle CAD$. Because the angles of a triangle add up to $180^{\circ}$, and $\angle B = \angle C$ and $\angle BAD = \angle CAD$, the third angles are also equal: $\angle ADB = \angle ADC$. In triangles $ABD$ and $ACD$ we now have two pairs of equal angles, and the side $AD$ is common to both and lies between the angles of each pair. By the ASA congruence rule, $\Delta ABD \cong \Delta ACD$. Therefore $AB = AC$.

So the sides opposite to equal angles of a triangle are equal. This is the converse of the previous theorem, and it is the tool to use when you need to prove that a triangle is isosceles.

Together the two results say: in a triangle, two sides are equal exactly when the two angles opposite to them are equal.

## Worked Example

Let us apply these results to a problem. Suppose we have a triangle $ABC$ where the bisector $AD$ of $\angle A$ is perpendicular to side $BC$. We need to show that $AB = AC$ and that $\Delta ABC$ is an isosceles triangle.

We can prove this by considering $\Delta ABD$ and $\Delta ACD$. In these two triangles, we have $\angle BAD = \angle CAD$ (since $AD$ is the bisector), $AD = AD$ (common), and $\angle ADB = \angle ADC = 90^{\circ}$. By the ASA congruence rule, $\Delta ABD \cong \Delta ACD$. Therefore, $AB = AC$, which means $\Delta ABC$ is an isosceles triangle.

## Two More Examples with Numbers

**Finding angles.** In an isosceles triangle $ABC$ with $AB = AC$, the angle at the top is $\angle A = 40^{\circ}$. The angles opposite the equal sides are equal, so $\angle B = \angle C$. The three angles add up to $180^{\circ}$, so $\angle B + \angle C = 180^{\circ} - 40^{\circ} = 140^{\circ}$. Hence $\angle B = \angle C = 70^{\circ}$.

**Using the converse with algebra.** In triangle $PQR$, $\angle Q = (3x + 10)^{\circ}$ and $\angle R = (5x - 20)^{\circ}$, and we are told that $PQ = PR$. The angles opposite the equal sides $PR$ and $PQ$ are $\angle Q$ and $\angle R$, so they are equal: $3x + 10 = 5x - 20$. This gives $30 = 2x$ and $x = 15$. Then $\angle Q = 3(15) + 10 = 55^{\circ}$ and $\angle R = 5(15) - 20 = 55^{\circ}$. The angle at $P$ is $180^{\circ} - 55^{\circ} - 55^{\circ} = 70^{\circ}$.

## Key points

*   The sum of the lengths of any two sides of a triangle must be greater than the length of the third side (triangle inequality).
*   If a triangle has two equal sides, the angles opposite those sides are equal.
*   If two angles of a triangle are equal, the sides opposite to them are also equal.
*   In an equilateral triangle, all three sides are equal, so all three angles are equal to $60^{\circ}$.
*   If the bisector of an angle in a triangle is perpendicular to the opposite side, the triangle is isosceles.