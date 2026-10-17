# Properties of Triangles

Triangles are fundamental shapes in geometry, and understanding their properties helps us solve a wide variety of mathematical problems. You may already know that a triangle has three sides, three angles, and three vertices. In this section, we will explore deeper relationships between the sides and angles of triangles, specifically focusing on the triangle inequality and the angle-side relationships. These concepts are crucial for understanding why certain triangles can or cannot exist and how the lengths of sides dictate the sizes of their opposite angles.

## The Triangle Inequality

Before we discuss the relationships between sides and angles, we must first understand the basic constraints on the lengths of a triangle's sides. Not every set of three numbers can be the lengths of the sides of a triangle. For three line segments to form a triangle, the sum of the lengths of any two sides must be greater than the length of the third side. This rule is called the triangle inequality [S3]. 

To see why this is important, imagine you are trying to build a triangular frame using three sticks. If you pick sticks of lengths 4 cm, 6 cm, and 8 cm, you can check if they will work. The sum of the two shorter sides is $4 + 6 = 10$ cm, which is greater than 8 cm. The sum of the other pairs is also greater than the remaining side. Because this condition is met, a triangle with these measurements can exist. However, if you tried to use sticks of lengths 2 cm, 3 cm, and 10 cm, the sum of the two shorter sides ($2 + 3 = 5$ cm) would be less than 10 cm, making it impossible to form a closed triangle.

## Angle-Side Relationships

A very important property of triangles connects the lengths of their sides to the sizes of their angles. If a triangle has two equal sides, then the angles opposite to those equal sides are also equal. This is known as the angle-side relationship [S1]. 

Let us say we have an isosceles triangle where two sides are equal. For example, if $\Delta$ ABC has $AB = AC$, then the angles opposite these sides, $\angle B$ and $\angle C$, must be equal. This result can be proved by drawing the bisector of $\angle A$ and letting it intersect the base $BC$ at a point $D$. In $\Delta$ BAD and $\Delta$ CAD, we have $AB = AC$, $\angle BAD = \angle CAD$, and $AD = AD$ (common). By the SAS congruence rule, $\Delta BAD \cong \Delta CAD$, which means $\angle ABD = \angle ACD$, so $\angle B = \angle C$ [S1].

This property also tells us something about equilateral triangles. Since all three sides are equal, all three angles must be equal. We know that the sum of the angles in any triangle is $180^{\circ}$. Therefore, if we divide $180^{\circ}$ by three, we find that each angle in an equilateral triangle measures exactly $60^{\circ}$.

## The Converse of the Angle-Side Relationship

Is the converse also true? That is: If two angles of any triangle are equal, can we conclude that the sides opposite to them are also equal? Yes, we can [S1]. 

To see why, imagine you construct a triangle $ABC$ with $BC$ of any length and $\angle B = \angle C = 50^{\circ}$. If you draw the bisector of $\angle A$ and let it intersect $BC$ at $D$, and then cut out the triangle from a sheet of paper and fold it along $AD$ so that vertex $C$ falls on vertex $B$, you will observe that side $AC$ covers side $AB$ completely. This means $AC = AB$ [S1]. 

This proves that the sides opposite to equal angles of a triangle are equal. This is the converse of the previous theorem. You can prove this theorem by the ASA congruence rule. This relationship is very useful for solving problems where you need to prove that a triangle is isosceles.

## Worked Example

Let us apply these results to a problem. Suppose we have a triangle $ABC$ where the bisector $AD$ of $\angle A$ is perpendicular to side $BC$. We need to show that $AB = AC$ and that $\Delta ABC$ is an isosceles triangle [S1].

We can prove this by considering $\Delta ABD$ and $\Delta ACD$. In these two triangles, we have $\angle BAD = \angle CAD$ (since $AD$ is the bisector), $AD = AD$ (common), and $\angle ADB = \angle ADC = 90^{\circ}$. By the ASA congruence rule, $\Delta ABD \cong \Delta ACD$. Therefore, $AB = AC$, which means $\Delta ABC$ is an isosceles triangle [S1].

## Key points

*   The sum of the lengths of any two sides of a triangle must be greater than the length of the third side (triangle inequality).
*   If a triangle has two equal sides, the angles opposite those sides are equal.
*   If two angles of a triangle are equal, the sides opposite to them are also equal.
*   In an equilateral triangle, all three sides are equal, so all three angles are equal to $60^{\circ}$.
*   If the bisector of an angle in a triangle is perpendicular to the opposite side, the triangle is isosceles.

<!-- TERMS: triangle inequality, isosceles triangle, angle bisector, perpendicular, ASA congruence rule, SAS congruence rule, equilateral triangle, vertices -->