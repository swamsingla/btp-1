---
{
  "concept": "nth Term of an AP",
  "slug": "ap-nth-term",
  "grade": 10,
  "language": "en",
  "subject": "maths",
  "area": "Sequences",
  "model": "sarvam-105b",
  "settings": {
    "temperature": 0.3,
    "max_tokens": 8000,
    "reasoning_effort": "none"
  },
  "usage": {
    "completion_tokens": 1426,
    "prompt_tokens": 6115,
    "total_tokens": 7541,
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
  "generated_at": "2026-10-17T22:03:40",
  "source_grade": 10,
  "grade_delta": 0,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g10_maths_chapter5_015",
      "chapter": "chapter5",
      "section": "5.3 nth Term of an AP"
    }
  ],
  "citation_check": {
    "cited": [
      "1"
    ],
    "invented_citations": [],
    "unused_sources": [],
    "explanatory_paragraphs_without_a_citation": 10,
    "words": 897,
    "target_words": [
      1000,
      1350
    ],
    "untraceable_sections": 0,
    "ok": true,
    "structural_problems": [
      "arithmetic: '-81 = 21 - 3' -- -81 is -81, the page writes 21 - 3",
      "arithmetic: '-81 = 24 - 3' -- -81 is -81, the page writes 24 - 3"
    ]
  },
  "terms": [
    "arithmetic progression",
    "first term",
    "common difference",
    "general term",
    "nth term"
  ]
}
---

# nth Term of an AP

In your previous classes, you have studied arithmetic progressions, or APs, where a sequence of numbers increases or decreases by a constant amount. Finding the $n$th term of an AP is a powerful shortcut that saves you from adding the common difference over and over again. This formula is essential for solving real-world problems, such as calculating future values in finance or determining the number of items in a specific row of a pattern.

## The General Term Formula

An arithmetic progression is a sequence of numbers where the difference between any two consecutive terms is always the same. This fixed amount is called the common difference, denoted by $d$. The very first number in the sequence is called the first term, denoted by $a$. 

To find any term in the sequence, we use a specific algebraic rule. Let us look at the beginning of the sequence:
- The first term is $a$.
- The second term is $a + d$, which can be written as $a + (2 - 1)d$.
- The third term is $a + 2d$, which is $a + (3 - 1)d$.
- The fourth term is $a + 3d$, which is $a + (4 - 1)d$.

Observing this pattern, you can see that for any given term, we start with the first term $a$ and add the common difference $d$ a certain number of times. The number of times we add $d$ is exactly one less than the term's position in the sequence. Therefore, the $n$th term of an AP with first term $a$ and common difference $d$ is given by $a_n = a + (n - 1)d$. The $n$th term is also called the general term of the AP.

## Finding a Specific Term

Using the formula $a_n = a + (n - 1)d$, you can find the value of any term if you know the first term, the common difference, and the position of the term.

Example: Find the 10th term of the AP: 2, 7, 12, ...

Here, the first term $a = 2$. The common difference $d = 7 - 2 = 5$. We want to find the 10th term, so $n = 10$. Substituting these values into the formula gives:
$a_{10} = 2 + (10 - 1) \times 5$
$a_{10} = 2 + 45$
$a_{10} = 47$

Therefore, the 10th term of the given AP is 47.

## Finding the Position of a Term

Sometimes, you might already know the value of a specific term and need to find out which position it holds in the sequence. You can rearrange the general term formula to solve for $n$.

Example: Which term of the AP : 21, 18, 15, ... is -81?

Here, $a = 21$ and $d = 18 - 21 = -3$. We are given that $a_n = -81$. We substitute these values into the formula:
$-81 = 21 + (n - 1)(-3)$
$-81 = 21 - 3n + 3$
$-81 = 24 - 3n$
$-105 = -3n$
$n = 35$

Therefore, the 35th term of the given AP is -81.

## Counting the Terms and Testing a Number

The same formula tells us how many terms a finite AP has. Example: How many terms are there in the AP 3, 8, 13, ..., 183?

Here $a = 3$, $d = 8 - 3 = 5$, and the last term is $a_n = 183$. Substituting into $a_n = a + (n - 1)d$:
$$ 183 = 3 + (n - 1) \times 5 $$
$$ 180 = (n - 1) \times 5 $$
$$ n - 1 = 36 $$
$$ n = 37 $$
So the AP has 37 terms.

The position $n$ must always be a whole number, because it counts places in the list. This lets us test whether a number belongs to an AP. Example: Is 301 a term of the AP 5, 11, 17, 23, ...?

Here $a = 5$ and $d = 6$. If 301 were a term, then $301 = 5 + (n - 1) \times 6$, so $(n - 1) \times 6 = 296$ and $n - 1 = \frac{296}{6} = 49\frac{1}{3}$. This is not a whole number, so 301 is not a term of this AP.

## Real-World Applications

The concept of the $n$th term is not just an abstract mathematical rule; it is highly useful for solving practical problems involving linear growth or decay.

Example: A sum of ₹ 1000 is invested at 8% simple interest per year. Calculate the interest at the end of each year. Do these interests form an AP? If so, find the interest at the end of 30 years making use of this fact.

The simple interest formula is $\text{Simple Interest} = \frac{\mathrm{P} \times \mathrm{R} \times \mathrm{T}}{100}$.
- The interest at the end of the 1st year = $\frac{1000 \times 8 \times 1}{100}$ = ₹ 80
- The interest at the end of the 2nd year = $\frac{1000 \times 8 \times 2}{100}$ = ₹ 160
- The interest at the end of the 3rd year = $\frac{1000 \times 8 \times 3}{100}$ = ₹ 240

The interests (in ₹) at the end of the 1st, 2nd, 3rd, ... years, respectively are $80, 160, 240, \dots$.

It is an AP as the difference between the consecutive terms in the list is 80, i.e., $d = 80$. Also, $a = 80$. So, to find the interest at the end of 30 years, we shall find $a_{30}$.
$a_{30} = a + (30 - 1) d = 80 + 29 \times 80 = 2400$

So, the interest at the end of 30 years will be ₹ 2400.

If an AP has $m$ terms, its last term is $a_m$, which is sometimes written as $l$. For a finite AP with first term $a$, common difference $d$ and $m$ terms, the last term is $l = a + (m - 1)d$.

## Key points

- The $n$th term of an AP is given by the formula $a_n = a + (n - 1)d$, where $a$ is the first term and $d$ is the common difference.
- You can find the value of any specific term by identifying $a$, $d$, and $n$ and substituting them into the formula.
- If you know the value of a term and the first term and common difference, you can rearrange the formula to solve for $n$ and find its position.
- The position $n$ must be a whole number, so a number is a term of an AP only if solving for $n$ gives a whole number.
- The general term formula is widely used to solve real-world problems involving uniform increments or decrements, such as simple interest or linear patterns.
- The last term of an AP, if there are $m$ terms, is denoted by $a_m$ or sometimes by $l$.