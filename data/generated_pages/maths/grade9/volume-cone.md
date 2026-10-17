---
{
  "concept": "Volume of Cone",
  "slug": "volume-cone",
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
    "completion_tokens": 1272,
    "prompt_tokens": 5824,
    "total_tokens": 7096,
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
  "generated_at": "2026-10-17T14:34:04",
  "source_grade": 9,
  "grade_delta": 0,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g9_maths_chapter11_015",
      "chapter": "chapter11",
      "section": "11.3 Volume of a Right Circular Cone"
    },
    {
      "ref": "S2",
      "passage_id": "g9_maths_chapter11_003",
      "chapter": "chapter11",
      "section": "11.1 Surface Area of a Right Circular Cone"
    }
  ],
  "citation_check": {
    "cited": [
      "1",
      "2"
    ],
    "invented_citations": [],
    "unused_sources": [],
    "explanatory_paragraphs_without_a_citation": 4,
    "words": 945,
    "target_words": [
      1000,
      1350
    ],
    "untraceable_sections": 4,
    "ok": false,
    "structural_problems": []
  },
  "terms": [
    "right circular cone",
    "vertex",
    "height",
    "base radius",
    "slant height",
    "volume"
  ]
}
---

# Volume of Cone

You may already know how to find the volume of a cuboid or a cylinder. A cone is another common three-dimensional shape that you encounter every day, such as a traffic cone or a party hat. Understanding the volume of a cone is important because it allows us to calculate exactly how much space is inside these pointed objects. This page will explain exactly what a cone is, how to measure its parts, and how to calculate its volume using a simple formula.

## What is a Right Circular Cone?

A right circular cone is a solid shape that has a flat, round base and a single pointed top, which is called the vertex. If you imagine spinning a right-angled triangle around one of the two sides that meet at the right angle, you will get a right circular cone. The height of the cone is the straight distance from the vertex down to the very centre of the round base. The base radius is the distance from the centre of the base to the edge of the round base. The slant height is the distance measured along the curved side of the cone, from the edge of the base up to the vertex. In this chapter, whenever the word "cone" is used, it always refers to a right circular cone.

## The Relationship Between a Cone and a Cylinder

To find the volume of a cone, we can use a very practical experiment that involves comparing it to a cylinder. Imagine that you have a right circular cylinder and a right circular cone that share the exact same base radius and the exact same height. If you fill the cone completely with sand and pour that sand into the cylinder, the cylinder will only fill up partially. If you fill the cone with sand a second time and pour it into the cylinder, the cylinder will still not be full. However, if you fill the cone for a third time and pour the sand into the cylinder, the cylinder will be completely full to the brim. This experiment shows us that it takes exactly three cones to fill a cylinder of the same base radius and height. Therefore, the volume of a cone is exactly one-third of the volume of a cylinder that has the same base radius and height.

## The Formula for Volume

Because the volume of a cone is one-third of the volume of a cylinder, we can easily write down a formula for it. The volume of a cylinder is given by the base area multiplied by the height, which is $\pi r^2 h$. Since a cone holds exactly one-third of that space, the formula for the volume of a cone is:
$$ V = \frac{1}{3}\pi r^2 h $$
Here, $r$ represents the base radius of the cone, and $h$ represents the height of the cone. It is very important to use the correct height in this formula. You must use the perpendicular height measured straight down from the vertex to the centre of the base, and not the slant height.

## Using the Formula with Slant Height

Sometimes, a question might give you the slant height of a cone instead of the height. The slant height is the distance measured along the curved surface from the edge of the base up to the vertex. If you are given the slant height, you cannot use it directly in the volume formula. Instead, you must first calculate the height using the Pythagorean theorem. The relationship between the height, base radius, and slant height is given by the rule $l^2 = r^2 + h^2$, where $l$ is the slant height, $r$ is the base radius, and $h$ is the height. You can rearrange this rule to find the height by writing $h = \sqrt{l^2 - r^2}$. Once you have found the height, you can substitute that value into the volume formula to find your final answer.

## Worked example

Let us look at a worked example to see how this all fits together. Suppose we have a cone with a height of $21$ cm and a slant height of $28$ cm. We need to find the volume of this cone. First, we must find the base radius using the rule $l^2 = r^2 + h^2$. Substituting the given values, we get $r = \sqrt{28^2 - 21^2}$ cm. This simplifies to $r = \sqrt{784 - 441}$ cm, which means $r = \sqrt{343}$ cm, or $r = 7\sqrt{7}$ cm. Now that we have the base radius, we can use the volume formula $V = \frac{1}{3}\pi r^2 h$. Substituting our values, we get $V = \frac{1}{3} \times \frac{22}{7} \times (7\sqrt{7})^2 \times 21$ cm$^3$. Simplifying the squared term gives $49 \times 7 = 343$. So the equation becomes $V = \frac{1}{3} \times \frac{22}{7} \times 343 \times 21$ cm$^3$. Multiplying this out, we find that the volume of the cone is $7546$ cm$^3$.

## A Second Example with Whole Numbers

Take a cone with base radius $r = 6$ cm and slant height $l = 10$ cm. The question gives the slant height, so we first find the height: $h = \sqrt{l^2 - r^2} = \sqrt{100 - 36} = \sqrt{64} = 8$ cm.

Now the volume is $V = \frac{1}{3}\pi r^2 h = \frac{1}{3} \times \pi \times 36 \times 8 = 96\pi$ cm$^3$. With $\pi = 3.14$, this is $96 \times 3.14 = 301.44$ cm$^3$.

We can check this against the cylinder. A cylinder with the same base radius $6$ cm and height $8$ cm has volume $\pi r^2 h = \pi \times 36 \times 8 = 288\pi$ cm$^3$. One-third of $288\pi$ is $96\pi$, which matches the cone. Notice that if we had wrongly used the slant height $10$ cm in place of the height, we would have got $\frac{1}{3}\pi \times 36 \times 10 = 120\pi$ cm$^3$, which is too large.

## Key points
* A right circular cone has a round base, a vertex, a height, a base radius, and a slant height.
* The volume of a cone is exactly one-third of the volume of a cylinder that has the same base radius and height.
* The formula for the volume of a cone is $V = \frac{1}{3}\pi r^2 h$.
* If the slant height is given, use $l^2 = r^2 + h^2$ to find the height before using the volume formula.
* Always use the perpendicular height $h$ in the volume formula, never the slant height $l$.