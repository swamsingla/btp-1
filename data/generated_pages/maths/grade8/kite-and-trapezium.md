---
{
  "concept": "Kite and Trapezium Properties",
  "slug": "kite-and-trapezium",
  "grade": 8,
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
    "completion_tokens": 1342,
    "prompt_tokens": 6024,
    "total_tokens": 7366,
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
  "generated_at": "2026-10-12T21:48:24",
  "source_grade": 8,
  "grade_delta": 0,
  "hand_edited": "2026-10-12: line-by-line hand audit against the textbook, edited directly. Fixed: circular kite proof (now SSS then SAS), degenerate kite worked example (6+6=12), trapezium worked example that derived R from P, isosceles proof with the right angle at the wrong vertex and the wrong condition (RHS, not SAS), wrong angle pair in the isosceles example, 'a kite is not a parallelogram' (a rhombus is both), 'only one pair' of parallel sides.",
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g8_maths_part1_chapter4_025",
      "chapter": "chapter4",
      "section": "4.6 Kite and Trapezium"
    },
    {
      "ref": "S2",
      "passage_id": "g8_maths_part1_chapter4_016",
      "chapter": "chapter4",
      "section": "4.3 More Quadrilaterals with Parallel Opposite Sides"
    },
    {
      "ref": "S3",
      "passage_id": "g8_maths_part1_chapter4_021",
      "chapter": "chapter4",
      "section": "4.4 Quadrilaterals with Equal Sidelengths"
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
    "explanatory_paragraphs_without_a_citation": 7,
    "words": 869,
    "target_words": [
      950,
      1300
    ],
    "untraceable_sections": 0,
    "ok": true,
    "structural_problems": [],
    "verification": {
      "verdict": "spiralled",
      "checks": 2,
      "tokens": 10969
    }
  },
  "terms": [
    "kite",
    "trapezium",
    "isosceles trapezium",
    "adjacent sides",
    "diagonal",
    "bisect",
    "transversal",
    "parallel sides",
    "congruent triangles"
  ]
}
---

# Kite and Trapezium Properties

Squares, rectangles, and parallelograms are quadrilaterals. These shapes all have pairs of parallel opposite sides. But not all quadrilaterals behave this way. In this page, we will look at two other interesting quadrilaterals: the kite and the trapezium. A kite has no parallel sides, and a trapezium is only guaranteed one pair of parallel sides.

## What is a Kite?

A kite is a quadrilateral that can be labelled $ABCD$ such that $AB = BC$, and $CD = DA$. This means that two pairs of adjacent sides are equal.
**Property 1:** In a kite, the diagonal $BD$ bisects $\angle ABC$ and $\angle ADC$, and it bisects the diagonal $AC$, that is, $AO = OC$, and is perpendicular to it.

To see why, let the diagonals meet at $O$. First consider $\Delta ABD$ and $\Delta CBD$. We have $AB = CB$ and $AD = CD$, and $BD$ is common to both triangles. So $\Delta ABD \cong \Delta CBD$ by the Side-Side-Side (SSS) condition. Therefore $\angle ABD = \angle CBD$ and $\angle ADB = \angle CDB$, which means the diagonal $BD$ bisects $\angle ABC$ and $\angle ADC$. Now consider $\Delta AOB$ and $\Delta COB$. We have $AB = CB$, $\angle ABO = \angle CBO$, and $BO$ is common, so $\Delta AOB \cong \Delta COB$ by the Side-Angle-Side (SAS) condition. Hence $AO = OC$ and $\angle AOB = \angle COB$. These two angles form a straight angle, so they add up to $180^{\circ}$, and each is $90^{\circ}$.

**Worked example:** In a kite $ABCD$ with $AB = BC$ and $CD = DA$, suppose $\angle ABD = 35^{\circ}$. Since the diagonal $BD$ bisects $\angle ABC$, $\angle CBD = 35^{\circ}$ and $\angle ABC = 70^{\circ}$. The diagonals meet at a right angle at $O$, so in $\Delta AOB$, $\angle BAO = 180^{\circ} - 90^{\circ} - 35^{\circ} = 55^{\circ}$.

## What is a Trapezium?

A trapezium is a quadrilateral with at least one pair of parallel opposite sides. This is different from a parallelogram, which has two pairs of parallel opposite sides.

**Property 1:** In a trapezium, the two angles at the ends of each non-parallel side add up to $180^{\circ}$.

If $PQ$ is parallel to $SR$, then $\angle S + \angle P = 180^{\circ}$ and $\angle R + \angle Q = 180^{\circ}$. This is because the angles are interior angles on the same side of a transversal cutting across two parallel lines.

**Worked example:** In a trapezium $PQRS$ with $PQ \parallel SR$, suppose $\angle P = 110^{\circ}$ and $\angle Q = 80^{\circ}$. Since $\angle S + \angle P = 180^{\circ}$, $\angle S = 180^{\circ} - 110^{\circ} = 70^{\circ}$. Since $\angle R + \angle Q = 180^{\circ}$, $\angle R = 180^{\circ} - 80^{\circ} = 100^{\circ}$. The four angles add up to $110^{\circ} + 80^{\circ} + 70^{\circ} + 100^{\circ} = 360^{\circ}$.

## What is an Isosceles Trapezium?

When the non-parallel sides of a trapezium have the same lengths, the trapezium is called an isosceles trapezium.

**Property 2:** In an isosceles trapezium, the angles opposite to the equal sides are equal.

To see why, consider an isosceles trapezium $UVWX$ where $UV$ is parallel to $XW$. Draw line segments $XY$ and $WZ$ perpendicular to $UV$. Since $XY$ and $WZ$ are perpendicular to the parallel lines $UV$ and $XW$, the quadrilateral $XWZY$ is a rectangle. This means $XY = WZ$. Now, consider $\Delta UXY$ and $\Delta VWZ$. We have $UX = VW$ (the equal non-parallel sides), $XY = WZ$, and $\angle UYX = \angle VZW = 90^{\circ}$. Therefore, $\Delta UXY \cong \Delta VWZ$ by the Right angle-Hypotenuse-Side (RHS) congruence condition. This proves that $\angle U = \angle V$.

**Worked example:** An isosceles trapezium has equal non-parallel sides of 8 cm. The angles opposite these sides, $\angle U$ and $\angle V$, are both $100^{\circ}$ (here $UV$ is the shorter parallel side). The remaining angles must each be $80^{\circ}$, because $\angle U + \angle X = 180^{\circ}$ and $\angle V + \angle W = 180^{\circ}$.

## Summary of Properties

It is helpful to compare the kite and trapezium with other quadrilaterals. Parallelograms have parallel opposite sides, and a rectangle is a special kind of parallelogram with all angles equal to $90^{\circ}$. A rhombus is a quadrilateral in which all the sides have the same length. Every rhombus is also a parallelogram, and the properties of a parallelogram hold true for a rhombus as well.

A kite has two pairs of adjacent equal sides and is generally not a parallelogram (a rhombus is both a kite and a parallelogram). A trapezium needs only one pair of parallel opposite sides. An isosceles trapezium is a special case where the non-parallel sides are equal, making the base angles equal as well.

## Key points

*   A kite is a quadrilateral with two pairs of adjacent equal sides, $AB = BC$ and $CD = DA$.
*   In a kite $ABCD$ with $AB = BC$ and $CD = DA$, the diagonal $BD$ bisects the angles at $B$ and $D$, and bisects the other diagonal $AC$ at a right angle.
*   A trapezium has at least one pair of parallel opposite sides.
*   In a trapezium, the two angles at the ends of each non-parallel side add up to $180^{\circ}$.
*   An isosceles trapezium has equal non-parallel sides, and the angles opposite these sides are equal.
