---
{
  "concept": "Zeroes of a Polynomial",
  "slug": "zeroes-of-a-polynomial",
  "grade": 9,
  "language": "en",
  "subject": "maths",
  "area": "Algebra",
  "hand_edited": "2026-10-17: held for length (802 words) and five 'arithmetic' flags, which are false positives (the checker reads p(1), p(2), p(-2) as the numbers 1, 2, -2; the arithmetic on the page was correct). The generated page also had no citation tags and an unsupported opening claim ('understand the behaviour of polynomial functions'). Rewritten by hand from Section 2.3 with tags, adding values at a point (Example 2), the zero of 2x + 1, the zero -b/a of a linear polynomial and p(0) = -2. All values re-checked.",
  "model": "sarvam-105b",
  "settings": {
    "temperature": 0.3,
    "max_tokens": 8000,
    "reasoning_effort": "none"
  },
  "usage": {
    "completion_tokens": 1212,
    "prompt_tokens": 6607,
    "total_tokens": 7819,
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
  "generated_at": "2026-10-17T04:58:35",
  "source_grade": 9,
  "grade_delta": 0,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g9_maths_chapter2_012",
      "chapter": "chapter2",
      "section": "2.3 Zeroes of a Polynomial"
    }
  ],
  "citation_check": {
    "cited": [
      "1"
    ],
    "invented_citations": [],
    "unused_sources": [],
    "explanatory_paragraphs_without_a_citation": 0,
    "words": 834,
    "target_words": [
      1000,
      1350
    ],
    "untraceable_sections": 0,
    "ok": true,
    "structural_problems": []
  },
  "terms": [
    "polynomial",
    "zero of a polynomial",
    "polynomial equation",
    "root",
    "constant polynomial",
    "zero polynomial",
    "linear polynomial"
  ]
}
---

# Zeroes of a Polynomial

This page looks at the value of a polynomial at a number, and at the numbers for which that value is zero. These numbers are called the zeroes of the polynomial.

## Value of a Polynomial at a Number

Consider the polynomial $p(x) = 5x^{3} - 2x^{2} + 3x - 2$. If we replace $x$ by 1 everywhere in $p(x)$, we get $p(1) = 5 \times (1)^{3} - 2 \times (1)^{2} + 3 \times (1) - 2 = 5 - 2 + 3 - 2 = 4$. So we say that the value of $p(x)$ at $x = 1$ is 4. Similarly, $p(0) = 5(0)^{3} - 2(0)^{2} + 3(0) - 2 = -2$.

Here are three more examples, finding the value of a polynomial at a given value of the variable:

*   For $p(x) = 5x^{2} - 3x + 7$ at $x = 1$: $p(1) = 5(1)^{2} - 3(1) + 7 = 5 - 3 + 7 = 9$.
*   For $q(y) = 3y^{3} - 4y + \sqrt{11}$ at $y = 2$: $q(2) = 3(2)^{3} - 4(2) + \sqrt{11} = 24 - 8 + \sqrt{11} = 16 + \sqrt{11}$.
*   For $p(t) = 4t^4 + 5t^3 - t^2 + 6$ at $t = a$: $p(a) = 4a^{4} + 5a^{3} - a^{2} + 6$.

## Zero of a Polynomial

Now consider the polynomial $p(x) = x - 1$. Here $p(1) = 1 - 1 = 0$. As $p(1) = 0$, we say that 1 is a zero of the polynomial $p(x)$. Similarly, 2 is a zero of $q(x)$, where $q(x) = x - 2$.

In general, a zero of a polynomial $p(x)$ is a number $c$ such that $p(c) = 0$.

## Zeroes and Polynomial Equations

The zero of the polynomial $x - 1$ is obtained by equating it to 0, that is $x - 1 = 0$, which gives $x = 1$. We say $p(x) = 0$ is a polynomial equation, and 1 is the root of the polynomial equation $p(x) = 0$. So 1 is the zero of the polynomial $x - 1$, or a root of the polynomial equation $x - 1 = 0$.

Finding a zero of $p(x)$ is the same as solving the equation $p(x) = 0$. For example, to find a zero of $p(x) = 2x + 1$, we solve $2x + 1 = 0$, which gives $x = -\frac{1}{2}$. So $-\frac{1}{2}$ is a zero of the polynomial $2x + 1$.

## Zero of a Linear Polynomial

Let $p(x) = ax + b$ with $a \neq 0$ be a linear polynomial. Finding a zero of $p(x)$ amounts to solving $p(x) = 0$, that is $ax + b = 0$ with $a \neq 0$. Then $ax = -b$, so $x = -\frac{b}{a}$. Hence $x = -\frac{b}{a}$ is the only zero of $p(x)$, which means a linear polynomial has one and only one zero. In this way 1 is the zero of $x - 1$, and $-2$ is the zero of $x + 2$.

## Zeroes of Constant Polynomials

Consider the constant polynomial 5. It has no zero, because replacing $x$ by any number in $5x^0$ still gives us 5. In fact, a non-zero constant polynomial has no zero. For the zero polynomial, by convention, every real number is a zero.

## Checking Whether a Number Is a Zero

To check whether $-2$ and 2 are zeroes of the polynomial $x + 2$, let $p(x) = x + 2$. Then $p(2) = 2 + 2 = 4$ and $p(-2) = -2 + 2 = 0$. Therefore $-2$ is a zero of the polynomial $x + 2$, but 2 is not.

## Observations

Our observations about the zeroes of polynomials are:

*   A zero of a polynomial need not be 0.
*   0 may be a zero of a polynomial.
*   Every linear polynomial has one and only one zero.
*   A polynomial can have more than one zero.

## Worked Example

Verify whether 2 and 0 are zeroes of the polynomial $x^{2} - 2x$. Let $p(x) = x^{2} - 2x$. Then $p(2) = 2^{2} - 4 = 4 - 4 = 0$ and $p(0) = 0 - 0 = 0$. Hence 2 and 0 are both zeroes of the polynomial $x^{2} - 2x$. This polynomial shows that a polynomial can have more than one zero, and that 0 can be one of them.

## Key points

*   The value of a polynomial $p(x)$ at $x = c$ is found by replacing $x$ by $c$ everywhere in $p(x)$.
*   A zero of a polynomial $p(x)$ is a number $c$ such that $p(c) = 0$.
*   Finding a zero of $p(x)$ amounts to solving the polynomial equation $p(x) = 0$.
*   The linear polynomial $ax + b$, with $a \neq 0$, has one and only one zero, $-\frac{b}{a}$.
*   A non-zero constant polynomial has no zero, and by convention every real number is a zero of the zero polynomial.
*   A polynomial can have more than one zero.
