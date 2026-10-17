---
{
  "concept": "Laws of Exponents for Real Numbers",
  "slug": "laws-of-exponents-real",
  "grade": 9,
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
    "completion_tokens": 1503,
    "prompt_tokens": 4124,
    "total_tokens": 5627,
    "completion_tokens_details": {
      "accepted_prediction_tokens": null,
      "audio_tokens": null,
      "reasoning_tokens": 0,
      "rejected_prediction_tokens": null
    },
    "prompt_tokens_details": null
  },
  "target_words": [
    725,
    1350
  ],
  "generated_at": "2026-10-17T04:58:18",
  "source_grade": 9,
  "grade_delta": 0,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g9_maths_chapter1_025",
      "chapter": "chapter1",
      "section": "1.5 Laws of Exponents for Real Numbers"
    }
  ],
  "citation_check": {
    "cited": [
      "1"
    ],
    "invented_citations": [],
    "unused_sources": [],
    "explanatory_paragraphs_without_a_citation": 2,
    "words": 836,
    "target_words": [
      725,
      1350
    ],
    "untraceable_sections": 0,
    "ok": true,
    "structural_problems": []
  },
  "hand_edited": "2026-10-17: held only for 'notation' (false positive: the check flags \\sqrt[n]{a}, valid LaTeX). Hand audit: 'you have already learned / you know' opening replaced; the whole-number laws, a^0 = 1 and negative-exponent examples from Section 1.5 added; filler sentences removed. Worked example (8^(2/3) * 8^(1/3) = 8) checked.",
  "terms": [
    "rational exponent",
    "base",
    "exponent",
    "nth root",
    "real number",
    "positive real number",
    "product of powers",
    "quotient of powers",
    "power of a power",
    "product to a power"
  ]
}
---

# Laws of Exponents for Real Numbers

This page extends the laws of exponents to the case where the base is a positive real number and the exponents are rational numbers, such as $\frac{1}{2}$ or $\frac{3}{4}$. To do this we first need to understand what an exponent like $\frac{3}{2}$ means. This also lets us write roots, like square roots, as exponents.

## Laws of Exponents for Natural Numbers

Here $a$, $m$ and $n$ are natural numbers, $a$ is called the base, and $m$ and $n$ are the exponents. The laws of exponents are:

(i) $a^m \cdot a^n = a^{m+n}$

(ii) $(a^m)^n = a^{mn}$

(iii) $\frac{a^m}{a^n} = a^{m-n}$, where $m > n$

(iv) $a^m b^m = (ab)^m$

For example, $17^{2} \cdot 17^{5} = 17^{7}$, $(5^{2})^{7} = 5^{14}$, $\frac{23^{10}}{23^{7}} = 23^{3}$ and $7^{3} \cdot 9^{3} = 63^{3}$.

Also $(a)^0 = 1$. Using law (iii), we get $\frac{1}{a^n} = a^{-n}$. This lets us extend the laws to negative exponents too. For example, $17^{2} \cdot 17^{-5} = 17^{-3} = \frac{1}{17^{3}}$, $(5^{2})^{-7} = 5^{-14}$, $\frac{23^{-10}}{23^{7}} = 23^{-17}$ and $(7)^{-3} \cdot (9)^{-3} = (63)^{-3}$.

## Understanding Rational Exponents

Before we can use the laws of exponents with fractions, we need to know what a fraction like $\frac{3}{2}$ actually means. We define the $n$-th root of a positive real number $a$ as the positive number $b$ that satisfies $b^n = a$. In the language of exponents, we write $\sqrt[n]{a} = a^{\frac{1}{n}}$. For example, $\sqrt[3]{2}$ is simply $2^{\frac{1}{3}}$.

Now, let us look at a fractional exponent like $4^{\frac{3}{2}}$. We can interpret this in two different ways using our definition. The first way is to take the square root of 4 first, and then raise the result to the power of 3. This gives us $(4^{\frac{1}{2}})^{3} = 2^{3} = 8$. The second way is to raise 4 to the power of 3 first, and then take the square root of the result. This gives us $(4^{3})^{\frac{1}{2}} = 64^{\frac{1}{2}} = 8$. Both ways give the same answer, 8.

Here is the formal rule. Let $a > 0$ be a real number. Let $m$ and $n$ be integers such that $m$ and $n$ have no common factors other than 1, and $n > 0$. Then, we define $a^{\frac{m}{n}} = (\sqrt[n]{a})^{m} = \sqrt[n]{a^{m}}$.

## Applying the Laws to Rational Exponents

The laws of exponents can be extended to rational exponents. They hold when the base $a$ is a positive real number and the exponents $p$ and $q$ are rational numbers.

The first law is the product rule. If you multiply two powers with the same base, you add the exponents. For example, $2^{\frac{2}{3}} \cdot 2^{\frac{1}{3}} = 2^{\left(\frac{2}{3} + \frac{1}{3}\right)} = 2^{1} = 2$.

The second law is the power of a power rule. If you raise a power to another power, you multiply the exponents. For example, $\left(3^{\frac{1}{5}}\right)^{4} = 3^{\frac{4}{5}}$.

The third law is the quotient rule. If you divide two powers with the same base, you subtract the exponents. For example, $\frac{7^{\frac{1}{5}}}{7^{\frac{1}{3}}} = 7^{\left(\frac{1}{5} - \frac{1}{3}\right)} = 7^{\frac{3 - 5}{15}} = 7^{\frac{-2}{15}}$.

The fourth law is the product to a power rule. If you multiply two different bases raised to the same exponent, you can combine the bases. For example, $13^{\frac{1}{5}} \cdot 17^{\frac{1}{5}} = (13 \times 17)^{\frac{1}{5}} = 221^{\frac{1}{5}}$.

## The Extended Laws

Putting it all together, the extended laws of exponents for real numbers are as follows. Let $a > 0$ be a real number and let $p$ and $q$ be rational numbers. Then:

(i) $a^p \cdot a^q = a^{p+q}$
(ii) $(a^p)^q = a^{pq}$
(iii) $\frac{a^p}{a^q} = a^{p-q}$
(iv) $a^p b^p = (ab)^p$

These laws can be used to simplify expressions that involve roots and powers.

## Worked example

Let us look at a worked example to see how these rules work together. Suppose we want to simplify the expression $8^{\frac{2}{3}} \cdot 8^{\frac{1}{3}}$. We can use the first law, which says that when we multiply powers with the same base, we add the exponents. We add $\frac{2}{3}$ and $\frac{1}{3}$ to get $\frac{3}{3}$, which is 1. So, $8^{\frac{2}{3}} \cdot 8^{\frac{1}{3}} = 8^{1} = 8$.

Alternatively, we can solve this using the definition of rational exponents. We know that $8^{\frac{2}{3}}$ is the same as $(\sqrt[3]{8})^{2}$. Since the cube root of 8 is 2, this becomes $2^{2}$, which is 4. Similarly, $8^{\frac{1}{3}}$ is the cube root of 8, which is 2. Multiplying these two results together gives $4 \times 2 = 8$. Both methods give the same answer, which confirms that our rules are working correctly.

## Key points

*   A positive real number $a$ raised to the power of $\frac{1}{n}$ is defined as the $n$-th root of $a$, written as $a^{\frac{1}{n}} = \sqrt[n]{a}$.
*   For a positive real number $a$, the expression $a^{\frac{m}{n}}$ can be evaluated as $(\sqrt[n]{a})^{m}$ or $\sqrt[n]{a^{m}}$.
*   The laws of exponents, including the product, quotient, and power rules, apply to rational exponents just as they do to whole number exponents.
*   When multiplying powers with the same base, you add the exponents.
*   When dividing powers with the same base, you subtract the exponents.