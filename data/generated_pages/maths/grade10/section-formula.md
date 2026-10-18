---
{
  "concept": "Section Formula and Midpoint",
  "slug": "section-formula",
  "grade": 10,
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
    "completion_tokens": 1146,
    "prompt_tokens": 7207,
    "total_tokens": 8353,
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
  "generated_at": "2026-10-17T22:37:11",
  "source_grade": 10,
  "grade_delta": 0,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g10_maths_chapter7_013",
      "chapter": "chapter7",
      "section": "7.3 Section Formula"
    },
    {
      "ref": "S2",
      "passage_id": "g10_maths_chapter11_005",
      "chapter": "chapter11",
      "section": "11.1 Areas of Sector and Segment of a Circle"
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
    "explanatory_paragraphs_without_a_citation": 3,
    "words": 687,
    "target_words": [
      1000,
      1350
    ],
    "untraceable_sections": 0,
    "ok": true,
    "structural_problems": [
      "length: 687 words, under 1000"
    ]
  },
  "terms": [
    "section formula",
    "midpoint",
    "internal division",
    "ratio",
    "coordinates"
  ]
}
---

# Section Formula and Midpoint

Imagine a telephone company wants to place a relay tower exactly between two locations, A and B. If the tower is positioned such that its distance from B is twice its distance from A, the tower divides the line segment AB in the ratio 1 : 2. To find the exact coordinates of this tower, we need a reliable mathematical method. This topic is exactly about finding the coordinates of a point that divides a line segment in a given ratio.

## The Section Formula

When a point P lies between two points A and B on a line, it divides the segment AB internally. Let the coordinates of A be $(x_1, y_1)$ and the coordinates of B be $(x_2, y_2)$. If P divides the line segment joining A and B internally in the ratio $m_1: m_2$, the coordinates of P are given by the section formula.

The coordinates of the point $P(x, y)$ which divides the line segment joining the points $A(x_{1}, y_{1})$ and $B(x_{2}, y_{2})$ , internally, in the ratio $m_{1}: m_{2}$ are

$$ \left(\frac {m _ {1} x _ {2} + m _ {2} x _ {1}}{m _ {1} + m _ {2}}, \frac {m _ {1} y _ {2} + m _ {2} y _ {1}}{m _ {1} + m _ {2}}\right) $$

This is known as the section formula. Here the ratio $m_1 : m_2$ means $AP : PB$. If the ratio in which P divides AB is $k: 1$, then the coordinates of the point P will be

$$ \left(\frac {k x _ {2} + x _ {1}}{k + 1}, \frac {k y _ {2} + y _ {1}}{k + 1}\right). $$

## Where the Formula Comes From

Let $P(x, y)$ divide $AB$ so that $AP : PB = m_1 : m_2$. Draw perpendiculars from $A$, $P$ and $B$ to the $x$-axis, and draw $AQ$ and $PC$ parallel to the $x$-axis, with $Q$ on the perpendicular from $P$ and $C$ on the perpendicular from $B$. Triangles $APQ$ and $PBC$ are similar by the AA criterion, so
$$ \frac{AP}{PB} = \frac{AQ}{PC} = \frac{m_1}{m_2} $$
Here $AQ = x - x_1$ and $PC = x_2 - x$. So $\frac{x - x_1}{x_2 - x} = \frac{m_1}{m_2}$, which gives $m_2(x - x_1) = m_1(x_2 - x)$, and therefore
$$ x = \frac{m_1 x_2 + m_2 x_1}{m_1 + m_2} $$
The same argument with vertical distances gives the formula for $y$.

## The Midpoint

A special case of the section formula is the midpoint. The mid-point of a line segment divides the line segment in the ratio 1 : 1. Therefore, the coordinates of the mid-point P of the join of the points A( $x_{1}, y_{1}$ ) and B( $x_{2}, y_{2}$ ) is

$$ \left(\frac {1 \cdot x _ {1} + 1 \cdot x _ {2}}{1 + 1}, \frac {1 \cdot y _ {1} + 1 \cdot y _ {2}}{1 + 1}\right) = \left(\frac {x _ {1} + x _ {2}}{2}, \frac {y _ {1} + y _ {2}}{2}\right). $$

## Worked example

Let us solve an example based on the section formula. Find the coordinates of the point which divides the line segment joining the points $(4, -3)$ and $(8, 5)$ in the ratio $3:1$ internally.

Let $\mathrm{P}(x, y)$ be the required point. Using the section formula, we get

$$ x = \frac {3 \times 8 + 1 \times 4}{3 + 1} = \frac {24 + 4}{4} = \frac {28}{4} = 7 $$

$$ y = \frac {3 \times 5 + 1 \times (-3)}{3 + 1} = \frac {15 - 3}{4} = \frac {12}{4} = 3 $$

Therefore, the coordinates of the required point are $(7, 3)$.

As a check, the distance from $(4, -3)$ to $(7, 3)$ is $\sqrt{3^2 + 6^2} = \sqrt{45}$, and the distance from $(7, 3)$ to $(8, 5)$ is $\sqrt{1^2 + 2^2} = \sqrt{5}$. Since $\sqrt{45} = 3\sqrt{5}$, the ratio of the two distances is $3 : 1$, as required.

Example (midpoint): Find the mid-point of the segment joining $(-2, 8)$ and $(6, -4)$. The mid-point is $\left(\frac{-2 + 6}{2}, \frac{8 + (-4)}{2}\right) = (2, 2)$.

## Key points

*   The section formula gives the coordinates of a point that divides a line segment joining two points $(x_1, y_1)$ and $(x_2, y_2)$ in a given ratio $m_1 : m_2$.
*   The formula for internal division is $\left(\frac {m _ {1} x _ {2} + m _ {2} x _ {1}}{m _ {1} + m _ {2}}, \frac {m _ {1} y _ {2} + m _ {2} y _ {1}}{m _ {1} + m _ {2}}\right)$.
*   The midpoint is a special case of the section formula where the ratio is $1:1$, giving the coordinates $\left(\frac {x _ {1} + x _ {2}}{2}, \frac {y _ {1} + y _ {2}}{2}\right)$.
*   If the ratio is given as $k:1$, the coordinates of the point P will be $\left(\frac {k x _ {2} + x _ {1}}{k + 1}, \frac {k y _ {2} + y _ {1}}{k + 1}\right)$.
*   You can verify your answer by checking that the ratio of the distances from the point to the endpoints matches the given ratio.