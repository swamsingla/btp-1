---
{
  "concept": "Prime Factorisation",
  "slug": "prime-factorisation",
  "grade": 6,
  "language": "en",
  "prior_knowledge_fix": "2026-10-13: removed or rewrote an unsupported claim about what the student has already studied; edited directly in the tagged copy and the published copy",
  "subject": "maths",
  "area": "Number Theory",
  "model": "sarvam-105b",
  "settings": {
    "temperature": 0.3,
    "max_tokens": 8000,
    "reasoning_effort": "none"
  },
  "usage": {
    "completion_tokens": 1672,
    "prompt_tokens": 5740,
    "total_tokens": 7412,
    "completion_tokens_details": null,
    "prompt_tokens_details": null
  },
  "target_words": [
    700,
    1250
  ],
  "generated_at": "2026-10-02T19:45:15",
  "source_grade": 7,
  "grade_delta": 1,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g7_maths_part2_chapter3_003",
      "chapter": "chapter3",
      "section": "3.1 The Greatest of All"
    },
    {
      "ref": "S2",
      "passage_id": "g7_maths_part1_chapter4_006",
      "chapter": "chapter4",
      "section": "4.2 Revisiting Arithmetic Expressions"
    },
    {
      "ref": "S3",
      "passage_id": "g7_maths_part2_chapter3_020",
      "chapter": "chapter3",
      "section": "3.3 Patterns, Properties, and a Pretty Procedure!"
    }
  ],
  "citation_check": {
    "cited": [
      "1"
    ],
    "invented_citations": [],
    "unused_sources": [
      "2",
      "3"
    ],
    "explanatory_paragraphs_without_a_citation": 0,
    "words": 1009,
    "target_words": [
      700,
      1250
    ],
    "untraceable_sections": 0,
    "ok": true,
    "structural_problems": []
  },
  "terms": [
    "prime factorisation",
    "prime number",
    "composite number",
    "division method",
    "factors",
    "highest common factor",
    "prime factors"
  ],
  "hand_edited": "2026-10-02: the 105 example pasted the division table for 30 where 35's belonged, and the 225 tables skipped the 25 step. All five \\begin{array} division tables replaced with plain prose division chains, which are unambiguous and do not depend on the renderer supporting LaTeX arrays. The factor list for 225 also jumped from 1 straight to pairs, omitting the single factors 3 and 5 that the final list included. Answers were already correct (105, 30, 225, 1200) and are unchanged. Not regenerated. Grade 6 word band recalibrated from 900-1250 to 700-1250 on 2026-10-02 after two full runs showed the model never reaches 900 for these concepts (see the comment on GRADE_WORDS in build_context.py); this page kept its text and had its recorded band updated to the new standard. Source tags added on 2026-10-02 by the generator's repair stage (build_context.render_repair), which annotates an existing page instead of rewriting it, so the hand corrections above were preserved; the tagged copy is in data/intermediate/generated_tagged and the published text carries no tags."
}
---

# Prime Factorisation

Prime factorisation is a way to break down any number into the smallest building blocks of mathematics: prime numbers. Every whole number greater than 1 is either a prime number itself, or it is a product of prime numbers. This method is very useful because it helps us find the factors of a number quickly, and it makes finding the Highest Common Factor (HCF) of two numbers much easier. If you know what prime numbers are and the divisibility rules for 2, 4, 5, 8, and 10, you already have some useful tools for finding prime factorisation.

## What is Prime Factorisation?

Any number can be written as a product of prime numbers by going on factorising the composite numbers until only prime numbers are left. This final result is called the prime factorisation of the given number. For example, we can find the prime factorisation of 90 by breaking it down:
$$ 90 = 3 \times 3 \times 2 \times 5 $$ The number 90 could also have been factorised in different ways at the start, like $3 \times 30$ or $2 \times 45$. However, no matter which starting pair you choose, the resulting prime factors are always the same, just possibly in a different order. For example, if we start with $3 \times 30$ and factorise 30 further, we get:
$$ 90 = 3 \times 30 = 3 \times 2 \times 15 = 3 \times 2 \times 3 \times 5 $$ This is the same set of prime factors as before. Also, if you are given a prime number itself, its prime factorisation is simply the prime number itself.

## The Division Method

To make the process of finding prime factors simple and reliable, we use the division method. In this method, we divide the number by the smallest prime factor that goes into it exactly. We keep doing this until the number left at the bottom is a prime number. 

Let us find the prime factorisation of 105 this way. The smallest prime that divides 105 is 3, and $105 \div 3 = 35$. The smallest prime that divides 35 is 5, and $35 \div 5 = 7$. Now 7 is itself a prime number, so we stop. The prime factorisation is the primes we divided by, together with the prime we were left with:
$$ 105 = 3 \times 5 \times 7 $$ The same method works for 30. The smallest prime that divides 30 is 2, and $30 \div 2 = 15$. The smallest prime that divides 15 is 3, and $15 \div 3 = 5$. Now 5 is prime, so we stop, which gives $30 = 2 \times 3 \times 5$. The division method is much easier to carry out than randomly picking factors, especially for numbers with many factors.

## Finding Factors from Prime Factorisation

Once you have the prime factorisation of a number, you can use it to find all of its factors. You do this by taking different combinations of the prime factors and multiplying them together. 

For example, let us find the factors of 225. First we need its prime factorisation, using the division method. The smallest prime that divides 225 is 3, and $225 \div 3 = 75$. Three divides 75 as well, and $75 \div 3 = 25$. Three does not divide 25, but 5 does, and $25 \div 5 = 5$. Finally 5 is prime, so we stop. So the prime factorisation of 225 is $225 = 3 \times 3 \times 5 \times 5$.

Now, we can find all the factors of 225 by taking different combinations of these prime factors. We start with 1, which is always a factor because it uses none of them. Taking one prime factor at a time gives 3 and 5. Taking two at a time gives $3 \times 3 = 9$, $3 \times 5 = 15$ and $5 \times 5 = 25$. Taking three at a time gives $3 \times 3 \times 5 = 45$ and $3 \times 5 \times 5 = 75$. Finally, taking all four gives $3 \times 3 \times 5 \times 5 = 225$. 

Collecting all of these together, the factors of 225 are: 1, 3, 5, 9, 15, 25, 45, 75, 225.

## Worked Example

Let us apply the division method to find the prime factorisation of 1200. The smallest prime that divides 1200 is 2, and we can keep dividing by 2 for a while: $1200 \div 2 = 600$, then $600 \div 2 = 300$, then $300 \div 2 = 150$, then $150 \div 2 = 75$. That is four divisions by 2. Now 2 no longer divides 75, but 3 does, and $75 \div 3 = 25$. Then 5 divides 25, and $25 \div 5 = 5$. Finally 5 is prime, so we stop.

Collecting the primes we divided by, together with the 5 left at the end, the prime factorisation of 1200 is $1200 = 2 \times 2 \times 2 \times 2 \times 3 \times 5 \times 5$. You can check it: $16 \times 3 \times 25 = 1200$.

## Key points

*   Prime factorisation is the process of breaking down a number into the product of its prime factors.
*   The division method is a reliable way to find the prime factorisation of a number by repeatedly dividing by the smallest prime factor.
*   The resulting prime factors of a number are always the same, regardless of the starting pair of factors.
*   Once you have the prime factorisation of a number, you can find all of its factors by taking different combinations of the prime factors.
*   Prime factorisation is a useful tool for finding the HCF of two or more numbers.
