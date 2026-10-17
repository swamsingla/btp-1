# Area of Triangles

Area tells us how much flat space a shape covers. We measure this space in square units, like square centimetres or square metres. Knowing the area of a triangle is very useful. You might use it to find the area of a slice of land or a piece of cloth.

## When You Do Not Know the Height

You may already know that the formula for the area of any triangle is $\frac{1}{2} \times \text{base} \times \text{height}$. This rule works perfectly when you know the height of the triangle. But what if you only know the lengths of the three sides? A famous method called Heron's formula solves this exact problem [S1].

Heron was a mathematician who lived in Alexandria, Egypt, around 10 AD to 75 AD [S1]. He worked in applied mathematics and is considered an encyclopedic writer. His geometrical works deal largely with problems on mensuration written in three books [S1]. In Book I, he derived a famous formula for the area of a triangle in terms of its three sides [S1].

The formula given by Heron about the area of a triangle is also known as Hero's formula [S1]. It is stated as:

$$
\text{Area of a triangle} = \sqrt {s (s - a) (s - b) (s - c)}
$$

where $a, b$ and $c$ are the sides of the triangle, and $s = \text{semi-perimeter}$, i.e., half the perimeter of the triangle $= \frac{a + b + c}{2}$ [S1].

This formula is very helpful where it is not possible to find the height of the triangle easily [S1]. Let us look at an example of how to use it.

## Worked example

Imagine you have a triangular park with sides measuring $40$ m, $32$ m, and $24$ m. You want to find the area of the park, but you do not know the height.

First, we need to find the semi-perimeter $s$.
$s = \frac{40 + 32 + 24}{2}$ m = $48$ m [S1].

Let us take $a = 40$ m, $b = 24$ m and $c = 32$ m. Next, we calculate the values of $s - a$, $s - b$, and $s - c$.
$s - a = (48 - 40)$ m = $8$ m [S1].
$s - b = (48 - 24)$ m = $24$ m [S1].
$s - c = (48 - 32)$ m = $16$ m [S1].

Now, we plug these values into Heron's formula to find the area.
Area of the park = $\sqrt {48 \times 8 \times 24 \times 16}$ m$^2$ [S1].

Here $48 \times 8 = 384$ and $24 \times 16 = 384$, so the product under the square root is $384 \times 384$. Its square root is $384$, so the area is $384$ m$^2$ [S1].

You can actually check this answer using the basic formula you already know! Notice that $32^2 + 24^2 = 1024 + 576 = 1600 = 40^2$ [S1]. This means the sides of the park make a right triangle. The largest side, which is $40$ m, will be the hypotenuse [S1]. The angle between the sides $32$ m and $24$ m will be $90^\circ$ [S1].

Using the basic formula, the area is $\frac{1}{2} \times 32 \times 24 \, m^{2} = 384 \, m^{2}$ [S1].

As you can see, the area we got using Heron's formula is exactly the same as the area found by using the basic formula [S1].

## Solving Ratio Problems

Sometimes, you will be given the sides of a triangle in a ratio. You can use Heron's formula to find the area in these cases too.

Suppose the sides of a triangular plot are in the ratio of $3 : 5 : 7$ and its perimeter is $300$ m [S1]. We can represent the sides as $3x$, $5x$, and $7x$ [S1].

We know that the perimeter is the sum of all sides.
$3x + 5x + 7x = 300$ [S1].
$15x = 300$, which gives $x = 20$ [S1].

So the actual sides of the triangle are $3 \times 20 \mathrm{~m}$, $5 \times 20 \mathrm{~m}$, and $7 \times 20 \mathrm{~m}$ [S1].
The sides are $60\mathrm{m}$, $100\mathrm{m}$, and $140\mathrm{m}$ [S1].

Can you now find the area using Heron's formula? [S1]

First, we find the semi-perimeter $s$.
$s = \frac{60 + 100 + 140}{2}$ m = $150$ m [S1].

Now, we apply Heron's formula.
Area = $\sqrt{150(150 - 60)(150 - 100)(150 - 140)}$ m$^2$ [S1].
Area = $\sqrt{150\times 90\times 50\times 10}$ m$^2$ [S1].
Area = $1500\sqrt{3}$ m$^2$, since $150 \times 90 \times 50 \times 10 = 6{,}750{,}000 = 1500^2 \times 3$ (about $2598$ m$^2$) [S1].

## Key points
* The basic formula for the area of any triangle is $A = \frac{1}{2} \times b \times h$.
* Heron's formula allows you to find the area of a triangle using only its three side lengths.
* Heron's formula is Area $= \sqrt {s (s - a) (s - b) (s - c)}$, where $s = \frac{a + b + c}{2}$.
* This method is useful when the height of the triangle is difficult or impossible to find.
* When sides are given in a ratio, you can find the actual side lengths by using the perimeter.

<!-- TERMS: semi-perimeter, Heron's formula, right triangle, hypotenuse -->