---
{
  "concept": "Bayes' Theorem",
  "slug": "bayes-theorem",
  "grade": 12,
  "language": "en",
  "subject": "maths",
  "area": "Probability",
  "model": "sarvam-105b",
  "settings": {
    "temperature": 0.3,
    "max_tokens": 8000,
    "reasoning_effort": "none"
  },
  "usage": {
    "completion_tokens": 1708,
    "prompt_tokens": 6823,
    "total_tokens": 8531,
    "completion_tokens_details": {
      "accepted_prediction_tokens": null,
      "audio_tokens": null,
      "reasoning_tokens": 0,
      "rejected_prediction_tokens": null
    },
    "prompt_tokens_details": null
  },
  "target_words": [
    1050,
    1450
  ],
  "generated_at": "2026-10-08T06:57:03",
  "source_grade": 12,
  "grade_delta": 0,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g12_maths_part2_chapter7_026",
      "chapter": "chapter7",
      "section": "13.5 Bayes' Theorem"
    },
    {
      "ref": "S2",
      "passage_id": "g12_maths_part2_chapter7_006",
      "chapter": "chapter7",
      "section": "13.2.1 Properties of conditional probability"
    },
    {
      "ref": "S3",
      "passage_id": "g12_maths_part2_chapter7_001",
      "chapter": "chapter7",
      "section": "13.1 Introduction"
    }
  ],
  "citation_check": {
    "cited": [
      "1",
      "2"
    ],
    "invented_citations": [],
    "unused_sources": [
      "3"
    ],
    "explanatory_paragraphs_without_a_citation": 6,
    "words": 943,
    "target_words": [
      1050,
      1450
    ],
    "untraceable_sections": 0,
    "ok": true,
    "structural_problems": [],
    "grounding": {
      "cited_sentences": 5,
      "checked": 3,
      "not_judgeable_mostly_maths": 2,
      "cites_a_source_never_given": 0,
      "unsupported": [
        {
          "claim": "However, the real challenge arises when we observe an outcome and need to figure out the probability of the initial condition that caused it .",
          "cites": [
            "S1"
          ],
          "support_probability": 0.1
        },
        {
          "claim": "Since there are 430 girls out of 1000 students, $P(F) = \\frac{430}{1000} = 0.43$ .",
          "cites": [
            "S2"
          ],
          "support_probability": 0.106
        }
      ],
      "unsupported_fraction": 0.667,
      "threshold": 0.5,
      "max_unsupported_fraction": 0.34
    }
  },
  "terms": [
    "bayes' theorem",
    "prior probability",
    "likelihood",
    "total probability",
    "conditional probability",
    "reverse probability"
  ]
}
---

# Bayes' Theorem

Bayes' Theorem is a powerful tool in probability that allows us to update our beliefs about an event after we have observed some new evidence. In everyday life, we often want to know the probability of a cause given an effect, rather than just the probability of an effect given a cause. This theorem, published posthumously in 1763, provides a mathematical way to reverse conditional probabilities. It is particularly useful when we need to find the reverse probability of a hypothesis after an event has occurred.

## The Problem of Reverse Probability

In standard conditional probability, we know the initial conditions and want to find the outcome. For instance, we can easily calculate the probability of drawing a white ball if we are already told that the ball came from Bag I. However, the real challenge arises when we observe an outcome and need to figure out the probability of the initial condition that caused it. This is known as reverse probability, and it requires a different approach than standard conditional probability.

## The Formula and Its Components

The formula for Bayes' Theorem is given by:
$$ P(B_i|A) = \frac{P(B_i)P(A|B_i)}{P(A)} $$
Here, $P(B_i)$ represents the prior probability of the event $B_i$ occurring before any new evidence is observed. The term $P(A|B_i)$ is the likelihood, which is the probability of observing the evidence $A$ given that $B_i$ has occurred. The denominator, $P(A)$, is the total probability of the evidence $A$ occurring, regardless of the cause.

To understand this better, consider a practical example involving a school. Suppose a school has 1000 students, out of which 430 are girls. We are told that 10% of the girls study in Class XII. We want to find the probability that a student chosen at random studies in Class XII, given that the chosen student is a girl.

Let $E$ denote the event that a randomly chosen student studies in Class XII, and let $F$ denote the event that the randomly chosen student is a girl. We are looking for $P(E|F)$. 

First, we calculate the prior probability of selecting a girl, $P(F)$. Since there are 430 girls out of 1000 students, $P(F) = \frac{430}{1000} = 0.43$.

Next, we need to find the joint probability of both events occurring, $P(E \cap F)$. Since 10% of the 430 girls are in Class XII, there are 43 girls in Class XII. Therefore, $P(E \cap F) = \frac{43}{1000} = 0.043$.

Using the conditional probability formula, we can now calculate $P(E|F)$:
$$ P(E|F) = \frac{P(E \cap F)}{P(F)} = \frac{0.043}{0.43} = 0.1 $$
Thus, the probability that a student studies in Class XII given that they are a girl is 0.1.

## Applying Bayes' Theorem

Now, let's apply Bayes' Theorem to find the probability that a student is a girl given that they study in Class XII. We want to find $P(F|E)$.

Using the formula:
$$ P(F|E) = \frac{P(F)P(E|F)}{P(E)} $$
We already know $P(F) = 0.43$ and $P(E|F) = 0.1$. To find $P(E)$, we need to know the total number of students in Class XII. However, the problem does not provide this information directly. If we assume that only the 43 girls are in Class XII (which is not stated in the extract), then $P(E) = \frac{43}{1000} = 0.043$.

Plugging these values into the formula:
$$ P(F|E) = \frac{0.43 \times 0.1}{0.043} = \frac{0.043}{0.043} = 1 $$
This result suggests that if only girls are in Class XII, then the probability of a student being a girl given that they are in Class XII is 1, which is logical but relies on an unstated assumption.

## Worked Example: Two Bags and Balls

To further illustrate Bayes' Theorem, consider the classic problem of two bags. Bag I contains 2 white and 3 red balls, while Bag II contains 4 white and 5 red balls. We randomly select one bag and draw a ball from it. We want to find the probability that the ball was drawn from Bag II given that it is white.

Let $B_1$ be the event that Bag I is selected, and $B_2$ be the event that Bag II is selected. Since we select the bag at random, $P(B_1) = \frac{1}{2}$ and $P(B_2) = \frac{1}{2}$.

The probability of drawing a white ball from Bag I is $P(A|B_1) = \frac{2}{5}$, and from Bag II is $P(A|B_2) = \frac{4}{9}$.

The total probability of drawing a white ball, $P(A)$, is:
$$ P(A) = P(B_1)P(A|B_1) + P(B_2)P(A|B_2) = \frac{1}{2} \times \frac{2}{5} + \frac{1}{2} \times \frac{4}{9} = \frac{1}{5} + \frac{2}{9} = \frac{19}{45} $$

Now, using Bayes' Theorem to find $P(B_2|A)$:
$$ P(B_2|A) = \frac{P(B_2)P(A|B_2)}{P(A)} = \frac{\frac{1}{2} \times \frac{4}{9}}{\frac{19}{45}} = \frac{\frac{2}{9}}{\frac{19}{45}} = \frac{2}{9} \times \frac{45}{19} = \frac{10}{19} $$
Thus, the probability that the white ball was drawn from Bag II is $\frac{10}{19}$.

## Key points

*   Bayes' Theorem allows us to reverse conditional probabilities, finding the probability of a cause given an effect.
*   The formula is $ P(B_i|A) = \frac{P(B_i)P(A|B_i)}{P(A)} $, where $P(B_i)$ is the prior probability, $P(A|B_i)$ is the likelihood, and $P(A)$ is the total probability of the evidence.
*   The total probability $P(A)$ can be calculated using the law of total probability, which sums the probabilities of the evidence across all possible causes.
*   In the school example, the probability of a student being a girl given that they are in Class XII depends on the total number of students in Class XII, which must be known to apply the theorem correctly.
*   Bayes' Theorem is widely used in statistics, machine learning, and medical testing to update probabilities based on new evidence.