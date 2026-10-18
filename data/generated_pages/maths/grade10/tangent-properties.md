---
{
  "concept": "Properties of Tangents from External Point",
  "slug": "tangent-properties",
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
    "completion_tokens": 1356,
    "prompt_tokens": 6146,
    "total_tokens": 7502,
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
  "generated_at": "2026-10-18T00:59:21",
  "source_grade": 10,
  "grade_delta": 0,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g10_maths_chapter10_008",
      "chapter": "chapter10",
      "section": "10.3 Number of Tangents from a Point on a Circle"
    },
    {
      "ref": "S2",
      "passage_id": "g10_maths_chapter10_005",
      "chapter": "chapter10",
      "section": "10.2 Tangent to a Circle"
    },
    {
      "ref": "S3",
      "passage_id": "g10_maths_chapter6_001",
      "chapter": "chapter6",
      "section": "6.1 Introduction"
    }
  ],
  "citation_check": {
    "cited": [
      "1",
      "2"
    ],
    "invented_citations": [],
    "unused_sources": [
      "3"
    ],
    "explanatory_paragraphs_without_a_citation": 0,
    "words": 940,
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
    "external point",
    "point of contact",
    "radius",
    "perpendicular",
    "rhs congruence",
    "cpct",
    "isosceles triangle",
    "angle bisector",
    "pythagoras theorem",
    "similar triangles",
    "aa similarity"
  ]
}
---

# Properties of Tangents from External Point

When you stand outside a circular park and throw two stones so they just graze the boundary, the distance from your hand to each point of touch is exactly the same. This is the central property we study here: two tangents drawn from a single point outside a circle are always equal in length. This rule is not just a curiosity; it is a powerful tool used to solve geometry problems involving circles, chords, and angles, and it builds directly on what you already know about tangents and triangle congruence.

## How Many Tangents Can You Draw?

Before we prove that the lengths are equal, it is important to understand exactly how many tangents can be drawn from a given point. If the point lies inside the circle, no tangent can be drawn because every line through that point will cut the circle at two places. If the point lies exactly on the circle, there is only one tangent, which touches the circle at that very point. However, when the point lies outside the circle, you can draw exactly two tangents. These two tangent segments share a common starting point, known as the external point, and they touch the circle at two distinct points called the points of contact.

## The Equal Length Property

The most important fact about these two tangents is that their lengths are always equal. If you take an external point $P$ and draw tangents $PQ$ and $PR$ to the circle, touching it at $Q$ and $R$, the length of the tangent from $P$ to the circle is defined as the length of the segment from $P$ to the point of contact. The theorem states that $PQ = PR$.

To understand why this is true, we look at the triangles formed by the centre of the circle, the external point, and the points of contact. Let us say the circle has centre $O$. By a fundamental property of tangents, the radius is always perpendicular to the tangent at the point of contact. Therefore, the angles $OQP$ and $ORP$ are right angles. If we draw the line from the centre $O$ to the external point $P$, we create two right-angled triangles: $OQP$ and $ORP$. In these two triangles, the radius $OQ$ is equal to the radius $OR$ because they are both radii of the same circle. The side $OP$ is common to both triangles. By the Right-angle-Hypotenuse-Side (RHS) congruence rule, the two triangles are congruent. Consequently, by the Corresponding Parts of Congruent Triangles (CPCT) rule, the lengths of the tangents $PQ$ and $PR$ must be equal.

The theorem can also be proved by using the Pythagoras Theorem. Since $PQ^2 = OP^2 - OQ^2$ and $PR^2 = OP^2 - OR^2$, and because $OQ = OR$, it follows that $PQ^2 = PR^2$, which gives $PQ = PR$.

## The Line to the Centre Bisects the Angle

A direct and useful consequence of the equal-length property is that the line connecting the external point to the centre of the circle acts as an angle bisector. The two right-angled triangles $OQP$ and $ORP$ from the proof above are congruent, so their corresponding angles are equal. In particular, $\angle OPQ = \angle OPR$. This means the line $OP$ bisects the angle $\angle QPR$ between the two tangents.

## Worked Example

Let us apply this rule to a practical problem. Suppose you have a circle with a radius of $5$ cm and a chord $PQ$ that is $8$ cm long. The tangents are drawn at points $P$ and $Q$, and they meet at an external point $T$. We need to find the length of the tangent $TP$.

First, we join the centre $O$ to the external point $T$, and let $OT$ meet the chord $PQ$ at $M$. Because the tangents $TP$ and $TQ$ are equal, the triangle $TPQ$ is isosceles, and $OT$ is the angle bisector of $\angle PTQ$. This means $OT$ is perpendicular to the chord $PQ$ and bisects it. Therefore, $PM$ is exactly half of $PQ$, which is $4$ cm.

Next, we look at the right-angled triangle $OMP$. We know the hypotenuse $OP$ is $5$ cm and the side $PM$ is $4$ cm. Using the Pythagoras theorem, the length of $OM$ is $\sqrt{5^2 - 4^2} = \sqrt{25 - 16} = 3$ cm.

Finally, we consider the right-angled triangle $TMP$. The angle $MPO$ is equal to the angle $PTM$ because each of them adds up to $90^\circ$ with the angle $TPM$. This means triangle $TMP$ is similar to triangle $PMO$ by the Angle-Angle (AA) similarity rule. Using the ratio of corresponding sides, we get $\frac{TP}{PO} = \frac{MP}{MO}$. Substituting the known values gives $\frac{TP}{5} = \frac{4}{3}$. Solving for $TP$, we find that $TP = \frac{20}{3}$ cm.

## Key points

*   From a point outside a circle, exactly two tangents can be drawn.
*   The lengths of these two tangents from the external point to the circle are always equal.
*   The line joining the external point to the centre of the circle bisects the angle between the two tangents.
*   The proof of equal lengths relies on the congruence of the two right-angled triangles formed by the radii.
*   This property is frequently used to solve problems involving chords, concentric circles, and distances.