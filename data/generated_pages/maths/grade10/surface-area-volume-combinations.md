---
{
  "concept": "Surface Area and Volume of Combined Solids",
  "slug": "surface-area-volume-combinations",
  "grade": 10,
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
    "completion_tokens": 1263,
    "prompt_tokens": 6694,
    "total_tokens": 7957,
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
  "generated_at": "2026-10-18T00:59:12",
  "source_grade": 10,
  "grade_delta": 0,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g10_maths_chapter12_005",
      "chapter": "chapter12",
      "section": "12.2 Surface Area of a Combination of Solids"
    },
    {
      "ref": "S2",
      "passage_id": "g10_maths_chapter12_010",
      "chapter": "chapter12",
      "section": "12.3 Volume of a Combination of Solids"
    },
    {
      "ref": "S3",
      "passage_id": "g10_maths_chapter12_001",
      "chapter": "chapter12",
      "section": "12.1 Introduction"
    }
  ],
  "citation_check": {
    "cited": [],
    "invented_citations": [],
    "unused_sources": [
      "1",
      "2",
      "3"
    ],
    "explanatory_paragraphs_without_a_citation": 5,
    "words": 1039,
    "target_words": [
      1000,
      1350
    ],
    "untraceable_sections": 3,
    "ok": false,
    "structural_problems": []
  },
  "terms": [
    "frustum",
    "combined solids",
    "conversion of solids",
    "curved surface area",
    "total surface area",
    "volume",
    "constituents",
    "cuboid",
    "hemisphere",
    "cylinder",
    "cone",
    "sphere",
    "slant height"
  ]
}
---

# Surface Area and Volume of Combined Solids

In our daily lives, we encounter many objects that are not simple cubes or spheres but are made by joining two or more basic solids together. These are called combined solids. To find the surface area or volume of such objects, we use a simple strategy: we break the object down into the basic solids we already know, solve for each part, and then combine the results. The exact way we combine them depends on whether we are calculating the total surface area or the volume, because surface areas can hide inside the object when the parts join, while volumes always add up.

## Combining Surface Areas of Combined Solids

When two solids are joined together to form a new shape, some of the original flat surfaces disappear inside the new object. Therefore, we cannot simply add the total surface areas of the individual parts. Instead, we must identify which surfaces are actually exposed to the outside world.

The total surface area of the new solid is the sum of the areas of the surfaces that remain exposed. Usually the joined faces are hidden, so we add the curved surface areas of the parts, but any flat face that stays exposed must be added too.

For example, if we join a cylinder with two identical hemispheres at either end, the resulting shape is like a capsule or a test tube. When we look at the outer surface of this new object, we only see the curved surface of the cylinder and the curved surfaces of the two hemispheres. The flat circular faces where the hemispheres meet the cylinder are hidden from view. Thus, the total surface area is the sum of the curved surface area of the cylinder and the curved surface areas of both hemispheres.

Similarly, if we join a cone and a hemisphere by placing their flat faces together, we create a smooth, round-bottomed toy. Its outer surface consists of the curved surface area of the hemisphere and the curved surface area of the cone, so the total surface area of the toy is the sum of these two curved surface areas.

## Combining Volumes of Combined Solids

The way we calculate volume is different from the way we calculate surface area. When we join two basic solids to form a new solid, the total volume of the new solid is the sum of the volumes of the constituents. For a cone surmounted on a hemisphere of the same radius $r$, for instance, the volume is $\frac{1}{3}\pi r^2 h + \frac{2}{3}\pi r^3$, where $h$ is the height of the cone.

## Conversion of Solids

Sometimes, a solid is melted down and reshaped into a different solid. This process is called the conversion of solids. The key rule here is that the volume of the new solid will be exactly equal to the volume of the original solid. This is because the material is simply changing its shape, not being added to or removed from.

## Worked Example

Imagine a toy rocket in the shape of a cone mounted on a cylinder. The height of the entire rocket is 26 cm, while the height of the conical part is 6 cm. The base of the conical portion has a diameter of 5 cm, while the base diameter of the cylindrical portion is 3 cm. If the conical portion is to be painted orange and the cylindrical portion yellow, find the area of the rocket painted with each of these colours.

First, we calculate the dimensions of each part. The radius of the cone is $r = 2.5$ cm, and the height of the cone is 6 cm. The radius of the cylinder is $r' = 1.5$ cm, and the height of the cylinder is $26 - 6 = 20$ cm.

Next, we find the slant height of the cone using the Pythagorean theorem:

$$ l = \sqrt{r^2 + h^2} = \sqrt{2.5^2 + 6^2} = 6.5 \text{ cm} $$

Now, we calculate the area to be painted orange. The base of the cone is larger than the top of the cylinder it rests on, so a ring-shaped part of the cone's base is also visible and has to be painted. The area to be painted orange is the curved surface area of the cone plus the area of the base of the cone, minus the area of the base of the cylinder:

$$ \pi r l + \pi r^2 - \pi r'^2 = \pi (2.5 \times 6.5 + 2.5^2 - 1.5^2) = \pi \times 20.25 $$

Using $\pi = 3.14$, the area to be painted orange is $63.585 \text{ cm}^2$.

Finally, we calculate the area to be painted yellow. This is the curved surface area of the cylinder plus the area of one base of the cylinder:

$$ 2\pi r' h' + \pi r'^2 = \pi \times 1.5 \times (2 \times 20 + 1.5) = 4.71 \times 41.5 $$

This gives an area of $195.465 \text{ cm}^2$ to be painted yellow.

## Key points

*   To find the surface area of a combined solid, identify the exposed surfaces and sum their curved surface areas.
*   When calculating volume, simply add the volumes of the individual parts to find the total volume.
*   When a solid is melted and reshaped into a new solid, the volume remains unchanged.
*   Always check if a surface is hidden inside the combined solid before adding it to the total surface area.
*   Use the correct formulas for the basic solids and substitute the given dimensions carefully.