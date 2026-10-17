# Heron's Formula

You may already know how to find the area of a triangle if you know its base and its height. The formula is $\frac{1}{2} \times base \times height$. But what if you only know the lengths of the three sides, and you have no idea how tall the triangle is? Imagine you are a surveyor standing at a triangular park. You measure the three sides, but the height is hidden by a thick hedge, and you cannot easily measure it. You might think the problem is impossible. However, there is a brilliant shortcut. A mathematician named Heron discovered a way to calculate the area using only the side lengths. This is known as Heron's Formula.

## The History of Heron

Heron was born in about 10 AD, possibly in Alexandria in Egypt. He worked in applied mathematics. His works on mathematical and physical subjects are so numerous and varied that he is considered to be an encyclopedic writer in these fields [S1]. His geometrical works deal largely with problems on mensuration written in three books. Book I deals with the area of squares, rectangles, triangles, trapezoids (trapezia), various other specialised quadrilaterals, the regular polygons, circles, surfaces of cylinders, cones, spheres etc. In this book, Heron has derived the famous formula for the area of a triangle in terms of its three sides [S1]. Heron lived from 10 C.E. to 75 C.E. [S1].

## The Formula and the Semi-Perimeter

The formula given by Heron about the area of a triangle is also known as Hero's formula. It is stated as:

$$
\text{Area of a triangle} = \sqrt {s (s - a) (s - b) (s - c)}\tag{I}
$$

where $a, b$ and $c$ are the sides of the triangle, and $s = \text{semi-perimeter}$, i.e., half the perimeter of the triangle $= \frac{a + b + c}{2}$ [S1].

The semi-perimeter is simply half of the total distance around the outside of the triangle. To use the formula, you must first add up the three sides to find the perimeter, and then divide that total by two. This gives you the value of $s$. Once you have $s$, you subtract each of the three sides from $s$ one by one. This gives you three new numbers: $s - a$, $s - b$, and $s - c$. Finally, you multiply $s$ by these three new numbers, and you take the square root of the result. This gives you the area.

## Checking Your Work with a Right Triangle

Sometimes, Heron's formula can help you check if a triangle is a right triangle. A right triangle has one angle that is exactly $90^{\circ}$. In a right triangle, the longest side is called the hypotenuse. The other two sides are the legs of the triangle. If you use Heron's formula and find that the area matches the area you would get using the standard $\frac{1}{2} \times base \times height$ rule, you can confirm your side lengths are correct.

For example, suppose you have a triangular park whose sides are 40 m, 32 m, and 24 m [S1]. You can use Heron's formula to find the area. First, you find the semi-perimeter:
$s = \frac{40 + 32 + 24}{2} = 48$ m.
Next, you find the differences:
$s - a = (48 - 40) \mathrm{m} = 8 \mathrm{m}$,
$s - b = (48 - 32) \mathrm{m} = 16 \mathrm{m}$,
$s - c = (48 - 24) \mathrm{m} = 24 \mathrm{m}$.
Now, you plug these into the formula:
Area $= \sqrt{48 \times 8 \times 16 \times 24} \mathrm{m} ^ {2} = 384 \mathrm{m} ^ {2}$.
You can also check if this is a right triangle by using the Pythagorean theorem on the sides. You will see that $32^{2} + 24^{2} = 1024 + 576 = 1600 = 40^{2}$ [S1]. Therefore, the sides of the park make a right triangle. The largest side, i.e., BC which is 40 m will be the hypotenuse and the angle between the sides AB and AC will be $90^{\circ}$ [S1]. You can check that the area of the park is $\frac{1}{2} \times 32 \times 24 \, m^{2} = 384 \, m^{2}$ [S1]. We find that the area we have got is the same as we found by using Heron's formula.

## Using the Formula on Other Triangles

Heron's formula is helpful where it is not possible to find the height of the triangle easily [S1]. Let us apply it to calculate the area of an equilateral triangle with side 10 cm [S1]. For an equilateral triangle, all three sides are the same length. So, $a = b = c = 10$ cm. We have $s = \frac{10 + 10 + 10}{2}$ cm = 15 cm [S1].
HERON'S FORMULA:
$$
\begin{array}{r l}
\text{Area of triangle} & = \sqrt {1 5 (1 5 - 1 0) (1 5 - 1 0) (1 5 - 1 0)} \mathrm{cm} ^ {2} \\
& = \sqrt {1 5 \times 5 \times 5 \times 5} \mathrm{cm} ^ {2} = 2 5 \sqrt {3} \mathrm{cm} ^ {2}
\end{array}
$$
Now, let us try an isosceles triangle with unequal side as 8 cm and each equal side as 5 cm [S1]. For an isosceles triangle, two sides are the same length. So, $a = 8$ cm, $b = 5$ cm, and $c = 5$ cm. We have $s = \frac{8 + 5 + 5}{2}$ cm = 9 cm [S1].
Area of triangle $= \sqrt{9(9 - 8)(9 - 5)(9 - 5)}\mathrm{cm}^2 = \sqrt{9\times 1\times 4\times 4}\mathrm{cm}^2 = 12\mathrm{cm}^2$ [S1].

## Solving More Examples

Let us now solve some more examples to see how the formula works in everyday situations [S1].

**Example 1:** Find the area of a triangle, two sides of which are 8 cm and 11 cm and the perimeter is 32 cm [S1].
Solution: Here we have perimeter of the triangle $= {32}\mathrm{\;{cm}},a = 8\mathrm{\;{cm}}$ and $b = {11}\mathrm{\;{cm}}$ [S1]. Third side $c = 32\mathrm{cm} - (8 + 11)\mathrm{cm} = 13\mathrm{cm}$ [S1].
So, $2s = 32$, i.e., $s = 16~\mathrm{cm}$ [S1].
$s - a = (1 6 - 8) \mathrm{cm} = 8 \mathrm{cm}$,
$s - b = (1 6 - 1 1) \mathrm{cm} = 5 \mathrm{cm}$,
$s - c = (1 6 - 1 3) \mathrm{cm} = 3 \mathrm{cm}$ [S1].
Therefore, area of the triangle $= \sqrt{s(s - a)(s - b)(s - c)}$
$= \sqrt {1 6 \times 8 \times 5 \times 3} \mathrm{cm} ^ {2} = 8 \sqrt {3 0} \mathrm{cm} ^ {2}$ [S1].

**Example 2:** A triangular park ABC has sides 120m, 80m and 50m [S1]. A gardener Dhania has to put a fence all around it and also plant grass inside. How much area does she need to plant? Find the cost of fencing it with barbed wire at the rate of ₹20 per metre leaving a space 3m wide for a gate on one side [S1].
Solution: For finding area of the park, we have
$2 s = 5 0 \mathrm{m} + 8 0 \mathrm{m} + 1 2 0 \mathrm{m} = 2 5 0 \mathrm{m}$ [S1].
i.e., $s = 1 2 5 \mathrm{m}$ [S1].
Now,
$s - a = (1 2 5 - 1 2 0) \mathrm{m} = 5 \mathrm{m}$,
$s - b = (1 2 5 - 8 0) \mathrm{m} = 4 5 \mathrm{m}$,
$s - c = (1 2 5 - 5 0) \mathrm{m} = 7 5 \mathrm{m}$ [S1].
Therefore, area of the park = $\sqrt{s(s - a)(s - b)(s - c)}$ = $\sqrt{125 \times 5 \times 45 \times 75} \mathrm{~m}^2$ = $375 \sqrt{15} \mathrm{~m}^2$ [S1].
Also, perimeter of the park = AB + BC + CA = 250 m [S1].
Therefore, length of the wire needed for fencing = 250 m - 3 m (to be left for gate) = 247 m [S1].
And so the cost of fencing = ₹20 × 247 = ₹4940 [S1].

**Example 3:** The sides of a triangular plot are in the ratio of 3 : 5 : 7 and its perimeter is 300 m. Find its area [S1].
Solution: Suppose that the sides, in metres, are $3x$, $5x$ and $7x$ [S1]. Then, we know that $3x + 5x + 7x = 300$ (perimeter of the triangle) [S1].
Therefore, $15x = 300$, which gives $x = 20$ [S1].
So the sides of the triangle are $3 \times 20 \mathrm{~m}$, $5 \times 20 \mathrm{~m}$ and $7 \times 20 \mathrm{~m}$ i.e., $60\mathrm{m}$, $100\mathrm{m}$ and $140\mathrm{m}$ [S1].
We have $s = \frac{60 + 100 + 140}{2}$ m = 150 m [S1].
and area will be $\sqrt{150(150 - 60)(150 - 100)(150 - 140)}\mathrm{m}^2$ [S1].
$= \sqrt{150\times 90\times 50\times 10}\mathrm{m}^2$ [S1].
$= 1500\sqrt{3}\mathrm{m}^2$ [S1].

## Worked Example

Let us try a new problem to practice. Imagine you are buying a triangular plot of land to build a small house. You measure the three sides of the plot, and you find they are 7 cm, 24 cm, and 25 cm. You do not have a tool to measure the height directly, so you decide to use Heron's formula.

First, you need to find the semi-perimeter, $s$. You add up the three sides: $7 + 24 + 25 = 56$ cm. Then you divide by two to find $s$: $s = \frac{56}{2} = 28$ cm.

Next, you find the differences between $s$ and each side.
$s - a = 28 - 7 = 21$ cm.
$s - b = 28 - 24 = 4$ cm.
$s - c = 28 - 25 = 3$ cm.

Now, you plug these values into Heron's formula.
Area $= \sqrt{s(s - a)(s - b)(s - c)}$
Area $= \sqrt{28 \times 21 \times 4 \times 3}$
Area $= \sqrt{7056}$
Area $= 84$ cm$^2$.

You can check if this is a right triangle by seeing if $7^2 + 24^2 = 25^2$. Indeed, $49 + 576 = 625$, which is $25^2$. So, this is a right triangle. You can also use the standard base and height formula to check your answer. If you use 24 cm as the base and 7 cm as the height, the area is $\frac{1}{2} \times 24 \times 7 = 84$ cm$^2$. The answers match perfectly.

## Key points

*   Heron's Formula allows you to find the area of a triangle using only the lengths of its three sides.
*   The formula is Area = $\sqrt{s(s-a)(s-b)(s-c)}$, where $a, b, c$ are the sides and $s$ is the semi-perimeter.
*   The semi-perimeter is calculated as half the perimeter: $s = \frac{a + b + c}{2}$.
*   The formula is especially useful when the height of the triangle is difficult or impossible to measure.
*   You can use Heron's formula to verify if a triangle is a right triangle by comparing the area with the standard $\frac{1}{2} \times base \times height$ formula.

<!-- TERMS: Heron's Formula, semi-perimeter, scalene triangle, Heron, Alexandria, right triangle, hypotenuse, equilateral triangle, isosceles triangle, perimeter -->