---
{
  "concept": "Area of Sector and Segment of a Circle",
  "slug": "area-of-sector-and-segment",
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
    "completion_tokens": 995,
    "prompt_tokens": 7067,
    "total_tokens": 8062,
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
  "generated_at": "2026-10-18T00:58:17",
  "source_grade": 10,
  "grade_delta": 0,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g10_maths_chapter11_005",
      "chapter": "chapter11",
      "section": "11.1 Areas of Sector and Segment of a Circle"
    },
    {
      "ref": "S2",
      "passage_id": "g10_maths_chapter12_006",
      "chapter": "chapter12",
      "section": "12.2 Surface Area of a Combination of Solids"
    }
  ],
  "citation_check": {
    "cited": [],
    "invented_citations": [],
    "unused_sources": [
      "1",
      "2"
    ],
    "explanatory_paragraphs_without_a_citation": 4,
    "words": 721,
    "target_words": [
      1000,
      1350
    ],
    "untraceable_sections": 4,
    "ok": false,
    "structural_problems": [
      "length: 721 words, under 1000"
    ]
  },
  "terms": [
    "sector",
    "segment",
    "radius",
    "chord",
    "arc",
    "angle of sector",
    "unitary method",
    "central angle"
  ]
}
---

# Area of Sector and Segment of a Circle

Understanding the area of sectors and segments of a circle is a fundamental skill in geometry. In everyday life, we encounter circular objects constantly, from the slices of a pizza to the curved windows in a bus. Calculating the exact area of these curved portions is essential for engineers designing roads, architects planning roundabouts, and even for students solving geometry problems. This page explains how to measure the area of these specific parts of a circle using the radius and the central angle.

## Defining the Sector of a Circle

A sector of a circle is a portion of the circular region enclosed by two radii and the corresponding arc. The angle formed by these two radii at the center of the circle is called the angle of the sector. For example, if the angle at the center is $30^{\circ}$, the sector is a small slice resembling a piece of cake. Every circle also has a major sector, which is the larger portion of the circle on the opposite side of the minor sector. The angle of this major sector is always $360^{\circ}$ minus the angle of the minor sector. When we talk about sectors, we usually mean the minor sector unless specified otherwise.

## Finding the Area of a Sector

To find the area of a sector, we use a direct proportion based on the total area of the circle. The area of a full circle is $\pi r^2$. We can think of the entire circle as a single sector with an angle of $360^{\circ}$ at the center. Using the unitary method, we can scale this down. If the angle of a sector is $1^{\circ}$, its area is $\frac{\pi r^2}{360}$. Therefore, if the angle is $\theta^{\circ}$, the area of the sector is $\frac{\theta}{360} \times \pi r^2$. This formula allows us to calculate the area of any slice of a circle, provided we know the radius and the central angle.

## Understanding the Segment of a Circle

A segment of a circle is the portion of the circular region enclosed between a chord and the corresponding arc. Unlike a sector, which is bounded by two radii, a segment is bounded by a straight line and a curve. Just like sectors, segments can be minor or major. The minor segment is the smaller area, while the major segment is the larger area. When the word segment is used without any qualifier, it refers to the minor segment.

## Calculating the Area of a Segment

The area of a segment is found by subtracting the area of a triangle from the area of a sector. Specifically, the area of a segment is the area of the corresponding sector minus the area of the triangle formed by the two radii and the chord. If the angle of the sector is $\theta$ and the radius is $r$, the area of the sector is $\frac{\theta}{360} \times \pi r^2$. The area of the triangle can be calculated using the formula $\frac{1}{2} r^2 \sin \theta$, or by other methods depending on the given information. The formula for the area of a segment is $\frac{\theta}{360} \times \pi r^2 - \text{area of} \Delta \mathrm{OAB}$.

## Worked Example

Let us apply these rules to a practical problem. Suppose we have a circle with a radius of $5 \, \text{cm}$ and a sector with a central angle of $72^{\circ}$. To find the area of this sector, we use the formula $\frac{\theta}{360} \times \pi r^2$. Substituting the values, we get $\frac{72}{360} \times \pi \times 5^2$. This simplifies to $0.2 \times 25\pi$, which equals $5\pi \, \text{cm}^2$. If we use $\pi \approx 3.14$, the area is approximately $15.7 \, \text{cm}^2$.

## Worked Example: Area of a Segment

Now let us find the area of a segment. Take a circle of radius $10 \, \text{cm}$ and let a chord AB subtend a central angle of $90^{\circ}$ at the centre O. The minor sector OAB has area $\frac{90}{360} \times \pi \times 10^2 = 25\pi \, \text{cm}^2$. With $\pi \approx 3.14$, this is $78.5 \, \text{cm}^2$.

Since the angle at O is $90^{\circ}$, the triangle OAB is a right triangle with both perpendicular sides equal to the radius, $10 \, \text{cm}$. Its area is $\frac{1}{2} \times 10 \times 10 = 50 \, \text{cm}^2$.

The area of the minor segment is therefore $78.5 - 50 = 28.5 \, \text{cm}^2$.

## Major Sector and Major Segment

The same ideas let us find the larger parts. The area of the major sector is $\pi r^2$ minus the area of the minor sector, or equivalently $\frac{360 - \theta}{360} \times \pi r^2$. In the same way, the area of the major segment is $\pi r^2$ minus the area of the minor segment. For the circle above, the whole circle has area $100\pi = 314 \, \text{cm}^2$, so the major segment has area $314 - 28.5 = 285.5 \, \text{cm}^2$.

## Key points

*   A sector is the area enclosed by two radii and an arc, and its area is $\frac{\theta}{360} \times \pi r^2$.
*   A segment is the area enclosed by a chord and an arc, and it is calculated by subtracting the area of a triangle from the area of a sector.
*   The angle of a major sector is always $360^{\circ}$ minus the angle of the minor sector.
*   The area of a major sector or major segment is $\pi r^2$ minus the area of the corresponding minor part.
*   When the term sector or segment is used alone, it refers to the minor version of that shape.