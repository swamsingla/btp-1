---
{
  "concept": "Basic Geometric Constructions",
  "slug": "basic-constructions",
  "grade": 7,
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
    "completion_tokens": 1061,
    "prompt_tokens": 3256,
    "total_tokens": 4317,
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
  "generated_at": "2026-10-12T14:11:22",
  "source_grade": 7,
  "grade_delta": 0,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g7_maths_part2_chapter6_000",
      "chapter": "chapter6",
      "section": "6.1 Geometric Constructions"
    },
    {
      "ref": "S2",
      "passage_id": "g7_maths_part2_chapter6_008",
      "chapter": "chapter6",
      "section": "6.1 Geometric Constructions — Figure it Out"
    },
    {
      "ref": "S3",
      "passage_id": "g7_maths_part2_chapter6_015",
      "chapter": "chapter6",
      "section": "6.1 Geometric Constructions — Figure it Out"
    },
    {
      "ref": "S4",
      "passage_id": "g7_maths_part2_chapter6_022",
      "chapter": "chapter6",
      "section": "6.2 Tiling — SUMMARY"
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
    "unused_sources": [],
    "explanatory_paragraphs_without_a_citation": 0,
    "words": 683,
    "target_words": [
      700,
      1250
    ],
    "untraceable_sections": 0,
    "ok": true,
    "structural_problems": [],
    "verification": {
      "verdict": "ok",
      "checks": 2,
      "tokens": 3009
    }
  },
  "terms": [
    "perpendicular bisector",
    "angle bisection",
    "equilateral triangle",
    "bisection",
    "congruence"
  ],
  "hand_edited": "2026-10-12: regenerated from the Grade 7 constructions section with the Grade 6 page supplied as what the reader already knows. Hand audit found one error of substance: the worked example built a 60 degree angle from arcs of 'any radius' centred on both ends of a segment AB, which gives an isosceles triangle and not 60 degrees unless the radius equals AB; it also only repeated the section above it. Replaced by a 30 degree construction (60 degrees, then bisect). Also: the 60 degree steps used a point B they never defined; the bisection steps did not say A and B lie on the arms; the opening paragraph was the Grade 6 page's and spoke of measuring with an unmarked ruler; a question and a 'we have seen' pointing at text not on the page were turned into statements."
}
---

# Basic Geometric Constructions

A geometric construction draws a figure exactly, using only an unmarked ruler and a compass. The ruler draws straight lines and the compass carries a length from one place to another, so nothing has to be measured or guessed. You may already know how to use two arcs to find a point at a given distance from two other points. The same idea gives three constructions that are used again and again: cutting a line segment into two equal parts at a right angle, cutting an angle into two equal parts, and making an angle of exactly $60^\circ$.

## Perpendicular Bisector

A division of a line segment, or any geometrical quantity, into two identical parts is called bisection. A line that bisects a given line and is perpendicular to it, is called the perpendicular bisector.

We can construct a perpendicular bisector using the simplest geometric tools — an unmarked ruler and a compass. The method rests on one fact about a line segment $XY$: joining any two points, one above $XY$ and one below, that are each at equal distances from $X$ and $Y$ gives the perpendicular bisector of $XY$.

1. Taking some fixed radius, from $X$ and then $Y$, construct two sufficiently long arcs above $XY$. Name the point where the arcs meet as $A$.
2. Using the same radius, from $X$ and then $Y$, construct two sufficiently long arcs below $XY$. Name the point where the arcs meet as $B$.
3. $AB$ is the required perpendicular bisector.

Any point that is of equal distance from the two endpoints of a given line segment lies on its perpendicular bisector. This property can be used to construct the perpendicular bisector using a ruler and compass.

## Angle Bisection

An angle can be bisected and copied using the congruence properties of triangles.

To bisect an angle whose vertex is $O$, follow these steps:
1. Mark a point $A$ on one arm of the angle and a point $B$ on the other arm such that $OA = OB$.
2. Choosing any sufficiently long radius, cut arcs from $A$ and $B$, keeping the radius same. Mark the point of intersection as $C$.
3. $OC$ bisects $\angle AOB$.

## Constructing a $60^\circ$ Angle

A $60^\circ$ angle can be constructed using a ruler and a compass by constructing an equilateral triangle.

Suppose we need a $60^\circ$ angle at point $A$ on a line segment $AX$.
Step 1: Construct an arc with centre $A$ and any radius. Name the point where this arc cuts $AX$ as $B$.
Step 2: With the same radius, cut another arc from $B$ that meets the first arc. Let $C$ be the point at which the arcs meet.

The lengths $AB$, $AC$ and $BC$ are all equal to the radius, so $ABC$ is an equilateral triangle and $\angle CAX = 60^\circ$.

## Related Constructions

The method of constructing the perpendicular bisector can be modified to draw a $90^\circ$ angle at any point on a line using only a ruler and compass.

A $45^\circ$ angle can be constructed by first constructing a $90^\circ$ angle and then bisecting it.

A $30^\circ$ angle can be constructed by bisecting a $60^\circ$ angle.
A $15^\circ$ angle can be constructed by bisecting a $30^\circ$ angle.

## Worked example

Let us construct a $30^\circ$ angle at a point $A$ on a line $AX$, by making a $60^\circ$ angle and then bisecting it.

Step 1: With centre $A$ and any radius, draw an arc that cuts $AX$. Name the point where it cuts $AX$ as $B$.
Step 2: With the same radius and centre $B$, cut the first arc. Name the point where the arcs meet as $C$. Now $\angle CAB = 60^\circ$.
Step 3: The points $B$ and $C$ are already at the same distance from $A$, so they can be used to bisect the angle. Choose any sufficiently long radius, cut an arc from $B$ and an arc from $C$ keeping the radius the same, and name the point where these arcs meet as $D$.
Step 4: Join $A$ and $D$.

The line $AD$ bisects $\angle CAB$, so $\angle DAB$ is half of $60^\circ$, which is $30^\circ$.

## Key points

*   A division of a line segment, or any geometrical quantity, into two identical parts is called bisection.
*   Any point that is of equal distance from the two endpoints of a given line segment lies on its perpendicular bisector.
*   The method of constructing the perpendicular bisector can be modified to draw a $90^\circ$ angle at any point on a line using only a ruler and compass.
*   An angle can be bisected and copied using the congruence properties of triangles.
*   A $60^\circ$ angle can be constructed using a ruler and a compass by constructing an equilateral triangle.