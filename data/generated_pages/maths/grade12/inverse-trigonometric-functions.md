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
    "completion_tokens": 2212,
    "prompt_tokens": 6332,
    "total_tokens": 8544,
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
  "generated_at": "2026-10-08T05:16:59",
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
    "cited": [
      "1",
      "2"
    ],
    "invented_citations": [],
    "unused_sources": [
      "3"
    ],
    "explanatory_paragraphs_without_a_citation": 3,
    "words": 1118,
    "target_words": [
      1050,
      1450
    ],
    "untraceable_sections": 0,
    "ok": true,
    "structural_problems": []
  },
  "terms": [
    "inverse trigonometric functions",
    "principal value branches",
    "domain",
    "range",
    "chain rule",
    "derivative",
    "identity",
    "trigonometric substitution",
    "simplification"
  ]
}
---

# Inverse Trigonometric Functions

You have already studied trigonometric functions like sine, cosine, and tangent, and you know that these functions are not one-to-one. This means that if you are given a value like $\frac{1}{2}$, there are actually infinitely many angles whose sine is $\frac{1}{2}$. To make these functions invertible, we need to restrict their domains to specific intervals called principal value branches. This concept is crucial because it allows us to define unique inverse functions, which are widely used in calculus for finding derivatives and integrals, and in physics for determining angles from given ratios.

## The Core Idea and Principal Value Branches

An inverse trigonometric function takes a ratio of sides and returns the angle itself. For instance, if $y = \sin^{-1}x$, it means that $x = \sin y$. However, because sine is periodic and not one-to-one over its entire domain, we must restrict the range of the inverse function to a specific interval. This restricted range is known as the principal value branch. 

When we write $\sin^{-1}(\sin x) = x$, this equality only holds true if $x$ is within the principal value branch of the inverse sine function, specifically $x \in \left[ \frac {-\pi}{2}, \frac {\pi}{2} \right]$. Similarly, the identity $\sin \left(\sin^{-1} x\right) = x$ is valid only for $x \in [-1, 1]$, which is the domain of the inverse sine function. These restrictions are essential because without them, the inverse functions would not be well-defined, and many mathematical properties and identities would break down.

## Fundamental Identities

The inverse trigonometric functions obey specific identities that connect them to their direct trigonometric counterparts. The most fundamental identity arises from the fact that the sine and inverse sine functions are inverses of each other, provided we stay within the principal value branches and their respective domains.

If $y = \sin^{-1}x$, then $x = \sin y$. This relationship is equivalent to the following identities:
$$
\sin \left(\sin^{-1} x\right) = x, \quad x \in [-1, 1]
$$
and
$$
\sin^{-1} (\sin x) = x, \quad x \in \left[ \frac{-\pi}{2}, \frac{\pi}{2} \right]
$$.

For suitable values of the domain, similar results hold for the remaining trigonometric functions, such as cosine and tangent. These identities are the foundation for proving more complex properties and for simplifying expressions involving inverse trigonometric functions.

## Derivatives of Inverse Trigonometric Functions

In calculus, the derivatives of inverse trigonometric functions are extremely important. These derivatives are derived using the chain rule and the fundamental identities discussed previously. The derivatives are defined within the principal value branches of the corresponding inverse trigonometric functions, wherever they are defined.

Let us consider the derivative of $f(x) = \sin^{-1}x$. Assuming the derivative exists, we let $y = \sin^{-1}x$, which implies $x = \sin y$. Differentiating both sides with respect to $x$, we get:
$$
1 = \cos y \frac{dy}{dx}
$$
which implies that
$$
\frac{dy}{dx} = \frac{1}{\cos y} = \frac{1}{\cos \left(\sin^{-1} x\right)}
$$.

This result is defined only when $\cos y \neq 0$, which means $\sin^{-1} x \neq -\frac{\pi}{2}, \frac{\pi}{2}$, or equivalently, $x \neq -1, 1$, so $x \in (-1, 1)$. To simplify this expression, we use the identity $\cos^2 y = 1 - \sin^2 y$. Since $x = \sin y$, we have $\cos^2 y = 1 - x^2$. Furthermore, because $y \in \left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$, $\cos y$ is positive, so $\cos y = \sqrt{1 - x^2}$. Therefore, for $x \in (-1, 1)$:
$$
\frac{dy}{dx} = \frac{1}{\sqrt{1 - x^2}}
$$.

The derivatives of other inverse trigonometric functions follow similar patterns. For instance, the derivative of $\cos^{-1}x$ is $\frac{-1}{\sqrt{1-x^{2}}}$ and the derivative of $\tan^{-1}x$ is $\frac{1}{1+x^{2}}$.

## Simplifying Expressions

One of the practical applications of inverse trigonometric functions is simplifying complex algebraic expressions. By using appropriate trigonometric substitutions and identities, we can reduce complicated expressions to their simplest forms.

For example, consider the expression $\sin^{-1}\left(2x\sqrt{1 - x^2}\right)$. We can show that this expression simplifies to $2\sin^{-1}x$ under specific conditions. Let $x = \sin \theta$, which means $\sin^{-1}x = \theta$. Substituting this into the expression, we get:
$$
\sin^{-1} \left(2 \sin \theta \sqrt{1 - \sin^2 \theta}\right) = \sin^{-1} (2 \sin \theta \cos \theta) = \sin^{-1} (\sin 2 \theta) = 2 \theta = 2 \sin^{-1} x
$$
This simplification is valid for $- \frac{1}{\sqrt{2}} \leq x \leq \frac{1}{\sqrt{2}}$.

Similarly, the same expression can be shown to equal $2\cos^{-1}x$ when $\frac{1}{\sqrt{2}} \leq x \leq 1$. In this case, we let $x = \cos \theta$, and proceeding as above, we find that $\sin^{-1}\left(2x\sqrt{1 - x^2}\right) = 2\cos^{-1}x$.

Another example involves the expression $\tan^{-1}\frac{\cos x}{1 - \sin x}$. By rewriting the numerator and denominator using half-angle identities, we can simplify this expression. We write:
$$
\tan^{-1} \left(\frac {\cos x}{1 - \sin x}\right) = \tan^{-1} \left[ \frac {\cos^2 \frac{x}{2} - \sin^2 \frac{x}{2}}{\cos^2 \frac{x}{2} + \sin^2 \frac{x}{2} - 2 \sin \frac{x}{2} \cos \frac{x}{2}} \right]
$$
$$
= \tan^{-1} \left[ \frac {\left(\cos \frac{x}{2} + \sin \frac{x}{2}\right) \left(\cos \frac{x}{2} - \sin \frac{x}{2}\right)}{\left(\cos \frac{x}{2} - \sin \frac{x}{2}\right)^2} \right]
$$
$$
= \tan^{-1} \left[ \frac {\cos \frac{x}{2} + \sin \frac{x}{2}}{\cos \frac{x}{2} - \sin \frac{x}{2}} \right] = \tan^{-1} \left[ \frac {1 + \tan \frac{x}{2}}{1 - \tan \frac{x}{2}} \right]
$$
$$
= \tan^{-1} \left[ \tan \left(\frac{\pi}{4} + \frac{x}{2}\right) \right] = \frac{\pi}{4} + \frac{x}{2}
$$
This simplification is valid for $-\frac{3\pi}{2} < x < \frac{\pi}{2}$.

## Worked example

Let us apply the derivative rule for inverse trigonometric functions. We want to find the derivative of $f(x) = \tan^{-1}(x)$ assuming it exists. Let $y = \tan^{-1}x$, which means $x = \tan y$. Differentiating both sides with respect to $x$, we get:
$$
1 = \sec^2 y \frac{dy}{dx}
$$
which implies that
$$
\frac{dy}{dx} = \frac{1}{\sec^2 y} = \frac{1}{1 + \tan^2 y}
$$
Since $x = \tan y$, we have $\tan^2 y = x^2$, so:
$$
\frac{dy}{dx} = \frac{1}{1 + x^2}
$$
This result is valid for all real numbers $x$, as the domain of $\tan^{-1}x$ is the set of all real numbers.

## Key points

*   Inverse trigonometric functions are defined by restricting the domains of trigonometric functions to their principal value branches.
*   The identity $\sin \left(\sin^{-1} x\right) = x$ holds for $x \in [-1, 1]$, and $\sin^{-1} (\sin x) = x$ holds for $x \in \left[ \frac{-\pi}{2}, \frac{\pi}{2} \right]$.
*   The derivative of $\sin^{-1}x$ is $\frac{1}{\sqrt{1 - x^2}}$ for $x \in (-1, 1)$, and the derivative of $\tan^{-1}x$ is $\frac{1}{1 + x^2}$ for all real $x$.
*   Expressions involving inverse trigonometric functions can often be simplified using appropriate trigonometric substitutions and identities.
*   These functions and their properties are valid only within their principal value branches and wherever they are defined.