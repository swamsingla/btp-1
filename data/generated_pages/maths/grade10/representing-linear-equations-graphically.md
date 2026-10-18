---
{
  "concept": "Graphing Linear Equations",
  "slug": "representing-linear-equations-graphically",
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
    "completion_tokens": 999,
    "prompt_tokens": 6776,
    "total_tokens": 7775,
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
  "generated_at": "2026-10-17T22:04:52",
  "source_grade": 10,
  "grade_delta": 0,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g10_maths_chapter3_004",
      "chapter": "chapter3",
      "section": "3.2 Graphical Method of Solution of a Pair of Linear Equations"
    },
    {
      "ref": "S2",
      "passage_id": "g10_maths_chapter3_009",
      "chapter": "chapter3",
      "section": "3.3 Algebraic Methods of Solving a Pair of Linear Equations"
    },
    {
      "ref": "S3",
      "passage_id": "g10_maths_chapter7_001",
      "chapter": "chapter7",
      "section": "7.1 Introduction"
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
    "words": 723,
    "target_words": [
      1000,
      1350
    ],
    "untraceable_sections": 0,
    "ok": true,
    "structural_problems": [
      "sections: no 'key points' section"
    ]
  },
  "terms": [
    "slope",
    "y-intercept",
    "cartesian coordinate plane",
    "rise over run",
    "rate of change",
    "slope-intercept form",
    "linear equation",
    "coordinate axes",
    "abscissa",
    "ordinate"
  ]
}
---

# Graphing Linear Equations

Graphing linear equations is the process of drawing a straight line on a Cartesian coordinate plane to represent all the possible solutions of a linear equation. You may already know how to plot a single point, but a line contains infinitely many points that satisfy the equation. This skill matters because it lets you see an equation as a picture, and because the point where two such lines meet gives the solution of a pair of linear equations.

## Solutions as Points on a Line

A linear equation in two variables, such as $x - 2y = 0$, has infinitely many solutions. Each solution is a pair of values $(x, y)$ that makes the equation true, and each pair can be plotted as a point. For $x - 2y = 0$, the pairs $(0, 0)$, $(2, 1)$ and $(4, 2)$ are solutions. Plotting them, we find that they lie on one straight line.

This is true in general: the graph of a linear equation in two variables is a straight line. Every point on the line gives a solution of the equation, and every solution gives a point on the line. A point that does not lie on the line is not a solution.

To draw the line, it is enough to find two solutions, plot them, and join them with a straight line. A third solution is useful as a check, because it must fall on the same line.

## The Slope-Intercept Form

Another way to graph a line is by using the slope-intercept form, which is written as $y = mx + c$. In this formula, $m$ represents the slope of the line, and $c$ represents the y-intercept. The y-intercept is the exact point where the line crosses the y-axis. Because the y-axis is the vertical axis, any point on it has an x-coordinate of zero, meaning the coordinates of the y-intercept are always $(0, c)$. 

The slope, $m$, tells you how steep the line is and whether it goes up or down as you move from left to right. If $m$ is a positive number, the line rises from left to right. If $m$ is a negative number, the line falls from left to right. A slope of zero means the line is perfectly flat, while a large positive or negative slope means the line is very steep.

## Plotting the Intercept and the Slope

To draw a line using $y = mx + c$, you first plot the y-intercept at $(0, c)$ on your graph paper. After marking this point, you use the slope $m$ to find your next point. The slope is defined as the "rise over run," which means you move vertically by the numerator and horizontally by the denominator. For example, if the slope is $2$, you can write it as $\frac{2}{1}$, meaning you move up 2 units and right 1 unit to find your next point. Once you have two points, you simply draw a straight line through them.

Consider the equation $y = 2x - 2$. Here, the y-intercept $c$ is $-2$, so you start by plotting the point $(0, -2)$. The slope $m$ is $2$, which is $\frac{2}{1}$. Starting from $(0, -2)$, you move up 2 units to $-2 + 2 = 0$, and right 1 unit to $1$. This gives you the second point $(1, 0)$. Drawing a line through $(0, -2)$ and $(1, 0)$ gives you the correct graph of the equation.

## Interpreting the Slope

The slope of a line is not just a number to memorise; it tells you how much $y$ changes for every increase of 1 in $x$. In the equation $y = 2x - 2$, the slope is $2$. This means that every time $x$ increases by 1, $y$ increases by 2. You can check this with the points we found: moving from $(0, -2)$ to $(1, 0)$, $x$ goes up by 1 and $y$ goes up by 2.

When the slope is negative, $y$ goes down as $x$ goes up. For example, if the temperature of a cooling drink is plotted against time, the line would have a negative slope. Always pay attention to the sign of the slope, as it tells you whether the line rises or falls from left to right.

## Worked example

Let us apply these rules to graph the equation $y = -4x + 3$. 

First, identify the y-intercept $c$, which is $3$. This means we start by plotting the point $(0, 3)$ on the y-axis. Next, look at the slope $m$, which is $-4$. We can write this as $\frac{-4}{1}$. Starting from $(0, 3)$, we apply the slope: we move down 4 units to $3 - 4 = -1$, and right 1 unit to $1$. This gives us our second point $(1, -1)$. Finally, we draw a straight line through $(0, 3)$ and $(1, -1)$. This line represents all the possible solutions to the equation $y = -4x + 3$.

## Two Lines on the Same Graph

If we draw the graphs of two linear equations on the same axes, there are three possibilities.

First, the lines may intersect at a single point. For example, the line $x - 2y = 0$ passes through $(0, 0)$, $(2, 1)$ and $(4, 2)$, and the line $3x + 4y - 20 = 0$ passes through $(4, 2)$ because $3(4) + 4(2) - 20 = 0$. The lines meet at $(4, 2)$, and this point is the one solution of the pair.

Second, the lines may be parallel. For example, $x + 2y - 4 = 0$ passes through $(4, 0)$ and $(0, 2)$, while $2x + 4y - 12 = 0$ passes through $(6, 0)$ and $(0, 3)$. These lines never meet, so the pair has no solution.

Third, the lines may coincide. For example, $2x + 3y - 9 = 0$ and $4x + 6y - 18 = 0$ both pass through $(0, 3)$ and $(3, 1)$, so they are the same line. Every point on it is a solution, so the pair has infinitely many solutions.

## Key points

*   The graph of a linear equation in two variables is a straight line; every point on it is a solution, and every solution is a point on it.
*   Two solutions are enough to draw the line, and a third is a useful check.
*   In the form $y = mx + c$, the line crosses the y-axis at $(0, c)$ and $m$ is the slope: $y$ changes by $m$ for each increase of 1 in $x$.
*   Two lines on the same graph can intersect (one solution), be parallel (no solution) or coincide (infinitely many solutions).