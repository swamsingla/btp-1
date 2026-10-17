---
{
  "concept": "Area of Triangle Using Determinants",
  "slug": "area-using-determinants",
  "grade": 12,
  "language": "en",
  "subject": "maths",
  "area": "Linear Algebra",
  "model": "sarvam-105b",
  "settings": {
    "temperature": 0.3,
    "max_tokens": 8000,
    "reasoning_effort": "none"
  },
  "usage": {
    "completion_tokens": 1310,
    "prompt_tokens": 5836,
    "total_tokens": 7146,
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
  "generated_at": "2026-10-08T07:31:26",
  "source_grade": 12,
  "grade_delta": 0,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g12_maths_part1_chapter4_015",
      "chapter": "chapter4",
      "section": "4.3 Area of a Triangle"
    },
    {
      "ref": "S2",
      "passage_id": "g12_maths_part2_chapter2_004",
      "chapter": "chapter2",
      "section": "8.2 Area under Simple Curves"
    },
    {
      "ref": "S3",
      "passage_id": "g12_maths_part1_chapter4_004",
      "chapter": "chapter4",
      "section": "4.2.2 Determinant of a matrix of order two"
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
    "explanatory_paragraphs_without_a_citation": 0,
    "words": 672,
    "target_words": [
      1050,
      1450
    ],
    "untraceable_sections": 0,
    "ok": true,
    "short": [
      "length: 672 words, under 1050"
    ],
    "structural_problems": [],
    "grounding": {
      "cited_sentences": 10,
      "checked": 8,
      "not_judgeable_mostly_maths": 2,
      "cites_a_source_never_given": 0,
      "unsupported": [
        {
          "claim": "For a $2 \\times 2$ matrix $\\mathrm{A} = \\begin{bmatrix} a_{11} & a_{12}\\\\ a_{21} & a_{22} \\end{bmatrix}$, the determinant is defined as $\\det (\\mathrm{A}) = | \\mathrm{A} | = \\Delta = \\left| \\begin{arr",
          "cites": [
            "S3"
          ],
          "support_probability": 0.407
        },
        {
          "claim": "To find the area of a triangle, we use a $3 \\times 3$ matrix where the first column contains the $x$-coordinates, the second column contains the $y$-coordinates, and the third column contains the cons",
          "cites": [
            "S1"
          ],
          "support_probability": 0.02
        }
      ],
      "unsupported_fraction": 0.25,
      "threshold": 0.5,
      "max_unsupported_fraction": 0.34
    },
    "verification": {
      "verdict": "spiralled",
      "checks": 2,
      "tokens": 11500
    }
  },
  "terms": [
    "determinant",
    "matrix",
    "absolute value",
    "collinear",
    "coordinates"
  ]
}
---

# Area of Triangle Using Determinants

The area of a triangle can be calculated using the coordinates of its vertices. In earlier classes, we have studied that the area of a triangle whose vertices are $(x_{1}, y_{1})$, $(x_{2}, y_{2})$, and $(x_{3}, y_{3})$, is given by the expression $\frac{1}{2}[x_{1}(y_{2}-y_{3}) + x_{2}(y_{3}-y_{1}) + x_{3}(y_{1}-y_{2})]$. This expression can be written in the form of a determinant as $\Delta = \frac {1}{2} \left| \begin{array}{c c c} x _ {1} & y _ {1} & 1 \\ x _ {2} & y _ {2} & 1 \\ x _ {3} & y _ {3} & 1 \end{array} \right|$. This method is a powerful tool in coordinate geometry, allowing for a compact and systematic calculation of area.

## The Determinant Formula

A determinant is a special number that can be calculated from a square matrix. For a $2 \times 2$ matrix $\mathrm{A} = \begin{bmatrix} a_{11} & a_{12}\\ a_{21} & a_{22} \end{bmatrix}$, the determinant is defined as $\det (\mathrm{A}) = | \mathrm{A} | = \Delta = \left| \begin{array}{c c} a_{11} & a_{12} \\ a_{21} & a_{22} \end{array} \right| = a_{11} a_{22} - a_{21} a_{12}$. To find the area of a triangle, we use a $3 \times 3$ matrix where the first column contains the $x$-coordinates, the second column contains the $y$-coordinates, and the third column contains the constant $1$ for each vertex.

The formula for the area of a triangle is $\Delta = \frac {1}{2} \left| \begin{array}{c c c} x_{1} & y_{1} & 1 \\ x_{2} & y_{2} & 1 \\ x_{3} & y_{3} & 1 \end{array} \right|$. The absolute value is taken because area is a positive quantity. If the area is given, we can use both positive and negative values of the determinant for calculation.

## Calculating the Determinant

To calculate the area, we expand the $3 \times 3$ determinant along the first row. The formula is $\frac {1}{2} [ x_{1} (y_{2} \cdot 1 - 1 \cdot y_{3}) - y_{1} (x_{2} \cdot 1 - 1 \cdot x_{3}) + 1 (x_{2} y_{3} - y_{2} x_{3}) ]$. This simplifies to $\frac {1}{2} [ x_{1} (y_{2} - y_{3}) - y_{1} (x_{2} - x_{3}) + (x_{2} y_{3} - x_{3} y_{2}) ]$.

The area of the triangle formed by three collinear points is zero. This is because the points lie on a straight line, so they do not form a triangle with a non-zero area.

## Worked example

Find the area of the triangle whose vertices are (3, 8), (-4, 2) and (5, 1).

Solution:
The area of triangle is given by
$$
\Delta = \frac {1}{2} \left| \begin{array}{c c c} 3 & 8 & 1 \\ - 4 & 2 & 1 \\ 5 & 1 & 1 \end{array} \right|
$$

Expanding the determinant along the first row:
$$
\begin{array}{l}
= \frac {1}{2} [ 3 (2 \cdot 1 - 1 \cdot 1) - 8 ((-4) \cdot 1 - 1 \cdot 5) + 1 ((-4) \cdot 1 - 2 \cdot 5) ] \\
= \frac {1}{2} [ 3 (2 - 1) - 8 (-4 - 5) + 1 (-4 - 10) ] \\
= \frac {1}{2} [ 3(1) - 8(-9) + 1(-14) ] \\
= \frac {1}{2} [ 3 + 72 - 14 ] \\
= \frac {1}{2} [ 61 ] \\
= \frac {61}{2}
\end{array}
$$

## Key points
- The area of a triangle with vertices $(x_{1}, y_{1})$, $(x_{2}, y_{2})$, and $(x_{3}, y_{3})$ is given by $\Delta = \frac {1}{2} \left| \begin{array}{c c c} x_{1} & y_{1} & 1 \\ x_{2} & y_{2} & 1 \\ x_{3} & y_{3} & 1 \end{array} \right|$.
- The absolute value is taken because area is a positive quantity.
- If the area is given, use both positive and negative values of the determinant for calculation.
- The area of the triangle formed by three collinear points is zero.
- The formula can be expanded along any row or column.