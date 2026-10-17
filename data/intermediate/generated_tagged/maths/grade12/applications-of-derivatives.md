# Applications of Derivatives — Word Problems

Derivatives are not just abstract symbols on a page; they are powerful tools used in physics to calculate velocity, in economics to determine marginal profit, and in engineering to optimize designs. When you study the rate at which a quantity changes, you are directly applying the derivative. This page bridges the gap between pure calculus and the real world, showing you how to translate everyday scenarios into mathematical equations.

## Optimisation in Economics and Business

In business, managers constantly seek to maximise profit or minimise cost. This process of finding the best possible outcome is called optimisation. An optimisation problem involves finding the maximum profit, minimum cost, or the minimum use of resources. A special but very important class of optimisation problems is the linear programming problem [S3]. 

Consider a furniture dealer who deals in only two items—tables and chairs. He has Rs 50,000 to invest and has storage space of at most 60 pieces. A table costs Rs 2500 and a chair Rs 500. He estimates that from the sale of one table, he can make a profit of Rs 250 and that from the sale of one chair a profit of Rs 75. He wants to know how many tables and chairs he should buy from the available money so as to maximise his total profit, assuming that he can sell all the items which he buys [S3].

To solve this, we use the concepts of feasible and infeasible solutions. The common region determined by all the constraints including non-negative constraints $x, y \geq 0$ of a linear programming problem is called the feasible region (or solution region) for the problem. Every point in this region is called a feasible solution to the problem. Any point outside the feasible region is called an infeasible solution [S1].

## The Corner Point Method

When you have a feasible region, how do you find the exact combination that gives the maximum profit? You use the Corner Point Method. 

Theorem 1 states that when $Z = ax + by$ has an optimal value, where the variables $x$ and $y$ are subject to constraints described by linear inequalities, this optimal value must occur at a corner point (vertex) of the feasible region. Theorem 2 adds that if the feasible region is bounded, the objective function $Z$ has both a maximum and a minimum value on the region, and each of these occurs at a corner point of the region [S1].

The method comprises of the following steps:
1. Find the feasible region of the linear programming problem and determine its corner points (vertices) either by inspection or by solving the two equations of the lines intersecting at that point.
2. Evaluate the objective function $Z = ax + by$ at each corner point. Let $M$ and $m$, respectively denote the largest and smallest values of these points.
3. (i) When the feasible region is bounded, $M$ and $m$ are the maximum and minimum values of $Z$. (ii) In case, the feasible region is unbounded, we have:
   4. (a) $M$ is the maximum value of $Z$, if the open half plane determined by $ax + by > \mathrm{M}$ has no point in common with the feasible region. Otherwise, $Z$ has no maximum value. (b) Similarly, $m$ is the minimum value of $Z$, if the open half plane determined by $ax + by < m$ has no point in common with the feasible region. Otherwise, $Z$ has no minimum value [S1].

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

Hence, the maximum value of $Z$ is 120 at the point $(30, 0)$ [S1].

## Handling Unbounded Regions

Sometimes, the feasible region is unbounded, meaning it extends indefinitely in any direction. In this case, a maximum or a minimum value of the objective function may not exist. However, if it exists, it must occur at a corner point of the region [S1].

To decide if an unbounded region has a maximum or minimum, you must graph the inequality. For example, if you find a candidate minimum value of $Z$, you graph the inequality $ax + by < m$ and check whether the resulting open half plane has points in common with the feasible region. If it has common points, then your candidate value is not the minimum. If it does not, your candidate value is the true minimum [S1].

## Key points

- An optimisation problem may involve finding maximum profit, minimum cost, or minimum use of resources [S3].
- The common region determined by all the constraints including non-negative constraints $x, y \geq 0$ is called the feasible region [S1].
- Theorem 1: When $Z = ax + by$ has an optimal value, this optimal value must occur at a corner point (vertex) of the feasible region [S1].
- Theorem 2: If the feasible region is bounded, the objective function $Z$ has both a maximum and a minimum value on the region, and each of these occurs at a corner point of the region [S1].
- For unbounded regions, check the open half-plane to confirm if a maximum or minimum value actually exists.

<!-- TERMS: optimisation, linear programming, feasible region, infeasible solution, objective function, corner point, bounded, unbounded, feasible solutions, optimal solution -->