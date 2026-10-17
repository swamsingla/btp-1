---
{
  "concept": "Graphical Method for LPP",
  "slug": "graphical-method-lpp",
  "grade": 12,
  "language": "en",
  "subject": "maths",
  "area": "Optimisation",
  "model": "sarvam-105b",
  "settings": {
    "temperature": 0.3,
    "max_tokens": 8000,
    "reasoning_effort": "none"
  },
  "usage": {
    "completion_tokens": 1343,
    "prompt_tokens": 6204,
    "total_tokens": 7547,
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
  "generated_at": "2026-10-08T06:51:43",
  "source_grade": 12,
  "grade_delta": 0,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g12_maths_part2_chapter6_011",
      "chapter": "chapter6",
      "section": "12.2.2 Graphical method of solving linear programming problems"
    },
    {
      "ref": "S2",
      "passage_id": "g12_maths_part2_chapter6_001",
      "chapter": "chapter6",
      "section": "12.1 Introduction"
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
    "words": 953,
    "target_words": [
      1050,
      1450
    ],
    "untraceable_sections": 0,
    "ok": true,
    "structural_problems": [],
    "grounding": {
      "cited_sentences": 13,
      "checked": 13,
      "not_judgeable_mostly_maths": 0,
      "cites_a_source_never_given": 0,
      "unsupported": [
        {
          "claim": "For example, if you are a furniture dealer with a limited budget, your constraints might be $5x + y \\leq 100$ and $x + y \\leq 60$, along with non-negative constraints like $x \\geq 0$ and $y \\geq 0$ .",
          "cites": [
            "S1"
          ],
          "support_probability": 0.035
        },
        {
          "claim": "For instance, if your objective function is $Z = 250x + 75y$ and your corner points are $(0, 0)$, $(0, 60)$, $(10, 50)$, and $(20, 0)$, you calculate the value of $Z$ at each of these coordinates .",
          "cites": [
            "S1"
          ],
          "support_probability": 0.126
        },
        {
          "claim": "If your feasible region is bounded, the largest value you calculated is the maximum value of $Z$, and the smallest is the minimum value of $Z$ .",
          "cites": [
            "S1"
          ],
          "support_probability": 0.183
        },
        {
          "claim": "To do this, you graph the inequality $ax + by > \\text{M}$ or $ax + by < \\text{m}$ and see if the resulting open half-plane has any points in common with your feasible region .",
          "cites": [
            "S1"
          ],
          "support_probability": 0.053
        }
      ],
      "unsupported_fraction": 0.308,
      "threshold": 0.5,
      "max_unsupported_fraction": 0.34
    },
    "verification": {
      "verdict": "ok",
      "checks": 2,
      "tokens": 5518
    }
  },
  "terms": [
    "feasible region",
    "infeasible region",
    "feasible solution",
    "infeasible solution",
    "optimal solution",
    "linear programming problem",
    "objective function",
    "corner point",
    "vertex",
    "bounded",
    "unbounded",
    "convex region",
    "half plane"
  ]
}
---

# Graphical Method for LPP

The graphical method is a visual way to solve linear programming problems (LPP). You have already studied how to graph systems of linear inequalities in two variables. Now, you will use that skill to find the best possible outcome when you need to maximise profit or minimise cost. In a business, you might want to know the maximum profit you can make or the minimum cost to run a factory, given certain limits like budget and storage space. The graphical method helps you turn these real-life limits into lines on a graph so you can find the best solution.

## Plotting Constraints and Finding the Feasible Region

To start, you need to turn the limits of your problem into mathematical inequalities. For example, if you are a furniture dealer with a limited budget, your constraints might be $5x + y \leq 100$ and $x + y \leq 60$, along with non-negative constraints like $x \geq 0$ and $y \geq 0$. You graph each of these inequalities as a line on a coordinate plane. 

The area where all these shaded regions overlap is called the feasible region. Every point inside or on the boundary of this shaded area is a feasible solution, meaning it satisfies all your given limits. The region outside this overlap is called the infeasible region. Because you are dealing with linear programming, this feasible region will always be a convex polygon.

## The Corner Point Theorem

When you have a feasible region, you might wonder how to find the exact point that gives you the maximum profit. The extracts provide two fundamental theorems to help you. Theorem 1 states that if the objective function $Z = ax + by$ has an optimal value, that value must occur at a corner point, or vertex, of the feasible region. Theorem 2 adds that if the feasible region is bounded, the objective function will definitely have both a maximum and a minimum value, and each will occur at a corner point. 

If your feasible region is unbounded, it might not have a maximum or minimum value at all. However, if an optimal value does exist in an unbounded region, it must still occur at a corner point. Because of this, you do not need to test every single point in the shaded region. You only need to find the corner points.

## The Corner Point Method

Once you have identified the corner points of your feasible region, you can find the optimal solution using the Corner Point Method. The steps are straightforward. First, determine the coordinates of the corner points. You can do this by inspection or by solving the two equations of the lines that intersect at that point. 

Second, evaluate the objective function $Z = ax + by$ at each corner point. For instance, if your objective function is $Z = 250x + 75y$ and your corner points are $(0, 0)$, $(0, 60)$, $(10, 50)$, and $(20, 0)$, you calculate the value of $Z$ at each of these coordinates. 

Finally, compare these values. If your feasible region is bounded, the largest value you calculated is the maximum value of $Z$, and the smallest is the minimum value of $Z$. 

## Handling Special Cases

Sometimes, you might encounter special situations. If two corner points produce the same maximum or minimum value for the objective function, then every point on the line segment joining those two points will also give the same optimal value. 

If your region is unbounded, you must be careful. You might find a smallest or largest value at a corner point, but you need to check if the region actually extends further in that direction. To do this, you graph the inequality $ax + by > \text{M}$ or $ax + by < \text{m}$ and see if the resulting open half-plane has any points in common with your feasible region. If it does, then your value is not actually the maximum or minimum.

## Worked example

Let us apply the Corner Point Method to a simple problem. Maximise $Z = 4x + y$ subject to the constraints $x + y \leq 50$, $3x + y \leq 90$, and $x \geq 0, y \geq 0$. 

First, we graph the constraints to find the feasible region OABC. The corner points are $O(0, 0)$, $A(30, 0)$, $B(20, 30)$, and $C(0, 50)$. 

Next, we evaluate the objective function $Z = 4x + y$ at each of these points. At $O(0, 0)$, $Z = 0$. At $C(0, 50)$, $Z = 50$. At $B(20, 30)$, $Z = 4(20) + 30 = 110$. At $A(30, 0)$, $Z = 4(30) = 120$. 

Since the feasible region is bounded, the maximum value of $Z$ is 120, which occurs at the corner point $A(30, 0)$.

## Key points

* The feasible region is the common area determined by all constraints of a linear programming problem and it is always a convex region.
* The optimal value of the objective function $Z$ must occur at a corner point of the feasible region.
* If the feasible region is bounded, the objective function is guaranteed to have both a maximum and a minimum value.
* If two corner points yield the same optimal value, every point on the line segment joining them is also an optimal solution.
* For an unbounded region, you must verify the optimal value by checking if an open half-plane intersects the feasible region.