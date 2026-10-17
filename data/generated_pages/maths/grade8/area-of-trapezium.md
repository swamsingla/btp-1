---
{
  "concept": "Area of Trapezium",
  "slug": "area-of-trapezium",
  "grade": 8,
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
    "completion_tokens": 1116,
    "prompt_tokens": 6008,
    "total_tokens": 7124,
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
  "generated_at": "2026-10-12T21:18:36",
  "source_grade": 8,
  "grade_delta": 0,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g8_maths_part1_chapter4_025",
      "chapter": "chapter4",
      "section": "4.6 Kite and Trapezium"
    },
    {
      "ref": "S2",
      "passage_id": "g8_maths_part1_chapter6_017",
      "chapter": "chapter6",
      "section": "6.2 Special Cases of the Distributive Property"
    }
  ],
  "citation_check": {
    "cited": [
      "1"
    ],
    "invented_citations": [],
    "unused_sources": [
      "2"
    ],
    "explanatory_paragraphs_without_a_citation": 2,
    "words": 843,
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
      "tokens": 9332
    }
  },
  "terms": [
    "trapezium",
    "quadrilateral",
    "parallel sides",
    "isosceles trapezium",
    "perpendicular height",
    "parallelogram"
  ],
  "hand_edited": "2026-10-12: second line-by-line audit against the textbook, edited directly: removed made-up everyday examples, fixed a doubled period, height is the perpendicular distance (not 'vertical'), derivation wording (two copies make a parallelogram, the trapezium is half), added the isosceles base-angle property. 2026-10-12: hand audit: contradicted its own definition ('only one pair' vs 'at least one pair'); vague same-side angle sentence made exact."
}
---

# Area of Trapezium

A trapezium is a special type of quadrilateral with at least one pair of parallel opposite sides. Understanding how to calculate the area of this shape is a crucial skill because it allows you to measure the surface of many real-world objects. In this section, we will build on your existing knowledge of the area of a parallelogram and discover a simple, reliable formula to find the area of any trapezium.

## Understanding the Shape and Its Properties

Before we can calculate the area, we need to be absolutely clear about what a trapezium is and how its sides relate to each other. A trapezium is defined as a quadrilateral with at least one pair of parallel opposite sides. The parallel sides are traditionally called the bases, while the non-parallel sides are called the legs. When the non-parallel sides of a trapezium have the same lengths, it is given a special name: an isosceles trapezium. 

Because of its parallel sides, a trapezium shares some interesting angle properties with parallelograms. The two angles at the ends of each non-parallel side (the angles between a leg and the two bases) always add up to $180^{\circ}$. This happens because the parallel sides act like train tracks, and each non-parallel side acts like a railway crossing. When a straight line crosses two parallel tracks, the angles on the same side of the crossing add up to $180^{\circ}$. In an isosceles trapezium, the two angles at each of the parallel sides (the base angles) are also equal.

## The Area Formula

Now that we understand the shape, let us move on to finding its area. You may already know that the area of a parallelogram is calculated by multiplying its base by its height. A trapezium is very similar, but because only one pair of its sides is guaranteed to be parallel, we need to adjust our approach slightly. 

The area of a trapezium is given by the formula $\text{Area} = \frac{1}{2} \times (a + b) \times h$. In this formula, $a$ and $b$ represent the lengths of the two parallel sides, and $h$ represents the perpendicular height between them. The height is the perpendicular distance between the two parallel sides. It is crucial to remember that we use the perpendicular height, not the length of the slanted sides.

## Deriving the Formula

Why is the area half of the sum of the parallel sides times the height? There is a very neat way to visualize this. Imagine you have a trapezium. If you take an exact copy of that trapezium and rotate it by $180^{\circ}$, you can join it to the original along a non-parallel side. The two pairs of parallel sides line up, and together the two trapeziums form a parallelogram. 

The base of this new parallelogram will be the sum of the two parallel sides of the trapezium, which is $(a + b)$. The height of this new parallelogram will be exactly the same as the height of the original trapezium, $h$. Since we know the area of a parallelogram is base times height, the area of the new shape is $(a + b) \times h$. This parallelogram is made of two identical copies of the trapezium, so the original trapezium is exactly half of it. Therefore, to find the area of the original trapezium, we simply take half of the area of the new parallelogram. This gives us the formula $\frac{1}{2} \times (a + b) \times h$.

## Worked Example

To see how this formula works in practice, let us solve a problem together. Imagine you are looking at a plot of land shaped like a trapezium. The two parallel sides of the plot measure $10$ metres and $6$ metres respectively. The perpendicular height between these two parallel sides is $4$ metres. 

Using the formula $\text{Area} = \frac{1}{2} \times (a + b) \times h$, we first add the lengths of the parallel sides. $10 + 6 = 16$ metres. Next, we multiply this sum by the height. $16 \times 4 = 64$ square metres. Finally, we take half of this result because the formula requires it. $\frac{1}{2} \times 64 = 32$. Therefore, the area of the plot of land is $32$ square metres.

## Key points

* A trapezium is a quadrilateral with at least one pair of parallel opposite sides.
* The area of a trapezium is calculated using the formula $\text{Area} = \frac{1}{2} \times (a + b) \times h$.
* The height $h$ must always be the perpendicular distance between the parallel sides, not the length of the slanted sides.
* An isosceles trapezium is a special trapezium where the non-parallel sides have equal lengths.
* The area formula is derived by imagining two identical trapeziums fitting together to form a parallelogram.