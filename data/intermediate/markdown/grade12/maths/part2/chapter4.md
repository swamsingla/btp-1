<!-- page 1 of 39 -->

The image provided is a QR code. As per the instructions, I am to process text and non-textual graphical content that can be extracted from it. Therefore, no textual content should be output for OCR.

Chapter

12080CH10

10

# VECTOR ALGEBRA

In most sciences one generation tears down what another has built and what one has established another undoes. In Mathematics alone each generation builds a new story to the old structure. – HERMAN HANKEL

## 10.1 Introduction

In our day to day life, we come across many queries such as – What is your height? How should a football player hit the ball to give a pass to another player of his team? Observe that a possible answer to the first query may be 1.6 meters, a quantity that involves only one value (magnitude) which is a real number. Such quantities are called scalars. However, an answer to the second query is a quantity (called force) which involves muscular strength (magnitude) and direction (in which another player is positioned). Such quantities are called vectors. In mathematics, physics and engineering, we frequently come across with both types of quantities, namely, scalar quantities such as length, mass, time, distance, speed, area, volume, temperature, work,

![Image block](doc:8590c4e/tier:standard/page:1/block:9)

W.R. Hamilton (1805-1865)

money, voltage, density, resistance etc. and vector quantities like displacement, velocity, acceleration, force, weight, momentum, electric field intensity etc.

In this chapter, we will study some of the basic concepts about vectors, various operations on vectors, and their algebraic and geometric properties. These two type of properties, when considered together give a full realisation to the concept of vectors, and lead to their vital applicability in various areas as mentioned above.

## 10.2 Some Basic Concepts

Let $l$ be any straight line in plane or three dimensional space. This line can be given two directions by means of arrowheads. A line with one of these directions prescribed is called a directed line (Fig 10.1 (i), (ii)).

Reprint 2025-26

<!-- page 2 of 39 -->

VECTOR ALGEBRA

339

![Image block](doc:8590c4e/tier:standard/page:2/block:3)

![Image block](doc:8590c4e/tier:standard/page:2/block:4)

Fig 10.1

![Image block](doc:8590c4e/tier:standard/page:2/block:6)

Now observe that if we restrict the line $l$ to the line segment AB, then a magnitude is prescribed on the line $l$ with one of the two directions, so that we obtain a directed line segment (Fig 10.1(iii)). Thus, a directed line segment has magnitude as well as direction.

Definition 1 A quantity that has magnitude as well as direction is called a vector.

Notice that a directed line segment is a vector (Fig 10.1(iii)), denoted as $\overline{\mathrm{AB}}$ or simply as $\vec{a}$, and read as 'vector $\overline{\mathrm{AB}}'$ or 'vector $\vec{a}$'.

The point A from where the vector AB starts is called its initial point, and the point B where it ends is called its terminal point. The distance between initial and terminal points of a vector is called the magnitude (or length) of the vector, denoted as  $|\overline{AB}|$ , or  $|\vec{a}|$ , or a. The arrow indicates the direction of the vector.

Note Since the length is never negative, the notation $|\vec{a}| < 0$ has no meaning.

## Position Vector

From Class XI, recall the three dimensional right handed rectangular coordinate system (Fig 10.2(i)). Consider a point P in space, having coordinates $(x,y,z)$ with respect to the origin $O(0,0,0)$. Then, the vector $\overline{\mathrm{OP}}$ having O and P as its initial and terminal points, respectively, is called the position vector of the point P with respect to O. Using distance formula (from Class XI), the magnitude of $\overline{\mathrm{OP}}$ (or $\vec{r}$) is given by

$$
\mid \overline {{\mathrm{OP}}} \mid = \sqrt {x ^ {2} + y ^ {2} + z ^ {2}}
$$

In practice, the position vectors of points A, B, C, etc., with respect to the origin O are denoted by $\vec{a}$, $\vec{b}$, $\vec{c}$, etc., respectively (Fig 10.2 (ii)).

Reprint 2025-26

<!-- page 3 of 39 -->

340

MATHEMATICS

![Image block](doc:8590c4e/tier:standard/page:3/block:3)

Fig 10.2

## Direction Cosines

Consider the position vector $\overline{\mathrm{OP}}$ (or $\vec{r}$) of a point $\mathrm{P}(x,y,z)$ as in Fig 10.3. The angles $\alpha$, $\beta$, $\gamma$ made by the vector $\vec{r}$ with the positive directions of $x$, $y$ and $z$-axes respectively, are called its direction angles. The cosine values of these angles, i.e., $\cos \alpha$, $\cos \beta$ and $\cos \gamma$ are called direction cosines of the vector $\vec{r}$, and usually denoted by $l$, $m$ and $n$, respectively. Z

![Image block](doc:8590c4e/tier:standard/page:3/block:7)

From Fig 10.3, one may note that the triangle OAP is right angled, and in it, we have $\cos \alpha = \frac{x}{r}$ ($r$ stands for $|\vec{r}|$). Similarly, from the right angled triangles OBP and OCP, we may write $\cos \beta = \frac{y}{r}$ and $\cos \gamma = \frac{z}{r}$. Thus, the coordinates of the point P may also be expressed as $(lr, mr, nr)$. The numbers $lr, mr$ and $nr$, proportional to the direction cosines are called as direction ratios of vector $\vec{r}$, and denoted as $a, b$ and $c$, respectively.

Reprint 2025-26

<!-- page 4 of 39 -->

VECTOR ALGEBRA

341

Note One may note that $l^2 + m^2 + n^2 = 1$ but $a^2 + b^2 + c^2 \neq 1$, in general.

## 10.3 Types of Vectors

Zero Vector A vector whose initial and terminal points coincide, is called a zero vector (or null vector), and denoted as  $\vec{0}$ . Zero vector can not be assigned a definite direction as it has zero magnitude. Or, alternatively otherwise, it may be regarded as having any direction. The vectors  $\overrightarrow{AA}$ ,  $\overrightarrow{BB}$  represent the zero vector,

Unit Vector A vector whose magnitude is unity (i.e., 1 unit) is called a unit vector. The unit vector in the direction of a given vector $\vec{a}$ is denoted by $\hat{a}$.

Coinitial Vectors Two or more vectors having the same initial point are called coinitial vectors.

Collinear Vectors Two or more vectors are said to be collinear if they are parallel to the same line, irrespective of their magnitudes and directions.

Equal Vectors Two vectors  $\vec{a}$  and  $\vec{b}$  are said to be equal, if they have the same magnitude and direction regardless of the positions of their initial points, and written as  $\vec{a} = \vec{b}$ .

Negative of a Vector A vector whose magnitude is the same as that of a given vector (say,  $\overline{AB}$ ), but direction is opposite to that of it, is called negative of the given vector. For example, vector  $\overline{BA}$  is negative of the vector  $\overline{AB}$ , and written as  $\overline{BA} = -\overline{AB}$ .

Remark The vectors defined above are such that any of them may be subject to its parallel displacement without changing its magnitude and direction. Such vectors are called free vectors. Throughout this chapter, we will be dealing with free vectors only.

Example 1 Represent graphically a displacement of 40 km, 30° west of south.

Solution The vector  $\overline{OP}$  represents the required displacement (Fig 10.4).

Example 2 Classify the following measures as scalars and vectors.

(i) 5 seconds

(ii) $1000\mathrm{cm}^3$

![Image block](doc:8590c4e/tier:standard/page:4/block:17)

Fig 10.4

Reprint 2025-26

<!-- page 5 of 39 -->

![Image block](doc:8590c4e/tier:standard/page:5/block:1)

342 MATHEMATICS

(iii) 10 Newton (iv) $30\mathrm{km / hr}$ (v) $10\mathrm{g / cm}^3$

(vi) $20\mathrm{m / s}$ towards north

## Solution

(i) Time-scalar (ii) Volume-scalar (iii) Force-vector

(iv) Speed-scalar (v) Density-scalar (vi) Velocity-vector

Example 3 In Fig 10.5, which of the vectors are:
(i) Collinear (ii) Equal (iii) Coinitial

## Solution

(i) Collinear vectors: $\vec{a}$, $\vec{c}$ and $\vec{d}$.

(ii) Equal vectors: $\vec{a}$ and $\vec{c}$.

(iii) Coinitial vectors: $\vec{b}$, $\vec{c}$ and $\vec{d}$.

![Image block](doc:8590c4e/tier:standard/page:5/block:13)

## EXERCISE 10.1

1. Represent graphically a displacement of 40 km, 30° east of north.

2. Classify the following measures as scalars and vectors.
(i) 10 kg (ii) 2 meters north-west (iii) 40°
(iv) 40 watt (v) 10⁻¹⁹ coulomb (vi) 20 m/s²

3. Classify the following as scalar and vector quantities.
(i) time period (ii) distance (iii) force
(iv) velocity (v) work done

4. In Fig 10.6 (a square), identify the following vectors.
(i) Coinitial (ii) Equal
(iii) Collinear but not equal

5. Answer the following as true or false.
(i)  $\vec{a}$  and  $-\vec{a}$  are collinear.

(ii) Two collinear vectors are always equal in magnitude.

![Image block](doc:8590c4e/tier:standard/page:5/block:21)

Fig 10.6

(iii) Two vectors having same magnitude are collinear.

(iv) Two collinear vectors having the same magnitude are equal.

Reprint 2025-26

<!-- page 6 of 39 -->

VECTOR ALGEBRA

343

## 10.4 Addition of Vectors

A vector  $\overline{AB}$  simply means the displacement from a point A to the point B. Now consider a situation that a girl moves from A to B and then from B to C (Fig 10.7). The net displacement made by the girl from point A to the point C, is given by the vector  $\overline{AC}$  and expressed as

![Image block](doc:8590c4e/tier:standard/page:6/block:5)

$$
\overrightarrow {\mathrm{AC}} = \overrightarrow {\mathrm{AB}} + \overrightarrow {\mathrm{BC}}
$$

This is known as the triangle law of vector addition.

In general, if we have two vectors $\vec{a}$ and $\vec{b}$ (Fig 10.8 (i)), then to add them, they are positioned so that the initial point of one coincides with the terminal point of the other (Fig 10.8(ii)).

![Image block](doc:8590c4e/tier:standard/page:6/block:9)

Fig 10.8

For example, in Fig 10.8 (ii), we have shifted vector $\vec{b}$ without changing its magnitude and direction, so that it's initial point coincides with the terminal point of $\vec{a}$. Then, the vector $\vec{a} + \vec{b}$, represented by the third side AC of the triangle ABC, gives us the sum (or resultant) of the vectors $\vec{a}$ and $\vec{b}$ i.e., in triangle ABC (Fig 10.8 (ii)), we have

$$
\overrightarrow {\mathrm{AB}} + \overrightarrow {\mathrm{BC}} = \overrightarrow {\mathrm{AC}}
$$

Now again, since $\overline{\mathrm{AC}} = -\overline{\mathrm{CA}}$, from the above equation, we have

$$
\overline {{\mathrm{AB}}} + \overline {{\mathrm{BC}}} + \overline {{\mathrm{CA}}} = \overline {{\mathrm{AA}}} = \vec {0}
$$

This means that when the sides of a triangle are taken in order, it leads to zero resultant as the initial and terminal points get coincided (Fig 10.8(iii)).

Reprint 2025-26

<!-- page 7 of 39 -->

344

MATHEMATICS

Now, construct a vector $\overrightarrow{\mathrm{BC}'}$ so that its magnitude is same as the vector $\overrightarrow{\mathrm{BC}}$, but the direction opposite to that of it (Fig 10.8 (iii)), i.e.,

$$
\overrightarrow {\mathrm{BC} ^ {\prime}} = - \overrightarrow {\mathrm{BC}}
$$

Then, on applying triangle law from the Fig 10.8 (iii), we have

$$
\overline {{\mathrm{AC} ^ {\prime}}} = \overline {{\mathrm{AB}}} + \overline {{\mathrm{BC} ^ {\prime}}} = \overline {{\mathrm{AB}}} + (- \overline {{\mathrm{BC}}}) = \vec {a} - \vec {b}
$$

The vector $\overline{\mathrm{AC}}$ is said to represent the difference of $\vec{a}$ and $\vec{b}$.

Now, consider a boat in a river going from one bank of the river to the other in a direction perpendicular to the flow of the river. Then, it is acted upon by two velocity vectors—one is the velocity imparted to the boat by its engine and other one is the velocity of the flow of river water. Under the simultaneous influence of these two velocities, the boat in actual starts travelling with a different velocity. To have a precise

idea about the effective speed and direction (i.e., the resultant velocity) of the boat, we have the following law of vector addition.

If we have two vectors  $\vec{a}$  and  $\vec{b}$  represented by the two adjacent sides of a parallelogram in magnitude and direction (Fig 10.9), then their sum  $\vec{a} + \vec{b}$  is represented in magnitude and direction by the diagonal of the parallelogram through their common point. This is known as the parallelogram law of vector addition.

![Image block](doc:8590c4e/tier:standard/page:7/block:11)

Note From Fig 10.9, using the triangle law, one may note that

$$
\overrightarrow {\mathrm{OA}} + \overrightarrow {\mathrm{AC}} = \overrightarrow {\mathrm{OC}}
$$

or

$$
\overrightarrow {\mathrm{OA}} + \overrightarrow {\mathrm{OB}} = \overrightarrow {\mathrm{OC}}
$$

$$
(\text {since} \overline {{\mathrm{AC}}} = \overline {{\mathrm{OB}}})
$$

which is parallelogram law. Thus, we may say that the two laws of vector addition are equivalent to each other.

## Properties of vector addition

Property 1 For any two vectors $\vec{a}$ and $\vec{b}$,

$$
\vec {a} + \vec {b} = \vec {b} + \vec {a}
$$

(Commutative property)

Reprint 2025-26

<!-- page 8 of 39 -->

VECTOR ALGEBRA

345

Proof Consider the parallelogram ABCD (Fig 10.10). Let $\overline{\mathrm{AB}} = \vec{a}$ and $\overline{\mathrm{BC}} = \vec{b}$, then using the triangle law, from triangle ABC, we have

$$
\overrightarrow {\mathrm{AC}} = \vec {a} + \vec {b}
$$

Now, since the opposite sides of a parallelogram are equal and parallel, from Fig 10.10, we have, $\overrightarrow{\mathrm{AD}} = \overrightarrow{\mathrm{BC}} = \vec{b}$ and $\overrightarrow{\mathrm{DC}} = \overrightarrow{\mathrm{AB}} = \vec{a}$. Again using triangle law, from triangle ADC, we have

![Image block](doc:8590c4e/tier:standard/page:8/block:6)

$$
\overline {{\mathrm{AC}}} = \overline {{\mathrm{AD}}} + \overline {{\mathrm{DC}}} = \vec {b} + \vec {a}
$$

Hence

$$
\vec {a} + \vec {b} = \vec {b} + \vec {a}
$$

Property 2 For any three vectors $a, b$ and $c$

$$
(\vec {a} + \vec {b}) + \vec {c} = \vec {a} + (\vec {b} + \vec {c})
$$

(Associative property)

Proof Let the vectors $\vec{a},\vec{b}$ and $\vec{c}$ be represented by $\overline{\mathrm{PQ}}$, $\overline{\mathrm{QR}}$ and $\overline{\mathrm{RS}}$, respectively, as shown in Fig 10.11(i) and (ii).

![Image block](doc:8590c4e/tier:standard/page:8/block:14)

(i)

![Image block](doc:8590c4e/tier:standard/page:8/block:16)

(ii)

Fig 10.11

Then
and
So

$$
\vec {a} + \vec {b} = \overline {{\mathrm{PQ}}} + \overline {{\mathrm{QR}}} = \overline {{\mathrm{PR}}}
$$

$$
\vec {b} + \vec {c} = \overrightarrow {\mathrm{QR}} + \overrightarrow {\mathrm{RS}} = \overrightarrow {\mathrm{QS}}
$$

$$
(\vec {a} + \vec {b}) + \vec {c} = \overline {{\mathrm{PR}}} + \overline {{\mathrm{RS}}} = \overline {{\mathrm{PS}}}.
$$

Reprint 2025-26

<!-- page 9 of 39 -->

346

MATHEMATICS

and

$$
\vec {a} + (\vec {b} + \vec {c}) = \overline {{\mathrm{PQ}}} + \overline {{\mathrm{QS}}} = \overline {{\mathrm{PS}}}
$$

Hence

$$
(\vec {a} + \vec {b}) + \vec {c} = \vec {a} + (\vec {b} + \vec {c})
$$

Remark The associative property of vector addition enables us to write the sum of three vectors  $\vec{a}, \vec{b}, \vec{c}$  as  $\vec{a} + \vec{b} + \vec{c}$  without using brackets.

Note that for any vector $a$, we have

$$
\vec {a} + \vec {0} = \vec {0} + \vec {a} = \vec {a}
$$

Here, the zero vector $\bar{0}$ is called the additive identity for the vector addition.

## 10.5 Multiplication of a Vector by a Scalar

Let $\vec{a}$ be a given vector and $\lambda$ a scalar. Then the product of the vector $\vec{a}$ by the scalar $\lambda$, denoted as $\lambda\vec{a}$, is called the multiplication of vector $\vec{a}$ by the scalar $\lambda$. Note that, $\lambda\vec{a}$ is also a vector, collinear to the vector $\vec{a}$. The vector $\lambda\vec{a}$ has the direction same (or opposite) to that of vector $\vec{a}$ according as the value of $\lambda$ is positive (or negative). Also, the magnitude of vector $\lambda\vec{a}$ is $|\lambda|$ times the magnitude of the vector $\vec{a}$, i.e.,

$$
| \lambda \vec {a} | = | \lambda | | \vec {a} |
$$

A geometric visualisation of multiplication of a vector by a scalar is given in Fig 10.12.

![Image block](doc:8590c4e/tier:standard/page:9/block:15)

![Image block](doc:8590c4e/tier:standard/page:9/block:16)

![Image block](doc:8590c4e/tier:standard/page:9/block:17)

Fig 10.12

![Image block](doc:8590c4e/tier:standard/page:9/block:19)

When $\lambda = -1$, then $\lambda \vec{a} = -\vec{a}$, which is a vector having magnitude equal to the magnitude of $\vec{a}$ and direction opposite to that of the direction of $\vec{a}$. The vector $-\vec{a}$ is called the negative (or additive inverse) of vector $\vec{a}$ and we always have

$$
\vec {a} + (- \vec {a}) = (- \vec {a}) + \vec {a} = \vec {0}
$$

Also, if $\lambda = \frac{1}{|a|}$, provided $\vec{a} \neq 0$ i.e. $\vec{a}$ is not a null vector, then

$$
\left| \lambda \vec {a} \right| = \left| \lambda \right| \left| \vec {a} \right| = \frac {1}{\left| \vec {a} \right|} \left| \vec {a} \right| = 1
$$

Reprint 2025-26

<!-- page 10 of 39 -->

VECTOR ALGEBRA

347

So, $\lambda \bar{a}$ represents the unit vector in the direction of $\bar{a}$. We write it as

$$
\hat {a} = \frac {1}{| \vec {a} |} \vec {a}
$$

Note For any scalar $k$, $k\vec{0} = \vec{0}$.

## 10.5.1 Components of a vector

Let us take the points A(1, 0, 0), B(0, 1, 0) and C(0, 0, 1) on the x-axis, y-axis and z-axis, respectively. Then, clearly Z

$$
\mid \overline {{\mathrm{OA}}} \mid = 1, \mid \overline {{\mathrm{OB}}} \mid = 1 \text {and} \mid \overline {{\mathrm{OC}}} \mid = 1
$$

The vectors $\overrightarrow{\mathrm{OA}}$, $\overrightarrow{\mathrm{OB}}$ and $\overrightarrow{\mathrm{OC}}$, each having magnitude 1, are called unit vectors along the axes OX, OY and OZ, respectively, and denoted by $\hat{i}, \hat{j}$ and $\hat{k}$, respectively (Fig 10.13).

![Image block](doc:8590c4e/tier:standard/page:10/block:10)

Fig 10.13

Now, consider the position vector $\overline{\mathrm{OP}}$ of a point $\mathrm{P}(x,y,z)$

as in Fig 10.14. Let $\mathrm{P}_1$ be the foot of the perpendicular from $\mathrm{P}$ on the plane XOY.

![Image block](doc:8590c4e/tier:standard/page:10/block:14)

We, thus, see that  $P_{1}P$  is parallel to z-axis. As  $\hat{i}, \hat{j}$  and  $\hat{k}$  are the unit vectors along the x, y and z-axes, respectively, and by the definition of the coordinates of P, we have  $\overrightarrow{P_{1}P} = \overrightarrow{OR} = z\hat{k}$ . Similarly,  $\overrightarrow{QP_{1}} = \overrightarrow{OS} = y\hat{j}$  and  $\overrightarrow{OQ} = x\hat{i}$ .

Reprint 2025-26

<!-- page 11 of 39 -->

348

MATHEMATICS

Therefore, it follows that

$$
\overrightarrow {\mathrm{OP} _ {1}} = \overrightarrow {\mathrm{OQ}} + \overrightarrow {\mathrm{QP} _ {1}} = x \hat {i} + y \hat {j}
$$

and

$$
\overline {{\mathrm{OP}}} = \overline {{\mathrm{OP} _ {1}}} + \overline {{\mathrm{P} _ {1} \mathrm{P}}} = x \hat {i} + y \hat {j} + z \hat {k}
$$

Hence, the position vector of $\mathrm{P}$ with reference to $\mathrm{O}$ is given by

$$
\overline {{\mathrm{OP}}} (\text {or} \vec {r}) = x \hat {i} + y \hat {j} + z \hat {k}
$$

This form of any vector is called its component form. Here, $x$, $y$ and $z$ are called as the scalar components of $\vec{r}$, and $x\hat{i}$, $y\hat{j}$ and $z\hat{k}$ are called the vector components of $\vec{r}$ along the respective axes. Sometimes $x$, $y$ and $z$ are also termed as rectangular components.

The length of any vector $\vec{r} = x\hat{i} + y\hat{j} + z\hat{k}$, is readily determined by applying the Pythagoras theorem twice. We note that in the right angle triangle OQP$_1$ (Fig 10.14)

$$
\left| \overrightarrow {\mathrm{OP} _ {1}} \right| = \sqrt {\left| \overrightarrow {\mathrm{OQ}} \right| ^ {2} + \left| \overrightarrow {\mathrm{QP} _ {1}} \right| ^ {2}} = \sqrt {x ^ {2} + y ^ {2}},
$$

and in the right angle triangle $\mathrm{OP}_1\mathrm{P}$, we have

$$
\overline {{\mathrm{OP}}} = \sqrt {\left| \overrightarrow {\mathrm{OP} _ {1}} \right| ^ {2} + \left| \overrightarrow {\mathrm{P} _ {1} \mathrm{P}} \right| ^ {2}} = \sqrt {(x ^ {2} + y ^ {2}) + z ^ {2}}
$$

Hence, the length of any vector $\vec{r} = x\hat{i} + y\hat{j} + z\hat{k}$ is given by

$$
| \vec {r} | = \left| x \hat {i} + y \hat {j} + z \hat {k} \right| = \sqrt {x ^ {2} + y ^ {2} + z ^ {2}}
$$

If  $\bar{a}$  and  $\bar{b}$  are any two vectors given in the component form  $a_{1}\hat{i} + a_{2}\hat{j} + a_{3}\hat{k}$  and  $b_{1}\hat{i} + b_{2}\hat{j} + b_{3}\hat{k}$ , respectively, then

(i) the sum (or resultant) of the vectors $\vec{a}$ and $\vec{b}$ is given by

$$
\vec {a} + \vec {b} = (a _ {1} + b _ {1}) \hat {i} + (a _ {2} + b _ {2}) \hat {j} + (a _ {3} + b _ {3}) \hat {k}
$$

(ii) the difference of the vector $\vec{a}$ and $\vec{b}$ is given by

$$
\vec {a} - \vec {b} = (a _ {1} - b _ {1}) \hat {i} + (a _ {2} - b _ {2}) \hat {j} + (a _ {3} - b _ {3}) \hat {k}
$$

(iii) the vectors $\bar{a}$ and $\bar{b}$ are equal if and only if

$$
\left| \begin{array}{l} a _ {1} = b _ {1}, a _ {2} = b _ {2} \quad \text {and} \quad a _ {3} = b _ {3} \end{array} \right.
$$

(iv) the multiplication of vector $\vec{a}$ by any scalar $\lambda$ is given by

$$
\lambda \vec {a} = (\lambda a _ {1}) \hat {i} + (\lambda a _ {2}) \hat {j} + (\lambda a _ {3}) \hat {k}
$$

Reprint 2025-26

<!-- page 12 of 39 -->

VECTOR ALGEBRA

349

The addition of vectors and the multiplication of a vector by a scalar together give the following distributive laws:

Let $\vec{a}$ and $\vec{b}$ be any two vectors, and $k$ and $m$ be any scalars. Then

(i) $k\vec{a} +m\vec{a} = (k + m)\vec{a}$

(ii) $k(m\vec{a}) = (km)\vec{a}$

(iii) $k(\vec{a} +\vec{b}) = k\vec{a} +k\vec{b}$

## Remarks

(i) One may observe that whatever be the value of $\lambda$, the vector $\lambda \vec{a}$ is always collinear to the vector $\vec{a}$. In fact, two vectors $\vec{a}$ and $\vec{b}$ are collinear if and only if there exists a nonzero scalar $\lambda$ such that $\vec{b} = \lambda \vec{a}$. If the vectors $\vec{a}$ and $\vec{b}$ are given in the component form, i.e. $\vec{a} = a_1\hat{i} + a_2\hat{j} + a_3\hat{k}$ and $\vec{b} = b_1\hat{i} + b_2\hat{j} + b_3\hat{k}$, then the two vectors are collinear if and only if

$$
\begin{array}{l} b _ {1} \hat {i} + b _ {2} \hat {j} + b _ {3} \hat {k} = \lambda (a _ {1} \hat {i} + a _ {2} \hat {j} + a _ {3} \hat {k}) \\ \Leftrightarrow \quad b _ {1} \hat {i} + b _ {2} \hat {j} + b _ {3} \hat {k} = (\lambda a _ {1}) \hat {i} + (\lambda a _ {2}) \hat {j} + (\lambda a _ {3}) \hat {k} \\ \Leftrightarrow \quad b _ {1} = \lambda a _ {1},   b _ {2} = \lambda a _ {2},   b _ {3} = \lambda a _ {3} \\ \Leftrightarrow \quad \frac {b _ {1}}{a _ {1}} = \frac {b _ {2}}{a _ {2}} = \frac {b _ {3}}{a _ {3}} = \lambda \end{array}
$$

(ii) If $\vec{a} = a_1\hat{i} + a_2\hat{j} + a_3\hat{k}$, then $a_1, a_2, a_3$ are also called direction ratios of $\vec{a}$.

(iii) In case if it is given that $l, m, n$ are direction cosines of a vector, then $\hat{l} + m\hat{j} + n\hat{k} = (\cos \alpha)\hat{i} + (\cos \beta)\hat{j} + (\cos \gamma)\hat{k}$ is the unit vector in the direction of that vector, where $\alpha, \beta$ and $\gamma$ are the angles which the vector makes with $x, y$ and $z$ axes respectively.

Example 4 Find the values of $x, y$ and $z$ so that the vectors $\vec{a} = x\hat{i} + 2\hat{j} + z\hat{k}$ and $\vec{b} = 2\hat{i} + y\hat{j} + \hat{k}$ are equal.

Solution Note that two vectors are equal if and only if their corresponding components are equal. Thus, the given vectors  $\vec{a}$  and  $\vec{b}$  will be equal if and only if

$$
x = 2, y = 2, z = 1
$$

Reprint 2025-26

<!-- page 13 of 39 -->

350

MATHEMATICS

Example 5 Let $\vec{a} = \hat{i} + 2\hat{j}$ and $\vec{b} = 2\hat{i} + \hat{j}$. Is $|\vec{a}| = |\vec{b}|$? Are the vectors $\vec{a}$ and $\vec{b}$ equal?

Solution We have $|\vec{a}| = \sqrt{1^2 + 2^2} = \sqrt{5}$ and $|\vec{b}| = \sqrt{2^2 + 1^2} = \sqrt{5}$

So, $|\vec{a}| = |\vec{b}|$. But, the two vectors are not equal since their corresponding components are distinct.

Example 6 Find unit vector in the direction of vector $\vec{a} = 2\hat{i} +3\hat{j} +\hat{k}$

Solution The unit vector in the direction of a vector $\vec{a}$ is given by $\hat{a} = \frac{1}{|\vec{a}|}\vec{a}$.

Now

$$
| \vec {a} | = \sqrt {2 ^ {2} + 3 ^ {2} + 1 ^ {2}} = \sqrt {1 4}
$$

Therefore

$$
\hat {a} = \frac {1}{\sqrt {1 4}} (2 \hat {i} + 3 \hat {j} + \hat {k}) = \frac {2}{\sqrt {1 4}} \hat {i} + \frac {3}{\sqrt {1 4}} \hat {j} + \frac {1}{\sqrt {1 4}} \hat {k}
$$

Example 7 Find a vector in the direction of vector $\vec{a} = \hat{i} - 2\hat{j}$ that has magnitude 7 units.

Solution The unit vector in the direction of the given vector $\vec{a}$ is

$$
\hat {a} = \frac {1}{| \vec {a} |} \vec {a} = \frac {1}{\sqrt {5}} (\hat {i} - 2 \hat {j}) = \frac {1}{\sqrt {5}} \hat {i} - \frac {2}{\sqrt {5}} \hat {j}
$$

Therefore, the vector having magnitude equal to 7 and in the direction of $\vec{a}$ is

$$
7 \hat {a} = 7 \left(\frac {1}{\sqrt {5}} \hat {i} - \frac {2}{\sqrt {5}} \hat {j}\right) = \frac {7}{\sqrt {5}} \hat {i} - \frac {1 4}{\sqrt {5}} \hat {j}
$$

Example 8 Find the unit vector in the direction of the sum of the vectors, $\vec{a} = 2\hat{i} + 2\hat{j} - 5\hat{k}$ and $\vec{b} = 2\hat{i} + \hat{j} + 3\hat{k}$.

Solution The sum of the given vectors is

$$
\vec {a} + \vec {b} (= \vec {c}, \text {say}) = 4 \hat {i} + 3 \hat {j} - 2 \hat {k}
$$

and

$$
\left| \vec {c} \right| = \sqrt {4 ^ {2} + 3 ^ {2} + (- 2) ^ {2}} = \sqrt {2 9}
$$

Reprint 2025-26

<!-- page 14 of 39 -->

VECTOR ALGEBRA

351

Thus, the required unit vector is

$$
\hat {c} = \frac {1}{| \vec {c} |} \vec {c} = \frac {1}{\sqrt {2 9}} (4 \hat {i} + 3 \hat {j} - 2 \hat {k}) = \frac {4}{\sqrt {2 9}} \hat {i} + \frac {3}{\sqrt {2 9}} \hat {j} - \frac {2}{\sqrt {2 9}} \hat {k}
$$

Example 9 Write the direction ratio's of the vector $\vec{a} = \hat{i} +\hat{j} -2\hat{k}$ and hence calculate its direction cosines.

Solution Note that the direction ratio's $a, b, c$ of a vector $\vec{r} = x\hat{i} + y\hat{j} + z\hat{k}$ are just the respective components $x, y$ and $z$ of the vector. So, for the given vector, we have $a = 1$, $b = 1$ and $c = -2$. Further, if $l, m$ and $n$ are the direction cosines of the given vector, then

$$
1 = \frac {a}{| \vec {r} |} = \frac {1}{\sqrt {6}}, \quad m = \frac {b}{| \vec {r} |} = \frac {1}{\sqrt {6}}, \quad n = \frac {c}{| \vec {r} |} = \frac {- 2}{\sqrt {6}} \text {as} | \vec {r} | = \sqrt {6}
$$

Thus, the direction cosines are $\left(\frac{1}{\sqrt{6}}, \frac{1}{\sqrt{6}}, -\frac{2}{\sqrt{6}}\right)$.

## 10.5.2 Vector joining two points

If $\mathrm{P}_1(x_1, y_1, z_1)$ and $\mathrm{P}_2(x_2, y_2, z_2)$ are any two points, then the vector joining $\mathrm{P}_1$ and $\mathrm{P}_2$ is the vector $\overline{\mathrm{P}_1\mathrm{P}_2}$ (Fig 10.15).

Joining the points  $P_{1}$  and  $P_{2}$  with the origin O, and applying triangle law, from the triangle  $OP_{1}P_{2}$ , we have

$$
\overrightarrow {\mathrm{OP} _ {1}} + \overline {{\mathrm{P} _ {1} \mathrm{P} _ {2}}} = \overrightarrow {\mathrm{OP} _ {2}}
$$

![Image block](doc:8590c4e/tier:standard/page:14/block:13)

Using the properties of vector addition, the above equation becomes

Fig 10.15

i.e.

$$
\begin{array}{r l} \overrightarrow {\mathrm{P} _ {1} \mathrm{P} _ {2}} & = \overrightarrow {\mathrm{OP} _ {2}} - \overrightarrow {\mathrm{OP} _ {1}} \\ \overrightarrow {\mathrm{P} _ {1} \mathrm{P} _ {2}} & = (x _ {2} \hat {i} + y _ {2} \hat {j} + z _ {2} \hat {k}) - (x _ {1} \hat {i} + y _ {1} \hat {j} + z _ {1} \hat {k}) \\ & = (x _ {2} - x _ {1}) \hat {i} + (y _ {2} - y _ {1}) \hat {j} + (z _ {2} - z _ {1}) \hat {k} \end{array}
$$

The magnitude of vector $\overline{\mathrm{P}_1\mathrm{P}_2}$ is given by

$$
| \overline {{\mathrm{P} _ {1} \mathrm{P} _ {2}}} | = \sqrt {(x _ {2} - x _ {1}) ^ {2} + (y _ {2} - y _ {1}) ^ {2} + (z _ {2} - z _ {1}) ^ {2}}
$$

Reprint 2025-26

<!-- page 15 of 39 -->

352

MATHEMATICS

Example 10 Find the vector joining the points P(2, 3, 0) and Q(-1, -2, -4) directed from P to Q.

Solution Since the vector is to be directed from P to Q, clearly P is the initial point and Q is the terminal point. So, the required vector joining P and Q is the vector  $\overline{PQ}$ , given by

$$
\overline {{\mathrm{PQ}}} = (- 1 - 2) \hat {i} + (- 2 - 3) \hat {j} + (- 4 - 0) \hat {k}
$$

i.e.

$$
\overline {{\mathrm{PQ}}} = - 3 \hat {i} - 5 \hat {j} - 4 \hat {k}.
$$

## 10.5.3 Section formula

Let $P$ and $Q$ be two points represented by the position vectors $\overline{OP}$ and $\overline{OQ}$, respectively,

with respect to the origin O. Then the line segment

joining the points P and Q may be divided by a third point, say R, in two ways – internally (Fig 10.16) and externally (Fig 10.17). Here, we intend to find the position vector $\overrightarrow{\mathrm{OR}}$ for the point R with respect to the origin O. We take the two cases one by one.

![Image block](doc:8590c4e/tier:standard/page:15/block:12)

Case I When R divides PQ internally (Fig 10.16).

If R divides $\overline{\mathrm{PQ}}$ such that $m\overline{\mathrm{RQ}} = n\overline{\mathrm{PR}}$,

Fig 10.16

where $m$ and $n$ are positive scalars, we say that the point $R$ divides $\overline{PQ}$ internally in the ratio of $m : n$. Now from triangles ORQ and OPR, we have

$$
\overrightarrow {\mathrm{RQ}} = \overrightarrow {\mathrm{OQ}} - \overrightarrow {\mathrm{OR}} = \vec {b} - \vec {r}
$$

and

$$
\overline {{\mathrm{PR}}} = \overline {{\mathrm{OR}}} - \overline {{\mathrm{OP}}} = \vec {r} - \vec {a},
$$

Therefore, we have

or

$$
\left| \begin{array}{c c} m (\vec {b} - \vec {r}) = n (\vec {r} - \vec {a}) & \text {(Why?)} \\ \vec {r} = \frac {m \vec {b} + n \vec {a}}{m + n} \end{array} \right|
$$

(on simplification)

Hence, the position vector of the point R which divides P and Q internally in the ratio of $m : n$ is given by

$$
\overrightarrow {\mathrm{OR}} = \frac {m \vec {b} + n \vec {a}}{m + n}
$$

Reprint 2025-26

<!-- page 16 of 39 -->

VECTOR ALGEBRA

353

Case II When R divides PQ externally (Fig 10.17). We leave it to the reader as an exercise to verify that the position vector of the point R which divides the line segment PQ externally in the ratio

m : n    i.e.  $\frac{PR}{QR} = \frac{m}{n}$  is given by

$$
\overline {{\mathrm{OR}}} = \frac {m \vec {b} - n \vec {a}}{m - n}
$$

![Image block](doc:8590c4e/tier:standard/page:16/block:6)

Fig 10.17

Remark If R is the midpoint of PQ, then m = n. And therefore, from Case I, the midpoint R of  $\overline{PQ}$ , will have its position vector as

$$
\overrightarrow {\mathrm{OR}} = \frac {\vec {a} + \vec {b}}{2}
$$

Example 11 Consider two points P and Q with position vectors $\overline{\mathrm{OP}} = 3\vec{a} -2\vec{b}$ and $\overline{\mathrm{OQ}} = \vec{a} +\vec{b}$. Find the position vector of a point R which divides the line joining P and Q in the ratio 2:1, (i) internally, and (ii) externally.

## Solution

(i) The position vector of the point R dividing the join of P and Q internally in the ratio 2:1 is

$$
\overrightarrow {\mathrm{OR}} = \frac {2 (\vec {a} + \vec {b}) + (3 \vec {a} - 2 \vec {b})}{2 + 1} = \frac {5 \vec {a}}{3}
$$

(ii) The position vector of the point R dividing the join of P and Q externally in the ratio 2:1 is

$$
\overrightarrow {\mathrm{OR}} = \frac {2 (\vec {a} + \vec {b}) - (3 \vec {a} - 2 \vec {b})}{2 - 1} = 4 \vec {b} - \vec {a}
$$

Example 12 Show that the points $\mathrm{A}(2\hat{i} - \hat{j} + \hat{k})$, $\mathrm{B}(\hat{i} - 3\hat{j} - 5\hat{k})$, $\mathrm{C}(3\hat{i} - 4j - 4\hat{k})$ are the vertices of a right angled triangle.

Solution We have

$$
\overline {{\mathrm{AB}}} = (1 - 2) \hat {i} + (- 3 + 1) \hat {j} + (- 5 - 1) \hat {k} = - \hat {i} - 2 \hat {j} - 6 \hat {k}
$$

$$
\overline {{\mathrm{BC}}} = (3 - 1) \hat {i} + (- 4 + 3) \hat {j} + (- 4 + 5) \hat {k} = 2 \hat {i} - \hat {j} + \hat {k}
$$

and

$$
\overrightarrow {\mathrm{CA}} = (2 - 3) \hat {i} + (- 1 + 4) \hat {j} + (1 + 4) \hat {k} = - \hat {i} + 3 \hat {j} + 5 \hat {k}
$$

Reprint 2025-26

<!-- page 17 of 39 -->

354

MATHEMATICS

Further, note that

$$
\left| \overline {{\mathrm{AB}}} \right| ^ {2} = 4 1 = 6 + 3 5 = \left| \overline {{\mathrm{BC}}} \right| ^ {2} + \left| \overrightarrow {\mathrm{CA}} \right| ^ {2}
$$

Hence, the triangle is a right angled triangle.

## EXERCISE 10.2

1. Compute the magnitude of the following vectors:

$$
\vec {a} = \hat {i} + \hat {j} + k; \quad \vec {b} = 2 \hat {i} - 7 \hat {j} - 3 \hat {k}; \quad \vec {c} = \frac {1}{\sqrt {3}} \hat {i} + \frac {1}{\sqrt {3}} \hat {j} - \frac {1}{\sqrt {3}} \hat {k}
$$

2. Write two different vectors having same magnitude.

3. Write two different vectors having same direction.

4. Find the values of $x$ and $y$ so that the vectors $2\hat{i} + 3\hat{j}$ and $x\hat{i} + y\hat{j}$ are equal.

5. Find the scalar and vector components of the vector with initial point (2, 1) and terminal point $(-5, 7)$.

6. Find the sum of the vectors $\vec{a} = \hat{i} - 2\hat{j} + \hat{k}$, $\vec{b} = -2\hat{i} + 4\hat{j} + 5\hat{k}$ and $\vec{c} = \hat{i} - 6\hat{j} - 7\hat{k}$

7. Find the unit vector in the direction of the vector $\vec{a} = \hat{i} +\hat{j} +2\hat{k}$ .

8. Find the unit vector in the direction of vector $\overline{\mathrm{PQ}}$, where P and Q are the points (1, 2, 3) and (4, 5, 6), respectively.

9. For given vectors, $\vec{a} = 2\hat{i} - \hat{j} + 2\hat{k}$ and $\vec{b} = -\hat{i} + \hat{j} - \hat{k}$, find the unit vector in the direction of the vector $\vec{a} + \vec{b}$.

10. Find a vector in the direction of vector $5\hat{i} - \hat{j} + 2\hat{k}$ which has magnitude 8 units.

11. Show that the vectors $2\hat{i} - 3\hat{j} + 4\hat{k}$ and $-4\hat{i} + 6\hat{j} - 8\hat{k}$ are collinear.

12. Find the direction cosines of the vector $\hat{i} + 2\hat{j} + 3\hat{k}$.

13. Find the direction cosines of the vector joining the points A(1, 2, -3) and B(-1, -2, 1), directed from A to B.

14. Show that the vector $\hat{i} +\hat{j} +\hat{k}$ is equally inclined to the axes OX, OY and OZ.

15. Find the position vector of a point R which divides the line joining two points P and Q whose position vectors are  $\hat{i} + 2\hat{j} - \hat{k}$  and  $-\hat{i} + \hat{j} + \hat{k}$  respectively, in the ratio 2 : 1

(i) internally

(ii) externally

Reprint 2025-26

<!-- page 18 of 39 -->

VECTOR ALGEBRA

355

16. Find the position vector of the mid point of the vector joining the points P(2, 3, 4) and Q(4, 1, -2).

17. Show that the points A, B and C with position vectors, $\vec{a} = 3\hat{i} - 4\hat{j} - 4\hat{k}$, $\vec{b} = 2\hat{i} - \hat{j} + \hat{k}$ and $\vec{c} = \hat{i} - 3\hat{j} - 5\hat{k}$, respectively form the vertices of a right angled triangle.

18. In triangle ABC (Fig 10.18), which of the following is not true:

(A) $\overline{\mathrm{AB}} +\overline{\mathrm{BC}} +\overline{\mathrm{CA}} = \overline{0}$

(B) $\overrightarrow{\mathrm{AB}} +\overrightarrow{\mathrm{BC}} -\overrightarrow{\mathrm{AC}} = \vec{0}$

(C) $\overrightarrow{\mathrm{AB}} +\overrightarrow{\mathrm{BC}} -\overrightarrow{\mathrm{AC}} = \vec{0}$

![Image block](doc:8590c4e/tier:standard/page:18/block:9)

(D) $\overrightarrow{\mathrm{AB}} -\overrightarrow{\mathrm{CB}} +\overrightarrow{\mathrm{CA}} = \vec{0}$

Fig 10.18

19. If $\vec{a}$ and $\vec{b}$ are two collinear vectors, then which of the following are incorrect:

(A) $\vec{b} = \lambda \vec{a}$, for some scalar $\lambda$

(B) $\vec{a} = \pm \vec{b}$

(C) the respective components of $\vec{a}$ and $b$ are not proportional

(D) both the vectors $\bar{a}$ and $\bar{b}$ have same direction, but different magnitudes.

## 10.6 Product of Two Vectors

So far we have studied about addition and subtraction of vectors. An other algebraic operation which we intend to discuss regarding vectors is their product. We may recall that product of two numbers is a number, product of two matrices is again a matrix. But in case of functions, we may multiply them in two ways, namely, multiplication of two functions pointwise and composition of two functions. Similarly, multiplication of two vectors is also defined in two ways, namely, scalar (or dot) product where the result is a scalar, and vector (or cross) product where the result is a vector. Based upon these two types of products for vectors, they have found various applications in geometry, mechanics and engineering. In this section, we will discuss these two types of products.

## 10.6.1 Scalar (or dot) product of two vectors

Definition 2 The scalar product of two nonzero vectors $\vec{a}$ and $\vec{b}$, denoted by $\vec{a} \cdot \vec{b}$, is

Reprint 2025-26

<!-- page 19 of 39 -->

356

MATHEMATICS

defined as

$$
\vec {a} \cdot \vec {b} = | \vec {a} | | \vec {b} | \cos \theta ,
$$

![Image block](doc:8590c4e/tier:standard/page:19/block:5)

where, $\theta$ is the angle between $\vec{a}$ and $\vec{b}, 0 \leq \theta \leq \pi$ (Fig 10.19). If either $\vec{a} = 0$ or $\vec{b} = 0$ then $\theta$ is not defined, and in this case, we define $\vec{a} \cdot \vec{b} = 0$

Fig 10.19

## Observations

1. $\vec{a} \cdot \vec{b}$ is a real number.

2. Let $\vec{a}$ and $\vec{b}$ be two nonzero vectors, then $\vec{a} \cdot \vec{b} = 0$ if and only if $\vec{a}$ and $\vec{b}$ are perpendicular to each other. i.e. $\vec{a} \cdot \vec{b} = 0 \Leftrightarrow \vec{a} \perp \vec{b}$

3. If $\theta = 0$, then $\vec{a} \cdot \vec{b} = |\vec{a}| |\vec{b}|$ In particular, $\vec{a} \cdot \vec{a} = |\vec{a}|^2$, as $\theta$ in this case is 0.

4. If $\theta = \pi$, then $\vec{a} \cdot \vec{b} = -|\vec{a}| |\vec{b}|$ In particular, $\vec{a} \cdot \vec{b} = -|\vec{a}| |\vec{b}|$, as $\theta$ in this case is $\pi$.

5. In view of the Observations 2 and 3, for mutually perpendicular unit vectors $\hat{i},\hat{j}$ and $\hat{k}$, we have

$$
\hat {i} \cdot \hat {i} = \hat {j} \cdot \hat {j} = \hat {k} \cdot \hat {k} = 1,
$$

$$
\hat {i} \cdot \hat {j} = \hat {j} \cdot \hat {k} = \hat {k} \cdot \hat {i} = 0
$$

6. The angle between two nonzero vectors $\vec{a}$ and $\vec{b}$ is given by

$$
\left| \cos \theta = \frac {\vec {a} \cdot \vec {b}}{| \vec {a} | | \vec {b} |}, \text {or} \theta = \cos^ {- 1} \left(\frac {\vec {a} . \vec {b}}{| \vec {a} | | \vec {b} |}\right) \right|
$$

7. The scalar product is commutative. i.e.

$$
\vec {a} \cdot \vec {b} = \vec {b} \cdot \vec {a}
$$

(Why?)

## Two important properties of scalar product

Property 1 (Distributivity of scalar product over addition) Let  $\vec{a}$ ,  $\vec{b}$  and  $\vec{c}$  be any three vectors, then

$$
\vec {a} \cdot (\vec {b} + \vec {c}) = \vec {a} \cdot \vec {b} + \vec {a} \cdot \vec {c}
$$

Reprint 2025-26

<!-- page 20 of 39 -->

VECTOR ALGEBRA

357

Property 2 Let $\bar{a}$ and $\bar{b}$ be any two vectors, and $l$ be any scalar. Then

$$
(\lambda \vec {a}) \cdot \vec {b} = (\lambda \vec {a}) \cdot \vec {b} = \lambda (\vec {a} \cdot \vec {b}) = \vec {a} \cdot (\lambda \vec {b})
$$

If two vectors  $\vec{a}$  and  $\vec{b}$  are given in component form as  $a_{1}\hat{i} + a_{2}\hat{j} + a_{3}\hat{k}$  and  $b_{1}\hat{i} + b_{2}\hat{j} + b_{3}\hat{k}$ , then their scalar product is given as

$$
\begin{array}{r l} \vec {a} \cdot \vec {b} = & (a _ {1} \hat {i} + a _ {2} \hat {j} + a _ {3} \hat {k}) \cdot (b _ {1} \hat {i} + b _ {2} \hat {j} + b _ {3} \hat {k}) \\ = & a _ {1} \hat {i} \cdot (b _ {1} \hat {i} + b _ {2} \hat {j} + b _ {3} \hat {k}) + a _ {2} \hat {j} \cdot (b _ {1} \hat {i} + b _ {2} \hat {j} + b _ {3} \hat {k}) + a _ {3} \hat {k} \cdot (b _ {1} \hat {i} + b _ {2} \hat {j} + b _ {3} \hat {k}) \\ = & a _ {1} b _ {1} (\hat {i} \cdot \hat {i}) + a _ {1} b _ {2} (\hat {i} \cdot \hat {j}) + a _ {1} b _ {3} (\hat {i} \cdot \hat {k}) + a _ {2} b _ {1} (\hat {j} \cdot \hat {i}) + a _ {2} b _ {2} (\hat {j} \cdot \hat {j}) + a _ {2} b _ {3} (\hat {j} \cdot \hat {k}) \\ & + a _ {3} b _ {1} (\hat {k} \cdot \hat {i}) + a _ {3} b _ {2} (\hat {k} \cdot \hat {j}) + a _ {3} b _ {3} (\hat {k} \cdot \hat {k}) \text {(Using the above Properties 1 and 2)} \\ = & a _ {1} b _ {1} + a _ {2} b _ {2} + a _ {3} b _ {3} \quad \text {(Using Observation 5)} \end{array}
$$

Thus $\vec{a} \cdot \vec{b} = a_1 b_1 + a_2 b_2 + a_3 b_3$

## 10.6.2 Projection of a vector on a line

Suppose a vector $\overline{\mathrm{AB}}$ makes an angle $\theta$ with a given directed line $l$ (say), in the anticlockwise direction (Fig 10.20). Then the projection of $\overline{\mathrm{AB}}$ on $l$ is a vector $\vec{p}$ (say) with magnitude $|\overline{\mathrm{AB}}| |\cos \theta|$, and the direction of $\vec{p}$ being the same (or opposite) to that of the line $l$, depending upon whether $\cos \theta$ is positive or negative. The vector $\vec{p}$

![Image block](doc:8590c4e/tier:standard/page:20/block:10)

Fig 10.20

Reprint 2025-26

<!-- page 21 of 39 -->

358

MATHEMATICS

is called the projection vector, and its magnitude $|\vec{p}|$ is simply called as the projection of the vector $\overline{\mathrm{AB}}$ on the directed line $l$.

For example, in each of the following figures (Fig 10.20(i) to (iv)), projection vector of $\overrightarrow{\mathrm{AB}}$ along the line $l$ is vector $\overrightarrow{\mathrm{AC}}$.

## Observations

1. If $\hat{p}$ is the unit vector along a line $l$, then the projection of a vector $\vec{a}$ on the line $l$ is given by $\vec{a} \cdot \hat{p}$.

2. Projection of a vector $\vec{a}$ on other vector $\vec{b}$, is given by

$$
\left| \vec {a} \cdot \hat {b}, \quad \text {or} \quad \vec {a} \cdot \left(\frac {\vec {b}}{| \vec {b} |}\right), \text {or} \frac {1}{| \vec {b} |} (\vec {a} \cdot \vec {b}) \right|
$$

3. If  $\theta=0$ , then the projection vector of AB will be AB itself and if  $\theta=\pi$ , then the projection vector of  $\overline{AB}$  will be  $\overline{BA}$ .

4. If $\theta = \frac{\pi}{2}$ or $\theta = \frac{3\pi}{2}$, then the projection vector of $\overline{\mathrm{AB}}$ will be zero vector.

Remark If  $\alpha$ ,  $\beta$  and  $\gamma$  are the direction angles of vector  $\vec{a}=a_{1}\hat{i}+a_{2}\hat{j}+a_{3}\hat{k}$ , then its direction cosines may be given as

$$
\cos \alpha = \frac {\vec {a} \cdot \hat {i}}{| \vec {a} | | \hat {i} |} = \frac {a _ {1}}{| \vec {a} |}, \cos \beta = \frac {a _ {2}}{| \vec {a} |}, \text {and} \cos \gamma = \frac {a _ {3}}{| \vec {a} |}
$$

Also, note that $|\vec{a}| \cos \alpha$, $|\vec{a}| \cos \beta$ and $|\vec{a}| \cos \gamma$ are respectively the projections of $\vec{a}$ along OX, OY and OZ. i.e., the scalar components $a_1, a_2$ and $a_3$ of the vector $\vec{a}$, are precisely the projections of $\vec{a}$ along $x$-axis, $y$-axis and $z$-axis, respectively. Further, if $\vec{a}$ is a unit vector, then it may be expressed in terms of its direction cosines as

$$
\vec {a} = \cos \alpha \hat {i} + \cos \beta \hat {j} + \cos \gamma \hat {k}
$$

Example 13 Find the angle between two vectors $\vec{a}$ and $\vec{b}$ with magnitudes 1 and 2 respectively and when $\vec{a} \cdot \vec{b} = 1$.

Solution Given $\vec{a} \cdot \vec{b} = 1, |\vec{a}| = 1$ and $|\vec{b}| = 2$. We have

$$
\theta = \cos^ {- 1} \left(\frac {\vec {a} \cdot \vec {b}}{| \vec {a} | | \vec {b} |}\right) = \cos^ {- 1} \left(\frac {1}{2}\right) = \frac {\pi}{3}
$$

Reprint 2025-26

<!-- page 22 of 39 -->

VECTOR ALGEBRA

359

Example 14 Find angle ‘θ’ between the vectors $\vec{a} = \hat{i} + \hat{j} - \hat{k}$ and $\vec{b} = \hat{i} - \hat{j} + \hat{k}$.

Solution The angle $\theta$ between two vectors $\vec{a}$ and $\vec{b}$ is given by

$$
\cos \theta = \frac {\vec {a} \cdot \vec {b}}{| \vec {a} | | \vec {b} |}
$$

Now

$$
\vec {a} \cdot \vec {b} = (\hat {i} + \hat {j} - \hat {k}) \cdot (\hat {i} - \hat {j} + \hat {k}) = 1 - 1 - 1 = - 1.
$$

Therefore, we have

$$
\cos \theta = \frac {- 1}{3}
$$

hence the required angle is

$$
\theta = \cos^ {- 1} \left(- \frac {1}{3}\right)
$$

Example 15 If $\vec{a} = 5\hat{i} -\hat{j} -3\hat{k}$ and $\vec{b} = \hat{i} +3\hat{j} -5\hat{k}$, then show that the vectors $\vec{a} +\vec{b}$ and $\vec{a} -\vec{b}$ are perpendicular.

Solution We know that two nonzero vectors are perpendicular if their scalar product is zero.

Here

$$
\vec {a} + \vec {b} = (5 \hat {i} - \hat {j} - 3 \hat {k}) + (\hat {i} + 3 \hat {j} - 5 \hat {k}) = 6 \hat {i} + 2 \hat {j} - 8 \hat {k}
$$

and

$$
\vec {a} - \vec {b} = (5 \hat {i} - \hat {j} - 3 \hat {k}) - (\hat {i} + 3 \hat {j} - 5 \hat {k}) = 4 \hat {i} - 4 \hat {j} + 2 \hat {k}
$$

So

$$
(\vec {a} + \vec {b}). (\vec {a} - \vec {b}) = (6 \hat {i} + 2 \hat {j} - 8 \hat {k}) \cdot (4 \hat {i} - 4 \hat {j} + 2 \hat {k}) = 2 4 - 8 - 1 6 = 0.
$$

Hence  $\vec{a}+\vec{b}$  and  $\vec{a}-\vec{b}$  are perpendicular vectors.

Example 16 Find the projection of the vector $\vec{a} = 2\hat{i} + 3\hat{j} + 2\hat{k}$ on the vector $\vec{b} = \hat{i} + 2\hat{j} + \hat{k}$.

Solution The projection of vector $\vec{a}$ on the vector $\vec{b}$ is given by

$$
\frac {1}{| \vec {b} |} (\vec {a} \cdot \vec {b}) = \frac {(2 \times 1 + 3 \times 2 + 2 \times 1)}{\sqrt {(1) ^ {2} + (2) ^ {2} + (1) ^ {2}}} = \frac {1 0}{\sqrt {6}} = \frac {5}{3} \sqrt {6}
$$

Example 17 Find $|\vec{a} - \vec{b}|$, if two vectors $\vec{a}$ and $\vec{b}$ are such that $|\vec{a}| = 2$, $|\vec{b}| = 3$ and $\vec{a} \cdot \vec{b} = 4$.

Solution We have

$$
\begin{array}{r l} & {\mid \vec {a} - \vec {b} \mid^ {2} = (\vec {a} - \vec {b}) \cdot (\vec {a} - \vec {b})} \\ & {\qquad = \vec {a}. \vec {a} - \vec {a} \cdot \vec {b} - \vec {b} \cdot \vec {a} + \vec {b} \cdot \vec {b}} \end{array}
$$

Reprint 2025-26

<!-- page 23 of 39 -->

360

MATHEMATICS

$$
= | \vec {a} | ^ {2} - 2 (\vec {a} \cdot \vec {b}) + | \vec {b} | ^ {2}
$$

$$
= (2) ^ {2} - 2 (4) + (3) ^ {2}
$$

Therefore

$$
| \vec {a} - \vec {b} | = \sqrt {5}
$$

Example 18 If $\vec{a}$ is a unit vector and $(\vec{x} -\vec{a})\cdot (\vec{x} +\vec{a}) = 8$ , then find $|\vec{x} |$

Solution Since $\vec{a}$ is a unit vector, $|\vec{a}| = 1$. Also,

$$
\left(\vec {x} - \vec {a}\right) \cdot \left(\vec {x} + \vec {a}\right) = 8
$$

or

$$
\vec {x} \cdot \vec {x} + \vec {x} \cdot \vec {a} - \vec {a} \cdot \vec {x} - \vec {a} \cdot \vec {a} = 8
$$

or

$$
| \vec {x} | ^ {2} - 1 = 8 \text {i.e.} | \vec {x} | ^ {2} = 9
$$

Therefore

$|\vec{x}| = 3$ (as magnitude of a vector is non negative).

Example 19 For any two vectors $\vec{a}$ and $\vec{b}$, we always have $|\vec{a} \cdot \vec{b}| \leq |\vec{a}| |\vec{b}|$ (Cauchy-Schwartz inequality).

Solution The inequality holds trivially when either $\vec{a} = \vec{0}$ or $\vec{b} = \vec{0}$. Actually, in such a situation we have $|\vec{a} \cdot \vec{b}| = 0 = |\vec{a}| |\vec{b}|$. So, let us assume that $|\vec{a}| \neq 0 \neq |\vec{b}|$.

$$
\frac {| \vec {a} \cdot \vec {b} |}{| \vec {a} | | \vec {b} |} = | \cos \theta | \leq 1
$$

Therefore

$$
| \vec {a} \cdot \vec {b} | \leq | \vec {a} | | \vec {b} |
$$

Example 20 For any two vectors $\vec{a}$ and $\vec{b}$, we always have $|\vec{a} +\vec{b} |\leq |\vec{a}| + |\vec{b} |$ (triangle inequality).

![Image block](doc:8590c4e/tier:standard/page:23/block:22)

Solution The inequality holds trivially in case either $\vec{a} = \vec{0}$ or $\vec{b} = \vec{0}$ (How?). So, let $|\vec{a}| \neq \vec{0} \neq |\vec{b}|$. Then,

$$
\begin{array}{r l} \left| \vec {a} + \vec {b} \right| ^ {2} & = (\vec {a} + \vec {b}) ^ {2} = (\vec {a} + \vec {b}) \cdot (\vec {a} + \vec {b}) \\ & = \vec {a} \cdot \vec {a} + \vec {a} \cdot \vec {b} + \vec {b} \cdot \vec {a} + \vec {b} \cdot \vec {b} \\ & = | \vec {a} | ^ {2} + 2 \vec {a} \cdot \vec {b} + | \vec {b} | ^ {2} \\ & \leq | \vec {a} | ^ {2} + 2 | \vec {a} \cdot \vec {b} | + | \vec {b} | ^ {2} \\ & \leq | \vec {a} | ^ {2} + 2 | \vec {a} \| \vec {b} | + | \vec {b} | ^ {2} \\ & = (| \vec {a} | + | \vec {b} |) ^ {2} \end{array}
$$

Fig 10.21

(scalar product is commutative)
(since $x \leq |x| \forall x \in \mathbf{R}$)
(from Example 19)

Reprint 2025-26

<!-- page 24 of 39 -->

VECTOR ALGEBRA

361

Hence

$$
| \vec {a} + \vec {b} | \leq | \vec {a} | + | \vec {b} |
$$

Remark If the equality holds in triangle inequality (in the above Example 20), i.e.

$$
| \vec {a} + \vec {b} | = | \vec {a} | + | \vec {b} |,
$$

then

$$
| \overline {{\mathrm{AC}}} | = | \overline {{\mathrm{AB}}} | + | \overline {{\mathrm{BC}}} |
$$

showing that the points A, B and C are collinear.

Example 21 Show that the points A $(-2\hat{i}+3\hat{j}+5\hat{k})$ , B $(\hat{i}+2\hat{j}+3\hat{k})$  and C $(7\hat{i}-\hat{k})$  are collinear.

Solution We have

$$
\overline {{\mathrm{AB}}} = (1 + 2) \hat {i} + (2 - 3) \hat {j} + (3 - 5) \hat {k} = 3 \hat {i} - \hat {j} - 2 \hat {k},
$$

$$
\overline {{\mathrm{BC}}} = (7 - 1) \hat {i} + (0 - 2) \hat {j} + (- 1 - 3) \hat {k} = 6 \hat {i} - 2 \hat {j} - 4 \hat {k},
$$

$$
\overline {{\mathrm{AC}}} = (7 + 2) \hat {i} + (0 - 3) \hat {j} + (- 1 - 5) \hat {k} = 9 \hat {i} - 3 \hat {j} - 6 \hat {k}
$$

$$
\left| \overline {{\mathrm{AB}}} \right| = \sqrt {1 4}, \left| \overline {{\mathrm{BC}}} \right| = 2 \sqrt {1 4} \text {and} \left| \overline {{\mathrm{AC}}} \right| = 3 \sqrt {1 4}
$$

Therefore

$$
\left| \overline {{\mathrm{AC}}} \right| = \left| \overline {{\mathrm{AB}}} \right| + \left| \overline {{\mathrm{BC}}} \right|
$$

Hence the points A, B and C are collinear.

Note In Example 21, one may note that although $\overrightarrow{AB} +\overrightarrow{BC} +\overrightarrow{CA} = \vec{0}$ but the points A, B and C do not form the vertices of a triangle.

## EXERCISE 10.3

1. Find the angle between two vectors $\vec{a}$ and $\vec{b}$ with magnitudes $\sqrt{3}$ and 2, respectively having $\vec{a} \cdot \vec{b} = \sqrt{6}$.

2. Find the angle between the vectors $\hat{i} - 2\hat{j} + 3\hat{k}$ and $3\hat{i} - 2\hat{j} + \hat{k}$

3. Find the projection of the vector $\hat{i} -\hat{j}$ on the vector $\hat{i} +\hat{j}$.

4. Find the projection of the vector $\hat{i} + 3\hat{j} + 7\hat{k}$ on the vector $7\hat{i} - \hat{j} + 8\hat{k}$.

5. Show that each of the given three vectors is a unit vector:

$$
\frac {1}{7} (2 \hat {i} + 3 \hat {j} + 6 \hat {k}), \frac {1}{7} (3 \hat {i} - 6 \hat {j} + 2 \hat {k}), \frac {1}{7} (6 \hat {i} + 2 \hat {j} - 3 \hat {k})
$$

Also, show that they are mutually perpendicular to each other.

Reprint 2025-26

<!-- page 25 of 39 -->

362

MATHEMATICS

6. Find $|\vec{a}|$ and $|\vec{b}|$, if $(\vec{a} + \vec{b}) \cdot (\vec{a} - \vec{b}) = 8$ and $|\vec{a}| = 8|\vec{b}|$.

7. Evaluate the product $(3\vec{a} - 5\vec{b}) \cdot (2\vec{a} + 7\vec{b})$.

8. Find the magnitude of two vectors $\vec{a}$ and $\vec{b}$, having the same magnitude and such that the angle between them is $60^{\circ}$ and their scalar product is $\frac{1}{2}$.

9. Find $|\vec{x}|$, if for a unit vector $\vec{a}$, $(\vec{x} - \vec{a}) \cdot (\vec{x} + \vec{a}) = 12$.

10. If $\vec{a} = 2\hat{i} + 2\hat{j} + 3\hat{k}$, $\vec{b} = -\hat{i} + 2\hat{j} + \hat{k}$ and $\vec{c} = 3\hat{i} + \hat{j}$ are such that $\vec{a} + \lambda \vec{b}$ is perpendicular to $\vec{c}$, then find the value of $\lambda$.

11. Show that $|\vec{a}| \vec{b} + |\vec{b}| \vec{a}$ is perpendicular to $|\vec{a}| \vec{b} - |\vec{b}| \vec{a}$, for any two nonzero vectors $\vec{a}$ and $\vec{b}$.

12. If $\vec{a} \cdot \vec{a} = 0$ and $\vec{a} \cdot \vec{b} = 0$, then what can be concluded about the vector $\vec{b}$?

13. If $\vec{a},\vec{b},\vec{c}$ are unit vectors such that $\vec{a} +\vec{b} +\vec{c} = \vec{0}$, find the value of $\vec{a}\cdot \vec{b} +\vec{b}\cdot \vec{c} +\vec{c}\cdot \vec{a}$.

14. If either vector $\vec{a} = \vec{0}$ or $\vec{b} = \vec{0}$, then $\vec{a} \cdot \vec{b} = 0$. But the converse need not be true. Justify your answer with an example.

15. If the vertices A, B, C of a triangle ABC are (1, 2, 3), (-1, 0, 0), (0, 1, 2), respectively, then find $\angle ABC$. [∠ABC is the angle between the vectors $\overline{BA}$ and $\overline{BC}$].

16. Show that the points $\mathrm{A}(1,2,7)$, $\mathrm{B}(2,6,3)$ and $\mathrm{C}(3,10,-1)$ are collinear.

17. Show that the vectors $2\hat{i} - \hat{j} + \hat{k}$, $\hat{i} - 3\hat{j} - 5\hat{k}$ and $3\hat{i} - 4\hat{j} - 4\hat{k}$ form the vertices of a right angled triangle.

18. If $\vec{a}$ is a nonzero vector of magnitude 'a' and $\lambda$ a nonzero scalar, then $\lambda \vec{a}$ is unit vector if (A) $\lambda = 1$ (B) $\lambda = -1$ (C) $a = |\lambda|$ (D) $a = 1 / |\lambda|$

## 10.6.3 Vector (or cross) product of two vectors

In Section 10.2, we have discussed on the three dimensional right handed rectangular coordinate system. In this system, when the positive $x$-axis is rotated counterclockwise

Reprint 2025-26

<!-- page 26 of 39 -->

VECTOR ALGEBRA

363

into the positive $y$-axis, a right handed (standard) screw would advance in the direction of the positive $z$-axis (Fig 10.22(i)).

In a right handed coordinate system, the thumb of the right hand points in the direction of the positive z-axis when the fingers are curled in the direction away from the positive x-axis toward the positive y-axis (Fig 10.22(ii)).

![Image block](doc:8590c4e/tier:standard/page:26/block:5)

Fig 10.22 (i), (ii)

Definition 3 The vector product of two nonzero vectors $\vec{a}$ and $\vec{b}$, is denoted by $\vec{a} \times \vec{b}$ and defined as

$$
\vec {a} \times \vec {b} = | \vec {a} | | \vec {b} | \sin \theta \hat {n},
$$

where, $\theta$ is the angle between $\vec{a}$ and $\vec{b}$, $0 \leq \theta \leq \pi$ and $\hat{n}$ is a unit vector perpendicular to both $\vec{a}$ and $\vec{b}$, such that $\vec{a}, \vec{b}$ and $\hat{n}$ form a right handed system (Fig 10.23). i.e., the right handed system rotated from $\vec{a}$ to $\vec{b}$ moves in the direction of $\hat{n}$.

![Image block](doc:8590c4e/tier:standard/page:26/block:10)

Fig 10.23

If either $\vec{a} = \vec{0}$ or $\vec{b} = \vec{0}$, then $\theta$ is not defined and in this case, we define $\vec{a} \times \vec{b} = \vec{0}$. Observations

1. $\vec{a} \times \vec{b}$ is a vector.

2. Let $\vec{a}$ and $\vec{b}$ be two nonzero vectors. Then $\vec{a} \times \vec{b} = \vec{0}$ if and only if $\vec{a}$ and $\vec{b}$ are parallel (or collinear) to each other, i.e.,

$$
\vec {a} \times \vec {b} = \vec {0} \Leftrightarrow \vec {a} \| \vec {b}
$$

Reprint 2025-26

<!-- page 27 of 39 -->

364

MATHEMATICS

In particular, $\vec{a} \times \vec{a} = \vec{0}$ and $\vec{a} \times (-\vec{a}) = \vec{0}$, since in the first situation, $\theta = 0$ and in the second one, $\theta = \pi$, making the value of $\sin \theta$ to be 0.

3. If $\theta = \frac{\pi}{2}$ then $\vec{a} \times \vec{b} = |\vec{a}| |\vec{b}|$.

4. In view of the Observations 2 and 3, for mutually perpendicular unit vectors $\hat{i},\hat{j}$ and $\hat{k}$ (Fig 10.24), we have

![Image block](doc:8590c4e/tier:standard/page:27/block:6)

$$
\begin{array}{l} \hat {i} \times \hat {i} = \hat {j} \times \hat {j} = \hat {k} \times \hat {k} = \vec {0} \\ \hat {i} \times \hat {j} = \hat {k}, \quad \hat {j} \times \hat {k} = \hat {i}, \quad \hat {k} \times \hat {i} = \hat {j} \end{array}
$$

Fig 10.24

5. In terms of vector product, the angle between two vectors  $\vec{a}$  and  $\vec{b}$  may be given as

$$
\left| \sin \theta = \frac {\left| \vec {a} \times \vec {b} \right|}{\left| \vec {a} \right| \left| \vec {b} \right|} \right|
$$

6. It is always true that the vector product is not commutative, as $\vec{a} \times \vec{b} = -\vec{b} \times \vec{a}$. Indeed, $\vec{a} \times \vec{b} = |\vec{a}| \|\vec{b}| \sin \theta \hat{n}$, where $\vec{a}, \vec{b}$ and $\hat{n}$ form a right handed system, i.e., $\theta$ is traversed from $\vec{a}$ to $\vec{b}$, Fig 10.25 (i). While, $\vec{b} \times \vec{a} = |\vec{a}| \|\vec{b}| \sin \theta \hat{n}_1$, where $\vec{b}, \vec{a}$ and $\hat{n}_1$ form a right handed system i.e. $\theta$ is traversed from $\vec{b}$ to $\vec{a}$, Fig 10.25(ii).

![Image block](doc:8590c4e/tier:standard/page:27/block:12)

(i)

![Image block](doc:8590c4e/tier:standard/page:27/block:14)

Fig 10.25 (i), (ii)

(ii)

Thus, if we assume $\vec{a}$ and $\vec{b}$ to lie in the plane of the paper, then $\hat{n}$ and $\hat{n}_1$ both will be perpendicular to the plane of the paper. But, $\hat{n}$ being directed above the paper while $\hat{n}_1$ directed below the paper. i.e. $\hat{n}_1 = -\hat{n}$.

Reprint 2025-26

<!-- page 28 of 39 -->

VECTOR ALGEBRA

365

Hence

$$
\begin{array}{r l} \vec {a} \times \vec {b} = & | \vec {a} \| \vec {b} | \sin \theta \hat {n} \\ = & - | \vec {a} \| \vec {b} | \sin \theta \hat {n} _ {1} = - \vec {b} \times \vec {a} \end{array}
$$

7. In view of the Observations 4 and 6, we have

$$
\hat {j} \times \hat {i} = - \hat {k}, \hat {k} \times \hat {j} = - \hat {i} \text {and} \hat {i} \times \hat {k} = - \hat {j}.
$$

8. If $\vec{a}$ and $\vec{b}$ represent the adjacent sides of a triangle then its area is given as

$$
\frac {1}{2} | \vec {a} \times \vec {b} |
$$

By definition of the area of a triangle, we have from Fig 10.26,

Area of triangle ABC =  $\frac{1}{2}$ AB·CD.

![Image block](doc:8590c4e/tier:standard/page:28/block:11)

Fig 10.26

But $\mathrm{AB} = |\vec{b}|$ (as given), and $\mathrm{CD} = |\vec{a}| \sin \theta$.

Thus, Area of triangle $\mathrm{ABC} = \frac{1}{2} |\vec{b}||\vec{a} |\sin \theta = \frac{1}{2} |\vec{a}\times \vec{b}|.$

9. If $\vec{a}$ and $\vec{b}$ represent the adjacent sides of a parallelogram, then its area is given

by $|\vec{a}\times \vec{b} |$

From Fig 10.27, we have

Area of parallelogram ABCD = AB. DE.

But $\mathrm{AB} = |\vec{b}|$ (as given), and

![Image block](doc:8590c4e/tier:standard/page:28/block:20)

Fig 10.27

Thus,

Area of parallelogram ABCD = | $\vec{b}$ || $\vec{a}$ | sin θ = | $\vec{a} \times \vec{b}$ | .

We now state two important properties of vector product.

Property 3 (Distributivity of vector product over addition): If $\vec{a},\vec{b}$ and $\vec{c}$ are any three vectors and $\lambda$ be a scalar, then

(i) $\vec{a}\times (\vec{b} +\vec{c}) = \vec{a}\times \vec{b} +\vec{a}\times \vec{c}$

(ii) $\lambda (\vec{a}\times \vec{b}) = (\lambda \vec{a})\times \vec{b} = \vec{a}\times (\lambda \vec{b})$

Reprint 2025-26

<!-- page 29 of 39 -->

366

MATHEMATICS

Let $\vec{a}$ and $\vec{b}$ be two vectors given in component form as $a_1\hat{i} + a_2\hat{j} + a_3\hat{k}$ and $b_1\hat{i} + b_2\hat{j} + b_3\hat{k}$, respectively. Then their cross product may be given by

$$
\vec {a} \times \vec {b} = \left| \begin{array}{c c c} \hat {i} & \hat {j} & \hat {k} \\ a _ {1} & a _ {2} & a _ {3} \\ b _ {1} & b _ {2} & b _ {3} \end{array} \right|
$$

Explanation We have

$$
\begin{array}{r l} \vec {a} \times \vec {b} & = (a _ {1} \hat {i} + a _ {2} \hat {j} + a _ {3} \hat {k}) \times (b _ {1} \hat {i} + b _ {2} \hat {j} + b _ {3} \hat {k}) \\ & = a _ {1} b _ {1} (\hat {i} \times \hat {i}) + a _ {1} b _ {2} (\hat {i} \times \hat {j}) + a _ {1} b _ {3} (\hat {i} \times \hat {k}) + a _ {2} b _ {1} (\hat {j} \times \hat {i}) \\ & \quad + a _ {2} b _ {2} (\hat {j} \times \hat {j}) + a _ {2} b _ {3} (\hat {j} \times \hat {k}) \\ & \quad + a _ {3} b _ {1} (\hat {k} \times \hat {i}) + a _ {3} b _ {2} (\hat {k} \times \hat {j}) + a _ {3} b _ {3} (\hat {k} \times \hat {k}) \\ & = a _ {1} b _ {2} (\hat {i} \times \hat {j}) - a _ {1} b _ {3} (\hat {k} \times \hat {i}) - a _ {2} b _ {1} (\hat {i} \times \hat {j}) \\ & \quad + a _ {2} b _ {3} (\hat {j} \times \hat {k}) + a _ {3} b _ {1} (\hat {k} \times \hat {i}) - a _ {3} b _ {2} (\hat {j} \times \hat {k}) \end{array}
$$

(by Property 1)

$$
\begin{array}{r l} (\text {as} \hat {i} \times \hat {i} = \hat {j} \times \hat {j} = \hat {k} \times \hat {k} = 0 \text {and} \hat {i} \times \hat {k} = - \hat {k} \times \hat {i}, \hat {j} \times \hat {i} = - \hat {i} \times \hat {j} \text {and} \\ & = a _ {1} b _ {2} \hat {k} - a _ {1} b _ {3} \hat {j} - a _ {2} b _ {1} \hat {k} + a _ {2} b _ {3} \hat {i} + a _ {3} b _ {1} \hat {j} - a _ {3} b _ {2} \hat {i} \\ & (\text {as} \hat {i} \times \hat {j} = \hat {k}, \hat {j} \times \hat {k} = \hat {i} \text {and} \hat {k} \times \hat {i} = \hat {j}) \\ & = (a _ {2} b _ {3} - a _ {3} b _ {2}) \hat {i} - (a _ {1} b _ {3} - a _ {3} b _ {1}) \hat {j} + (a _ {1} b _ {2} - a _ {2} b _ {1}) \hat {k} \\ & = \left| \begin{array}{c c c} \hat {i} & \hat {j} & \hat {k} \\ a _ {1} & a _ {2} & a _ {3} \\ b _ {1} & b _ {2} & b _ {3} \end{array} \right| \end{array}
$$

$$
\hat {k} \times \hat {j} = - \hat {j} \times \hat {k})
$$

Example 22 Find $|\vec{a} \times \vec{b}|$, if $\vec{a} = 2\hat{i} + \hat{j} + 3\hat{k}$ and $\vec{b} = 3\hat{i} + 5\hat{j} - 2\hat{k}$

Solution We have

$$
\begin{array}{r l} \vec {a} \times \vec {b} = & \left| \begin{array}{c c c} \hat {i} & \hat {j} & \hat {k} \\ 2 & 1 & 3 \\ 3 & 5 & - 2 \end{array} \right| \\ = & \hat {i} (- 2 - 1 5) - (- 4 - 9) \hat {j} + (1 0 - 3) \hat {k} = - 1 7 \hat {i} + 1 3 \hat {j} + 7 \hat {k} \end{array}
$$

Hence

$$
\left| \vec {a} \times \vec {b} \right| = \sqrt {(- 1 7) ^ {2} + (1 3) ^ {2} + (7) ^ {2}} = \sqrt {5 0 7}
$$

Reprint 2025-26

<!-- page 30 of 39 -->

VECTOR ALGEBRA

367

Example 23 Find a unit vector perpendicular to each of the vectors $(\vec{a} + \vec{b})$ and $(\vec{a} - \vec{b})$, where $\vec{a} = \hat{i} + \hat{j} + \hat{k}$, $\vec{b} = \hat{i} + 2\hat{j} + 3\hat{k}$.

Solution We have $\vec{a} +\vec{b} = 2\hat{i} +3\hat{j} +4\hat{k}$ and $\vec{a} -\vec{b} = -\hat{j} -2\hat{k}$

A vector which is perpendicular to both $\vec{a} +\vec{b}$ and $\vec{a} -\vec{b}$ is given by

$$
\begin{array}{c} (\vec {a} + \vec {b}) \times (\vec {a} - \vec {b}) = \left| \begin{array}{c c c} \hat {i} & \hat {j} & \hat {k} \\ 2 & 3 & 4 \\ 0 & - 1 & - 2 \end{array} \right| = - 2 \hat {i} + 4 \hat {j} - 2 \hat {k} (= \vec {c}, \text {say}) \\ | \vec {c} | = \sqrt {4 + 1 6 + 4} = \sqrt {2 4} = 2 \sqrt {6} \end{array}
$$

Now

Therefore, the required unit vector is

$$
\frac {\vec {c}}{| \vec {c} |} = \frac {- 1}{\sqrt {6}} \hat {i} + \frac {2}{\sqrt {6}} \hat {j} - \frac {1}{\sqrt {6}} \hat {k}
$$

Note There are two perpendicular directions to any plane. Thus, another unit vector perpendicular to $\vec{a} +\vec{b}$ and $\vec{a} -\vec{b}$ will be $\frac{1}{\sqrt{6}}\hat{i} -\frac{2}{\sqrt{6}}\hat{j} +\frac{1}{\sqrt{6}}\hat{k}$. But that will be a consequence of $(\vec{a} -\vec{b})\times (\vec{a} +\vec{b})$ .

Example 24 Find the area of a triangle having the points A(1, 1, 1), B(1, 2, 3) and C(2, 3, 1) as its vertices.

Solution We have $\overrightarrow{\mathrm{AB}} = \hat{j} + 2\hat{k}$ and $\overrightarrow{\mathrm{AC}} = \hat{i} + 2\hat{j}$. The area of the given triangle is $\frac{1}{2} |\overrightarrow{\mathrm{AB}} \times \overrightarrow{\mathrm{AC}}|$.

Now,

$$
\overline {{\mathrm{AB}}} \times \overline {{\mathrm{AC}}} = \left| \begin{array}{c c c} \hat {i} & \hat {j} & \hat {k} \\ 0 & 1 & 2 \\ 1 & 2 & 0 \end{array} \right| = - 4 \hat {i} + 2 \hat {j} - \hat {k}
$$

Therefore

$$
\mid \overline {{\mathrm{AB}}} \times \overline {{\mathrm{AC}}} \mid = \sqrt {1 6 + 4 + 1} = \sqrt {2 1}
$$

Thus, the required area is $\frac{1}{2}\sqrt{21}$

Reprint 2025-26

<!-- page 31 of 39 -->

368

MATHEMATICS

Example 25 Find the area of a parallelogram whose adjacent sides are given by the vectors $\vec{a} = 3\hat{i} +\hat{j} +4\hat{k}$ and $\vec{b} = \hat{i} -\hat{j} +\hat{k}$

Solution The area of a parallelogram with  $\vec{a}$  and  $\vec{b}$  as its adjacent sides is given by  $|\vec{a}\times\vec{b}|$ .

Now

$$
\vec {a} \times \vec {b} = \left| \begin{array}{c c c} \hat {i} & \hat {j} & \hat {k} \\ 3 & 1 & 4 \\ 1 & - 1 & 1 \end{array} \right| = 5 \hat {i} + \hat {j} - 4 \hat {k}
$$

Therefore

$$
| \vec {a} \times \vec {b} | = \sqrt {2 5 + 1 + 1 6} = \sqrt {4 2}
$$

and hence, the required area is $\sqrt{42}$.

## EXERCISE 10.4

1. Find $|\vec{a}\times \vec{b} |$ , if $\vec{a} = \hat{i} -7\hat{j} +7\hat{k}$ and $\vec{b} = 3\hat{i} -2\hat{j} +2\hat{k},$

2. Find a unit vector perpendicular to each of the vector $\vec{a} +\vec{b}$ and $\vec{a} -\vec{b}$, where $\vec{a} = 3\hat{i} +2\hat{j} +2\hat{k}$ and $\vec{b} = \hat{i} +2\hat{j} -2\hat{k}$.

3. If a unit vector $\vec{a}$ makes angles $\frac{\pi}{3}$ with $\hat{i}, \frac{\pi}{4}$ with $\hat{j}$ and an acute angle $\theta$ with $\hat{k}$, then find $\theta$ and hence, the components of $\vec{a}$.

4. Show that

$$
(\vec {a} - \vec {b}) \times (\vec {a} + \vec {b}) = 2 (\vec {a} \times \vec {b})
$$

5. Find $\lambda$ and $\mu$ if $(2\hat{i} + 6\hat{j} + 27\hat{k}) \times (\hat{i} + \lambda \hat{j} + \mu \hat{k}) = \vec{0}$.

6. Given that $\vec{a} \cdot \vec{b} = 0$ and $\vec{a} \times \vec{b} = \vec{0}$. What can you conclude about the vectors $\vec{a}$ and $\vec{b}$?

7. Let the vectors $\vec{a},\vec{b},\vec{c}$ be given as $a_1\hat{i} + a_2\hat{j} + a_3\hat{k}, b_1\hat{i} + b_2\hat{j} + b_3\hat{k}, c_1\hat{i} + c_2\hat{j} + c_3\hat{k}$. Then show that $\vec{a}\times (\vec{b} +\vec{c}) = \vec{a}\times \vec{b} +\vec{a}\times \vec{c}$.

8. If either $\vec{a} = \vec{0}$ or $\vec{b} = \vec{0}$, then $\vec{a} \times \vec{b} = \vec{0}$. Is the converse true? Justify your answer with an example.

9. Find the area of the triangle with vertices $\mathrm{A}(1,1,2)$, $\mathrm{B}(2,3,5)$ and $\mathrm{C}(1,5,5)$.

Reprint 2025-26

<!-- page 32 of 39 -->

VECTOR ALGEBRA

369

10. Find the area of the parallelogram whose adjacent sides are determined by the vectors $\vec{a} = \hat{i} - \hat{j} + 3\hat{k}$ and $\vec{b} = 2\hat{i} - 7\hat{j} + \hat{k}$.

11. Let the vectors $\vec{a}$ and $\vec{b}$ be such that $|\vec{a}| = 3$ and $|\vec{b}| = \frac{\sqrt{2}}{3}$, then $\vec{a} \times \vec{b}$ is a unit vector, if the angle between $\vec{a}$ and $\vec{b}$ is (A) $\pi / 6$ (B) $\pi / 4$ (C) $\pi / 3$ (D) $\pi / 2$

12. Area of a rectangle having vertices A, B, C and D with position vectors  $-\hat{i}+\frac{1}{2}\hat{j}+4\hat{k}, \hat{i}+\frac{1}{2}\hat{j}+4\hat{k}, \hat{i}-\frac{1}{2}\hat{j}+4\hat{k}$  and  $-\hat{i}-\frac{1}{2}\hat{j}+4\hat{k}$ , respectively is
(A)  $\frac{1}{2}$  (B) 1
(C) 2 (D) 4

## Miscellaneous Examples

Example 26 Write all the unit vectors in XY-plane.

Solution Let $\vec{r} = x\hat{i} +y\hat{j}$ be a unit vector in XY-plane (Fig 10.28). Then, from the figure, we have $x = \cos \theta$ and $y = \sin \theta$ (since $|\vec{r}| = 1$). So, we may write the vector $\vec{r}$ as

$$
\vec {r} \left(= \overline {{\mathrm{OP}}}\right) = \cos \theta \hat {i} + \sin \theta \hat {j}
$$

Clearly,

$$
| \vec {r} | = \sqrt {\cos^ {2} \theta + \sin^ {2} \theta} = 1
$$

![Image block](doc:8590c4e/tier:standard/page:32/block:12)

Fig 10.28

Also, as $\theta$ varies from 0 to $2\pi$, the point P (Fig 10.28) traces the circle $x^{2} + y^{2} = 1$ counterclockwise, and this covers all possible directions. So, (1) gives every unit vector in the XY-plane.

Reprint 2025-26

<!-- page 33 of 39 -->

370

MATHEMATICS

Example 27 If $\hat{i} + \hat{j} + \hat{k}$, $2\hat{i} + 5\hat{j}$, $3\hat{i} + 2\hat{j} - 3\hat{k}$ and $\hat{i} - 6\hat{j} - \hat{k}$ are the position vectors of points A, B, C and D respectively, then find the angle between $\overrightarrow{\mathrm{AB}}$ and $\overrightarrow{\mathrm{CD}}$. Deduce that $\overrightarrow{\mathrm{AB}}$ and $\overrightarrow{\mathrm{CD}}$ are collinear.

Solution Note that if $\theta$ is the angle between AB and CD, then $\theta$ is also the angle between $\overline{\mathrm{AB}}$ and $\overline{\mathrm{CD}}$.

Now

$$
\begin{array}{r l} \overline {{\mathrm{AB}}} & = \text {Position vector of B - Position vector of A} \\ & = (2 \hat {i} + 5 \hat {j}) - (\hat {i} + \hat {j} + \hat {k}) = \hat {i} + 4 \hat {j} - \hat {k} \end{array}
$$

Therefore

$$
\overline {{| \mathrm{AB} |}} = \sqrt {(1) ^ {2} + (4) ^ {2} + (- 1) ^ {2}} = 3 \sqrt {2}
$$

Similarly

$$
\overline {{\mathrm{CD}}} = - 2 \hat {i} - 8 \hat {j} + 2 \hat {k} \text {and} | \overline {{\mathrm{CD}}} | = 6 \sqrt {2}
$$

Thus

$$
\begin{array}{r l} \cos \theta & = \frac {\overrightarrow {\mathrm{AB}} \cdot \overrightarrow {\mathrm{CD}}}{| \overrightarrow {\mathrm{AB}} | | \overrightarrow {\mathrm{CD}} |} \\ & = \frac {1 (- 2) + 4 (- 8) + (- 1) (2)}{(3 \sqrt {2}) (6 \sqrt {2})} = \frac {- 3 6}{3 6} = - 1 \end{array}
$$

Since $0 \leq \theta \leq \pi$, it follows that $\theta = \pi$. This shows that $\overline{\mathrm{AB}}$ and $\overline{\mathrm{CD}}$ are collinear.

Alternatively, $\overline{\mathrm{AB}} = -\frac{1}{2}\overrightarrow{\mathrm{CD}}$ which implies that $\overline{\mathrm{AB}}$ and $\overline{\mathrm{CD}}$ are collinear vectors.

Example 28 Let $\vec{a},\vec{b}$ and $\vec{c}$ be three vectors such that $|\vec{a}| = 3,|\vec{b}| = 4,|\vec{c}| = 5$ and each one of them being perpendicular to the sum of the other two, find $|\vec{a} +\vec{b} +\vec{c} |$

Solution Given $\vec{a} \cdot (\vec{b} + \vec{c}) = 0$, $\vec{b} \cdot (\vec{c} + \vec{a}) = 0$, $\vec{c} \cdot (\vec{a} + \vec{b}) = 0$.

Now

$$
\left| \begin{array}{c} | \vec {a} + \vec {b} + \vec {c} | ^ {2} = (\vec {a} + \vec {b} + \vec {c}) ^ {2} = (\vec {a} + \vec {b} + \vec {c}) \cdot (\vec {a} + \vec {b} + \vec {c}) \\ = \vec {a} \cdot \vec {a} + \vec {a} \cdot (\vec {b} + \vec {c}) + \vec {b} \cdot \vec {b} + \vec {b} \cdot (\vec {a} + \vec {c}) \\ + \vec {c}. (\vec {a} + \vec {b}) + \vec {c}. \vec {c} \\ = | \vec {a} | ^ {2} + | \vec {b} | ^ {2} + | \vec {c} | ^ {2} \\ = 9 + 1 6 + 2 5 = 5 0 \end{array} \right|
$$

Therefore

$$
| \vec {a} + \vec {b} + \vec {c} | = \sqrt {5 0} = 5 \sqrt {2}
$$

Reprint 2025-26

<!-- page 34 of 39 -->

VECTOR ALGEBRA

371

Example 29 Three vectors $\vec{a}$, $\vec{b}$ and $\vec{c}$ satisfy the condition $\vec{a} + \vec{b} + \vec{c} = \vec{0}$. Evaluate the quantity $\mu = \vec{a} \cdot \vec{b} + \vec{b} \cdot \vec{c} + \vec{c} \cdot \vec{a}$, if $|\vec{a}| = 3$, $|\vec{b}| = 4$ and $|\vec{c}| = 2$.

Solution Since $\vec{a} +\vec{b} +\vec{c} = \vec{0}$ , we have

$$
\vec {a} + \vec {b} + \vec {c} = \vec {0} = 0
$$

or

$$
\vec {a} \cdot \vec {a} + \vec {a} \cdot \vec {b} + \vec {a} \cdot \vec {c} = 0
$$

Therefore

$$
\vec {a} \cdot \vec {b} + \vec {a} \cdot \vec {c} = - \left| \vec {a} \right| ^ {2} = - 9\tag{... (1}
$$

Again,

$$
\vec {b} \cdot (\vec {a} + \vec {b} + \vec {c}) = 0
$$

or

$$
\vec {a} \cdot \vec {b} + \vec {b} \cdot \vec {c} = - \left| \vec {b} \right| ^ {2} = - 1 6\tag{... (2}
$$

Similarly

$$
\vec {a} \cdot \vec {c} + \vec {b} \cdot \vec {c} = - 4.\tag{... (3}
$$

Adding (1), (2) and (3), we have

$$
2 (\vec {a} \cdot \vec {b} + \vec {b} \cdot \vec {c} + \vec {a} \cdot \vec {c}) = - 2 9
$$

or

$$
2 \mu = - 2 9, \text {i.e.,} \mu = \frac {- 2 9}{2}
$$

Example 30 If with reference to the right handed system of mutually perpendicular unit vectors $\hat{i}, \hat{j}$ and $\hat{k}$, $\vec{\alpha} = 3\hat{i} - \hat{j}$, $\vec{\beta} = 2\hat{i} + \hat{j} - 3\hat{k}$, then express $\vec{\beta}$ in the form $\vec{\beta} = \vec{\beta}_1 + \vec{\beta}_2$, where $\vec{\beta}_1$ is parallel to $\vec{\alpha}$ and $\vec{\beta}_2$ is perpendicular to $\vec{\alpha}$.

Solution Let $\vec{\beta}_1 = \lambda \vec{\alpha}$, $\lambda$ is a scalar, i.e., $\vec{\beta}_1 = 3\lambda \hat{\imath} - \lambda \hat{\jmath}$.

Now

$$
\vec {\beta} _ {2} = \vec {\beta} - \vec {\beta} _ {1} = (2 - 3 \lambda) \hat {i} + (1 + \lambda) \hat {j} - 3 \hat {k}.
$$

Now, since $\bar{\beta}_2$ is to be perpendicular to $\vec{\alpha}$, we should have $\vec{\alpha} \cdot \bar{\beta}_2 = 0$ . i.e.,

$$
3 (2 - 3 \lambda) - (1 + \lambda) = 0
$$

or

$$
\lambda = \frac {1}{2}
$$

Therefore

$$
\vec {\beta} _ {1} = \frac {3}{2} \hat {i} - \frac {1}{2} \hat {j} \quad \text {and} \quad \vec {\beta} _ {2} = \frac {1}{2} \hat {i} + \frac {3}{2} \hat {j} - 3 \hat {k}
$$

Reprint 2025-26

<!-- page 35 of 39 -->

372

MATHEMATICS

## Miscellaneous Exercise on Chapter 10

1. Write down a unit vector in XY-plane, making an angle of $30^{\circ}$ with the positive direction of $x$-axis.

2. Find the scalar components and magnitude of the vector joining the points $\mathrm{P}(x_1, y_1, z_1)$ and $\mathrm{Q}(x_2, y_2, z_2)$.

3. A girl walks 4 km towards west, then she walks 3 km in a direction  $30^{\circ}$  east of north and stops. Determine the girl’s displacement from her initial point of departure.

4. If $\vec{a} = \vec{b} +\vec{c}$, then is it true that $|\vec{a}| = |\vec{b}| + |\vec{c} |?$ Justify your answer.

5. Find the value of $x$ for which $x(\hat{i} + \hat{j} + \hat{k})$ is a unit vector.

6. Find a vector of magnitude 5 units, and parallel to the resultant of the vectors $\vec{a} = 2\hat{i} + 3\hat{j} - \hat{k}$ and $\vec{b} = \hat{i} - 2\hat{j} + \hat{k}$.

7. If $\vec{a} = \hat{i} + \hat{j} + \hat{k}$, $\vec{b} = 2\hat{i} - \hat{j} + 3\hat{k}$ and $\vec{c} = \hat{i} - 2\hat{j} + \hat{k}$, find a unit vector parallel to the vector $2\vec{a} - \vec{b} + 3\vec{c}$.

8. Show that the points A(1, -2, -8), B(5, 0, -2) and C(11, 3, 7) are collinear, and find the ratio in which B divides AC.

9. Find the position vector of a point R which divides the line joining two points P and Q whose position vectors are  $(2\vec{a} + \vec{b})$  and  $(\vec{a} - 3\vec{b})$  externally in the ratio 1 : 2. Also, show that P is the mid point of the line segment RQ.

10. The two adjacent sides of a parallelogram are $2\hat{i} - 4\hat{j} + 5\hat{k}$ and $\hat{i} - 2\hat{j} - 3\hat{k}$. Find the unit vector parallel to its diagonal. Also, find its area.

11. Show that the direction cosines of a vector equally inclined to the axes OX, OY and OZ are  $\pm\left(\frac{1}{\sqrt{3}}, \frac{1}{\sqrt{3}}, \frac{1}{\sqrt{3}}\right)$ .

12. Let $\vec{a} = \hat{i} + 4\hat{j} + 2\hat{k}$, $\vec{b} = 3\hat{i} - 2\hat{j} + 7\hat{k}$ and $\vec{c} = 2\hat{i} - \hat{j} + 4\hat{k}$. Find a vector $\vec{d}$ which is perpendicular to both $\vec{a}$ and $\vec{b}$, and $\vec{c} \cdot \vec{d} = 15$.

13. The scalar product of the vector $\hat{i} + \hat{j} + \hat{k}$ with a unit vector along the sum of vectors $2\hat{i} + 4\hat{j} - 5\hat{k}$ and $\lambda \hat{i} + 2\hat{j} + 3\hat{k}$ is equal to one. Find the value of $\lambda$.

14. If $\vec{a},\vec{b},\vec{c}$ are mutually perpendicular vectors of equal magnitudes, show that the vector $\vec{c}\cdot \vec{d} = 15$ is equally inclined to $\vec{a},\vec{b}$ and $\vec{c}$.

Reprint 2025-26

<!-- page 36 of 39 -->

VECTOR ALGEBRA

373

15. Prove that  $(\vec{a}+\vec{b})\cdot(\vec{a}+\vec{b})=|\vec{a}|^{2}+|\vec{b}|^{2}$ , if and only if  $\vec{a},\vec{b}$  are perpendicular, given  $\vec{a}\neq\vec{0},\vec{b}\neq\vec{0}$ .

Choose the correct answer in Exercises 16 to 19.

16. If $\theta$ is the angle between two vectors $\vec{a}$ and $\vec{b}$, then $\vec{a} \cdot \vec{b} \geq 0$ only when (A) $0 < \theta < \frac{\pi}{2}$ (B) $0 \leq \theta \leq \frac{\pi}{2}$ (C) $0 < \theta < \pi$ (D) $0 \leq \theta \leq \pi$

17. Let $\vec{a}$ and $\vec{b}$ be two unit vectors and $\theta$ is the angle between them. Then $\vec{a} + \vec{b}$ is a unit vector if (A) $\theta = \frac{\pi}{4}$ (B) $\theta = \frac{\pi}{3}$ (C) $\theta = \frac{\pi}{2}$ (D) $\theta = \frac{2\pi}{3}$

18. The value of $\hat{i}.\hat{j}\times \hat{k}) + \hat{j}\cdot (\hat{i}\times \hat{k}) + \hat{k}\cdot (\hat{i}\times \hat{j})$ is (A) 0 (B) -1 (C) 1 (D) 3

19. If $\theta$ is the angle between any two vectors $\vec{a}$ and $\vec{b}$, then $|\vec{a} \cdot \vec{b}| = |\vec{a} \times \vec{b}|$ when $\theta$ is equal to (A) 0 (B) $\frac{\pi}{4}$ (C) $\frac{\pi}{2}$ (D) $\pi$

## Summary

Position vector of a point  $P(x, y, z)$  is given as  $\overline{\mathrm{OP}}(=\vec{r})=x\hat{i}+y\hat{j}+z\hat{k}$ , and its magnitude by  $\sqrt{x^{2}+y^{2}+z^{2}}$ .

The scalar components of a vector are its direction ratios, and represent its projections along the respective axes.

The magnitude (r), direction ratios (a, b, c) and direction cosines (l, m, n) of any vector are related as:

$$
l = \frac {a}{r}, \quad m = \frac {b}{r}, \quad n = \frac {c}{r}
$$

Reprint 2025-26

<!-- page 37 of 39 -->

374

MATHEMATICS

The vector sum of the three sides of a triangle taken in order is $\vec{0}$.

The vector sum of two coinitial vectors is given by the diagonal of the parallelogram whose adjacent sides are the given vectors.

The multiplication of a given vector by a scalar $\lambda$, changes the magnitude of the vector by the multiple $|\lambda|$, and keeps the direction same (or makes it opposite) according as the value of $\lambda$ is positive (or negative).

For a given vector  $\vec{a}$ , the vector  $\hat{a}=\frac{\vec{a}}{|\vec{a}|}$  gives the unit vector in the direction of  $\vec{a}$ .

The position vector of a point R dividing a line segment joining the points P and Q whose position vectors are  $\vec{a}$  and  $\vec{b}$  respectively, in the ratio m : n

(i) internally, is given by  $\frac{n\vec{a} + m\vec{b}}{m + n}$ .

(ii) externally, is given by $\frac{m\vec{b} - n\vec{a}}{m - n}$.

The scalar product of two given vectors $\vec{a}$ and $\vec{b}$ having angle $\theta$ between them is defined as

$$
\vec {a} \cdot \vec {b} = | \vec {a} \| \vec {b} | \cos \theta .
$$

Also, when  $\vec{a} \cdot \vec{b}$  is given, the angle ‘θ’ between the vectors  $\vec{a}$  and  $\vec{b}$  may be determined by

$$
\cos \theta = \frac {\vec {a} \cdot \vec {b}}{| \vec {a} | | \vec {b} |}
$$

If $\theta$ is the angle between two vectors $\vec{a}$ and $\vec{b}$, then their cross product is given as

$$
\vec {a} \times \vec {b} = | \vec {a} | | \vec {b} | \sin \theta \hat {n}
$$

where $\hat{n}$ is a unit vector perpendicular to the plane containing $\vec{a}$ and $\vec{b}$. Such that $\vec{a},\vec{b},\hat{n}$ form right handed system of coordinate axes.

If we have two vectors $\vec{a}$ and $\vec{b}$, given in component form as $\vec{a} = a_1\hat{i} + a_2\hat{j} + a_3\hat{k}$ and $\vec{b} = b_1\hat{i} + b_2\hat{j} + b_3\hat{k}$ and $\lambda$ any scalar,

Reprint 2025-26

<!-- page 38 of 39 -->

VECTOR ALGEBRA

375

then

$$
\vec {a} + \vec {b} = (a _ {1} + b _ {1}) \hat {i} + (a _ {2} + b _ {2}) \hat {j} + (a _ {3} + b _ {3}) \hat {k};
$$

$$
\lambda \vec {a} = (\lambda a _ {1}) \hat {i} + (\lambda a _ {2}) \hat {j} + (\lambda a _ {3}) \hat {k};
$$

$$
\vec {a} \cdot \vec {b} = a _ {1} b _ {1} + a _ {2} b _ {2} + a _ {3} b _ {3};
$$

and

$$
\vec {a} \times \vec {b} = \left| \begin{array}{c c c} \hat {i} & \hat {j} & \hat {k} \\ a _ {1} & b _ {1} & c _ {1} \\ a _ {2} & b _ {2} & c _ {2} \end{array} \right|.
$$

## Historical Note

The word vector has been derived from a Latin word vectus, which means “to carry”. The germinal ideas of modern vector theory date from around 1800 when Caspar Wessel (1745-1818) and Jean Robert Argand (1768-1822) described that how a complex number  $a + ib$  could be given a geometric interpretation with the help of a directed line segment in a coordinate plane. William Rowen Hamilton (1805-1865) an Irish mathematician was the first to use the term vector for a directed line segment in his book Lectures on Quaternions (1853). Hamilton’s method of quaternions (an ordered set of four real numbers given as:

$a + b\hat{i} + c\hat{j} + d\hat{k}, \hat{i}, \hat{j}, \hat{k}$ following certain algebraic rules) was a solution to the

problem of multiplying vectors in three dimensional space. Though, we must mention here that in practice, the idea of vector concept and their addition was known much earlier ever since the time of Aristotle (384-322 B.C.), a Greek philosopher, and pupil of Plato (427-348 B.C.). That time it was supposed to be known that the combined action of two or more forces could be seen by adding them according to parallelogram law. The correct law for the composition of forces, that forces add vectorially, had been discovered in the case of perpendicular forces by Stevin-Simon (1548-1620). In 1586 A.D., he analysed the principle of geometric addition of forces in his treatise DeBeghinselen der Weeghconst (“Principles of the Art of Weighing”), which caused a major breakthrough in the development of mechanics. But it took another 200 years for the general concept of vectors to form.

In the 1880, Josaih Willard Gibbs (1839-1903), an American physicist and mathematician, and Oliver Heaviside (1850-1925), an English engineer, created what we now know as vector analysis, essentially by separating the real (scalar)

Reprint 2025-26

<!-- page 39 of 39 -->

376

MATHEMATICS

part of quaternion from its imaginary (vector) part. In 1881 and 1884, Gibbs printed a treatise entitled Element of Vector Analysis. This book gave a systematic and concise account of vectors. However, much of the credit for demonstrating the applications of vectors is due to the D. Heaviside and P.G. Tait (1831-1901) who contributed significantly to this subject.

Reprint 2025-26