# Bayes' Theorem

In probability, we study the conditional probability of an event given that another event has occurred, which is helpful in understanding Bayes' theorem [S3]. Famous mathematician John Bayes' solved the problem of finding reverse probability by using conditional probability [S1]. The formula developed by him is known as 'Bayes theorem', which was published posthumously in 1763 [S1]. This theorem is helpful when we need to find the reverse probability of an event after another event has occurred [S1].

## The Problem of Reverse Probability

To understand the problem of reverse probability, consider two bags, Bag I and Bag II. Bag I contains 2 white and 3 red balls, and Bag II contains 4 white and 5 red balls [S1]. One ball is drawn at random from one of the bags [S1].

We can easily find the probability of selecting any of the bags (which is $\frac{1}{2}$) or the probability of drawing a ball of a particular colour (say white) from a particular bag (say Bag I) [S1]. In other words, we can find the probability that the ball drawn is of a particular colour, if we are given the bag from which the ball is drawn [S1].

But, can we find the probability that the ball drawn is from a particular bag (say Bag II), if the colour of the ball drawn is given? [S1] Here, we have to find the reverse probability of Bag II to be selected when an event occurred after it is known [S1]. John Bayes' solved the problem of finding reverse probability by using conditional probability [S1].

## The Formula and Its Components

The formula developed by John Bayes' is known as 'Bayes theorem' [S1]. Before stating and proving the Bayes' theorem, we must first understand the preliminary results and properties of conditional probability [S1].

Let $E$ and $F$ be events of a sample space $S$ of an experiment, then we have the following properties [S2]:

**Property 1**
$$ \mathrm{P(S|F)} = \mathrm{P(F|F)} = 1 $$
This is because:
$$ \mathrm{P(S|F)} = \frac{\mathrm{P(S \cap F)}}{\mathrm{P(F)}} = \frac{\mathrm{P(F)}}{\mathrm{P(F)}} = 1 $$
$$ \mathrm{P(F|F)} = \frac{\mathrm{P(F \cap F)}}{\mathrm{P(F)}} = \frac{\mathrm{P(F)}}{\mathrm{P(F)}} = 1 $$

**Property 2**
If $A$ and $B$ are any two events of a sample space $S$ and $F$ is an event of $S$ such that $P(F) \neq 0$, then [S2]:
$$ \mathrm{P((A \cup B)|F)} = \mathrm{P(A|F)} + \mathrm{P(B|F)} - \mathrm{P((A \cap B)|F)} $$
In particular, if $A$ and $B$ are disjoint events, then [S2]:
$$ \mathrm{P((A \cup B)|F)} = \mathrm{P(A|F)} + \mathrm{P(B|F)} $$

**Property 3**
$$ \mathrm{P(E'|F)} = 1 - \mathrm{P(E|F)} $$
This is because $S = E \cup E'$, and since $E$ and $E'$ are disjoint events, we have [S2]:
$$ \mathrm{P(E \cup E'|F)} = 1 $$
$$ \mathrm{P(E|F)} + \mathrm{P(E'|F)} = 1 $$
$$ \mathrm{P(E'|F)} = 1 - \mathrm{P(E|F)} $$

## Applying Bayes' Theorem

To understand how we apply conditional probability, which is helpful in understanding Bayes' theorem [S3], let us consider an example in a school [S2].

In a school, there are 1000 students, out of which 430 are girls [S2]. It is known that out of 430, 10% of the girls study in class XII [S2]. What is the probability that a student chosen randomly studies in Class XII given that the chosen student is a girl? [S2]

Let $E$ denote the event that a student chosen randomly studies in Class XII and $F$ be the event that the randomly chosen student is a girl [S2]. We have to find $P(E|F)$ [S2].

The probability of choosing a girl is [S2]:
$$ \mathrm{P(F)} = \frac{430}{1000} = 0.43 $$
The probability of choosing a student who is both a girl and in Class XII is [S2]:
$$ \mathrm{P(E \cap F)} = \frac{43}{1000} = 0.043 $$
Using the definition of conditional probability, we find [S2]:
$$ \mathrm{P(E|F)} = \frac{\mathrm{P(E \cap F)}}{\mathrm{P(F)}} = \frac{0.043}{0.43} = 0.1 $$

## Worked Example: Two Bags and Balls

Consider that there are two bags I and II. Bag I contains 2 white and 3 red balls and Bag II contains 4 white and 5 red balls [S1]. One ball is drawn at random from one of the bags [S1].

We can find the probability of selecting any of the bags, which is [S1]:
$$ \mathrm{P(Bag\ I)} = \frac{1}{2}, \quad \mathrm{P(Bag\ II)} = \frac{1}{2} $$

We can also find the probability of drawing a ball of a particular colour (say white) from a particular bag (say Bag I) [S1]. Since Bag I contains 2 white and 3 red balls, the probability of drawing a white ball given that Bag I is selected is [S1]:
$$ \mathrm{P(White|Bag\ I)} = \frac{2}{5} $$

But, can we find the probability that the ball drawn is from a particular bag (say Bag II), if the colour of the ball drawn is given? [S1] Here, we have to find the reverse probability of Bag II to be selected when an event occurred after it is known [S1]. John Bayes' solved the problem of finding reverse probability by using conditional probability [S1].

## Key points

*   John Bayes' solved the problem of finding reverse probability by using conditional probability, and the formula developed by him is known as Bayes' theorem [S1].
*   Reverse probability involves finding the probability of an initial condition (such as a specific bag) after an event (such as drawing a ball of a certain colour) has occurred [S1].
*   Before stating Bayes' theorem, we use preliminary results of conditional probability, such as the properties of sample spaces and disjoint events [S1, S2].
*   Conditional probability can be applied to find the probability of an event given that another event has occurred, which is helpful in understanding Bayes' theorem [S2, S3].

<!-- TERMS: Bayes' Theorem, prior probability, likelihood, total probability, conditional probability, reverse probability -->
