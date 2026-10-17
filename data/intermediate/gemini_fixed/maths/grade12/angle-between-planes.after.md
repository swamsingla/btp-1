# Angle Between Two Lines

In three-dimensional geometry, we use vector algebra to make the study of geometry simple and elegant [S2]. In this section, we shall study the angle between two lines [S2].

## Understanding Direction Ratios

Let $L_{1}$ and $L_{2}$ be two lines passing through the origin and with direction ratios $a_{1}, b_{1}, c_{1}$ and $a_{2}, b_{2}, c_{2}$, respectively [S1]. Let P be a point on $L_{1}$ and Q be a point on $L_{2}$ [S1]. If we consider the directed lines OP and OQ, the acute angle between them is $\theta$ [S1]. The directed line segments OP and OQ are vectors with components $a_{1}, b_{1}, c_{1}$ and $a_{2}, b_{2}, c_{2}$, respectively [S1].

In case the lines $L_{1}$ and $L_{2}$ do not pass through the origin, we may take lines $L_{1}^{\prime}$ and $L_{2}^{\prime}$ which are parallel to $L_{1}$ and $L_{2}$ respectively and pass through the origin [S1].

## The Dot Product Formula

The angle $\theta$ between the two lines is given by [S1]:

$$ \cos \theta = \left| \frac {a _ {1} a _ {2} + b _ {1} b _ {2} + c _ {1} c _ {2}}{\sqrt {a _ {1} ^ {2} + b _ {1} ^ {2} + c _ {1} ^ {2}} \sqrt {a _ {2} ^ {2} + b _ {2} ^ {2} + c _ {2} ^ {2}}} \right| $$

The angle between the lines in terms of $\sin \theta$ is given by [S1]:

$$ \sin \theta = \frac {\sqrt {(a _ {1} b _ {2} - a _ {2} b _ {1}) ^ {2} + (b _ {1} c _ {2} - b _ {2} c _ {1}) ^ {2} + (c _ {1} a _ {2} - c _ {2} a _ {1}) ^ {2}}}{\sqrt {a _ {1} ^ {2} + b _ {1} ^ {2} + c _ {1} ^ {2}} \sqrt {a _ {2} ^ {2} + b _ {2} ^ {2} + c _ {2} ^ {2}}} $$

If $\theta$ is the acute angle between the lines given by the vector equations $\vec {r} = \overline {{a}} _ {1} + \lambda \vec {b} _ {1}$ and $\vec {r} = \vec {a} _ {2} + \mu \vec {b} _ {2}$, then [S1]:

$$ \cos \theta = \left| \frac {\vec {b} _ {1} \cdot \vec {b} _ {2}}{\left| \vec {b} _ {1} \right| \left| \vec {b} _ {2} \right|} \right| $$

In Cartesian form, if $\theta$ is the angle between the lines [S1]:

$$ \frac {x - x _ {1}}{a _ {1}} = \frac {y - y _ {1}}{b _ {1}} = \frac {z - z _ {1}}{c _ {1}} $$

and

$$ \frac {x - x _ {2}}{a _ {2}} = \frac {y - y _ {2}}{b _ {2}} = \frac {z - z _ {2}}{c _ {2}} $$

where $a_1, b_1, c_1$ and $a_2, b_2, c_2$ are the direction ratios of the lines, respectively, then [S1]:

$$ \cos \theta = \left| \frac {a _ {1} a _ {2} + b _ {1} b _ {2} + c _ {1} c _ {2}}{\sqrt {a _ {1} ^ {2} + b _ {1} ^ {2} + c _ {1} ^ {2}} \sqrt {a _ {2} ^ {2} + b _ {2} ^ {2} + c _ {2} ^ {2}}} \right| $$

## From Direction Ratios to Direction Cosines

If instead of direction ratios for the lines $L_1$ and $L_2$, direction cosines, namely, $l_{1}, m_{1}, n_{1}$ for $L_1$ and $l_{2}, m_{2}, n_{2}$ for $L_2$ are given, then the formulas take the following form [S1]:

$$ \cos \theta = | l _ {1} l _ {2} + m _ {1} m _ {2} + n _ {1} n _ {2} | $$

since $l _ {1} ^ {2} + m _ {1} ^ {2} + n _ {1} ^ {2} = 1 = l _ {2} ^ {2} + m _ {2} ^ {2} + n _ {2} ^ {2}$ [S1], and

$$ \sin \theta = \sqrt {\left(l _ {1} m _ {2} - l _ {2} m _ {1}\right) ^ {2} - (m _ {1} n _ {2} - m _ {2} n _ {1}) ^ {2} + (n _ {1} l _ {2} - n _ {2} l _ {1}) ^ {2}} $$

## Worked Example

Find the angle between the pair of lines given by [S1]:

$$ \vec {r} = 3 \hat {i} + 2 \hat {j} - 4 \hat {k} + \lambda (3 \hat {i} + 5 \hat {j} + 4 \hat {k}) $$

and

$$ \frac {x + 1}{1} = \frac {y - 4}{1} = \frac {z - 5}{2} $$

**Solution:**
The direction ratios of the first line are 3, 5, 4 and the direction ratios of the second line are 1, 1, 2 [S1]. If $\theta$ is the angle between them, then [S1]:

$$ \cos \theta = \left| \frac {3 \cdot 1 + 5 \cdot 1 + 4 \cdot 2}{\sqrt {3 ^ {2} + 5 ^ {2} + 4 ^ {2}} \sqrt {1 ^ {2} + 1 ^ {2} + 2 ^ {2}}} \right| = \frac {1 6}{\sqrt {5 0} \sqrt {6}} = \frac {1 6}{5 \sqrt {2} \sqrt {6}} = \frac {8 \sqrt {3}}{1 5} $$

Hence, the required angle is $\cos^{-1}\left(\frac{8\sqrt{3}}{15}\right)$ [S1].

## Key points

* The angle $\theta$ between two lines with direction ratios $a_1, b_1, c_1$ and $a_2, b_2, c_2$ is given by $\cos \theta = \left| \frac {a _ {1} a _ {2} + b _ {1} b _ {2} + c _ {1} c _ {2}}{\sqrt {a _ {1} ^ {2} + b _ {1} ^ {2} + c _ {1} ^ {2}} \sqrt {a _ {2} ^ {2} + b _ {2} ^ {2} + c _ {2} ^ {2}}} \right|$ [S1].
* If direction cosines $l_1, m_1, n_1$ and $l_2, m_2, n_2$ are given instead of direction ratios, the formula simplifies to $\cos \theta = | l _ {1} l _ {2} + m _ {1} m _ {2} + n _ {1} n _ {2} |$ [S1].
* Two lines with direction ratios $a_1, b_1, c_1$ and $a_2, b_2, c_2$ are perpendicular if $a_1 a_2 + b_1 b_2 + c_1 c_2 = 0$ [S1].
* Two lines with direction ratios $a_1, b_1, c_1$ and $a_2, b_2, c_2$ are parallel if $\frac {a _ {1}}{a _ {2}} = \frac {b _ {1}}{b _ {2}} = \frac {c _ {1}}{c _ {2}}$ [S1].

<!-- TERMS: normal vector, direction ratios, direction cosines, dot product, magnitude, acute angle, dihedral angle -->
