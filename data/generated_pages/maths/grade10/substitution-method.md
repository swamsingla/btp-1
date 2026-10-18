---
{
  "concept": "Substitution Method",
  "slug": "substitution-method",
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
    "completion_tokens": 1518,
    "prompt_tokens": 4326,
    "total_tokens": 5844,
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
  "generated_at": "2026-10-17T22:05:02",
  "source_grade": 10,
  "grade_delta": 0,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g10_maths_chapter3_009",
      "chapter": "chapter3",
      "section": "3.3 Algebraic Methods of Solving a Pair of Linear Equations"
    }
  ],
  "citation_check": {
    "cited": [
      "1"
    ],
    "invented_citations": [],
    "unused_sources": [],
    "explanatory_paragraphs_without_a_citation": 0,
    "words": 1042,
    "target_words": [
      1000,
      1350
    ],
    "untraceable_sections": 0,
    "ok": true,
    "structural_problems": []
  },
  "terms": [
    "substitution method",
    "linear equations",
    "variable",
    "infinitely many solutions",
    "inconsistent",
    "verify"
  ]
}
---

# Substitution Method

In Grade 10, you have learned how to solve a pair of linear equations graphically. The graphical method is not convenient in cases when the point representing the solution of the linear equations has non-integral coordinates like $\left(\sqrt{3}, 2\sqrt{7}\right)$, $(-1.75, 3.3)$, $\left(\frac{4}{13}, \frac{1}{19}\right)$, etc. There is every possibility of making mistakes while reading such coordinates. Is there any alternative method of finding the solution? There are several algebraic methods, which we shall now discuss.

## The Core Idea

The substitution method is an algebraic technique for finding the exact values of the variables in a pair of linear equations. Instead of estimating where two lines cross on a graph, we use the equations themselves to build a chain of logic. The method works by expressing one variable in terms of the other from one of the equations, and then substituting that expression into the second equation. This process reduces the pair of equations to a single equation with a single unknown. Once we solve for that one variable, we substitute the value back into the expression from the first step to find the remaining variable. This is why the method is known as the substitution method, as we have substituted the value of one variable by expressing it in terms of the other variable to solve the pair of linear equations.

## Step-by-Step Process

To understand the substitution method more clearly, let us consider it stepwise. Step 1: Find the value of one variable, say $y$ in terms of the other variable, i.e., $x$ from either equation, whichever is convenient. Step 2: Substitute this value of $y$ in the other equation, and reduce it to an equation in one variable, i.e., in terms of $x$, which can be solved. Sometimes, as in some examples, you can get statements with no variable. If this statement is true, you can conclude that the pair of linear equations has infinitely many solutions. If the statement is false, then the pair of linear equations is inconsistent. Step 3: Substitute the value of $x$ (or $y$) obtained in Step 2 in the equation used in Step 1 to obtain the value of the other variable.

## Worked Example

Consider the following pair of equations:
$$
x + 2y = 3
$$
$$
3x - y = 7
$$
To begin the substitution method, we pick either of the equations and write one variable in terms of the other. Let us consider the first equation:
$$
x + 2y = 3
$$
and write it as:
$$
x = 3 - 2y
$$
Next, we substitute this value of $x$ in the second equation. We get:
$$
3(3 - 2y) - y = 7
$$
Expanding the brackets gives:
$$
9 - 6y - y = 7
$$
Combining like terms results in:
$$
9 - 7y = 7
$$
Subtracting 9 from both sides yields:
$$
-7y = -2
$$
Dividing by -7 gives:
$$
y = \frac{2}{7}
$$
Finally, we substitute this value of $y$ in the expression $x = 3 - 2y$ from the first step. We get:
$$
x = 3 - 2\left(\frac{2}{7}\right) = 3 - \frac{4}{7} = \frac{21}{7} - \frac{4}{7} = \frac{17}{7}
$$
Therefore, the solution is $x = \frac{17}{7}$ and $y = \frac{2}{7}$.

## Special Cases

When we substitute the value of one variable in the other equation, we sometimes get statements with no variable. If this statement is true, you can conclude that the pair of linear equations has infinitely many solutions. If the statement is false, then the pair of linear equations is inconsistent.

For instance, if we have the equations $x + 2y = 4$ and $2x + 4y = 8$, we might substitute $x = 4 - 2y$ to get $2(4 - 2y) + 4y = 8$, which simplifies to $8 = 8$. This is a true statement, meaning the equations are essentially the same line and have infinitely many solutions. On the other hand, if we have $x + 2y = 4$ and $2x + 4y = 12$, we might substitute $x = 4 - 2y$ to get $2(4 - 2y) + 4y = 12$, which simplifies to $8 = 12$. This is a false statement, meaning the lines are parallel and never cross, so the system is inconsistent.

## Real-World Application

The substitution method is highly useful for solving everyday word problems. Consider a situation where the cost of 2 pencils and 3 erasers is ₹9, and the cost of 4 pencils and 6 erasers is ₹18. Let the cost of a pencil be $x$ and the cost of an eraser be $y$. The pair of linear equations formed are:
$$
2x + 3y = 9
$$
$$
4x + 6y = 18
$$
We first express the value of $x$ in terms of $y$ from the first equation:
$$
x = \frac{9 - 3y}{2}
$$
Now we substitute this value of $x$ in the second equation:
$$
4\left(\frac{9 - 3y}{2}\right) + 6y = 18
$$
Simplifying this gives:
$$
2(9 - 3y) + 6y = 18
$$
$$
18 - 6y + 6y = 18
$$
$$
18 = 18
$$
This statement is true for all values of $y$. However, we do not get a specific value of $y$ as a solution. Therefore, we cannot obtain a specific value of $x$. This situation has arisen because both the given equations are the same. Therefore, the equations have infinitely many solutions. We cannot find a unique cost of a pencil and an eraser, because there are many common solutions to the given situation.

## Key points
* The substitution method is an algebraic method used to solve a pair of linear equations by expressing one variable in terms of the other.
* The process involves three main steps: express one variable in terms of the other, substitute this value into the second equation, and then solve for the remaining variable.
* After finding the value of the first variable, substitute it back into the initial expression to find the value of the second variable.
* A true statement with no variable indicates infinitely many solutions, while a false statement indicates an inconsistent system.
* Always verify the final solution by substituting both values back into the original equations to ensure they are satisfied.