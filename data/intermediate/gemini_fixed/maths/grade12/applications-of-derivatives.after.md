# Applications of Derivatives — Word Problems

Derivatives are powerful tools used in engineering, science, social science, and many other fields [S2]. For instance, we can use derivatives to determine the rate of change of quantities, to find the equations of tangent and normal to a curve at a point, and to find turning points on the graph of a function to locate where the largest or smallest value (locally) of a function occurs [S2]. We can also use derivatives to find intervals on which a function is increasing or decreasing, or to find approximate values of certain quantities [S2].

While many optimization problems can be solved using derivatives to find turning points [S2], a special and very important class of optimization problems is the linear programming problem, which we solve using graphical methods [S3].

## Optimisation in Economics and Business

Problems which seek to maximise (or, minimise) profit (or, cost) form a general class of problems called optimisation problems [S3]. Thus, an optimisation problem may involve finding maximum profit, minimum cost, or minimum use of resources etc [S3]. A special but a very important class of optimisation problems is the linear programming problem [S3]. 

Consider a furniture dealer who deals in only two items—tables and chairs. He has Rs 50,000 to invest and has storage space of at most 60 pieces. A table costs Rs 2500 and a chair Rs 500. He estimates that from the sale of one table, he can make a profit of Rs 250 and that from the sale of one chair a profit of Rs 75. He wants to know how many tables and chairs he should buy from the available money so as to maximise his total profit, assuming that he can sell all the items which he buys [S3].

To solve this, we use the concepts of feasible and infeasible solutions. The common region determined by all the constraints including non-negative constraints $x, y \geq 0$ of a linear programming problem is called the feasible region (or solution region) for the problem [S1]. Every point of this region is called a feasible solution to the problem, and points within and on the boundary of the feasible region represent feasible solutions of the constraints [S1]. Any point outside the feasible region is called an infeasible solution [S1]. Any point in the feasible region that gives the optimal value (maximum or minimum) of the objective function is called an optimal solution [S1].

## The Corner Point Method

When you have a feasible region, how do you find the exact combination that gives the maximum profit? You use the Corner Point Method. 

A fundamental theorem states that when the objective function $Z = ax + by$ has an optimal value (maximum or minimum), where the variables $x$ and $y$ are subject to constraints described by linear inequalities, this optimal value must occur at a corner point (vertex) of the feasible region [S1]. A corner point of a feasible region is a point in the region which is the intersection of two boundary lines [S1]. Another theorem states that if the feasible region is bounded, then the objective function $Z$ has both a maximum and a minimum value on the feasible region and each of these occurs at a corner point (vertex) of the region [S1].

The method comprises of the following steps:
1. Find the feasible region of the linear programming problem and determine its corner points (vertices) either by inspection or by solving the two equations of the lines intersecting at that point.
2. Evaluate the objective function $Z = ax + by$ at each corner point. Let $M$ and $m$, respectively denote the largest and smallest values of these points.
3. (i) When the feasible region is bounded, $M$ and $m$ are the maximum and minimum values of $Z$.
   (ii) In case, the feasible region is unbounded, we have:
   (a) $M$ is the maximum value of $Z$, if the open half plane determined by $ax + by > M$ has no point in common with the feasible region. Otherwise, $Z$ has no maximum value.
   (b) Similarly, $m$ is the minimum value of $Z$, if the open half plane determined by $ax + by < m$ has no point in common with the feasible region. Otherwise, $Z$ has no minimum value [S1].

## Worked example

Let us apply this to a simplified scenario. Suppose a dealer wants to maximise the objective function $Z = 4x + y$ subject to the constraints:
$$ x + y \leq 50 $$
$$ 3x + y \leq 90 $$
$$ x \geq 0, y \geq 0 $$

First, we graph the constraints to find the feasible region. The shaded region in the graph is the feasible region determined by the system of constraints. We observe that the feasible region is bounded. The coordinates of the corner points are $(0, 0)$, $(30, 0)$, $(20, 30)$ and $(0, 50)$ respectively.

Now we evaluate $Z$ at each corner point:
| Corner Point | Corresponding value of $Z$ |
|---|---|
| (0, 0) | 0 |
| (30, 0) | 120 |
| (20, 30) | 110 |
| (0, 50) | 50 |

Hence, the maximum value of $Z$ is 120 at the point $(30, 0)$ [S1].

## Handling Unbounded Regions

A feasible region of a system of linear inequalities is said to be bounded if it can be enclosed within a circle [S1]. Otherwise, it is called unbounded, meaning that the feasible region does extend indefinitely in any direction [S1]. In this case, a maximum or a minimum value of the objective function may not exist. However, if it exists, it must occur at a corner point of the region [S1].

To decide if an unbounded region has a maximum or minimum, you must graph the inequality. For example, if you find a candidate minimum value $m$ of $Z$, you graph the inequality $ax + by < m$ and check whether the resulting open half plane has points in common with the feasible region. If it has common points, then $Z$ has no minimum value. If it does not, then $m$ is the minimum value of $Z$ [S1].

## Key points

- An optimisation problem may involve finding maximum profit, minimum cost, or minimum use of resources [S3].
- The common region determined by all the constraints including non-negative constraints $x, y \geq 0$ is called the feasible region [S1].
- When the objective function $Z = ax + by$ has an optimal value, this optimal value must occur at a corner point (vertex) of the feasible region [S1].
- If the feasible region is bounded, the objective function $Z$ has both a maximum and a minimum value on the region, and each of these occurs at a corner point of the region [S1].
- For unbounded regions, check the open half-plane to confirm if a maximum or minimum value actually exists [S1].

<!-- TERMS: optimisation, linear programming, feasible region, infeasible solution, objective function, corner point, bounded, unbounded, feasible solutions, optimal solution -->
