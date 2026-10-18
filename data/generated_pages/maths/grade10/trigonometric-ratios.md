---
{
  "concept": "Trigonometric Ratios",
  "slug": "trigonometric-ratios",
  "grade": 10,
  "language": "en",
  "subject": "maths",
  "area": "Trigonometry",
  "model": "sarvam-105b",
  "settings": {
    "temperature": 0.3,
    "max_tokens": 8000,
    "reasoning_effort": "none"
  },
  "usage": {
    "completion_tokens": 1846,
    "prompt_tokens": 6115,
    "total_tokens": 7961,
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
  "generated_at": "2026-10-17T22:37:23",
  "source_grade": 10,
  "grade_delta": 0,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g10_maths_chapter8_004",
      "chapter": "chapter8",
      "section": "8.2 Trigonometric Ratios"
    }
  ],
  "citation_check": {
    "cited": [
      "1"
    ],
    "invented_citations": [],
    "unused_sources": [],
    "explanatory_paragraphs_without_a_citation": 2,
    "words": 1141,
    "target_words": [
      1000,
      1350
    ],
    "untraceable_sections": 0,
    "ok": true,
    "structural_problems": []
  },
  "terms": [
    "right triangle",
    "hypotenuse",
    "opposite side",
    "adjacent side",
    "acute angle",
    "trigonometric ratios",
    "sine",
    "cosine",
    "tangent",
    "cosecant",
    "secant",
    "cotangent",
    "similar triangles",
    "pythagorean theorem"
  ]
}
---

# Trigonometric Ratios

Trigonometric ratios are special relationships between the sides of a right triangle and one of its acute angles. They allow us to connect the geometry of a triangle to the specific angle inside it. By using these ratios, we can solve problems involving unknown lengths or angles in situations ranging from building construction to navigation, making them a fundamental tool in practical mathematics.

## The Parts of a Right Triangle

To understand trigonometric ratios, we first need to identify the three sides of a right triangle relative to a chosen acute angle. Consider a right triangle $ABC$ where the right angle is at $B$. The longest side, which is always opposite the right angle, is called the hypotenuse. The side that touches our chosen acute angle, but is not the hypotenuse, is called the adjacent side. Finally, the side that faces the angle and is not the hypotenuse is called the opposite side.

If we choose angle $A$, the side $BC$ is opposite to angle $A$, and the side $AB$ is adjacent to angle $A$. However, if we switch our focus to angle $C$, the side $AB$ becomes opposite, and the side $BC$ becomes adjacent. The hypotenuse $AC$ stays the same. This means the labels for adjacent and opposite sides change depending on which acute angle you are measuring.

## The Six Trigonometric Ratios

There are six trigonometric ratios that relate the sides of a right triangle to its angles. The three primary ratios are sine, cosine, and tangent. The other three are their reciprocals.

The sine of an angle $A$ is the ratio of the length of the side opposite the angle to the length of the hypotenuse:
$$
\sin A = \frac{\text{side opposite to angle } A}{\text{hypotenuse}} = \frac{BC}{AC}
$$

The cosine of an angle $A$ is the ratio of the length of the side adjacent to the angle to the length of the hypotenuse:
$$
\cos A = \frac{\text{side adjacent to angle } A}{\text{hypotenuse}} = \frac{AB}{AC}
$$

The tangent of an angle $A$ is the ratio of the length of the side opposite the angle to the length of the side adjacent to the angle:
$$
\tan A = \frac{\text{side opposite to angle } A}{\text{side adjacent to angle } A} = \frac{BC}{AB}
$$

The remaining three ratios are the reciprocals of the primary ones. The cosecant of an angle is the reciprocal of the sine:
$$
\csc A = \frac{1}{\sin A} = \frac{\text{hypotenuse}}{\text{side opposite to angle } A} = \frac{AC}{BC}
$$

The secant of an angle is the reciprocal of the cosine:
$$
\sec A = \frac{1}{\cos A} = \frac{\text{hypotenuse}}{\text{side adjacent to angle } A} = \frac{AC}{AB}
$$

The cotangent of an angle is the reciprocal of the tangent:
$$
\cot A = \frac{1}{\tan A} = \frac{\text{side adjacent to angle } A}{\text{side opposite to angle } A} = \frac{AB}{BC}
$$

These ratios are often abbreviated as $\sin A$, $\cos A$, $\tan A$, $\csc A$, $\sec A$, and $\cot A$ respectively. It is important to remember that $\sin A$ is not the product of $\sin$ and $A$; the symbol $\sin$ separated from $A$ has no meaning on its own.

## Ratios and Similar Triangles

The value of a trigonometric ratio depends only on the angle, not on the overall size of the triangle. If you draw a right triangle and then draw a smaller or larger right triangle that shares the same angle, the ratios will be identical. This is because the triangles are similar.

For instance, if you take a point $P$ on the hypotenuse $AC$ and draw a perpendicular $PQ$ to the adjacent side $AB$, you create a new smaller right triangle. This new triangle will be similar to the original triangle by the AA similarity criterion. Because the triangles are similar, the ratios of their corresponding sides are equal, meaning the trigonometric ratios remain exactly the same.

## Finding the Other Ratios

If you know the value of one trigonometric ratio for a specific angle, you can find the values of the other five ratios. To do this, you need to find the length of the missing side. You can use the Pythagorean theorem to do this.

Suppose in a right triangle $ABC$, $\sin A = \frac{1}{3}$. This means the side opposite angle $A$ and the hypotenuse are in the ratio $1:3$. Let the opposite side be $k$, which makes the hypotenuse $3k$. To find the adjacent side, we use the Pythagorean theorem:
$$
AB^2 = AC^2 - BC^2 = (3k)^2 - (k)^2 = 8k^2
$$
Taking the square root gives the length of the adjacent side $AB = 2\sqrt{2}k$. Now we can find the other ratios:
$$
\cos A = \frac{AB}{AC} = \frac{2\sqrt{2}k}{3k} = \frac{2\sqrt{2}}{3}
$$
We can also find the reciprocal ratios by simply taking the inverse of the primary ones.

## Worked example

Let us apply this rule to find all the trigonometric ratios of an angle if we are given that $\tan A = \frac{4}{3}$.

First, we draw a right triangle and identify the sides. Since $\tan A = \frac{\text{opposite}}{\text{adjacent}}$, the opposite side is $4k$ and the adjacent side is $3k$ for some positive number $k$.

Next, we use the Pythagorean theorem to find the length of the hypotenuse:
$$
AC^2 = AB^2 + BC^2 = (3k)^2 + (4k)^2 = 9k^2 + 16k^2 = 25k^2
$$
Taking the square root gives $AC = 5k$.

Now we can calculate the primary ratios:
$$
\sin A = \frac{BC}{AC} = \frac{4k}{5k} = \frac{4}{5}
$$
$$
\cos A = \frac{AB}{AC} = \frac{3k}{5k} = \frac{3}{5}
$$

Finally, we find the reciprocal ratios by taking the inverse of the primary ones:
$$
\cot A = \frac{1}{\tan A} = \frac{1}{4/3} = \frac{3}{4}
$$
$$
\csc A = \frac{1}{\sin A} = \frac{1}{4/5} = \frac{5}{4}
$$
$$
\sec A = \frac{1}{\cos A} = \frac{1}{3/5} = \frac{5}{3}
$$

## Key points

- In a right triangle, the side opposite the angle is the side that does not touch it, while the adjacent side is the one that touches it but is not the hypotenuse.
- The six trigonometric ratios are $\sin A$, $\cos A$, $\tan A$, $\csc A$, $\sec A$, and $\cot A$.
- The reciprocal ratios are $\csc A = \frac{1}{\sin A}$, $\sec A = \frac{1}{\cos A}$, and $\cot A = \frac{1}{\tan A}$.
- The value of a trigonometric ratio is constant for a given angle, regardless of the size of the triangle, because all right triangles with the same angle are similar.
- The value of $\sin A$ or $\cos A$ is always less than or equal to 1 because the hypotenuse is always the longest side of a right triangle.