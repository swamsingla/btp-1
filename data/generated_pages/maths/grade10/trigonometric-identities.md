---
{
  "concept": "Trigonometric Identities",
  "slug": "trigonometric-identities",
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
    "completion_tokens": 1350,
    "prompt_tokens": 8003,
    "total_tokens": 9353,
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
  "generated_at": "2026-10-17T22:37:44",
  "source_grade": 10,
  "grade_delta": 0,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g10_maths_chapter8_022",
      "chapter": "chapter8",
      "section": "8.4 Trigonometric Identities"
    },
    {
      "ref": "S2",
      "passage_id": "g10_maths_chapter8_010",
      "chapter": "chapter8",
      "section": "8.2 Trigonometric Ratios"
    }
  ],
  "citation_check": {
    "cited": [
      "1",
      "2"
    ],
    "invented_citations": [],
    "unused_sources": [],
    "explanatory_paragraphs_without_a_citation": 6,
    "words": 1043,
    "target_words": [
      1000,
      1350
    ],
    "untraceable_sections": 0,
    "ok": true,
    "structural_problems": []
  },
  "terms": [
    "trigonometric identity",
    "trigonometric ratios",
    "sine",
    "cosine",
    "tangent",
    "secant",
    "cosecant",
    "cotangent",
    "pythagorean theorem"
  ]
}
---

# Trigonometric Identities

An identity is an equation that holds true for all possible values of its variables. In the same way, a trigonometric identity is an equation involving trigonometric ratios of an angle that is true for every value of that angle. These identities are the fundamental building blocks of trigonometry. They allow us to express one trigonometric ratio in terms of another. If we know the value of one ratio for a specific angle, we can use these identities to find the exact values of all the other ratios for that same angle.

## The Pythagorean Foundation

The most important trigonometric identities are derived directly from the Pythagorean theorem. Consider a right-angled triangle where the right angle is at vertex B. According to the Pythagorean theorem, the square of the hypotenuse is equal to the sum of the squares of the other two sides:
$$
AB^2 + BC^2 = AC^2
$$

If we divide the entire equation by $AC^2$, we get
$$
\left(\frac{AB}{AC}\right)^2 + \left(\frac{BC}{AC}\right)^2 = 1
$$
which is the same as
$$
\cos^2 A + \sin^2 A = 1
$$
This is the first fundamental identity, and it holds for every acute angle $A$.

## The Second and Third Identities

We can derive two more identities by dividing the Pythagorean equation by the square of the side adjacent to angle A, and then by the square of the side opposite to angle A.

Dividing $AB^2 + BC^2 = AC^2$ by $AB^2$ gives the second identity:
$$
1 + \tan^2 A = \sec^2 A
$$
Dividing by $BC^2$ gives the third identity:
$$
\cot^2 A + 1 = \csc^2 A
$$

## Using Identities to Find Missing Ratios

These identities are extremely useful when we need to find the exact values of trigonometric ratios. Let us say we are given that $\tan A = \frac{1}{\sqrt{3}}$. 

Using the second identity, we can find the secant of angle $A$:
$$
\sec^2 A = 1 + \tan^2 A = 1 + \frac{1}{3} = \frac{4}{3}, \quad \text{so} \quad \sec A = \frac{2}{\sqrt{3}}
$$

From the secant, we can easily find the cosine of angle $A$ by taking its reciprocal: $\cos A = \frac{\sqrt{3}}{2}$.

Finally, we can use the first identity to find the sine of angle $A$:
$$
\sin^2 A = 1 - \cos^2 A = 1 - \frac{3}{4} = \frac{1}{4}, \quad \text{so} \quad \sin A = \frac{1}{2}
$$
From this, $\csc A = 2$.

## Expressing Ratios in Terms of Sine

We can also use the first identity to write other trigonometric ratios purely in terms of the sine of an angle. If we rearrange the identity, we find that $\cos^2 A = 1 - \sin^2 A$.

Taking the square root of both sides, and remembering that $\cos A$ is positive for an acute angle, gives
$$
\cos A = \sqrt{1 - \sin^2 A}
$$

Using this, we can write
$$
\tan A = \frac{\sin A}{\sqrt{1 - \sin^2 A}}, \qquad \sec A = \frac{1}{\sqrt{1 - \sin^2 A}}
$$

## Proving More Complex Identities

These basic identities can be used to prove more complicated trigonometric equations. For instance, we can prove that
$$
\sec A \, (1 - \sin A)(\sec A + \tan A) = 1
$$

We start by writing secant and tangent in terms of sine and cosine, and then combine the last bracket into one fraction:
$$
\text{LHS} = \frac{1}{\cos A} (1 - \sin A) \left(\frac{1}{\cos A} + \frac{\sin A}{\cos A}\right) = \frac{(1 - \sin A)(1 + \sin A)}{\cos^2 A} = \frac{1 - \sin^2 A}{\cos^2 A}
$$

From the first identity, $1 - \sin^2 A = \cos^2 A$. Substituting this in, we get $\frac{\cos^2 A}{\cos^2 A} = 1 = \text{RHS}$.

## Worked example

Let us apply the identities to find the exact values of the trigonometric ratios for an acute angle $A$ where $\tan A = \frac{4}{3}$.

First, we use the second identity to find $\sec A$:
$$
\sec^2 A = 1 + \tan^2 A = 1 + \frac{16}{9} = \frac{25}{9}, \quad \text{so} \quad \sec A = \frac{5}{3}
$$

Next, we find $\cos A$ by taking the reciprocal of the secant: $\cos A = \frac{3}{5}$.

Finally, we use the first identity to find $\sin A$:
$$
\sin^2 A = 1 - \cos^2 A = 1 - \frac{9}{25} = \frac{16}{25}, \quad \text{so} \quad \sin A = \frac{4}{5}
$$

The remaining ratios are the reciprocals: $\cot A = \frac{3}{4}$ and $\csc A = \frac{5}{4}$.

## Key points

*   A trigonometric identity is an equation involving trigonometric ratios that is true for all values of the angle.
*   The three fundamental identities are $\sin^2\theta + \cos^2\theta = 1$, $1 + \tan^2\theta = \sec^2\theta$, and $1 + \cot^2\theta = \csc^2\theta$.
*   These identities can be used to express any one trigonometric ratio in terms of another.
*   They are also used to prove more complex trigonometric equations by substituting basic definitions and simplifying.
*   Note that $\tan A = \frac{\sin A}{\cos A}$ and $\cot A = \frac{\cos A}{\sin A}$, which helps in rewriting expressions.