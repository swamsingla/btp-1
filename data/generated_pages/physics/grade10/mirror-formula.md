---
{
  "concept": "Mirror Formula and Magnification",
  "slug": "mirror-formula",
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
    "completion_tokens": 2007,
    "prompt_tokens": 5590,
    "total_tokens": 7597,
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
  "generated_at": "2026-10-18T05:56:50",
  "source_grade": 10,
  "grade_delta": 0,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g10_science_chapter9_021",
      "chapter": "chapter9",
      "section": "9.2.4 Mirror Formula and Magnification"
    },
    {
      "ref": "S2",
      "passage_id": "g10_science_chapter9_048",
      "chapter": "chapter9",
      "section": "9.3.7 Lens Formula and Magnification"
    },
    {
      "ref": "S3",
      "passage_id": "g10_science_chapter9_017",
      "chapter": "chapter9",
      "section": "9.2.3 Sign Convention for Reflection by Spherical Mirrors"
    }
  ],
  "citation_check": {
    "cited": [
      "1",
      "3"
    ],
    "invented_citations": [],
    "unused_sources": [
      "2"
    ],
    "explanatory_paragraphs_without_a_citation": 0,
    "words": 1369,
    "target_words": [
      1000,
      1350
    ],
    "untraceable_sections": 0,
    "ok": true,
    "structural_problems": []
  },
  "terms": [
    "reflection",
    "spherical mirror",
    "object distance",
    "image distance",
    "focal length",
    "mirror formula",
    "magnification",
    "principal focus",
    "new cartesian sign convention",
    "real image",
    "virtual image",
    "concave mirror",
    "convex mirror"
  ]
}
---

# Mirror Formula and Magnification

When you look into a bathroom mirror, you see a clear reflection of your face. But how does a piece of glass with a shiny coating reflect light so as to create that image? The answer lies in a simple mathematical relationship between the mirror, the object, and the image it creates. In physics, we use two powerful tools to describe exactly what happens: the mirror formula and the concept of magnification. The mirror formula connects the distance of an object from the mirror to the distance of its image, while magnification tells us how much larger or smaller that image appears compared to the actual object. Understanding these two ideas is essential because they allow us to predict exactly where an image will form and what it will look like, which is the foundation for designing shaving mirrors, vehicle mirrors and many optical instruments.

## The Mirror Formula

To understand how images are formed, we first need to define three specific distances. The distance of the object from the pole of the mirror is called the object distance, denoted by $u$. The distance of the image from the pole of the mirror is called the image distance, denoted by $v$. Finally, the distance of the principal focus from the pole is called the focal length, denoted by $f$. These three quantities are not independent; they are linked by a fixed mathematical rule known as the mirror formula. This relationship is expressed as $\frac {1}{v} + \frac {1}{u} = \frac {1}{f}$. This formula is valid in all situations for all spherical mirrors and for all positions of the object. 

Because the mirror formula involves distances, we cannot just plug in positive numbers. We must know whether an image is real or virtual, and whether it is formed in front of or behind the mirror. This is where the New Cartesian Sign Convention comes in. According to this convention, the pole (P) of the mirror is taken as the origin (0, 0) of a coordinate system, and the principal axis is taken as the x-axis. The object is always placed to the left of the mirror, which means light from the object falls on the mirror from the left-hand side. All distances measured to the right of the origin (along the +x-axis) are taken as positive, while those measured to the left of the origin (along the -x-axis) are taken as negative. Distances measured perpendicular to and above the principal axis (along the +y-axis) are taken as positive, and distances measured below the principal axis (along the -y-axis) are taken as negative. 

Using these sign conventions, we can solve for any unknown distance. For example, if a car's rear-view mirror is convex, its focal length is positive. If a bus is located 5.00 m in front of this mirror, the object distance $u$ is $-5.00\mathrm{m}$. If the radius of curvature is 3.00 m, the focal length $f$ is $+1.50\mathrm{m}$. Using the mirror formula, we can calculate that $\frac {1}{v} = \frac {1}{1 . 5 0} + \frac {1}{5 . 0 0} = \frac {6 . 5 0}{7 . 5 0}$, which gives an image distance $v$ of $+1.15\mathrm{m}$. The positive sign tells us the image is formed behind the mirror.

## Magnification

Once we know where the image forms, we often want to know how big it is. This is where magnification comes in. Magnification gives the relative extent to which the image of an object is magnified with respect to the object size. It is expressed as the ratio of the height of the image to the height of the object, and it is usually represented by the letter $m$. If $h$ is the height of the object and $h'$ is the height of the image, then the magnification $m$ is given by the equation $m = \frac {h'}{h}$. 

However, magnification can also be calculated using the object and image distances. It can be expressed as $m = -\frac {v}{u}$. This is a very useful shortcut because it means we do not need to measure the actual heights of the object and image; we can calculate the magnification purely from the distances. 

The sign of the magnification tells us important information about the image. The height of the object is always taken to be positive as the object is usually placed above the principal axis. The height of the image should be taken as positive for virtual images, but it is to be taken as negative for real images. A negative sign in the value of the magnification indicates that the image is real, while a positive sign indicates that the image is virtual. 

Let us look at a practical example. Suppose a 4.0 cm tall object is placed 25.0 cm in front of a concave mirror with a focal length of 15.0 cm. The object distance $u$ is $-25.0\mathrm{cm}$, and the focal length $f$ is $-15.0\mathrm{cm}$. Using the mirror formula, we find that the image distance $v$ is $-37.5\mathrm{cm}$. Because $v$ is negative, the image is real and formed in front of the mirror. To find the size of the image, we use the magnification formula. The magnification is $m = -\frac{v}{u} = -\frac{-37.5}{-25.0} = -1.5$. The height of the image is $h' = m \times h = -1.5 \times 4.0\,\mathrm{cm} = -6.0\,\mathrm{cm}$. The negative sign means the image is inverted, and its size (6.0 cm) is larger than the object (4.0 cm), so the image is real, inverted and enlarged.

## Worked Example

To see how these concepts work together, let us solve a problem from scratch. Imagine an object 3.0 cm tall placed 10.0 cm in front of a concave mirror whose focal length is 8.0 cm. We want to find the position, nature, and size of the image. 

First, we identify our values. The object distance $u = -10.0\mathrm{cm}$ because the object is placed to the left of the mirror. The focal length $f = -8.0\mathrm{cm}$ because the focus of a concave mirror is to the left of the pole. We can use the mirror formula $\frac {1}{v} + \frac {1}{u} = \frac {1}{f}$ to find the image distance. Rearranging the formula gives $\frac {1}{v} = \frac {1}{f} - \frac {1}{u} = \frac {1}{-8.0} - \frac {1}{-10.0} = -\frac {1}{8} + \frac {1}{10} = \frac {-5 + 4}{40} = \frac {-1}{40}$. Therefore, $v = -40\,\mathrm{cm}$. 

Since $v$ is negative, the image is real and formed 40 cm in front of the mirror. Next, we calculate the magnification using $m = -\frac {v}{u} = -\frac {-40}{-10} = -4$. The magnification is $-4$, which means the image is 4 times larger than the object and inverted. Finally, we find the height of the image using $h' = m \times h = -4 \times 3.0 = -12\,\mathrm{cm}$. The negative sign confirms the image is inverted, and its size is 12 cm.

## Key points

- The mirror formula, $\frac {1}{v} + \frac {1}{u} = \frac {1}{f}$, relates the object distance ($u$), image distance ($v$), and focal length ($f$) for any spherical mirror.
- The New Cartesian Sign Convention requires measuring distances from the pole of the mirror, with distances to the left of the pole being negative and distances to the right being positive.
- Magnification ($m$) is the ratio of the height of the image to the height of the object ($m = \frac {h'}{h}$) and is also equal to $-\frac {v}{u}$.
- A positive magnification indicates a virtual and erect image, while a negative magnification indicates a real and inverted image.
- You must use the New Cartesian Sign Convention while substituting numerical values for $u$, $v$, $f$, and $R$ in the mirror formula for solving problems.