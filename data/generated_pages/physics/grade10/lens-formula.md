---
{
  "concept": "Lens Formula and Magnification",
  "slug": "lens-formula",
  "grade": 10,
  "language": "en",
  "subject": "physics",
  "area": "Optics",
  "model": "sarvam-105b",
  "settings": {
    "temperature": 0.3,
    "max_tokens": 8000,
    "reasoning_effort": "none"
  },
  "usage": {
    "completion_tokens": 1187,
    "prompt_tokens": 5895,
    "total_tokens": 7082,
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
  "generated_at": "2026-10-18T04:40:18",
  "source_grade": 10,
  "grade_delta": 0,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g10_science_chapter9_047",
      "chapter": "chapter9",
      "section": "9.3.7 Lens Formula and Magnification"
    },
    {
      "ref": "S2",
      "passage_id": "g10_science_chapter9_021",
      "chapter": "chapter9",
      "section": "9.2.4 Mirror Formula and Magnification"
    },
    {
      "ref": "S3",
      "passage_id": "g10_science_chapter9_050",
      "chapter": "chapter9",
      "section": "9.3.8 Power of a Lens"
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
    "words": 749,
    "target_words": [
      1000,
      1350
    ],
    "untraceable_sections": 0,
    "ok": true,
    "structural_problems": [
      "length: 749 words, under 1000"
    ]
  },
  "terms": [
    "lens formula",
    "magnification",
    "focal length",
    "object-distance",
    "image-distance",
    "power of a lens",
    "dioptre",
    "concave lens",
    "convex lens",
    "erect",
    "virtual",
    "real",
    "inverted"
  ]
}
---

# Lens Formula and Magnification

When you look through a magnifying glass to read tiny print, or when your eye doctor checks your vision with a lens, you are using the principles of refraction and magnification. Lenses are transparent objects with curved surfaces that bend light rays to form images. Understanding how a lens forms an image, where that image appears, and how large it looks is essential for designing cameras, telescopes, and eyeglasses. The relationship between the object's position, the image's position, and the lens's focal length is described by the lens formula, while the relative size of the image compared to the object is described by magnification.

## The Lens Formula

Just as there is a mathematical relationship for spherical mirrors, there is a specific formula for spherical lenses. This formula gives the relationship between object-distance $(u)$, image-distance $(v)$ and the focal length $(f)$. The lens formula is expressed as

$$
\frac {1}{v} - \frac {1}{u} = \frac {1}{f}
$$

The lens formula given above is general and is valid in all situations for any spherical lens. Take proper care of the signs of different quantities, while putting numerical values for solving problems relating to lenses. 

To use this formula, you must apply the New Cartesian Sign Convention, which means you must assign a positive or negative sign to the distance values based on their direction relative to the lens:

- All distances are measured from the optical centre of the lens.
- The object is placed to the left of the lens, so the object-distance $u$ is negative.
- Distances measured in the direction of the incident light (to the right of the lens) are positive.
- Distances measured against the direction of the incident light (to the left) are negative.
- Heights measured upwards, above the principal axis, are positive. Heights measured downwards are negative.
- The focal length $f$ of a convex lens is positive and that of a concave lens is negative.

## Magnification

The magnification produced by a lens is defined as the ratio of the height of the image and the height of the object. Magnification is represented by the letter $m$. If $h$ is the height of the object and $h'$ is the height of the image given by a lens, then the magnification produced by the lens is given by

$$
m = \frac {\text{ Height   of   the   Image }}{\text{ Height   of   the   object }} = \frac {h ^ {\prime}}{h}
$$

Magnification produced by a lens is also related to the object-distance $u$, and the image-distance $v$. This relationship is given by

$$
m = \frac{h'}{h} = \frac{v}{u}
$$

## Worked example

Consider a concave lens with a focal length of $15 \, \mathrm{cm}$. Let us place an object $30 \, \mathrm{cm}$ from the lens and find where the image forms and how large it is. For a concave lens, $f = -15 \, \mathrm{cm}$, and the object is on the left, so $u = -30 \, \mathrm{cm}$.

First, we use the lens formula to find the image-distance $v$:

$$
\frac{1}{v} = \frac{1}{f} + \frac{1}{u} = \frac{1}{-15} + \frac{1}{-30} = \frac{-2 - 1}{30} = \frac{-3}{30} = \frac{1}{-10}
$$

Thus, the image-distance is $v = -10 \, \mathrm{cm}$. The negative sign shows that the image is formed on the same side of the lens as the object, $10 \, \mathrm{cm}$ from the lens.

Next, we calculate the magnification $m$ using the relationship between $v$ and $u$:

$$
m = \frac{v}{u} = \frac{-10 \, \mathrm{cm}}{-30 \, \mathrm{cm}} = +\frac{1}{3} \approx +0.33
$$

The positive sign shows that the image is erect and virtual, and since $m$ is less than 1, the image is smaller than the object (diminished) at one-third of its height.

A second example, with a convex lens: let the focal length be $f = +10 \, \mathrm{cm}$ and the object be placed at $u = -15 \, \mathrm{cm}$. Then

$$
\frac{1}{v} = \frac{1}{f} + \frac{1}{u} = \frac{1}{10} - \frac{1}{15} = \frac{3 - 2}{30} = \frac{1}{30}
$$

so $v = +30 \, \mathrm{cm}$. The positive sign shows that the image is formed on the other side of the lens. The magnification is $m = \frac{v}{u} = \frac{+30}{-15} = -2$. The negative sign shows that the image is real and inverted, and it is twice as large as the object.

## Power of a Lens

The degree of convergence or divergence of light rays achieved by a lens is expressed in terms of its power. The power of a lens is defined as the reciprocal of its focal length. It is represented by the letter $P$. The power $P$ of a lens of focal length $f$ is given by

$$
P = \frac {1}{f}
$$

The SI unit of power of a lens is the dioptre. It is denoted by the letter D. If $f$ is expressed in metres, then power is expressed in dioptres. Thus, $1 \, \mathrm{D} = 1 \, \mathrm{m}^{-1}$. The power of a convex lens is positive and that of a concave lens is negative.

For example, a convex lens of focal length $f = +50 \, \mathrm{cm} = +0.5 \, \mathrm{m}$ has power $P = \frac{1}{0.5} = +2 \, \mathrm{D}$. In the same way, a concave lens of power $-4 \, \mathrm{D}$ has focal length $f = \frac{1}{P} = \frac{1}{-4} = -0.25 \, \mathrm{m}$, which is $-25 \, \mathrm{cm}$.

## Key points

*   The lens formula relates the object-distance $(u)$, image-distance $(v)$, and focal length $(f)$ of a spherical lens as $\frac {1}{v} - \frac {1}{u} = \frac {1}{f}$.
*   Magnification ($m$) is the ratio of the height of the image to the height of the object, $m = \frac{h'}{h}$.
*   Magnification is also the ratio of the image-distance to the object-distance, $m = \frac{v}{u}$.
*   The power of a lens is the reciprocal of its focal length, $P = \frac {1}{f}$, measured in dioptres (D).
*   The lens formula is general and valid for any spherical lens in any situation.