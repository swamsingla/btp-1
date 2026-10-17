---
{
  "concept": "Irrational Numbers",
  "slug": "irrational-numbers",
  "grade": 9,
  "language": "en",
  "subject": "maths",
  "area": "Number Systems",
  "hand_edited": "2026-10-17: Hand audit against Section 1.2. 'the number line has gaps' and 'just as real as rational numbers' (not in the book) removed; the two Hippacus myths, which the page had merged into one, restated as the book gives them; sqrt(n) rule given with the book's condition (after sqrt(n-1) is located); 'no gaps left' for Cantor-Dedekind replaced by the book's meaning; worked example step clarified. Note: the real-number sentences cite S1 though they come from the next passages of the same section.",
  "model": "sarvam-105b",
  "settings": {
    "temperature": 0.3,
    "max_tokens": 8000,
    "reasoning_effort": "none"
  },
  "usage": {
    "completion_tokens": 1292,
    "prompt_tokens": 7099,
    "total_tokens": 8391,
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
  "generated_at": "2026-10-17T04:57:51",
  "source_grade": 9,
  "grade_delta": 0,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g9_maths_chapter1_005",
      "chapter": "chapter1",
      "section": "1.2 Irrational Numbers"
    },
    {
      "ref": "S2",
      "passage_id": "g9_maths_chapter1_013",
      "chapter": "chapter1",
      "section": "1.3 Real Numbers and their Decimal Expansions"
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
    "explanatory_paragraphs_without_a_citation": 1,
    "words": 873,
    "target_words": [
      1000,
      1350
    ],
    "untraceable_sections": 0,
    "ok": true,
    "structural_problems": []
  },
  "terms": [
    "irrational numbers",
    "real numbers",
    "rational numbers",
    "pythagoras theorem",
    "number line",
    "square root"
  ]
}
---

# Irrational Numbers

So far in your maths studies, you have worked with numbers that can be written as fractions, where both the top and the bottom are integers. These are called rational numbers. However, there may be numbers on the number line that are not rational. There are indeed numbers that cannot be written in the form $\frac{p}{q}$ where $p$ and $q$ are integers and $q \neq 0$. These numbers are called irrational numbers, because they cannot be written as a ratio of integers.

## The Discovery of Irrational Numbers

The story of irrational numbers begins in ancient Greece with a group of mathematicians and philosophers known as the Pythagoreans, who followed the famous thinker Pythagoras. Around 400 BC, they were the first to discover that some numbers could not be written as a ratio of integers. There are many myths surrounding this discovery by the Pythagorean Hippacus of Croton. In all of them he has an unfortunate end, either for discovering that $\sqrt{2}$ is irrational or for disclosing the secret about $\sqrt{2}$ to people outside the secret Pythagorean sect.

## Defining Irrational Numbers

To understand what makes a number irrational, we need to look at how it is written. A number is called irrational if it cannot be written in the form $\frac{p}{q}$, where $p$ and $q$ are integers and $q \neq 0$. 

You might wonder if there are many of these numbers. Just like there are infinitely many rational numbers, there are also infinitely many irrational numbers. Some familiar examples include $\sqrt{2}$, $\sqrt{3}$, $\sqrt{15}$, and the number $\pi$. 

It is important to remember that when we use the symbol $\sqrt{}$, we assume it is the positive square root of the number. For example, $\sqrt{4} = 2$, even though both 2 and -2 are square roots of 4.

## Locating Irrational Numbers on the Number Line

You might ask how we can find the exact spot for an irrational number on the number line if we cannot write it as a simple fraction. We can locate them using geometry and the Pythagoras theorem. 

For example, to locate $\sqrt{2}$ on the number line, we can use a square with sides of 1 unit. By the Pythagoras theorem, the diagonal of this square is $\sqrt{1^2 + 1^2} = \sqrt{2}$. If we transfer this square onto the number line so that one corner is at zero, we can use a compass to draw an arc from the zero point with a radius equal to the diagonal. The point where the arc crosses the number line corresponds to $\sqrt{2}$.

We can find $\sqrt{3}$ in a similar way. Once we have located $\sqrt{2}$, we can construct a perpendicular line of unit length from the end of $\sqrt{2}$. Using the Pythagoras theorem again, we find that the distance from the start to the new end is $\sqrt{\left(\sqrt{2}\right)^2 + 1^2} = \sqrt{3}$. In the same way, we can locate $\sqrt{n}$ for any positive integer $n$, after $\sqrt{n-1}$ has been located.

## Real Numbers and the Number Line

When we put all rational numbers and all irrational numbers together into one big collection, we get what is called the collection of real numbers, denoted by $R$. 

This means that every real number is either rational or irrational. It also means that every real number can be represented by a unique point on the number line, and every point on the number line represents a unique real number. This is why we call the number line the real number line.

In the 1870s, two German mathematicians, Cantor and Dedekind, proved that there is a perfect match between every real number and a point on the number line. In other words, once the irrational numbers are put in along with the rational numbers, no number is left over on the number line.

## Worked Example

Let us try to locate $\sqrt{5}$ on the number line using the method described above. 

First, we know that $\sqrt{2}$ is located on the number line. We can construct a perpendicular line of unit length from the end of $\sqrt{2}$. Using the Pythagoras theorem, the distance from the start to the new end is $\sqrt{\left(\sqrt{2}\right)^2 + 1^2} = \sqrt{3}$. 

Next, we construct another perpendicular line of unit length from the end of $\sqrt{3}$. The distance from the start to this new end is $\sqrt{\left(\sqrt{3}\right)^2 + 1^2} = \sqrt{4} = 2$. 

Finally, we construct one more perpendicular line of unit length at the end of the segment of length 2. The distance from the start to this final end is $\sqrt{2^2 + 1^2} = \sqrt{5}$. By using a compass, we can draw an arc from the zero point with a radius of $\sqrt{5}$ to find its exact location on the number line.

## Key points

*   An irrational number cannot be written in the form $\frac{p}{q}$, where $p$ and $q$ are integers and $q \neq 0$.
*   There are infinitely many irrational numbers, such as $\sqrt{2}$, $\sqrt{3}$, $\sqrt{15}$, and $\pi$.
*   The Pythagoreans in Greece discovered irrational numbers around 400 BC.
*   Irrational numbers can be located on the number line using the Pythagoras theorem and a compass.
*   The collection of all rational numbers and irrational numbers together is called the real numbers, denoted by $R$.