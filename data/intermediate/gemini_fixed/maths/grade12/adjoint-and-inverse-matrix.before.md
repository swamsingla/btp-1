
# Adjoint and Inverse of a Matrix

In the previous chapter, we learned about the basic algebra of matrices and how they can represent systems of linear equations [S3]. A matrix is a powerful tool, but just like a number, it is often useful to find its inverse. To do this, we first need a specific matrix called the adjoint. The adjoint is a stepping stone that allows us to calculate the inverse of any square matrix, provided a certain condition is met.

## Adjoint of a Matrix

The adjoint of a square matrix is a fundamental concept used to find the inverse. According to Definition 3, the adjoint of a square matrix $A = [a_{ij}]_{n\times n}$ is defined as the transpose of the matrix $[A_{ij}]_{n\times n}$, where $A_{ij}$ is the cofactor of the element $a_{ij}$. The adjoint of the matrix A is denoted by adj A [S2].

To understand this, consider a 3 by 3 matrix:
$$
\mathrm{A} = \left[ \begin{array}{c c c} a _ {1 1} & a _ {1 2} & a _ {1 3} \\ a _ {2 1} & a _ {2 2} & a _ {2 3} \\ a _ {3 1} & a _ {3 2} & a _ {3 3} \end{array} \right]
$$
To find the adjoint of this matrix, we first construct a matrix of cofactors, and then we take its transpose. This means we swap the rows and columns. The resulting adjoint matrix looks like this:
$$
\text{adj} \mathrm{A} = \left[ \begin{array}{l l l} \mathrm{A} _ {1 1} & \mathrm{A} _ {2 1} & \mathrm{A} _ {3 1} \\ \mathrm{A} _ {1 2} & \mathrm{A} _ {2 2} & \mathrm{A} _ {3 2} \\ \mathrm{A} _ {1 3} & \mathrm{A} _ {2 3} & \mathrm{A} _ {3 3} \end{array} \right]
$$

For a 2 by 2 matrix, there is a much simpler shortcut. If the matrix is:
$$
\mathrm{A} = \left[ \begin{array}{c c} a _ {1 1} & a _ {1 2} \\ a _ {2 1} & a _ {2 2} \end{array} \right]
$$
The adj A can be obtained by interchanging $a_{11}$ and $a_{22}$ and by changing the signs of $a_{12}$ and $a_{21}$ [S2].

**Example 12** illustrates this perfectly. If we have the matrix $\mathrm{A} = \begin{bmatrix} 2 & 3 \\ 1 & 4 \end{bmatrix}$, we apply the shortcut. We interchange 2 and 4, and we change the signs of 3 and 1. This gives us:
$$
\text{adj} \mathrm{A} = \left[ \begin{array}{c c} 4 & - 3 \\ - 1 & 2 \end{array} \right]
$$
This shortcut saves a lot of time when dealing with smaller matrices.

## Singular and Non-Singular Matrices

Before we can find the inverse of a matrix, we need to understand whether the matrix is invertible. This depends on its determinant. 

A square matrix $\mathrm{A}$ is said to be singular if $|\mathrm{A}| = 0$ [S2]. For example, if we look at the matrix $A = \begin{bmatrix} 1 & 2 \\ 4 & 8 \end{bmatrix}$, the determinant of this matrix is zero. Hence, A is a singular matrix [S2].

Conversely, a square matrix $\mathrm{A}$ is said to be non-singular if $|\mathrm{A}| \neq 0$ [S2]. For instance, if we take $\mathrm{A} = \left[ \begin{array}{l l} 1 & 2 \\ 3 & 4 \end{array} \right]$, then $| \mathrm{A} | = \left| \begin{array}{c c} 1 & 2 \\ 3 & 4 \end{array} \right| = 4 - 6 = - 2 \neq 0$. Hence, A is a nonsingular matrix [S2].

## The Condition for the Inverse

Theorem 4 states that a square matrix $\mathbf{A}$ is invertible if and only if $\mathbf{A}$ is a nonsingular matrix [S2]. This means that the existence of an inverse is entirely dependent on the determinant. If the determinant is zero, the matrix is singular, and no inverse exists. 

Because of this, the inverse of a matrix $A$, denoted $A^{-1}$, is calculated using the adjoint and the determinant. The formula is:
$$
A^{-1} = \frac{1}{|A|} \text{adj} A
$$
This formula holds true when $|A| \neq 0$ [S2].

## The Fundamental Theorem

Theorem 1 gives us a crucial relationship between a matrix, its adjoint, and its determinant [S2]. It states that if A is any given square matrix of order $n$, then:
$$
\mathrm{A} (a d j \mathrm{A}) = (a d j \mathrm{A}) \mathrm{A} = | \mathrm{A} | \mathrm{I}
$$
where $I$ is the identity matrix of order $n$ [S2].

This theorem is the foundation of the inverse formula. It tells us that when we multiply a matrix by its adjoint, we get the determinant multiplied by the identity matrix. If the determinant is not zero, we can simply divide both sides by the determinant to isolate the identity matrix. This gives us:
$$
\mathrm{A} \left(\frac {1}{| \mathrm{A} |} \operatorname{adj} \mathrm{A}\right) = \left(\frac {1}{| \mathrm{A} |} \operatorname{adj} \mathrm{A}\right) \mathrm{A} = \mathrm{I}
$$
Since $A^{-1}$ is defined as the matrix that, when multiplied by $A$, gives the identity matrix, we can see that $A^{-1} = \frac{1}{|A|} \text{adj} A$ [S2].

## Worked Example

Let's apply this to a 3 by 3 matrix to see how it works in practice.

**Example 13:** If $\mathrm{A} = \begin{bmatrix} 1 & 3 & 3 \\ 1 & 4 & 3 \\ 1 & 3 & 4 \end{bmatrix}$, verify that $\mathrm{A}adj\mathrm{A} = |\mathrm{A}|$ I. Also find $\mathrm{A}^{-1}$ [S2].

**Solution:** 
First, we need to find the determinant of A. 
$|\mathbf{A}| = 1(16 - 9) - 3(4 - 3) + 3(3 - 4) = 1 \neq 0$ [S2].
Since the determinant is 1, the matrix is non-singular, and an inverse exists.

Next, we find the cofactors and the adjoint. The cofactors are:
$A_{11}=7, A_{12}=-1, A_{13}=-1, A_{21}=-3, A_{22}=1, A_{23}=0, A_{31}=-3, A_{32}=0, A_{33}=1$ [S2].
The adjoint is the transpose of the cofactor matrix:
$$
\text{adj} \mathrm{A} = \left[ \begin{array}{c c c} 7 & - 3 & - 3 \\ - 1 & 1 & 0 \\ - 1 & 0 & 1 \end{array} \right]
$$
If we multiply $A$ by $adj A$, we get the identity matrix, which is $|\mathrm{A}|$ I because $|\mathrm{A}| = 1$ [S2].

Finally, we find the inverse using the formula $A^{-1} = \frac{1}{|A|} \text{adj} A$:
$$
\mathrm{A} ^ {- 1} = \frac {1}{1} \left[ \begin{array}{c c c} 7 & - 3 & - 3 \\ - 1 & 1 & 0 \\ - 1 & 0 & 1 \end{array} \right] = \left[ \begin{array}{c c c} 7 & - 3 & - 3 \\ - 1 & 1 & 0 \\ - 1 & 0 & 1 \end{array} \right]
$$
So, the inverse of the matrix is the same as its adjoint in this case because the determinant was 1.

## Key points

*   The adjoint of a square matrix $A$ is the transpose of the matrix of cofactors, denoted as adj A [S2].
*   For a 2 by 2 matrix, the adjoint is found by swapping the diagonal elements and changing the signs of the off-diagonal elements [S2].
*   A matrix is singular if its determinant is zero, and non-singular if its determinant is not zero [S2].
*   The inverse of a matrix $A$, denoted $A^{-1}$, exists if and only if $A$ is non-singular [S2].
*   The formula for the inverse is $A^{-1} = \frac{1}{|A|} \text{adj} A$, which is valid when $|A| \neq 0$ [S2].
*   The fundamental theorem states that $A (\text{adj} A) = (\text{adj} A) A = |A| I$ [S2].
*   The determinant of the adjoint of a matrix $A$ is equal to $|A|^{n-1}$, where $n$ is the order of the matrix [S2].