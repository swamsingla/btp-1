---
{
  "concept": "Properties of Parallelogram",
  "slug": "properties-of-parallelogram",
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
    "completion_tokens": 966,
    "prompt_tokens": 8107,
    "total_tokens": 9073,
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
  "generated_at": "2026-10-17T14:34:20",
  "source_grade": 9,
  "grade_delta": 0,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g9_maths_chapter8_002",
      "chapter": "chapter8",
      "section": "8.1 Properties of a Parallelogram"
    },
    {
      "ref": "S2",
      "passage_id": "g9_maths_chapter7_013",
      "chapter": "chapter7",
      "section": "7.4 Some Properties of a Triangle"
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
    "explanatory_paragraphs_without_a_citation": 1,
    "words": 689,
    "target_words": [
      1000,
      1350
    ],
    "untraceable_sections": 0,
    "ok": true,
    "structural_problems": [
      "length: 689 words, under 1000"
    ]
  },
  "terms": [
    "parallelogram",
    "diagonal",
    "bisect",
    "congruent",
    "alternate angles",
    "transversal",
    "quadrilateral",
    "converse",
    "midpoint"
  ]
}
---

# Properties of Parallelogram

A parallelogram is a quadrilateral with two pairs of parallel sides. In Grade 8, you learned that opposite sides, opposite angles, and adjacent angles have specific relationships within this shape. This page builds on that foundation by exploring the deeper properties of the diagonals and the converse theorems, which allow you to prove that a given quadrilateral is a parallelogram.

## Diagonals Bisect Each Other

One of the most important properties of a parallelogram is how its diagonals interact. If you draw a parallelogram and measure the segments of its diagonals, you will find that they cut each other exactly in half.

A theorem states that the diagonals of a parallelogram bisect each other. This means the point where the two diagonals intersect is the midpoint of both diagonals. If the diagonals intersect at a point $O$, then $OA = OC$ and $OB = OD$.

The converse of this theorem is also true: if the diagonals of a quadrilateral bisect each other, then it is a parallelogram.

Here is why the first theorem holds. Let the diagonals $AC$ and $BD$ of parallelogram $ABCD$ meet at $O$. Look at triangles $AOB$ and $COD$. Since $AB \parallel DC$ and $AC$ is a transversal, $\angle OAB = \angle OCD$ (alternate angles). Since $BD$ is also a transversal, $\angle OBA = \angle ODC$ (alternate angles). Also $AB = DC$, because opposite sides of a parallelogram are equal. So $\Delta AOB \cong \Delta COD$ by the ASA rule. By corresponding parts of congruent triangles, $OA = OC$ and $OB = OD$.

For the converse, suppose $OA = OC$ and $OB = OD$. In triangles $AOB$ and $COD$, we have $OA = OC$, $OB = OD$, and $\angle AOB = \angle COD$ (vertically opposite angles). So $\Delta AOB \cong \Delta COD$ by the SAS rule, and then $\angle OAB = \angle OCD$. These are alternate angles for lines $AB$ and $DC$ cut by the transversal $AC$, so $AB \parallel DC$. In the same way, the triangles $AOD$ and $COB$ are congruent, which gives $AD \parallel BC$. Both pairs of opposite sides are parallel, so the quadrilateral is a parallelogram.

## Opposite Sides are Equal

Another fundamental property is that the opposite sides of a parallelogram are equal in length. This theorem says that in a parallelogram, opposite sides are equal.

You can prove this by drawing a diagonal, which divides the parallelogram into two congruent triangles. Since the triangles are congruent, their corresponding sides must be equal.

The converse of this property is also true: if each pair of opposite sides of a quadrilateral is equal, then it is a parallelogram.

## Opposite Angles are Equal

Similarly, the opposite angles of a parallelogram are equal. This theorem says that in a parallelogram, opposite angles are equal. It follows from the congruent triangles made by the diagonal: in $\Delta ABC \cong \Delta CDA$, the angles $\angle B$ and $\angle D$ are corresponding parts, so $\angle B = \angle D$. Using the other diagonal in the same way gives $\angle A = \angle C$.

The converse of this property is also true: if in a quadrilateral, each pair of opposite angles is equal, then it is a parallelogram.

## Diagonal Divides into Congruent Triangles

A key property of parallelograms is that a diagonal divides it into two congruent triangles. A diagonal of a parallelogram divides it into two congruent triangles.

Proof: Let $ABCD$ be a parallelogram and $AC$ be a diagonal. The diagonal $AC$ divides the parallelogram into two triangles, namely $\Delta ABC$ and $\Delta CDA$. Since $BC \parallel AD$ and $AC$ is a transversal, $\angle BCA = \angle DAC$ (alternate angles). Also, since $AB \parallel DC$ and $AC$ is a transversal, $\angle BAC = \angle DCA$ (alternate angles). And $AC = CA$ (common). So, $\Delta ABC \cong \Delta CDA$ (ASA rule).

## Worked example

Consider a parallelogram $ABCD$ where the length of side $AB$ is $8$ cm and the length of side $AD$ is $6$ cm. The diagonal $AC$ intersects the other diagonal $BD$ at point $O$.

Since opposite sides of a parallelogram are equal, we know that $AB = DC = 8$ cm and $AD = BC = 6$ cm.

Since the diagonals bisect each other, we know that $OA = OC$ and $OB = OD$.

If the length of diagonal $AC$ is $10$ cm, then the length of $OA$ and $OC$ is $5$ cm each.

## A Second Example: Finding Unknowns

In parallelogram $PQRS$, the diagonals meet at $O$, with $OP = 3x + 1$ and $OR = 5x - 7$. Since the diagonals bisect each other, $OP = OR$. So $3x + 1 = 5x - 7$, which gives $8 = 2x$ and $x = 4$. Then $OP = 3(4) + 1 = 13$, and $OR = 5(4) - 7 = 13$, so each is $13$. The whole diagonal $PR$ is $13 + 13 = 26$ units long.

Now suppose $\angle P = 70^{\circ}$ in the same parallelogram. Opposite angles are equal, so $\angle R = 70^{\circ}$. Adjacent angles of a parallelogram add up to $180^{\circ}$, so $\angle Q = 180^{\circ} - 70^{\circ} = 110^{\circ}$, and $\angle S = 110^{\circ}$ as well. Check: $70 + 110 + 70 + 110 = 360$, the angle sum of a quadrilateral.

Finally, we can use the converse. A quadrilateral has sides $5$ cm, $7$ cm, $5$ cm and $7$ cm, taken in order around it. Each pair of opposite sides is equal, so it must be a parallelogram. We did not have to measure any angle.

## Key points

*   A parallelogram is a quadrilateral in which both pairs of opposite sides are parallel.
*   A diagonal of a parallelogram divides it into two congruent triangles.
*   In a parallelogram, opposite sides are equal.
*   In a parallelogram, opposite angles are equal.
*   The diagonals of a parallelogram bisect each other.
*   If each pair of opposite sides of a quadrilateral is equal, then it is a parallelogram.
*   If each pair of opposite angles of a quadrilateral is equal, then it is a parallelogram.
*   If the diagonals of a quadrilateral bisect each other, then it is a parallelogram.