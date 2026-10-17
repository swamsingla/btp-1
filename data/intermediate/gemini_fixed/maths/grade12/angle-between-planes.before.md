# Angle Between Two Planes

In three-dimensional space, two planes can intersect along a line, or they might be parallel or coincident. When they intersect, they form a dihedral angle. This angle is crucial in fields ranging from architecture to crystallography, as it dictates how surfaces meet in space. In this section, we will learn how to calculate this angle using the fundamental concept of normal vectors.

## Understanding Normal Vectors

Every plane in three-dimensional space has a unique vector that is perpendicular to it. This vector is called the normal vector. If you imagine a plane as a perfectly flat sheet of paper, the normal vector points straight out from the surface, like a flagpole planted on a flat field. The direction of this normal vector completely determines the orientation of the plane. Therefore, if we know the normal vectors of two different planes, we can determine the angle between those two planes simply by finding the angle between their respective normal vectors.

## The Dot Product Formula

The angle between two planes is defined as the angle between their normal vectors. Let $\vec{n}_1$ and $\vec{n}_2$ be the normal vectors of two planes. Let $\theta$ be the acute angle between these two normal vectors. We can calculate $\theta$ using the dot product of the two vectors. The dot product of two vectors $\vec{a}$ and $\vec{b}$, denoted as $\vec{a} \cdot \vec{b}$, is given by the sum of the products of their corresponding components. If $\vec{n}_1 = a_1\hat{i} + b_1\hat{j} + c_1\hat{k}$ and $\vec{n}_2 = a_2\hat{i} + b_2\hat{j} + c_2\hat{k}$, then their dot product is $a_1a_2 + b_1b_2 + c_1c_2$ [S1].

The magnitude of a vector $\vec{n}$ is calculated using the Pythagorean theorem in three dimensions. For $\vec{n} = a\hat{i} + b\hat{j} + c\hat{k}$, the magnitude $|\vec{n}|$ is $\sqrt{a^2 + b^2 + c^2}$. The cosine of the angle $\theta$ between the two normal vectors is the ratio of their dot product to the product of their magnitudes. This gives us the formula:

$$ \cos \theta = \left| \frac {a _ {1} a _ {2} + b _ {1} b _ {2} + c _ {1} c _ {2}}{\sqrt {a _ {1} ^ {2} + b _ {1} ^ {2} + c _ {1} ^ {2}} \sqrt {a _ {2} ^ {2} + b _ {2} ^ {2} + c _ {2} ^ {2}}} \right| \tag{... (1} $$

The absolute value is taken to ensure that we always find the acute angle between the planes [S1].

## From Direction Ratios to Direction Cosines

Sometimes, the plane equations are given in a form where the coefficients of $x$, $y$, and $z$ are direction ratios. These coefficients represent the components of the normal vector. If the normal vector is given in terms of direction cosines $l, m, n$, the formula simplifies because the sum of the squares of the direction cosines is always 1. The formula for the angle between two planes using direction cosines is:

$$ \cos \theta = | l _ {1} l _ {2} + m _ {1} m _ {2} + n _ {1} n _ {2} | $$

This simplified form is very useful when the plane equations are already normalized to unit length [S1].

## Worked Example

Let us consider two planes given by the equations $x + 2y + 2z = 5$ and $2x - y + 2z = 8$. To find the angle between these two planes, we first need to identify the normal vectors of each plane. The coefficients of $x$, $y$, and $z$ in the plane equation give us the components of the normal vector.

For the first plane, $x + 2y + 2z = 5$, the normal vector $\vec{n}_1$ has components $1, 2, 2$ [S1].
For the second plane, $2x - y + 2z = 8$, the normal vector $\vec{n}_2$ has components $2, -1, 2$ [S1].

Now, we apply the dot product formula to find the angle $\theta$ between these two normal vectors.

First, calculate the dot product $\vec{n}_1 \cdot \vec{n}_2$:
$$ \vec{n}_1 \cdot \vec{n}_2 = (1)(2) + (2)(-1) + (2)(2) = 2 - 2 + 4 = 4 $$

Next, calculate the magnitude of $\vec{n}_1$:
$$ |\vec{n}_1| = \sqrt{1^2 + 2^2 + 2^2} = \sqrt{1 + 4 + 4} = \sqrt{9} = 3 $$

Then, calculate the magnitude of $\vec{n}_2$:
$$ |\vec{n}_2| = \sqrt{2^2 + (-1)^2 + 2^2} = \sqrt{4 + 1 + 4} = \sqrt{9} = 3 $$

Now, substitute these values into the formula for $\cos \theta$:
$$ \cos \theta = \left| \frac {4}{3 \times 3} \right| = \frac {4}{9} $$

Therefore, the angle between the two planes is $\cos^{-1}\left(\frac{4}{9}\right)$ [S1].

## Key points

* The angle between two planes is equal to the angle between their normal vectors.
* The formula for the angle $\theta$ between two planes with normal vectors $\vec{n}_1 = (a_1, b_1, c_1)$ and $\vec{n}_2 = (a_2, b_2, c_2)$ is given by $\cos \theta = \left| \frac {a _ {1} a _ {2} + b _ {1} b _ {2} + c _ {1} c _ {2}}{\sqrt {a _ {1} ^ {2} + b _ {1} ^ {2} + c _ {1} ^ {2}} \sqrt {a _ {2} ^ {2} + b _ {2} ^ {2} + c _ {2} ^ {2}}} \right| [S1].$
* If the plane equations are given in the form $lx + my + nz = p$, where $l, m, n$ are direction cosines, the formula simplifies to $\cos \theta = | l _ {1} l _ {2} + m _ {1} m _ {2} + n _ {1} n _ {2} |$ [S1].
* The absolute value is taken to ensure that the angle $\theta$ is always the acute angle between the planes [S1].
* If the dot product of the normal vectors is zero, the planes are perpendicular to each other [S1].

<!-- TERMS: normal vector, direction ratios, direction cosines, dot product, magnitude, acute angle, dihedral angle -->