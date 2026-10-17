<!-- page 1 of 9 -->

The image provided is a QR code. As per the instructions, I am to process text and non-textual information (a non-textual content) and not contain any textual content suitable for OCR processing. Therefore, no textual content can be extracted or converted according to the given instructions.

11076CK08

Chapter

7

# BINOMIAL THEOREM

◆ Mathematics is a most exact science and its conclusions are capable of absolute proofs. – C.P. STEINMETZ◆

## 7.1 Introduction

In earlier classes, we have learnt how to find the squares and cubes of binomials like $a + b$ and $a - b$. Using them, we could evaluate the numerical values of numbers like $(98)^{2} = (100 - 2)^{2}$, $(999)^{3} = (1000 - 1)^{3}$, etc. However, for higher powers like $(98)^{5}$, $(101)^{6}$, etc., the calculations become difficult by using repeated multiplication. This difficulty was overcome by a theorem known as binomial theorem. It gives an easier way to expand $(a + b)^{n}$, where $n$ is an integer or a rational number. In this Chapter, we study binomial theorem for positive integral indices only.

![Image block](doc:80ca051/tier:standard/page:1/block:9)

<details>
<summary>seal</summary>

1
R0
</details>

Blaise Pascal (1623-1662)

## 7.2 Binomial Theorem for Positive Integral Indices

Let us have a look at the following identities done earlier:

$$
(a + b) ^ {0} = 1 \quad \quad \quad \quad a + b \neq 0
$$

$$
(a + b) ^ {1} = a + b
$$

$$
(a + b) ^ {2} = a ^ {2} + 2 a b + b ^ {2}
$$

$$
(a + b) ^ {3} = a ^ {3} + 3 a ^ {2} b + 3 a b ^ {2} + b ^ {3}
$$

$$
(a + b) ^ {4} = (a + b) ^ {3} (a + b) = a ^ {4} + 4 a ^ {3} b + 6 a ^ {2} b ^ {2} + 4 a b ^ {3} + b ^ {4}
$$

In these expansions, we observe that

(i) The total number of terms in the expansion is one more than the index. For example, in the expansion of  $(a + b)^{2}$ , number of terms is 3 whereas the index of  $(a + b)^{2}$  is 2.

(ii) Powers of the first quantity ‘a’ go on decreasing by 1 whereas the powers of the second quantity ‘b’ increase by 1, in the successive terms.

(iii) In each term of the expansion, the sum of the indices of $a$ and $b$ is the same and is equal to the index of $a + b$.

Reprint 2025-26

<!-- page 2 of 9 -->

BINOMIAL THEOREM

127

We now arrange the coefficients in these expansions as follows (Fig 7.1):

![Image block](doc:80ca051/tier:standard/page:2/block:4)

Do we observe any pattern in this table that will help us to write the next row? Yes we do. It can be seen that the addition of 1's in the row for index 1 gives rise to 2 in the row for index 2. The addition of 1, 2 and 2, 1 in the row for index 2, gives rise to 3 and 3 in the row for index 3 and so on. Also, 1 is present at the beginning and at the end of each row. This can be continued till any index of our interest.

We can extend the pattern given in Fig 7.2 by writing a few more rows.

![Image block](doc:80ca051/tier:standard/page:2/block:7)

## Pascal's Triangle

The structure given in Fig 7.2 looks like a triangle with 1 at the top vertex and running down the two slanting sides. This array of numbers is known as Pascal's triangle, after the name of French mathematician Blaise Pascal. It is also known as Meru Prastara by Pingla.

Expansions for the higher powers of a binomial are also possible by using Pascal's triangle. Let us expand  $(2x + 3y)^{5}$  by using Pascal's triangle. The row for index 5 is 1 5 10 10 5 1

Using this row and our observations (i), (ii) and (iii), we get

$$
\begin{array}{l l} (2 x + 3 y) ^ {5} & = (2 x) ^ {5} + 5 (2 x) ^ {4} (3 y) + 1 0 (2 x) ^ {3} (3 y) ^ {2} + 1 0 (2 x) ^ {2} (3 y) ^ {3} + 5 (2 x) (3 y) ^ {4} + (3 y) ^ {5} \\ & = 3 2 x ^ {5} + 2 4 0 x ^ {4} \mathrm{y} + 7 2 0 x ^ {3} \mathrm{y} ^ {2} + 1 0 8 0 x ^ {2} y ^ {3} + 8 1 0 x y ^ {4} + 2 4 3 y ^ {5}. \end{array}
$$

Reprint 2025-26

<!-- page 3 of 9 -->

128

MATHEMATICS

Now, if we want to find the expansion of $(2x + 3y)^{12}$, we are first required to get the row for index 12. This can be done by writing all the rows of the Pascal's triangle till index 12. This is a slightly lengthy process. The process, as you observe, will become more difficult, if we need the expansions involving still larger powers.

We thus try to find a rule that will help us to find the expansion of the binomial for any power without writing all the rows of the Pascal's triangle, that come before the row of the desired index.

For this, we make use of the concept of combinations studied earlier to rewrite

the numbers in the Pascal's triangle. We know that $^n\mathrm{C}_r = \frac{n!}{r!(n - r)!}$, $0 \leq r \leq n$ and

$n$ is a non-negative integer. Also, $^n\mathrm{C}_0 = 1 = ^n\mathrm{C}_n$

The Pascal's triangle can now be rewritten as (Fig 7.3)

![Image block](doc:80ca051/tier:standard/page:3/block:9)

Fig 7.3 Pascal's triangle

Observing this pattern, we can now write the row of the Pascal's triangle for any index without writing the earlier rows. For example, for the index 7 the row would be

$$
\begin{array}{c} ^ 7 \mathrm{C} _ {0} \quad^ 7 \mathrm{C} _ {1} \quad^ 7 \mathrm{C} _ {2} \quad^ 7 \mathrm{C} _ {3} \quad^ 7 \mathrm{C} _ {4} \quad^ 7 \mathrm{C} _ {5} \quad^ 7 \mathrm{C} _ {6} \quad^ 7 \mathrm{C} _ {7}. \end{array}
$$

Thus, using this row and the observations (i), (ii) and (iii), we have

$$
(a + b) ^ {7} = ^ {7} \mathrm{C} _ {0} a ^ {7} + 7 \mathrm{C} _ {1} a ^ {6} b + ^ {7} \mathrm{C} _ {2} a ^ {5} b ^ {2} + ^ {7} \mathrm{C} _ {3} a ^ {4} b ^ {3} + 7 \mathrm{C} _ {4} a ^ {3} b ^ {4} + ^ {7} \mathrm{C} _ {5} a ^ {2} b ^ {5} + ^ {7} \mathrm{C} _ {6} a b ^ {6} + ^ {7} \mathrm{C} _ {7} b ^ {7}
$$

An expansion of a binomial to any positive integral index say $n$ can now be visualised using these observations. We are now in a position to write the expansion of a binomial to any positive integral index.

Reprint 2025-26

<!-- page 4 of 9 -->

BINOMIAL THEOREM

129

## 7.2.1 Binomial theorem for any positive integer $n$,

$$
(a + b) ^ {n} = ^ {n} \mathrm{C} _ {0} a ^ {n} + ^ {n} \mathrm{C} _ {1} a ^ {n - 1} b + ^ {n} \mathrm{C} _ {2} a ^ {n - 2} b ^ {2} + \dots + ^ {n} \mathrm{C} _ {n - 1} a. b ^ {n - 1} + ^ {n} \mathrm{C} _ {n} b ^ {n}
$$

Proof The proof is obtained by applying principle of mathematical induction.

Let the given statement be

$$
\mathrm{P} (n): (a + b) ^ {n} = ^ {n} \mathrm{C} _ {0} a ^ {n} + ^ {n} \mathrm{C} _ {1} a ^ {n - 1} b + ^ {n} \mathrm{C} _ {2} a ^ {n - 2} b ^ {2} + \dots + ^ {n} \mathrm{C} _ {n - 1} a. b ^ {n - 1} + ^ {n} \mathrm{C} _ {n} b ^ {n}
$$

For $n = 1$, we have

$$
\mathrm{P} (1): (a + b) ^ {1} = ^ 1 \mathrm{C} _ {0} a ^ {1} + ^ 1 \mathrm{C} _ {1} b ^ {1} = a + b
$$

Thus, P (1) is true.

Suppose $\mathrm{P}(k)$ is true for some positive integer $k$, i.e.

$$
(a + b) ^ {k} = ^ {k} \mathrm{C} _ {0} a ^ {k} + ^ {k} \mathrm{C} _ {1} a ^ {k - 1} b + ^ {k} \mathrm{C} _ {2} a ^ {k - 2} b ^ {2} + \dots + ^ {k} \mathrm{C} _ {k} b ^ {k}
$$

(1)

We shall prove that $\mathrm{P}(k + 1)$ is also true, i.e.,

$$
(a + b) ^ {k + 1} = ^ {k + 1} \mathrm{C} _ {0} a ^ {k + 1} + ^ {k + 1} \mathrm{C} _ {1} a ^ {k} b + ^ {k + 1} \mathrm{C} _ {2} a ^ {k - 1} b ^ {2} + \dots + ^ {k + 1} \mathrm{C} _ {k + 1} b ^ {k + 1}
$$

$$
\begin{array}{l} \text {ow,} (a + b) ^ {k + 1} = (a + b) (a + b) ^ {k} \\ \quad = (a + b) (^ {k} \mathrm{C} _ {0} a ^ {k} + ^ {k} \mathrm{C} _ {1} a ^ {k - 1} b + ^ {k} \mathrm{C} _ {2} a ^ {k - 2} b ^ {2} +... + ^ {k} \mathrm{C} _ {k - 1} a b ^ {k - 1} + ^ {k} \mathrm{C} _ {k} b ^ {k}) \\ \quad \text {[from (1)]} \\ \quad = ^ {k} \mathrm{C} _ {0} a ^ {k + 1} + ^ {k} \mathrm{C} _ {1} a ^ {k} b + ^ {k} \mathrm{C} _ {2} a ^ {k - 1} b ^ {2} +... + ^ {k} \mathrm{C} _ {k - 1} a ^ {2} b ^ {k - 1} + ^ {k} \mathrm{C} _ {k} a b ^ {k} + ^ {k} \mathrm{C} _ {0} a ^ {k} b \\ \quad \quad + ^ {k} \mathrm{C} _ {1} a ^ {k - 1} b ^ {2} + ^ {k} \mathrm{C} _ {2} a ^ {k - 2} b ^ {3} +... + ^ {k} \mathrm{C} _ {k - 1} a b ^ {k} + ^ {k} \mathrm{C} _ {k} b ^ {k + 1} \\ \quad \text {[by actual multiplication]} \\ \quad = ^ {k} \mathrm{C} _ {0} a ^ {k + 1} + (^ {k} \mathrm{C} _ {1} + ^ {k} \mathrm{C} _ {0}) a ^ {k} b + (^ {k} \mathrm{C} _ {2} + ^ {k} \mathrm{C} _ {1}) a ^ {k - 1} b ^ {2} +... \\ \quad \quad + (^ {k} \mathrm{C} _ {k} + ^ {k} \mathrm{C} _ {k - 1}) a b ^ {k} + ^ {k} \mathrm{C} _ {k} b ^ {k + 1} \\ \quad \text {[grouping like terms]} \\ \quad = ^ {k + 1} \mathrm{C} _ {0} a ^ {k + 1} + ^ {k + 1} \mathrm{C} _ {1} a ^ {k} b + ^ {k + 1} \mathrm{C} _ {2} a ^ {k - 1} \mathrm{b} ^ {2} +... + ^ {k + 1} \mathrm{C} _ {k} a b ^ {k} + ^ {k + 1} \mathrm{C} _ {k + 1} b ^ {k + 1} \end{array}
$$

$$
(\text {by using} ^ {k + 1} \mathrm{C} _ {0} = 1, ^ {k} \mathrm{C} _ {r} + ^ {k} \mathrm{C} _ {r - 1} = ^ {k + 1} \mathrm{C} _ {r} \quad \text {and} ^ {k} \mathrm{C} _ {k} = 1 = ^ {k + 1} \mathrm{C} _ {k + 1})
$$

Thus, it has been proved that $\mathrm{P}(k + 1)$ is true whenever $\mathrm{P}(k)$ is true. Therefore, by principle of mathematical induction, $\mathrm{P}(n)$ is true for every positive integer $n$.

We illustrate this theorem by expanding $(x + 2)^6$:

$$
\begin{array}{r l} (x + 2) ^ {6} & = ^ {6} \mathrm{C} _ {0} x ^ {6} + ^ {6} \mathrm{C} _ {1} x ^ {5}. 2 + ^ {6} \mathrm{C} _ {2} x ^ {4} 2 ^ {2} + ^ {6} \mathrm{C} _ {3} x ^ {3}. 2 ^ {3} + ^ {6} \mathrm{C} _ {4} x ^ {2}. 2 ^ {4} + ^ {6} \mathrm{C} _ {5} x. 2 ^ {5} + ^ {6} \mathrm{C} _ {6}. 2 ^ {6}. \\ & = x ^ {6} + 1 2 x ^ {5} + 6 0 x ^ {4} + 1 6 0 x ^ {3} + 2 4 0 x ^ {2} + 1 9 2 x + 6 4 \end{array}
$$

$$
\text {Thus} (x + 2) ^ {6} = x ^ {6} + 1 2 x ^ {5} + 6 0 x ^ {4} + 1 6 0 x ^ {3} + 2 4 0 x ^ {2} + 1 9 2 x + 6 4.
$$

Reprint 2025-26

<!-- page 5 of 9 -->

130

MATHEMATICS

## Observations

1. The notation $\sum_{k=0}^{n}{}^n\mathrm{C}_k a^{n-k}b^k$ stands for

$^{n}\mathrm{C}_{0}a^{n}b^{0} + ^{n}\mathrm{C}_{1}a^{n - 1}b^{1} + \dots + ^{n}\mathrm{C}_{r}a^{n - r}b^{r} + \dots + ^{n}\mathrm{C}_{n}a^{n - n}b^{n},$ where $b^0 = 1 = a^{n - n}$.

Hence the theorem can also be stated as

$$
\left(a + b\right) ^ {n} = \sum_ {k = 0} ^ {n} ^ {n} \mathrm{C} _ {k} a ^ {n - k} b ^ {k}.
$$

2. The coefficients  $^{n}C_{r}$  occurring in the binomial theorem are known as binomial coefficients.

3. There are $(n + 1)$ terms in the expansion of $(a + b)^n$, i.e., one more than the index.

4. In the successive terms of the expansion the index of $a$ goes on decreasing by unity. It is $n$ in the first term, $(n - 1)$ in the second term, and so on ending with zero in the last term. At the same time the index of $b$ increases by unity, starting with zero in the first term, 1 in the second and so on ending with $n$ in the last term.

5. In the expansion of $(a + b)^n$, the sum of the indices of $a$ and $b$ is $n + 0 = n$ in the first term, $(n - 1) + 1 = n$ in the second term and so on $0 + n = n$ in the last term. Thus, it can be seen that the sum of the indices of $a$ and $b$ is $n$ in every term of the expansion.

7.2.2 Some special cases In the expansion of $(a + b)^n$,

(i) Taking $a = x$ and $b = -y$, we obtain

$$
\begin{array}{l l} (x - y) ^ {n} & = [ x + (- y) ] ^ {n} \\ & = ^ {n} \mathrm{C} _ {0} x ^ {n} + ^ {n} \mathrm{C} _ {1} x ^ {n - 1} (- y) + ^ {n} \mathrm{C} _ {2} x ^ {n - 2} (- y) ^ {2} + ^ {n} \mathrm{C} _ {3} x ^ {n - 3} (- y) ^ {3} + \dots + ^ {n} \mathrm{C} _ {n} (- y) ^ {n} \\ & = ^ {n} \mathrm{C} _ {0} x ^ {n} - ^ {n} \mathrm{C} _ {1} x ^ {n - 1} y + ^ {n} \mathrm{C} _ {2} x ^ {n - 2} y ^ {2} - ^ {n} \mathrm{C} _ {3} x ^ {n - 3} y ^ {3} + \dots + (- 1) ^ {n} ^ {n} \mathrm{C} _ {n} y ^ {n} \end{array}
$$

Thus $(x - y)^{n} = {}^{n}\mathrm{C}_{0}x^{n} - {}^{n}\mathrm{C}_{1}x^{n - 1}y + {}^{n}\mathrm{C}_{2}x^{n - 2}y^{2} + \ldots +(-1)^{n}{}^{n}\mathrm{C}_{n}y^{n}$

Using this, we have

$$
\begin{array}{r l} (x - 2 y) ^ {5} = & ^ 5 \mathrm{C} _ {0} x ^ {5} - ^ {5} \mathrm{C} _ {1} x ^ {4} (2 y) + ^ {5} \mathrm{C} _ {2} x ^ {3} (2 y) ^ {2} - ^ {5} \mathrm{C} _ {3} x ^ {2} (2 y) ^ {3} + \\ & ^ 5 \mathrm{C} _ {4} x (2 y) ^ {4} - ^ {5} \mathrm{C} _ {5} (2 y) ^ {5} \\ = & x ^ {5} - 1 0 x ^ {4} \mathrm{y} + 4 0 x ^ {3} y ^ {2} - 8 0 x ^ {2} y ^ {3} + 8 0 x y ^ {4} - 3 2 y ^ {5}. \end{array}
$$

(ii) Taking $a = 1$, $b = x$, we obtain

Thus

$$
\begin{array}{c} (1 + x) ^ {n} = ^ {n} \mathrm{C} _ {0} (1) ^ {n} + ^ {n} \mathrm{C} _ {1} (1) ^ {n - 1} x + ^ {n} \mathrm{C} _ {2} (1) ^ {n - 2} x ^ {2} + \ldots + ^ {n} \mathrm{C} _ {n} x ^ {n} \\ = ^ {n} \mathrm{C} _ {0} + ^ {n} \mathrm{C} _ {1} x + ^ {n} \mathrm{C} _ {2} x ^ {2} + ^ {n} \mathrm{C} _ {3} x ^ {3} + \ldots + ^ {n} \mathrm{C} _ {n} x ^ {n} \\ (1 + x) ^ {n} = ^ {n} \mathrm{C} _ {0} + ^ {n} \mathrm{C} _ {1} x + ^ {n} \mathrm{C} _ {2} x ^ {2} + ^ {n} \mathrm{C} _ {3} x ^ {3} + \ldots + ^ {n} \mathrm{C} _ {n} x ^ {n} \end{array}
$$

Reprint 2025-26

<!-- page 6 of 9 -->

BINOMIAL THEOREM

131

In particular, for $x = 1$, we have

$$
2 ^ {n} = ^ {n} \mathrm{C} _ {0} + ^ {n} \mathrm{C} _ {1} + ^ {n} \mathrm{C} _ {2} + \dots + ^ {n} \mathrm{C} _ {n}.
$$

(iii) Taking $a = 1$, $b = -x$, we obtain

$$
(1 - x) ^ {n} = ^ {n} C _ {0} - ^ {n} C _ {1} x + ^ {n} C _ {2} x ^ {2} - \dots + (- 1) ^ {n} ^ {n} C _ {n} x ^ {n}
$$

In particular, for $x = 1$, we get

$$
0 = ^ {n} \mathrm{C} _ {0} - ^ {n} \mathrm{C} _ {1} + ^ {n} \mathrm{C} _ {2} - \dots + (- 1) ^ {n} ^ {n} \mathrm{C} _ {n}
$$

Example 1 Expand $\left(x^{2} + \frac{3}{x}\right)^{4}, x \neq 0$

Solution By using binomial theorem, we have

$$
\begin{array}{r l} x ^ {2} + \frac {3}{x} ^ {4} & = ^ {4} C _ {0} (x ^ {2}) ^ {4} + ^ {4} C _ {1} (x ^ {2}) ^ {3} \left(\frac {3}{x}\right) + ^ {4} C _ {2} (x ^ {2}) ^ {2} \left(\frac {3}{x}\right) ^ {2} + ^ {4} C _ {3} (x ^ {2}) \left(\frac {3}{x}\right) ^ {3} + ^ {4} C _ {4} \left(\frac {3}{x}\right) ^ {4} \\ & = x ^ {8} + 4. x ^ {6}. \frac {3}{x} + 6. x ^ {4}. \frac {9}{x ^ {2}} + 4. x ^ {2}. \frac {2 7}{x ^ {3}} + \frac {8 1}{x ^ {4}} \\ & = x ^ {8} + 1 2 x ^ {5} + 5 4 x ^ {2} + \frac {1 0 8}{x} + \frac {8 1}{x ^ {4}}. \end{array}
$$

Example 2 Compute (98) $^{5}$ .

Solution We express 98 as the sum or difference of two numbers whose powers are easier to calculate, and then use Binomial Theorem.

Write $98 = 100 - 2$

$$
\begin{array}{r l} \text {Therefore,} (9 8) ^ {5} & = (1 0 0 - 2) ^ {5} \\ & = ^ {5} \mathrm{C} _ {0} (1 0 0) ^ {5} - ^ {5} \mathrm{C} _ {1} (1 0 0) ^ {4}. 2 + ^ {5} \mathrm{C} _ {2} (1 0 0) ^ {3} 2 ^ {2} \\ & - ^ {5} \mathrm{C} _ {3} (1 0 0) ^ {2} (2) ^ {3} + ^ {5} \mathrm{C} _ {4} (1 0 0) (2) ^ {4} - ^ {5} \mathrm{C} _ {5} (2) ^ {5} \\ & = 1 0 0 0 0 0 0 0 0 0 0 - 5 \times 1 0 0 0 0 0 0 0 0 \times 2 + 1 0 \times 1 0 0 0 0 0 0 \times 4 - 1 0 \times 1 0 0 0 0 \\ & \times 8 + 5 \times 1 0 0 \times 1 6 - 3 2 \\ & = 1 0 0 4 0 0 0 8 0 0 0 - 1 0 0 0 8 0 0 0 3 2 = 9 0 3 9 2 0 7 9 6 8. \end{array}
$$

Example 3 Which is larger $(1.01)^{1000000}$ or 10,000?

Solution Splitting 1.01 and using binomial theorem to write the first few terms we have

Reprint 2025-26

<!-- page 7 of 9 -->

132

MATHEMATICS

$$
\begin{array}{r l} (1. 0 1) ^ {1 0 0 0 0 0 0} & = (1 + 0. 0 1) ^ {1 0 0 0 0 0 0} \\ & = ^ {1 0 0 0 0 0 0} \mathrm{C} _ {0} + ^ {1 0 0 0 0 0 0} \mathrm{C} _ {1} (0. 0 1) + \text {other positive terms} \\ & = 1 + 1 0 0 0 0 0 0 \times 0. 0 1 + \text {other positive terms} \\ & = 1 + 1 0 0 0 0 + \text {other positive terms} \\ & > 1 0 0 0 0 \end{array}
$$

Hence

$$
(1. 0 1) ^ {1 0 0 0 0 0 0} > 1 0 0 0 0
$$

Example 4 Using binomial theorem, prove that $6^{n} - 5n$ always leaves remainder 1 when divided by 25.

Solution For two numbers $a$ and $b$ if we can find numbers $q$ and $r$ such that $a = bq + r$, then we say that $b$ divides $a$ with $q$ as quotient and $r$ as remainder. Thus, in order to show that $6^n - 5n$ leaves remainder 1 when divided by 25, we prove that $6^n - 5n = 25k + 1$, where $k$ is some natural number.

We have

$$
(1 + a) ^ {n} = ^ {n} \mathrm{C} _ {0} + ^ {n} \mathrm{C} _ {1} a + ^ {n} \mathrm{C} _ {2} a ^ {2} + \dots + ^ {n} \mathrm{C} _ {n} a ^ {n}
$$

For $a = 5$ , we get

$$
(1 + 5) ^ {n} = ^ {n} \mathrm{C} _ {0} + ^ {n} \mathrm{C} _ {1} 5 + ^ {n} \mathrm{C} _ {2} 5 ^ {2} + \dots + ^ {n} \mathrm{C} _ {n} 5 ^ {n}
$$

i.e.

$$
(6) ^ {n} = 1 + 5 n + 5 ^ {2}. ^ {n} \mathrm{C} _ {2} + 5 ^ {3}. ^ {n} \mathrm{C} _ {3} + \dots + 5 ^ {n}
$$

i.e.

$$
6 ^ {n} - 5 n = 1 + 5 ^ {2} \left(^ {n} C _ {2} + ^ {n} C _ {3} 5 + \dots + 5 ^ {n - 2}\right)
$$

or

$$
6 ^ {n} - 5 n = 1 + 2 5 \left(^ {n} \mathrm{C} _ {2} + 5. ^ {n} \mathrm{C} _ {3} + \dots + 5 ^ {n - 2}\right)
$$

or

$$
6 ^ {n} - 5 n = 2 5 k + 1 \quad \text {where} k = ^ {n} \mathrm{C} _ {2} + 5. ^ {n} \mathrm{C} _ {3} + \dots + 5 ^ {n - 2}.
$$

This shows that when divided by 25, $6^{n} - 5n$ leaves remainder 1.

## EXERCISE 7.1

Expand each of the expressions in Exercises 1 to 5.

1. $(1 - 2x)^{5}$

2.

$$
\left(\frac {2}{x} - \frac {x}{2}\right) ^ {5}
$$

$$
3. (2 x - 3) ^ {6}
$$

Reprint 2025-26

<!-- page 8 of 9 -->

BINOMIAL THEOREM

133

4. $\left(\frac{x}{3} +\frac{1}{x}\right)^{5}$ 5. $\left(x + \frac{1}{x}\right)^6$

Using binomial theorem, evaluate each of the following:

6. $(96)^{3}$ 7. $(102)^{5}$ 8. $(101)^{4}$

9. $(99)^{5}$

10. Using Binomial Theorem, indicate which number is larger (1.1)$^{10000}$ or 1000.

11. Find $(a + b)^4 - (a - b)^4$. Hence, evaluate $(\sqrt{3} + \sqrt{2})^4 - (\sqrt{3} - \sqrt{2})^4$.

12. Find $(x + 1)^6 + (x - 1)^6$. Hence or otherwise evaluate $(\sqrt{2} + 1)^6 + (\sqrt{2} - 1)^6$.

13. Show that $9^{n+1} - 8n - 9$ is divisible by 64, whenever $n$ is a positive integer.

14. Prove that $\sum_{r=0}^{n} 3^{r^n} C_r = 4^n$.

## Miscellaneous Exercise on Chapter

1. If $a$ and $b$ are distinct integers, prove that $a - b$ is a factor of $a^n - b^n$, whenever $n$ is a positive integer. [Hint write $a^n = (a - b + b)^n$ and expand]

2. Evaluate $\left(\sqrt{3} +\sqrt{2}\right)^6 -\left(\sqrt{3} -\sqrt{2}\right)^6$

3. Find the value of $\left(a^2 +\sqrt{a^2 - 1}\right)^4 +\left(a^2 -\sqrt{a^2 - 1}\right)^4.$

4. Find an approximation of $(0.99)^{5}$ using the first three terms of its expansion.

5. Expand using Binomial Theorem $\left(1 + \frac{x}{2} -\frac{2}{x}\right)^4, x\neq 0$.

6. Find the expansion of $(3x^{2} - 2ax + 3a^{2})^{3}$ using binomial theorem.

## Summary

The expansion of a binomial for any positive integral $n$ is given by Binomial Theorem, which is $(a + b)^n = {}^n\mathrm{C}_0a^n + {}^n\mathrm{C}_1a^{n - 1}b + {}^n\mathrm{C}_2a^{n - 2}b^2 + \dots + {}^n\mathrm{C}_{n - 1}a.b^{n - 1} + {}^n\mathrm{C}_n b^n$.

\- The coefficients of the expansions are arranged in an array. This array is called Pascal's triangle.

Reprint 2025-26

<!-- page 9 of 9 -->

134

MATHEMATICS

## Historical Note

The ancient Indian mathematicians knew about the coefficients in the expansions of $(x + y)^n$, $0 \leq n \leq 7$. The arrangement of these coefficients was in the form of a diagram called Meru-Prastara, provided by Pingla in his book Chhanda shastra (200B.C.). This triangular arrangement is also found in the work of Chinese mathematician Chu-shi-kie in 1303. The term binomial coefficients was first introduced by the German mathematician, Michael Stipel (1486-1567) in approximately 1544. Bombelli (1572) also gave the coefficients in the expansion of $(a + b)^n$, for $n = 1,2\ldots,7$ and Oughtred (1631) gave them for $n = 1,2,\dots,10$. The arithmetic triangle, popularly known as Pascal's triangle and similar to the Meru-Prastara of Pingla was constructed by the French mathematician Blaise Pascal (1623-1662) in 1665.

The present form of the binomial theorem for integral values of $n$ appeared in Trate du triange arithmetic, written by Pascal and published posthumously in 1665.

Reprint 2025-26