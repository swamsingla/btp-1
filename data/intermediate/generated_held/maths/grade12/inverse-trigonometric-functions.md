---
{
  "concept": "Inverse Trigonometric Functions",
  "slug": "inverse-trigonometric-functions",
  "grade": 12,
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
    "completion_tokens": 2095,
    "prompt_tokens": 6332,
    "total_tokens": 8427,
    "completion_tokens_details": {
      "accepted_prediction_tokens": null,
      "audio_tokens": null,
      "reasoning_tokens": 0,
      "rejected_prediction_tokens": null
    },
    "prompt_tokens_details": null
  },
  "target_words": [
    1050,
    1450
  ],
  "generated_at": "2026-10-08T07:07:12",
  "source_grade": 12,
  "grade_delta": 0,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g12_maths_part1_chapter2_014",
      "chapter": "chapter2",
      "section": "2.3 Properties of Inverse Trigonometric Functions"
    },
    {
      "ref": "S2",
      "passage_id": "g12_maths_part1_chapter5_033",
      "chapter": "chapter5",
      "section": "5.3.3 Derivatives of inverse trigonometric functions"
    },
    {
      "ref": "S3",
      "passage_id": "g12_maths_part2_chapter1_006",
      "chapter": "chapter1",
      "section": "7.2 Integration as an Inverse Process of Differentiation"
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
    "explanatory_paragraphs_without_a_citation": 12,
    "words": 1117,
    "target_words": [
      1050,
      1450
    ],
    "untraceable_sections": 4,
    "ok": false,
    "structural_problems": []
  },
  "terms": [
    "inverse trigonometric functions",
    "principal value branch",
    "sin inverse",
    "cos inverse",
    "tan inverse",
    "domain",
    "range",
    "chain rule",
    "derivative",
    "continuous functions",
    "identity",
    "pythagorean identity",
    "differentiation"
  ]
}
---

# Inverse Trigonometric Functions

You have already studied the basic trigonometric functions, such as sine, cosine, and tangent, in your Grade 11 mathematics class. These functions take an angle as input and give you a ratio as output. Sometimes, you need to reverse this process. You might know the ratio and need to find the original angle. This is exactly what inverse trigonometric functions do. They are the inverses of the standard trigonometric functions, allowing you to find an angle when you know its sine, cosine, or tangent value.

## Principal Value Branches

Because trigonometric functions are periodic, a single output value corresponds to infinitely many angles. For example, if $\sin y = \frac{1}{2}$, then $y$ could be $\frac{\pi}{6}$, $\frac{5\pi}{6}$, $\frac{13\pi}{6}$, and so on. This makes the inverse relation ambiguous. To make inverse trigonometric functions well-defined, we must restrict the range of the original function to a specific interval. This restricted interval is called the principal value branch.

For the inverse sine function, denoted as $\sin^{-1} x$, we restrict the range of $x$ to $\left[ \frac{-\pi}{2}, \frac{\pi}{2} \right]$. For the inverse cosine function, $\cos^{-1} x$, the range is restricted to $[0, \pi]$. For the inverse tangent function, $\tan^{-1} x$, the range is restricted to $\left( \frac{-\pi}{2}, \frac{\pi}{2} \right)$. These restrictions ensure that every valid input $x$ maps to exactly one unique output angle.

## Basic Definitions

The inverse trigonometric functions are defined by their direct relationship with the standard trigonometric functions. If $y = \sin^{-1} x$, then $x = \sin y$. Similarly, if $x = \cos^{-1} y$, then $y = \cos x$, and if $x = \tan^{-1} y$, then $y = \tan x$.

This definition leads to two fundamental identities. The first is that applying the sine function to its inverse returns the original input. Specifically, $\sin \left( \sin^{-1} x \right) = x$, provided $x$ is in the domain $[-1, 1]$. The second identity is that applying the inverse sine function to the sine of an angle returns the angle itself, but only if that angle is within the principal value branch. Thus, $\sin^{-1} (\sin x) = x$, provided $x \in \left[ \frac{-\pi}{2}, \frac{\pi}{2} \right]$.

## Properties and Identities

Working with inverse trigonometric functions involves using specific algebraic identities and substitutions. These identities are extremely useful for simplifying complex expressions.

Consider the identity for the double angle of sine: $\sin 2\theta = 2 \sin \theta \cos \theta$. If we substitute $x = \sin \theta$, then $\sqrt{1 - x^2} = \cos \theta$ (since $\theta$ is in the principal branch where cosine is positive). This leads to the identity:
$$
\sin^{-1} \left( 2x \sqrt{1 - x^2} \right) = 2 \sin^{-1} x
$$
This identity is valid for $x$ in the range $\left[ -\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}} \right]$.

Similarly, if we use the substitution $x = \cos \theta$, we can derive another useful identity:
$$
\sin^{-1} \left( 2x \sqrt{1 - x^2} \right) = 2 \cos^{-1} x
$$
This version is valid for $x$ in the range $\left[ \frac{1}{\sqrt{2}}, 1 \right]$.

Another common technique is simplifying expressions involving $\tan^{-1}$ by using half-angle substitutions. For instance, the expression $\tan^{-1} \left( \frac{\cos x}{1 - \sin x} \right)$, where $x$ is in the range $\left( -\frac{3\pi}{2}, \frac{\pi}{2} \right)$, can be simplified by expressing the numerator and denominator in terms of $\frac{x}{2}$. This yields:
$$
\tan^{-1} \left[ \frac{1 + \tan \frac{x}{2}}{1 - \tan \frac{x}{2}} \right] = \frac{\pi}{4} + \frac{x}{2}
$$
This demonstrates how algebraic manipulation combined with trigonometric identities can reduce a complex inverse trigonometric expression to a simple linear form.

## Derivatives

The study of calculus introduces the concept of the derivative, which measures the rate of change of a function. The inverse trigonometric functions are continuous, and we can find their derivatives using the chain rule.

To find the derivative of $f(x) = \sin^{-1} x$, we start by letting $y = \sin^{-1} x$. This implies $x = \sin y$. Differentiating both sides with respect to $x$ gives:
$$
1 = \cos y \frac{dy}{dx}
$$
Solving for $\frac{dy}{dx}$ yields:
$$
\frac{dy}{dx} = \frac{1}{\cos y}
$$
Since $y = \sin^{-1} x$, we can rewrite this as $\frac{d}{dx} \left( \sin^{-1} x \right) = \frac{1}{\cos \left( \sin^{-1} x \right)}$.

This expression is only defined when $\cos y \neq 0$. This occurs when $\sin^{-1} x \neq -\frac{\pi}{2}$ and $\sin^{-1} x \neq \frac{\pi}{2}$, which corresponds to $x$ being in the open interval $(-1, 1)$.

To make this derivative more practical, we use the Pythagorean identity $\cos^2 y = 1 - \sin^2 y$. Substituting $x = \sin y$ gives $\cos^2 y = 1 - x^2$. Since $y$ is restricted to $\left( -\frac{\pi}{2}, \frac{\pi}{2} \right)$, $\cos y$ is always positive, so $\cos y = \sqrt{1 - x^2}$.

Therefore, the derivative of the inverse sine function is:
$$
\frac{d}{dx} \left( \sin^{-1} x \right) = \frac{1}{\sqrt{1 - x^2}}
$$
for $x \in (-1, 1)$.

Similarly, we can derive the derivatives of the inverse cosine and inverse tangent functions. The derivative of $\cos^{-1} x$ is $\frac{-1}{\sqrt{1 - x^2}}$, and the derivative of $\tan^{-1} x$ is $\frac{1}{1 + x^2}$.

## Worked example

Let us apply the derivative rule for the inverse sine function to a specific problem. Suppose we want to find the derivative of $f(x) = \sin^{-1} (2x)$ with respect to $x$.

We use the chain rule. Let $u = 2x$. Then $f(x) = \sin^{-1} u$. The derivative of $\sin^{-1} u$ with respect to $u$ is $\frac{1}{\sqrt{1 - u^2}}$. The derivative of $u$ with respect to $x$ is $2$.

Applying the chain rule, we get:
$$
\frac{df}{dx} = \frac{d}{du} \left( \sin^{-1} u \right) \cdot \frac{du}{dx} = \frac{1}{\sqrt{1 - u^2}} \cdot 2 = \frac{2}{\sqrt{1 - (2x)^2}}
$$
Simplifying the denominator, we have:
$$
\frac{df}{dx} = \frac{2}{\sqrt{1 - 4x^2}}
$$
This derivative is valid as long as the denominator is not zero, which means $4x^2 < 1$, or $x \in \left( -\frac{1}{2}, \frac{1}{2} \right)$.

## Key points

*   Inverse trigonometric functions, such as $\sin^{-1} x$, $\cos^{-1} x$, and $\tan^{-1} x$, are used to find an angle when the trigonometric ratio is known.
*   Because trigonometric functions are periodic, their inverses are restricted to specific ranges called principal value branches.
*   For $\sin^{-1} x$, the principal value branch is $\left[ \frac{-\pi}{2}, \frac{\pi}{2} \right]$.
*   The fundamental identity $\sin \left( \sin^{-1} x \right) = x$ holds true for $x \in [-1, 1]$.
*   The derivative of $\sin^{-1} x$ is $\frac{1}{\sqrt{1 - x^2}}$, defined for $x \in (-1, 1)$.
*   The derivative of $\cos^{-1} x$ is $\frac{-1}{\sqrt{1 - x^2}}$, defined for $x \in (-1, 1)$.
*   The derivative of $\tan^{-1} x$ is $\frac{1}{1 + x^2}$, defined for all real numbers $x \in \mathbb{R}$.