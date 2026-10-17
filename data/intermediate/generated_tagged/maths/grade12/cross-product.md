# Cross (Vector) Product

The cross product is a way to multiply two vectors in three-dimensional space. Unlike the dot product, which gives a scalar result, the cross product gives a new vector. This vector is perpendicular to the plane formed by the two original vectors. The cross product is very useful in physics and engineering for calculating torque, angular momentum, and areas of geometric shapes like parallelograms and triangles.

## The Right-Handed Coordinate System

Before we define the cross product, we need to understand the right-handed rectangular coordinate system. In this system, when the positive $x$-axis is rotated counterclockwise into the positive $y$-axis, a right-handed (standard) screw would advance in the direction of the positive $z$-axis [S1].

You can also remember this by using your right hand. Point your thumb in the direction of the positive $z$-axis. Curl your fingers in the direction away from the positive $x$-axis toward the positive $y$-axis [S1].

## Definition of the Vector Product

The vector product of two nonzero vectors $\vec{a}$ and $\vec{b}$ is denoted by $\vec{a} \times \vec{b}$ and is defined as [S1]:

$$
\vec {a} \times \vec {b} = | \vec {a} | | \vec {b} | \sin \theta \hat {n},
$$

where:
*   $\theta$ is the angle between $\vec{a}$ and $\vec{b}$, where $0 \leq \theta \leq \pi$.
*   $\hat{n}$ is a unit vector perpendicular to both $\vec{a}$ and $\vec{b}$.
*   The vectors $\vec{a}$, $\vec{b}$, and $\hat{n}$ must form a right-handed system. This means the system rotated from $\vec{a}$ to $\vec{b}$ moves in the direction of $\hat{n}$ [S1].

If either $\vec{a} = \vec{0}$ or $\vec{b} = \vec{0}$, we define $\vec{a} \times \vec{b} = \vec{0}$ [S1].

## Properties of the Vector Product

The cross product has several important properties and observations [S1].

1.  $\vec{a} \times \vec{b}$ is a vector.
2.  If $\vec{a}$ and $\vec{b}$ are parallel (or collinear), then $\vec{a} \times \vec{b} = \vec{0}$. This happens because $\theta = 0$ or $\pi$, making $\sin \theta = 0$.
3.  If $\theta = \frac{\pi}{2}$, then $\vec{a} \times \vec{b} = |\vec{a}| |\vec{b}|$.
4.  For mutually perpendicular unit vectors $\hat{i}, \hat{j}, \hat{k}$, we have:
    $$ \begin{array}{l} \hat {i} \times \hat {i} = \hat {j} \times \hat {j} = \hat {k} \times \hat {k} = \vec {0} \\ \hat {i} \times \hat {j} = \hat {k}, \quad \hat {j} \times \hat {k} = \hat {i}, \quad \hat {k} \times \hat {i} = \hat {j} \end{array} $$
5.  The angle between two vectors $\vec{a}$ and $\vec{b}$ can be found using:
    $$ \left| \sin \theta = \frac {\left| \vec {a} \times \vec {b} \right|}{\left| \vec {a} \right| \left| \vec {b} \right|} \right| $$
6.  The vector product is not commutative. We always have $\vec{a} \times \vec{b} = -\vec{b} \times \vec{a}$ [S1].
7.  From the non-commutative property, we get:
    $$ \hat {j} \times \hat {i} = - \hat {k}, \quad \hat {k} \times \hat {j} = - \hat {i}, \quad \hat {i} \times \hat {k} = - \hat {j}. $$
8.  If $\vec{a}$ and $\vec{b}$ represent the adjacent sides of a triangle, its area is $\frac {1}{2} | \vec {a} \times \vec {b} |$ [S1].
9.  If $\vec{a}$ and $\vec{b}$ represent the adjacent sides of a parallelogram, its area is $|\vec{a} \times \vec{b} |$ [S1].

## Distributivity and Component Form

The vector product is distributive over addition. If $\vec{a}, \vec{b}, \vec{c}$ are vectors and $\lambda$ is a scalar, then [S1]:
*   $\vec{a} \times (\vec{b} +\vec{c}) = \vec{a} \times \vec{b} +\vec{a} \times \vec{c}$
*   $\lambda (\vec{a}\times \vec{b}) = (\lambda \vec{a})\times \vec{b} = \vec{a}\times (\lambda \vec{b})$

If $\vec{a} = a_1\hat{i} + a_2\hat{j} + a_3\hat{k}$ and $\vec{b} = b_1\hat{i} + b_2\hat{j} + b_3\hat{k}$, then their cross product is [S1]:
$$ \vec {a} \times \vec {b} = \left| \begin{array}{c c c} \hat {i} & \hat {j} & \hat {k} \\ a _ {1} & a _ {2} & a _ {3} \\ b _ {1} & b _ {2} & b _ {3} \end{array} \right| $$

## Worked Example

Let's find the area of a triangle having the points A(1, 1, 1), B(1, 2, 3), and C(2, 3, 1) as its vertices.

First, we find the vectors representing two sides of the triangle:
$\overrightarrow{\mathrm{AB}} = \hat{j} + 2\hat{k}$
$\overrightarrow{\mathrm{AC}} = \hat{i} + 2\hat{j}$

The area of the triangle is $\frac{1}{2} |\overrightarrow{\mathrm{AB}} \times \overrightarrow{\mathrm{AC}}|$.

Now, we calculate the cross product:
$$
\overline {{\mathrm{AB}}} \times \overline {{\mathrm{AC}}} = \left| \begin{array}{c c c} \hat {i} & \hat {j} & \hat {k} \\ 0 & 1 & 2 \\ 1 & 2 & 0 \end{array} \right| = - 4 \hat {i} + 2 \hat {j} - \hat {k}
$$

Next, we find the magnitude of this resulting vector:
$$
\mid \overline {{\mathrm{AB}}} \times \overline {{\mathrm{AC}}} \mid = \sqrt {1 6 + 4 + 1} = \sqrt {2 1}
$$

Finally, we find the area of the triangle:
$$
\text{Area} = \frac{1}{2} \mid \overline {{\mathrm{AB}}} \times \overline {{\mathrm{AC}}} \mid = \frac{1}{2}\sqrt{21}
$$

## Key points

*   The cross product of two vectors $\vec{a}$ and $\vec{b}$ is a vector perpendicular to both, given by $\vec {a} \times \vec {b} = | \vec {a} | | \vec {b} | \sin \theta \hat {n}$.
*   The result depends on the right-handed coordinate system, meaning $\vec{a} \times \vec{b} = -\vec{b} \times \vec{a}$.
*   The area of a triangle formed by two adjacent vectors is half the magnitude of their cross product.
*   The area of a parallelogram formed by two adjacent vectors is the magnitude of their cross product.
*   The cross product can be calculated using the determinant of a 3x3 matrix with $\hat{i}, \hat{j}, \hat{k}$.

<!-- TERMS: cross product, vector product, right-handed coordinate system, unit vector, magnitude, determinant -->