# Conditional Probability

In earlier Classes, we have studied the probability as a measure of uncertainty of events in a random experiment. [S1] We discussed the axiomatic approach formulated by Russian Mathematician, A.N. Kolmogorov (1903-1987) and treated probability as a function of outcomes of the experiment. [S1] We have also established equivalence between the axiomatic theory and the classical theory of probability in case of equally likely outcomes. [S1] On the basis of this relationship, we obtained probabilities of events associated with discrete sample spaces. [S1] We have also studied the addition rule of probability. [S1] In this chapter, we shall discuss the important concept of conditional probability of an event given that another event has occurred, which will be helpful in understanding the Bayes' theorem, multiplication rule of probability and independence of events. [S1] We shall also learn an important concept of random variable and its probability distribution and also the mean and variance of a probability distribution. [S1] In the last section of the chapter, we shall study an important discrete probability distribution called Binomial distribution. [S1] Throughout this chapter, we shall take up the experiments having equally likely outcomes, unless stated otherwise. [S1]

## Defining the Terms

Let $E$ and $F$ be events of a sample space $S$ of an experiment. [S2] We discuss the important concept of conditional probability of an event given that another event has occurred. [S1] For the conditional probability, we consider the elementary events of the experiment to be equally likely and the corresponding definition of the probability of an event is used. [S2] However, the same definition can also be used in the general case where the elementary events of the sample space are not equally likely, the probabilities $P(E \cap F)$ and $P(F)$ being calculated accordingly. [S2]

The conditional probability of an event $E$ given that $F$ has occurred is given by:

$$
\mathrm{P} (\mathrm{E} | \mathrm{F}) = \frac { \mathrm{P} (\mathrm{E} \cap \mathrm{F}) }{ \mathrm{P} (\mathrm{F}) }
$$

[S2]

## Properties of Conditional Probability

Let $E$ and $F$ be events of a sample space $S$ of an experiment, then we have: [S2]

**Property 1** $\mathrm{P(S|F)} = \mathrm{P(F|F)} = 1$ [S2]

We know that

$$
\mathrm{P} (\mathrm{S} | \mathrm{F}) = \frac {\mathrm{P} (\mathrm{S} \cap \mathrm{F})}{\mathrm{P} (\mathrm{F})} = \frac {\mathrm{P} (\mathrm{F})}{\mathrm{P} (\mathrm{F})} = 1
$$

[S2]

$$
\mathrm{P} (\mathrm{F} | \mathrm{F}) = \frac {\mathrm{P} (\mathrm{F} \cap \mathrm{F})}{\mathrm{P} (\mathrm{F})} = \frac {\mathrm{P} (\mathrm{F})}{\mathrm{P} (\mathrm{F})} = 1
$$

[S2]

$$
\mathrm{P} (\mathrm{S} | \mathrm{F}) = \mathrm{P} (\mathrm{F} | \mathrm{F}) = 1
$$

[S2]

**Property 2** If $A$ and $B$ are any two events of a sample space $S$ and $F$ is an event of $S$ such that $\mathrm{P(F)} \neq 0$, then

$$
\mathrm{P} ((\mathrm{A} \cup \mathrm{B}) | \mathrm{F}) = \mathrm{P} (\mathrm{A} | \mathrm{F}) + \mathrm{P} (\mathrm{B} | \mathrm{F}) - \mathrm{P} ((\mathrm{A} \cap \mathrm{B}) | \mathrm{F})
$$

[S2]

In particular, if $A$ and $B$ are disjoint events, then

$$
\mathrm{P} ((\mathrm{A} \cup \mathrm{B}) | \mathrm{F}) = \mathrm{P} (\mathrm{A} | \mathrm{F}) + \mathrm{P} (\mathrm{B} | \mathrm{F})
$$

[S2]

**Property 3** $\mathrm{P(E'|F)} = 1 - \mathrm{P(E|F)}$ [S2]

From Property 1, we know that $\mathrm{P(S|F)} = 1$. [S2] Since $S = E \cup E'$, we have:

$$
\mathrm{P} (\mathrm{E} \cup \mathrm{E} ^ {\prime} | \mathrm{F}) = 1
$$

[S2]

$$
\mathrm{P} (\mathrm{E} | \mathrm{F}) + \mathrm{P} (\mathrm{E} ^ {\prime} | \mathrm{F}) = 1
$$

[S2]

since $E$ and $E'$ are disjoint events. [S2] This gives:

$$
\mathrm{P} (\mathrm{E} ^ {\prime} | \mathrm{F}) = 1 - \mathrm{P} (\mathrm{E} | \mathrm{F})
$$

[S2]

## Bayes' Theorem

Consider that there are two bags I and II. [S3] Bag I contains 2 white and 3 red balls and Bag II contains 4 white and 5 red balls. [S3] One ball is drawn at random from one of the bags. [S3] We can find the probability of selecting any of the bags (i.e. $\frac{1}{2}$) or probability of drawing a ball of a particular colour (say white) from a particular bag (say Bag I). [S3] In other words, we can find the probability that the ball drawn is of a particular colour, if we are given the bag from which the ball is drawn. [S3] But, can we find the probability that the ball drawn is from a particular bag (say Bag II), if the colour of the ball drawn is given? [S3] Here, we have to find the reverse probability of Bag II to be selected when an event occurred after it is known. [S3] Famous mathematician, John Bayes' solved the problem of finding reverse probability by using conditional probability. [S3] The formula developed by him is known as 'Bayes theorem' which was published posthumously in 1763. [S3]

## Worked example

A family has two children. What is the probability that both the children are boys given that at least one of them is a boy? [S2]

**Solution:**
Let $b$ stand for boy and $g$ for girl. [S2] The sample space of the experiment is

$$
S = \{(b, b), (g, b), (b, g), (g, g) \}
$$

[S2]

Let $E$ and $F$ denote the following events:
$E$ : ‘both the children are boys’
$F$ : ‘at least one of the child is a boy’ [S2]

$$
\mathrm{E} = \{(b, b) \} \text{and} \mathrm{F} = \{(b, b), (g, b), (b, g) \}
$$

[S2]

$$
\mathrm{E} \cap \mathrm{F} = \{(b, b) \}
$$

[S2]

$$
\mathrm{P} (\mathrm{F}) = \frac {3}{4} \text{and} \mathrm{P} (\mathrm{E} \cap \mathrm{F}) = \frac {1}{4}
$$

[S2]

$$
\mathrm{P} (\mathrm{E} | \mathrm{F}) = \frac {\mathrm{P} (\mathrm{E} \cap \mathrm{F})}{\mathrm{P} (\mathrm{F})} = \frac {\frac {1}{4}}{\frac {3}{4}} = \frac {1}{3}
$$

[S2]

## Key points

- Conditional probability is the probability of an event given that another event has occurred. [S1]
- For any events $E$ and $F$ of a sample space $S$, the conditional probability of the sample space $S$ given $F$ is 1, and the conditional probability of $F$ given $F$ is also 1. [S2]
- If $A$ and $B$ are disjoint events of a sample space $S$ and $F$ is an event of $S$ such that $P(F) \neq 0$, then $P((A \cup B)|F) = P(A|F) + P(B|F)$. [S2]
- The conditional probability of the complement of an event $E$ given $F$ is given by $P(E'|F) = 1 - P(E|F)$. [S2]
- Bayes' theorem, published posthumously in 1763, uses conditional probability to solve the problem of finding reverse probabilities. [S3]

<!-- TERMS: Bernoulli trial, binomial distribution, binomial coefficient, mean, variance, standard deviation, random variable, discrete probability distribution, success, failure, probability of success, probability of failure -->
