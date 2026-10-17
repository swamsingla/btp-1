---
{
  "concept": "Perpendicular Bisector",
  "slug": "perpendicular-bisector",
  "grade": 8,
  "language": "en",
  "hand_edited": "2026-10-13: 'Why it Works' proof was wrong (said one intersection point and two endpoints give two triangles) -> rewritten with A, B, M and SSS then SAS; 'we need a point' -> two points; added radius must exceed half the segment; worked example was circular (drew the line through 'the midpoint', which is what is being found) -> uses A and B, M, with a sqrt(24) check; 'centre of a line' -> midpoint of a segment. Verifier verdict 'spiralled'.",
  "subject": "maths",
  "area": "Geometry",
  "model": "sarvam-105b",
  "settings": {
    "temperature": 0.3,
    "max_tokens": 8000,
    "reasoning_effort": "none"
  },
  "usage": {
    "completion_tokens": 790,
    "prompt_tokens": 4023,
    "total_tokens": 4813,
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
  "generated_at": "2026-10-13T22:59:00",
  "source_grade": 7,
  "grade_delta": -1,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g7_maths_part2_chapter6_001",
      "chapter": "chapter6",
      "section": "6.1 Geometric Constructions"
    }
  ],
  "citation_check": {
    "cited": [
      "1"
    ],
    "invented_citations": [],
    "unused_sources": [],
    "explanatory_paragraphs_without_a_citation": 1,
    "words": 634,
    "target_words": [
      950,
      1300
    ],
    "untraceable_sections": 0,
    "ok": true,
    "short": [
      "length: 634 words, under 950"
    ],
    "structural_problems": [],
    "verification": {
      "verdict": "spiralled",
      "checks": 1,
      "tokens": 8996
    }
  },
  "terms": [
    "perpendicular bisector",
    "congruent triangles",
    "equidistant",
    "midpoint",
    "right angle",
    "geometric construction",
    "compass",
    "unmarked ruler",
    "line segment",
    "endpoint",
    "radius",
    "intersection point"
  ]
}
---

# Perpendicular Bisector

A perpendicular bisector is a line that cuts a line segment exactly in half at a right angle. It is the set of all points that are equidistant from two given endpoints. This concept matters because it helps us find the exact midpoint of any line segment, which is useful in design, construction, and solving geometry problems.

## Finding the Perpendicular Bisector

To find the perpendicular bisector of a line segment, we need two points that are each equally distant from both endpoints. Every point that is equidistant from two points lies on the perpendicular bisector of the segment joining them, and two such points are enough to draw the line. 

We can construct this line using a compass and an unmarked ruler. First, take a fixed radius that is more than half the length of the segment, and draw an arc from one endpoint. (With a smaller radius the two arcs would never meet.) Next, using the same radius, draw another arc from the second endpoint. The two arcs will intersect at a point. This point is equidistant from both endpoints because it was found using the same compass radius.

## Why it Works

The construction works because of congruent triangles. Let the segment have endpoints X and Y. Let the two arcs above the line meet at A, let the two arcs below the line meet at B, and let the line AB cross the segment XY at M. Join AX, AY, BX and BY. The two arcs above the line have the same radius, so $AX = AY$. In the same way, $BX = BY$. The side AB is common to triangles AXB and AYB, so these two triangles are congruent (SSS), and therefore $\angle XAB = \angle YAB$.

Now look at triangles AXM and AYM. They have $AX = AY$, the common side AM, and $\angle XAM = \angle YAM$, so they are congruent (SAS). Because corresponding parts of congruent triangles are equal, $XM = MY$ and $\angle AMX = \angle AMY$. These two angles lie along a straight line, so they add up to $180^{\circ}$, and each of them is exactly $90^{\circ}$. So AB splits the segment XY into two equal halves at a right angle.

## Construction Steps

We can draw the perpendicular bisector of any line segment using only a compass and an unmarked ruler. We must use the same compass radius for both arcs to ensure the intersection point is equidistant from the endpoints.

1. Take a fixed radius on your compass, more than half the length of the segment. From one endpoint of the segment, draw a large arc above the line.
2. Without changing the compass radius, place the compass on the second endpoint and draw another arc above the line.
3. The two arcs will cross at a point. Call this point A.
4. Repeat the process below the line to find a second intersection point, B.
5. Use the unmarked ruler to draw a straight line through points A and B.
6. The line AB is the perpendicular bisector of the original segment.

## Worked Example

Let us apply this construction to a line segment that is 10 cm long. We will call the endpoints X and Y. 

First, set your compass to a radius of 7 cm. Place the compass point on X and draw an arc above the line XY. Next, place the compass point on Y and draw another arc above XY. The two arcs will intersect at a point we will call A. 

Repeat this below the line, again with a radius of 7 cm, to find the second intersection point B. Draw a straight line through A and B. It meets XY at a point M. By the argument above, M is the midpoint of XY, so $XM = MY = 5$ cm, and the line AB meets XY at a right angle. You can check this with a ruler and a set square. So AB is the perpendicular bisector of XY. (The point A is $\sqrt{7^2 - 5^2} = \sqrt{24}$, about 4.9 cm, away from the line XY, which also shows that a 7 cm radius is long enough for the arcs to meet.)

## Key points
- A perpendicular bisector divides a line segment into two equal parts at a right angle.
- Any point on the perpendicular bisector is equidistant from the two endpoints of the segment.
- To construct it, draw intersecting arcs from both endpoints using the same compass radius.
- The line joining the two intersection points of the arcs is the perpendicular bisector.
- This construction uses only an unmarked ruler and a compass.