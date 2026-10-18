---
{
  "concept": "Basic Proportionality Theorem (Thales)",
  "slug": "basic-proportionality-theorem",
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
    "completion_tokens": 1137,
    "prompt_tokens": 5386,
    "total_tokens": 6523,
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
  "generated_at": "2026-10-17T22:06:08",
  "source_grade": 10,
  "grade_delta": 0,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g10_maths_chapter6_008",
      "chapter": "chapter6",
      "section": "6.3 Similarity of Triangles"
    }
  ],
  "citation_check": {
    "cited": [],
    "invented_citations": [],
    "unused_sources": [
      "1"
    ],
    "explanatory_paragraphs_without_a_citation": 6,
    "words": 798,
    "target_words": [
      1000,
      1350
    ],
    "untraceable_sections": 4,
    "ok": false,
    "structural_problems": [
      "length: 798 words, under 1000"
    ]
  },
  "terms": [
    "basic proportionality theorem",
    "thales",
    "equiangular triangles",
    "corresponding sides",
    "corresponding angles",
    "trapezium",
    "parallel lines",
    "proportion",
    "ratio"
  ]
}
---

# Basic Proportionality Theorem (Thales)

Imagine you are making a large banner for your school fest, but you only have a small triangular piece of paper. To make it bigger, you need to scale up the dimensions while keeping the exact same shape. The Basic Proportionality Theorem, also known as Thales Theorem or BPT, is a powerful mathematical tool that helps us understand how lines parallel to the sides of a triangle divide the other sides proportionally. This theorem is fundamental because it allows us to prove that two triangles are similar, which means their corresponding angles are equal and their corresponding sides are in the same ratio.

## Understanding Similar Triangles

Before diving into the theorem, it is important to recall what it means for two triangles to be similar. A triangle is a polygon, so the conditions for the similarity of two polygons apply to it. Two triangles are similar if their corresponding angles are equal and their corresponding sides are in the same ratio or proportion. If the corresponding angles of two triangles are equal, they are known as equiangular triangles. The famous Greek mathematician Thales gave an important truth relating to two equiangular triangles: the ratio of any two corresponding sides in two equiangular triangles is always the same.

## The Basic Proportionality Theorem

The Basic Proportionality Theorem states that if a line is drawn parallel to one side of a triangle to intersect the other two sides in distinct points, the other two sides are divided in the same ratio. To see this in action, consider a triangle ABC in which a line parallel to side BC intersects the other two sides AB and AC at D and E respectively. We need to prove that $\frac{\mathrm{AD}}{\mathrm{DB}} = \frac{\mathrm{AE}}{\mathrm{EC}}$.

The proof relies on the areas of the smaller triangles created by the parallel line. Join B to E and C to D. Draw $EN \perp AB$ and $DM \perp AC$.

The area of $\Delta$ ADE is $\frac {1}{2} \mathrm{AD} \times \mathrm{EN}$. Similarly, the area of $\Delta$ BDE is $\frac {1}{2} \mathrm{DB} \times \mathrm{EN}$. Dividing, we get
$$ \frac{\mathrm{ar}(\mathrm{ADE})}{\mathrm{ar}(\mathrm{BDE})} = \frac{\mathrm{AD}}{\mathrm{DB}} \tag{1} $$
The area of $\Delta$ ADE is also $\frac {1}{2} \mathrm{AE} \times \mathrm{DM}$, and the area of $\Delta$ DEC is $\frac {1}{2} \mathrm{EC} \times \mathrm{DM}$. Dividing, we get
$$ \frac{\mathrm{ar}(\mathrm{ADE})}{\mathrm{ar}(\mathrm{DEC})} = \frac{\mathrm{AE}}{\mathrm{EC}} \tag{2} $$

Because $\Delta$ BDE and $\Delta$ DEC are on the same base DE and between the same parallels BC and DE, their areas are equal. The left-hand sides of (1) and (2) have the same numerator ar(ADE) and equal denominators, so they are equal. Hence the right-hand sides are equal too:
$$ \frac {\mathrm{AD}}{\mathrm{DB}} = \frac {\mathrm{AE}}{\mathrm{EC}} $$

## The Converse of the Theorem

The converse of this theorem is also true. If a line divides any two sides of a triangle in the same ratio, then the line is parallel to the third side. This means that if $\frac{\mathrm{AD}}{\mathrm{DB}} = \frac{\mathrm{AE}}{\mathrm{EC}}$, then the line DE must be parallel to BC. This is a very useful property for solving geometry problems where you need to prove that two lines are parallel based on the ratios of the sides they divide.

## Applying the Theorem to Trapeziums

The Basic Proportionality Theorem can be applied to other quadrilaterals like trapeziums. For example, if ABCD is a trapezium with AB parallel to DC, and E and F are points on the non-parallel sides AD and BC respectively such that EF is parallel to AB, we can show that $\frac{\mathrm{AE}}{\mathrm{ED}} = \frac{\mathrm{BF}}{\mathrm{FC}}$. This is done by joining AC to intersect EF at G.

In $\Delta$ ADC, $EG \parallel DC$, so by the theorem $\frac{\mathrm{AE}}{\mathrm{ED}} = \frac{\mathrm{AG}}{\mathrm{GC}}$. In $\Delta$ CAB, $GF \parallel AB$, so $\frac{\mathrm{CG}}{\mathrm{GA}} = \frac{\mathrm{CF}}{\mathrm{FB}}$, which means $\frac{\mathrm{AG}}{\mathrm{GC}} = \frac{\mathrm{BF}}{\mathrm{FC}}$. Since both $\frac{\mathrm{AE}}{\mathrm{ED}}$ and $\frac{\mathrm{BF}}{\mathrm{FC}}$ equal $\frac{\mathrm{AG}}{\mathrm{GC}}$, they are equal to each other.

## Worked Example

Let us work through a problem to see how the theorem is applied. Suppose we have a triangle ABC and a line DE parallel to BC intersects AB at D and AC at E. If AD is 6 cm and DB is 9 cm, we need to find the ratio of AE to EC. According to the Basic Proportionality Theorem, $\frac{\mathrm{AD}}{\mathrm{DB}} = \frac{\mathrm{AE}}{\mathrm{EC}}$. Substituting the given values, we get $\frac{6}{9} = \frac{\mathrm{AE}}{\mathrm{EC}}$. Simplifying the fraction, we find $\frac{2}{3} = \frac{\mathrm{AE}}{\mathrm{EC}}$. This means that AE is $\frac{2}{3}$ of EC, or equivalently, AE is $\frac{2}{5}$ of AC.

Now a converse example. In triangle ABC, D lies on AB and E lies on AC with AD = 3 cm, DB = 4.5 cm, AE = 2 cm and EC = 3 cm. Then $\frac{\mathrm{AD}}{\mathrm{DB}} = \frac{3}{4.5} = \frac{2}{3}$ and $\frac{\mathrm{AE}}{\mathrm{EC}} = \frac{2}{3}$. The ratios are equal, so by the converse of the theorem, DE is parallel to BC.

## Key points

* Two triangles are similar if their corresponding angles are equal and their corresponding sides are in the same ratio.
* The Basic Proportionality Theorem states that a line parallel to one side of a triangle divides the other two sides proportionally.
* The converse of the theorem states that if a line divides two sides of a triangle in the same ratio, then the line is parallel to the third side.
* The theorem can be applied to other figures: in a trapezium ABCD with AB ∥ DC, a line EF parallel to AB divides the non-parallel sides in the same ratio, $\frac{\mathrm{AE}}{\mathrm{ED}} = \frac{\mathrm{BF}}{\mathrm{FC}}$.
* The ratio of corresponding sides in similar triangles is always the same.