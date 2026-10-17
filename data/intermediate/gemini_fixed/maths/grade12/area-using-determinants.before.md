# Area of Triangle Using Determinants

The area of a triangle can be calculated using the coordinates of its vertices. In earlier classes, we have studied that the area of a triangle whose vertices are $(x_{1}, y_{1})$, $(x_{2}, y_{2})$, and $(x_{3}, y_{3})$, is given by the expression $\frac{1}{2}[x_{1}(y_{2}-y_{3}) + x_{2}(y_{3}-y_{1}) + x_{3}(y_{1}-y_{2})]$ [S1]. This expression can be written in the form of a determinant as $\Delta = \frac {1}{2} \left| \begin{array}{c c c} x _ {1} & y _ {1} & 1 \\ x _ {2} & y _ {2} & 1 \\ x _ {3} & y _ {3} & 1 \end{array} \right|$ [S1]. This method is a powerful tool in coordinate geometry, allowing for a compact and systematic calculation of area.

## The Determinant Formula

A determinant is a special number that can be calculated from a square matrix. For a $2 \times 2$ matrix $\mathrm{A} = \begin{bmatrix} a_{11} & a_{12}\\ a_{21} & a_{22} \end{bmatrix}$, the determinant is defined as $\det (\mathrm{A}) = | \mathrm{A} | = \Delta = \left| \begin{array}{c c} a_{11} & a_{12} \\ a_{21} & a_{22} \end{array} \right| = a_{11} a_{22} - a_{21} a_{12}$ [S3]. To find the area of a triangle, we use a $3 \times 3$ matrix where the first column contains the $x$-coordinates, the second column contains the $y$-coordinates, and the third column contains the constant $1$ for each vertex [S1].

The formula for the area of a triangle is $\Delta = \frac {1}{2} \left| \begin{array}{c c c} x_{1} & y_{1} & 1 \\ x_{2} & y_{2} & 1 \\ x_{3} & y_{3} & 1 \end{array} \right|$ [S1]. The absolute value is taken because area is a positive quantity [S1]. If the area is given, we can use both positive and negative values of the determinant for calculation [S1].

## Calculating the Determinant

To calculate the area, we expand the $3 \times 3$ determinant along the first row. The formula is $\frac {1}{2} [ x_{1} (y_{2} \cdot 1 - 1 \cdot y_{3}) - y_{1} (x_{2} \cdot 1 - 1 \cdot x_{3}) + 1 (x_{2} y_{3} - y_{2} x_{3}) ]$ [S1]. This simplifies to $\frac {1}{2} [ x_{1} (y_{2} - y_{3}) - y_{1} (x_{2} - x_{3}) + (x_{2} y_{3} - x_{3} y_{2}) ]$ [S1].

The area of the triangle formed by three collinear points is zero [S1]. This is because the points lie on a straight line, so they do not form a triangle with a non-zero area.

## Worked example

Find the area of the triangle whose vertices are (3, 8), (-4, 2) and (5, 1).

Solution:
The area of triangle is given by
$$
\Delta = \frac {1}{2} \left| \begin{array}{c c c} 3 & 8 & 1 \\ - 4 & 2 & 1 \\ 5 & 1 & 1 \end{array} \right|
$$

Expanding the determinant along the first row:
$$
\begin{array}{l}
= \frac {1}{2} [ 3 (2 \cdot 1 - 1 \cdot 1) - 8 ((-4) \cdot 1 - 1 \cdot 5) + 1 ((-4) \cdot 1 - 2 \cdot 5) ] \\
= \frac {1}{2} [ 3 (2 - 1) - 8 (-4 - 5) + 1 (-4 - 10) ] \\
= \frac {1}{2} [ 3(1) - 8(-9) + 1(-14) ] \\
= \frac {1}{2} [ 3 + 72 - 14 ] \\
= \frac {1}{2} [ 61 ] \\
= \frac {61}{2}
\end{array}
$$

## Key points
- The area of a triangle with vertices $(x_{1}, y_{1})$, $(x_{2}, y_{2})$, and $(x_{3}, y_{3})$ is given by $\Delta = \frac {1}{2} \left| \begin{array}{c c c} x_{1} & y_{1} & 1 \\ x_{2} & y_{2} & 1 \\ x_{3} & y_{3} & 1 \end{array} \right|$ [S1].
- The absolute value is taken because area is a positive quantity [S1].
- If the area is given, use both positive and negative values of the determinant for calculation [S1].
- The area of the triangle formed by three collinear points is zero [S1].
- The formula can be expanded along any row or column [S3].

<!-- TERMS: determinant, matrix, absolute value, collinear, coordinates -->