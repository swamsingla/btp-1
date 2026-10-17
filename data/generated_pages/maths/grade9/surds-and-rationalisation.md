---
{
  "concept": "Surds and Rationalisation",
  "slug": "surds-and-rationalisation",
  "grade": 9,
  "language": "en",
  "subject": "maths",
  "area": "Number Systems",
  "hand_edited": "2026-10-17: held for length (518 words). Hand audit found the page defined 'surd' and 'conjugate', words that do not appear anywhere in the Grade 9 text, and cited the 425 BC Theodorus sentence to a passage that does not contain it. Rewritten by hand from Section 1.4 (Examples 11-19) and 1.2: operations on irrational numbers, identities, simplify examples, rationalising 1/sqrt2, 1/(2+sqrt3), 1/(7+3sqrt2), 5/(sqrt3-sqrt5). Every example's arithmetic checked. The 'arithmetic' flag on the original was a false positive.",
  "model": "sarvam-105b",
  "settings": {
    "temperature": 0.3,
    "max_tokens": 8000,
    "reasoning_effort": "none"
  },
  "usage": {
    "completion_tokens": 1129,
    "prompt_tokens": 7032,
    "total_tokens": 8161,
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
  "generated_at": "2026-10-17T04:58:09",
  "source_grade": 9,
  "grade_delta": 0,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g9_maths_chapter1_017",
      "chapter": "chapter1",
      "section": "1.4 Operations on Real Numbers"
    },
    {
      "ref": "S2",
      "passage_id": "g9_maths_chapter1_005",
      "chapter": "chapter1",
      "section": "1.2 Irrational Numbers"
    }
  ],
  "citation_check": {
    "cited": [
      "1",
      "2"
    ],
    "invented_citations": [],
    "unused_sources": [],
    "explanatory_paragraphs_without_a_citation": 0,
    "words": 1030,
    "target_words": [
      1000,
      1350
    ],
    "untraceable_sections": 0,
    "ok": true,
    "structural_problems": []
  },
  "terms": [
    "irrational number",
    "rational number",
    "square root",
    "rationalising the denominator",
    "real number"
  ]
}
---

# Surds and Rationalisation

This page is about expressions that contain irrational square roots such as $\sqrt{2}$ and $\sqrt{3}$. We see what happens when such numbers are added, multiplied and divided, how identities for square roots help us simplify expressions, and how to rationalise a denominator that contains a square root.

## Irrational Square Roots

A number is called irrational if it cannot be written in the form $\frac{p}{q}$, where $p$ and $q$ are integers and $q \neq 0$. Some examples are $\sqrt{2}$, $\sqrt{3}$, $\sqrt{15}$ and $\pi$.

When we use the symbol $\sqrt{}$, we assume that it is the positive square root of the number. So $\sqrt{4}=2$, though both 2 and $-2$ are square roots of 4. For a real number $a > 0$, $\sqrt{a} = b$ means $b^2 = a$ and $b > 0$.

## Operations on Irrational Numbers

The sum, difference, quotient and product of irrational numbers are not always irrational. For example, $\left(\sqrt{6}\right)+\left(-\sqrt{6}\right)$, $\left(\sqrt{2}\right)-\left(\sqrt{2}\right)$, $\left(\sqrt{3}\right)\cdot\left(\sqrt{3}\right)$ and $\frac{\sqrt{17}}{\sqrt{17}}$ are all rational.

Now take a rational number together with an irrational one. Since $\sqrt{3}$ has a non-terminating non-recurring decimal expansion, the same is true for $2 + \sqrt{3}$ and $2\sqrt{3}$. Therefore both $2 + \sqrt{3}$ and $2\sqrt{3}$ are irrational numbers.

Examples like these lead to the following facts, which are true:

*   The sum or difference of a rational number and an irrational number is irrational.
*   The product or quotient of a non-zero rational number with an irrational number is irrational.
*   If we add, subtract, multiply or divide two irrationals, the result may be rational or irrational.

We can test a number by writing it as a decimal. Using $\sqrt{5} = 2.236\ldots$, $\sqrt{2} = 1.4142\ldots$ and $\pi = 3.1415\ldots$, we get $7\sqrt{5} = 15.652\ldots$, $\frac{7}{\sqrt{5}} = \frac{7\sqrt{5}}{\sqrt{5}\sqrt{5}} = \frac{7\sqrt{5}}{5} = 3.1304\ldots$, $\sqrt{2} + 21 = 22.4142\ldots$ and $\pi - 2 = 1.1415\ldots$. All of these are non-terminating non-recurring decimals, so all of them are irrational numbers.

Here is how irrational numbers are added, multiplied and divided:

*   Add $2\sqrt{2} + 5\sqrt{3}$ and $\sqrt{2} - 3\sqrt{3}$. Collecting the like terms, $\left(2\sqrt{2} + \sqrt{2}\right) + \left(5\sqrt{3} - 3\sqrt{3}\right) = (2 + 1)\sqrt{2} + (5 - 3)\sqrt{3} = 3\sqrt{2} + 2\sqrt{3}$.
*   Multiply $6\sqrt{5}$ by $2\sqrt{5}$. We get $6 \times 2 \times \sqrt{5} \times \sqrt{5} = 12 \times 5 = 60$.
*   Divide $8\sqrt{15}$ by $2\sqrt{3}$. Writing $\sqrt{15} = \sqrt{3} \times \sqrt{5}$, we get $\frac{8\sqrt{3} \times \sqrt{5}}{2\sqrt{3}} = 4\sqrt{5}$.

## Identities for Square Roots

Some identities relating to square roots are useful in various ways. The remaining ones follow from the distributive law of multiplication over addition of real numbers, and from the identity $(x + y)(x - y) = x^{2} - y^{2}$, for any real numbers $x$ and $y$. Let $a$ and $b$ be positive real numbers. Then:

(i) $\sqrt{ab} = \sqrt{a}\sqrt{b}$

(ii) $\sqrt{\frac{a}{b}} = \frac{\sqrt{a}}{\sqrt{b}}$

(iii) $\left(\sqrt{a} + \sqrt{b}\right)\left(\sqrt{a} - \sqrt{b}\right) = a - b$

(iv) $\left(a + \sqrt{b}\right)\left(a - \sqrt{b}\right) = a^2 - b$

(v) $\left(\sqrt{a} + \sqrt{b}\right)\left(\sqrt{c} + \sqrt{d}\right) = \sqrt{ac} + \sqrt{ad} + \sqrt{bc} + \sqrt{bd}$

(vi) $\left(\sqrt{a} + \sqrt{b}\right)^2 = a + 2\sqrt{ab} + b$

Here "simplify" means that the expression should be written as the sum of a rational and an irrational number. Let us simplify some expressions using the identities.

*   $\left(5+\sqrt{7}\right)\left(2+\sqrt{5}\right) = 10 + 5\sqrt{5} + 2\sqrt{7} + \sqrt{35}$, by the distributive law.
*   $\left(5 + \sqrt{5}\right)\left(5 - \sqrt{5}\right) = 5^2 - \left(\sqrt{5}\right)^2 = 25 - 5 = 20$, by identity (iv).
*   $\left(\sqrt{3} + \sqrt{7}\right)^2 = \left(\sqrt{3}\right)^2 + 2\sqrt{3}\sqrt{7} + \left(\sqrt{7}\right)^2 = 3 + 2\sqrt{21} + 7 = 10 + 2\sqrt{21}$, by identity (vi).
*   $\left(\sqrt{11} - \sqrt{7}\right)\left(\sqrt{11} + \sqrt{7}\right) = \left(\sqrt{11}\right)^2 - \left(\sqrt{7}\right)^2 = 11 - 7 = 4$, by identity (iii).

## Rationalising the Denominator

Look at $\frac{1}{\sqrt{2}}$. It is irrational, and it may be easier to handle if the denominator is a rational number. To rationalise the denominator means to make the denominator into a rational number. To do so, we need the identities involving square roots.

We want to write $\frac{1}{\sqrt{2}}$ as an equivalent expression in which the denominator is a rational number. We know that $\sqrt{2} \cdot \sqrt{2}$ is rational. We also know that multiplying $\frac{1}{\sqrt{2}}$ by $\frac{\sqrt{2}}{\sqrt{2}}$ gives an equivalent expression, since $\frac{\sqrt{2}}{\sqrt{2}} = 1$. Putting these two facts together, $\frac{1}{\sqrt{2}} = \frac{1}{\sqrt{2}} \times \frac{\sqrt{2}}{\sqrt{2}} = \frac{\sqrt{2}}{2}$. In this form it is easy to locate $\frac{1}{\sqrt{2}}$ on the number line, because it is half way between 0 and $\sqrt{2}$.

When the denominator has two terms, we multiply and divide by the same two terms with the sign between them changed, so that an identity removes the square roots from the denominator. To rationalise $\frac{1}{2 + \sqrt{3}}$ we use identity (iv) and multiply and divide by $2 - \sqrt{3}$:

$\frac{1}{2 + \sqrt{3}}\times \frac{2 - \sqrt{3}}{2 - \sqrt{3}} = \frac{2 - \sqrt{3}}{4 - 3} = 2 - \sqrt{3}$.

In the same way, to rationalise $\frac{1}{7 + 3\sqrt{2}}$ we multiply and divide by $7 - 3\sqrt{2}$, which gives $\frac{7 - 3\sqrt{2}}{49 - 18} = \frac{7 - 3\sqrt{2}}{31}$.

So, when the denominator of an expression contains a term with a square root, converting it to an equivalent expression whose denominator is a rational number is called rationalising the denominator.

## Worked Example

Rationalise the denominator of $\frac{5}{\sqrt{3} - \sqrt{5}}$. Here we use identity (iii), $\left(\sqrt{a} + \sqrt{b}\right)\left(\sqrt{a} - \sqrt{b}\right) = a - b$, with $a = 3$ and $b = 5$, so we multiply and divide by $\sqrt{3} + \sqrt{5}$.

$\frac{5}{\sqrt{3} - \sqrt{5}} = \frac{5}{\sqrt{3} - \sqrt{5}} \times \frac{\sqrt{3} + \sqrt{5}}{\sqrt{3} + \sqrt{5}} = \frac{5\left(\sqrt{3} + \sqrt{5}\right)}{3 - 5} = \left(\frac{-5}{2}\right)\left(\sqrt{3} + \sqrt{5}\right)$.

## Key points

*   The sum, difference, quotient and product of two irrational numbers may be rational or irrational.
*   The sum or difference of a rational number and an irrational number is irrational.
*   The product or quotient of a non-zero rational number with an irrational number is irrational.
*   Identities such as $\left(\sqrt{a} + \sqrt{b}\right)\left(\sqrt{a} - \sqrt{b}\right) = a - b$ and $\left(a + \sqrt{b}\right)\left(a - \sqrt{b}\right) = a^2 - b$ help us simplify expressions with square roots.
*   Rationalising the denominator means converting an expression with a square root in the denominator into an equivalent expression whose denominator is a rational number.
