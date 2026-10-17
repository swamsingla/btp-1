---
{
  "concept": "Linear Programming",
  "slug": "linear-programming",
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
    "completion_tokens": 1355,
    "prompt_tokens": 6260,
    "total_tokens": 7615,
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
  "generated_at": "2026-10-08T07:38:20",
  "source_grade": 12,
  "grade_delta": 0,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g12_maths_part2_chapter6_009",
      "chapter": "chapter6",
      "section": "12.2.2 Graphical method of solving linear programming problems"
    },
    {
      "ref": "S2",
      "passage_id": "g12_maths_part2_chapter6_002",
      "chapter": "chapter6",
      "section": "12.2 Linear Programming Problem and its Mathematical Formulation"
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
    "explanatory_paragraphs_without_a_citation": 1,
    "words": 987,
    "target_words": [
      1050,
      1450
    ],
    "untraceable_sections": 0,
    "ok": true,
    "structural_problems": [],
    "grounding": {
      "cited_sentences": 9,
      "checked": 9,
      "not_judgeable_mostly_maths": 0,
      "cites_a_source_never_given": 0,
      "unsupported": [
        {
          "claim": "The coefficients $a$ and $b$ are constants that represent the profit or cost per unit of each variable .",
          "cites": [
            "S1"
          ],
          "support_probability": 0.041
        },
        {
          "claim": "The same logic applies to finding the minimum value $m$ using the inequality $ax + by < m$ .",
          "cites": [
            "S1"
          ],
          "support_probability": 0.311
        }
      ],
      "unsupported_fraction": 0.222,
      "threshold": 0.5,
      "max_unsupported_fraction": 0.34
    },
    "verification": {
      "verdict": "ok",
      "checks": 1,
      "tokens": 1558
    }
  },
  "terms": [
    "linear programming",
    "objective function",
    "constraints",
    "feasible region",
    "feasible solution",
    "infeasible solution",
    "optimal solution",
    "corner point",
    "vertex",
    "bounded",
    "unbounded",
    "linear inequalities",
    "corner point method"
  ]
}
---

# Linear Programming

Linear programming is a powerful mathematical technique used to find the best possible outcome, such as maximum profit or minimum cost, given a set of limited resources. It helps decision-makers, like a furniture dealer deciding how many tables and chairs to stock, to make optimal choices under strict constraints.

## The Objective Function

The goal of any linear programming problem is to optimize a specific quantity. This quantity is expressed mathematically using an objective function. The objective function is a linear equation that represents the value we want to maximize or minimize, such as total profit or total cost. It is typically written in the form $Z = ax + by$, where $Z$ is the quantity to be optimized, and $x$ and $y$ are the variables representing the decisions to be made. The coefficients $a$ and $b$ are constants that represent the profit or cost per unit of each variable.

## Constraints and the Feasible Region

In the real world, decisions are never made in a vacuum. We are always limited by resources such as money, time, or physical space. These limitations are called constraints. Constraints are expressed as a system of linear inequalities involving the variables $x$ and $y$. For example, a dealer might have a maximum budget and a limited storage space, which translates into inequalities like $x + y \leq 60$.

When we graph these inequalities on a coordinate plane, they divide the plane into two halves. The set of points that satisfies all the constraints simultaneously forms a common region. This region is called the feasible region, or solution region. The feasible region is always a convex region. Every point within and on the boundary of this region represents a feasible solution to the problem, meaning it is a valid combination of $x$ and $y$ that satisfies all the given constraints. Any point outside this region is called an infeasible solution.

## The Corner Point Method

Because the feasible region contains infinitely many points, finding the exact point that gives the maximum or minimum value of the objective function $Z = ax + by$ can seem daunting. However, we can use a highly efficient method called the Corner Point Method. This method relies on two fundamental theorems.

The first theorem states that when the objective function $Z = ax + by$ has an optimal value, this optimal value must occur at a corner point, or vertex, of the feasible region. The second theorem adds that if the feasible region is bounded, meaning it can be enclosed within a circle, then the objective function $Z$ has both a maximum and a minimum value, and each of these occurs at a corner point of the region.

The corner point method comprises a straightforward procedure. First, you must find the feasible region of the linear programming problem and determine its corner points either by inspection or by solving the two equations of the lines intersecting at that point. Next, you evaluate the objective function $Z = ax + by$ at each corner point. Let $M$ and $m$ denote the largest and smallest values of $Z$ found among these points. If the feasible region is bounded, $M$ and $m$ are the maximum and minimum values of $Z$, respectively.

If the feasible region is unbounded, the situation is slightly different. To verify if $M$ is the maximum value of $Z$, you must check if the open half-plane determined by $ax + by > M$ has any points in common with the feasible region. If it does not, then $M$ is the maximum value of $Z$. If it does have common points, then $Z$ has no maximum value. The same logic applies to finding the minimum value $m$ using the inequality $ax + by < m$.

## Worked Example

Let us apply the corner point method to a problem where we want to maximize the objective function $Z = 4x + y$. The constraints are given by the following system of linear inequalities: $x + y \leq 50$, $3x + y \leq 90$, $x \geq 0$, and $y \geq 0$.

First, we graph the system of inequalities to find the feasible region. The shaded region formed by these constraints is a bounded region with corner points at $O(0, 0)$, $A(30, 0)$, $B(20, 30)$, and $C(0, 50)$.

Next, we evaluate the objective function $Z = 4x + y$ at each of these corner points:
- At $O(0, 0)$, $Z = 4(0) + 0 = 0$.
- At $A(30, 0)$, $Z = 4(30) + 0 = 120$.
- At $B(20, 30)$, $Z = 4(20) + 30 = 110$.
- At $C(0, 50)$, $Z = 4(0) + 50 = 50$.

Since the feasible region is bounded, the largest value of $Z$ is the maximum value. Here, the largest value is $120$, which occurs at the corner point $A(30, 0)$. Therefore, the maximum value of $Z$ is $120$.

## Key points

- The objective function $Z = ax + by$ is the linear equation representing the quantity to be maximized or minimized.
- Constraints are the linear inequalities that limit the values of the variables $x$ and $y$.
- The feasible region is the common region determined by all the constraints, including non-negative constraints $x, y \geq 0$.
- The corner point method states that for a bounded feasible region, the optimal value of the objective function occurs at a vertex of the region.
- For an unbounded feasible region, an optimal value may not exist, but if it does, it must occur at a corner point.
- If two corner points produce the same maximum or minimum value, every point on the line segment joining them also gives the same optimal value.