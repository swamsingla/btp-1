---
{
  "concept": "Circle Theorems",
  "slug": "circle-theorems",
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
    "completion_tokens": 1122,
    "prompt_tokens": 6199,
    "total_tokens": 7321,
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
  "generated_at": "2026-10-17T06:34:49",
  "source_grade": 9,
  "grade_delta": 0,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g9_maths_chapter9_012",
      "chapter": "chapter9",
      "section": "9.4 Angle Subtended by an Arc of a Circle"
    },
    {
      "ref": "S2",
      "passage_id": "g9_maths_chapter9_008",
      "chapter": "chapter9",
      "section": "9.3 Equal Chords and their Distances from the Centre"
    },
    {
      "ref": "S3",
      "passage_id": "g9_maths_chapter9_001",
      "chapter": "chapter9",
      "section": "9.1 Angle Subtended by a Chord at a Point"
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
    "explanatory_paragraphs_without_a_citation": 2,
    "words": 863,
    "target_words": [
      1000,
      1350
    ],
    "untraceable_sections": 0,
    "ok": true,
    "structural_problems": []
  },
  "terms": [
    "chord",
    "arc",
    "congruent",
    "semicircle",
    "diameter",
    "right angle",
    "segment",
    "concyclic",
    "angle subtended",
    "radius",
    "sss",
    "cpct"
  ]
}
---

# Circle Theorems

Circle theorems are a set of rules that describe the relationships between angles, chords, and arcs inside a circle. Understanding these rules allows you to solve complex geometry problems without having to measure every single line and angle with a protractor. These concepts are fundamental to geometry and help us understand the hidden symmetry of circular shapes.

## Equal Chords and Central Angles

When you draw two chords of the same length inside a circle, they create a very specific relationship with the centre of the circle. If two chords of a circle are equal, then their corresponding arcs are congruent and conversely, if two arcs are congruent, then their corresponding chords are equal. This means that if you take a piece of string and lay it along the two arcs, the strings will match perfectly. 

Because the arcs are congruent, the angles that these arcs make at the centre of the circle are also equal. Congruent arcs (or equal arcs) of a circle subtend equal angles at the centre. This is a direct result of the fact that equal chords of a circle subtend equal angles at the centre. You can prove this by looking at the two triangles formed by the chords and the radii. Two sides of each triangle are radii of the circle, so they are equal in length, and the third side of each is one of the equal chords. Using the SSS (Side-Side-Side) congruence rule, we can see that the triangles are congruent, which means their corresponding angles at the centre must be equal.

## The Angle in a Semicircle

A semicircle is exactly half of a circle, formed by a diameter. When you draw a triangle inside a circle such that one of its sides is the diameter and the opposite vertex lies anywhere on the circle's edge, the angle at that vertex is always a right angle. 

According to Theorem 9.7, the angle subtended by an arc at the centre is double the angle subtended by it at any point on the remaining part of the circle. If the arc is a semicircle, the angle at the centre is $180^\circ$. Therefore, the angle subtended by it at any point on the circle is exactly half of $180^\circ$, which is $90^\circ$. If you take any other point on the semicircle, the angle formed at that point will also be $90^\circ$. This proves that the angle in a semicircle is a right angle.

## Angles in the Same Segment

Imagine you have a chord in a circle, which divides the circle into two parts called segments. If you pick any two points on the same arc, and draw lines to the endpoints of the chord, you will form two angles. These angles are located in the same segment of the circle. 

Theorem 9.8 states that angles in the same segment of a circle are equal. This happens because both of these angles are subtended by the exact same arc. Since the angle at the centre is double the angle at the circumference for any given arc, and the centre is fixed, the angles at the circumference must be equal to each other. 

The converse of this theorem is also true. If a line segment joining two points subtends equal angles at two other points lying on the same side of the line containing the line segment, the four points lie on a circle (i.e. they are concyclic). This is a powerful tool for proving that a set of points forms a circle.

## Worked example

Consider a circle with a chord PQ. The angle subtended by this chord at the centre, O, is $80^\circ$. You want to find the angle subtended by the same chord at a point A on the remaining part of the circle. 

Using Theorem 9.7, we know that the angle at the centre is double the angle at the circumference. Therefore, the angle at point A is exactly half of the central angle. The calculation is as follows:
$$ \angle POQ = 2 \angle PAQ $$
$$ 80^\circ = 2 \times \angle PAQ $$
$$ \angle PAQ = \frac{80^\circ}{2} = 40^\circ $$
So, the angle at point A is $40^\circ$. If you were to pick another point, say B, on the same arc, the angle PBQ would also be $40^\circ$, proving that angles in the same segment are equal.

## Key points
* Equal chords of a circle subtend equal angles at the centre.
* Congruent arcs (or equal arcs) of a circle subtend equal angles at the centre.
* The angle subtended by an arc at the centre is double the angle subtended by it at any point on the remaining part of the circle.
* Angles in the same segment of a circle are equal.
* The angle in a semicircle is a right angle.
* If a line segment joining two points subtends equal angles at two other points lying on the same side of the line containing the line segment, the four points lie on a circle.