# Bernoulli Trials

Repeated independent trials with two outcomes form the foundation of many real-world probability models. [S1] In this chapter, we shall discuss the important concept of conditional probability of an event given that another event has occurred, which will be helpful in understanding the Bayes' theorem, multiplication rule of probability and independence of events. [S1] We shall also learn an important concept of random variable and its probability distribution and also the mean and variance of a probability distribution. [S1] In the last section of the chapter, we shall study an important discrete probability distribution called Binomial distribution. [S1] Throughout this chapter, we shall take up the experiments having equally likely outcomes, unless stated otherwise. [S1]

## Defining the Terms

A Bernoulli trial is a random experiment with exactly two possible outcomes. [S1] We label one of these outcomes as a success and the other as a failure. [S1] The probability of success is denoted by $p$, and the probability of failure is denoted by $q = 1 - p$. [S1] For a sequence of trials to be considered Bernoulli trials, three specific conditions must be met. [S1] First, the trials must be independent, meaning the outcome of one trial does not affect the outcome of any other trial. [S1] Second, the probability of success must remain constant for every trial. [S1] Third, each trial must result in exactly one of the two outcomes. [S1]

## The Binomial Distribution

When we conduct a fixed number of Bernoulli trials, the number of successes we observe follows a specific probability pattern known as the binomial distribution. [S1] Suppose we perform $n$ independent trials and we are interested in the probability of obtaining exactly $r$ successes. [S1] The formula for this probability is given by:

$$
P(X = r) = \binom{n}{r} p^r q^{n-r}
$$

where $\binom{n}{r} = \frac{n!}{r!(n-r)!}$ is the binomial coefficient. [S1] This formula calculates the probability of getting exactly $r$ successes in $n$ trials, where the probability of success on any single trial is $p$ and the probability of failure is $q$. [S1]

## The Mean and Variance

The binomial distribution has specific measures of central tendency and spread. [S1] The mean, or the expected number of successes, is given by:

$$
\mu = np
$$

[S1] The variance, which measures the spread of the distribution, is given by:

$$
\sigma^2 = npq
$$

[S1] The standard deviation is the square root of the variance, $\sigma = \sqrt{npq}$. [S1] These measures help us understand the typical number of successes we can expect and how much the actual number of successes might vary from trial to trial. [S1]

## Worked example

Consider a scenario where a student is taking a multiple-choice test with 10 questions, and each question has 4 options. [S1] The student guesses the answer to each question randomly. [S1] Let us define a success as the student guessing a question correctly. [S1] The probability of success on any single question is $p = \frac{1}{4}$, and the probability of failure is $q = \frac{3}{4}$. [S1] We want to find the probability that the student guesses exactly 3 questions correctly out of 10. [S1]

Using the binomial distribution formula, we have $n = 10$, $r = 3$, $p = \frac{1}{4}$, and $q = \frac{3}{4}$. [S1] The probability of exactly 3 successes is:

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

So, the probability of guessing exactly 3 questions correctly is approximately 0.2503, or about 25.03%. [S1]

## Key points

- A Bernoulli trial is a random experiment with exactly two outcomes, success and failure, where the probability of success is $p$ and failure is $q = 1 - p$. [S1]
- For a sequence of trials to be Bernoulli trials, the trials must be independent, the probability of success must remain constant, and each trial must have exactly two outcomes. [S1]
- The number of successes in $n$ Bernoulli trials follows a binomial distribution, with probability $P(X = r) = \binom{n}{r} p^r q^{n-r}$. [S1]
- The mean of a binomial distribution is $\mu = np$, and the variance is $\sigma^2 = npq$. [S1]
- The binomial distribution is a discrete probability distribution, and its study is an important part of understanding random variables and their distributions. [S1]

<!-- TERMS: Bernoulli trial, binomial distribution, binomial coefficient, mean, variance, standard deviation, random variable, discrete probability distribution, success, failure, probability of success, probability of failure -->