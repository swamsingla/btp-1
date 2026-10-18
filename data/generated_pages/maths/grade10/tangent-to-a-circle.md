---
{
  "concept": "Tangent to a Circle",
  "slug": "tangent-to-a-circle",
  "grade": 10,
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
    "completion_tokens": 1283,
    "prompt_tokens": 6351,
    "total_tokens": 7634,
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
  "generated_at": "2026-10-17T22:37:52",
  "source_grade": 10,
  "grade_delta": 0,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g10_maths_chapter10_004",
      "chapter": "chapter10",
      "section": "10.2 Tangent to a Circle"
    },
    {
      "ref": "S2",
      "passage_id": "g10_maths_chapter10_010",
      "chapter": "chapter10",
      "section": "10.3 Number of Tangents from a Point on a Circle"
    },
    {
      "ref": "S3",
      "passage_id": "g10_maths_chapter10_001",
      "chapter": "chapter10",
      "section": "10.1 Introduction"
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
    "explanatory_paragraphs_without_a_citation": 3,
    "words": 1010,
    "target_words": [
      1000,
      1350
    ],
    "untraceable_sections": 0,
    "ok": true,
    "structural_problems": []
  },
  "terms": [
    "tangent",
    "circle",
    "point of contact",
    "secant",
    "radius",
    "perpendicular",
    "normal",
    "chord",
    "external point",
    "congruent",
    "right-angled triangle"
  ]
}
---

# Tangent to a Circle

A tangent is a straight line that touches a circle at exactly one point. This single common point is called the point of contact. Understanding tangents is crucial because they appear in everyday objects, such as the rope on a pulley or the wheel of a bicycle rolling on the ground. The word 'tangent' comes from the Latin word 'tangere', which means to touch and was introduced by the Danish mathematician Thomas Fincke in 1583.

## What is a Tangent?

To understand a tangent, we must first look at how a line can interact with a circle. There are three possible situations. A line might not intersect the circle at all, it might cut through the circle at two points, or it might touch the circle at exactly one point. 

A line that intersects the circle at two points is called a secant. A tangent is actually a special case of a secant. As a line moves closer to the circle, the two intersection points get closer and closer together. When these two points finally coincide, the line becomes a tangent. At this moment, the chord formed by the secant shrinks to a single point. 

You can easily see this by drawing a circle and a secant on a piece of paper. If you draw several lines parallel to the secant on either side, the length of the chord cut by the lines will gradually decrease. Eventually, the length becomes zero, and you have a tangent.

## The Perpendicular Property

One of the most important rules about a tangent is its relationship with the radius of the circle. The radius that passes through the point of contact is always perpendicular to the tangent line. 

To prove this, imagine a circle with centre $O$ and a tangent line $XY$ touching the circle at point $P$. Take any other point $Q$ on the tangent line. Because $Q$ lies outside the circle, the distance from the centre $O$ to $Q$ must be greater than the radius $OP$. This means $OQ > OP$. Since this is true for every point on the tangent line except $P$, the radius $OP$ is the shortest distance from the centre to the line. In geometry, the shortest distance from a point to a line is always perpendicular to the line.

This property is very useful in real life. For example, if you look at a bicycle or a cart moving, the wheel rolls along a line that is a tangent to the circle representing the wheel. At all times, the radius through the point of contact with the ground is at right angles to the tangent.

## Number of Tangents from a Point

The number of tangents you can draw from a specific point depends on where that point is located. If you pick a point inside the circle, you cannot draw any tangent through it. If you pick a point exactly on the circle, you can draw exactly one tangent. If you pick a point outside the circle, you can draw exactly two tangents.

This leads to three clear cases. First, if a point lies inside the circle, no tangent can pass through it. Second, if a point lies on the circle, there is one and only one tangent. Third, if a point lies outside the circle, there are exactly two tangents.

When you draw two tangents from an external point to a circle, they have a special property. The lengths of these tangents are always equal. For instance, if you draw tangents from an external point $P$ to a circle at points $T_1$ and $T_2$, the lengths $PT_1$ and $PT_2$ will be identical. 

This happens because the two tangent segments and the radii form two right-angled triangles. In these triangles, the radii are equal, and the line from the centre to the external point is a common side. By the right-angle-hypotenuse-side rule, the two triangles are congruent, which means their corresponding sides are equal.

## Worked Example

Let us apply the rule that the lengths of tangents from an external point are equal. Suppose a circle has a radius of 5 cm. A chord inside this circle has a length of 8 cm. The tangents drawn at the ends of this chord intersect at an external point. We want to find the length of the tangent from this external point to the circle.

Let the circle have centre $O$, let the chord be $AB$, and let the tangents at $A$ and $B$ meet at $P$. The two tangent lengths $PA$ and $PB$ are equal, and the radii $OA$ and $OB$ are equal, so the line $OP$ cuts the chord $AB$ at right angles at its midpoint $M$. Therefore $AM = 4$ cm.

Next, we look at the right-angled triangle $OMA$. Using the Pythagorean theorem, $OM = \sqrt{5^2 - 4^2} = 3$ cm. Note that 3 cm is the distance from the centre to the chord, not to the point $P$.

Now consider the triangle $OAP$. The tangent $PA$ is perpendicular to the radius $OA$, so this triangle has a right angle at $A$. The triangles $OMA$ and $OAP$ share the angle at $O$ and each has a right angle, so they are similar. Hence
$$
\frac{OP}{OA} = \frac{OA}{OM}, \quad \text{so} \quad OP = \frac{5 \times 5}{3} = \frac{25}{3} \text{ cm}.
$$

Finally, in the right-angled triangle $OAP$, the Pythagorean theorem gives
$$
PA = \sqrt{OP^2 - OA^2} = \sqrt{\frac{625}{9} - 25} = \sqrt{\frac{400}{9}} = \frac{20}{3} \text{ cm}.
$$
So the length of the tangent from $P$ to the circle is $\frac{20}{3}$ cm, or about 6.67 cm.

## Key points

*   A tangent to a circle is a line that intersects the circle at only one point, called the point of contact.
*   A tangent is a special case of a secant where the two endpoints of the corresponding chord coincide.
*   The tangent at any point of a circle is perpendicular to the radius through the point of contact.
*   There is one and only one tangent to a circle at any point on the circle.
*   From a point outside the circle, exactly two tangents can be drawn, and their lengths are equal.