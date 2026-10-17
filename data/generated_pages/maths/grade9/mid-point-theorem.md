---
{
  "concept": "Mid-Point Theorem",
  "slug": "mid-point-theorem",
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
    "completion_tokens": 812,
    "prompt_tokens": 5815,
    "total_tokens": 6627,
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
  "generated_at": "2026-10-17T06:36:11",
  "source_grade": 9,
  "grade_delta": 0,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g9_maths_chapter8_009",
      "chapter": "chapter8",
      "section": "8.2 The Mid-point Theorem"
    },
    {
      "ref": "S2",
      "passage_id": "g9_maths_chapter7_009",
      "chapter": "chapter7",
      "section": "7.3 Criteria for Congruence of Triangles"
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
    "words": 586,
    "target_words": [
      1000,
      1350
    ],
    "untraceable_sections": 0,
    "ok": true,
    "structural_problems": [
      "length: 586 words, under 1000"
    ]
  },
  "terms": [
    "mid-point theorem",
    "congruent triangles",
    "parallelogram",
    "transversal",
    "bisect"
  ]
}
---

# Mid-Point Theorem

The Mid-Point Theorem is a powerful result about triangles. It tells us exactly what happens when we connect the middle of two sides. This rule is extremely useful because it lets us find unknown lengths and prove that lines are parallel without measuring them. If you know the length of the base of a triangle, you immediately know the length of the line joining the midpoints of the other two sides.

## The Rule

In any triangle, if you take the midpoint of two sides and join them, the new line segment is parallel to the third side and exactly half its length. For example, in triangle $ABC$, if $E$ and $F$ are the midpoints of $AB$ and $AC$, then the line segment $EF$ is parallel to the base $BC$, and $EF = \frac{1}{2} BC$. 

This relationship is very useful in geometry. The converse is also true: a line drawn through the midpoint of one side, parallel to another side, will automatically bisect the third side. 

## Proof

You can prove this theorem by extending the line segment $EF$ and using congruent triangles. Consider triangle $ABC$ where $E$ and $F$ are the midpoints of $AB$ and $AC$. Extend $EF$ to a point $D$ such that $FD = EF$, and join $C$ to $D$.

In triangles $AEF$ and $CDF$, we have $AF = CF$ (since $F$ is the midpoint of $AC$), $\angle AFE = \angle CFD$ (vertically opposite angles) and $EF = DF$ (by construction). So the triangles are congruent by the SAS rule. Therefore $AE = CD$, and $\angle AEF = \angle CDF$, which are alternate angles, so $AB \parallel CD$. Since $E$ is the midpoint of $AB$, $BE = AE = CD$. Now $BE = CD$ and $BE \parallel CD$, so the quadrilateral $BCDE$ is a parallelogram. In a parallelogram the opposite sides are parallel and equal, so $ED \parallel BC$ and $ED = BC$. Since $EF = \frac{1}{2} ED$, we get $EF \parallel BC$ and $EF = \frac{1}{2} BC$.

## Worked Example

Let us apply this theorem to a specific problem. Imagine a triangular plot of land $ABC$ where $D$ and $E$ are the midpoints of sides $AB$ and $BC$ respectively. A surveyor wants to know the length of the fence connecting $D$ to $E$, and also wants to know if this fence is parallel to the base $AC$.

Because $D$ and $E$ are the midpoints of the sides of the triangle, we can apply the Mid-Point Theorem. The theorem states that the line segment joining the midpoints of two sides of a triangle is parallel to the third side. Therefore, the fence $DE$ is parallel to the base $AC$. 

Furthermore, the theorem states that this joining line is exactly half the length of the third side. If the base $AC$ measures $20$ metres, then the fence $DE$ must measure exactly half of that. So, $DE = \frac{1}{2} \times 20 = 10$ metres. The surveyor can now confidently tell the landowner that the fence is $10$ metres long and runs parallel to the base $AC$.

## Key points

*   The line segment joining the midpoints of two sides of a triangle is parallel to the third side.
*   The length of this joining line segment is exactly half the length of the third side.
*   The converse is also true: a line drawn through the midpoint of one side, parallel to another side, bisects the third side.