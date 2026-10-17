---
{
  "concept": "Applications of Derivatives — Word Problems",
  "slug": "applications-of-derivatives",
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
    "completion_tokens": 1380,
    "prompt_tokens": 6383,
    "total_tokens": 7763,
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
  "generated_at": "2026-10-08T06:24:26",
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
      "passage_id": "g12_maths_part1_chapter6_001",
      "chapter": "chapter6",
      "section": "6.1 Introduction"
    },
    {
      "ref": "S3",
      "passage_id": "g12_maths_part2_chapter6_001",
      "chapter": "chapter6",
      "section": "12.1 Introduction"
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
    "words": 1016,
    "target_words": [
      1050,
      1450
    ],
    "untraceable_sections": 0,
    "ok": true,
    "structural_problems": [],
    "grounding": {
      "cited_sentences": 5,
      "checked": 4,
      "not_judgeable_mostly_maths": 1,
      "cites_a_source_never_given": 0,
      "unsupported": [],
      "unsupported_fraction": 0.0,
      "threshold": 0.5,
      "max_unsupported_fraction": 0.34
    },
    "verification": {
      "verdict": "spiralled",
      "checks": 1,
      "tokens": 9587
    }
  },
  "terms": [
    "optimisation",
    "linear programming",
    "feasible region",
    "infeasible solution",
    "objective function",
    "corner point",
    "bounded",
    "unbounded",
    "feasible solutions",
    "optimal solution"
  ]
}
---

# Applications of Derivatives — Word Problems

Derivatives are not just abstract symbols on a page; they are powerful tools used in physics to calculate velocity, in economics to determine marginal profit, and in engineering to optimize designs. When you study the rate at which a quantity changes, you are directly applying the derivative. This page bridges the gap between pure calculus and the real world, showing you how to translate everyday scenarios into mathematical equations.

## Optimisation in Economics and Business

In business, managers constantly seek to maximise profit or minimise cost. This process of finding the best possible outcome is called optimisation. An optimisation problem involves finding the maximum profit, minimum cost, or the minimum use of resources. A special but very important class of optimisation problems is the linear programming problem. 

Consider a furniture dealer who deals in only two items—tables and chairs. He has Rs 50,000 to invest and has storage space of at most 60 pieces. A table costs Rs 2500 and a chair Rs 500. He estimates that from the sale of one table, he can make a profit of Rs 250 and that from the sale of one chair a profit of Rs 75. He wants to know how many tables and chairs he should buy from the available money so as to maximise his total profit, assuming that he can sell all the items which he buys.

To solve this, we use the concepts of feasible and infeasible solutions. The common region determined by all the constraints including non-negative constraints $x, y \geq 0$ of a linear programming problem is called the feasible region (or solution region) for the problem. Every point in this region is called a feasible solution to the problem. Any point outside the feasible region is called an infeasible solution.

## The Corner Point Method

When you have a feasible region, how do you find the exact combination that gives the maximum profit? You use the Corner Point Method. 

Theorem 1 states that when $Z = ax + by$ has an optimal value, where the variables $x$ and $y$ are subject to constraints described by linear inequalities, this optimal value must occur at a corner point (vertex) of the feasible region. Theorem 2 adds that if the feasible region is bounded, the objective function $Z$ has both a maximum and a minimum value on the region, and each of these occurs at a corner point of the region.

The method comprises of the following steps:
1. Find the feasible region of the linear programming problem and determine its corner points (vertices) either by inspection or by solving the two equations of the lines intersecting at that point.
2. Evaluate the objective function $Z = ax + by$ at each corner point. Let $M$ and $m$, respectively denote the largest and smallest values of these points.
3. (i) When the feasible region is bounded, $M$ and $m$ are the maximum and minimum values of $Z$. (ii) In case, the feasible region is unbounded, we have:
   4. (a) $M$ is the maximum value of $Z$, if the open half plane determined by $ax + by > \mathrm{M}$ has no point in common with the feasible region. Otherwise, $Z$ has no maximum value. (b) Similarly, $m$ is the minimum value of $Z$, if the open half plane determined by $ax + by < m$ has no point in common with the feasible region. Otherwise, $Z$ has no minimum value.

## Worked example

Let us apply this to a simplified scenario. Suppose a dealer wants to maximise the objective function $Z = 4x + y$ subject to the constraints:
$$ x + y \leq 50 $$
$$ 3x + y \leq 90 $$
$$ x \geq 0, y \geq 0 $$

First, we graph the constraints to find the feasible region. The shaded region in the graph is the feasible region determined by the system of constraints. We observe that the feasible region is bounded. The coordinates of the corner points O, A, B and C are $(0, 0)$, $(30, 0)$, $(20, 30)$ and $(0, 50)$ respectively.

Now we evaluate $Z$ at each corner point:
| Corner Point | Corresponding value of $Z$ |
|---|---|
| (0, 0) | 0 |
| (30, 0) | 120 |
| (20, 30) | 110 |
| (0, 50) | 50 |

Hence, the maximum value of $Z$ is 120 at the point $(30, 0)$.

## Handling Unbounded Regions

Sometimes, the feasible region is unbounded, meaning it extends indefinitely in any direction. In this case, a maximum or a minimum value of the objective function may not exist. However, if it exists, it must occur at a corner point of the region.

To decide if an unbounded region has a maximum or minimum, you must graph the inequality. For example, if you find a candidate minimum value of $Z$, you graph the inequality $ax + by < m$ and check whether the resulting open half plane has points in common with the feasible region. If it has common points, then your candidate value is not the minimum. If it does not, your candidate value is the true minimum.

## Key points

- An optimisation problem may involve finding maximum profit, minimum cost, or minimum use of resources.
- The common region determined by all the constraints including non-negative constraints $x, y \geq 0$ is called the feasible region.
- Theorem 1: When $Z = ax + by$ has an optimal value, this optimal value must occur at a corner point (vertex) of the feasible region.
- Theorem 2: If the feasible region is bounded, the objective function $Z$ has both a maximum and a minimum value on the region, and each of these occurs at a corner point of the region.
- For unbounded regions, check the open half-plane to confirm if a maximum or minimum value actually exists.