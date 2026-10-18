---
{
  "concept": "Nature of Roots — Discriminant",
  "slug": "nature-of-roots",
  "grade": 10,
  "language": "en",
  "subject": "maths",
  "area": "Algebra",
  "model": "sarvam-105b",
  "settings": {
    "temperature": 0.3,
    "max_tokens": 8000,
    "reasoning_effort": "none"
  },
  "usage": {
    "completion_tokens": 1208,
    "prompt_tokens": 5614,
    "total_tokens": 6822,
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
  "generated_at": "2026-10-17T22:05:47",
  "source_grade": 10,
  "grade_delta": 0,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g10_maths_chapter4_013",
      "chapter": "chapter4",
      "section": "4.4 Nature of Roots"
    },
    {
      "ref": "S2",
      "passage_id": "g10_maths_chapter4_011",
      "chapter": "chapter4",
      "section": "4.3 Solution of a Quadratic Equation by Factorisation"
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
    "words": 836,
    "target_words": [
      1000,
      1350
    ],
    "untraceable_sections": 1,
    "ok": true,
    "structural_problems": [
      "length: 836 words, under 1000"
    ]
  },
  "terms": [
    "quadratic equation",
    "discriminant",
    "roots",
    "real roots",
    "distinct roots",
    "equal roots",
    "quadratic formula",
    "square root",
    "coefficients a",
    "b",
    "c"
  ]
}
---

# Nature of Roots — Discriminant

Every time you solve a quadratic equation of the form $ax^2 + bx + c = 0$, you are looking for the values of $x$ that make the equation true. Sometimes you find two different answers, sometimes you find the same answer twice, and sometimes the equation has no real answer at all. Instead of solving the whole equation every single time, you can use a special shortcut called the discriminant. The discriminant tells you exactly what kind of answers to expect before you even start calculating.

## The Quadratic Formula and the Square Root

To understand the discriminant, you first need to look at the quadratic formula. This formula gives you the roots of the equation.

$$
x = \frac {- b \pm \sqrt {b ^ {2} - 4 a c}}{2 a}
$$

The most important part of this formula for our discussion is the square root: $\sqrt{b^2 - 4ac}$. You already know that you can only take the square root of a number that is zero or positive and get a real answer. If the number inside the square root is negative, you cannot find a real number whose square is that negative value.

## What is the Discriminant?

The expression $b^2 - 4ac$ is called the discriminant of the quadratic equation. It is the part of the formula that sits under the square root sign. Because this expression determines whether the quadratic equation has real roots or not, it is given a special name.

## Three Possible Outcomes

The value of the discriminant tells us exactly what kind of roots the equation will have.

(i) If $b^2 - 4ac > 0$, the equation has two distinct real roots.

(ii) If $b^2 - 4ac = 0$, the equation has two equal real roots.

(iii) If $b^2 - 4ac < 0$, the equation has no real roots.

When the discriminant is exactly zero, the plus-or-minus part of the formula becomes zero, giving the exact same root twice.

## Worked Example

Let us look at a new example to see how this works in practice. Consider the quadratic equation $2x^2 - 4x + 3 = 0$. First, we identify the values of $a$, $b$, and $c$. Here, $a = 2$, $b = -4$, and $c = 3$.

Next, we calculate the discriminant.

$$
b ^ {2} - 4 a c = (- 4) ^ {2} - (4 \times 2 \times 3) = 1 6 - 2 4 = - 8
$$

Since $-8 < 0$, the discriminant is negative. According to the rule, this means the equation has no real roots. We do not even need to solve the equation to know this fact.

Now consider $x^2 - 6x + 9 = 0$, where $a = 1$, $b = -6$ and $c = 9$. The discriminant is $(-6)^2 - 4 \times 1 \times 9 = 36 - 36 = 0$. So the equation has two equal real roots. Using the formula, $x = \frac{6 \pm 0}{2} = 3$, so the root is $3$, repeated twice.

Finally, consider $2x^2 - 5x + 3 = 0$. Here the discriminant is $(-5)^2 - 4 \times 2 \times 3 = 25 - 24 = 1 > 0$, so there are two distinct real roots. Indeed, $x = \frac{5 \pm 1}{4}$ gives $x = \frac{3}{2}$ or $x = 1$.

## An Everyday Application

Understanding the nature of roots helps us solve real-world problems. Imagine you are trying to place a pole on the boundary of a circular park. The park has a diameter of 13 metres. You want to place the pole at a point where the difference of its distances from two diametrically opposite gates is exactly 7 metres.

Let us call the distance from the pole to gate B as $x$ metres. Then, the distance to gate A is $x + 7$ metres. Because the gates are at the two ends of a diameter, and the angle in a semicircle is a right angle, the angle at the pole is a right angle, making a right-angled triangle.

Using the Pythagorean theorem:

$$
\mathrm{AP} ^ {2} + \mathrm{PB} ^ {2} = \mathrm{AB} ^ {2}
$$

$$
(x + 7) ^ {2} + x ^ {2} = 1 3 ^ {2}
$$

Expanding this gives:

$$
x ^ {2} + 1 4 x + 4 9 + x ^ {2} = 1 6 9
$$

$$
2 x ^ {2} + 1 4 x - 1 2 0 = 0
$$

Dividing by 2, we get:

$$
x ^ {2} + 7 x - 6 0 = 0
$$

To find the distance $x$, we need to know if this equation has real roots. We calculate the discriminant:

$$
b ^ {2} - 4 a c = 7 ^ {2} - 4 \times 1 \times (- 6 0) = 2 8 9
$$

Since $289 > 0$, the discriminant is positive. This means the equation has two real roots, and it is possible to place the pole on the boundary of the park. Solving, $x = \frac{-7 \pm 17}{2}$, so $x = 5$ or $x = -12$. A distance cannot be negative, so $x = 5$ m: the pole is 5 m from gate B and 12 m from gate A. As a check, $5^2 + 12^2 = 169 = 13^2$.

## Key points

*   The discriminant of a quadratic equation $ax^2 + bx + c = 0$ is the value $b^2 - 4ac$.
*   If the discriminant is greater than zero, the equation has two distinct real roots.
*   If the discriminant is equal to zero, the equation has two equal real roots.
*   If the discriminant is less than zero, the equation has no real roots.
*   Checking the discriminant first saves time by telling you whether solving the equation is even possible.