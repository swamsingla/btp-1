---
{
  "concept": "Surface Area of Cone",
  "slug": "surface-area-cone",
  "grade": 9,
  "language": "en",
  "subject": "maths",
  "area": "Mensuration",
  "model": "sarvam-105b",
  "settings": {
    "temperature": 0.3,
    "max_tokens": 8000,
    "reasoning_effort": "none"
  },
  "usage": {
    "completion_tokens": 1117,
    "prompt_tokens": 4693,
    "total_tokens": 5810,
    "completion_tokens_details": {
      "accepted_prediction_tokens": null,
      "audio_tokens": null,
      "reasoning_tokens": 0,
      "rejected_prediction_tokens": null
    },
    "prompt_tokens_details": null
  },
  "target_words": [
    1000,
    1350
  ],
  "generated_at": "2026-10-17T14:33:41",
  "source_grade": 9,
  "grade_delta": 0,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g9_maths_chapter11_000",
      "chapter": "chapter11",
      "section": "11.1 Surface Area of a Right Circular Cone"
    }
  ],
  "citation_check": {
    "cited": [
      "1"
    ],
    "invented_citations": [],
    "unused_sources": [],
    "explanatory_paragraphs_without_a_citation": 0,
    "words": 780,
    "target_words": [
      1000,
      1350
    ],
    "untraceable_sections": 0,
    "ok": true,
    "structural_problems": [
      "length: 780 words, under 1000"
    ]
  },
  "terms": [
    "vertex",
    "height",
    "radius",
    "slant height",
    "curved surface area",
    "total surface area",
    "right circular cone",
    "pythagorean theorem"
  ]
}
---

# Surface Area of Cone

You may already know how to find the surface area of a cylinder or a cube. In this section, we will look at the cone. A cone is a shape you see every day. It is the shape of an ice cream cone or a traffic cone. Knowing how to find the surface area of a cone helps us figure out how much material is needed to make these objects.

## Understanding the Cone

A right circular cone is a solid with a circular base and a pointed top. The pointed top is called the vertex. The distance from the vertex straight down to the center of the base is called the height, and it is denoted by $h$. The distance from the center of the base to the edge is called the radius, denoted by $r$. The distance from the vertex down to the edge of the base is called the slant height, denoted by $l$. In this chapter, whenever we say the word "cone," we mean a right circular cone.

## The Curved Surface Area

Imagine you have a paper cone. You can cut it straight down the side and open it up. The paper you get is a curved piece. It looks like a slice of a round cake. If you cut this paper into hundreds of tiny pieces, each piece is almost a small triangle. The height of each small triangle is the slant height $l$. 

The area of one small triangle is $\frac{1}{2} \times \text{base} \times l$. To find the area of the whole curved paper, you add up the areas of all these tiny triangles. This gives you $\frac{1}{2} \times l \times (\text{sum of all the bases})$. The sum of all the bases makes up the curved boundary of the paper. This curved boundary is exactly the circumference of the circular base of the cone, which is $2\pi r$. 

So when the cone is opened out, the flat piece is part of a circle. Its radius is the slant height $l$, because every point on its curved edge was at distance $l$ from the vertex. Its curved edge has length $2\pi r$, because it wrapped around the base. Do not confuse the two radii: the circle that forms the base has radius $r$, while the opened-out piece has radius $l$.

Therefore, the curved surface area of the cone is $\frac{1}{2} \times l \times 2\pi r$, which simplifies to $\pi r l$. Here, $r$ is the base radius and $l$ is the slant height. You can also find the slant height using the height and the radius. By applying the Pythagorean Theorem, $l^{2}=r^{2}+h^{2}$, which means $l = \sqrt{r^2 + h^2}$.

## The Total Surface Area

Sometimes, you need to cover the entire outside of the cone. This includes the curved part and the flat circular base. To find the total surface area, you add the curved surface area to the area of the base. The area of the base is $\pi r^{2}$. 

So, the total surface area of a cone is $\pi r l + \pi r^{2}$. You can factor out $\pi r$ to get $\pi r(l + r)$. This formula gives you the total outside area of the cone.

## Worked Example

Let us use these formulas to solve a problem. Imagine you have a party hat shaped like a cone. The hat has a height of $8$ cm and a base radius of $6$ cm. You want to know how much colored paper is needed to cover the outside of the hat.

First, you need to find the slant height $l$. Using the Pythagorean Theorem, $l = \sqrt{r^2 + h^2}$. Substituting the values, $l = \sqrt{6^2 + 8^2} = \sqrt{36 + 64} = \sqrt{100} = 10$ cm.

Next, you find the curved surface area using the formula $\pi r l$. Substituting the values, the curved surface area is $\pi \times 6 \times 10 = 60\pi$ square cm.

If you wanted to cover the base of the hat as well, you would add the area of the base, which is $\pi r^{2} = \pi \times 6^2 = 36\pi$ square cm. The total surface area would then be $60\pi + 36\pi = 96\pi$ square cm.

## A Second Example: Using the Numbers

Now let us put in a value for $\pi$. Take a cone with base radius $r = 7$ cm and slant height $l = 25$ cm, and use $\pi = \frac{22}{7}$.

The curved surface area is $\pi r l = \frac{22}{7} \times 7 \times 25 = 22 \times 25 = 550$ square cm.

The base area is $\pi r^{2} = \frac{22}{7} \times 7 \times 7 = 154$ square cm, so the total surface area is $550 + 154 = 704$ square cm. You get the same answer from the combined formula: $\pi r(l + r) = \frac{22}{7} \times 7 \times (25 + 7) = 22 \times 32 = 704$ square cm.

This cone has height $h$ with $l^{2} = r^{2} + h^{2}$, so $h^{2} = 25^{2} - 7^{2} = 625 - 49 = 576$, and $h = 24$ cm. Knowing any two of $r$, $h$ and $l$ lets you find the third with the Pythagorean Theorem.

## Key points

*   A cone has a circular base, a vertex, a height $h$, a radius $r$, and a slant height $l$.
*   The curved surface area of a cone is given by the formula $\text{CSA} = \pi r l$.
*   The total surface area of a cone is given by the formula $\text{TSA} = \pi r(r+l)$.
*   The slant height $l$ can be calculated using the Pythagorean Theorem as $l = \sqrt{r^2 + h^2}$.
*   When a cone is cut open, the curved surface becomes a piece of a circle whose radius is the slant height $l$ and whose curved edge has length $2\pi r$.
*   The base of a cone is a circle, so its area is $\pi r^{2}$.