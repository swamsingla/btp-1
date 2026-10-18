---
{
  "concept": "Pair of Linear Equations in Two Variables",
  "slug": "pair-of-linear-equations",
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
    "completion_tokens": 3031,
    "prompt_tokens": 6182,
    "total_tokens": 9213,
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
  "generated_at": "2026-10-17T22:04:44",
  "source_grade": 10,
  "grade_delta": 0,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g10_maths_chapter3_009",
      "chapter": "chapter3",
      "section": "3.3 Algebraic Methods of Solving a Pair of Linear Equations"
    },
    {
      "ref": "S2",
      "passage_id": "g10_maths_chapter3_006",
      "chapter": "chapter3",
      "section": "3.2 Graphical Method of Solution of a Pair of Linear Equations"
    }
  ],
  "citation_check": {
    "cited": [],
    "invented_citations": [],
    "unused_sources": [
      "1",
      "2"
    ],
    "explanatory_paragraphs_without_a_citation": 12,
    "words": 1817,
    "target_words": [
      1000,
      1350
    ],
    "untraceable_sections": 5,
    "ok": false,
    "structural_problems": [
      "arithmetic: '-4 = 0' -- -4 is -4, the page writes 0"
    ]
  },
  "terms": [
    "pair of linear equations",
    "substitution method",
    "consistent pair",
    "inconsistent pair",
    "dependent pair",
    "cartesian coordinate system",
    "non-integral coordinates",
    "algebraic methods"
  ]
}
---

# Pair of Linear Equations in Two Variables

You have already learned how to graph a single linear equation in two variables on the Cartesian Coordinate System to draw a straight line. A pair of linear equations in two variables means you are working with two such equations simultaneously. The solution to the pair is the point where the two lines intersect. This is a fundamental concept in Grade 10 maths because it allows us to solve real-world problems involving two unknown quantities, such as finding the cost of two different items or determining two people's ages based on past and future conditions.

## The Graphical Method and Its Limitations

You can solve a pair of linear equations graphically, by drawing both lines and reading off the point where they meet. The graphical method is not convenient in cases when the point representing the solution of the linear equations has non-integral coordinates like $\left(\sqrt{3}, 2\sqrt{7}\right)$, $(-1.75, 3.3)$, $\left(\frac{4}{13}, \frac{1}{19}\right)$, etc. There is every possibility of making mistakes while reading such coordinates. Is there any alternative method of finding the solution? There are several algebraic methods, which we shall now discuss.

## The Substitution Method

We shall explain the method of substitution by taking some examples.

**Worked example**
Solve the following pair of equations by substitution method:

$$
7 x - 1 5 y = 2\tag{1}
$$

$$
x + 2 y = 3\tag{2}
$$

Solution :

Step 1 : We pick either of the equations and write one variable in terms of the other. Let us consider Equation (2) and write it as

$$
\begin{array}{r l} x + 2 y & = 3 \\ x & = 3 - 2 y \end{array}\tag{3}
$$

Step 2 : Substitute the value of $x$ in Equation (1). We get

$$
\begin{array}{r l} 7 (3 - 2 y) - 1 5 y & = 2 \\ 2 1 - 1 4 y - 1 5 y & = 2 \\ - 2 9 y & = - 1 9 \end{array}
$$

Therefore,

$$
y = \frac {1 9}{2 9}
$$

Step 3 : Substituting this value of $y$ in Equation (3), we get

$$
x = 3 - 2 \left(\frac {1 9}{2 9}\right) = \frac {4 9}{2 9}
$$

Therefore, the solution is $x = \frac{49}{29}$, $y = \frac{19}{29}$.

Verification : Substituting $x = \frac{49}{29}$ and $y = \frac{19}{29}$, you can verify that both the Equations (1) and (2) are satisfied.

## Types of Solutions and Consistency

To understand the substitution method more clearly, let us consider it stepwise: Step 1: Find the value of one variable, say $y$ in terms of the other variable, i.e., $x$ from either equation, whichever is convenient. Step 2 : Substitute this value of y in the other equation, and reduce it to an equation in one variable, i.e., in terms of x, which can be solved. Sometimes, as in the last two worked examples below, you can get statements with no variable. If this statement is true, you can conclude that the pair of linear equations has infinitely many solutions. If the statement is false, then the pair of linear equations is inconsistent. Step 3 : Substitute the value of x (or y) obtained in Step 2 in the equation used in Step 1 to obtain the value of the other variable. Remark : We have substituted the value of one variable by expressing it in terms of the other variable to solve the pair of linear equations. That is why the method is known as the substitution method.

**Worked example**
Solve the following question—Aftab tells his daughter, “Seven years ago, I was seven times as old as you were then. Also, three years from now, I shall be three times as old as you will be.” (Isn’t this interesting?) Represent this situation algebraically and find their ages by the method of substitution.

Solution : Let s and t be the ages (in years) of Aftab and his daughter, respectively. Then, the pair of linear equations that represent the situation is

$$
s - 7 = 7 (t - 7), \text{i.e.,} s - 7 t + 4 2 = 0\tag{1}
$$

and

$$
s + 3 = 3 (t + 3), \text{i.e.,} s - 3 t = 6\tag{2}
$$

Using Equation (2), we get $s = 3t + 6$.

Putting this value of $s$ in Equation (1), we get

$$
(3 t + 6) - 7 t + 4 2 = 0,
$$

i.e.,

$$
4 t = 4 8, \text{   which   gives   } t = 1 2.
$$

Putting this value of $t$ in Equation (2), we get

$$
s = 3 (1 2) + 6 = 4 2
$$

So, Aftab and his daughter are 42 and 12 years old, respectively.

Verify this answer by checking if it satisfies the conditions of the given problems.

## Inconsistent and Dependent Pairs

**Worked example**
In a shop the cost of 2 pencils and 3 erasers is ₹9 and the cost of 4 pencils and 6 erasers is ₹18. Find the cost of each pencil and each eraser.

Solution : The pair of linear equations formed were:

$$
2 x + 3 y = 9\tag{1}
$$

$$
4 x + 6 y = 1 8\tag{2}
$$

We first express the value of $x$ in terms of $y$ from the equation $2x + 3y = 9$, to get

$$
x = \frac {9 - 3 y}{2}\tag{3}
$$

Now we substitute this value of $x$ in Equation (2), to get

$$ \begin{array}{c} \frac {4 (9 - 3 y)}{2} + 6 y = 1 8 \\ 1 8 - 6 y + 6 y = 1 8 \\ 1 8 = 1 8 \end{array} $$

This statement is true for all values of y. However, we do not get a specific value of y as a solution. Therefore, we cannot obtain a specific value of x. This situation has arisen because both the given equations are the same. Therefore, Equations (1) and (2) have infinitely many solutions. We cannot find a unique cost of a pencil and an eraser, because there are many common solutions, to the given situation.

**Worked example**
Two rails are represented by the equations $x + 2y - 4 = 0$ and $2x + 4y - 12 = 0$. Will the rails cross each other?

Solution : The pair of linear equations formed is:
$$ x + 2 y - 4 = 0 \quad (1) $$
$$ 2 x + 4 y - 1 2 = 0 \quad (2) $$
We express $x$ in terms of $y$ from Equation (1) to get
$$ x = 4 - 2 y $$
Now, we substitute this value of $x$ in Equation (2) to get
$$ 2 (4 - 2 y) + 4 y - 1 2 = 0 $$
The terms in $y$ cancel, and we are left with $8 - 12 = 0$, that is, $-4 = 0$, which is a false statement.

Therefore, the equations do not have a common solution. So, the two rails will not cross each other.

## Summary of Line Behaviour

A pair of linear equations which has no solution, is called an inconsistent pair of linear equations. A pair of linear equations in two variables, which has a solution, is called a consistent pair of linear equations. A pair of linear equations which are equivalent has infinitely many distinct common solutions. Such a pair is called a dependent pair of linear equations in two variables. Note that a dependent pair of linear equations is always consistent.

We can now summarise the behaviour of lines representing a pair of linear equations in two variables and the existence of solutions as follows:

(i) the lines may intersect in a single point. In this case, the pair of equations has a unique solution (consistent pair of equations).

(ii) the lines may be parallel. In this case, the equations have no solution (inconsistent pair of equations).

(iii) the lines may be coincident. In this case, the equations have infinitely many solutions [dependent (consistent) pair of equations].

Consider the following three pairs of equations.

(i) $x - 2y = 0$ and $3x + 4y - 20 = 0$ (The lines intersect)

(ii) $2x + 3y - 9 = 0$ and $4x + 6y - 18 = 0$ (The lines coincide)

(iii) $x + 2y - 4 = 0$ and $2x + 4y - 12 = 0$ (The lines are parallel)

Let us now write down, and compare, the values of $\frac{a_1}{a_2}, \frac{b_1}{b_2}$ and $\frac{c_1}{c_2}$ in all the three examples. Here, a general pair of equations is written as $a_1 x + b_1 y + c_1 = 0$ and $a_2 x + b_2 y + c_2 = 0$, where $a_1, b_1, c_1$ and $a_2, b_2, c_2$ are the coefficients.

| Pair of lines | $\frac{a_1}{a_2}$ | $\frac{b_1}{b_2}$ | $\frac{c_1}{c_2}$ | Compare the ratios | Graphical representation | Algebraic interpretation |
| --- | --- | --- | --- | --- | --- | --- |
| $x - 2y = 0$ and $3x + 4y - 20 = 0$ | $\frac{1}{3}$ | $\frac{-2}{4}$ | $\frac{0}{-20}$ | $\frac{a_1}{a_2} \neq \frac{b_1}{b_2}$ | Intersecting lines | Exactly one solution (unique) |
| $2x + 3y - 9 = 0$ and $4x + 6y - 18 = 0$ | $\frac{2}{4}$ | $\frac{3}{6}$ | $\frac{-9}{-18}$ | $\frac{a_1}{a_2} = \frac{b_1}{b_2} = \frac{c_1}{c_2}$ | Coincident lines | Infinitely many solutions |
| $x + 2y - 4 = 0$ and $2x + 4y - 12 = 0$ | $\frac{1}{2}$ | $\frac{2}{4}$ | $\frac{-4}{-12}$ | $\frac{a_1}{a_2} = \frac{b_1}{b_2} \neq \frac{c_1}{c_2}$ | Parallel lines | No solution |

From the table above, you can observe that if the lines represented by the equation $$ a _ {1} x + b _ {1} y + c _ {1} = 0 $$ and $$ a _ {2} x + b _ {2} y + c _ {2} = 0 $$ are (i) intersecting, then $\frac{a_1}{a_2} \neq \frac{b_1}{b_2}$. (ii) coincident, then $\frac{a_{1}}{a_{2}}=\frac{b_{1}}{b_{2}}=\frac{c_{1}}{c_{2}}$ . (iii) parallel, then $\frac{a_{1}}{a_{2}}=\frac{b_{1}}{b_{2}}\neq\frac{c_{1}}{c_{2}}$ In fact, the converse is also true for any pair of lines. You can verify them by considering some more examples by yourself.

## Key points

- A pair of linear equations in two variables is solved algebraically using the substitution method, where you express one variable in terms of the other.
- If substituting the value of one variable results in a true statement with no variables, the pair has infinitely many solutions and is a dependent pair.
- If substituting results in a false statement with no variables, the pair has no solution and is an inconsistent pair.
- A consistent pair has at least one solution: exactly one if the lines intersect, and infinitely many if they coincide. An inconsistent pair has none.
- The ratios $\frac{a_1}{a_2}$, $\frac{b_1}{b_2}$, and $\frac{c_1}{c_2}$ determine the nature of the lines: intersecting if the first two ratios are unequal, coincident if all three are equal, and parallel if the first two are equal but the third is different.