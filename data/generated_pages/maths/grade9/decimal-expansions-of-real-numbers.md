---
{
  "concept": "Decimal Expansions of Real Numbers",
  "slug": "decimal-expansions-of-real-numbers",
  "grade": 9,
  "language": "en",
  "subject": "maths",
  "area": "Number Systems",
  "hand_edited": "2026-10-17: Hand audit against Section 1.3. Opening paragraph (calculator, 'For a Grade 9 student') replaced; the repeating-3 notation corrected from 3\\overline{3} to 3.\\overline{3}; duplicated sentence merged; the 1/6 worked example (not in the book) spelled out digit by digit and its over-tagging removed. All arithmetic checked: 639/250 = 2.556, 126/99 = 14/11, 1/6 = 0.1\\overline{6}.",
  "model": "sarvam-105b",
  "settings": {
    "temperature": 0.3,
    "max_tokens": 8000,
    "reasoning_effort": "none"
  },
  "usage": {
    "completion_tokens": 1662,
    "prompt_tokens": 7209,
    "total_tokens": 8871,
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
  "generated_at": "2026-10-17T04:58:01",
  "source_grade": 9,
  "grade_delta": 0,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g9_maths_chapter1_010",
      "chapter": "chapter1",
      "section": "1.3 Real Numbers and their Decimal Expansions"
    },
    {
      "ref": "S2",
      "passage_id": "g9_maths_chapter1_026",
      "chapter": "chapter1",
      "section": "1.5 Laws of Exponents for Real Numbers"
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
    "words": 858,
    "target_words": [
      1000,
      1350
    ],
    "untraceable_sections": 0,
    "ok": true,
    "structural_problems": []
  },
  "terms": [
    "rational numbers",
    "irrational numbers",
    "decimal expansion",
    "terminating decimals",
    "non-terminating recurring decimals",
    "non-terminating non-recurring decimals",
    "remainders",
    "quotient"
  ]
}
---

# Decimal Expansions of Real Numbers

When you write a real number using digits after a decimal point, you get its decimal expansion. In this page we look at the decimal expansions of rational and irrational numbers, to see whether the expansions can help us tell the two kinds of number apart.

## The Division Method and Remainders

To find the decimal expansion of a rational number, you divide the numerator by the denominator. As you do this, you will notice what happens to the remainders. There are only two things that can happen to the remainders during this division process. Either the remainder becomes zero after a certain stage, or it never becomes zero and starts repeating itself. 

If the remainder becomes zero, the division stops and the decimal expansion ends after a finite number of steps. If the remainder never becomes zero and starts repeating, the decimal expansion goes on forever. When the remainders repeat, we get a repeating block of digits in the quotient.

## Terminating Decimals

Let us look at the case where the remainder becomes zero. When you divide a fraction and the remainder finally hits zero, the decimal expansion terminates. We call these numbers terminating decimals. A great example of this is the fraction $\frac{7}{8}$. When you divide 7 by 8, the remainder eventually becomes zero, giving us the decimal expansion $0.875$. 

Other examples of terminating decimals include $\frac{1}{2} = 0.5$ and $\frac{639}{250} = 2.556$. In all of these cases, the decimal ends after a finite number of steps.

## Non-Terminating Recurring Decimals

Now let us look at the case where the remainder never becomes zero. In the examples of $\frac{10}{3}$ and $\frac{1}{7}$, we notice that the remainders repeat after a certain stage. This forces the decimal expansion to go on forever. In other words, we have a repeating block of digits in the quotient. We call this a non-terminating recurring decimal. 

For example, $\frac{10}{3} = 3.3333\ldots$. The usual way to show that 3 repeats in the quotient is to write it as $3.\overline{3}$. Similarly, since the block of digits 142857 repeats in the quotient of $\frac{1}{7}$, we write $\frac{1}{7}$ as $0.\overline{142857}$, where the bar above the digits indicates the block of digits that repeats. Another example is $3.57272\ldots$, which can be written as $3.5\overline{72}$.

## Converting Decimals to Fractions

You might wonder if a number with a terminating or non-terminating recurring decimal expansion is actually a rational number. The answer is yes. Every number with a non-terminating recurring decimal expansion can be expressed in the form $\frac{p}{q}$, where $p$ and $q$ are integers and $q \neq 0$.

For terminating decimals, this is easy. For example, you can show that 3.142678 is a rational number by writing it as $\frac{3142678}{1000000}$.

For non-terminating recurring decimals, you can use a trick with algebra. Let us take the example of $0.3333\ldots$. Let us call this number $x$, so $x = 0.3333\ldots$. Now, if we multiply $x$ by 10, we get $10x = 3.3333\ldots$. Since $x = 0.3333\ldots$, we can substitute $x$ back into the equation to get $10x = 3 + x$. Solving for $x$, we get $9x = 3$, which means $x = \frac{3}{9} = \frac{1}{3}$.

You can use this same trick for more complex repeating decimals. For example, to express $1.272727\ldots$ as a fraction, let $x = 1.272727\ldots$. Since two digits are repeating, we multiply $x$ by 100 to get $100x = 127.272727\ldots$. We can then write $100x = 126 + 1.272727\ldots$, which means $100x = 126 + x$. Subtracting $x$ from both sides gives $99x = 126$, so $x = \frac{126}{99} = \frac{14}{11}$.

## Non-Terminating Non-Recurring Decimals

So, what about the decimal expansion of irrational numbers? Because of the property above, we can conclude that the decimal expansion of an irrational number is non-terminating non-recurring. Moreover, a number whose decimal expansion is non-terminating non-recurring is irrational.

A famous example of an irrational number is $\sqrt{2}$. Its decimal expansion is $1.4142135623730950488016887242096\ldots$. Another famous irrational number is $\pi$, whose decimal expansion is $3.14159265358979323846264338327950\ldots$. It is important to note that we often take $\frac{22}{7}$ as an approximate value for $\pi$, but $\pi \neq \frac{22}{7}$.

## Worked example

Let us apply what we have learned to find the decimal expansion of a fraction. Suppose we want to find the decimal expansion of $\frac{1}{6}$. When we divide 1 by 6, the first digit after the decimal point is 1 and the remainder is 4. Dividing 40 by 6 then gives the digit 6 and the remainder 4 again, so the remainders are 4, 4, 4, and so on. Since the remainder keeps repeating, we get a repeating block of digits in the quotient. The decimal expansion of $\frac{1}{6}$ is $0.1\overline{6}$.

## Key points

*   The decimal expansion of a rational number is either terminating or non-terminating recurring.
*   A number with a terminating decimal expansion is rational, and a number with a non-terminating recurring decimal expansion is also rational.
*   The decimal expansion of an irrational number is non-terminating non-recurring.
*   A number with a non-terminating non-recurring decimal expansion is irrational.
*   The number of entries in the repeating string of remainders is less than the divisor.