# Equivalence Relations and Partitions

An equivalence relation is a powerful mathematical tool that allows us to group elements of a set into distinct categories. When a set is divided by an equivalence relation, the resulting subsets are called equivalence classes. These classes naturally partition the original set, meaning they are disjoint and cover every element. Understanding this connection between relations and partitions is essential for advanced topics in mathematics, such as modular arithmetic and abstract algebra.

## The Three Properties of a Relation

Before we can define an equivalence relation, we must understand three fundamental properties: reflexive, symmetric, and transitive. A relation in a set $A$ is simply a subset of $A \times A$ [S1]. If $(a, b) \in \mathbb{R}$, we say that $a$ is related to $b$ and we denote it as $aRb$. 

A relation $R$ in a set $A$ is called reflexive if $(a, a) \in R$, for every $a \in A$ [S1]. This means every element is related to itself. 

A relation $R$ in a set $A$ is called symmetric if $(a_1, a_2) \in R$ implies that $(a_2, a_1) \in R$, for all $a_1, a_2 \in A$ [S1]. This means if $a$ is related to $b$, then $b$ must also be related to $a$. 

A relation $R$ in a set $A$ is called transitive if $(a_1, a_2) \in R$ and $(a_2, a_3) \in R$ implies that $(a_1, a_3) \in R$, for all $a_1, a_2, a_3 \in A$ [S1]. This means if $a$ is related to $b$, and $b$ is related to $c$, then $a$ must be related to $c$.

## Defining an Equivalence Relation

A relation $R$ in a set $A$ is said to be an equivalence relation if $R$ is reflexive, symmetric, and transitive [S1]. 

For illustration, consider the set of all triangles in a plane, $T$. Let $R$ be a relation in $T$ given by $R = \{(T_1, T_2) : T_1 \text{ is congruent to } T_2\}$ [S1]. 

$R$ is reflexive, since every triangle is congruent to itself. 
$R$ is symmetric, because if $T_1$ is congruent to $T_2$, then $T_2$ is congruent to $T_1$. 
$R$ is transitive, because if $T_1$ is congruent to $T_2$ and $T_2$ is congruent to $T_3$, then $T_1$ is congruent to $T_3$. 

Therefore, $R$ is an equivalence relation [S1]. 

Another example is the relation $R$ in the set $Z$ of integers given by $R = \{(a, b): 2 \text{ divides } a - b\}$ [S1]. 
$R$ is reflexive, as 2 divides $(a - a)$ for all $a \in Z$. 
$R$ is symmetric, because if 2 divides $a - b$, then 2 divides $b - a$. 
$R$ is transitive, because if 2 divides $a - b$ and 2 divides $b - c$, then $a - c = (a - b) + (b - c)$ is even, so 2 divides $a - c$. 

Thus, $R$ is an equivalence relation in $Z$ [S1].

## Equivalence Classes and Partitions

In Example 5, note that all even integers are related to zero, as $(0, \pm 2)$, $(0, \pm 4)$ etc., lie in $R$ and no odd integer is related to 0, as $(0, \pm 1)$, $(0, \pm 3)$ etc., do not lie in $R$ [S1]. 

Therefore, the set $E$ of all even integers and the set $O$ of all odd integers are subsets of $Z$ satisfying the following conditions: 
(i) All elements of $E$ are related to each other and all elements of $O$ are related to each other.
(ii) No element of $E$ is related to any element of $O$ and vice-versa.
(iii) $E$ and $O$ are disjoint and $Z = E \cup O$ [S1].

The subset $E$ is called the equivalence class containing zero and is denoted by $[0]$. Similarly, $O$ is the equivalence class containing 1 and is denoted by $[1]$ [S1]. 

Given an arbitrary equivalence relation $R$ in an arbitrary set $X$, $R$ divides $X$ into mutually disjoint subsets $A_i$ called partitions or subdivisions of $X$ satisfying: 
(i) all elements of $A_i$ are related to each other, for all $i$,
(ii) no element of $A_i$ is related to any element of $A_i$, $i \neq j$,
(iii) $\cup A_j = X$ and $A_i \cap A_j = \phi, i \neq j$ [S1].

The subsets $A_i$ are called equivalence classes [S1].

## The Reverse Process

The interesting part of the situation is that we can go reverse also. For example, consider a subdivision of the set $Z$ given by three mutually disjoint subsets $A_1, A_2$ and $A_3$ whose union is $Z$ with 
$A_1 = \{x \in Z: x \text{ is a multiple of } 3\} = \{\dots , -6, -3, 0, 3, 6, \dots\}$ [S1],
$A_2 = \{x \in Z: x - 1 \text{ is a multiple of } 3\} = \{\dots , -5, -2, 1, 4, 7, \dots\}$ [S1],
$A_3 = \{x \in Z: x - 2 \text{ is a multiple of } 3\} = \{\dots , -4, -1, 2, 5, 8, \dots\}$ [S1].

Define a relation $R$ in $Z$ given by $R = \{(a, b) : 3 \text{ divides } a - b\}$ [S1]. Following the arguments similar to those used in Example 5, we can show that $R$ is an equivalence relation. 

Also, $A_1$ coincides with the set of all integers in $Z$ which are related to zero, $A_2$ coincides with the set of all integers which are related to 1 and $A_3$ coincides with the set of all integers in $Z$ which are related to 2. Thus, $A_1 = [0]$, $A_2 = [1]$ and $A_3 = [2]$. In fact, $A_1 = [3r]$, $A_2 = [3r + 1]$ and $A_3 = [3r + 2]$, for all $r \in Z$ [S1].

## Worked Example

Let us apply this concept to the set of all students in a school. Consider the relation $R$ in the set $A$ of all students of a boys school given by $R = \{(a, b) : a \text{ is sister of } b\}$ [S1]. 

Since the school is a boys school, no student of the school can be sister of any student of the school. Hence, $R = \phi$, showing that $R$ is the empty relation [S1]. 

It is also obvious that the difference between heights of any two students of the school has to be less than 3 meters. This shows that $R' = A \times A$ is the universal relation [S1]. 

The empty relation and the universal relation are sometimes called trivial relations [S1].

## Key points

*   An equivalence relation is a relation that is reflexive, symmetric, and transitive.
*   An equivalence relation partitions a set into mutually disjoint subsets called equivalence classes.
*   The equivalence classes cover the entire set, meaning their union is the original set.
*   The equivalence classes are disjoint, meaning their intersection is the empty set.
*   The reverse process is also true: a partition of a set defines an equivalence relation.
<!-- TERMS: equivalence relation, partition, equivalence class, reflexive, symmetric, transitive, empty relation, universal relation -->