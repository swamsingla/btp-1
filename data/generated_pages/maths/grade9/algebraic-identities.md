---
{
  "concept": "Algebraic Identities",
  "slug": "algebraic-identities",
  "grade": 9,
  "language": "en",
  "subject": "maths",
  "area": "Algebra",
  "model": "sarvam-105b",
  "settings": {
    "temperature": 0.3,
    "max_tokens": 3500,
    "reasoning_effort": "none"
  },
  "usage": {
    "completion_tokens": 1685,
    "prompt_tokens": 4944,
    "total_tokens": 6629,
    "completion_tokens_details": null,
    "prompt_tokens_details": null
  },
  "target_words": [
    700,
    1000
  ],
  "generated_at": "2026-10-02T11:54:05",
  "source_grade": 9,
  "grade_delta": 0,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g9_maths_chapter2_021",
      "chapter": "chapter2",
      "section": "2.5 Algebraic Identities"
    },
    {
      "ref": "S2",
      "passage_id": "g9_maths_chapter2_000",
      "chapter": "chapter2",
      "section": "2.1 Introduction"
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
    "words": 980,
    "target_words": [
      700,
      1000
    ],
    "ok": true
  }
}
---

# Algebraic Identities

An algebraic identity is a special algebraic equation that remains true for every possible value of the variables it contains. You might have already used some of these identities in earlier classes to multiply expressions quickly or to break down complex algebraic expressions into simpler factors. In this chapter, we will explore how these standard formulas can be used to simplify our calculations and solve problems much faster.

## The Four Standard Identities

The foundation of algebraic identities rests on four standard formulas that you should memorize. These are the building blocks for almost every problem you will encounter in this topic.

The first two identities are the expansions of squared binomials. The first is the expansion of the sum of two variables, and the second is the expansion of their difference.

Identity I: $(x + y)^{2} = x^{2} + 2xy + y^{2}$
Identity II: $(x - y)^{2} = x^{2} - 2xy + y^{2}$

The third identity is the difference of two squares. It shows how a subtraction of squares can be factored into a multiplication of two binomials.

Identity III: $x^{2} - y^{2} = (x + y)(x - y)$

The fourth identity is a useful formula for multiplying two binomials that share the same first term. It allows you to find the product without multiplying term by term.

Identity IV: $(x + a)(x + b) = x^{2} + (a + b)x + ab$

## Expanding Trinomials

Sometimes, you will encounter an expression with three terms, known as a trinomial. You can expand the square of a trinomial by using the first standard identity as a stepping stone. Let us consider the expression $(x + y + z)^2$. We can treat the first two terms as a single variable, say $t = x + y$, and apply Identity I.

$(t + z)^2 = t^2 + 2tz + z^2$

Substituting $t = x + y$ back into the equation gives us:

$(x + y)^2 + 2(x + y)z + z^2$

Now, we apply Identity I again to the $(x + y)^2$ part:

$x^2 + 2xy + y^2 + 2xz + 2yz + z^2$

Rearranging the terms in descending order of the variables, we get the standard formula for expanding a trinomial squared.

Identity V: $(x + y + z)^{2} = x^{2} + y^{2} + z^{2} + 2xy + 2yz + 2zx$

This identity is incredibly useful when you need to expand expressions like $(3a + 4b + 5c)^2$ quickly without doing the multiplication manually.

## Expanding Cubes

Just as we can expand the square of a sum or difference, we can also expand the cube of a binomial. The first identity for cubes expands the sum of two variables, and the second identity expands their difference.

Identity VI: $(x + y)^{3} = x^{3} + y^{3} + 3xy(x + y)$
Identity VII: $(x - y)^{3} = x^{3} - y^{3} - 3xy(x - y) = x^{3} - 3x^{2}y + 3xy^{2} - y^{3}$

To use these identities, you simply need to identify which parts of your expression correspond to $x$ and $y$, and then substitute them into the formula. This saves a lot of time when dealing with complex algebraic terms.

## Using Identities for Quick Calculations

One of the most practical uses of algebraic identities is to perform arithmetic calculations without a calculator. By cleverly choosing values for your variables, you can turn a difficult multiplication into a simple application of an identity.

Consider the problem of finding the product of $105 \times 106$. Instead of multiplying directly, you can use Identity IV. Let us write $105$ as $(100 + 5)$ and $106$ as $(100 + 6)$. Here, $x = 100$, $a = 5$, and $b = 6$.

Using Identity IV: $(x + a)(x + b) = x^{2} + (a + b)x + ab$

$(100 + 5)(100 + 6) = 100^2 + (5 + 6) \cdot 100 + (5 \cdot 6)$

$= 10000 + 1100 + 30$

$= 11130$

This method is much faster and less prone to errors than traditional multiplication, especially when dealing with larger numbers.

## Worked example

Let us apply Identity III to factorise the expression $\frac {2 5}{4} x ^ {2} - \frac {y ^ {2}}{9}$.

First, we need to recognize that $\frac {2 5}{4} x ^ {2}$ is a perfect square. We can write it as $\left(\frac {5}{2} x\right)^2$ because $\left(\frac {5}{2}\right)^2 = \frac {2 5}{4}$.

Similarly, $\frac {y ^ {2}}{9}$ is a perfect square because it can be written as $\left(\frac {y}{3}\right)^2$ since $\left(\frac {y}{3}\right)^2 = \frac {y ^ {2}}{9}$.

Now, our expression becomes $\left(\frac {5}{2} x\right)^2 - \left(\frac {y}{3}\right)^2$.

We can now apply Identity III: $x^{2} - y^{2} = (x + y)(x - y)$

Let $x = \frac {5}{2} x$ and $y = \frac {y}{3}$.

$\left(\frac {5}{2} x\right)^2 - \left(\frac {y}{3}\right)^2 = \left(\frac {5}{2} x + \frac {y}{3}\right) \left(\frac {5}{2} x - \frac {y}{3}\right)$

This is the fully factorised form of the given expression.

## Key points

*   An algebraic identity is an equation that holds true for all values of the variables involved.
*   Identity I and Identity II are used to expand the square of a binomial, while Identity III is used to factorise the difference of two squares.
*   Identity IV is a shortcut for multiplying two binomials with the same first term.
*   Identity V expands the square of a trinomial into a sum of squares and product terms.
*   Identity VI and Identity VII expand the cube of a binomial, making it easier to handle higher powers.
*   These identities are not just for algebra; they can be used to perform quick arithmetic calculations.