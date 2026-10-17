
# Addition Theorem of Probability

Probability theory attempts to quantify the chances of occurrence or non-occurrence of events in our daily lives [S1]. When we want to find the likelihood of two events happening together, we use the Addition Theorem of Probability. This rule helps us calculate the probability of the union of two events, denoted as $P(A \cup B)$. It is essential because simply adding the probabilities of two events can sometimes give us a number greater than 1, which is impossible in probability. The theorem provides a precise way to handle this, whether the events overlap or not.

## Mutually Exclusive Events

When two events cannot happen at the same time, they are called mutually exclusive events. This means the intersection of the two events is an empty set, or $A \cap B = \phi$. In this specific case, the Addition Theorem becomes very simple. We just add the probability of the first event to the probability of the second event. This rule is actually one of the fundamental axioms of probability. 

To understand this, consider the axioms of probability. The probability of the entire sample space $S$ is always equal to 1 [S1]. The third axiom states that if $E$ and $F$ are mutually exclusive events, then $P(E \cup F) = P(E) + P(F)$. We can also prove that the probability of an impossible event, represented by the empty set $\phi$, is exactly 0. We do this by letting $F = \phi$ and noting that $E$ and $\phi$ are disjoint. Therefore, from axiom (iii), we get $P(E \cup \phi) = P(E) + P(\phi)$, which simplifies to $P(E) = P(E) + P(\phi)$, meaning $P(\phi) = 0$ [S1].

Let us look at an everyday situation. Imagine you are drawing a single card from a standard deck of 52 playing cards. Let event $A$ be drawing a diamond, and let event $B$ be drawing a spade. A card cannot be both a diamond and a spade at the same time, so these events are mutually exclusive. The probability of drawing a diamond is $\frac{1}{4}$, and the probability of drawing a spade is also $\frac{1}{4}$ [S1]. Using the Addition Theorem for mutually exclusive events, the probability of drawing either a diamond or a spade is $\frac{1}{4} + \frac{1}{4} = \frac{1}{2}$.

## Non-Mutually Exclusive Events

Sometimes, two events can happen at the same time. These are called non-mutually exclusive events, or overlapping events. If we simply add their probabilities, we end up counting the overlapping outcomes twice. To fix this, we must subtract the probability of the intersection. The formula for the Addition Theorem in this case is $P(A \cup B) = P(A) + P(B) - P(A \cap B)$.

This rule is derived by looking at how sets overlap. The union of $A$ and $B$ can be broken down into three parts: the outcomes that are only in $A$, the outcomes that are only in $B$, and the outcomes that are in both $A$ and $B$. When we calculate $P(A) + P(B)$, the outcomes in the intersection $A \cap B$ are counted twice. Therefore, we subtract $P(A \cap B)$ to get the correct total [S1].

Consider the experiment of tossing a coin three times. Let event $A$ be getting exactly two heads, so $A = \{HHT, HTH, THH\}$. Let event $B$ be getting at least two heads, so $B = \{HTH, THH, HHH\}$. Notice that $A$ and $B$ share the outcomes $HTH$ and $THH$. If we add their probabilities, we count $HTH$ and $THH$ twice. We must subtract the probability of $A \cap B$ to find the correct probability of $A \cup B$ [S1].

## Worked Example

Let us apply the Addition Theorem to a practical problem. Imagine a factory that produces pens. They examine three consecutive pens and classify them as Good (G) or Bad (B). The sample space for this experiment is $S = \{BBB, BBG, BGB, GBB, BGG, GBG, GGB, GGG\}$ [S1]. Let event $A$ be the event that exactly one pen is bad. This means $A = \{BBG, BGB, GBB\}$. Let event $B$ be the event that at least two pens are bad. This means $B = \{BBB, BBG, BGB, GBB\}$.

First, we need to find the probabilities of the sample points. The text assigns a probability of $\frac{1}{8}$ to each outcome [S1]. 
The probability of event $A$ is the sum of the probabilities of its outcomes: $P(A) = P(BBG) + P(BGB) + P(GBB) = \frac{1}{8} + \frac{1}{8} + \frac{1}{8} = \frac{3}{8}$ [S1].
The probability of event $B$ is $P(B) = P(BBB) + P(BBG) + P(BGB) + P(GBB) = \frac{1}{8} + \frac{1}{8} + \frac{1}{8} + \frac{1}{8} = \frac{4}{8} = \frac{1}{2}$ [S1].

Now, we want to find the probability of event $A$ or event $B$. We use the Addition Theorem for non-mutually exclusive events. We must first find the intersection, $A \cap B$. The outcomes common to both $A$ and $B$ are $\{BBG, BGB, GBB\}$. So, $P(A \cap B) = \frac{1}{8} + \frac{1}{8} + \frac{1}{8} = \frac{3}{8}$ [S1].

Applying the formula $P(A \cup B) = P(A) + P(B) - P(A \cap B)$, we get:
$P(A \cup B) = \frac{3}{8} + \frac{4}{8} - \frac{3}{8} = \frac{4}{8} = \frac{1}{2}$ [S1].
This means there is a 50% chance that exactly one pen is bad, or at least two pens are bad.

## Key points

*   For mutually exclusive events, the Addition Theorem states that $P(A \cup B) = P(A) + P(B)$, because the intersection is the empty set $\phi$ [S1].
*   For non-mutually exclusive events, the correct formula is $P(A \cup B) = P(A) + P(B) - P(A \cap B)$ to avoid double-counting the overlapping outcomes [S1].
*   The probability of an impossible event, represented by the empty set $\phi$, is always 0, which is derived directly from the axioms of probability [S1].
*   The probability of any event $E$ can be found by summing the probabilities of the individual elementary outcomes that make up $E$ [S1].
*   The probability of the complement of an event, $P(A')$, is equal to $1 - P(A)$, because $A$ and $A'$ are mutually exclusive and exhaustive [S1].