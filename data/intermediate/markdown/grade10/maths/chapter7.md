<!-- page 1 of 14 -->

1062CH07

1062CH07

# COORDINATE GEOMETRY

## 7.1 Introduction

In Class IX, you have studied that to locate the position of a point on a plane, we require a pair of coordinate axes. The distance of a point from the y-axis is called its x-coordinate, or abscissa. The distance of a point from the x-axis is called its y-coordinate, or ordinate. The coordinates of a point on the x-axis are of the form  $(x, 0)$ , and of a point on the y-axis are of the form  $(0, y)$ .

Here is a play for you. Draw a set of a pair of perpendicular axes on a graph paper. Now plot the following points and join them as directed: Join the point A(4, 8) to B(3, 9) to C(3, 8) to D(1, 6) to E(1, 5) to F(3, 3) to G(6, 3) to H(8, 5) to I(8, 6) to J(6, 8) to K(6, 9) to L(5, 8) to A. Then join the points P(3.5, 7), Q (3, 6) and R(4, 6) to form a triangle. Also join the points X(5.5, 7), Y(5, 6) and Z(6, 6) to form a triangle. Now join S(4, 5), T(4.5, 4) and U(5, 5) to form a triangle. Lastly join S to the points (0, 5) and (0, 6) and join U to the points (9, 5) and (9, 6). What picture have you got?

Also, you have seen that a linear equation in two variables of the form  $ax + by + c = 0$ , (a, b are not simultaneously zero), when represented graphically, gives a straight line. Further, in Chapter 2, you have seen the graph of  $y = ax^{2} + bx + c$  ( $a \neq 0$ ), is a parabola. In fact, coordinate geometry has been developed as an algebraic tool for studying geometry of figures. It helps us to study geometry using algebra, and understand algebra with the help of geometry. Because of this, coordinate geometry is widely applied in various fields such as physics, engineering, navigation, seismology and art!

In this chapter, you will learn how to find the distance between the two points whose coordinates are given. You will also study how to find the coordinates of the point which divides a line segment joining two given points in a given ratio.

Reprint 2025-26

<!-- page 2 of 14 -->

100

MATHEMATICS

## 7.2 Distance Formula

Let us consider the following situation:

A town B is located 36 km east and 15 km north of the town A. How would you find the distance from town A to town B without actually measuring it. Let us see. This situation can be represented graphically as shown in Fig. 7.1. You may use the Pythagoras Theorem to calculate this distance.

Now, suppose two points lie on the $x$-axis. Can we find the distance between them? For instance, consider two points A(4, 0) and B(6, 0) in Fig. 7.2. The points A and B lie on the $x$-axis.

![Chart block](doc:d7eef70/tier:standard/page:2/block:7)

From the figure you can see that OA = 4 units and OB = 6 units.

Therefore, the distance of B from A, i.e., AB = OB - OA = 6 - 4 = 2 units.

So, if two points lie on the $x$-axis, we can easily find the distance between them.

![Chart block](doc:d7eef70/tier:standard/page:2/block:11)

Now, suppose we take two points lying on the $y$-axis. Can you find the distance between them. If the points $C(0, 3)$ and $D(0, 8)$ lie on the $y$-axis, similarly we find that $CD = 8 - 3 = 5$ units (see Fig. 7.2).

Fig. 7.2

Next, can you find the distance of A from C (in Fig. 7.2)? Since OA = 4 units and OC = 3 units, the distance of A from C, i.e.,  $AC = \sqrt{3^{2} + 4^{2}} = 5$  units. Similarly, you can find the distance of B from D = BD = 10 units.

Now, if we consider two points not lying on coordinate axis, can we find the distance between them? Yes! We shall use Pythagoras theorem to do so. Let us see an example.

In Fig. 7.3, the points P(4, 6) and Q(6, 8) lie in the first quadrant. How do we use Pythagoras theorem to find the distance between them? Let us draw PR and QS perpendicular to the x-axis from P and Q respectively. Also, draw a perpendicular from P on QS to meet QS at T. Then the coordinates of R and S are (4, 0) and (6, 0), respectively. So, RS = 2 units. Also, QS = 8 units and TS = PR = 6 units.

Reprint 2025-26

<!-- page 3 of 14 -->

COORDINATE GEOMETRY

101

Therefore, QT = 2 units and PT = RS = 2 units.

Now, using the Pythagoras theorem, we have

$$
\begin{array}{r l} \mathrm{PQ} ^ {2} & = \mathrm{PT} ^ {2} + \mathrm{QT} ^ {2} \\ & = 2 ^ {2} + 2 ^ {2} = 8 \end{array}
$$

So,

$$
\mathrm{PQ} = 2 \sqrt {2} \text {units}
$$

How will we find the distance between two points in two different quadrants?

Consider the points P(6, 4) and Q(-5, -3) (see Fig. 7.4). Draw QS perpendicular to the x-axis. Also draw a perpendicular PT from the point P on QS (extended) to meet y-axis at the point R.

![Chart block](doc:d7eef70/tier:standard/page:3/block:10)

Fig. 7.3

![Image block](doc:d7eef70/tier:standard/page:3/block:12)

Fig. 7.4

Then PT = 11 units and QT = 7 units. (Why?)

Using the Pythagoras Theorem to the right triangle PTQ, we get  $PQ = \sqrt{11^{2} + 7^{2}} = \sqrt{170}$  units.

Reprint 2025-26

<!-- page 4 of 14 -->

102

MATHEMATICS

Let us now find the distance between any two points  $P(x_{1}, y_{1})$  and  $Q(x_{2}, y_{2})$ . Draw PR and QS perpendicular to the x-axis. A perpendicular from the point P on QS is drawn to meet it at the point T (see Fig. 7.5).

Then, $\mathrm{OR} = x_{1}$, $\mathrm{OS} = x_{2}$. So, $\mathrm{RS} = x_{2} - x_{1} = \mathrm{PT}$.

Also, $\mathrm{SQ} = y_{2}$, $\mathrm{ST} = \mathrm{PR} = y_{1}$. So, $\mathrm{QT} = y_{2} - y_{1}$.

Now, applying the Pythagoras theorem in $\Delta$ PTQ, we get

![Image block](doc:d7eef70/tier:standard/page:4/block:7)

Therefore,

$$
\begin{array}{r l} \mathrm{PQ} ^ {2} & = \mathrm{PT} ^ {2} + \mathrm{QT} ^ {2} \\ & = (x _ {2} - x _ {1}) ^ {2} + (y _ {2} - y _ {1}) ^ {2} \\ \mathrm{PQ} & = \sqrt {(x _ {2} - x _ {1}) ^ {2} + (y _ {2} - y _ {1}) ^ {2}} \end{array}
$$

Fig. 7.5

Note that since distance is always non-negative, we take only the positive square root. So, the distance between the points $\mathrm{P}(x_1, y_1)$ and $\mathrm{Q}(x_2, y_2)$ is

$$
\mathrm{PQ} = \sqrt {\left(x _ {2} - x _ {1}\right) ^ {2} + \left(y _ {2} - y _ {1}\right) ^ {2}},
$$

which is called the distance formula.

Remarks :

1. In particular, the distance of a point $\mathrm{P}(x,y)$ from the origin $\mathrm{O}(0,0)$ is given by

2. We can also write, $\mathrm{PQ} = \sqrt{\left(x_1 - x_2\right)^2 + \left(y_1 - y_2\right)^2}$. (Why?)

Example 1 : Do the points (3, 2), (-2, -3) and (2, 3) form a triangle? If so, name the type of triangle formed.

Solution : Let us apply the distance formula to find the distances PQ, QR and PR, where P(3, 2), Q(-2, -3) and R(2, 3) are the given points. We have

$$
\mathrm{PQ} = \sqrt {(3 + 2) ^ {2} + (2 + 3) ^ {2}} = \sqrt {5 ^ {2} + 5 ^ {2}} = \sqrt {5 0} = 7. 0 7 (\text {approx.})
$$

$$
\mathrm{QR} = \sqrt {(- 2 - 2) ^ {2} + (- 3 - 3) ^ {2}} = \sqrt {(- 4) ^ {2} + (- 6) ^ {2}} = \sqrt {5 2} = 7. 2 1 (\text {approx.})
$$

$$
\mathrm{PR} = \sqrt {(3 - 2) ^ {2} + (2 - 3) ^ {2}} = \sqrt {1 ^ {2} + (- 1) ^ {2}} = \sqrt {2} = 1. 4 1 (\text {approx.})
$$

Since the sum of any two of these distances is greater than the third distance, therefore, the points P, Q and R form a triangle.

Reprint 2025-26

<!-- page 5 of 14 -->

COORDINATE GEOMETRY

103

Also, $\mathrm{PQ}^2 +\mathrm{PR}^2 = \mathrm{QR}^2$ , by the converse of Pythagoras theorem, we have $\angle \mathrm{P} = 90^{\circ}$ . Therefore, PQR is a right triangle.

Example 2 : Show that the points $(1, 7), (4, 2), (-1, -1)$ and $(-4, 4)$ are the vertices of a square.

Solution : Let A(1, 7), B(4, 2), C(-1, -1) and D(-4, 4) be the given points. One way of showing that ABCD is a square is to use the property that all its sides should be equal and both its digonals should also be equal. Now,

$$
\mathrm{AB} = \sqrt {(1 - 4) ^ {2} + (7 - 2) ^ {2}} = \sqrt {9 + 2 5} = \sqrt {3 4}
$$

$$
\mathrm{BC} = \sqrt {(4 + 1) ^ {2} + (2 + 1) ^ {2}} = \sqrt {2 5 + 9} = \sqrt {3 4}
$$

$$
\mathrm{CD} = \sqrt {(- 1 + 4) ^ {2} + (- 1 - 4) ^ {2}} = \sqrt {9 + 2 5} = \sqrt {3 4}
$$

$$
\mathrm{DA} = \sqrt {(1 + 4) ^ {2} + (7 - 4) ^ {2}} = \sqrt {2 5 + 9} = \sqrt {3 4}
$$

$$
\mathrm{AC} = \sqrt {(1 + 1) ^ {2} + (7 + 1) ^ {2}} = \sqrt {4 + 6 4} = \sqrt {6 8}
$$

$$
\mathrm{BD} = \sqrt {(4 + 4) ^ {2} + (2 - 4) ^ {2}} = \sqrt {6 4 + 4} = \sqrt {6 8}
$$

Since, AB = BC = CD = DA and AC = BD, all the four sides of the quadrilateral ABCD are equal and its diagonals AC and BD are also equal. Therefore, ABCD is a square.

Alternative Solution : We find the four sides and one diagonal, say, AC as above. Here  $AD^{2} + DC^{2} = 34 + 34 = 68 = AC^{2}$ . Therefore, by the converse of Pythagoras theorem,  $\angle D = 90^{\circ}$ . A quadrilateral with all four sides equal and one angle  $90^{\circ}$  is a square. So, ABCD is a square.

Example 3 : Fig. 7.6 shows the arrangement of desks in a classroom. Ashima, Bharti and Camella are seated at A(3, 1), B(6, 4) and C(8, 6) respectively. Do you think they are seated in a line? Give reasons for your answer.

![Chart block](doc:d7eef70/tier:standard/page:5/block:15)

Fig. 7.6

Reprint 2025-26

<!-- page 6 of 14 -->

104

MATHEMATICS

Solution : Using the distance formula, we have

$$
\mathrm{AB} = \sqrt {(6 - 3) ^ {2} + (4 - 1) ^ {2}} = \sqrt {9 + 9} = \sqrt {1 8} = 3 \sqrt {2}
$$

$$
\mathrm{BC} = \sqrt {(8 - 6) ^ {2} + (6 - 4) ^ {2}} = \sqrt {4 + 4} = \sqrt {8} = 2 \sqrt {2}
$$

$$
\mathrm{AC} = \sqrt {(8 - 3) ^ {2} + (6 - 1) ^ {2}} = \sqrt {2 5 + 2 5} = \sqrt {5 0} = 5 \sqrt {2}
$$

Since, $\mathrm{AB} + \mathrm{BC} = 3\sqrt{2} + 2\sqrt{2} = 5\sqrt{2} = \mathrm{AC}$, we can say that the points A, B and C are collinear. Therefore, they are seated in a line.

Example 4 : Find a relation between $x$ and $y$ such that the point $(x, y)$ is equidistant from the points (7, 1) and (3, 5).

Solution : Let $\mathrm{P}(x,y)$ be equidistant from the points A(7, 1) and B(3, 5).

We are given that $\mathrm{AP} = \mathrm{BP}$. So, $\mathrm{AP}^2 = \mathrm{BP}^2$

i.e.,

$$
(x - 7) ^ {2} + (y - 1) ^ {2} = (x - 3) ^ {2} + (y - 5) ^ {2}
$$

i.e.,

$$
x ^ {2} - 1 4 x + 4 9 + y ^ {2} - 2 y + 1 = x ^ {2} - 6 x + 9 + y ^ {2} - 1 0 y + 2 5
$$

i.e.,

$$
x - y = 2
$$

which is the required relation.

Remark : Note that the graph of the equation x - y = 2 is a line. From your earlier studies, you know that a point which is equidistant from A and B lies on the perpendicular bisector of AB. Therefore, the graph of x - y = 2 is the perpendicular bisector of AB (see Fig. 7.7).

Example 5: Find a point on the y-axis which is equidistant from the points A(6, 5) and B(-4, 3).

![Image block](doc:d7eef70/tier:standard/page:6/block:20)

Solution : We know that a point on the y-axis is of the form  $(0, y)$ . So, let the point  $P(0, y)$  be equidistant from A and B. Then

Fig. 7.7

$$
(6 - 0) ^ {2} + (5 - y) ^ {2} = (- 4 - 0) ^ {2} + (3 - y) ^ {2}
$$

i.e.,

$$
3 6 + 2 5 + y ^ {2} - 1 0 y = 1 6 + 9 + y ^ {2} - 6 y
$$

i.e.,

$$
4 y = 3 6
$$

i.e.,

$$
y = 9
$$

Reprint 2025-26

<!-- page 7 of 14 -->

COORDINATE GEOMETRY

105

So, the required point is (0, 9).

Let us check our solution: $\mathrm{AP} = \sqrt{(6 - 0)^2 + (5 - 9)^2} = \sqrt{36 + 16} = \sqrt{52}$

$$
\mathrm{BP} = \sqrt {(- 4 - 0) ^ {2} + (3 - 9) ^ {2}} = \sqrt {1 6 + 3 6} = \sqrt {5 2}
$$

Note : Using the remark above, we see that  $(0, 9)$  is the intersection of the y-axis and the perpendicular bisector of AB.

## EXERCISE 7.1

1. Find the distance between the following pairs of points:
(i)  $(2,3),(4,1)$  (ii)  $(-5,7),(-1,3)$  (iii)  $(a,b),(-a,-b)$

2. Find the distance between the points (0, 0) and (36, 15). Can you now find the distance between the two towns A and B discussed in Section 7.2.

3. Determine if the points $(1,5),(2,3)$ and $(-2, - 11)$ are collinear.

4. Check whether $(5, -2)$, $(6, 4)$ and $(7, -2)$ are the vertices of an isosceles triangle.

5. In a classroom, 4 friends are seated at the points A, B, C and D as shown in Fig. 7.8. Champa and Chameli walk into the class and after observing for a few minutes Champa asks Chameli, "Don't you think ABCD is a square?" Chameli disagrees. Using distance formula, find which of them is correct.

6. Name the type of quadrilateral formed, if any, by the following points, and give reasons for your answer:

![Chart block](doc:d7eef70/tier:standard/page:7/block:14)

(i) $(-1, -2), (1, 0), (-1, 2), (-3, 0)$

(ii) $(-3,5),(3,1),(0,3),(-1, - 4)$

(iii) $(4,5),(7,6),(4,3),(1,2)$

Fig. 7.8

7. Find the point on the $x$-axis which is equidistant from $(2, -5)$ and $(-2, 9)$.

8. Find the values of $y$ for which the distance between the points $P(2, -3)$ and $Q(10, y)$ is 10 units.

Reprint 2025-26

<!-- page 8 of 14 -->

106

MATHEMATICS

9. If $\mathrm{Q}(0,1)$ is equidistant from $\mathrm{P}(5, -3)$ and $\mathrm{R}(x,6)$, find the values of $x$. Also find the distances QR and PR.

10. Find a relation between $x$ and $y$ such that the point $(x, y)$ is equidistant from the point $(3, 6)$ and $(-3, 4)$.

## 7.3 Section Formula

Let us recall the situation in Section 7.2. Suppose a telephone company wants to position a relay tower at P between A and B is such a way that the distance of the tower from B is twice its distance from A. If P lies on AB, it will divide AB in the ratio 1 : 2 (see Fig. 7.9). If we take A as the origin O, and 1 km as one unit on both the axis, the coordinates of B will be (36, 15). In order to know the position of the tower, we must know the coordinates of P. How do we find these coordinates?

![Image block](doc:d7eef70/tier:standard/page:8/block:7)

Let the coordinates of P be $(x, y)$. Draw perpendiculars from P and B to the $x$-axis, meeting it in D and E, respectively. Draw PC perpendicular to BE. Then, by the AA similarity criterion, studied in Chapter 6, $\Delta$ POD and $\Delta$ BPC are similar.

Therefore,  $\frac{OD}{PC}=\frac{OP}{PB}=\frac{1}{2}$ , and  $\frac{PD}{BC}=\frac{OP}{PB}=\frac{1}{2}$

So, $\frac{x}{36 - x} = \frac{1}{2}$ and $\frac{y}{15 - y} = \frac{1}{2}$.

These equations give $x = 12$ and $y = 5$.

You can check that P(12, 5) meets the condition that OP : PB = 1 : 2.

Now let us use the understanding that you may have developed through this example to obtain the general formula.

Consider any two points $\mathrm{A}(x_1, y_1)$ and $\mathrm{B}(x_2, y_2)$ and assume that $\mathrm{P}(x, y)$ divides AB internally in the ratio $m_1: m_2$, i.e., $\frac{\mathrm{PA}}{\mathrm{PB}} = \frac{m_1}{m_2}$ (see Fig. 7.10).

![Image block](doc:d7eef70/tier:standard/page:8/block:15)

Fig. 7.10

Reprint 2025-26

<!-- page 9 of 14 -->

COORDINATE GEOMETRY

107

Draw AR, PS and BT perpendicular to the $x$-axis. Draw AQ and PC parallel to the $x$-axis. Then, by the AA similarity criterion,

$$
\Delta \text {PAQ} \sim \Delta \text {BPC}
$$

Therefore,

$$
\frac {\mathrm{PA}}{\mathrm{BP}} = \frac {\mathrm{AQ}}{\mathrm{PC}} = \frac {\mathrm{PQ}}{\mathrm{BC}}\tag{1}
$$

Now,

$$
\mathrm{AQ} = \mathrm{RS} = \mathrm{OS} - \mathrm{OR} = x - x _ {1}
$$

$$
\mathrm{PC} = \mathrm{ST} = \mathrm{OT} - \mathrm{OS} = x _ {2} - x
$$

$$
\mathrm{PQ} = \mathrm{PS} - \mathrm{QS} = \mathrm{PS} - \mathrm{AR} = y - y _ {1}
$$

$$
\mathrm{BC} = \mathrm{BT-CT} = \mathrm{BT-PS} = y _ {2} - y
$$

Substituting these values in (1), we get

Taking

Similarly, taking

$$
\left\{ \begin{array}{l} \frac {m _ {1}}{m _ {2}} = \frac {x - x _ {1}}{x _ {2} - x} = \frac {y - y _ {1}}{y _ {2} - y} \\ \frac {m _ {1}}{m _ {2}} = \frac {x - x _ {1}}{x _ {2} - x}, \text {we get} x = \frac {m _ {1} x _ {2} + m _ {2} x _ {1}}{m _ {1} + m _ {2}} \\ \frac {m _ {1}}{m _ {2}} = \frac {y - y _ {1}}{y _ {2} - y}, \text {we get} y = \frac {m _ {1} y _ {2} + m _ {2} y _ {1}}{m _ {1} + m _ {2}} \end{array} \right.
$$

So, the coordinates of the point  $P(x, y)$  which divides the line segment joining the points  $A(x_{1}, y_{1})$  and  $B(x_{2}, y_{2})$ , internally, in the ratio  $m_{1}: m_{2}$  are

$$
\left(\frac {m _ {1} x _ {2} + m _ {2} x _ {1}}{m _ {1} + m _ {2}}, \frac {m _ {1} y _ {2} + m _ {2} y _ {1}}{m _ {1} + m _ {2}}\right)\tag{2}
$$

This is known as the section formula.

This can also be derived by drawing perpendiculars from A, P and B on the y-axis and proceeding as above.

If the ratio in which P divides AB is $k: 1$, then the coordinates of the point P will be

$$
\left(\frac {k x _ {2} + x _ {1}}{k + 1}, \frac {k y _ {2} + y _ {1}}{k + 1}\right).
$$

Special Case : The mid-point of a line segment divides the line segment in the ratio 1 : 1. Therefore, the coordinates of the mid-point P of the join of the points A( $x_{1}, y_{1}$ ) and B( $x_{2}, y_{2}$ ) is

$$
\left(\frac {1 \cdot x _ {1} + 1 \cdot x _ {2}}{1 + 1}, \frac {1 \cdot y _ {1} + 1 \cdot y _ {2}}{1 + 1}\right) = \left(\frac {x _ {1} + x _ {2}}{2}, \frac {y _ {1} + y _ {2}}{2}\right).
$$

Let us solve a few examples based on the section formula.

Reprint 2025-26

<!-- page 10 of 14 -->

108

MATHEMATICS

Example 6 : Find the coordinates of the point which divides the line segment joining the points $(4, -3)$ and $(8, 5)$ in the ratio $3:1$ internally.

Solution : Let $\mathrm{P}(x, y)$ be the required point. Using the section formula, we get

$$
x = \frac {3 (8) + 1 (4)}{3 + 1} = 7, y = \frac {3 (5) + 1 (- 3)}{3 + 1} = 3
$$

Therefore, (7, 3) is the required point.

Example 7 : In what ratio does the point  $(-4, 6)$  divide the line segment joining the points A(-6, 10) and B(3, -8)?

Solution : Let  $(-4, 6)$  divide AB internally in the ratio  $m_{1}: m_{2}$ . Using the section formula, we get

$$
(- 4, 6) = \left(\frac {3 m _ {1} - 6 m _ {2}}{m _ {1} + m _ {2}}, \frac {- 8 m _ {1} + 1 0 m _ {2}}{m _ {1} + m _ {2}}\right)\tag{1}
$$

Recall that if $(x,y) = (a,b)$ then $x = a$ and $y = b$.

So,

$$
- 4 = \frac {3 m _ {1} - 6 m _ {2}}{m _ {1} + m _ {2}} \text {and} 6 = \frac {- 8 m _ {1} + 1 0 m _ {2}}{m _ {1} + m _ {2}}
$$

Now,

gives us

i.e.,

$$
\begin{array}{c} - 4 = \frac {3 m _ {1} - 6 m _ {2}}{m _ {1} + m _ {2}} \\ - 4 m _ {1} - 4 m _ {2} = 3 m _ {1} - 6 m _ {2} \\ 7 m _ {1} = 2 m _ {2} \\ m _ {1}: m _ {2} = 2: 7 \end{array}
$$

i.e.,

You should verify that the ratio satisfies the $y$-coordinate also.

Now,

$$
\begin{array}{r l} \frac {- 8 m _ {1} + 1 0 m _ {2}}{m _ {1} + m _ {2}} & = \frac {- 8 \frac {m _ {1}}{m _ {2}} + 1 0}{\frac {m _ {1}}{m _ {2}} + 1} \quad (\text {Dividing throughout by} m _ {2}) \\ & = \frac {- 8 \times \frac {2}{7} + 1 0}{\frac {2}{7} + 1} = 6 \end{array}
$$

Reprint 2025-26

<!-- page 11 of 14 -->

COORDINATE GEOMETRY

109

Therefore, the point $(-4, 6)$ divides the line segment joining the points $A(-6, 10)$ and $B(3, -8)$ in the ratio $2:7$.

Alternatively : The ratio $m_1 : m_2$ can also be written as $\frac{m_1}{m_2} : 1$, or $k : 1$. Let $(-4, 6)$ divide AB internally in the ratio $k : 1$. Using the section formula, we get

$$
(- 4, 6) = \left(\frac {3 k - 6}{k + 1}, \frac {- 8 k + 1 0}{k + 1}\right)\tag{2}
$$

So,

$$
- 4 = \frac {3 k - 6}{k + 1}
$$

i.e.,

$$
- 4 k - 4 = 3 k - 6
$$

i.e.,

$$
7 k = 2
$$

i.e.,

$$
k: 1 = 2: 7
$$

You can check for the $y$-coordinate also.

So, the point $(-4, 6)$ divides the line segment joining the points $A(-6, 10)$ and $B(3, -8)$ in the ratio $2:7$.

Note : You can also find this ratio by calculating the distances PA and PB and taking their ratios provided you know that A, P and B are collinear.

Example 8 : Find the coordinates of the points of trisection (i.e., points dividing in three equal parts) of the line segment joining the points A(2, -2) and B(-7, 4).

Solution : Let P and Q be the points of trisection of AB i.e., AP = PQ = QB (see Fig. 7.11).

![Image block](doc:d7eef70/tier:standard/page:11/block:19)

Fig. 7.11

Therefore, P divides AB internally in the ratio 1 : 2. Therefore, the coordinates of P, by applying the section formula, are

$$
\left(\frac {1 (- 7) + 2 (2)}{1 + 2}, \frac {1 (4) + 2 (- 2)}{1 + 2}\right), \text {i.e.,} (- 1, 0)
$$

Now, Q also divides AB internally in the ratio 2 : 1. So, the coordinates of Q are

$$
\left(\frac {2 (- 7) + 1 (2)}{2 + 1}, \frac {2 (4) + 1 (- 2)}{2 + 1}\right), \text {i.e.,} (- 4, 2)
$$

Reprint 2025-26

<!-- page 12 of 14 -->

110

MATHEMATICS

Therefore, the coordinates of the points of trisection of the line segment joining A and B are $(-1, 0)$ and $(-4, 2)$.

Note : We could also have obtained Q by noting that it is the mid-point of PB. So, we could have obtained its coordinates using the mid-point formula.

Example 9 : Find the ratio in which the y-axis divides the line segment joining the points  $(5, -6)$  and  $(-1, -4)$ . Also find the point of intersection.

Solution : Let the ratio be $k:1$. Then by the section formula, the coordinates of the point which divides AB in the ratio $k:1$ are $\left(\frac{-k+5}{k+1},\frac{-4k-6}{k+1}\right)$.

This point lies on the $y$-axis, and we know that on the $y$-axis the abscissa is 0.

Therefore,

$$
\frac {- k + 5}{k + 1} = 0
$$

So,

$$
k = 5
$$

That is, the ratio is $5:1$. Putting the value of $k = 5$, we get the point of intersection as $\left(0, \frac{-13}{3}\right)$.

Example 10 : If the points A(6, 1), B(8, 2), C(9, 4) and D(p, 3) are the vertices of a parallelogram, taken in order, find the value of p.

Solution : We know that diagonals of a parallelogram bisect each other.

So, the coordinates of the mid-point of AC = coordinates of the mid-point of BD

i.e.,

$$
\left(\frac {6 + 9}{2}, \frac {1 + 4}{2}\right) = \left(\frac {8 + p}{2}, \frac {2 + 3}{2}\right)
$$

i.e.,

$$
\left(\frac {1 5}{2}, \frac {5}{2}\right) = \left(\frac {8 + p}{2}, \frac {5}{2}\right)
$$

SO,

$$
\frac {1 5}{2} = \frac {8 + p}{2}
$$

i.e.,

$$
p = 7
$$

Reprint 2025-26

<!-- page 13 of 14 -->

COORDINATE GEOMETRY

111

## EXERCISE 7.2

1. Find the coordinates of the point which divides the join of $(-1, 7)$ and $(4, -3)$ in the ratio $2: 3$.

2. Find the coordinates of the points of trisection of the line segment joining $(4, -1)$ and $(-2, -3)$.

3. To conduct Sports Day activities, in your rectangular shaped school ground ABCD, lines have been drawn with chalk powder at a distance of 1m each. 100 flower pots have been placed at a distance of 1m from each other along AD, as shown in Fig. 7.12. Niharika runs $\frac{1}{4}$ th the distance AD on the 2nd line and posts a green flag. Preet runs $\frac{1}{5}$ th the distance AD on the eighth line and posts a red flag. What is the distance between both the flags? If Rashmi has to post a blue flag exactly halfway between the line segment joining the two flags, where should she post her flag?

![Image block](doc:d7eef70/tier:standard/page:13/block:7)

Fig. 7.12

4. Find the ratio in which the line segment joining the points $(-3, 10)$ and $(6, -8)$ is divided by $(-1, 6)$.

5. Find the ratio in which the line segment joining $\mathrm{A}(1, - 5)$ and $\mathrm{B}(-4,5)$ is divided by the $x$-axis. Also find the coordinates of the point of division.

6. If (1, 2), (4, y), (x, 6) and (3, 5) are the vertices of a parallelogram taken in order, find x and y.

7. Find the coordinates of a point A, where AB is the diameter of a circle whose centre is $(2, -3)$ and B is $(1, 4)$.

8. If A and B are $(-2, -2)$ and $(2, -4)$, respectively, find the coordinates of P such that $AP = \frac{3}{7} AB$ and P lies on the line segment AB.

9. Find the coordinates of the points which divide the line segment joining $\mathrm{A}(-2, 2)$ and $\mathrm{B}(2, 8)$ into four equal parts.

10. Find the area of a rhombus if its vertices are  $(3, 0)$ ,  $(4, 5)$ ,  $(-1, 4)$  and  $(-2, -1)$  taken in order. [Hint: Area of a rhombus =  $\frac{1}{2}$  (product of its diagonals)]

Reprint 2025-26

<!-- page 14 of 14 -->

112

MATHEMATICS

## 7.4 Summary

In this chapter, you have studied the following points :

1. The distance between $\mathrm{P}(x_1,y_1)$ and $\mathrm{Q}(x_2,y_2)$ is $\sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$.

2. The distance of a point $\mathrm{P}(x,y)$ from the origin is $\sqrt{x^2 + y^2}$.

3. The coordinates of the point $\mathrm{P}(x,y)$ which divides the line segment joining the points $\mathrm{A}(x_1,y_1)$ and $\mathrm{B}(x_2,y_2)$ internally in the ratio $m_{1}:m_{2}$ are

$$
\left(\frac {m _ {1} x _ {2} + m _ {2} x _ {1}}{m _ {1} + m _ {2}}, \frac {m _ {1} y _ {2} + m _ {2} y _ {1}}{m _ {1} + m _ {2}}\right).
$$

4. The mid-point of the line segment joining the points $\mathrm{P}(x_1, y_1)$ and $\mathrm{Q}(x_2, y_2)$ is $\left(\frac{x_1 + x_2}{2}, \frac{y_1 + y_2}{2}\right)$.

## A NOTE TO THE READER

Section 7.3 discusses the Section Formula for the coordinates $(x, y)$ of a point P which divides internally the line segment joining the points $A(x_1, y_1)$ and $B(x_2, y_2)$ in the ratio $m_1 : m_2$ as follows:

$$
x = \frac {m _ {1} x _ {2} + m _ {2} x _ {1}}{m _ {1} + m _ {2}}, \quad y = \frac {m _ {1} y _ {2} + m _ {2} y _ {1}}{m _ {1} + m _ {2}}
$$

Note that, here, $\mathrm{PA}:\mathrm{PB} = m_1:m_2$

However, if P does not lie between A and B but lies on the line AB, outside the line segment AB, and PA: $\mathrm{PB} = m_1:m_2$, we say that P divides externally the line segment joining the points A and B. You will study Section Formula for such case in higher classes.

Reprint 2025-26