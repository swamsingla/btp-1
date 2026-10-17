---
{
  "concept": "Area Between Two Curves",
  "slug": "area-between-two-curves",
  "grade": 12,
  "language": "en",
  "subject": "maths",
  "area": "Calculus",
  "model": "sarvam-105b",
  "settings": {
    "temperature": 0.3,
    "max_tokens": 8000,
    "reasoning_effort": "none"
  },
  "usage": {
    "completion_tokens": 2217,
    "prompt_tokens": 5142,
    "total_tokens": 7359,
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
  "generated_at": "2026-10-08T05:17:57",
  "source_grade": 12,
  "grade_delta": 0,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g12_maths_part2_chapter2_003",
      "chapter": "chapter2",
      "section": "8.2 Area under Simple Curves"
    },
    {
      "ref": "S2",
      "passage_id": "g12_maths_part2_chapter1_058",
      "chapter": "chapter1",
      "section": "7.8.1 Area function"
    },
    {
      "ref": "S3",
      "passage_id": "g12_maths_part2_chapter2_001",
      "chapter": "chapter2",
      "section": "8.1 Introduction"
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
    "explanatory_paragraphs_without_a_citation": 5,
    "words": 1359,
    "target_words": [
      1050,
      1450
    ],
    "untraceable_sections": 0,
    "ok": true,
    "structural_problems": []
  },
  "terms": [
    "area between two curves",
    "definite integral",
    "elementary strip",
    "horizontal strips",
    "area function"
  ]
}
---

# Area Between Two Curves

In Grade 12 mathematics, you already know how to calculate the area under a single curve using definite integrals. However, many real-world problems require finding the space enclosed between two different functions. For instance, a civil engineer might need to know the area between a parabolic arch and a straight road to calculate the volume of earth to be moved. This page explains how to use integral calculus to find the exact area between two curves, $y = f(x)$ and $y = g(x)$, over a specific interval.

## The Basic Idea

Imagine you are looking at a map of two rivers that run parallel to each other but curve and bend slightly. If you want to know the total land area between the banks of these two rivers over a stretch of land from point $a$ to point $b$, you cannot simply use basic geometry formulas for rectangles. Instead, you can imagine slicing the land into thousands of incredibly thin vertical strips. Each strip has a very small width, $dx$, and a height that represents the distance between the two riverbanks at that specific $x$ coordinate. 

To find the area of one of these tiny strips, you multiply its height by its width. The height of the strip is the difference between the top riverbank and the bottom riverbank. If the top riverbank is represented by $y = f(x)$ and the bottom riverbank is represented by $y = g(x)$, then the height of the strip is $f(x) - g(x)$. The area of this elementary strip, which we call $dA$, is therefore $(f(x) - g(x))dx$.

To find the total area between the curves, we add up the areas of all these tiny strips from the starting point $x = a$ to the ending point $x = b$. In calculus, adding up an infinite number of infinitely small quantities is exactly what a definite integral does. We express this total area, which we can call $A$, as:
$$
\mathrm{A} = \int_ {a} ^ {b} [f(x) - g(x)] dx
$$
This formula gives the exact area between the two curves. It is important to note that this formula assumes $f(x) \ge g(x)$ for all $x$ in the interval $[a, b]$. If the curves cross each other, you must find the exact points of intersection and split the integral into separate parts.

## Using Horizontal Strips

Sometimes, it is much easier to calculate the area between two curves by using horizontal strips instead of vertical ones. This method is particularly useful when the curves are better expressed as functions of $y$, meaning the equations are in the form $x = f(y)$ and $x = g(y)$. 

In this orientation, we slice the region into very thin horizontal strips. Each strip has a small height $dy$. The width of the strip is the horizontal distance between the two curves. If the rightmost curve is $x = f(y)$ and the leftmost curve is $x = g(y)$, then the width of the strip is $f(y) - g(y)$. The elementary area of this horizontal strip, $dA$, is therefore $(f(y) - g(y))dy$.

To find the total area, we integrate this width with respect to $y$, from the bottom of the region $y = c$ to the top $y = d$. The formula for the area using horizontal strips is:
$$
\mathrm{A} = \int_ {c} ^ {d} [f(y) - g(y)] dy
$$
Choosing between vertical and horizontal strips depends on which method requires less algebraic manipulation. For example, if the curves are given by $x = y^2$ and $x = y + 2$, it is much easier to integrate with respect to $y$ than to solve for $y$ and integrate with respect to $x$.

## Dealing with Negative Areas

When you calculate a definite integral, the result can sometimes be negative. In the context of area, a negative result does not mean the physical area is negative. It simply means that the function you subtracted from was actually below the function you subtracted it from over that interval.

The definite integral calculates a signed area. If the region lies entirely below the $x$-axis, the integral will yield a negative number. However, area is a physical quantity and must always be a positive value. Therefore, if your integral result is negative, you must take its absolute value to find the actual area. This is written as $\left|\int_{a}^{b} f(x) dx\right|$.

In more complex scenarios, a single curve might cross the $x$-axis multiple times between $a$ and $b$. In this case, the region is split into sub-regions. Some parts will yield a positive area, and others will yield a negative area. To find the total geometric area, you must add the absolute values of the areas of all the sub-regions. For example, if a curve creates two regions, one with area $A_1$ and another with area $A_2$, the total area is $|A_1| + |A_2|$.

## Worked example

Let us apply the rule for finding the area between two curves to a practical problem. Consider the parabola $y = x^2$ and the straight line $y = 4 - x^2$. We want to find the exact area of the region enclosed between these two curves.

First, we need to find the points where the curves intersect. We set the equations equal to each other:
$$
x^2 = 4 - x^2
$$
Adding $x^2$ to both sides gives $2x^2 = 4$. Dividing by 2 gives $x^2 = 2$, which means $x = \sqrt{2}$ and $x = -\sqrt{2}$. These are our limits of integration, $a = -\sqrt{2}$ and $b = \sqrt{2}$.

Next, we identify which function is on top and which is on the bottom within this interval. If we test $x = 0$, we get $y = 0$ for the parabola and $y = 4$ for the line. Since $4 > 0$, the line $y = 4 - x^2$ is the top curve and the parabola $y = x^2$ is the bottom curve.

Using the formula for the area between two curves, we subtract the bottom function from the top function and integrate from $-\sqrt{2}$ to $\sqrt{2}$:
$$
\mathrm{A} = \int_{-\sqrt{2}}^{\sqrt{2}} [(4 - x^2) - x^2] dx
$$
Simplifying the expression inside the integral:
$$
\mathrm{A} = \int_{-\sqrt{2}}^{\sqrt{2}} (4 - 2x^2) dx
$$
Now, we integrate term by term:
$$
\mathrm{A} = \left[ 4x - \frac{2x^3}{3} \right]_{-\sqrt{2}}^{\sqrt{2}}
$$
Evaluating at the upper limit $x = \sqrt{2}$:
$$
4(\sqrt{2}) - \frac{2(\sqrt{2})^3}{3} = 4\sqrt{2} - \frac{2(2\sqrt{2})}{3} = 4\sqrt{2} - \frac{4\sqrt{2}}{3} = \frac{12\sqrt{2} - 4\sqrt{2}}{3} = \frac{8\sqrt{2}}{3}
$$
Evaluating at the lower limit $x = -\sqrt{2}$:
$$
4(-\sqrt{2}) - \frac{2(-\sqrt{2})^3}{3} = -4\sqrt{2} - \frac{2(-2\sqrt{2})}{3} = -4\sqrt{2} + \frac{4\sqrt{2}}{3} = \frac{-12\sqrt{2} + 4\sqrt{2}}{3} = -\frac{8\sqrt{2}}{3}
$$
Subtracting the lower limit evaluation from the upper limit evaluation:
$$
\mathrm{A} = \frac{8\sqrt{2}}{3} - \left(-\frac{8\sqrt{2}}{3}\right) = \frac{16\sqrt{2}}{3}
$$
Since $\sqrt{2} \approx 1.414$, the area is approximately $7.54$ square units. This exact value represents the total space enclosed by the parabola and the line.

## Key points

*   The area between two curves $y = f(x)$ and $y = g(x)$ from $x = a$ to $x = b$ is found by integrating the difference of the functions: $\int_ {a} ^ {b} [f(x) - g(x)] dx$, provided $f(x) \ge g(x)$ in that interval.
*   If the curves cross, you must find the intersection points and split the integral into separate intervals where one function is consistently on top.
*   When using horizontal strips, the area is calculated as $\int_ {c} ^ {d} [f(y) - g(y)] dy$, where $f(y)$ is the right curve and $g(y)$ is the left curve.
*   A definite integral can yield a negative value, but physical area must always be positive. If the result is negative, take the absolute value, $\left|\int_{a}^{b} f(x) dx\right|$, and add the absolute values of any sub-regions.
*   The Area function, denoted $A(x)$, represents the accumulated area from a fixed starting point $a$ to a variable point $x$ on the x-axis, defined as $A(x) = \int_{a}^{x} f(x) dx$, and its properties are governed by the Fundamental Theorems of Calculus.