---
{
  "concept": "Cartesian Coordinate System",
  "slug": "cartesian-coordinate-system",
  "grade": 9,
  "language": "en",
  "subject": "maths",
  "area": "Coordinate Geometry",
  "hand_edited": "2026-10-17: held because the generated page had no citation tags (0 of 7 explanatory paragraphs cited). The text was accurate but it referred to points P and Q that it never defined (they come from a figure in the book). Rewritten by hand from Sections 3.1-3.2 with tags: P and Q now described in words, and the book's motivation (dot on a sheet, seating plan (5, 3), Descartes) and points on the axes added. The worked example R(-5, 2) is not in the book; it is consistent with the sign rules and its quadrant checked.",
  "model": "sarvam-105b",
  "settings": {
    "temperature": 0.3,
    "max_tokens": 8000,
    "reasoning_effort": "none"
  },
  "usage": {
    "completion_tokens": 1483,
    "prompt_tokens": 6168,
    "total_tokens": 7651,
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
  "generated_at": "2026-10-17T04:59:07",
  "source_grade": 9,
  "grade_delta": 0,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g9_maths_chapter3_007",
      "chapter": "chapter3",
      "section": "3.2 Cartesian System"
    },
    {
      "ref": "S2",
      "passage_id": "g9_maths_chapter3_004",
      "chapter": "chapter3",
      "section": "3.1 Introduction"
    }
  ],
  "citation_check": {
    "cited": [
      "1",
      "2"
    ],
    "invented_citations": [],
    "unused_sources": [],
    "explanatory_paragraphs_without_a_citation": 0,
    "words": 1273,
    "target_words": [
      1000,
      1350
    ],
    "untraceable_sections": 0,
    "ok": true,
    "structural_problems": []
  },
  "terms": [
    "cartesian plane",
    "origin",
    "x-axis",
    "y-axis",
    "quadrants",
    "abscissa",
    "ordinate",
    "coordinates"
  ]
}
---

# Cartesian Coordinate System

On a number line, one number is enough to describe the position of a point. There are many other situations in which we need to describe a position with reference to more than one line. This page shows how two perpendicular number lines let us describe the position of any point in a plane.

## Why Two Pieces of Information Are Needed

Suppose you put a dot on a sheet of paper. Saying "the dot is in the upper half of the paper" or "it is near the left edge" does not fix its position precisely. If you also say that the dot is nearly 5 cm away from the left edge, it gives some idea but still does not fix the position. If you add that the dot is at a distance of 9 cm above the bottom line, we know exactly where the dot is. We fixed the position by specifying its distances from two fixed lines, the left edge and the bottom line of the paper, so we need two independent pieces of information.

A seating plan works in the same way. The position of a student is described precisely by the column in which she or he sits and the row in which she or he sits. A desk in the 5th column and 3rd row can be written as $(5, 3)$, with the column number first and then the row number.

In general, the position of any object lying in a plane can be represented with the help of two perpendicular lines. This idea gave rise to an important branch of mathematics known as Coordinate Geometry. It was developed by the French philosopher and mathematician René Descartes, and in his honour the system for describing the position of a point in a plane is also known as the Cartesian system.

## The Axes and the Origin

Take two number lines, call them $X'X$ and $Y'Y$. Place $X'X$ horizontally and write the numbers on it just as on the number line, and do the same with $Y'Y$, except that $Y'Y$ is vertical. Combine the two lines so that they cross each other at their zeroes, or origins.

The horizontal line $X'X$ is called the $x$-axis and the vertical line $Y'Y$ is called the $y$-axis. The point where $X'X$ and $Y'Y$ cross is called the origin, and it is denoted by $O$. Since the positive numbers lie in the directions $OX$ and $OY$, these are called the positive directions of the $x$-axis and the $y$-axis. Similarly, $OX'$ and $OY'$ are called the negative directions of the $x$-axis and the $y$-axis.

## Quadrants

The axes divide the plane into four parts, called quadrants, numbered I, II, III and IV anticlockwise from $OX$. The plane consists of the axes and these quadrants. We call the plane the Cartesian plane, or the coordinate plane, or the $xy$-plane, and the axes are called the coordinate axes.

## Coordinates of a Point

Take a point $P$ whose perpendicular distance from the $y$-axis, measured along the positive direction of the $x$-axis, is 4 units, and whose perpendicular distance from the $x$-axis, measured along the positive direction of the $y$-axis, is 3 units. Take a point $Q$ whose distance from the $y$-axis, measured along the negative direction of the $x$-axis, is 6 units, and whose distance from the $x$-axis, measured along the negative direction of the $y$-axis, is 2 units. To describe such points without confusion, we write their coordinates using these conventions:

*   The $x$-coordinate of a point is its perpendicular distance from the $y$-axis measured along the $x$-axis, positive along the positive direction of the $x$-axis and negative along the negative direction. For $P$ it is $+4$ and for $Q$ it is $-6$. The $x$-coordinate is also called the abscissa.
*   The $y$-coordinate of a point is its perpendicular distance from the $x$-axis measured along the $y$-axis, positive along the positive direction of the $y$-axis and negative along the negative direction. For $P$ it is $+3$ and for $Q$ it is $-2$. The $y$-coordinate is also called the ordinate.
*   The $x$-coordinate comes first, and then the $y$-coordinate, and we place the coordinates in brackets. Hence the coordinates of $P$ are $(4, 3)$ and the coordinates of $Q$ are $(-6, -2)$.

The coordinates describe a point in the plane uniquely, and $(3, 4)$ is not the same as $(4, 3)$. The system of writing the abscissa first is only a convention, accepted all over the world, to avoid confusion.

## Points on the Axes

A point at a distance of $+4$ units from the $y$-axis and at distance zero from the $x$-axis has $x$-coordinate 4 and $y$-coordinate 0, so its coordinates are $(4, 0)$. Every point lying on the $x$-axis has zero distance from the $x$-axis, so the $y$-coordinate of every point on the $x$-axis is always zero. Thus the coordinates of any point on the $x$-axis are of the form $(x, 0)$, where $x$ is the distance of the point from the $y$-axis. Similarly, the coordinates of any point on the $y$-axis are of the form $(0, y)$, where $y$ is the distance of the point from the $x$-axis.

The origin $O$ has zero distance from both the axes, so its abscissa and ordinate are both zero, and the coordinates of the origin are $(0, 0)$.

## Signs of the Coordinates in the Quadrants

There is a relationship between the signs of the coordinates of a point and the quadrant in which it lies:

*   In the 1st quadrant the point is of the form $(+, +)$, since this quadrant is enclosed by the positive $x$-axis and the positive $y$-axis.
*   In the 2nd quadrant the point is of the form $(-, +)$, since it is enclosed by the negative $x$-axis and the positive $y$-axis.
*   In the 3rd quadrant the point is of the form $(-, -)$, since it is enclosed by the negative $x$-axis and the negative $y$-axis.
*   In the 4th quadrant the point is of the form $(+, -)$, since it is enclosed by the positive $x$-axis and the negative $y$-axis.

## Worked Example

A point $R$ is 5 units from the $y$-axis, measured along the negative direction of the $x$-axis, and 2 units from the $x$-axis, measured along the positive direction of the $y$-axis. Find its coordinates.

The $x$-coordinate (abscissa) of $R$ is $-5$, because the distance is measured along the negative direction of the $x$-axis. The $y$-coordinate (ordinate) of $R$ is $+2$, because the distance is measured along the positive direction of the $y$-axis. Since the $x$-coordinate comes first, the coordinates of $R$ are $(-5, 2)$. The signs $(-, +)$ show that $R$ lies in the 2nd quadrant.

## Key points

*   The position of a point in a plane is described with the help of two perpendicular lines, one horizontal and one vertical.
*   The horizontal line is the $x$-axis and the vertical line is the $y$-axis; they meet at the origin $O$.
*   The axes divide the plane into four quadrants, numbered I, II, III and IV anticlockwise from $OX$.
*   The $x$-coordinate, or abscissa, is the distance of a point from the $y$-axis, and the $y$-coordinate, or ordinate, is its distance from the $x$-axis.
*   Coordinates are written in the order $(x, y)$, and $(x, y) \neq (y, x)$ when $x \neq y$.
*   A point on the $x$-axis has coordinates $(x, 0)$, a point on the $y$-axis has coordinates $(0, y)$, and the origin is $(0, 0)$.
*   The coordinates have the signs $(+, +)$, $(-, +)$, $(-, -)$ and $(+, -)$ in the 1st, 2nd, 3rd and 4th quadrants.
