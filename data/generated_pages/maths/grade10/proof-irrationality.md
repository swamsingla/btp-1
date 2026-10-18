---
{
  "concept": "Proof of Irrationality",
  "slug": "proof-irrationality",
  "grade": 10,
  "language": "en",
  "subject": "maths",
  "area": "Number Theory",
  "model": "sarvam-105b",
  "settings": {
    "temperature": 0.3,
    "max_tokens": 8000,
    "reasoning_effort": "none"
  },
  "usage": {
    "completion_tokens": 1826,
    "prompt_tokens": 4857,
    "total_tokens": 6683,
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
  "generated_at": "2026-10-17T22:04:17",
  "source_grade": 10,
  "grade_delta": 0,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g10_maths_chapter1_010",
      "chapter": "chapter1",
      "section": "1.3 Revisiting Irrational Numbers"
    },
    {
      "ref": "S2",
      "passage_id": "g10_maths_chapter1_002",
      "chapter": "chapter1",
      "section": "1.1 Introduction"
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
    "explanatory_paragraphs_without_a_citation": 10,
    "words": 1017,
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
    "coprime",
    "proof by contradiction",
    "fundamental theorem of arithmetic",
    "theorem 1.2",
    "contradiction"
  ]
}
---

# Proof of Irrationality

In Grade 9, you learned about irrational numbers and how they fit with rational numbers to make up the real numbers. You even practiced locating them on the number line. However, you did not prove that numbers like $\sqrt{2}$ or $\sqrt{3}$ are actually irrational. In this section, we will prove that $\sqrt{2}$, $\sqrt{3}$, $\sqrt{5}$ and, in general, $\sqrt{p}$ is irrational, where $p$ is a prime. We use a technique called 'proof by contradiction' to do this.

## What is a Rational Number?

Before we prove a number is irrational, we must be absolutely clear about what a rational number is. A number $s$ is called rational if it can be written in the form $\frac{p}{q}$, where $p$ and $q$ are integers and $q \neq 0$. 

Every rational number can be simplified. If you have a fraction like $\frac{8}{12}$, you can divide the top and the bottom by their Highest Common Factor (HCF), which is 4. This gives you $\frac{2}{3}$. The numbers 2 and 3 have no common factors other than 1. When two integers have no common factors other than 1, we say they are coprime.

## The Key Theorem

To prove that square roots are irrational, we rely on a very important rule about prime numbers. This rule is based on the Fundamental Theorem of Arithmetic, which says that every composite number can be written as a product of primes in exactly one way, apart from the order of the factors. 

Theorem 1.2 states: Let $p$ be a prime number. If $p$ divides $a^2$, then $p$ divides $a$, where $a$ is a positive integer. 

This means that if a prime number perfectly divides a squared number, it must also perfectly divide the original number. For example, if 3 divides $a^2$, then 3 must divide $a$.

## Proof by Contradiction

Mathematicians often use a special technique to prove something is true. They assume the exact opposite of what they want to prove, and then they show that this assumption leads to a logical impossibility, or a contradiction. 

Let's prove that $\sqrt{2}$ is irrational.

We assume, to the contrary, that $\sqrt{2}$ is rational. 

If $\sqrt{2}$ is rational, we can write it as a fraction $\frac{a}{b}$, where $a$ and $b$ are coprime integers and $b \neq 0$. 

So, $\sqrt{2} = \frac{a}{b}$.

If we multiply both sides by $b$, we get $b\sqrt{2} = a$.

Now, we square both sides of the equation to remove the square root:
$(b\sqrt{2})^2 = a^2$
$2b^2 = a^2$

This equation tells us that $a^2$ is exactly divisible by 2. Because 2 is a prime number, Theorem 1.2 tells us that 2 must also divide $a$. 

If 2 divides $a$, we can write $a = 2c$ for some integer $c$.

Let's substitute $2c$ back into our equation:
$2b^2 = (2c)^2$
$2b^2 = 4c^2$

If we divide the entire equation by 2, we get:
$b^2 = 2c^2$

This means that $b^2$ is divisible by 2. Using Theorem 1.2 again, 2 must also divide $b$.

But wait. If 2 divides both $a$ and $b$, then $a$ and $b$ share a common factor of 2. This contradicts our original rule that $a$ and $b$ must be coprime.

Because our assumption that $\sqrt{2}$ is rational leads to a contradiction, the assumption must be false. Therefore, $\sqrt{2}$ is irrational.

## Proving Other Roots

We can use the exact same method to prove that $\sqrt{3}$ is irrational.

Assume, to the contrary, that $\sqrt{3}$ is rational. We can write it as $\frac{a}{b}$, where $a$ and $b$ are coprime integers.
$\sqrt{3} = \frac{a}{b}$
$b\sqrt{3} = a$

Squaring both sides gives us:
$3b^2 = a^2$

This means $a^2$ is divisible by 3. By Theorem 1.2, $a$ is divisible by 3. Let $a = 3c$.
$3b^2 = (3c)^2$
$3b^2 = 9c^2$
$b^2 = 3c^2$

This means $b^2$ is divisible by 3. By Theorem 1.2, $b$ is divisible by 3.
Therefore, $a$ and $b$ share a common factor of 3. This contradicts the fact that $a$ and $b$ are coprime.
So, $\sqrt{3}$ is irrational.

## Proving Combinations of Numbers

We can also use contradiction to prove that expressions involving irrational numbers are irrational. In Grade 9, you learned that the sum, difference, product, or quotient of a non-zero rational and an irrational number is irrational. Let's prove a specific case.

Show that $5 - \sqrt{3}$ is irrational.

Assume, to the contrary, that $5 - \sqrt{3}$ is rational.
This means we can write $5 - \sqrt{3} = \frac{a}{b}$, where $a$ and $b$ are coprime integers and $b \neq 0$.

If we rearrange this equation:
$5 - \frac{a}{b} = \sqrt{3}$
$\frac{5b - a}{b} = \sqrt{3}$

Since $a$ and $b$ are integers, $5b - a$ is also an integer. This means $\frac{5b - a}{b}$ is a rational number.
Therefore, $\sqrt{3}$ must be rational.

But this contradicts the fact that $\sqrt{3}$ is irrational.
So, we conclude that $5 - \sqrt{3}$ is irrational.

## Worked example

Let's apply the rule to prove that $3\sqrt{2}$ is irrational.

Assume, to the contrary, that $3\sqrt{2}$ is rational.
This means we can write $3\sqrt{2} = \frac{a}{b}$, where $a$ and $b$ are coprime integers and $b \neq 0$.

If we rearrange this equation:
$\sqrt{2} = \frac{a}{3b}$

Since $a$, $b$, and $3$ are all integers, $\frac{a}{3b}$ is a rational number.
Therefore, $\sqrt{2}$ must be rational.

But this contradicts the fact that $\sqrt{2}$ is irrational.
So, we conclude that $3\sqrt{2}$ is irrational.

## Key points

*   An irrational number cannot be written in the form $\frac{p}{q}$ where $p$ and $q$ are integers and $q \neq 0$.
*   Proof by contradiction assumes the opposite of what you want to prove, and shows it leads to a logical impossibility.
*   Theorem 1.2: If a prime $p$ divides $a^2$, then $p$ divides $a$.
*   The proof for $\sqrt{2}$ shows that if it were rational, both $a$ and $b$ would have to be divisible by 2, which contradicts them being coprime.
*   The exact same method proves that $\sqrt{3}$ is irrational, and that expressions like $5 - \sqrt{3}$ and $3\sqrt{2}$ are irrational.