---
{
  "concept": "Factors and Multiples",
  "slug": "factors-and-multiples",
  "grade": 6,
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
    "completion_tokens": 1923,
    "prompt_tokens": 5179,
    "total_tokens": 7102,
    "completion_tokens_details": null,
    "prompt_tokens_details": null
  },
  "target_words": [
    700,
    1250
  ],
  "generated_at": "2026-10-02T19:36:19",
  "source_grade": 6,
  "grade_delta": 0,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g6_maths_chapter5_000",
      "chapter": "chapter5",
      "section": "5.1 Common Multiples and Common Factors"
    },
    {
      "ref": "S2",
      "passage_id": "g6_maths_chapter5_012",
      "chapter": "chapter5",
      "section": "5.4 Prime Factorisation"
    },
    {
      "ref": "S3",
      "passage_id": "g6_maths_chapter5_019",
      "chapter": "chapter5",
      "section": "5.5 Divisibility Tests"
    }
  ],
  "citation_check": {
    "cited": [
      "1",
      "2",
      "3"
    ],
    "invented_citations": [],
    "unused_sources": [],
    "explanatory_paragraphs_without_a_citation": 0,
    "words": 1220,
    "target_words": [
      700,
      1250
    ],
    "untraceable_sections": 0,
    "ok": true,
    "structural_problems": []
  },
  "terms": [
    "factor",
    "multiple",
    "factor pair",
    "co-prime",
    "prime factorisation",
    "prime factor",
    "composite number",
    "common factor",
    "hcf",
    "lcm"
  ],
  "hand_edited": "Grade 6 word band recalibrated from 900-1250 to 700-1250 on 2026-10-02 after two full runs showed the model never reaches 900 for these concepts (see the comment on GRADE_WORDS in build_context.py); this page kept its text and had its recorded band updated to the new standard."
}
---

# Factors and Multiples

Factors and multiples are the building blocks of multiplication. A factor is a number that divides another number exactly without leaving a remainder, while a multiple is the result of multiplying a number by an integer. Understanding these concepts is essential because they help us simplify fractions, compare quantities, and solve everyday problems involving grouping and sharing.

## Multiples and the Idli-Vada Game

Imagine a group of friends playing a counting game in a circle. The first player says 1, the second says 2, and they continue counting upwards. However, whenever they reach a multiple of 3, they must say "idli" instead of the number. When they reach a multiple of 5, they must say "vada". If a number is a multiple of both 3 and 5, they must say "idli-vada".

The players must say "idli" for the numbers 3, 6, 9, 12, 18, and so on. They must say "vada" for the numbers 5, 10, 20, 25, and so on. Notice that 15 is missing from both lists, even though it is a multiple of 3 and a multiple of 5: it is a multiple of both, so it is the very first number where they must say "idli-vada". Any number that is a multiple of both 3 and 5 is called a common multiple.

## Factors as Divisors

A factor is simply a divisor of another number. If you have 12 candies and want to share them equally among 3 friends, 3 is a factor of 12 because 12 can be divided by 3 without any remainder. 

However, finding all the factors of a number requires care. For instance, if you write 56 as $14 \times 4$, you know that 14 and 4 are factors, but this does not tell you all the factors of 56. Similarly, you could write 56 as $7 \times 8$, which shows that 7 is a factor of 56. Because there are many ways to write a number as a product of two factors, you must be systematic to find every single factor.

## Factor Pairs

Factor pairs are two numbers that multiply together to give the original number. For the number 56, one factor pair is 14 and 4, and another is 7 and 8. 

Sometimes, you can write a number in many different ways as a product of two factors. For example, 80 can be written as 40 times 2, 20 times 4, 10 times 8, or 16 times 5. 

## Co-prime Numbers

Two numbers are called co-prime if they do not share any common factor other than 1. To check if two numbers are co-prime, you must look at their full set of factors. 

For example, let us check if 56 and 63 are co-prime. Anshu wrote 56 as $14 \times 4$ and 63 as $21 \times 3$. Based on these pairs, Anshu thought there were no common factors. However, Guna wrote 56 as $7 \times 8$ and 63 as $9 \times 7$, and Guna noticed that 7 is a factor of both numbers. Because 7 is a common factor, 56 and 63 are not co-prime.

## Prime Factorisation

To find all the factors of a number systematically, we use prime factorisation. This means breaking a number down into a product of prime numbers. 

Let us take 56. We know 56 is a composite number, so we can write it as $4 \times 14$. The number 14 is also composite, so we break it down further into $2 \times 7$. Now we have $56 = 4 \times 2 \times 7$. The number 4 is still composite, so we break it down into $2 \times 2$. 

Putting it all together, we get $56 = 2 \times 2 \times 2 \times 7$. All the factors appearing here, 2 and 7, are prime numbers, so we cannot divide them further. 

The prime factors of 56 are 2 and 7. Every number greater than 1 has a prime factorisation. The number 1 does not have a prime factorisation because it is not divisible by any prime number. 

## Order Does Not Matter

You might wonder if the order in which you multiply the prime factors changes the result. It does not. 

For example, the number 36 can be factorised in many ways. You could write it as $2 \times 18$, $6 \times 6$, $12 \times 3$, or $4 \times 9$. If you break all of these down into prime factors, you will always find two 2s and two 3s. 

Multiplying numbers in any order gives the same result. Therefore, the order of the prime factors does not matter. Usually, we write the prime factors in increasing order. For example, 36 is $2^2 \times 3^2$, and 30 is $2 \times 3 \times 5$.

## Prime Factorisation of a Product

When you find the prime factorisation of a number, you can also find the prime factorisation of a product of two numbers by combining their factorisations. 

For example, let us take the number 72. We can write 72 as a product of two factors, such as $12 \times 6$. Now, we find the prime factorisation of each of these factors. We know $12 = 2 \times 2 \times 3$ and $6 = 2 \times 3$. 

To find the prime factorisation of 72, we put these together: $72 = 2 \times 2 \times 3 \times 2 \times 3$. We can also write this as $2 \times 2 \times 2 \times 3 \times 3$. 

If you multiply these prime factors back together, you will get 72. You can observe how many times each prime factor occurs in the factorisation of 72, and you will see that it matches how many times it occurs in the factorisations of 12 and 6 put together.

## Worked example

Let us find the prime factorisation of 80. First, we write 80 as a product of two factors. Let us use $10 \times 8$. 

Next, we find the prime factorisation of each factor. The number 10 is $2 \times 5$. The number 8 is $2 \times 4$, and 4 is $2 \times 2$, so 8 is $2 \times 2 \times 2$. 

Now, we put these together to find the prime factorisation of 80: $80 = 2 \times 5 \times 2 \times 2 \times 2$. If we arrange these in increasing order, we get $80 = 2^4 \times 5$.

## Key points
- A multiple of a number is the product of that number and an integer.
- A factor of a number is a divisor that divides it exactly without leaving a remainder.
- Factor pairs are two numbers that multiply together to give the original number.
- Two numbers are co-prime if their only common factor is 1.
- Prime factorisation is breaking a number down into a product of prime numbers.
- The order of the prime factors does not matter.
- To find the prime factorisation of a product, combine the prime factorisations of the individual numbers.