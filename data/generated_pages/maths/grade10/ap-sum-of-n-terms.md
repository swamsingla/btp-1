---
{
  "concept": "Sum of First n Terms of an AP",
  "slug": "ap-sum-of-n-terms",
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
    "completion_tokens": 1706,
    "prompt_tokens": 5846,
    "total_tokens": 7552,
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
  "generated_at": "2026-10-17T22:03:50",
  "source_grade": 10,
  "grade_delta": 0,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g10_maths_chapter5_029",
      "chapter": "chapter5",
      "section": "5.4 Sum of First $n$ Terms of an AP"
    }
  ],
  "citation_check": {
    "cited": [
      "1"
    ],
    "invented_citations": [],
    "unused_sources": [],
    "explanatory_paragraphs_without_a_citation": 2,
    "words": 1095,
    "target_words": [
      1000,
      1350
    ],
    "untraceable_sections": 0,
    "ok": true,
    "structural_problems": []
  },
  "terms": [
    "arithmetic progression",
    "common difference",
    "first term",
    "last term",
    "nth term"
  ]
}
---

# Sum of First $n$ Terms of an AP

An arithmetic progression, or AP, is a sequence of numbers where the difference between consecutive terms is always the same. This constant difference is called the common difference, and the first term is simply the starting value. While you might already know how to find any specific term in an AP, adding up a long list of these terms one by one can be incredibly tedious and time-consuming. The sum of the first $n$ terms of an AP, denoted as $S_n$, gives us a powerful shortcut to find the total of any such sequence without having to write out every single number.

## The Story of Gauss

Imagine having to add up the numbers from 1 to 100. Doing this manually would take a very long time and leaves plenty of room for mistakes. The famous mathematician Carl Friedrich Gauss figured out a brilliant shortcut when he was just a young boy. He wrote the sum $S$ as $1 + 2 + 3 + \dots + 99 + 100$. Then, he wrote the exact same sum in reverse order: $100 + 99 + \dots + 3 + 2 + 1$. When he added these two rows together, he noticed that each column added up to exactly 101. Since there were 100 columns, the total was $100 \times 101$. Because this total counts the sum twice, he divided by 2 to get the final answer: $\frac{100 \times 101}{2} = 5050$.

## The General Formula

We can apply the exact same pairing trick to any arithmetic progression. Let us look at an AP with first term $a$ and common difference $d$. The terms look like this: $a, a + d, a + 2d, \dots$ up to the $n$th term, which is $a + (n - 1)d$. If we call the total sum of these $n$ terms $S$, we can write it out as:

$$ S = a + (a + d) + (a + 2d) + \dots + [a + (n - 1)d] $$

Now, we write the exact same sum in reverse order, starting from the last term and moving backward to the first:

$$ S = [a + (n - 1)d] + [a + (n - 2)d] + \dots + (a + d) + a $$

If we add these two equations together, we get $2S$. When we add the terms side by side, every single pair adds up to the exact same value: $2a + (n - 1)d$. Since there are $n$ such pairs, we can write:

$$ 2S = n [2a + (n - 1)d] $$

To find $S$, we simply divide both sides by 2. This gives us the standard formula for the sum of the first $n$ terms of an AP:

$$ S_n = \frac{n}{2} [2a + (n - 1)d] $$

This formula involves four quantities: the sum $S_n$, the number of terms $n$, the first term $a$, and the common difference $d$. If you know any three of these values, you can easily calculate the fourth.

## The Alternative Formula

Sometimes, a problem gives you the first term and the very last term of an AP, but it does not give you the common difference. In these situations, we can use a slightly different version of the formula that is much more convenient. We know that the $n$th term of an AP is $a_n = a + (n - 1)d$. We can substitute this into our original formula like this:

$$ S_n = \frac{n}{2} [a + (a + (n - 1)d)] $$

This simplifies to:

$$ S_n = \frac{n}{2} (a + a_n) $$

If there are exactly $n$ terms in the AP, the last term is often called $l$. So, we can write this as:

$$ S_n = \frac{n}{2} (a + l) $$

This form is incredibly useful because it allows you to find the total sum of a sequence even if you do not know how much the sequence increases by each step.

## Real-World Applications

Using these formulas makes solving everyday problems much faster. For example, imagine a parent who puts ₹100 into a child's money box on their first birthday, ₹150 on the second birthday, ₹200 on the third, and continues adding ₹50 every year. If we want to know the total amount saved by the child's 21st birthday, we can treat this as the sum of the first 21 terms of an AP. Here, the first term $a$ is ₹100, the common difference $d$ is ₹50, and the number of terms $n$ is 21. Plugging these into our formula gives us:

$$ S_{21} = \frac{21}{2} [2 \times 100 + (21 - 1) \times 50] = \frac{21}{2} [200 + 1000] = \frac{21}{2} \times 1200 = 12600 $$

So, the total amount collected in the money box by the 21st birthday is ₹12,600.

## Worked Example

Consider the arithmetic progression: 8, 3, -2, ... We want to find the sum of the first 22 terms of this sequence. First, we identify the values we know. The first term $a$ is 8. The second term is 3, so the common difference $d$ is $3 - 8 = -5$. The number of terms $n$ is 22. Now, we substitute these values into our standard sum formula:

$$ S_{22} = \frac{22}{2} [2 \times 8 + (22 - 1) \times (-5)] = 11 [16 + 21 \times (-5)] = 11 [16 - 105] = 11 \times (-89) = -979 $$

Therefore, the sum of the first 22 terms of this arithmetic progression is -979.

## Key points
- The sum of the first $n$ terms of an AP is given by $S_n = \frac{n}{2} [2a + (n - 1)d]$, where $a$ is the first term and $d$ is the common difference.
- If the first term $a$ and the last term $l$ are known, you can use the formula $S_n = \frac{n}{2} (a + l)$.
- The formula involves four quantities ($S_n, a, d, n$), and knowing any three allows you to find the fourth.
- Gauss's pairing trick for $1 + 2 + \dots + 100$ is the same idea as the general formula: write the sum forwards and backwards, and add.
- The sum of the first $n$ positive integers is a special case of the formula with $a = 1$ and $d = 1$, giving $S_n = \frac{n(n + 1)}{2}$.