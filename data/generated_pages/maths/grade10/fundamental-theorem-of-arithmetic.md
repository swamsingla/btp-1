---
{
  "concept": "Fundamental Theorem of Arithmetic",
  "slug": "fundamental-theorem-of-arithmetic",
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
    "completion_tokens": 2410,
    "prompt_tokens": 5501,
    "total_tokens": 7911,
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
  "generated_at": "2026-10-17T22:04:06",
  "source_grade": 10,
  "grade_delta": 0,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g10_maths_chapter1_005",
      "chapter": "chapter1",
      "section": "1.2 The Fundamental Theorem of Arithmetic"
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
    "explanatory_paragraphs_without_a_citation": 5,
    "words": 1482,
    "target_words": [
      1000,
      1350
    ],
    "untraceable_sections": 0,
    "ok": true,
    "structural_problems": [
      "sections: no 'key points' section",
      "questioning: 6 question marks — written as a worksheet"
    ]
  },
  "terms": [
    "fundamental theorem of arithmetic",
    "composite number",
    "prime factorisation",
    "hcf",
    "lcm",
    "prime numbers",
    "factor tree"
  ]
}
---

# Fundamental Theorem of Arithmetic

Every integer greater than 1 is uniquely expressible as a product of primes. This means that if you take any whole number bigger than 1, you can break it down into a specific set of prime numbers that multiply together to make it. This rule is like a mathematical fingerprint for numbers, ensuring that every number has its own unique set of prime factors. Understanding this theorem is crucial because it forms the foundation for many concepts in number theory, such as finding the Highest Common Factor (HCF) and the Least Common Multiple (LCM) of numbers. It also helps us understand the properties of rational numbers and their decimal expansions, which you will explore further in your studies.

## The Idea of Building Numbers from Primes

You have likely seen in your earlier classes that any natural number can be written as a product of its prime factors. For instance, $2 = 2$, $4 = 2 \times 2$, $253 = 11 \times 23$, and so on. Now, let us try and look at natural numbers from the other direction. That is, can any natural number be obtained by multiplying prime numbers? Let us see.

Take any collection of prime numbers, say 2, 3, 7, 11 and 23. If we multiply some or all of these numbers, allowing them to repeat as many times as we wish, we can produce a large collection of positive integers (In fact, infinitely many). Let us list a few:

$$
7 \times 11 \times 23 = 1771
$$

$$
3 \times 7 \times 11 \times 23 = 5313
$$

$$
2 \times 3 \times 7 \times 11 \times 23 = 10626
$$

$$
2^3 \times 3 \times 7^3 = 8232
$$

$$
2^2 \times 3 \times 7 \times 11 \times 23 = 21252
$$

and so on.

Now, let us suppose your collection of primes includes all the possible primes. What is your guess about the size of this collection? Does it contain only a finite number of integers, or infinitely many? In fact, there are infinitely many primes. So, if we combine all these primes in all possible ways, we will get an infinite collection of numbers, all the primes and all possible products of primes. The question is – can we produce all the composite numbers this way? What do you think? Do you think that there may be a composite number which is not the product of powers of primes? Before we answer this, let us factorise positive integers, that is, do the opposite of what we have done so far.

## Factorising Large Numbers

We are going to use the factor tree with which you are all familiar. Let us take some large number, say, 32760, and factorise it with a factor tree: $32760 = 2 \times 16380$, then $16380 = 2 \times 8190$, $8190 = 2 \times 4095$, $4095 = 3 \times 1365$, $1365 = 3 \times 455$, $455 = 5 \times 91$ and $91 = 7 \times 13$.

So we have factorised 32760 as $2 \times 2 \times 2 \times 3 \times 3 \times 5 \times 7 \times 13$ as a product of primes, i.e., $32760 = 2^3 \times 3^2 \times 5 \times 7 \times 13$ as a product of powers of primes.

Let us try another number, say, 123456789. This can be written as $3^2 \times 3803 \times 3607$. Of course, you have to check that 3803 and 3607 are primes! (Try it out for several other natural numbers yourself.) This leads us to a conjecture that every composite number can be written as the product of powers of primes. In fact, this statement is true, and is called the Fundamental Theorem of Arithmetic because of its basic crucial importance to the study of integers.

## The Statement of the Theorem

Theorem 1.1 (Fundamental Theorem of Arithmetic): Every composite number can be expressed (factorised) as a product of primes, and this factorisation is unique, apart from the order in which the prime factors occur.

An equivalent version of this theorem was probably first recorded as Proposition 14 of Book IX in Euclid's Elements, before it came to be known as the Fundamental Theorem of Arithmetic. However, the first correct proof was given by Carl Friedrich Gauss in his Disquisitiones Arithmeticae. Carl Friedrich Gauss is often referred to as the ‘Prince of Mathematicians’ and is considered one of the three greatest mathematicians of all time, along with Archimedes and Newton. He has made fundamental contributions to both mathematics and science.

The Fundamental Theorem of Arithmetic says that every composite number can be factorised as a product of primes. Actually it says more. It says that given any composite number it can be factorised as a product of prime numbers in a ‘unique’ way, except for the order in which the primes occur. That is, given any composite number there is one and only one way to write it as a product of primes, as long as we are not particular about the order in which the primes occur. So, for example, we regard $2 \times 3 \times 5 \times 7$ as the same as $3 \times 5 \times 7 \times 2$ , or any other possible order in which these primes are written. This fact is also stated in the following form: The prime factorisation of a natural number is unique, except for the order of its factors.

In general, given a composite number $x$, we factorise it as $x = p_1p_2\ldots p_n$, where $p_1, p_2, \ldots, p_n$ are primes and written in ascending order, i.e., $p_1 \leq p_2 \leq \ldots \leq p_n$. If we combine the same primes, we will get powers of primes. For example, $$ 32760 = 2 \times 2 \times 2 \times 3 \times 3 \times 5 \times 7 \times 13 = 2^3 \times 3^2 \times 5 \times 7 \times 13 $$ Once we have decided that the order will be ascending, then the way the number is factorised, is unique.

## Using the Theorem to Find HCF and LCM

The Fundamental Theorem of Arithmetic has many applications, both within mathematics and in other fields. Let us look at some examples.

Example: Find the HCF and LCM of 6 and 20 by the prime factorisation method.

Solution: We have : $6 = 2^1 \times 3^1$ and $20 = 2 \times 2 \times 5 = 2^2 \times 5^1$.

You can find HCF(6, 20) = 2 and LCM(6, 20) = 2 × 2 × 3 × 5 = 60, as done in your earlier classes.

Note that $HCF(6, 20) = 2^1 = \text{Product of the smallest power of each common prime factor in the numbers.}$

LCM (6, 20) = $2^2 \times 3^1 \times 5^1$ = Product of the greatest power of each prime factor, involved in the numbers.

From the example above, you might have noticed that HCF(6, 20) × LCM(6, 20) = 6 × 20. In fact, we can verify that for any two positive integers $a$ and $b$, HCF($a, b$) × LCM($a, b$) = $a \times b$.

Example: Find the HCF of 96 and 404 by the prime factorisation method. Hence, find their LCM.

Solution: The prime factorisation of 96 and 404 gives :

$$
96 = 2^5 \times 3, 404 = 2^2 \times 101
$$

Therefore, the HCF of these two integers is $2^2 = 4$.

$$ \text{LCM} (96, 404) = \frac {96 \times 404}{\mathrm{HCF} (96 , 404)} = \frac {96 \times 404}{4} = 9696 $$

Example: Find the HCF and LCM of 6, 72 and 120, using the prime factorisation method.

Solution: We have : $6 = 2 \times 3, 72 = 2^3 \times 3^2, 120 = 2^3 \times 3 \times 5$.

Here, $2^1$ and $3^1$ are the smallest powers of the common factors 2 and 3, respectively. So, HCF (6, 72, 120) = $2^1 \times 3^1 = 2 \times 3 = 6$

$2^3, 3^2$ and $5^1$ are the greatest powers of the prime factors 2, 3 and 5 respectively involved in the three numbers. So, LCM (6, 72, 120) = $2^3 \times 3^2 \times 5^1 = 360$

Remark: Notice, $6 \times 72 \times 120 \neq HCF(6, 72, 120) \times LCM(6, 72, 120)$.

## Worked Example

Consider the numbers $4^n$, where $n$ is a natural number. Check whether there is any value of $n$ for which $4^n$ ends with the digit zero.

Solution: If the number $4^n$ , for any n, were to end with the digit zero, then it would be divisible by 5. That is, the prime factorisation of $4^n$ would contain the prime 5. This is not possible because $4^n = (2)^{2n}$ ; so the only prime in the factorisation of $4^n$ is 2. So, the uniqueness of the Fundamental Theorem of Arithmetic guarantees that there are no other primes in the factorisation of $4^n$ . So, there is no natural number n for which $4^n$ ends with the digit zero.

## Key points

*   Every composite number can be written as a product of primes, and this factorisation is unique apart from the order of the prime factors (Fundamental Theorem of Arithmetic).
*   If we write the primes in ascending order and combine equal primes, we get a product of powers of primes, for example $32760 = 2^3 \times 3^2 \times 5 \times 7 \times 13$.
*   HCF is the product of the smallest power of each common prime factor, and LCM is the product of the greatest power of each prime factor involved.
*   For any two positive integers $a$ and $b$, $\text{HCF}(a, b) \times \text{LCM}(a, b) = a \times b$. This does not extend to three numbers.
*   Uniqueness lets us show that a number cannot have a prime in its factorisation, for example $4^n$ never ends with the digit zero because its only prime factor is 2.