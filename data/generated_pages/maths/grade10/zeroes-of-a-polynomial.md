---
{
  "concept": "Zeroes of a Polynomial",
  "slug": "zeroes-of-a-polynomial",
  "grade": 10,
  "language": "en",
  "subject": "maths",
  "area": "Algebra",
  "model": "sarvam-105b",
  "settings": {
    "temperature": 0.3,
    "max_tokens": 8000,
    "reasoning_effort": "none"
  },
  "usage": {
    "completion_tokens": 1516,
    "prompt_tokens": 6650,
    "total_tokens": 8166,
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
  "generated_at": "2026-10-18T00:59:43",
  "source_grade": 10,
  "grade_delta": 0,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g10_maths_chapter2_004",
      "chapter": "chapter2",
      "section": "2.2 Geometrical Meaning of the Zeroes of a Polynomial"
    }
  ],
  "citation_check": {
    "cited": [
      "1"
    ],
    "invented_citations": [],
    "unused_sources": [],
    "explanatory_paragraphs_without_a_citation": 1,
    "words": 979,
    "target_words": [
      1000,
      1350
    ],
    "untraceable_sections": 0,
    "ok": true,
    "structural_problems": []
  },
  "terms": [
    "zero of a polynomial",
    "linear polynomial",
    "quadratic polynomial",
    "cubic polynomial",
    "degree of a polynomial",
    "parabola",
    "x-coordinate"
  ]
}
---

# Zeroes of a Polynomial

A zero of a polynomial is a value of $x$ for which the polynomial evaluates to zero. These values are important because they represent the exact points where the graph of the polynomial intersects the $x$-axis, providing a crucial visual and algebraic link.

## Geometrical Meaning of the Zeroes

You may already know that a real number $k$ is a zero of the polynomial $p(x)$ if $p(k) = 0$. To understand why these zeroes matter, we can look at the geometrical representations of linear and quadratic polynomials.

Consider a linear polynomial $ax + b$, where $a \neq 0$. The graph of $y = ax + b$ is a straight line which intersects the $x$-axis at exactly one point, namely, $\left(\frac{-b}{a}, 0\right)$. Therefore, the linear polynomial $ax + b$, $a \neq 0$, has exactly one zero, namely, the $x$-coordinate of the point where the graph of $y = ax + b$ intersects the $x$-axis.

Now, let us look for the geometrical meaning of a zero of a quadratic polynomial. Consider the quadratic polynomial $x^{2} - 3x - 4$. The graph of the corresponding equation $y = x^{2} - 3x - 4$ has one of the two shapes either open upwards like $\bigcup$ or open downwards like $\bigcap$ depending on whether $a > 0$ or $a < 0$ in $y = ax^{2} + bx + c$. These curves are called parabolas.

The zeroes of the quadratic polynomial $x^{2} - 3x - 4$ are precisely the $x$-coordinates of the points where the parabola representing $y = x^{2} - 3x - 4$ intersects the $x$-axis. From the graph, we can observe that it cuts the $x$-axis at two distinct points, $(-1, 0)$ and $(4, 0)$. Indeed, $x^{2} - 3x - 4 = (x + 1)(x - 4)$, so the two zeroes of the quadratic polynomial are $-1$ and $4$.

## Cases for Quadratic Polynomials

From our observation earlier about the shape of the graph of $y = ax^{2} + bx + c$, the following three cases can happen.

Case (i): Here, the graph cuts the $x$-axis at two distinct points. The $x$-coordinates of these points are the two zeroes of the quadratic polynomial.

Case (ii): Here, the graph cuts the $x$-axis at exactly one point, i.e., at two coincident points. So, the two points of Case (i) coincide here to become one point. The $x$-coordinate of this single point is the only zero for the quadratic polynomial.

Case (iii): Here, the graph is either completely above the $x$-axis or completely below the $x$-axis. So, it does not cut the $x$-axis at any point. In this case, the quadratic polynomial has no zero.

## Zeroes of Cubic Polynomials

Now, what do you expect the geometrical meaning of the zeroes of a cubic polynomial to be? Let us find out. Consider the cubic polynomial $x^3 - 4x$. To see what the graph of $y = x^3 - 4x$ looks like, let us list a few values of $y$ corresponding to a few values for $x$.

| $x$ | -2 | -1 | 0 | 1 | 2 |
| --- | --- | --- | --- | --- | --- |
| $y = x^3 - 4x$ | 0 | 3 | 0 | -3 | 0 |

If we locate the points listed above on a graph paper and draw the graph, we see that the graph of $y = x^3 - 4x$ actually looks like a curve that intersects the $x$-axis at three points. We see from the table above that -2, 0 and 2 are zeroes of the cubic polynomial. Observe that -2, 0 and 2 are, in fact, the $x$-coordinates of the only points where the graph of $y = x^3 - 4x$ intersects the $x$-axis.

Let us take a few more examples. Consider the cubic polynomials $x^3$ and $x^3 - x^2$. Note that 0 is the only zero of the polynomial $x^3$. Also, 0 is the $x$-coordinate of the only point where the graph of $y = x^3$ intersects the $x$-axis. Similarly, since $x^3 - x^2 = x^2 (x - 1)$, 0 and 1 are the only zeroes of the polynomial $x^3 - x^2$.

From the examples above, we see that there are at most 3 zeroes for any cubic polynomial. In other words, any polynomial of degree 3 can have at most three zeroes.

## General Rule for Polynomials

In general, given a polynomial $p(x)$ of degree $n$, the graph of $y = p(x)$ intersects the $x$-axis at at most $n$ points. Therefore, a polynomial $p(x)$ of degree $n$ has at most $n$ zeroes.

This means that a quadratic polynomial can have either two distinct zeroes or two equal zeroes (i.e., one zero), or no zero. This also means that a polynomial of degree 2 has at most two zeroes.

## Worked Example

Consider the cubic polynomial $p(x) = x^3 - 5x^2 + 6x$. To find the zeroes, we can factor the polynomial as $x(x - 2)(x - 3)$. Therefore, the zeroes are $x = 0$, $x = 2$, and $x = 3$.

To verify these zeroes geometrically, we can observe that the graph of $y = x^3 - 5x^2 + 6x$ intersects the $x$-axis at three distinct points, and the $x$-coordinates of these points are the zeroes we found.

## Key points

*   A zero of a polynomial $p(x)$ is a number $k$ such that $p(k) = 0$.
*   The zeroes of a quadratic polynomial are precisely the $x$-coordinates of the points where the parabola representing $y = ax^2 + bx + c$ intersects the $x$-axis.
*   A quadratic polynomial can have either two distinct zeroes, two equal zeroes (i.e., one zero), or no zero.
*   Any polynomial of degree 3 can have at most three zeroes.
*   In general, given a polynomial $p(x)$ of degree $n$, the graph of $y = p(x)$ intersects the $x$-axis at at most $n$ points, and therefore a polynomial $p(x)$ of degree $n$ has at most $n$ zeroes.