---
{
  "concept": "Arithmetic Progressions",
  "slug": "arithmetic-progressions",
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
    "completion_tokens": 1085,
    "prompt_tokens": 5862,
    "total_tokens": 6947,
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
  "generated_at": "2026-10-17T22:03:30",
  "source_grade": 10,
  "grade_delta": 0,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g10_maths_chapter5_007",
      "chapter": "chapter5",
      "section": "5.2 Arithmetic Progressions"
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
    "explanatory_paragraphs_without_a_citation": 0,
    "words": 697,
    "target_words": [
      1000,
      1350
    ],
    "untraceable_sections": 0,
    "ok": true,
    "structural_problems": [
      "length: 697 words, under 1000",
      "arithmetic: '1 = 10 - 4 = 6' -- 1 is 1, the page writes 10 - 4",
      "arithmetic: '2 = 16 - 10 = 6' -- 2 is 2, the page writes 16 - 10",
      "arithmetic: '3 = 22 - 16 = 6' -- 3 is 3, the page writes 22 - 16"
    ]
  },
  "terms": [
    "arithmetic progression",
    "common difference",
    "first term",
    "succeeding term",
    "finite ap",
    "infinite ap",
    "general form"
  ]
}
---

# Arithmetic Progressions

An arithmetic progression is a sequence of numbers where each term after the first is found by adding a fixed number to the previous term. This fixed number is called the common difference. Understanding arithmetic progressions is essential because they model many real-world situations, such as calculating savings over time or tracking decreasing temperatures.

## Definition and General Form

In an arithmetic progression, every successive term is obtained by adding a fixed number to the preceding term, except for the first term. This fixed number is called the common difference of the AP. The common difference can be positive, negative, or zero.

We denote the first term of an AP by $a_1$, the second term by $a_2, \ldots$, the $n$th term by $a_n$, and the common difference by $d$. Then the AP becomes $a_1, a_2, a_3, \ldots, a_n$.

The condition for an AP is that the difference between any two consecutive terms is constant:
$$ a_2 - a_1 = a_3 - a_2 = \dots = a_n - a_{n-1} = d $$

If we call the first term $a$, then the AP is
$$ a, \; a + d, \; a + 2d, \; a + 3d, \; \ldots $$
This is called the general form of an AP. Each term is the first term plus some number of copies of $d$.

Here are some everyday lists that are APs:
- The heights of a row of steps, if each step is 15 cm higher than the last: 15, 30, 45, 60, ... Here $a = 15$ and $d = 15$.
- The number of seats in each row of a hall, if the first row has 20 seats and each row behind it has 2 more: 20, 22, 24, 26, ... Here $a = 20$ and $d = 2$.
- The temperature at the start of each hour on an evening when it falls by 2 degrees every hour, beginning at 30: 30, 28, 26, 24, ... Here $a = 30$ and $d = -2$.

## Finite and Infinite APs

An arithmetic progression can be finite or infinite. A finite AP has a last term, while an infinite AP does not.

For example, 2, 4, 6, 8, 10 has only five terms. Such an AP is called a finite AP, and its last term is 10. Similarly, the list of seats in a hall with exactly 12 rows is a finite AP.

On the other hand, 1, 4, 7, 10, ... goes on for ever. It is called an infinite arithmetic progression, and it has no last term.

## Finding the Common Difference

To know about an AP, you need to know both the first term $a$ and the common difference $d$. If you are given a list of numbers, you can check if it is an AP by finding $d$.

In an AP, every succeeding term is obtained by adding $d$ to the preceding term. So, $d$, found by subtracting any term from its succeeding term (the term which immediately follows it), should be the same for an AP.

In general, for an AP $a_1, a_2, \ldots, a_n$, we have:
$$ d = a_{k+1} - a_k $$
where $a_{k+1}$ and $a_k$ are the $(k+1)$th and the $k$th terms respectively.

To obtain $d$ in a given AP, you need not find all of $a_2 - a_1, a_3 - a_2, a_4 - a_3, \ldots$. It is enough to find only one of them.

When finding $d$, you should subtract the $k$th term from the $(k+1)$th term, even if the $(k+1)$th term is smaller.

For example, in the list 9, 5, 1, $-3$, ..., each term is 4 less than the one before it. So $d = 5 - 9 = -4$, and this is an AP with a negative common difference. In an AP where $d = 0$, such as 3, 3, 3, 3, ..., every term is the same.

Not every list with a pattern is an AP. Consider 1, 3, 6, 10, ... Here $3 - 1 = 2$, but $6 - 3 = 3$. The differences are not the same, so this list is not an AP.

## Worked Example

Example: For the list of numbers 4, 10, 16, 22, ..., determine if it is an AP and find the next two terms.

We have:
$$ a_2 - a_1 = 10 - 4 = 6 $$
$$ a_3 - a_2 = 16 - 10 = 6 $$
$$ a_4 - a_3 = 22 - 16 = 6 $$

Here, $a_{k+1} - a_k$ is the same every time. So, the given list of numbers forms an AP with the common difference $d = 6$.

The next two terms are:
$$ 22 + 6 = 28 $$
$$ 28 + 6 = 34 $$

Here is a second example, with a negative common difference. For the list 10, 7, 4, 1, ..., we have $7 - 10 = -3$, $4 - 7 = -3$ and $1 - 4 = -3$. The difference is the same each time, so it is an AP with $d = -3$. The next two terms are $1 + (-3) = -2$ and $-2 + (-3) = -5$.

## Key points

*   An arithmetic progression is a list of numbers where each term is obtained by adding a fixed number (the common difference) to the preceding term.
*   The general form of an AP is $a, a + d, a + 2d, a + 3d, \ldots$, where $a$ is the first term and $d$ is the common difference.
*   A finite AP has a last term, while an infinite AP does not.
*   To find the common difference $d$, subtract any term from its succeeding term: $d = a_{k+1} - a_k$.
*   The common difference $d$ can be positive, negative, or zero.