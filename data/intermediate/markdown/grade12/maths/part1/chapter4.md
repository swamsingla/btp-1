<!-- page 1 of 28 -->

The image provided is a QR code. It does not contain any text, mathematical formulas, tables, or figures that can be processed according to the given instructions. Therefore, no OCR output can be generated.

12079CH04

Chapter

4

# DETERMINANTS

All Mathematical truths are relative and conditional. — C.P. STEINMETZ

## 4.1 Introduction

In the previous chapter, we have studied about matrices and algebra of matrices. We have also learnt that a system of algebraic equations can be expressed in the form of matrices. This means, a system of linear equations like

$$
\begin{array}{l} a _ {1} x + b _ {1} y = c _ {1} \\ a _ {2} x + b _ {2} y = c _ {2} \end{array}
$$

can be represented as $\begin{bmatrix} a_1 & b_1 \\ a_2 & b_2 \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} c_1 \\ c_2 \end{bmatrix}$. Now, this system of equations has a unique solution or not, is determined by the number $a_1 b_2 - a_2 b_1$. (Recall that if $\frac{a_1}{a_2} \neq \frac{b_1}{b_2}$ or, $a_1 b_2 - a_2 b_1 \neq 0$, then the system of linear equations has a unique solution). The number $a_1 b_2 - a_2 b_1$

![Image block](doc:2c9e871/tier:standard/page:1/block:11)

P.S. Laplace (1749-1827)

which determines uniqueness of solution is associated with the matrix $\mathbf{A} = \begin{bmatrix} a_1 & b_1 \\ a_2 & b_2 \end{bmatrix}$

and is called the determinant of A or det A. Determinants have wide applications in Engineering, Science, Economics, Social Science, etc.

In this chapter, we shall study determinants up to order three only with real entries. Also, we will study various properties of determinants, minors, cofactors and applications of determinants in finding the area of a triangle, adjoint and inverse of a square matrix, consistency and inconsistency of system of linear equations and solution of linear equations in two or three variables using inverse of a matrix.

## 4.2 Determinant

To every square matrix  $A = [a_{ij}]$  of order n, we can associate a number (real or complex) called determinant of the square matrix A, where  $a_{ij} = (i,j)^{\text{th}}$  element of A.

Reprint 2025-26

<!-- page 2 of 28 -->

DETERMINANTS

77

This may be thought of as a function which associates each square matrix with a unique number (real or complex). If M is the set of square matrices, K is the set of numbers (real or complex) and  $f\colon M \to K$  is defined by  $f(A) = k$ , where  $A \in M$  and  $k \in K$ , then  $f(A)$  is called the determinant of A. It is also denoted by  $|A|$  or det A or  $\Delta$ .

If $\mathrm{A} = \begin{bmatrix} a & b \\ c & d \end{bmatrix}$, then determinant of $\mathrm{A}$ is written as $|\mathrm{A}| = \begin{vmatrix} a & b \\ c & d \end{vmatrix} = \det (\mathrm{A})$

## Remarks

(i) For matrix $\mathrm{A}$, $|\mathrm{A}|$ is read as determinant of $\mathrm{A}$ and not modulus of $\mathrm{A}$.

(ii) Only square matrices have determinants.

## 4.2.1 Determinant of a matrix of order one

Let $\mathrm{A} = [a]$ be the matrix of order 1, then determinant of $\mathrm{A}$ is defined to be equal to $a$.

## 4.2.2 Determinant of a matrix of order two

Let

$\mathrm{A} = \begin{bmatrix} a_{11} & a_{12}\\ a_{21} & a_{22} \end{bmatrix}$ be a matrix of order $2\times 2,$

then the determinant of $\mathrm{A}$ is defined as:

$$
\det (\mathrm{A}) = | \mathrm{A} | = \Delta = \left| \begin{array}{c c} a _ {1 1} & a _ {1 2} \\ a _ {2 1} & a _ {2 2} \end{array} \right| = a _ {1 1} a _ {2 2} - a _ {2 1} a _ {1 2}
$$

Example 1 Evaluate $\begin{vmatrix} 2 & 4 \\ -1 & 2 \end{vmatrix}$.

Solution We have  $\begin{vmatrix}2 & 4 \\ -1 & 2\end{vmatrix} = 2(2) - 4(-1) = 4 + 4 = 8.$

Example 2 Evaluate $\begin{vmatrix} x & x + 1 \\ x - 1 & x \end{vmatrix}$

Solution We have

$$
\left| \begin{array}{c c} x & x + 1 \\ x - 1 & x \end{array} \right| = x (x) - (x + 1) (x - 1) = x ^ {2} - (x ^ {2} - 1) = x ^ {2} - x ^ {2} + 1 = 1
$$

## 4.2.3 Determinant of a matrix of order $3 \times 3$

Determinant of a matrix of order three can be determined by expressing it in terms of second order determinants. This is known as expansion of a determinant along a row (or a column). There are six ways of expanding a determinant of order

Reprint 2025-26

<!-- page 3 of 28 -->

78

MATHEMATICS

3 corresponding to each of three rows ( $R_{1}$ ,  $R_{2}$  and  $R_{3}$ ) and three columns ( $C_{1}$ ,  $C_{2}$  and  $C_{3}$ ) giving the same value as shown below.

Consider the determinant of square matrix $\mathrm{A} = [a_{ij}]_{3\times 3}$

i.e.,

$$
\mid \mathrm{A} \mid = \left| \begin{array}{c c c} \boldsymbol {a} _ {1 1} & \boldsymbol {a} _ {1 2} & \boldsymbol {a} _ {1 3} \\ a _ {2 1} & a _ {2 2} & a _ {2 3} \\ a _ {3 1} & a _ {3 2} & a _ {3 3} \end{array} \right|
$$

## Expansion along first Row $(\mathbb{R}_1)$

Step 1 Multiply first element $a_{11}$ of $\mathrm{R}_1$ by $(-1)^{(1 + 1)}[(-1)^{\mathrm{sum of suffixes in} a_{11}}]$ and with the second order determinant obtained by deleting the elements of first row $(\mathrm{R}_1)$ and first column $(\mathrm{C}_1)$ of $|\mathrm{A}|$ as $a_{11}$ lies in $\mathrm{R}_1$ and $\mathrm{C}_1$,

i.e.,

$$
\left| (- 1) ^ {1 + 1} a _ {1 1} \left| \begin{array}{c c} a _ {2 2} & a _ {2 3} \\ a _ {3 2} & a _ {3 3} \end{array} \right| \right|
$$

Step 2 Multiply 2nd element $a_{12}$ of $\mathrm{R}_1$ by $(-1)^{1 + 2}[(-1)^{\mathrm{sum of suffixes in} a_{12}}]$ and the second order determinant obtained by deleting elements of first row $(\mathrm{R}_1)$ and 2nd column $(\mathrm{C}_2)$ of $|\mathrm{A}|$ as $a_{12}$ lies in $\mathrm{R}_1$ and $\mathrm{C}_2$,

i.e.,

$$
\left| (- 1) ^ {1 + 2} a _ {1 2} \left| \begin{array}{c c} a _ {2 1} & a _ {2 3} \\ a _ {3 1} & a _ {3 3} \end{array} \right| \right|
$$

Step 3 Multiply third element $a_{13}$ of $\mathrm{R}_1$ by $(-1)^{1 + 3}[(-1)^{\mathrm{sum of suffixes in} a_{13}}]$ and the second order determinant obtained by deleting elements of first row $(\mathrm{R}_1)$ and third column $(\mathrm{C}_3)$ of $|\mathrm{A}|$ as $a_{13}$ lies in $\mathrm{R}_1$ and $\mathrm{C}_3$,

i.e.,

$$
\left| (- 1) ^ {1 + 3} a _ {1 3} \left| \begin{array}{c c} a _ {2 1} & a _ {2 2} \\ a _ {3 1} & a _ {3 2} \end{array} \right| \right|
$$

Step 4 Now the expansion of determinant of A, that is, |A| written as sum of all three terms obtained in steps 1, 2 and 3 above is given by

$$
\det \mathrm{A} = | \mathrm{A} | = (- 1) ^ {1 + 1} a _ {1 1} \left| \begin{array}{l l} a _ {2 2} & a _ {2 3} \\ a _ {3 2} & a _ {3 3} \end{array} \right| + (- 1) ^ {1 + 2} a _ {1 2} \left| \begin{array}{l l} a _ {2 1} & a _ {2 3} \\ a _ {3 1} & a _ {3 3} \end{array} \right|
$$

$$
+ (- 1) ^ {1 + 3} a _ {1 3} \left| \begin{array}{c c} a _ {2 1} & a _ {2 2} \\ a _ {3 1} & a _ {3 2} \end{array} \right|
$$

or

$$
\begin{array}{r l} \left| \mathrm{A} \right| & = a _ {1 1} \left(a _ {2 2} a _ {3 3} - a _ {3 2} a _ {2 3}\right) - a _ {1 2} \left(a _ {2 1} a _ {3 3} - a _ {3 1} a _ {2 3}\right) \\ & + a _ {1 3} \left(a _ {2 1} a _ {3 2} - a _ {3 1} a _ {2 2}\right) \end{array}
$$

Reprint 2025-26

<!-- page 4 of 28 -->

DETERMINANTS

79

$$
\left| \begin{array}{c} = a _ {1 1} a _ {2 2} a _ {3 3} - a _ {1 1} a _ {3 2} a _ {2 3} - a _ {1 2} a _ {2 1} a _ {3 3} + a _ {1 2} a _ {3 1} a _ {2 3} + a _ {1 3} a _ {2 1} a _ {3 2} \\ - a _ {1 3} a _ {3 1} a _ {2 2} \end{array} \right. \dots\tag{... (1}
$$

Note We shall apply all four steps together.

Expansion along second row $(\mathbb{R}_2)$

$$
\mid \mathrm{A} \mid = \left| \begin{array}{c c c} \mathrm{a} _ {1 1} & \mathrm{a} _ {1 2} & \mathrm{a} _ {1 3} \\ \boldsymbol {a} _ {2 1} & \boldsymbol {a} _ {2 2} & \boldsymbol {a} _ {2 3} \\ \mathrm{a} _ {3 1} & \mathrm{a} _ {3 2} & \mathrm{a} _ {3 3} \end{array} \right|
$$

Expanding along $\mathbb{R}_2$, we get

$$
\begin{array}{l} \mid \mathrm{A} \mid = (- 1) ^ {2 + 1} a _ {2 1} \left| \begin{array}{c c} a _ {1 2} & a _ {1 3} \\ a _ {3 2} & a _ {3 3} \end{array} \right| + (- 1) ^ {2 + 2} a _ {2 2} \left| \begin{array}{c c} a _ {1 1} & a _ {1 3} \\ a _ {3 1} & a _ {3 3} \end{array} \right| \\ \quad + (- 1) ^ {2 + 3} a _ {2 3} \left| \begin{array}{c c} a _ {1 1} & a _ {1 2} \\ a _ {3 1} & a _ {3 2} \end{array} \right| \\ \quad = - a _ {2 1} (a _ {1 2} a _ {3 3} - a _ {3 2} a _ {1 3}) + a _ {2 2} (a _ {1 1} a _ {3 3} - a _ {3 1} a _ {1 3}) \\ \quad - a _ {2 3} (a _ {1 1} a _ {3 2} - a _ {3 1} a _ {1 2}) \\ \mid \mathrm{A} \mid = - a _ {2 1} a _ {1 2} a _ {3 3} + a _ {2 1} a _ {3 2} a _ {1 3} + a _ {2 2} a _ {1 1} a _ {3 3} - a _ {2 2} a _ {3 1} a _ {1 3} - a _ {2 3} a _ {1 1} a _ {3 2} \\ \quad + a _ {2 3} a _ {3 1} a _ {1 2} \\ \quad = a _ {1 1} a _ {2 2} a _ {3 3} - a _ {1 1} a _ {2 3} a _ {3 2} - a _ {1 2} a _ {2 1} a _ {3 3} + a _ {1 2} a _ {2 3} a _ {3 1} + a _ {1 3} a _ {2 1} a _ {3 2} \\ \quad - a _ {1 3} a _ {3 1} a _ {2 2} \end{array} \tag {2}\tag{2}
$$

Expansion along first Column $(\mathrm{C}_1)$

$$
\mid \mathrm{A} \mid = \left| \begin{array}{c c c} \boldsymbol {a} _ {1 1} & a _ {1 2} & a _ {1 3} \\ \boldsymbol {a} _ {2 1} & a _ {2 2} & a _ {2 3} \\ \boldsymbol {a} _ {3 1} & a _ {3 2} & a _ {3 3} \end{array} \right|
$$

By expanding along $C_1$, we get

$$
\begin{array}{r l} \mid \mathrm{A} \mid = & a _ {1 1} (- 1) ^ {1 + 1} \left| \begin{array}{c c} a _ {2 2} & a _ {2 3} \\ a _ {3 2} & a _ {3 3} \end{array} \right| + a _ {2 1} (- 1) ^ {2 + 1} \left| \begin{array}{c c} a _ {1 2} & a _ {1 3} \\ a _ {3 2} & a _ {3 3} \end{array} \right| \\ & + a _ {3 1} (- 1) ^ {3 + 1} \left| \begin{array}{c c} a _ {1 2} & a _ {1 3} \\ a _ {2 2} & a _ {2 3} \end{array} \right| \\ & = a _ {1 1} (a _ {2 2} a _ {3 3} - a _ {2 3} a _ {3 2}) - a _ {2 1} (a _ {1 2} a _ {3 3} - a _ {1 3} a _ {3 2}) + a _ {3 1} (a _ {1 2} a _ {2 3} - a _ {1 3} a _ {2 2}) \end{array}
$$

Reprint 2025-26

<!-- page 5 of 28 -->

80

MATHEMATICS

$$
\left| \begin{array}{c} | \mathrm{A} | = a _ {1 1} a _ {2 2} a _ {3 3} - a _ {1 1} a _ {2 3} a _ {3 2} - a _ {2 1} a _ {1 2} a _ {3 3} + a _ {2 1} a _ {1 3} a _ {3 2} + a _ {3 1} a _ {1 2} a _ {2 3} \\ - a _ {3 1} a _ {1 3} a _ {2 2} \\ = a _ {1 1} a _ {2 2} a _ {3 3} - a _ {1 1} a _ {2 3} a _ {3 2} - a _ {1 2} a _ {2 1} a _ {3 3} + a _ {1 2} a _ {2 3} a _ {3 1} + a _ {1 3} a _ {2 1} a _ {3 2} \\ - a _ {1 3} a _ {3 1} a _ {2 2} \end{array} \right| \dots
$$

Clearly, values of $|\mathrm{A}|$ in (1), (2) and (3) are equal. It is left as an exercise to the reader to verify that the values of $|\mathrm{A}|$ by expanding along $\mathbb{R}_3$, $C_2$ and $C_3$ are equal to the value of $|\mathrm{A}|$ obtained in (1), (2) or (3).

Hence, expanding a determinant along any row or column gives same value.

## Remarks

(i) For easier calculations, we shall expand the determinant along that row or column which contains maximum number of zeros.

(ii) While expanding, instead of multiplying by $(-1)^{i + j}$, we can multiply by $+1$ or $-1$ according as $(i + j)$ is even or odd.

(iii) Let $\mathrm{A} = \begin{bmatrix} 2 & 2 \\ 4 & 0 \end{bmatrix}$ and $\mathrm{B} = \begin{bmatrix} 1 & 1 \\ 2 & 0 \end{bmatrix}$. Then, it is easy to verify that $\mathrm{A} = 2\mathrm{B}$. Also $|\mathrm{A}| = 0 - 8 = -8$ and $|\mathrm{B}| = 0 - 2 = -2$.

Observe that, $|\mathrm{A}| = 4(-2) = 2^2 |\mathrm{B}|$ or $|\mathrm{A}| = 2^n |\mathrm{B}|$, where $n = 2$ is the order of square matrices A and B.

In general, if $\mathrm{A} = k\mathrm{B}$ where $\mathrm{A}$ and $\mathrm{B}$ are square matrices of order $n$, then $|\mathrm{A}| = k^n \mid \mathrm{B}|$, where $n = 1, 2, 3$

Example 3 Evaluate the determinant $\Delta = \begin{vmatrix} 1 & 2 & 4 \\ -1 & 3 & 0 \\ 4 & 1 & 0 \end{vmatrix}$.

Solution Note that in the third column, two entries are zero. So expanding along third column ( $C_{3}$ ), we get

$$
\begin{array}{r l} \Delta = 4 \left| \begin{array}{c c} - 1 & 3 \\ 4 & 1 \end{array} \right| - 0 \left| \begin{array}{c c} 1 & 2 \\ 4 & 1 \end{array} \right| + 0 \left| \begin{array}{c c} 1 & 2 \\ - 1 & 3 \end{array} \right| \\ = 4 (- 1 - 1 2) - 0 + 0 = - 5 2 \end{array}
$$

Example 4 Evaluate $\Delta = \begin{vmatrix} 0 & \sin \alpha & -\cos \alpha \\ -\sin \alpha & 0 & \sin \beta \\ \cos \alpha & -\sin \beta & 0 \end{vmatrix}$.

Reprint 2025-26

<!-- page 6 of 28 -->

DETERMINANTS

81

Solution Expanding along $\mathbb{R}_1$, we get

$$
\begin{array}{l} \Delta = 0 \left| \begin{array}{c c} 0 & \sin \beta \\ - \sin \beta & 0 \end{array} \right| - \sin \alpha \left| \begin{array}{c c} - \sin \alpha & \sin \beta \\ \cos \alpha & 0 \end{array} \right| - \cos \alpha \left| \begin{array}{c c} - \sin \alpha & 0 \\ \cos \alpha & - \sin \beta \end{array} \right| \\ = 0 - \sin \alpha (0 - \sin \beta \cos \alpha) - \cos \alpha (\sin \alpha \sin \beta - 0) \\ = \sin \alpha \sin \beta \cos \alpha - \cos \alpha \sin \alpha \sin \beta = 0 \end{array}
$$

Example 5 Find values of $x$ for which $\begin{vmatrix} 3 & x \\ x & 1 \end{vmatrix} = \begin{vmatrix} 3 & 2 \\ 4 & 1 \end{vmatrix}$.

Solution We have $\left| \begin{array}{cc}3 & x\\ x & 1 \end{array} \right| = \left| \begin{array}{cc}3 & 2\\ 4 & 1 \end{array} \right|$

i.e.

$$
3 - x ^ {2} = 3 - 8
$$

i.e.

$$
x ^ {2} = 8
$$

Hence

$$
x = \pm 2 \sqrt {2}
$$

## EXERCISE 4.1

Evaluate the determinants in Exercises 1 and 2.

1. $\begin{vmatrix}2&4\\-5&-1\end{vmatrix}$

2. (i) $\begin{vmatrix}\cos\theta & -\sin\theta \\ \sin\theta & \cos\theta\end{vmatrix}$

(ii)

$$
\left| \begin{array}{c c} x ^ {2} - x + 1 & x - 1 \\ x + 1 & x + 1 \end{array} \right|
$$

3. If  $A = \begin{bmatrix} 1 & 2 \\ 4 & 2 \end{bmatrix}$ , then show that  $|2A| = 4|A|$

4. If  $A = \begin{bmatrix} 1 & 0 & 1 \\ 0 & 1 & 2 \\ 0 & 0 & 4 \end{bmatrix}$ , then show that  $|3A| = 27|A|$

5. Evaluate the determinants

(i)

$$
\left| \begin{array}{c c c} 3 & - 1 & - 2 \\ 0 & 0 & - 1 \\ 3 & - 5 & 0 \end{array} \right|
$$

(ii)

$$
\left| \begin{array}{c c c} 3 & - 4 & 5 \\ 1 & 1 & - 2 \\ 2 & 3 & 1 \end{array} \right|
$$

Reprint 2025-26

<!-- page 7 of 28 -->

82

MATHEMATICS

$$
\left| \begin{array}{c c c} 0 & 1 & 2 \\ - 1 & 0 & - 3 \\ - 2 & 3 & 0 \end{array} \right|\tag{iii}
$$

(iv)

$$
\left| \begin{array}{c c c} 2 & - 1 & - 2 \\ 0 & 2 & - 1 \\ 3 & - 5 & 0 \end{array} \right|
$$

6. If A =  $\begin{bmatrix}1 & 1 & -2 \\ 2 & 1 & -3 \\ 5 & 4 & -9\end{bmatrix}$ , find |A|

7. Find values of x, if

$$
\left| \begin{array}{c c} 2 & 4 \\ 5 & 1 \end{array} \right| = \left| \begin{array}{c c} 2 x & 4 \\ 6 & x \end{array} \right|\tag{i}
$$

$$
\left| \begin{array}{c c} 2 & 3 \\ 4 & 5 \end{array} \right| = \left| \begin{array}{c c} x & 3 \\ 2 x & 5 \end{array} \right|
$$

8. If  $\begin{vmatrix} x & 2 \\ 18 & x \end{vmatrix} = \begin{vmatrix} 6 & 2 \\ 18 & 6 \end{vmatrix}$ , then x is equal to
(A) 6 (B) ± 6 (C) - 6 (D) 0

## 4.3 Area of a Triangle

In earlier classes, we have studied that the area of a triangle whose vertices are  $(x_{1}, y_{1})$ ,  $(x_{2}, y_{2})$  and  $(x_{3}, y_{3})$ , is given by the expression  $\frac{1}{2}[x_{1}(y_{2}-y_{3}) + x_{2}(y_{3}-y_{1}) + x_{3}(y_{1}-y_{2})]$ . Now this expression can be written in the form of a determinant as

$$
\Delta = \frac {1}{2} \left| \begin{array}{c c c} x _ {1} & y _ {1} & 1 \\ x _ {2} & y _ {2} & 1 \\ x _ {3} & y _ {3} & 1 \end{array} \right|\tag{... (1}
$$

Remarks

(i) Since area is a positive quantity, we always take the absolute value of the determinant in (1).

(ii) If area is given, use both positive and negative values of the determinant for calculation.

(iii) The area of the triangle formed by three collinear points is zero.

Example 6 Find the area of the triangle whose vertices are (3, 8), (-4, 2) and (5, 1). Solution The area of triangle is given by

$$
\Delta = \frac {1}{2} \left| \begin{array}{c c c} 3 & 8 & 1 \\ - 4 & 2 & 1 \\ 5 & 1 & 1 \end{array} \right|
$$

Reprint 2025-26

<!-- page 8 of 28 -->

DETERMINANTS

83

$$
\begin{array}{l} = \frac {1}{2} [ 3 (2 - 1) - 8 (- 4 - 5) + 1 (- 4 - 1 0) ] \\ = \frac {1}{2} (3 + 7 2 - 1 4) = \frac {6 1}{2} \end{array}
$$

Example 7 Find the equation of the line joining A(1, 3) and B(0, 0) using determinants and find $k$ if D(k, 0) is a point such that area of triangle ABD is 3sq units.

Solution Let $\mathrm{P}(x,y)$ be any point on AB. Then, area of triangle ABP is zero (Why?). So

$$
\frac {1}{2} \left| \begin{array}{c c c} 0 & 0 & 1 \\ 1 & 3 & 1 \\ x & y & 1 \end{array} \right| = 0
$$

This gives

$$
\frac {1}{2} (y - 3 x) = 0 \text {or} y = 3 x,
$$

which is the equation of required line AB.

Also, since the area of the triangle ABD is 3 sq. units, we have

$$
\frac {1}{2} \left| \begin{array}{c c c} 1 & 3 & 1 \\ 0 & 0 & 1 \\ k & 0 & 1 \end{array} \right| = \pm 3
$$

This gives, $\frac{-3k}{2} = \pm 3$, i.e., $k = \mp 2$.

## EXERCISE 4.2

1. Find area of the triangle with vertices at the point given in each of the following:
(i)  $(1,0)$ ,  $(6,0)$ ,  $(4,3)$ 
(ii)  $(2,7)$ ,  $(1,1)$ ,  $(10,8)$ 
(iii)  $(-2,-3)$ ,  $(3,2)$ ,  $(-1,-8)$

2. Show that points A $(a, b + c)$, B $(b, c + a)$, C $(c, a + b)$ are collinear.

3. Find values of $k$ if area of triangle is 4 sq. units and vertices are (i) $(k,0),(4,0),(0,2)$ (ii) $(-2,0),(0,4),(0,k)$

4. (i) Find equation of line joining (1, 2) and (3, 6) using determinants.
(ii) Find equation of line joining (3, 1) and (9, 3) using determinants.

5. If area of triangle is 35 sq units with vertices $(2, -6)$, $(5, 4)$ and $(k, 4)$. Then $k$ is (A) 12 (B) -2 (C) -12, -2 (D) 12, -2

Reprint 2025-26

<!-- page 9 of 28 -->

84

MATHEMATICS

## 4.4 Minors and Cofactors

In this section, we will learn to write the expansion of a determinant in compact form using minors and cofactors.

Definition 1 Minor of an element $a_{ij}$ of a determinant is the determinant obtained by deleting its $i$th row and $j$th column in which element $a_{ij}$ lies. Minor of an element $a_{ij}$ is denoted by $\mathrm{M}_{ij}$.

Remark Minor of an element of a determinant of order $n(n \geq 2)$ is a determinant of order $n - 1$.

Example 8 Find the minor of element 6 in the determinant $\Delta = \begin{vmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{vmatrix}$

Solution Since 6 lies in the second row and third column, its minor $\mathrm{M}_{23}$ is given by

$\mathrm{M}_{23} = \left| \begin{array}{ll}1 & 2\\ 7 & 8 \end{array} \right| = 8 - 14 = -6$ (obtained by deleting $\mathrm{R}_2$ and $C_3$ in $\Delta$).

Definition 2 Cofactor of an element $a_{ij}$, denoted by $\mathrm{A}_{ij}$ is defined by

$\mathrm{A}_{ij} = (-1)^{i + j}\mathrm{M}_{ij}$, where $\mathrm{M}_{ij}$ is minor of $a_{ij}$.

Example 9 Find minors and cofactors of all the elements of the determinant $\left| \begin{array}{cc}1 & -2\\ 4 & 3 \end{array} \right|$

Solution Minor of the element $a_{ij}$ is $\mathrm{M}_{ij}$

Here $a_{11} = 1$. So $\mathrm{M}_{11} =$ Minor of $a_{11} = 3$

$$
\mathrm{M} _ {1 2} = \text {Minor of the element} a _ {1 2} = 4
$$

$$
\mathrm{M} _ {2 1} = \text {Minor of the element} a _ {2 1} = - 2
$$

$$
\mathrm{M} _ {2 2} = \text {Minor of the element} a _ {2 2} = 1
$$

Now, cofactor of $a_{ij}$ is $\mathrm{A}_{ij}$. So

$$
\mathrm{A} _ {1 1} = (- 1) ^ {1 + 1} \mathrm{M} _ {1 1} = (- 1) ^ {2} (3) = 3
$$

$$
\mathrm{A} _ {1 2} = (- 1) ^ {1 + 2} \mathrm{M} _ {1 2} = (- 1) ^ {3} (4) = - 4
$$

$$
\mathrm{A} _ {2 1} = (- 1) ^ {2 + 1} \mathrm{M} _ {2 1} = (- 1) ^ {3} (- 2) = 2
$$

$$
\mathrm{A} _ {2 2} = (- 1) ^ {2 + 2} \mathrm{M} _ {2 2} = (- 1) ^ {4} (1) = 1
$$

Reprint 2025-26

<!-- page 10 of 28 -->

DETERMINANTS

85

Example 10 Find minors and cofactors of the elements $a_{11}, a_{21}$ in the determinant

$$
\Delta = \left| \begin{array}{c c c} a _ {1 1} & a _ {1 2} & a _ {1 3} \\ a _ {2 1} & a _ {2 2} & a _ {2 3} \\ a _ {3 1} & a _ {3 2} & a _ {3 3} \end{array} \right|
$$

Solution By definition of minors and cofactors, we have

Minor of $a_{11} = \mathrm{M}_{11} = \begin{vmatrix} a_{22} & a_{23} \\ a_{32} & a_{33} \end{vmatrix} = a_{22} a_{33} - a_{23} a_{32}$

Cofactor of $a_{11} = \mathrm{A}_{11} = (-1)^{1 + 1}$ $\mathrm{M}_{11} = a_{22}a_{33} - a_{23}a_{32}$

Minor of $a_{21} = \mathrm{M}_{21} = \begin{vmatrix} a_{12} & a_{13} \\ a_{32} & a_{33} \end{vmatrix} = a_{12}a_{33} - a_{13}a_{32}$

Cofactor of $a_{21} = \mathrm{A}_{21} = (-1)^{2 + 1}$ $\mathrm{M}_{21} = (-1)$ ($a_{12}a_{33} - a_{13}a_{32}) = -a_{12}a_{33} + a_{13}a_{32}$

Remark Expanding the determinant $\Delta$, in Example 21, along $R_{1}$, we have

$$
\begin{array}{l} \Delta = (- 1) ^ {1 + 1} a _ {1 1} \left| \begin{array}{c c} a _ {2 2} & a _ {2 3} \\ a _ {3 2} & a _ {3 3} \end{array} \right| + (- 1) ^ {1 + 2} a _ {1 2} \left| \begin{array}{c c} a _ {2 1} & a _ {2 3} \\ a _ {3 1} & a _ {3 3} \end{array} \right| + (- 1) ^ {1 + 3} a _ {1 3} \left| \begin{array}{c c} a _ {2 1} & a _ {2 2} \\ a _ {3 1} & a _ {3 2} \end{array} \right| \\ = a _ {1 1} \mathrm{A} _ {1 1} + a _ {1 2} \mathrm{A} _ {1 2} + a _ {1 3} \mathrm{A} _ {1 3}, \text {where A_{ij} is cofactor of a_{ij}} \end{array}
$$

$=$ sum of product of elements of $\mathrm{R}_{\mathrm{t}}$ with their corresponding cofactors

Similarly, $\Delta$ can be calculated by other five ways of expansion that is along $\mathrm{R}_2$, $\mathrm{R}_3$, $\mathrm{C}_1$, $\mathrm{C}_2$ and $\mathrm{C}_3$.

Hence $\Delta =$ sum of the product of elements of any row (or column) with their corresponding cofactors.

Note If elements of a row (or column) are multiplied with cofactors of any other row (or column), then their sum is zero. For example,

$$
\begin{array}{l} \Delta = a _ {1 1} \mathrm{A} _ {2 1} + a _ {1 2} \mathrm{A} _ {2 2} + a _ {1 3} \mathrm{A} _ {2 3} \\ = a _ {1 1} (- 1) ^ {1 + 1} \left| \begin{array}{c c} a _ {1 2} & a _ {1 3} \\ a _ {3 2} & a _ {3 3} \end{array} \right| + a _ {1 2} (- 1) ^ {1 + 2} \left| \begin{array}{c c} a _ {1 1} & a _ {1 3} \\ a _ {3 1} & a _ {3 3} \end{array} \right| + a _ {1 3} (- 1) ^ {1 + 3} \left| \begin{array}{c c} a _ {1 1} & a _ {1 2} \\ a _ {3 1} & a _ {3 2} \end{array} \right| \\ = \left| \begin{array}{c c c} a _ {1 1} & a _ {1 2} & a _ {1 3} \\ a _ {1 1} & a _ {1 2} & a _ {1 3} \\ a _ {3 1} & a _ {3 2} & a _ {3 3} \end{array} \right| = 0 (\text {since R} _ {1} \text {and R} _ {2} \text {are identical}) \end{array}
$$

Similarly, we can try for other rows and columns.

Reprint 2025-26

<!-- page 11 of 28 -->

86

MATHEMATICS

Example 11 Find minors and cofactors of the elements of the determinant

$$
\left| \begin{array}{c c c} 2 & - 3 & 5 \\ 6 & 0 & 4 \\ 1 & 5 & - 7 \end{array} \right| \text {and verify that} a _ {1 1} \mathrm{A} _ {3 1} + a _ {1 2} \mathrm{A} _ {3 2} + a _ {1 3} \mathrm{A} _ {3 3} = 0
$$

Solution We have $\mathrm{M}_{11} = \begin{vmatrix} 0 & 4 \\ 5 & -7 \end{vmatrix} = 0 - 20 = -20$; $\mathrm{A}_{11} = (-1)^{1 + 1}(-20) = -20$

$$
\mathrm{M} _ {1 2} = \left| \begin{array}{c c} 6 & 4 \\ 1 & - 7 \end{array} \right| = - 4 2 - 4 = - 4 6; \quad \mathrm{A} _ {1 2} = (- 1) ^ {1 + 2} (- 4 6) = 4 6
$$

$$
\mathrm{M} _ {1 3} = \left| \begin{array}{c c} 6 & 0 \\ 1 & 5 \end{array} \right| = 3 0 - 0 = 3 0;
$$

$$
\mathrm{A} _ {1 3} = (- 1) ^ {1 + 3} (3 0) = 3 0
$$

$$
\mathrm{M} _ {2 1} = \left| \begin{array}{c c} - 3 & 5 \\ 5 & - 7 \end{array} \right| = 2 1 - 2 5 = - 4;
$$

$$
\mathrm{A} _ {2 1} = (- 1) ^ {2 + 1} (- 4) = 4
$$

$$
\mathrm{M} _ {2 2} = \left| \begin{array}{c c} 2 & 5 \\ 1 & - 7 \end{array} \right| = - 1 4 - 5 = - 1 9;
$$

$$
\mathrm{A} _ {2 2} = (- 1) ^ {2 + 2} (- 1 9) = - 1 9
$$

$$
\mathrm{M} _ {2 3} = \left| \begin{array}{c c} 2 & - 3 \\ 1 & 5 \end{array} \right| = 1 0 + 3 = 1 3;
$$

$$
\mathrm{A} _ {2 3} = (- 1) ^ {2 + 3} (1 3) = - 1 3
$$

$$
\mathrm{M} _ {3 1} = \left| \begin{array}{c c} - 3 & 5 \\ 0 & 4 \end{array} \right| = - 1 2 - 0 = - 1 2;
$$

$$
\mathrm{A} _ {3 1} = (- 1) ^ {3 + 1} (- 1 2) = - 1 2
$$

$$
\mathrm{M} _ {3 2} = \left| \begin{array}{l l} 2 & 5 \\ 6 & 4 \end{array} \right| = 8 - 3 0 = - 2 2; \quad \mathrm{A} _ {3 2} = (- 1) ^ {3 + 2} (- 2 2) = 2 2
$$

and

$$
\mathrm{M} _ {3 3} = \left| \begin{array}{c c} 2 & - 3 \\ 6 & 0 \end{array} \right| = 0 + 1 8 = 1 8;
$$

$$
\mathrm{A} _ {3 3} = (- 1) ^ {3 + 3} (1 8) = 1 8
$$

Now

$$
a _ {1 1} = 2, a _ {1 2} = - 3, a _ {1 3} = 5; \mathrm{A} _ {3 1} = - 1 2, \mathrm{A} _ {3 2} = 2 2, \mathrm{A} _ {3 3} = 1 8
$$

So

$$
a _ {1 1} \mathrm{A} _ {3 1} + a _ {1 2} \mathrm{A} _ {3 2} + a _ {1 3} \mathrm{A} _ {3 3}
$$

$$
= 2 (- 1 2) + (- 3) (2 2) + 5 (1 8) = - 2 4 - 6 6 + 9 0 = 0
$$

Reprint 2025-26

<!-- page 12 of 28 -->

DETERMINANTS

87

## EXERCISE 4.3

Write Minors and Cofactors of the elements of following determinants:

$$
\left| \begin{array}{c c} 2 & - 4 \\ 0 & 3 \end{array} \right|
$$

(ii)

$$
\left| \begin{array}{c c} a & c \\ b & d \end{array} \right|
$$

$$
\left| \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right|
$$

(ii)

$$
\left| \begin{array}{c c c} 1 & 0 & 4 \\ 3 & 5 & - 1 \\ 0 & 1 & 2 \end{array} \right|
$$

3. Using Cofactors of elements of second row, evaluate $\Delta = \begin{vmatrix} 5 & 3 & 8 \\ 2 & 0 & 1 \\ 1 & 2 & 3 \end{vmatrix}$

4. Using Cofactors of elements of third column, evaluate $\Delta = \begin{vmatrix} 1 & x & yz \\ 1 & y & zx \\ 1 & z & xy \end{vmatrix}$.

5. If $\Delta = \begin{vmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{vmatrix}$ and $\mathrm{A}_{ij}$ is Cofactors of $a_{ij}$, then value of $\Delta$ is given by (A) $a_{11} \mathrm{~A}_{31} + a_{12} \mathrm{~A}_{32} + a_{13} \mathrm{~A}_{33}$ (B) $a_{11} \mathrm{~A}_{11} + a_{12} \mathrm{~A}_{21} + a_{13} \mathrm{~A}_{31}$ (C) $a_{21} \mathrm{~A}_{11} + a_{22} \mathrm{~A}_{12} + a_{23} \mathrm{~A}_{13}$ (D) $a_{11} \mathrm{~A}_{11} + a_{21} \mathrm{~A}_{21} + a_{31} \mathrm{~A}_{31}$

## 4.5 Adjoint and Inverse of a Matrix

In the previous chapter, we have studied inverse of a matrix. In this section, we shall discuss the condition for existence of inverse of a matrix.

To find inverse of a matrix $A$, i.e., $A^{-1}$ we shall first define adjoint of a matrix.

## 4.5.1 Adjoint of a matrix

Definition 3 The adjoint of a square matrix $\mathrm{A} = [a_{ij}]_{n\times n}$ is defined as the transpose of the matrix $[\mathrm{A}_{ij}]_{n\times n}$, where $\mathrm{A}_{ij}$ is the cofactor of the element $a_{ij}$. Adjoint of the matrix A is denoted by adj A.

Let

$$
\mathrm{A} = \left[ \begin{array}{c c c} a _ {1 1} & a _ {1 2} & a _ {1 3} \\ a _ {2 1} & a _ {2 2} & a _ {2 3} \\ a _ {3 1} & a _ {3 2} & a _ {3 3} \end{array} \right]
$$

Reprint 2025-26

<!-- page 13 of 28 -->

88

MATHEMATICS

Then

$$
\text {adj} \mathrm{A} = \text {Transpose of} \left[ \begin{array}{l l l} \mathrm{A} _ {1 1} & \mathrm{A} _ {1 2} & \mathrm{A} _ {1 3} \\ \mathrm{A} _ {2 1} & \mathrm{A} _ {2 2} & \mathrm{A} _ {2 3} \\ \mathrm{A} _ {3 1} & \mathrm{A} _ {3 2} & \mathrm{A} _ {3 3} \end{array} \right] = \left[ \begin{array}{l l l} \mathrm{A} _ {1 1} & \mathrm{A} _ {2 1} & \mathrm{A} _ {3 1} \\ \mathrm{A} _ {1 2} & \mathrm{A} _ {2 2} & \mathrm{A} _ {3 2} \\ \mathrm{A} _ {1 3} & \mathrm{A} _ {2 3} & \mathrm{A} _ {3 3} \end{array} \right]
$$

Example 12 Find adj A for $\mathrm{A} = \begin{bmatrix} 2 & 3 \\ 1 & 4 \end{bmatrix}$

Solution We have $\mathrm{A}_{11} = 4, \mathrm{A}_{12} = -1, \mathrm{A}_{21} = -3, \mathrm{A}_{22} = 2$

Hence

$$
\text {adj} \mathrm{A} = \left[ \begin{array}{c c} \mathrm{A} _ {1 1} & \mathrm{A} _ {2 1} \\ \mathrm{A} _ {1 2} & \mathrm{A} _ {2 2} \end{array} \right] = \left[ \begin{array}{c c} 4 & - 3 \\ - 1 & 2 \end{array} \right]
$$

Remark For a square matrix of order 2, given by

$$
\mathrm{A} = \left[ \begin{array}{c c} a _ {1 1} & a _ {1 2} \\ a _ {2 1} & a _ {2 2} \end{array} \right]
$$

The adj A can also be obtained by interchanging $a_{11}$ and $a_{22}$ and by changing signs of $a_{12}$ and $a_{21}$, i.e.,

![Image block](doc:2c9e871/tier:standard/page:13/block:12)

Change sign Interchange

We state the following theorem without proof.

Theorem 1 If A be any given square matrix of order $n$, then

$$
\mathrm{A} (a d j \mathrm{A}) = (a d j \mathrm{A}) \mathrm{A} = | \mathrm{A} | \mathrm{I},
$$

where $I$ is the identity matrix of order $n$

Verification

Let

$$
\mathrm{A} = \left[ \begin{array}{l l l} a _ {1 1} & a _ {1 2} & a _ {1 3} \\ a _ {2 1} & a _ {2 2} & a _ {2 3} \\ a _ {3 1} & a _ {3 2} & a _ {3 3} \end{array} \right], \text {then} a d j \mathrm{A} = \left[ \begin{array}{l l l} \mathrm{A} _ {1 1} & \mathrm{A} _ {2 1} & \mathrm{A} _ {3 1} \\ \mathrm{A} _ {1 2} & \mathrm{A} _ {2 2} & \mathrm{A} _ {3 2} \\ \mathrm{A} _ {1 3} & \mathrm{A} _ {2 3} & \mathrm{A} _ {3 3} \end{array} \right]
$$

Since sum of product of elements of a row (or a column) with corresponding cofactors is equal to  $|A|$  and otherwise zero, we have

Reprint 2025-26

<!-- page 14 of 28 -->

DETERMINANTS

89

$$
\mathrm{A} (a d j \mathrm{A}) = \left[ \begin{array}{c c c} | \mathrm{A} | & 0 & 0 \\ 0 & | \mathrm{A} | & 0 \\ 0 & 0 & | \mathrm{A} | \end{array} \right] = | \mathrm{A} | \left[ \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right] = | \mathrm{A} | \text {I}
$$

Similarly, we can show (adj A) $\mathrm{A} = |\mathrm{A}|$ I

Hence A (adj A) = (adj A) A = |A| 1

Definition 4 A square matrix $\mathrm{A}$ is said to be singular if $|\mathrm{A}| = 0$.

For example, the determinant of matrix  $A = \begin{bmatrix} 1 & 2 \\ 4 & 8 \end{bmatrix}$  is zero
Hence A is a singular matrix.

Definition 5 A square matrix $\mathrm{A}$ is said to be non-singular if $|\mathrm{A}| \neq 0$

Let

$$
\mathrm{A} = \left[ \begin{array}{l l} 1 & 2 \\ 3 & 4 \end{array} \right]. \text {Then} | \mathrm{A} | = \left| \begin{array}{c c} 1 & 2 \\ 3 & 4 \end{array} \right| = 4 - 6 = - 2 \neq 0.
$$

Hence A is a nonsingular matrix

We state the following theorems without proof.

Theorem 2 If A and B are nonsingular matrices of the same order, then AB and BA are also nonsingular matrices of the same order.

Theorem 3 The determinant of the product of matrices is equal to product of their respective determinants, that is, $|\mathbf{AB}| = |\mathbf{A}| |\mathbf{B}|$, where A and B are square matrices of the same order

Remark We know that (adj A) $\mathrm{A} = |\mathrm{A}|$ $\mathrm{I} = \begin{bmatrix} |\mathrm{A}| & 0 & 0 \\ 0 & |\mathrm{A}| & 0 \\ 0 & 0 & |\mathrm{A}|\end{bmatrix}, |\mathrm{A}| \neq 0$

Writing determinants of matrices on both sides, we have

$$
\left| (a d j \mathrm{A}) \mathrm{A} \right| = \left| \begin{array}{c c c} | \mathrm{A} | & 0 & 0 \\ 0 & | \mathrm{A} | & 0 \\ 0 & 0 & | \mathrm{A} | \end{array} \right|
$$

Reprint 2025-26

<!-- page 15 of 28 -->

90

MATHEMATICS

i.e.

$$
\left| (a d j \mathrm{A}) \right| \left| \mathrm{A} \right| = \left| \mathrm{A} \right| ^ {3} \left| \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right|\tag{Why?}
$$

i.e.

$$
\left| (\text {adj} \mathrm{A}) \right| \left| \mathrm{A} \right| = \left| \mathrm{A} \right| ^ {3} (1)
$$

i.e.

$$
| (a d j \mathrm{A}) | = | \mathrm{A} | ^ {2}
$$

In general, if A is $a$ square matrix of order $n$, then $|adj(A)| = |A|^{n-1}$.

Theorem 4 A square matrix $\mathbf{A}$ is invertible if and only if $\mathbf{A}$ is nonsingular matrix.

Proof Let A be invertible matrix of order $n$ and I be the identity matrix of order $n$.

Then, there exists a square matrix $B$ of order $n$ such that $AB = BA = I$

Now $\mathrm{AB} = \mathrm{I}.$ So $|\mathrm{AB}| = |\mathrm{I}|$ or $|\mathrm{A}| |\mathrm{B}| = 1$ (since $|\mathrm{I}| = 1, |\mathrm{AB}| = |\mathrm{A}||\mathrm{B}|$)

This gives  $\left|A\right|\neq0$ . Hence A is nonsingular.

Conversely, let A be nonsingular. Then  $|A| \neq 0$

Now

$$
\mathrm{A} (a d j \mathrm{A}) = (a d j \mathrm{A}) \mathrm{A} = | \mathrm{A} | \mathrm{I}
$$

(Theorem 1)

or

$$
\mathrm{A} \left(\frac {1}{| \mathrm{A} |} \operatorname{adj} \mathrm{A}\right) = \left(\frac {1}{| \mathrm{A} |} \operatorname{adj} \mathrm{A}\right) \mathrm{A} = \mathrm{I}
$$

or

$$
\mathrm{AB} = \mathrm{BA} = \mathrm{I}, \text {where} \mathrm{B} = \frac {1}{| \mathrm{A} |} \mathrm{adj} \mathrm{A}
$$

Thus A is invertible and  $A^{-1}=\frac{1}{|A|}adj$  A

Example 13 If $\mathrm{A} = \begin{bmatrix} 1 & 3 & 3 \\ 1 & 4 & 3 \\ 1 & 3 & 4 \end{bmatrix}$, then verify that $\mathrm{A}adj\mathrm{A} = |\mathrm{A}|$ I. Also find $\mathrm{A}^{-1}$.

Solution We have $|\mathbf{A}| = 1(16 - 9) - 3(4 - 3) + 3(3 - 4) = 1 \neq 0$

Now  $A_{11}=7$ ,  $A_{12}=-1$ ,  $A_{13}=-1$ ,  $A_{21}=-3$ ,  $A_{22}=1$ ,  $A_{23}=0$ ,  $A_{31}=-3$ ,  $A_{32}=0$ ,  $A_{33}=1$

Therefore

$$
\text {adj} \mathrm{A} = \left[ \begin{array}{c c c} 7 & - 3 & - 3 \\ - 1 & 1 & 0 \\ - 1 & 0 & 1 \end{array} \right]
$$

Reprint 2025-26

<!-- page 16 of 28 -->

DETERMINANTS

91

Now

$$
\begin{array}{r l} \mathrm{A} (a d j \mathrm{A}) & = \left[ \begin{array}{c c c} 1 & 3 & 3 \\ 1 & 4 & 3 \\ 1 & 3 & 4 \end{array} \right] \left[ \begin{array}{c c c} 7 & - 3 & - 3 \\ - 1 & 1 & 0 \\ - 1 & 0 & 1 \end{array} \right] \\ & = \left[ \begin{array}{c c c} 7 - 3 - 3 & - 3 + 3 + 0 & - 3 + 0 + 3 \\ 7 - 4 - 3 & - 3 + 4 + 0 & - 3 + 0 + 3 \\ 7 - 3 - 4 & - 3 + 3 + 0 & - 3 + 0 + 4 \end{array} \right] \end{array}
$$

$$
\left| = \left[ \begin{array}{l l l} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right] = (1) \quad \left[ \begin{array}{l l l} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right] = | \mathrm{A} |. \mathrm{I} \right|
$$

Also

$$
\mathrm{A} ^ {- 1} = \frac {1}{| \mathrm{A} |} a d j \mathrm{A} = \frac {1}{1} \left[ \begin{array}{c c c} 7 & - 3 & - 3 \\ - 1 & 1 & 0 \\ - 1 & 0 & 1 \end{array} \right] = \left[ \begin{array}{c c c} 7 & - 3 & - 3 \\ - 1 & 1 & 0 \\ - 1 & 0 & 1 \end{array} \right]
$$

Example 14 If $\mathrm{A} = \begin{bmatrix} 2 & 3 \\ 1 & -4 \end{bmatrix}$ and $\mathrm{B} = \begin{bmatrix} 1 & -2 \\ -1 & 3 \end{bmatrix}$, then verify that $(\mathrm{AB})^{-1} = \mathrm{B}^{-1}\mathrm{A}^{-1}$.

Solution We have AB =  $\begin{bmatrix}2 & 3 \\ 1 & -4\end{bmatrix}\begin{bmatrix}1 & -2 \\ -1 & 3\end{bmatrix}=\begin{bmatrix}-1 & 5 \\ 5 & -14\end{bmatrix}$

Since, $\left|\mathrm{AB}\right| = -11 \neq 0$, $(\mathrm{AB})^{-1}$ exists and is given by

$$
(\mathrm{AB}) ^ {- 1} = \frac {1}{| \mathrm{AB} |} \operatorname{adj} (\mathrm{AB}) = - \frac {1}{1 1} \left[ \begin{array}{l l} - 1 4 & - 5 \\ - 5 & - 1 \end{array} \right] = \frac {1}{1 1} \left[ \begin{array}{l l} 1 4 & 5 \\ 5 & 1 \end{array} \right]
$$

Further, $|\mathrm{A}| = -11 \neq 0$ and $|\mathrm{B}| = 1 \neq 0$. Therefore, $\mathrm{A}^{-1}$ and $\mathrm{B}^{-1}$ both exist and are given by

$$
\mathrm{A} ^ {- 1} = - \frac {1}{1 1} \left[ \begin{array}{c c} - 4 & - 3 \\ - 1 & 2 \end{array} \right], \mathrm{B} ^ {- 1} = \left[ \begin{array}{c c} 3 & 2 \\ 1 & 1 \end{array} \right]
$$

Therefore

$$
\mathrm{B} ^ {- 1} \mathrm{A} ^ {- 1} = - \frac {1}{1 1} \left[ \begin{array}{l l} 3 & 2 \\ 1 & 1 \end{array} \right] \left[ \begin{array}{l l} - 4 & - 3 \\ - 1 & 2 \end{array} \right] = - \frac {1}{1 1} \left[ \begin{array}{l l} - 1 4 & - 5 \\ - 5 & - 1 \end{array} \right] = \frac {1}{1 1} \left[ \begin{array}{l l} 1 4 & 5 \\ 5 & 1 \end{array} \right]
$$

Hence  $(\mathrm{AB})^{-1}=\mathrm{B}^{-1}\mathrm{A}^{-1}$

Reprint 2025-26

<!-- page 17 of 28 -->

92

MATHEMATICS

Example 15 Show that the matrix $\mathrm{A} = \begin{bmatrix} 2 & 3 \\ 1 & 2 \end{bmatrix}$ satisfies the equation $\mathrm{A}^2 - 4\mathrm{A} + \mathrm{I} = \mathrm{O}$, where I is $2 \times 2$ identity matrix and O is $2 \times 2$ zero matrix. Using this equation, find $\mathrm{A}^{-1}$.

Solution We have $\mathrm{A}^2 = \mathrm{A.A} = \begin{bmatrix} 2 & 3 \\ 1 & 2 \end{bmatrix} \begin{bmatrix} 2 & 3 \\ 1 & 2 \end{bmatrix} = \begin{bmatrix} 7 & 12 \\ 4 & 7 \end{bmatrix}$

Hence

$$
\mathrm{A} ^ {2} - 4 \mathrm{A} + \mathrm{I} = \left[ \begin{array}{l l} 7 & 1 2 \\ 4 & 7 \end{array} \right] - \left[ \begin{array}{l l} 8 & 1 2 \\ 4 & 8 \end{array} \right] + \left[ \begin{array}{l l} 1 & 0 \\ 0 & 1 \end{array} \right] = \left[ \begin{array}{l l} 0 & 0 \\ 0 & 0 \end{array} \right] = \mathrm{O}
$$

Now

$$
\mathrm{A} ^ {2} - 4 \mathrm{A} + \mathrm{I} = \mathrm{O}
$$

Therefore

$$
\mathrm{AA-4A=-I}
$$

or A A (A⁻¹) - 4 A A⁻¹ = - I A⁻¹ (Post multiplying by A⁻¹ because |A| ≠ 0)
or A (A A⁻¹) - 4I = - A⁻¹
or AI - 4I = - A⁻¹

or

$$
\mathrm{A} ^ {- 1} = 4 \mathrm{I} - \mathrm{A} = \left[ \begin{array}{l l} 4 & 0 \\ 0 & 4 \end{array} \right] - \left[ \begin{array}{l l} 2 & 3 \\ 1 & 2 \end{array} \right] = \left[ \begin{array}{l l} 2 & - 3 \\ - 1 & 2 \end{array} \right]
$$

Hence

$$
\mathrm{A} ^ {- 1} = \left[ \begin{array}{c c} 2 & - 3 \\ - 1 & 2 \end{array} \right]
$$

## EXERCISE 4.4

Find adjoint of each of the matrices in Exercises 1 and 2.

1.

$$
\left[ \begin{array}{c c} 1 & 2 \\ 3 & 4 \end{array} \right]
$$

2.

$$
\left[ \begin{array}{c c c} 1 & - 1 & 2 \\ 2 & 3 & 5 \\ - 2 & 0 & 1 \end{array} \right]
$$

Verify A (adj A) = (adj A) A = |A| I in Exercises 3 and 4

3.

$$
\left[ \begin{array}{c c} 2 & 3 \\ - 4 & - 6 \end{array} \right]
$$

4.

$$
\left[ \begin{array}{c c c} 1 & - 1 & 2 \\ 3 & 0 & - 2 \\ 1 & 0 & 3 \end{array} \right]
$$

Find the inverse of each of the matrices (if it exists) given in Exercises 5 to 11.

5.

$$
\left[ \begin{array}{c c} 2 & - 2 \\ 4 & 3 \end{array} \right]
$$

6.

$$
\left[ \begin{array}{c c} - 1 & 5 \\ - 3 & 2 \end{array} \right]
$$

7.

$$
\left[ \begin{array}{c c c} 1 & 2 & 3 \\ 0 & 2 & 4 \\ 0 & 0 & 5 \end{array} \right]
$$

Reprint 2025-26

<!-- page 18 of 28 -->

DETERMINANTS

93

$$
\left[ \begin{array}{c c c} 1 & 0 & 0 \\ 3 & 3 & 0 \\ 5 & 2 & - 1 \end{array} \right]
$$

$$
\left[ \begin{array}{c c c} 2 & 1 & 3 \\ 4 & - 1 & 0 \\ - 7 & 2 & 1 \end{array} \right]
$$

$$
\left[ \begin{array}{c c c} 1 & - 1 & 2 \\ 0 & 2 & - 3 \\ 3 & - 2 & 4 \end{array} \right]
$$

11. $\begin{bmatrix}1&0&0\\ 0&\cos\alpha&\sin\alpha\\ 0&\sin\alpha&-\cos\alpha\end{bmatrix}$

12. Let $\mathrm{A} = \begin{bmatrix} 3 & 7 \\ 2 & 5 \end{bmatrix}$ and $\mathrm{B} = \begin{bmatrix} 6 & 8 \\ 7 & 9 \end{bmatrix}$. Verify that $(\mathrm{AB})^{-1} = \mathrm{B}^{-1}\mathrm{A}^{-1}$.

13. If $\mathrm{A} = \begin{bmatrix} 3 & 1 \\ -1 & 2 \end{bmatrix}$, show that $\mathrm{A}^2 - 5\mathrm{A} + 7\mathrm{I} = \mathrm{O}$. Hence find $\mathrm{A}^{-1}$.

14. For the matrix $\mathrm{A} = \begin{bmatrix} 3 & 2 \\ 1 & 1 \end{bmatrix}$, find the numbers $a$ and $b$ such that $\mathrm{A}^2 + a\mathrm{A} + b\mathrm{I} = \mathrm{O}$.

15. For the matrix $\mathrm{A} = \begin{bmatrix} 1 & 1 & 1 \\ 1 & 2 & -3 \\ 2 & -1 & 3 \end{bmatrix}$

Show that $\mathrm{A}^3 - 6\mathrm{A}^2 + 5\mathrm{A} + 11\mathrm{I} = \mathrm{O}$. Hence, find $\mathrm{A}^{-1}$.

16. If A =  $\begin{bmatrix} 2 & -1 & 1 \\ -1 & 2 & -1 \\ 1 & -1 & 2 \end{bmatrix}$

Verify that $\mathrm{A}^3 - 6\mathrm{A}^2 + 9\mathrm{A} - 4\mathrm{I} = \mathrm{O}$ and hence find $\mathrm{A}^{-1}$

17. Let A be a nonsingular square matrix of order $3 \times 3$. Then $|adj$ A is equal to (A) $|\mathrm{A}|$ (B) $|\mathrm{A}|^2$ (C) $|\mathrm{A}|^3$ (D) $3|\mathrm{A}|$

18. If A is an invertible matrix of order 2, then det $(\mathrm{A}^{-1})$ is equal to (A) det (A) (B) $\frac{1}{\det(A)}$ (C) 1 (D) 0

## 4.6 Applications of Determinants and Matrices

In this section, we shall discuss application of determinants and matrices for solving the system of linear equations in two or three variables and for checking the consistency of the system of linear equations.

Reprint 2025-26

<!-- page 19 of 28 -->

94

MATHEMATICS

Consistent system A system of equations is said to be consistent if its solution (one or more) exists.

Inconsistent system A system of equations is said to be inconsistent if its solution does not exist.

Note In this chapter, we restrict ourselves to the system of linear equations having unique solutions only.

## 4.6.1 Solution of system of linear equations using inverse of a matrix

Let us express the system of linear equations as matrix equations and solve them using inverse of the coefficient matrix.

Consider the system of equations

$$
a _ {1} x + b _ {1} y + c _ {1} z = d _ {1}
$$

$$
a _ {2} x + b _ {2} y + c _ {2} z = d _ {2}
$$

$$
a _ {3} x + b _ {3} y + c _ {3} z = d _ {3}
$$

Let

$$
\mathrm{A} = \left[ \begin{array}{l l l} a _ {1} & b _ {1} & c _ {1} \\ a _ {2} & b _ {2} & c _ {2} \\ a _ {3} & b _ {3} & c _ {3} \end{array} \right], \mathrm{X} = \left[ \begin{array}{l} x \\ y \\ z \end{array} \right] \text {and} \mathrm{B} = \left[ \begin{array}{l} d _ {1} \\ d _ {2} \\ d _ {3} \end{array} \right]
$$

Then, the system of equations can be written as, $\mathrm{AX} = \mathrm{B}$, i.e.,

$$
\left[ \begin{array}{c c c} a _ {1} & b _ {1} & c _ {1} \\ a _ {2} & b _ {2} & c _ {2} \\ a _ {3} & b _ {3} & c _ {3} \end{array} \right] \left[ \begin{array}{c} x \\ y \\ z \end{array} \right] = \left[ \begin{array}{c} d _ {1} \\ d _ {2} \\ d _ {3} \end{array} \right]
$$

Case I If A is a nonsingular matrix, then its inverse exists. Now

$$
\mathrm{AX} = \mathrm{B}
$$

or

$$
\mathrm{A} ^ {- 1} (\mathrm{AX}) = \mathrm{A} ^ {- 1} \mathrm{B}
$$

(premultiplying by $\mathrm{A}^{-1}$)

or

$$
(\mathrm{A} ^ {- 1} \mathrm{A}) \mathrm{X} = \mathrm{A} ^ {- 1} \mathrm{B}
$$

(by associative property)

or

$$
\mathrm{IX} = \mathrm{A} ^ {- 1} \mathrm{B}
$$

or

$$
\mathrm{X} = \mathrm{A} ^ {- 1} \mathrm{B}
$$

This matrix equation provides unique solution for the given system of equations as inverse of a matrix is unique. This method of solving system of equations is known as Matrix Method.

Case II If A is a singular matrix, then $|\mathrm{A}| = 0$.

In this case, we calculate (adj A) B.

If (adj A) $\mathrm{B} \neq \mathrm{O}$, (O being zero matrix), then solution does not exist and the system of equations is called inconsistent.

Reprint 2025-26

<!-- page 20 of 28 -->

DETERMINANTS

95

If (adj A) B = O, then system may be either consistent or inconsistent according as the system have either infinitely many solutions or no solution.

Example 16 Solve the system of equations

$$
2 x + 5 y = 1
$$

$$
3 x + 2 y = 7
$$

Solution The system of equations can be written in the form $\mathrm{AX} = \mathrm{B}$, where

$$
\mathrm{A} = \left[ \begin{array}{l l} 2 & 5 \\ 3 & 2 \end{array} \right], \mathrm{X} = \left[ \begin{array}{l} x \\ y \end{array} \right] \text {and} \mathrm{B} = \left[ \begin{array}{l} 1 \\ 7 \end{array} \right]
$$

Now, $|\mathrm{A}| = -11 \neq 0$, Hence, A is nonsingular matrix and so has a unique solution.

Note that

$$
\mathrm{A} ^ {- 1} = - \frac {1}{1 1} \left[ \begin{array}{c c} 2 & - 5 \\ - 3 & 2 \end{array} \right]
$$

Therefore

$$
\mathrm{X} = \mathrm{A} ^ {- 1} \mathrm{B} = - \frac {1}{1 1} \left[ \begin{array}{c c} 2 & - 5 \\ - 3 & 2 \end{array} \right] \left[ \begin{array}{l} 1 \\ 7 \end{array} \right]
$$

i.e.

$$
\left[ \begin{array}{c} x \\ y \end{array} \right] = - \frac {1}{1 1} \left[ \begin{array}{c} - 3 3 \\ 1 1 \end{array} \right] = \left[ \begin{array}{c} 3 \\ - 1 \end{array} \right]
$$

Hence

$$
x = 3, y = - 1
$$

Example 17 Solve the following system of equations by matrix method.

$$
3 x - 2 y + 3 z = 8
$$

$$
2 x + y - z = 1
$$

$$
4 x - 3 y + 2 z = 4
$$

Solution The system of equations can be written in the form $\mathrm{AX} = \mathrm{B}$, where

$$
\mathrm{A} = \left[ \begin{array}{c c c} 3 & - 2 & 3 \\ 2 & 1 & - 1 \\ 4 & - 3 & 2 \end{array} \right], \mathrm{X} = \left[ \begin{array}{l} x \\ y \\ z \end{array} \right] \text {and} \mathrm{B} = \left[ \begin{array}{l} 8 \\ 1 \\ 4 \end{array} \right]
$$

We see that

$$
\left| \mathrm{A} \right| = 3 (2 - 3) + 2 (4 + 4) + 3 (- 6 - 4) = - 1 7 \neq 0
$$

Hence, A is nonsingular and so its inverse exists. Now

$$
\mathrm{A} _ {1 1} = - 1,
$$

$$
\mathrm{A} _ {1 2} = - 8,
$$

$$
\mathrm{A} _ {1 3} = - 1 0
$$

$$
\mathrm{A} _ {2 1} = - 5,
$$

$$
\mathrm{A} _ {2 2} = - 6,
$$

$$
\mathrm{A} _ {2 3} = 1
$$

$$
\mathrm{A} _ {3 1} = - 1,
$$

$$
\mathrm{A} _ {3 2} = 9,
$$

$$
\mathrm{A} _ {3 3} = 7
$$

Reprint 2025-26

<!-- page 21 of 28 -->

96

MATHEMATICS

Therefore

$$
\mathrm{A} ^ {- 1} = - \frac {1}{1 7} \left[ \begin{array}{c c c} - 1 & - 5 & - 1 \\ - 8 & - 6 & 9 \\ - 1 0 & 1 & 7 \end{array} \right]
$$

So

$$
\mathrm{X} = \mathrm{A} ^ {- 1} \mathrm{B} = - \frac {1}{1 7} \left[ \begin{array}{c c c} - 1 & - 5 & - 1 \\ - 8 & - 6 & 9 \\ - 1 0 & 1 & 7 \end{array} \right] \left[ \begin{array}{l} 8 \\ 1 \\ 4 \end{array} \right]
$$

i.e.

$$
\left[ \begin{array}{l} x \\ y \\ z \end{array} \right] = - \frac {1}{1 7} \left[ \begin{array}{l} - 1 7 \\ - 3 4 \\ - 5 1 \end{array} \right] = \left[ \begin{array}{l} 1 \\ 2 \\ 3 \end{array} \right]
$$

Hence

$$
x = 1, y = 2 \text {and} z = 3.
$$

Example 18 The sum of three numbers is 6. If we multiply third number by 3 and add second number to it, we get 11. By adding first and third numbers, we get double of the second number. Represent it algebraically and find the numbers using matrix method.

Solution Let first, second and third numbers be denoted by $x$, $y$ and $z$, respectively. Then, according to given conditions, we have

$$
\begin{array}{c} x + y + z = 6 \\ y + 3 z = 1 1 \\ x + z = 2 y \text {or} x - 2 y + z = 0 \end{array}
$$

This system can be written as $\mathrm{AX} = \mathrm{B}$, where

$$
\mathrm{A} = \left[ \begin{array}{l l l} 1 & 1 & 1 \\ 0 & 1 & 3 \\ 1 & 2 & 1 \end{array} \right], \mathrm{X} = \left[ \begin{array}{l} x \\ y \\ z \end{array} \right] \text {and} \mathrm{B} = \left[ \begin{array}{l} 6 \\ 1 1 \\ 0 \end{array} \right]
$$

Here $|\mathrm{A}| = 1(1 + 6) - (0 - 3) + (0 - 1) = 9 \neq 0$. Now we find adj A

$$
\begin{array}{l l l} \mathrm{A} _ {1 1} = 1 (1 + 6) = 7, & \mathrm{A} _ {1 2} = - (0 - 3) = 3, & \mathrm{A} _ {1 3} = - 1 \\ \mathrm{A} _ {2 1} = - (1 + 2) = - 3, & \mathrm{A} _ {2 2} = 0, & \mathrm{A} _ {2 3} = - (- 2 - 1) = 3 \\ \mathrm{A} _ {3 1} = (3 - 1) = 2, & \mathrm{A} _ {3 2} = - (3 - 0) = - 3, & \mathrm{A} _ {3 3} = (1 - 0) = 1 \end{array}
$$

Hence

$$
\text {adj} \mathrm{A} = \left[ \begin{array}{c c c} 7 & - 3 & 2 \\ 3 & 0 & - 3 \\ - 1 & 3 & 1 \end{array} \right]
$$

Reprint 2025-26

<!-- page 22 of 28 -->

DETERMINANTS

97

Thus

$$
\mathrm{A} ^ {- 1} = \frac {1}{| \mathrm{A} |} a d j (\mathrm{A}) = \frac {1}{9} \left[ \begin{array}{c c c} 7 & - 3 & 2 \\ 3 & 0 & - 3 \\ - 1 & 3 & 1 \end{array} \right]
$$

Since

$$
\mathrm{X} = \mathrm{A} ^ {- 1} \mathrm{B}
$$

$$
\mathrm{X} = \frac {1}{9} \left[ \begin{array}{c c c} 7 & - 3 & 2 \\ 3 & 0 & - 3 \\ - 1 & 3 & 1 \end{array} \right] \left[ \begin{array}{l} 6 \\ 1 1 \\ 0 \end{array} \right]
$$

or

$$
\left[ \begin{array}{l} x \\ y \\ z \end{array} \right] = \frac {1}{9} \left[ \begin{array}{l} 4 2 - 3 3 + 0 \\ 1 8 + 0 + 0 \\ - 6 + 3 3 + 0 \end{array} \right] = \frac {1}{9} \left[ \begin{array}{l} 9 \\ 1 8 \\ 2 7 \end{array} \right] = \left[ \begin{array}{l} 1 \\ 2 \\ 3 \end{array} \right]
$$

Thus

$$
x = 1, y = 2, z = 3
$$

## EXERCISE 4.5

Examine the consistency of the system of equations in Exercises 1 to 6.

1. $x + 2y = 2$

2. $2x - y = 5$

3. $x + 3y = 5$

$$
2 x + 3 y = 3
$$

$$
x + y = 4
$$

$$
2 x + 6 y = 8
$$

4. $x + y + z = 1$

5. $3x - y - 2z = 2$

$$
5 x - y + 4 z = 5
$$

$$
2 x + 3 y + 2 z = 2
$$

$$
2 y - z = - 1
$$

$$
2 x + 3 y + 5 z = 2
$$

$$
a x + a y + 2 a z = 4
$$

$$
3 x - 5 y = 3
$$

$$
5 x - 2 y + 6 z = - 1
$$

Solve system of linear equations, using matrix method, in Exercises 7 to 14.

7. $5x + 2y = 4$

8. $2x - y = -2$

9. $4x - 3y = 3$

$$
7 x + 3 y = 5
$$

$$
3 x + 4 y = 3
$$

$$
3 x - 5 y = 7
$$

$$
1 0. \quad 5 x + 2 y = 3
$$

$$
2 x + y + z = 1
$$

$$
x - y + z = 4 \tag {12}
$$

$$
3 x + 2 y = 5
$$

$$
x - 2 y - z = \frac {3}{2}
$$

$$
2 x + y - 3 z = 0
$$

$$
3 y - 5 z = 9
$$

$$
x + y + z = 2
$$

13. $2x + 3y + 3z = 5$

14. $x - y + 2z = 7$

$$
x - 2 y + z = - 4
$$

$$
3 x + 4 y - 5 z = - 5
$$

$$
3 x - y - 2 z = 3
$$

$$
2 x - y + 3 z = 1 2
$$

Reprint 2025-26

<!-- page 23 of 28 -->

98

MATHEMATICS

15. If $\mathrm{A} = \begin{bmatrix} 2 & -3 & 5 \\ 3 & 2 & -4 \\ 1 & 1 & -2 \end{bmatrix}$, find $\mathrm{A}^{-1}$. Using $\mathrm{A}^{-1}$ solve the system of equations
$2x - 3y + 5z = 11$
$3x + 2y - 4z = -5$
$x + y - 2z = -3$

16. The cost of 4 kg onion, 3 kg wheat and 2 kg rice is ₹60. The cost of 2 kg onion, 4 kg wheat and 6 kg rice is ₹90. The cost of 6 kg onion 2 kg wheat and 3 kg rice is ₹70. Find cost of each item per kg by matrix method.

## Miscellaneous Examples

Example 19 Use product  $\begin{bmatrix}1&1&2\\ 0&2&3\\ 3&2&4\end{bmatrix}\begin{bmatrix}2&0&1\\ 9&2&3\\ 6&1&2\end{bmatrix}$  to solve the system of equations

$$
\left| \begin{array}{c} x - y + 2 z = 1 \\ 2 y - 3 z = 1 \\ 3 x - 2 y + 4 z = 2 \end{array} \right|
$$

Solution Consider the product  $\begin{bmatrix}1&-1&2\\ 0&2&-3\\ 3&-2&4\end{bmatrix}\begin{bmatrix}-2&0&1\\ 9&2&-3\\ 6&1&-2\end{bmatrix}$

$$
= \left[ \begin{array}{c c c} - 2 - 9 + 1 2 & 0 - 2 + 2 & 1 + 3 - 4 \\ 0 + 1 8 - 1 8 & 0 + 4 - 3 & 0 - 6 + 6 \\ - 6 - 1 8 + 2 4 & 0 - 4 + 4 & 3 + 6 - 8 \end{array} \right] = \left[ \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right]
$$

Hence

$$
\left[ \begin{array}{r r r} 1 & - 1 & 2 \\ 0 & 2 & - 3 \\ 3 & - 2 & 4 \end{array} \right] ^ {- 1} = \left[ \begin{array}{r r r} - 2 & 0 & 1 \\ 9 & 2 & - 3 \\ 6 & 1 & - 2 \end{array} \right]
$$

Now, given system of equations can be written, in matrix form, as follows

$$
\left| \left[ \begin{array}{r r r} 1 & - 1 & 2 \\ 0 & 2 & - 3 \\ 3 & - 2 & 4 \end{array} \right] \left[ \begin{array}{l} x \\ y \\ z \end{array} \right] = \left[ \begin{array}{l} 1 \\ 1 \\ 2 \end{array} \right] \right|
$$

Reprint 2025-26

<!-- page 24 of 28 -->

DETERMINANTS

99

or

$$
\begin{array}{l} \left[ \begin{array}{c c} x & \\ y & = \left[ \begin{array}{c c c} 1 & - 1 & 2 \\ 0 & 2 & - 3 \\ 3 & - 2 & 4 \end{array} \right] ^ {- 1} \left[ \begin{array}{c} 1 \\ 1 \\ 2 \end{array} \right] = \left[ \begin{array}{c c c} 2 & 0 & 1 \\ 9 & 2 & 3 \\ 6 & 1 & 2 \end{array} \right] \left[ \begin{array}{c} 1 \\ 1 \\ 2 \end{array} \right] \end{array} \right] \end{array}
$$

$$
= \left[ \begin{array}{c} - 2 + 0 + 2 \\ 9 + 2 - 6 \\ 6 + 1 - 4 \end{array} \right] = \left[ \begin{array}{c} 0 \\ 5 \\ 3 \end{array} \right]
$$

Hence

$$
x = 0, y = 5 \text {and} z = 3
$$

Miscellaneous Exercises on Chapter 4

1. Prove that the determinant  $\begin{vmatrix} x & \sin\theta & \cos\theta \\ -\sin\theta & -x & 1 \\ \cos\theta & 1 & x \end{vmatrix}$  is independent of  $\theta$ .

2. Evaluate  $\begin{vmatrix}\cos\alpha\cos\beta & \cos\alpha\sin\beta & -\sin\alpha \\ -\sin\beta & \cos\beta & 0 \\ \sin\alpha\cos\beta & \sin\alpha\sin\beta & \cos\alpha\end{vmatrix}$

3. If $\mathrm{A}^{-1} = \begin{bmatrix} 3 & -1 & 1 \\ -15 & 6 & -5 \\ 5 & -2 & 2 \end{bmatrix}$ and $\mathrm{B} = \begin{bmatrix} 1 & 2 & -2 \\ -1 & 3 & 0 \\ 0 & -2 & 1 \end{bmatrix}$, find $(\mathrm{AB})^{-1}$

4. Let $\mathrm{A} = \begin{bmatrix} 1 & 2 & 1\\ 2 & 3 & 1\\ 1 & 1 & 5 \end{bmatrix}$. Verify that

$$
(\mathrm{i}) [ \text {adj A} ] ^ {- 1} = \text {adj (A} ^ {- 1})
$$

$$
(\mathrm{ii}) \quad (\mathrm{A} ^ {- 1}) ^ {- 1} = \mathrm{A}
$$

5. Evaluate  $\begin{vmatrix} x & y & x + y \\ y & x + y & x \\ x + y & x & y \end{vmatrix}$

6. Evaluate $\begin{vmatrix} 1 & x & y \\ 1 & x + y & y \\ 1 & x & x + y \end{vmatrix}$

Reprint 2025-26

<!-- page 25 of 28 -->

100

MATHEMATICS

Using properties of determinants in Exercises 11 to 15, prove that:

7. Solve the system of equations

$$
\left| \frac {2}{x} + \frac {3}{y} + \frac {1 0}{z} = 4 \right|
$$

$$
\left| \frac {4}{x} - \frac {6}{y} + \frac {5}{z} = 1 \right|
$$

$$
\frac {6}{x} + \frac {9}{y} - \frac {2 0}{z} = 2
$$

Choose the correct answer in Exercise 17 to 19.

8. If $x, y, z$ are nonzero real numbers, then the inverse of matrix $\mathbf{A} = \begin{bmatrix} x & 0 & 0 \\ 0 & y & 0 \\ 0 & 0 & z \end{bmatrix}$ is

(A)

$$
\left[ \begin{array}{c c c} x ^ {- 1} & 0 & 0 \\ 0 & y ^ {- 1} & 0 \\ 0 & 0 & z ^ {- 1} \end{array} \right]
$$

(B)

$$
xyz \left[ \begin{array}{ccc}x^{-1} & 0 & 0\\ 0 & y^{-1} & 0\\ 0 & 0 & z^{-1} \end{array} \right]
$$

(C)

$$
\frac {1}{x y z} \left[ \begin{array}{c c c} x & 0 & 0 \\ 0 & y & 0 \\ 0 & 0 & z \end{array} \right]
$$

(D)

$$
\frac {1}{x y z} \left[ \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right]
$$

9. Let $A = \begin{bmatrix} 1 & \sin \theta & 1 \\ -\sin \theta & 1 & \sin \theta \\ -1 & -\sin \theta & 1 \end{bmatrix}$, where $0 \leq \theta \leq 2\pi$. Then

(A) Det (A) = 0

(B) $\operatorname{Det}(\mathrm{A})\in (2,\infty)$

(C) $\operatorname{Det}(\mathrm{A})\in (2,4)$

(D) $\operatorname{Det}(\mathrm{A})\in [2,4]$

Reprint 2025-26

<!-- page 26 of 28 -->

DETERMINANTS

101

## Summary

Determinant of a matrix $\mathrm{A} = [a_{11}]_{1\times 1}$ is given by $|a_{11}| = a_{11}$

◆ Determinant of a matrix  $A=\begin{bmatrix}a_{11}&a_{12}\\ a_{21}&a_{22}\end{bmatrix}$  is given by

$$
\left| \mathrm{A} \right| = \left| \begin{array}{c c} a _ {1 1} & a _ {1 2} \\ a _ {2 1} & a _ {2 2} \end{array} \right| = a _ {1 1} a _ {2 2} - a _ {1 2} a _ {2 1}
$$

Determinant of a matrix $\mathrm{A} = \begin{bmatrix} a_1 & b_1 & c_1 \\ a_2 & b_2 & c_2 \\ a_3 & b_3 & c_3 \end{bmatrix}$ is given by (expanding along $\mathrm{R}_1$)

$$
\left| \mathrm{A} \right| = \left| \begin{array}{c c c} a _ {1} & b _ {1} & c _ {1} \\ a _ {2} & b _ {2} & c _ {2} \\ a _ {3} & b _ {3} & c _ {3} \end{array} \right| = a _ {1} \left| \begin{array}{c c} b _ {2} & c _ {2} \\ b _ {3} & c _ {3} \end{array} \right| - b _ {1} \left| \begin{array}{c c} a _ {2} & c _ {2} \\ a _ {3} & c _ {3} \end{array} \right| + c _ {1} \left| \begin{array}{c c} a _ {2} & b _ {2} \\ a _ {3} & b _ {3} \end{array} \right|
$$

For any square matrix $\mathrm{A}$, the $|\mathrm{A}|$ satisfy following properties.

Area of a triangle with vertices $(x_{1},y_{1}),(x_{2},y_{2})$ and $(x_{3},y_{3})$ is given by

![Image block](doc:2c9e871/tier:standard/page:26/block:11)

$$
\Delta = \frac {1}{2} \left| \begin{array}{c c c} x _ {1} & y _ {1} & 1 \\ x _ {2} & y _ {2} & 1 \\ x _ {3} & y _ {3} & 1 \end{array} \right|
$$

Minor of an element $a_{ij}$ of the determinant of matrix A is the determinant obtained by deleting $i^{\text{th}}$ row and $j^{th}$ column and denoted by $\mathrm{M}_{ij}$.

Cofactor of $a_{ij}$ of given by $\mathrm{A}_{ij} = (-1)^{i + j}\mathrm{M}_{ij}$

Value of determinant of a matrix A is obtained by sum of product of elements of a row (or a column) with corresponding cofactors. For example,

$$
\left| \mathrm{A} \right| = a _ {1 1} \mathrm{A} _ {1 1} + a _ {1 2} \mathrm{A} _ {1 2} + a _ {1 3} \mathrm{A} _ {1 3}.
$$

If elements of one row (or column) are multiplied with cofactors of elements of any other row (or column), then their sum is zero. For example, $a_{11}\mathrm{A}_{21} + a_{12}\mathrm{A}_{22} + a_{13}\mathrm{A}_{23} = 0$

Reprint 2025-26

<!-- page 27 of 28 -->

102

MATHEMATICS

If $\mathbf{A} = \begin{bmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{bmatrix}$, then $adj\mathbf{A} = \begin{bmatrix} \mathrm{A}_{11} & \mathrm{A}_{21} & \mathrm{A}_{31} \\ \mathrm{A}_{12} & \mathrm{A}_{22} & \mathrm{A}_{32} \\ \mathrm{A}_{13} & \mathrm{A}_{23} & \mathrm{A}_{33} \end{bmatrix}$, where $\mathrm{A}_{ij}$ is cofactor of $a_{ij}$

A (adj A) = (adj A) A = |A| I, where A is square matrix of order n.

A square matrix A is said to be singular or non-singular according as  $|A| = 0$  or  $|A| \neq 0$ .

If AB = BA = I, where B is square matrix, then B is called inverse of A. Also  $A^{-1} = B$  or  $B^{-1} = A$  and hence  $(A^{-1})^{-1} = A$ .

A square matrix A has inverse if and only if A is non-singular.

$\mathrm{A}^{-1} = \frac{1}{|\mathrm{A}|} (adj\mathrm{A})$

If $a_1x + b_1y + c_1z = d_1$

$$
\left| a _ {2} x + b _ {2} y + c _ {2} z = d _ {2} \right.
$$

$$
a _ {3} x + b _ {3} y + c _ {3} z = d _ {3},
$$

then these equations can be written as $\mathrm{AX} = \mathrm{B}$, where

$$
\mathrm{A} = \left[ \begin{array}{c c c} a _ {1} & b _ {1} & c _ {1} \\ a _ {2} & b _ {2} & c _ {2} \\ a _ {3} & b _ {3} & c _ {3} \end{array} \right], \mathrm{X} = \left[ \begin{array}{c} x \\ y \\ z \end{array} \right] \text {and} \mathrm{B} = \left[ \begin{array}{c} d _ {1} \\ d _ {2} \\ d _ {3} \end{array} \right]
$$

\- Unique solution of equation $\mathrm{AX} = \mathrm{B}$ is given by $\mathrm{X} = \mathrm{A}^{-1}\mathrm{B}$, where $|\mathrm{A}| \neq 0$

A system of equation is consistent or inconsistent according as its solution exists or not.

For a square matrix $A$ in matrix equation $AX = B$

(i) $|\mathrm{A}| \neq 0$, there exists unique solution

(ii) $|\mathrm{A}| = 0$ and (adj A) $\mathrm{B} \neq 0$, then there exists no solution

(iii) $|\mathrm{A}| = 0$ and (adj A) $\mathrm{B} = 0$, then system may or may not be consistent.

Reprint 2025-26

<!-- page 28 of 28 -->

DETERMINANTS

103

# Historical Note

The Chinese method of representing the coefficients of the unknowns of several linear equations by using rods on a calculating board naturally led to the discovery of simple method of elimination. The arrangement of rods was precisely that of the numbers in a determinant. The Chinese, therefore, early developed the idea of subtracting columns and rows as in simplification of a determinant Mikami, China, pp 30, 93.

Seki Kowa, the greatest of the Japanese Mathematicians of seventeenth century in his work ‘Kai Fukudai no Ho’ in 1683 showed that he had the idea of determinants and of their expansion. But he used this device only in eliminating a quantity from two equations and not directly in the solution of a set of simultaneous linear equations. T. Hayashi, “The Fakudoi and Determinants in Japanese Mathematics,” in the proc. of the Tokyo Math. Soc., V.

Vendermonde was the first to recognise determinants as independent functions. He may be called the formal founder. Laplace (1772), gave general method of expanding a determinant in terms of its complementary minors. In 1773 Lagrange treated determinants of the second and third orders and used them for purpose other than the solution of equations. In 1801, Gauss used determinants in his theory of numbers.

The next great contributor was Jacques - Philippe - Marie Binet, (1812) who stated the theorem relating to the product of two matrices of m-columns and n-rows, which for the special case of m = n reduces to the multiplication theorem.

Also on the same day, Cauchy (1812) presented one on the same subject. He used the word ‘determinant’ in its present sense. He gave the proof of multiplication theorem more satisfactory than Binet’s.

The greatest contributor to the theory was Carl Gustav Jacob Jacobi, after this the word determinant received its final acceptance.

Reprint 2025-26