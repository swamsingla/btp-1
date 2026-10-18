---
{
  "concept": "Elimination Method",
  "slug": "elimination-method",
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
    "completion_tokens": 1264,
    "prompt_tokens": 4157,
    "total_tokens": 5421,
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
  "generated_at": "2026-10-17T22:05:10",
  "source_grade": 10,
  "grade_delta": 0,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g10_maths_chapter3_016",
      "chapter": "chapter3",
      "section": "3.3.2 Elimination Method"
    }
  ],
  "citation_check": {
    "cited": [
      "1"
    ],
    "invented_citations": [],
    "unused_sources": [],
    "explanatory_paragraphs_without_a_citation": 7,
    "words": 864,
    "target_words": [
      1000,
      1350
    ],
    "untraceable_sections": 2,
    "ok": false,
    "structural_problems": []
  },
  "terms": [
    "elimination method",
    "simultaneous equations",
    "coefficients",
    "variable",
    "linear equation",
    "infinitely many solutions",
    "no solution",
    "inconsistent"
  ]
}
---

# Elimination Method

You have already learned how to solve simultaneous equations using the substitution method. However, there is another powerful technique called the elimination method. This approach is sometimes more convenient because it allows you to remove one variable directly by combining the equations. The core idea is to make the coefficients of either $x$ or $y$ equal so that adding or subtracting the equations cancels out one of the variables.

## The Basic Idea

When you have two linear equations, you can manipulate them to make the coefficients of one variable identical. Once the coefficients match, you can simply add or subtract the two equations. This subtraction removes that variable entirely, leaving you with a single linear equation in one variable. You can then solve for that remaining variable easily.

Consider the pair of equations:
$$ 2x + 3y = 10 $$
$$ 2x + y = 6 $$
Notice that the coefficient of $x$ is already 2 in both equations. If we subtract the second equation from the first, the $2x$ terms cancel out, leaving $2y = 4$. We can immediately solve for $y$ to get $y = 2$. Substituting $y = 2$ in the second equation gives $2x + 2 = 6$, so $x = 2$. This direct cancellation is the heart of the elimination method.

Often the coefficients are not already equal, so we must multiply first. Example: Solve $3x + 4y = 10$ and $2x - 2y = 2$. Multiply the second equation by 2 to get $4x - 4y = 4$. Now the coefficients of $y$ are $4$ and $-4$, which are opposites, so adding the two equations eliminates $y$:
$$ (3x + 4y) + (4x - 4y) = 10 + 4 $$
$$ 7x = 14, \quad \text{so} \quad x = 2 $$
Substituting $x = 2$ in $2x - 2y = 2$ gives $4 - 2y = 2$, so $y = 1$. Check in the first equation: $3(2) + 4(1) = 10$. ✓

## Step-by-Step Procedure

To apply the elimination method systematically, you need to follow a clear set of steps. First, you must make the coefficients of one variable equal. This is done by multiplying each equation by a suitable non-zero constant. After that, you add or subtract the equations to eliminate the chosen variable.

If the coefficients of $y$ are equal, you subtract one equation from the other to eliminate $y$. If the coefficients of $x$ are equal, you subtract one equation from the other to eliminate $x$. If the coefficients are equal in size but opposite in sign, you add the equations instead. This process leaves you with a simple equation in a single variable.

Once you have an equation with only one variable, you solve it to find the value of that variable. After finding this value, you substitute it back into one of the original equations. This substitution allows you to find the value of the second variable.

## Special Cases

Sometimes, when you eliminate a variable, you do not get a single value. Instead, you might get a statement that is always true or always false. If you get a true statement involving no variable, it means the original pair of equations has infinitely many solutions. This happens when the two equations represent the exact same line.

On the other hand, if you get a false statement involving no variable, it means the original pair of equations has no solution. This indicates that the two lines are parallel and will never intersect.

For example, consider the equations:
$$ 3x + 2y = 7 $$
$$ 6x + 4y = 15 $$
If we multiply the first equation by 2, we get $6x + 4y = 14$. Subtracting this from the second equation gives $0 = 1$, which is a false statement. Therefore, this pair of equations has no solution.

Now consider $2x + 3y = 9$ and $4x + 6y = 18$. If we multiply the first equation by 2, we get $4x + 6y = 18$, which is exactly the second equation. Subtracting gives $0 = 0$, which is a true statement. Therefore, this pair of equations has infinitely many solutions.

## Worked Example

Let us solve a real-world problem using the elimination method. Suppose the ratio of the incomes of two persons is 9 : 7 and the ratio of their expenditures is 4 : 3. If each of them manages to save ₹ 2000 per month, find their monthly incomes.

Let the incomes of the two persons be ₹ 9x and ₹ 7x respectively. Let their expenditures be ₹ 4y and ₹ 3y respectively. The equations formed in the situation are given by:
$$ 9x - 4y = 2000 \tag{1} $$
$$ 7x - 3y = 2000 \tag{2} $$

Step 1: Multiply Equation (1) by 3 and Equation (2) by 4 to make the coefficients of $y$ equal. Then we get the equations:
$$ 27x - 12y = 6000 \tag{3} $$
$$ 28x - 12y = 8000 \tag{4} $$

Step 2: Subtract Equation (3) from Equation (4) to eliminate $y$, because the coefficients of $y$ are the same. So, we get:
$$ (28x - 27x) - (12y - 12y) = 8000 - 6000 $$
i.e.,
$$ x = 2000 $$

Step 3: Substituting this value of $x$ in (1), we get:
$$ 9(2000) - 4y = 2000 $$
i.e.,
$$ y = 4000 $$

So, the solution of the equations is $x = 2000$ and $y = 4000$. Therefore, the monthly incomes of the persons are ₹ 18,000 and ₹ 14,000 respectively. Verification shows that $18000 : 14000 = 9 : 7$, and the ratio of their expenditures is $16000 : 12000 = 4 : 3$.

## Key points
*   Multiply both equations by suitable non-zero constants to make the coefficients of one variable numerically equal.
*   Add or subtract the equations to eliminate one variable and solve the resulting single-variable equation.
*   Substitute the found value back into an original equation to find the value of the second variable.
*   If elimination yields a true statement with no variables, the pair of equations has infinitely many solutions.
*   If elimination yields a false statement with no variables, the pair of equations has no solution.