---
{
  "concept": "Area of Triangles",
  "slug": "area-of-triangles",
  "grade": 8,
  "language": "en",
  "hand_edited": "2026-10-13: page said 'in Grade 9 you will learn Heron's formula' and then taught it -> reworded; dangling 'in these fields'; a,b,c labels stated; square-root and 1500*sqrt3 steps shown (6,750,000 = 1500^2 x 3, about 2598). Arithmetic checked by hand: all correct. Verifier verdict 'spiralled'; source grade is 9 (Heron's formula is a Grade 9 topic).",
  "subject": "maths",
  "area": "Mensuration",
  "model": "sarvam-105b",
  "settings": {
    "temperature": 0.3,
    "max_tokens": 8000,
    "reasoning_effort": "none"
  },
  "usage": {
    "completion_tokens": 1433,
    "prompt_tokens": 7988,
    "total_tokens": 9421,
    "completion_tokens_details": {
      "accepted_prediction_tokens": null,
      "audio_tokens": null,
      "reasoning_tokens": 0,
      "rejected_prediction_tokens": null
    },
    "prompt_tokens_details": null
  },
  "target_words": [
    950,
    1300
  ],
  "generated_at": "2026-10-13T22:57:54",
  "source_grade": 9,
  "grade_delta": 1,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g9_maths_chapter10_000",
      "chapter": "chapter10",
      "section": "10.1 Area of a Triangle — by Heron's Formula"
    },
    {
      "ref": "S2",
      "passage_id": "g9_maths_chapter11_003",
      "chapter": "chapter11",
      "section": "11.1 Surface Area of a Right Circular Cone"
    },
    {
      "ref": "S3",
      "passage_id": "g9_maths_chapter7_000",
      "chapter": "chapter7",
      "section": "7.1 Introduction"
    }
  ],
  "citation_check": {
    "cited": [
      "1"
    ],
    "invented_citations": [],
    "unused_sources": [
      "2",
      "3"
    ],
    "explanatory_paragraphs_without_a_citation": 0,
    "words": 833,
    "target_words": [
      950,
      1300
    ],
    "untraceable_sections": 0,
    "ok": true,
    "structural_problems": [],
    "verification": {
      "verdict": "spiralled",
      "checks": 1,
      "tokens": 9587
    }
  },
  "terms": [
    "semi-perimeter",
    "heron's formula",
    "right triangle",
    "hypotenuse"
  ]
}
---

# Area of Triangles

Area tells us how much flat space a shape covers. We measure this space in square units, like square centimetres or square metres. Knowing the area of a triangle is very useful. You might use it to find the area of a slice of land or a piece of cloth.

## When You Do Not Know the Height

You may already know that the formula for the area of any triangle is $\frac{1}{2} \times \text{base} \times \text{height}$. This rule works perfectly when you know the height of the triangle. But what if you only know the lengths of the three sides? A famous method called Heron's formula solves this exact problem.

Heron was a mathematician who lived in Alexandria, Egypt, around 10 AD to 75 AD. He worked in applied mathematics and is considered an encyclopedic writer. His geometrical works deal largely with problems on mensuration written in three books. In Book I, he derived a famous formula for the area of a triangle in terms of its three sides.

The formula given by Heron about the area of a triangle is also known as Hero's formula. It is stated as:

$$
\text{Area of a triangle} = \sqrt {s (s - a) (s - b) (s - c)}
$$

where $a, b$ and $c$ are the sides of the triangle, and $s = \text{semi-perimeter}$, i.e., half the perimeter of the triangle $= \frac{a + b + c}{2}$.

This formula is very helpful where it is not possible to find the height of the triangle easily. Let us look at an example of how to use it.

## Worked example

Imagine you have a triangular park with sides measuring $40$ m, $32$ m, and $24$ m. You want to find the area of the park, but you do not know the height.

First, we need to find the semi-perimeter $s$.
$s = \frac{40 + 32 + 24}{2}$ m = $48$ m.

Let us take $a = 40$ m, $b = 24$ m and $c = 32$ m. Next, we calculate the values of $s - a$, $s - b$, and $s - c$.
$s - a = (48 - 40)$ m = $8$ m.
$s - b = (48 - 24)$ m = $24$ m.
$s - c = (48 - 32)$ m = $16$ m.

Now, we plug these values into Heron's formula to find the area.
Area of the park = $\sqrt {48 \times 8 \times 24 \times 16}$ m$^2$.

Here $48 \times 8 = 384$ and $24 \times 16 = 384$, so the product under the square root is $384 \times 384$. Its square root is $384$, so the area is $384$ m$^2$.

You can actually check this answer using the basic formula you already know! Notice that $32^2 + 24^2 = 1024 + 576 = 1600 = 40^2$. This means the sides of the park make a right triangle. The largest side, which is $40$ m, will be the hypotenuse. The angle between the sides $32$ m and $24$ m will be $90^\circ$.

Using the basic formula, the area is $\frac{1}{2} \times 32 \times 24 \, m^{2} = 384 \, m^{2}$.

As you can see, the area we got using Heron's formula is exactly the same as the area found by using the basic formula.

## Solving Ratio Problems

Sometimes, you will be given the sides of a triangle in a ratio. You can use Heron's formula to find the area in these cases too.

Suppose the sides of a triangular plot are in the ratio of $3 : 5 : 7$ and its perimeter is $300$ m. We can represent the sides as $3x$, $5x$, and $7x$.

We know that the perimeter is the sum of all sides.
$3x + 5x + 7x = 300$.
$15x = 300$, which gives $x = 20$.

So the actual sides of the triangle are $3 \times 20 \mathrm{~m}$, $5 \times 20 \mathrm{~m}$, and $7 \times 20 \mathrm{~m}$.
The sides are $60\mathrm{m}$, $100\mathrm{m}$, and $140\mathrm{m}$.

Can you now find the area using Heron's formula?

First, we find the semi-perimeter $s$.
$s = \frac{60 + 100 + 140}{2}$ m = $150$ m.

Now, we apply Heron's formula.
Area = $\sqrt{150(150 - 60)(150 - 100)(150 - 140)}$ m$^2$.
Area = $\sqrt{150\times 90\times 50\times 10}$ m$^2$.
Area = $1500\sqrt{3}$ m$^2$, since $150 \times 90 \times 50 \times 10 = 6{,}750{,}000 = 1500^2 \times 3$ (about $2598$ m$^2$).

## Key points
* The basic formula for the area of any triangle is $A = \frac{1}{2} \times b \times h$.
* Heron's formula allows you to find the area of a triangle using only its three side lengths.
* Heron's formula is Area $= \sqrt {s (s - a) (s - b) (s - c)}$, where $s = \frac{a + b + c}{2}$.
* This method is useful when the height of the triangle is difficult or impossible to find.
* When sides are given in a ratio, you can find the actual side lengths by using the perimeter.