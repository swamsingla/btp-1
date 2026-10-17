---
{
  "concept": "Bernoulli Trials",
  "slug": "bernoulli-trials",
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
    "completion_tokens": 1324,
    "prompt_tokens": 5451,
    "total_tokens": 6775,
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
  "generated_at": "2026-10-08T07:40:08",
  "source_grade": 12,
  "grade_delta": 0,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g12_maths_part2_chapter7_001",
      "chapter": "chapter7",
      "section": "13.1 Introduction"
    },
    {
      "ref": "S2",
      "passage_id": "g12_maths_part2_chapter7_011",
      "chapter": "chapter7",
      "section": "13.2.1 Properties of conditional probability"
    },
    {
      "ref": "S3",
      "passage_id": "g12_maths_part2_chapter7_026",
      "chapter": "chapter7",
      "section": "13.5 Bayes' Theorem"
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
    "words": 787,
    "target_words": [
      1050,
      1450
    ],
    "untraceable_sections": 0,
    "ok": true,
    "short": [
      "length: 787 words, under 1050"
    ],
    "structural_problems": [],
    "grounding": {
      "cited_sentences": 7,
      "checked": 7,
      "not_judgeable_mostly_maths": 0,
      "cites_a_source_never_given": 0,
      "unsupported": [
        {
          "claim": "Repeated independent trials with two outcomes form the foundation of many real-world probability models.  In this chapter, we shall discuss the important concept of conditional probability of an event",
          "cites": [
            "S1"
          ],
          "support_probability": 0.045
        },
        {
          "claim": "A Bernoulli trial is a random experiment with exactly two possible outcomes.  We label one of these outcomes as a success and the other as a failure.  The probability of success is denoted by $p$, and",
          "cites": [
            "S1"
          ],
          "support_probability": 0.301
        },
        {
          "claim": "When we conduct a fixed number of Bernoulli trials, the number of successes we observe follows a specific probability pattern known as the binomial distribution.  Suppose we perform $n$ independent tr",
          "cites": [
            "S1"
          ],
          "support_probability": 0.024
        },
        {
          "claim": "where $\\binom{n}{r} = \\frac{n!}{r!(n-r)!}$ is the binomial coefficient.  This formula calculates the probability of getting exactly $r$ successes in $n$ trials, where the probability of success on any",
          "cites": [
            "S1"
          ],
          "support_probability": 0.113
        },
        {
          "claim": "The binomial distribution has specific measures of central tendency and spread.  The mean, or the expected number of successes, is given by:",
          "cites": [
            "S1"
          ],
          "support_probability": 0.103
        },
        {
          "claim": "The variance, which measures the spread of the distribution, is given by:",
          "cites": [
            "S1"
          ],
          "support_probability": 0.373
        },
        {
          "claim": "The standard deviation is the square root of the variance, $\\sigma = \\sqrt{npq}$.  These measures help us understand the typical number of successes we can expect and how much the actual number of suc",
          "cites": [
            "S1"
          ],
          "support_probability": 0.072
        }
      ],
      "unsupported_fraction": 1.0,
      "threshold": 0.5,
      "max_unsupported_fraction": 0.34
    }
  },
  "terms": [
    "bernoulli trial",
    "binomial distribution",
    "binomial coefficient",
    "mean",
    "variance",
    "standard deviation",
    "random variable",
    "discrete probability distribution",
    "success",
    "failure",
    "probability of success",
    "probability of failure"
  ]
}
---

# Bernoulli Trials

Repeated independent trials with two outcomes form the foundation of many real-world probability models. In this chapter, we shall discuss the important concept of conditional probability of an event given that another event has occurred, which will be helpful in understanding the Bayes' theorem, multiplication rule of probability and independence of events. We shall also learn an important concept of random variable and its probability distribution and also the mean and variance of a probability distribution. In the last section of the chapter, we shall study an important discrete probability distribution called Binomial distribution. Throughout this chapter, we shall take up the experiments having equally likely outcomes, unless stated otherwise.

## Defining the Terms

A Bernoulli trial is a random experiment with exactly two possible outcomes. We label one of these outcomes as a success and the other as a failure. The probability of success is denoted by $p$, and the probability of failure is denoted by $q = 1 - p$. For a sequence of trials to be considered Bernoulli trials, three specific conditions must be met. First, the trials must be independent, meaning the outcome of one trial does not affect the outcome of any other trial. Second, the probability of success must remain constant for every trial. Third, each trial must result in exactly one of the two outcomes.

## The Binomial Distribution

When we conduct a fixed number of Bernoulli trials, the number of successes we observe follows a specific probability pattern known as the binomial distribution. Suppose we perform $n$ independent trials and we are interested in the probability of obtaining exactly $r$ successes. The formula for this probability is given by:

$$
P(X = r) = \binom{n}{r} p^r q^{n-r}
$$

where $\binom{n}{r} = \frac{n!}{r!(n-r)!}$ is the binomial coefficient. This formula calculates the probability of getting exactly $r$ successes in $n$ trials, where the probability of success on any single trial is $p$ and the probability of failure is $q$.

## The Mean and Variance

The binomial distribution has specific measures of central tendency and spread. The mean, or the expected number of successes, is given by:

$$
\mu = np
$$ The variance, which measures the spread of the distribution, is given by:

$$
\sigma^2 = npq
$$ The standard deviation is the square root of the variance, $\sigma = \sqrt{npq}$. These measures help us understand the typical number of successes we can expect and how much the actual number of successes might vary from trial to trial.

## Worked example

Consider a scenario where a student is taking a multiple-choice test with 10 questions, and each question has 4 options. The student guesses the answer to each question randomly. Let us define a success as the student guessing a question correctly. The probability of success on any single question is $p = \frac{1}{4}$, and the probability of failure is $q = \frac{3}{4}$. We want to find the probability that the student guesses exactly 3 questions correctly out of 10.

Using the binomial distribution formula, we have $n = 10$, $r = 3$, $p = \frac{1}{4}$, and $q = \frac{3}{4}$. The probability of exactly 3 successes is:

$$
P(X = 3) = \binom{10}{3} \left(\frac{1}{4}\right)^3 \left(\frac{3}{4}\right)^7
$$

Calculating the binomial coefficient:

$$
\binom{10}{3} = \frac{10!}{3!(10-3)!} = \frac{10 \times 9 \times 8}{3 \times 2 \times 1} = 120
$$

Now, substituting the values:

$$
P(X = 3) = 120 \times \left(\frac{1}{4}\right)^3 \times \left(\frac{3}{4}\right)^7 = 120 \times \frac{1}{64} \times \frac{2187}{16384} = \frac{120 \times 2187}{64 \times 16384} = \frac{262440}{1048576} \approx 0.2503
$$

So, the probability of guessing exactly 3 questions correctly is approximately 0.2503, or about 25.03%.

## Key points

- A Bernoulli trial is a random experiment with exactly two outcomes, success and failure, where the probability of success is $p$ and failure is $q = 1 - p$.
- For a sequence of trials to be Bernoulli trials, the trials must be independent, the probability of success must remain constant, and each trial must have exactly two outcomes.
- The number of successes in $n$ Bernoulli trials follows a binomial distribution, with probability $P(X = r) = \binom{n}{r} p^r q^{n-r}$.
- The mean of a binomial distribution is $\mu = np$, and the variance is $\sigma^2 = npq$.
- The binomial distribution is a discrete probability distribution, and its study is an important part of understanding random variables and their distributions.