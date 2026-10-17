# Angle Between Two Lines in 3D

In three-dimensional space, lines do not always lie in the same plane, and they can point in infinitely many directions. Finding the angle between two lines in 3D is a fundamental skill in vector geometry. We use direction ratios or direction cosines to describe the orientation of a line, which allows us to calculate the exact angle between them using the dot product.

## Direction Ratios

Direction ratios are three numbers that are proportional to the direction cosines of a line. If a line has direction ratios $a_1, b_1, c_1$ and another line has $a_2, b_2, c_2$, we can treat these as the components of vectors pointing along the lines. To find the acute angle $\theta$ between two lines passing through the origin, we use the dot product formula. The cosine of the angle is given by the absolute value of the sum of the products of the corresponding direction ratios, divided by the product of the magnitudes of the vectors [S1].

$$
\cos \theta = \left| \frac {a _ {1} a _ {2} + b _ {1} b _ { {2} + c _ {1} c _ {2}}{\sqrt {a _ {1} ^ {2} + b _ {1} ^ {2} + c _ {1} ^ {2}} \sqrt {a _ {2} ^ {2} + b _ {2} ^ {2} + c _ {2} ^ {2}}} \right|\tag{... (1}
$$

Similarly, the sine of the angle can be found using the relationship $\sin \theta = \sqrt {1 - \cos^ {2} \theta}$. This can be expanded to give a formula involving the squares of the differences between the direction ratios [S1].

$$
\sin \theta = \frac {\sqrt {(a _ {1} b _ {2} - a _ { {2} b _ {1}) ^ {2} + (b _ {1} c _ {2} - b _ { {2} c _ {1}) ^ {2} + (c _ {1} a _ { {2} - c _ { {2} a _ {1}) ^ {2}}}{\sqrt {a _ {1} ^ {2} + b _ {1} ^ {2} + c _ {1} ^ {2}} \sqrt {a _ {2} ^ {2} + b _ {2} ^ {2} + c _ {2} ^ {2}}}
$$

## Direction Cosines

Direction cosines are the cosines of the angles that a line makes with the positive $x, y$, and $z$-axes. They are denoted by $l, m, n$. Because the sum of the squares of the direction cosines of a line is always 1, the formulas for the angle between two lines become simpler when using direction cosines rather than direction ratios [S1].

If the direction cosines of two lines are $l_1, m_1, n_1$ and $l_2, m_2, n_2$, then the cosine of the angle between them is simply the absolute value of the sum of the products of the corresponding direction cosines [S1].

$$
\cos \theta = | l _ {1} l _ {2} + m _ {1} m _ {2} + n _ {1} n _ {2} |
$$

The sine of the angle in terms of direction cosines is also given by a specific formula [S1].

$$
\sin \theta = \sqrt {\left(l _ {1} m _ {2} - l _ {2} m _ {1}\right) ^ {2} - (m _ {1} n _ {2} - m _ {2} n _ {1}) ^ {2} + (n _ {1} l _ {2} - n _ {2} l _ {1}) ^ {2}}
$$

## Conditions for Parallel and Perpendicular Lines

Using the formula for the cosine of the angle between two lines, we can easily determine if two lines are parallel or perpendicular. If the angle $\theta$ between the lines is $90^{\circ}$, the lines are perpendicular. This occurs when the numerator of the cosine formula is zero, meaning the sum of the products of the direction ratios is zero [S1].

$$
a _ {1} a _ {2} + b _ {1} b _ {2} + c _ {1} c _ {2} = 0
$$

If the angle $\theta$ is $0$, the lines are parallel. This happens when the direction ratios of the two lines are proportional to each other [S1].

$$
\frac {a _ {1}}{a _ {2}} = \frac {b _ {1}}{b _ {2}} = \frac {c _ {1}}{c _ {2}}
$$

## Worked Example

Suppose we have two lines given in vector form:
$$ \vec {r} = 3 \hat {i} + 2 \hat {j} - 4 \hat {k} + \lambda (\hat {i} + 2 \hat {j} + 2 \hat {k}) $$
and
$$ \frac {x + 1}{1} = \frac {y - 4}{1} = \frac {z - 5}{2} $$
The direction ratios of the first line are 1, 2, and 2. The direction ratios of the second line are 1, 1, and 2. To find the angle $\theta$ between them, we substitute these values into the cosine formula [S1].

$$
\cos \theta = \left| \frac {1 \cdot 1 + 2 \cdot 1 + 2 \cdot 2}{\sqrt {1 ^ {2} + 2 ^ {2} + 2 ^ {2}} \sqrt {1 ^ {2} + 1 ^ {2} + 2 ^ {2}}} \right| = \frac {1 + 2 + 4}{\sqrt {9} \sqrt {6}} = \frac {7}{3 \sqrt {6}}
$$
Hence, the required angle is $\cos^{-1}\left(\frac{7}{3 \sqrt {6}}\right)$.

## Key points

*   The angle between two lines in 3D is found using the dot product of their direction vectors, which are defined by their direction ratios or direction cosines [S1].
*   Direction ratios are proportional to the direction cosines and are used in the general formula for the angle between two lines [S1, S2].
*   Direction cosines are the cosines of the angles a line makes with the coordinate axes, and they satisfy the condition $l^2 + m^2 + n^2 = 1$ [S2].
*   Two lines are perpendicular if the sum of the products of their direction ratios is zero [S1].
*   Two lines are parallel if their corresponding direction ratios are proportional [S1].
<!-- TERMS: direction ratios, direction cosines, direction vectors, dot product, acute angle, proportional, vector form -->