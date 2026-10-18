---
{
  "concept": "Theoretical Probability",
  "slug": "theoretical-probability",
  "grade": 10,
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
    "completion_tokens": 1804,
    "prompt_tokens": 6617,
    "total_tokens": 8421,
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
  "generated_at": "2026-10-18T00:59:32",
  "source_grade": 10,
  "grade_delta": 0,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g10_maths_chapter14_005",
      "chapter": "chapter14",
      "section": "14.1 Probability — A Theoretical Approach"
    }
  ],
  "citation_check": {
    "cited": [],
    "invented_citations": [],
    "unused_sources": [
      "1"
    ],
    "explanatory_paragraphs_without_a_citation": 7,
    "words": 1267,
    "target_words": [
      1000,
      1350
    ],
    "untraceable_sections": 4,
    "ok": false,
    "structural_problems": [
      "latex: '\\frac {4 8}{5 2}}' does not parse -- KaTeX parse error: Expected 'EOF', got '}' at position 17: â€¦frac {4 8}{5 2}}Ì²",
      "latex: '\\mathrm{P(\\overline{E})} = \\frac {\\text{Number of ' does not parse -- KaTeX parse error: Can't use function '\\overline' in text mode at position 74: â€¦ favourabl"
    ]
  },
  "terms": [
    "theoretical probability",
    "classical probability",
    "equally likely outcomes",
    "unbiased",
    "random toss",
    "elementary event",
    "complement",
    "sure event",
    "impossible event"
  ]
}
---

# Theoretical Probability

Probability helps us describe how likely something is to happen. In your previous classes, you might have learned about experimental probability by actually doing an experiment many times and keeping track of the results. However, sometimes it is not possible to repeat an experiment over and over, especially if it is very expensive or difficult. For example, you cannot launch a satellite many times to see how often it fails. In situations like this, we use theoretical probability. Theoretical probability relies on making certain assumptions about an experiment so that we can calculate the exact chance of an event happening without actually repeating the experiment.

## The Basic Assumption

Theoretical probability works best when we assume that all possible outcomes of an experiment are equally likely. This means that every single outcome has the exact same chance of occurring as any other outcome. When we talk about a coin, we assume it is 'fair', which means it is perfectly symmetrical so that there is no reason for it to land on one side more often than the other. We also call this property of the coin being 'unbiased'. When we speak of a 'random toss', we mean that the coin is allowed to fall freely without any bias or interference.

For another example, suppose we throw a die once. We always assume it is a fair die. The possible outcomes are the numbers 1, 2, 3, 4, 5, and 6. Each number has the exact same possibility of showing up on top. Therefore, these outcomes are equally likely.

However, it is important to remember that not every experiment in the real world has equally likely outcomes. For instance, suppose a bag contains 4 red balls and 1 blue ball, and you draw a ball without looking. The possible outcomes are a red ball or a blue ball. Are these outcomes equally likely? Since there are 4 red balls and only one blue ball, you are more likely to get a red ball than a blue ball. So, a red ball and a blue ball are not equally likely outcomes. However, the outcome of drawing a ball of any colour from the bag is equally likely. Because of this, in this chapter, we will assume that all the experiments we study have equally likely outcomes.

## The Formula

The theoretical probability (also called classical probability) of an event E, written as P(E), is defined as the ratio of the number of outcomes that are favourable to the event E, divided by the number of all possible outcomes of the experiment. This formula holds true under the condition that the outcomes of the experiment are equally likely.

$$
\mathrm{P(E)} = \frac {\text{Number of outcomes favourable to E}}{\text{Number of all possible outcomes of the experiment}}
$$

This definition of probability was given by Pierre Simon Laplace in 1795.

## Impossible and Sure Events

Using the formula for theoretical probability, we can easily understand the probability of impossible and sure events. An impossible event is an event that is impossible to occur, meaning there are zero outcomes favourable to it. If we throw a standard die once, what is the probability of getting a number 8? We know there are only six possible outcomes: 1, 2, 3, 4, 5, and 6. Since no face of the die is marked 8, there is no outcome favourable to 8. Therefore, the number of such outcomes is zero.

$$
\mathrm{P}(\text{getting } 8) = \frac {0}{6} = 0
$$

So, the probability of an impossible event is 0.

On the other hand, a sure event (or certain event) is an event that is sure to occur. If every face of a die is marked with a number less than 7, it is guaranteed that we will always get a number less than 7 when it is thrown once. In this case, the number of favourable outcomes is exactly the same as the number of all possible outcomes.

$$
\mathrm{P(E)} = \mathrm{P}(\text{getting a number less than } 7) = \frac {6}{6} = 1
$$

So, the probability of a sure event is 1.

## Complementary Events

In probability, we often deal with complementary events. If E is an event, then 'not E' is called the complement of the event E, and it is denoted by $\overline{E}$. The events E and $\overline{E}$ are called complementary events.

For any event E, the sum of the probability of the event and the probability of its complement is always 1.

$$
\mathrm{P(E) + P(\overline{E}) = 1}
$$

This gives us the rule:

$$
\mathrm{P(\overline{E}) = 1 - P(E)}
$$

This rule is very useful when we want to find the probability of an event not happening.

## Worked example

Let us consider a well-shuffled standard deck of 52 playing cards. These cards are divided into 4 suits: spades (♠), hearts (♥), diamonds (♦), and clubs (♣). Clubs and spades are black, while hearts and diamonds are red. The cards in each suit are ace, king, queen, jack, 10, 9, 8, 7, 6, 5, 4, 3, and 2. Kings, queens, and jacks are called face cards.

Suppose one card is drawn from this deck. We want to calculate the probability that the card drawn will not be a king.

First, we identify the total number of possible outcomes. Since the deck has 52 cards, the total number of possible outcomes is 52.

Next, we identify the event E. Let E be the event that the card drawn is a king. There are 4 kings in a standard deck (one in each suit). So, the number of outcomes favourable to E is 4.

Using the formula for theoretical probability, we can find the probability of drawing a king:

$$
\mathrm{P(E)} = \frac {\text{Number of outcomes favourable to E}}{\text{Number of all possible outcomes}} = \frac {4}{52}
$$

Now, we want to find the probability that the card is not a king. This is the complement of event E, which we denote by $\overline{E}$. We can use the rule for complementary events:

$$
\mathrm{P(\overline{E}) = 1 - P(E)}
$$

Substituting the value of P(E):

$$
\mathrm{P(\overline{E}) = 1 - \frac {4}{52} = \frac {48}{52}}
$$

Therefore, the probability that the card drawn will not be a king is $\frac {48}{52}$.

Alternatively, we could have calculated this directly by counting the number of cards that are not kings. Since there are 52 cards in total and 4 of them are kings, there are $52 - 4 = 48$ cards that are not kings. The number of outcomes favourable to the event 'not a king' is 48.

$$
\mathrm{P(\overline{E})} = \frac {\text{Number of outcomes favourable to } \overline{E}}{\text{Number of all possible outcomes}} = \frac {48}{52}
$$

Both methods give us the same result, confirming our calculation.

## Key points

*   Theoretical probability is calculated using the formula $\mathrm{P(E)} = \frac {\text{Number of outcomes favourable to E}}{\text{Number of all possible outcomes of the experiment}}$, provided the outcomes are equally likely.
*   An impossible event has a probability of 0, while a sure (or certain) event has a probability of 1.
*   For any event E, the probability of its complement $\overline{E}$ is given by the rule $\mathrm{P(\overline{E})} = 1 - \mathrm{P(E)}$.
*   The theoretical probability of an event E always lies between 0 and 1, inclusive: $0 \leq \mathrm{P(E)} \leq 1$.