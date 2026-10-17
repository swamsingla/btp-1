# Pythagorean Triples

Pythagorean triples are sets of three positive integers $(a, b, c)$ that satisfy the equation $a^2 + b^2 = c^2$ [S2]. These sets are incredibly useful because they represent the exact side lengths of a right-angled triangle. You already know how to find the length of the longest side of a right triangle using the Pythagorean theorem. Pythagorean triples simply give you a shortcut: instead of calculating square roots, you can instantly identify the side lengths if they happen to be whole numbers. This page explains what these triples are, how to find them, and how they led to a famous problem in mathematics.

## What Are Baudhāyana Triples?

In ancient India, the mathematician Baudhāyana listed, in his Śulba-Sūtra, several integer triples $(a, b, c)$ that form the side lengths of a right-angled triangle. Because they satisfy the equation $a^2 + b^2 = c^2$, these are called Baudhāyana triples [S2]. They are also known as Pythagorean triples or right-angled triangle triples [S2].

Some well-known examples of these triples are $(3, 4, 5)$, $(5, 12, 13)$, $(8, 15, 17)$, $(7, 24, 25)$, $(12, 35, 37)$, and $(15, 36, 39)$ [S2]. You can easily check that they work using the Pythagorean theorem. For example, $3^2 + 4^2 = 9 + 16 = 25$, which is exactly $5^2$ [S2].

## Scaled Versions of Triples

There are infinitely many Pythagorean triples. One way to generate them is by taking an existing triple and multiplying all three numbers by the same positive integer $k$. For example, if we multiply $(3, 4, 5)$ by $3$, we get $(9, 12, 15)$. If we multiply it by $10$, we get $(30, 40, 50)$. 

If $(a, b, c)$ is a Pythagorean triple, then $(ka, kb, kc)$ is also a Pythagorean triple for any positive integer $k$ [S2]. We call this new set a scaled version of the original triple [S2]. To prove this, we check the equation: $(ka)^2 + (kb)^2 = k^2a^2 + k^2b^2 = k^2(a^2 + b^2)$. Since $a^2 + b^2 = c^2$, this becomes $k^2c^2$, which is exactly $(kc)^2$ [S2].

For example, if we take the triple $(5, 12, 13)$ and multiply it by $2$, we get $(10, 24, 26)$. Checking the equation, $10^2 + 24^2 = 100 + 576 = 676$, which is exactly $26^2$ [S2].

## Primitive Triples

Some Pythagorean triples have a common factor greater than 1, while others do not. A Pythagorean triple that does not have any common factor greater than 1 is called a primitive Pythagorean triple [S2]. 

The triple $(3, 4, 5)$ is primitive because the only number that divides 3, 4, and 5 is 1. However, $(9, 12, 15)$ is not primitive, because they are all divisible by 3 [S2]. 

If we have a non-primitive triple like $(9, 12, 15)$ and divide each number by their Highest Common Factor (HCF), which is 3, we get $(3, 4, 5)$. This resulting triple is primitive [S2]. If we can find all the primitive triples, we can find all the other triples by scaling them up [S2].

## Generating Primitive Triples

One way to generate primitive Pythagorean triples uses the relationship between consecutive odd numbers and square numbers. The sum of the first $n$ odd numbers is always $n^2$ [S2]. 

We can express this algebraically. The $n$-th odd number is $2n - 1$. Therefore, the sum of the first $(n - 1)$ odd numbers is $(n - 1)^2$, and adding the $n$-th odd number gives us $n^2$ [S2]. This gives us the equation:
$$ (n - 1)^2 + (2n - 1) = n^2 $$
If the $n$-th odd number, $2n - 1$, is also a perfect square, then we have a sum of two square numbers equal to another square number, which gives us a Pythagorean triple [S2].

Let us look at the number 9. It is the 5th odd number, and it is also a square number ($3 \times 3 = 9$) [S2]. So, we can substitute $n = 5$ into the equation to get:
$$ (5 - 1)^2 + 9 = 5^2 $$
$$ 4^2 + 3^2 = 5^2 $$
This gives us the primitive triple $(3, 4, 5)$ [S2].

Similarly, 25 is an odd square. It is the 13th odd number, so $n = 13$. Substituting this into the equation gives:
$$ (13 - 1)^2 + 25 = 13^2 $$
$$ 12^2 + 5^2 = 13^2 $$
This gives us the primitive triple $(5, 12, 13)$ [S2].

This method does not give every primitive triple. For example, $(8, 15, 17)$ is primitive, but none of its sides is one less than the hypotenuse, so it cannot come from this method.

## Fermat and a Famous Problem

We have seen that infinitely many square numbers can be written as a sum of two square numbers. This made the French mathematician Fermat, who lived in the 17th century, wonder whether a perfect cube can be a sum of two perfect cubes, a fourth power a sum of two fourth powers, and so on. In other words, does $x^n + y^n = z^n$ have a solution in natural numbers when $n > 2$? Fermat wrote in the margin of a book that it does not, and that he had a marvellous proof which the margin was too small to hold. No one ever found his proof, and more than 300 years of attempts followed. The statement, known as Fermat's Last Theorem, was finally proved by Andrew Wiles in 1994.

## Worked Example

Let us apply the scaling rule to a larger number. Suppose we want to find a Pythagorean triple using the primitive triple $(8, 15, 17)$ and a scaling factor of $5$. 

According to the rule, if $(a, b, c)$ is a Pythagorean triple, then $(ka, kb, kc)$ is also a Pythagorean triple [S2]. We multiply each number by $5$:
$$ (8 \times 5, 15 \times 5, 17 \times 5) = (40, 75, 85) $$
To check our answer, we substitute these values back into the equation $a^2 + b^2 = c^2$:
$$ 40^2 + 75^2 = 1600 + 5625 = 7225 $$
$$ 85^2 = 7225 $$
Since both sides are equal, $(40, 75, 85)$ is indeed a Pythagorean triple [S2].

## Key points
- A Pythagorean triple is a set of three positive integers $(a, b, c)$ that satisfy the equation $a^2 + b^2 = c^2$ [S2].
- If $(a, b, c)$ is a Pythagorean triple, then $(ka, kb, kc)$ is also a Pythagorean triple for any positive integer $k$ [S2].
- A Pythagorean triple with no common factor greater than 1 is called a primitive Pythagorean triple [S2].
- Primitive triples can be generated using the algebraic relationship between odd numbers and square numbers: $(n - 1)^2 + (2n - 1) = n^2$ [S2].
- Finding all primitive triples allows you to find all possible Pythagorean triples by scaling them up [S2].

<!-- TERMS: Pythagorean triples, Baudhāyana triples, right-angled triangle, positive integers, scaled version, primitive triple, Highest Common Factor, consecutive odd numbers, square numbers, algebraic relationship, equation, natural numbers, right-triangle, Pythagorean theorem -->