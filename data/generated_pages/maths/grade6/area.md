---
{
  "concept": "Area of 2D Figures",
  "slug": "area",
  "grade": 6,
  "language": "en",
  "prior_knowledge_fix": "2026-10-13: removed or rewrote an unsupported claim about what the student has already studied; edited directly in the tagged copy and the published copy",
  "subject": "maths",
  "area": "Mensuration",
  "model": "sarvam-105b",
  "settings": {
    "temperature": 0.3,
    "max_tokens": 8000,
    "reasoning_effort": "none"
  },
  "usage": {
    "completion_tokens": 1164,
    "prompt_tokens": 3198,
    "total_tokens": 4362,
    "completion_tokens_details": null,
    "prompt_tokens_details": null
  },
  "target_words": [
    700,
    1250
  ],
  "generated_at": "2026-10-02T19:26:50",
  "source_grade": 6,
  "grade_delta": 0,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g6_maths_chapter6_023",
      "chapter": "chapter6",
      "section": "6.2 Area"
    },
    {
      "ref": "S2",
      "passage_id": "g6_maths_chapter6_029",
      "chapter": "chapter6",
      "section": "6.3 Area of a Triangle"
    },
    {
      "ref": "S3",
      "passage_id": "g6_maths_chapter6_000",
      "chapter": "chapter6",
      "section": "6.1 Perimeter"
    }
  ],
  "citation_check": {
    "cited": [
      "1",
      "2",
      "3"
    ],
    "invented_citations": [],
    "unused_sources": [],
    "explanatory_paragraphs_without_a_citation": 0,
    "words": 968,
    "target_words": [
      700,
      1250
    ],
    "untraceable_sections": 0,
    "ok": true,
    "structural_problems": []
  },
  "terms": [
    "area",
    "closed figure",
    "square grid paper",
    "rectangle",
    "square",
    "triangle",
    "diagonal",
    "polygon",
    "perimeter",
    "length",
    "breadth",
    "side"
  ],
  "hand_edited": "2026-10-02: the page claimed a triangle has half the area of any rectangle it fits inside, 'regardless of the rectangle's dimensions', and repeated it in Key points. That is false; half requires a shared base and height. Both places corrected and the textbook colour references removed. Not regenerated. Grade 6 word band recalibrated from 900-1250 to 700-1250 on 2026-10-02 after two full runs showed the model never reaches 900 for these concepts (see the comment on GRADE_WORDS in build_context.py); this page kept its text and had its recorded band updated to the new standard. Source tags added on 2026-10-02 by the generator's repair stage (build_context.render_repair), which annotates an existing page instead of rewriting it, so the hand corrections above were preserved; the tagged copy is in data/intermediate/generated_tagged and the published text carries no tags."
}
---

# Area of 2D Figures

Area is a measure of the space inside a two-dimensional shape. When we talk about the area of a closed plane figure, we are measuring the exact amount of region enclosed by its boundaries. This concept is incredibly useful in everyday life, helping us determine how much paint is needed for a wall, how much grass seed to buy for a lawn, or how much floor space is left uncovered by a rug.

## The Basics of Area

You may already know how to calculate the area of some basic shapes. For a square, the area is found by multiplying the length of one side by itself, or the length times the width. For a rectangle, the area is the product of its length and its width. These formulas are the foundation for understanding more complex plane figures.

## Area of Rectangles and Squares

Let's recall the formulas for these fundamental shapes. The area of a square is calculated by multiplying the length of one of its sides by itself. For a rectangle, the area is the product of its length and its width.

To see how this works in a real-world scenario, imagine you are decorating a room. Suppose a floor is 5 m long and 4 m wide. You lay a square carpet with sides of 3 m in the center of the floor. To find out how much of the floor is still visible, you first calculate the total area of the floor. Using the formula, the area of the floor is $5 \mathrm{~m} \times 4 \mathrm{~m} = 20 \mathrm{sq~m}$. Next, you calculate the area of the carpet. The area of the carpet is $3 \mathrm{~m} \times 3 \mathrm{~m} = 9 \mathrm{sq~m}$. To find the uncovered area, you subtract the carpet area from the floor area. The area of the floor that is not carpeted is $20 \mathrm{sq~m} - 9 \mathrm{sq~m} = 11 \mathrm{sq~m}$.

## Area of a Triangle

A triangle is a closed plane figure made up of three line segments. You might wonder how the area of a triangle relates to the area of a rectangle or a square. Consider a rectangle. If you draw a diagonal line from one corner to the opposite corner and cut the rectangle along that line, you will get two triangles. If you place these two triangles next to each other, you will notice that they overlap each other exactly, meaning they have the same area.

This gives us a rule, but it has to be stated carefully. A triangle has half the area of a rectangle only when the two share the same base and the same height. For example, a triangle with a base of 6 cm and a height of 4 cm has half the area of a 6 cm by 4 cm rectangle, so its area is 12 sq cm. It is not true that every triangle you can draw inside a rectangle has half the rectangle's area: a thin triangle tucked into one corner of a large rectangle covers very little of it. Half is the largest share a triangle inside a rectangle can take, and it reaches that share exactly when its base is a full side of the rectangle and its tip touches the opposite side.

## Perimeter and Area

It is important to distinguish between the area and the perimeter of a closed figure. The perimeter is the total distance covered along the boundary of a figure when you go around it once. For a polygon, which is a closed plane figure made up of line segments, the perimeter is simply the sum of the lengths of all its sides.

For example, the perimeter of a rectangle is twice the sum of its length and its breadth, or $2 \times (\text{length} + \text{breadth})$. The perimeter of a square is four times the length of one of its sides. While the perimeter measures the boundary, the area measures the space enclosed within that boundary.

## Worked Example

Let's apply the concept of area to a new situation. Imagine a piece of land that is 12 m long and 10 m wide. In each of the four corners of this land, there is a square flower bed, and each bed has a side length of 4 m. To find the area of the remaining part of the land, you first calculate the total area of the land. The area of the land is $12 \mathrm{~m} \times 10 \mathrm{~m} = 120 \mathrm{sq~m}$.

Next, you calculate the area of one flower bed. The area of one flower bed is $4 \mathrm{~m} \times 4 \mathrm{~m} = 16 \mathrm{sq~m}$. Since there are four flower beds, the total area covered by the beds is $4 \times 16 \mathrm{sq~m} = 64 \mathrm{sq~m}$.

Finally, you subtract the total area of the flower beds from the total area of the land to find the remaining area. The area of the remaining part of the land is $120 \mathrm{sq~m} - 64 \mathrm{sq~m} = 56 \mathrm{sq~m}$.

## Key points

* The area of a closed figure is the amount of region enclosed by it.
* The area of a square is the length of a side multiplied by itself.
* The area of a rectangle is the product of its length and its width.
* A triangle has half the area of a rectangle when the two share the same base and the same height — not merely because the triangle fits inside the rectangle.
* The perimeter of a figure is the total distance along its outer boundary.
