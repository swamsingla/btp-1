---
{
  "concept": "Quadratic Equations",
  "slug": "quadratic-equations",
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
    "completion_tokens": 2736,
    "prompt_tokens": 6611,
    "total_tokens": 9347,
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
  "generated_at": "2026-10-17T22:05:27",
  "source_grade": 10,
  "grade_delta": 0,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g10_maths_chapter4_003",
      "chapter": "chapter4",
      "section": "4.2 Quadratic Equations"
    },
    {
      "ref": "S2",
      "passage_id": "g10_maths_chapter4_008",
      "chapter": "chapter4",
      "section": "4.3 Solution of a Quadratic Equation by Factorisation"
    },
    {
      "ref": "S3",
      "passage_id": "g10_maths_chapter4_002",
      "chapter": "chapter4",
      "section": "4.1 Introduction"
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
    "explanatory_paragraphs_without_a_citation": 1,
    "words": 1707,
    "target_words": [
      1000,
      1350
    ],
    "untraceable_sections": 0,
    "ok": true,
    "structural_problems": []
  },
  "terms": [
    "quadratic equation",
    "standard form",
    "root",
    "zero",
    "factorisation",
    "polynomial",
    "variable"
  ]
}
---

# Quadratic Equations

Quadratic equations are a fundamental concept in algebra that allow us to model and solve a wide variety of real-world problems. You will encounter them when calculating the area of a rectangular garden, determining the trajectory of a thrown ball, or figuring out the dimensions of a building. In Grade 10, understanding how to identify these equations and solve them is a crucial step in your mathematical journey, laying the groundwork for more advanced topics you will study in higher grades.

## Standard Form

A quadratic equation in the variable $x$ is an equation of the form $ax^2 + bx + c = 0$, where $a, b, c$ are real numbers, $a \neq 0$. For example, $2x^2 + x - 300 = 0$ is a quadratic equation. Similarly, $2x^2 - 3x + 1 = 0$, $4x - 3x^2 + 2 = 0$ and $1 - x^2 + 300 = 0$ are also quadratic equations.

In fact, any equation of the form $p(x)=0$, where $p(x)$ is a polynomial of degree 2, is a quadratic equation. But when we write the terms of $p(x)$ in descending order of their degrees, then we get the standard form of the equation. That is, $ax^{2}+bx+c=0$, $a\neq0$ is called the standard form of a quadratic equation.

## Solving by Factorisation

To solve a quadratic equation by factorisation, we use the knowledge of how to factorise quadratic polynomials by splitting their middle terms, which you learned in Grade 9. We then equate each factor to zero to find the roots.

A real number $\alpha$ is called a root of the quadratic equation $ax^{2} + bx + c = 0$, $a \neq 0$ if $a \alpha^{2} + b\alpha + c = 0$. We also say that $x = \alpha$ is a solution of the quadratic equation, or that $\alpha$ satisfies the quadratic equation. Note that the zeroes of the quadratic polynomial $ax^{2} + bx + c$ and the roots of the quadratic equation $ax^{2} + bx + c = 0$ are the same.

A quadratic polynomial can have at most two zeroes. So, any quadratic equation can have at most two roots.

Let us see how to solve by factorisation. Consider the quadratic equation $2x^{2} - 3x + 1 = 0$. If we replace $x$ by 1 on the LHS of this equation, we get $(2 \times 1^{2}) - (3 \times 1) + 1 = 0 = \text{RHS}$ of the equation. We say that 1 is a root of the quadratic equation $2x^{2} - 3x + 1 = 0$.

### Worked Example

Find the roots of the equation $6x^{2} - x - 2 = 0$, by factorisation.

Solution : We have
$$ \begin{array}{r l} 6 x ^ {2} - x - 2 & = 6 x ^ {2} + 3 x - 4 x - 2 \\ & = 3 x (2 x + 1) - 2 (2 x + 1) \\ & = (3 x - 2) (2 x + 1) \end{array} $$
The roots of $6x^{2} - x - 2 = 0$ are the values of $x$ for which $(3x - 2)(2x + 1) = 0$. Therefore, $3x - 2 = 0$ or $2x + 1 = 0$, i.e.,
$$ x = \frac {2}{3} \quad \text{or} \quad x = - \frac {1}{2} $$
Therefore, the roots of $6x^{2} - x - 2 = 0$ are $\frac{2}{3}$ and $-\frac{1}{2}$.

## Checking if an Equation is Quadratic

Before solving, we must first check whether a given equation is a quadratic equation. We do this by simplifying the equation and checking if it can be written in the standard form $ax^2 + bx + c = 0$.

Let us consider a few examples to see how this works.

Example 1: Check whether the following are quadratic equations:

(i) $(x - 2)^{2} + 1 = 2x - 3$

(ii) $x(x + 1) + 8 = (x + 2)(x - 2)$

(iii) $x(2x + 3) = x^{2} + 1$

(iv) $(x + 2)^{3} = x^{3} - 4$

**Solution:**

(i) $\mathrm{LHS} = (x - 2)^2 + 1 = x^2 - 4x + 4 + 1 = x^2 - 4x + 5$
Therefore, $(x - 2)^{2} + 1 = 2x - 3$ can be rewritten as
$$ x ^ {2} - 4 x + 5 = 2 x - 3 $$
i.e.,
$$ x ^ {2} - 6 x + 8 = 0 $$
It is of the form $ax^2 + bx + c = 0$. Therefore, the given equation is a quadratic equation.

(ii) Since $x(x + 1) + 8 = x^2 + x + 8$ and $(x + 2)(x - 2) = x^2 - 4$
$$ x ^ {2} + x + 8 = x ^ {2} - 4 $$
i.e.,
$$ x + 1 2 = 0 $$
It is not of the form $ax^2 + bx + c = 0$. Therefore, the given equation is not a quadratic equation.

(iii) Here,
$$ \mathrm{LHS} = x (2 x + 3) = 2 x ^ {2} + 3 x $$
So, $x(2x + 3) = x^{2} + 1$ can be rewritten as
$$ 2 x ^ {2} + 3 x = x ^ {2} + 1 $$
Therefore, we get $x^{2} + 3x - 1 = 0$
It is of the form $ax^2 + bx + c = 0$. So, the given equation is a quadratic equation.

(iv) Here,
$$ \mathrm{LHS} = (x + 2) ^ {3} = x ^ {3} + 6 x ^ {2} + 1 2 x + 8 $$
Therefore, $(x + 2)^{3} = x^{3} - 4$ can be rewritten as
$$ x ^ {3} + 6 x ^ {2} + 1 2 x + 8 = x ^ {3} - 4 $$
i.e.,
$$ 6 x ^ {2} + 1 2 x + 1 2 = 0 \quad \text{or,} \quad x ^ {2} + 2 x + 2 = 0 $$
It is of the form $ax^2 + bx + c = 0$. So, the given equation is a quadratic equation.

Remark: Be careful! In (ii) above, the given equation appears to be a quadratic equation, but it is not a quadratic equation. In (iv) above, the given equation appears to be a cubic equation (an equation of degree 3) and not a quadratic equation. But it turns out to be a quadratic equation. As you can see, often we need to simplify the given equation before deciding whether it is quadratic or not.

## Real-Life Applications

Quadratic equations arise in several situations in the world around us and in different fields of mathematics. Let us consider a few examples.

Example 2: Represent the following situations mathematically:
(i) John and Jivanti together have 45 marbles. Both of them lost 5 marbles each, and the product of the number of marbles they now have is 124. We would like to find out how many marbles they had to start with.
(ii) A cottage industry produces a certain number of toys in a day. The cost of production of each toy (in rupees) was found to be 55 minus the number of toys produced in a day. On a particular day, the total cost of production was ₹ 750. We would like to find out the number of toys produced on that day.

**Solution:**

(i) Let the number of marbles John had be $x$.
Then the number of marbles Jivanti had $= 45 - x$, because together they have 45.
The number of marbles left with John, when he lost 5 marbles = x - 5. The number of marbles left with Jivanti, when she lost 5 marbles $= 45 - x - 5$
$$ = 4 0 - x $$
Therefore, their product $= (x - 5)(40 - x)$
$$ = 40x - x^2 - 200 + 5x $$
$$ = -x^2 + 45x - 200 $$
So, $-x^{2} + 45x - 200 = 124$ (Given that product = 124)
i.e., $-x^{2} + 45x - 324 = 0$
i.e., $x^{2} - 45x + 324 = 0$
Therefore, the number of marbles John had, satisfies the quadratic equation
$$ x ^ {2} - 4 5 x + 3 2 4 = 0 $$
which is the required representation of the problem mathematically.

(ii) Let the number of toys produced on that day be $x$.
Therefore, the cost of production (in rupees) of each toy that day = 55 - x.
So, the total cost of production (in rupees) that day = x (55 - x)
$$ x (5 5 - x) = 7 5 0 $$
i.e.,
$$ 5 5 x - x ^ {2} = 7 5 0 $$
i.e.,
$$ - x ^ {2} + 5 5 x - 7 5 0 = 0 $$
i.e.,
$$ x ^ {2} - 5 5 x + 7 5 0 = 0 $$
Therefore, the number of toys produced that day satisfies the quadratic equation
$$ x ^ {2} - 5 5 x + 7 5 0 = 0 $$
which is the required representation of the problem mathematically.

## Key points
* A quadratic equation in the variable $x$ is an equation of the form $ax^2 + bx + c = 0$, where $a, b, c$ are real numbers, $a \neq 0$.
* The standard form of a quadratic equation is $ax^{2}+bx+c=0$, $a\neq0$.
* A real number $\alpha$ is called a root of the quadratic equation $ax^{2} + bx + c = 0$, $a \neq 0$ if $a \alpha^{2} + b\alpha + c = 0$.
* Any quadratic equation can have at most two roots.
* To solve by factorisation, split the middle term and equate each factor to zero.
* Often, we need to simplify the given equation before deciding whether it is quadratic or not.
* Quadratic equations arise in several situations in the world around us.