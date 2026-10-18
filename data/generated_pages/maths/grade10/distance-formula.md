---
{
  "concept": "Distance Formula",
  "slug": "distance-formula",
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
    "completion_tokens": 1984,
    "prompt_tokens": 6848,
    "total_tokens": 8832,
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
  "generated_at": "2026-10-17T22:37:01",
  "source_grade": 10,
  "grade_delta": 0,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g10_maths_chapter7_006",
      "chapter": "chapter7",
      "section": "7.2 Distance Formula"
    },
    {
      "ref": "S2",
      "passage_id": "g10_maths_chapter4_015",
      "chapter": "chapter4",
      "section": "4.4 Nature of Roots"
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
    "explanatory_paragraphs_without_a_citation": 2,
    "words": 1100,
    "target_words": [
      1000,
      1350
    ],
    "untraceable_sections": 0,
    "ok": true,
    "structural_problems": [
      "questioning: 7 question marks — written as a worksheet"
    ]
  },
  "terms": [
    "distance formula",
    "cartesian coordinate system",
    "pythagorean theorem",
    "right-angled triangle",
    "coordinates",
    "origin",
    "perpendicular"
  ]
}
---

# Distance Formula

How do you measure the distance between two towns if you cannot use a tape measure? In Grade 9, you learned the Cartesian Coordinate System, which allows us to describe any location using a pair of numbers. In earlier classes, you learned the Pythagorean Theorem, which relates the sides of a right-angled triangle. This page brings those two ideas together to help you find the distance between any two points on a graph without ever touching a ruler.

## Points on the Axes

Before finding the distance between two random points, it helps to understand the simpler cases. If two points lie on the $x$-axis, we can easily find the distance between them. For instance, consider two points $A(4, 0)$ and $B(6, 0)$. The points $A$ and $B$ lie on the $x$-axis. If you plot them, you can see that $OA = 4$ units and $OB = 6$ units, where $O$ is the origin. Therefore, the distance of $B$ from $A$, i.e., $AB = OB - OA = 6 - 4 = 2$ units. So, if two points lie on the $x$-axis, we can easily find the distance between them.

Now, suppose we take two points lying on the $y$-axis. If the points $C(0, 3)$ and $D(0, 8)$ lie on the $y$-axis, similarly we find that $CD = 8 - 3 = 5$ units.

## The Pythagorean Theorem

Next, we can find the distance of $A$ from $C$. Since $OA = 4$ units and $OC = 3$ units, and $\angle AOC = 90^\circ$, the distance of $A$ from $C$ is $AC = \sqrt{3^{2} + 4^{2}} = 5$ units. Similarly, the distance of $B$ from $D$ is $BD = \sqrt{6^{2} + 8^{2}} = 10$ units.

Two points that do not lie on a coordinate axis also have a distance between them, and we find it with the Pythagorean theorem. Let us see an example.

The points $P(4, 6)$ and $Q(6, 8)$ lie in the first quadrant. Let us draw $PR$ and $QS$ perpendicular to the $x$-axis from $P$ and $Q$ respectively. Also, draw a perpendicular from $P$ on $QS$ to meet $QS$ at $T$. Then the coordinates of $R$ and $S$ are $(4, 0)$ and $(6, 0)$, respectively. So, $RS = 2$ units. Also, $QS = 8$ units and $TS = PR = 6$ units. Therefore, $QT = 2$ units and $PT = RS = 2$ units. Now, using the Pythagorean theorem, we have
$$ \begin{array}{r l} \mathrm{PQ} ^ {2} & = \mathrm{PT} ^ {2} + \mathrm{QT} ^ {2} \\ & = 2 ^ {2} + 2 ^ {2} = 8 \end{array} $$
$$ \mathrm{PQ} = 2 \sqrt {2} \text{ units} $$
The same method works for two points in different quadrants. Consider the points $P(6, 4)$ and $Q(-5, -3)$. Draw $QS$ perpendicular to the $x$-axis. Also draw a perpendicular $PT$ from the point $P$ on $QS$ (extended), meeting it at $T(-5, 4)$. Then $PT = 6 - (-5) = 11$ units and $QT = 4 - (-3) = 7$ units. Using the Pythagorean Theorem in the right triangle $PTQ$, we get $PQ = \sqrt{11^{2} + 7^{2}} = \sqrt{170}$ units.

## The General Formula

Let us now find the distance between any two points $P(x_{1}, y_{1})$ and $Q(x_{2}, y_{2})$. Draw $PR$ and $QS$ perpendicular to the $x$-axis. A perpendicular from the point $P$ on $QS$ is drawn to meet it at the point $T$. Then, $OR = x_{1}$, $OS = x_{2}$. So, $RS = x_{2} - x_{1} = PT$. Also, $SQ = y_{2}$, $ST = PR = y_{1}$. So, $QT = y_{2} - y_{1}$. Now, applying the Pythagorean theorem in $\Delta PTQ$, we get
$$ \begin{array}{r l} \mathrm{PQ} ^ {2} & = \mathrm{PT} ^ {2} + \mathrm{QT} ^ {2} \\ & = (x _ {2} - x _ {1}) ^ {2} + (y _ {2} - y _ {1}) ^ {2} \\ \mathrm{PQ} & = \sqrt {(x _ {2} - x _ {1}) ^ {2} + (y _ {2} - y _ {1}) ^ {2}} \end{array} $$
Note that since distance is always non-negative, we take only the positive square root. So, the distance between the points $\mathrm{P}(x_1, y_1)$ and $\mathrm{Q}(x_2, y_2)$ is
$$ \mathrm{PQ} = \sqrt {\left(x _ {2} - x _ {1}\right) ^ {2} + \left(y _ {2} - y _ {1}\right) ^ {2}}, $$
which is called the distance formula.

Remarks:

1. In particular, the distance of a point $\mathrm{P}(x,y)$ from the origin $\mathrm{O}(0,0)$ is given by $\mathrm{OP} = \sqrt{x^{2} + y^{2}}$.

2. We can also write $\mathrm{PQ} = \sqrt{\left(x_1 - x_2\right)^2 + \left(y_1 - y_2\right)^2}$. This is the same value, because $(x_1 - x_2)^2 = (x_2 - x_1)^2$ and $(y_1 - y_2)^2 = (y_2 - y_1)^2$.

## Worked Example

Let us apply the distance formula to find the distances between three points: $P(3, 2)$, $Q(-2, -3)$ and $R(2, 3)$. We have
$$ \mathrm{PQ} = \sqrt {(3 - (-2)) ^ {2} + (2 - (-3)) ^ {2}} = \sqrt {5 ^ {2} + 5 ^ {2}} = \sqrt {50} = 7.07 \text{ (approx.)} $$
$$ \mathrm{QR} = \sqrt {(-2 - 2) ^ {2} + (-3 - 3) ^ {2}} = \sqrt {(- 4) ^ {2} + (- 6) ^ {2}} = \sqrt {52} = 7.21 \text{ (approx.)} $$
$$ \mathrm{PR} = \sqrt {(3 - 2) ^ {2} + (2 - 3) ^ {2}} = \sqrt {1 ^ {2} + (- 1) ^ {2}} = \sqrt {2} = 1.41 \text{ (approx.)} $$
Since the sum of any two of these distances is greater than the third distance, therefore, the points $P$, $Q$ and $R$ form a triangle. Also, $\mathrm{PQ}^2 +\mathrm{PR}^2 = \mathrm{QR}^2$, by the converse of Pythagoras theorem, we have $\angle \mathrm{P} = 90^{\circ}$. Therefore, $PQR$ is a right triangle.

## Key points

*   The distance formula is derived from the Pythagorean theorem and is used to find the distance between two points $P(x_{1}, y_{1})$ and $Q(x_{2}, y_{2})$ on a Cartesian plane.
*   The formula is $PQ = \sqrt{(x_{2} - x_{1})^{2} + (y_{2} - y_{1})^{2}}$.
*   If you subtract the coordinates in the opposite order, such as $(x_{1} - x_{2})^{2}$, the result is the same because squaring a negative number yields a positive number.
*   Distance is always a non-negative value, so we always take the positive square root when applying the formula.
*   You can use the distance formula to check if three points form a specific type of triangle, such as a right triangle, by verifying if the Pythagorean theorem holds true.