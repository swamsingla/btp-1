---
{
  "concept": "Angle Between Two Lines in 3D",
  "slug": "angle-between-lines-3d",
  "grade": 12,
  "language": "en",
  "subject": "maths",
  "area": "Coordinate Geometry",
  "model": "sarvam-105b",
  "settings": {
    "temperature": 0.3,
    "max_tokens": 8000,
    "reasoning_effort": "none"
  },
  "usage": {
    "completion_tokens": 1404,
    "prompt_tokens": 6569,
    "total_tokens": 7973,
    "completion_tokens_details": {
      "accepted_prediction_tokens": null,
      "audio_tokens": null,
      "reasoning_tokens": 0,
      "rejected_prediction_tokens": null
    },
    "prompt_tokens_details": null
  },
  "target_words": [
    1050,
    1450
  ],
  "generated_at": "2026-10-08T05:15:44",
  "source_grade": 12,
  "grade_delta": 0,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g12_maths_part2_chapter5_015",
      "chapter": "chapter5",
      "section": "11.4 Angle between Two Lines"
    },
    {
      "ref": "S2",
      "passage_id": "g12_maths_part2_chapter5_005",
      "chapter": "chapter5",
      "section": "11.2.1 Direction cosines of a line passing through two points"
    },
    {
      "ref": "S3",
      "passage_id": "g12_maths_part2_chapter5_001",
      "chapter": "chapter5",
      "section": "11.1 Introduction"
    }
  ],
  "citation_check": {
    "cited": [
      "1"
    ],
    "invented_citations": [],
    "unused_sources": [
      "2",
      "3"
    ],
    "explanatory_paragraphs_without_a_citation": 0,
    "words": 897,
    "target_words": [
      1050,
      1450
    ],
    "untraceable_sections": 0,
    "ok": true,
    "structural_problems": []
  },
  "terms": [
    "direction ratios",
    "direction cosines",
    "angle",
    "vector",
    "dot product",
    "perpendicular",
    "parallel",
    "origin",
    "magnitude",
    "cartesian form",
    "scalar product"
  ]
}
---

# Angle Between Two Lines in 3D

In Grade 12, you move from the flat world of two dimensions into the full three-dimensional space. Just as you can measure the angle between two roads on a map, you can measure the angle between two lines in space. This skill is essential for physics and engineering, where forces and beams interact in 3D environments. To find this angle, you use direction ratios or direction cosines, which are the components of the vectors that point along each line.

## From Direction Ratios to Direction Cosines

When a line passes through the origin, its direction can be described by three numbers called direction ratios. Let $L_{1}$ and $L_{2}$ be two lines passing through the origin and with direction ratios $a_{1}, b_{1}, c_{1}$ and $a_{2}, b_{2}, c_{2}$, respectively. If you pick a point $P$ on $L_{1}$ and a point $Q$ on $L_{2}$, the directed lines $OP$ and $OQ$ act as vectors. The angle $\theta$ between them is found using the dot product formula, which gives the cosine of the angle as the absolute value of the dot product of the direction vectors divided by the product of their magnitudes.

Sometimes, the line is described using direction cosines instead of direction ratios. Direction cosines, namely $l_{1}, m_{1}, n_{1}$ for $L_{1}$ and $l_{2}, m_{2}, n_{2}$ for $L_{2}$, are the actual cosines of the angles the line makes with the $x$, $y$, and $z$-axes. Because the sum of the squares of the direction cosines of a line is always 1, the formula for the cosine of the angle between two lines becomes much simpler. You just take the absolute value of the sum of the products of their respective direction cosines.

## The Sine of the Angle

While the cosine formula is the most common, the sine of the angle between two lines is also useful, especially when checking if lines are parallel. You can find the sine of the angle $\theta$ by taking the square root of 1 minus the square of the cosine of the angle. When you expand this formula using direction ratios, it simplifies to a very neat expression. It involves the square roots of the differences of the products of the direction ratios. This formula is particularly helpful because if the lines are parallel, the numerator becomes zero, which means the sine of the angle is zero.

## The Vector Approach

In many problems, you will be given the equations of the lines in vector form rather than just their direction ratios. If the lines are given by $\vec{r} = \overline{{a}}_1 + \lambda \vec{b}_1$ and $\vec{r} = \vec{a}_2 + \mu \vec{b}_2$, you can still find the angle between them. The direction vectors $\vec{b}_1$ and $\vec{b}_2$ act exactly like the direction ratios. You find the cosine of the angle by taking the absolute value of the dot product of these two direction vectors and dividing it by the product of their magnitudes.

## Cartesian Form

When the equations of the lines are given in Cartesian form, the process is very similar. The equations look like $\frac{x - x_1}{a_1} = \frac{y - y_1}{b_1} = \frac{z - z_1}{c_1}$ and $\frac{x - x_2}{a_2} = \frac{y - y_2}{b_2} = \frac{z - z_2}{c_2}$. Here, the numbers $a_1, b_1, c_1$ and $a_2, b_2, c_2$ are the direction ratios of the lines. You can plug these directly into the cosine formula to find the angle between them.

## Perpendicular and Parallel Lines

A key application of these formulas is determining the relationship between two lines. If the cosine of the angle between two lines is zero, the lines are perpendicular. Using the direction ratio formula, this means the sum of the products of their corresponding direction ratios must equal zero. On the other hand, if the sine of the angle is zero, the lines are parallel. This happens when the ratios of their corresponding direction ratios are equal to each other.

## Worked Example

Let us find the angle between the pair of lines given by $\vec{r} = 3 \hat{i} + 2 \hat{j} - 4 \hat{k} + \lambda (\hat{i} + 2 \hat{j} + 2 \hat{k})$ and $\frac{x + 1}{1} = \frac{y - 4}{1} = \frac{z - 5}{2}$. The direction ratios of the first line are 3, 5, 4 and the direction ratios of the second line are 1, 1, 2. If $\theta$ is the angle between them, then $\cos \theta = \left| \frac{3 \cdot 1 + 5 \cdot 1 + 4 \cdot 2}{\sqrt{3^2 + 5^2 + 4^2} \sqrt{1^2 + 1^2 + 2^2}} \right| = \frac{16}{\sqrt{50} \sqrt{6}} = \frac{16}{5 \sqrt{2} \sqrt{6}} = \frac{8 \sqrt{3}}{15}$. Hence, the required angle is $\cos^{-1}\left(\frac{8\sqrt{3}}{15}\right)$.

## Key points
* The angle between two lines in 3D can be found using direction ratios or direction cosines via the dot product formula.
* If the lines do not pass through the origin, you can draw parallel lines through the origin to use this formula.
* Two lines are perpendicular if the sum of the products of their direction ratios is zero.
* Two lines are parallel if the ratios of their corresponding direction ratios are equal.
* The vector form of the line equation uses direction vectors in the same way as direction ratios.