<!-- page 1 of 17 -->

The image provided is a QR code. As per the instructions, I am to process text and non-text content in standard OCR text. However, there is no textual content to extract or convert according to the given instructions. Therefore, no OCR text can be generated from this image.

Chapter

12079CH01

1

# RELATIONS AND FUNCTIONS

There is no permanent place in the world for ugly mathematics ... . It may be very hard to define mathematical beauty but that is just as true of beauty of any kind, we may not know quite what we mean by a beautiful poem, but that does not prevent us from recognising one when we read it. — G. H. HARDY

## 1.1 Introduction

Recall that the notion of relations and functions, domain, co-domain and range have been introduced in Class XI along with different types of specific real valued functions and their graphs. The concept of the term ‘relation’ in mathematics has been drawn from the meaning of relation in English language, according to which two objects or quantities are related if there is a recognisable connection or link between the two objects or quantities. Let A be the set of students of Class XII of a school and B be the set of students of Class XI of the same school. Then some of the examples of relations from A to B are

![Image block](doc:348d763/tier:standard/page:1/block:9)

(i) $\{(a,b)\in \mathrm{A}\times \mathrm{B}:a$ is brother of $b\}$

(ii) $\{(a,b)\in \mathrm{A}\times \mathrm{B}:a$ is sister of $b\}$,

Lejeune Dirichlet (1805-1859)

(iii) $\{(a,b)\in \mathrm{A}\times \mathrm{B};$ age of $a$ is greater than age of $b\}$,

(iv) $\{(a, b) \in \mathrm{A} \times \mathrm{B}$: total marks obtained by $a$ in the final examination is less than the total marks obtained by $b$ in the final examination},

(v) $\{(a, b) \in \mathrm{A} \times \mathrm{B}: a$ lives in the same locality as $b\}$. However, abstracting from this, we define mathematically a relation R from A to B as an arbitrary subset of $\mathrm{A} \times \mathrm{B}$.

If  $(a, b) \in \mathrm{R}$ , we say that a is related to b under the relation R and we write as a R b. In general,  $(a, b) \in \mathrm{R}$ , we do not bother whether there is a recognisable connection or link between a and b. As seen in Class XI, functions are special kind of relations.

In this chapter, we will study different types of relations and functions, composition of functions, invertible functions and binary operations.

Reprint 2025-26

<!-- page 2 of 17 -->

2

MATHEMATICS

## 1.2 Types of Relations

In this section, we would like to study different types of relations. We know that a relation in a set A is a subset of $\mathrm{A} \times \mathrm{A}$. Thus, the empty set $\phi$ and $\mathrm{A} \times \mathrm{A}$ are two extreme relations. For illustration, consider a relation R in the set $\mathrm{A} = \{1, 2, 3, 4\}$ given by $\mathrm{R} = \{(a, b): a - b = 10\}$. This is the empty set, as no pair $(a, b)$ satisfies the condition $a - b = 10$. Similarly, $\mathrm{R}' = \{(a, b): |a - b| \geq 0\}$ is the whole set $\mathrm{A} \times \mathrm{A}$, as all pairs $(a, b)$ in $\mathrm{A} \times \mathrm{A}$ satisfy $|a - b| \geq 0$. These two extreme examples lead us to the following definitions.

Definition 1 A relation R in a set A is called empty relation, if no element of A is related to any element of A, i.e., $\mathrm{R} = \phi \subset \mathrm{A} \times \mathrm{A}$.

Definition 2 A relation R in a set A is called universal relation, if each element of A is related to every element of A, i.e., $\mathrm{R} = \mathrm{A} \times \mathrm{A}$.

Both the empty relation and the universal relation are some times called trivial relations.

Example 1 Let A be the set of all students of a boys school. Show that the relation R in A given by $\mathrm{R} = \{(a, b) : a \text{ is sister of } b\}$ is the empty relation and $\mathrm{R}' = \{(a, b) : \text{the difference between heights of } a \text{ and } b \text{ is less than 3 meters}\}$ is the universal relation.

Solution Since the school is boys school, no student of the school can be sister of any student of the school. Hence, $R = \phi$, showing that $R$ is the empty relation. It is also obvious that the difference between heights of any two students of the school has to be less than 3 meters. This shows that $R' = A \times A$ is the universal relation.

Remark In Class XI, we have seen two ways of representing a relation, namely raster method and set builder method. However, a relation R in the set  $\{1, 2, 3, 4\}$  defined by  $R = \{(a, b) : b = a + 1\}$  is also expressed as a R b if and only if  $b = a + 1$  by many authors. We may also use this notation, as and when convenient.

If $(a,b)\in \mathbb{R}$, we say that $a$ is related to $b$ and we denote it as $a\mathrm{R}b$.

One of the most important relation, which plays a significant role in Mathematics, is an equivalence relation. To study equivalence relation, we first consider three types of relations, namely reflexive, symmetric and transitive.

Definition 3 A relation R in a set A is called

(i) reflexive, if $(a,a)\in \mathrm{R}$, for every $a\in \mathrm{A}$,

(ii) symmetric, if $(a_1, a_2) \in \mathbb{R}$ implies that $(a_2, a_1) \in \mathbb{R}$, for all $a_1, a_2 \in \mathbb{A}$.

(iii) transitive, if  $(a_{1}, a_{2}) \in \mathrm{R}$  and  $(a_{2}, a_{3}) \in \mathrm{R}$  implies that  $(a_{1}, a_{3}) \in \mathrm{R}$ , for all  $a_{1}, a_{2}, a_{3} \in A$ .

Reprint 2025-26

<!-- page 3 of 17 -->

RELATIONS AND FUNCTIONS

3

Definition 4 A relation R in a set A is said to be an equivalence relation if R is reflexive, symmetric and transitive.

Example 2 Let $\mathrm{T}$ be the set of all triangles in a plane with $\mathrm{R}$ a relation in $\mathrm{T}$ given by $\mathrm{R} = \{(T_1, T_2) : T_1 \text{ is congruent to } T_2\}$. Show that $\mathrm{R}$ is an equivalence relation.

Solution R is reflexive, since every triangle is congruent to itself. Further,  $(T_{1}, T_{2}) \in \mathrm{R} \Rightarrow T_{1}$  is congruent to  $T_{2} \Rightarrow T_{2}$  is congruent to  $T_{1} \Rightarrow (T_{2}, T_{1}) \in \mathrm{R}$ . Hence, R is symmetric. Moreover,  $(T_{1}, T_{2}), (T_{2}, T_{3}) \in \mathrm{R} \Rightarrow T_{1}$  is congruent to  $T_{2}$  and  $T_{2}$  is congruent to  $T_{3} \Rightarrow T_{1}$  is congruent to  $T_{3} \Rightarrow (T_{1}, T_{3}) \in \mathrm{R}$ . Therefore, R is an equivalence relation.

Example 3 Let L be the set of all lines in a plane and R be the relation in L defined as  $R = \{(L_{1}, L_{2}) : L_{1} \text{ is perpendicular to } L_{2}\}$ . Show that R is symmetric but neither reflexive nor transitive.

Solution R is not reflexive, as a line  $L_{1}$  can not be perpendicular to itself, i.e.,  $(\mathrm{L}_{1}, \mathrm{L}_{1}) \notin \mathrm{R}$ . R is symmetric as  $(\mathrm{L}_{1}, \mathrm{L}_{2}) \in \mathrm{R}$

$$
\begin{array}{l l} \Rightarrow & \mathrm{L} _ {1} \text {is perpendicular to L} _ {2} \\ \Rightarrow & \mathrm{L} _ {2} \text {is perpendicular to L} _ {1} \\ \Rightarrow & (\mathrm{L} _ {2}, \mathrm{L} _ {1}) \in \mathrm{R}. \end{array}
$$

![Image block](doc:348d763/tier:standard/page:3/block:9)

R is not transitive. Indeed, if $\mathrm{L}_1$ is perpendicular to $\mathrm{L}_2$ and

Fig 1.1

$$
\mathrm{L} _ {2}
$$

$$
\mathrm{L} _ {3}
$$

$$
\mathrm{L} _ {1}
$$

$L_{3}$ . In fact,  $L_{1}$  is parallel to  $L_{3}$ , i.e.,  $(L_{1}, L_{2}) \in R$ ,  $(L_{2}, L_{3}) \in R$  but  $(L_{1}, L_{3}) \notin R$ .

Example 4 Show that the relation R in the set $\{1,2,3\}$ given by $R = \{(1,1),(2,2),(3,3),(1,2),(2,3)\}$ is reflexive but neither symmetric nor transitive.

Solution R is reflexive, since (1, 1), (2, 2) and (3, 3) lie in R. Also, R is not symmetric, as $(1, 2) \in \mathrm{R}$ but $(2, 1) \notin \mathrm{R}$. Similarly, R is not transitive, as $(1, 2) \in \mathrm{R}$ and $(2, 3) \in \mathrm{R}$ but $(1, 3) \notin \mathrm{R}$.

Example 5 Show that the relation $\mathbf{R}$ in the set $\mathbf{Z}$ of integers given by

$$
\mathrm{R} = \{(a, b): 2 \text {divides} a - b \}
$$

is an equivalence relation.

Solution R is reflexive, as 2 divides  $(a - a)$  for all  $a \in Z$ . Further, if  $(a, b) \in R$ , then 2 divides a - b. Therefore, 2 divides b - a. Hence,  $(b, a) \in R$ , which shows that R is symmetric. Similarly, if  $(a, b) \in R$  and  $(b, c) \in R$ , then a - b and b - c are divisible by 2. Now,  $a - c = (a - b) + (b - c)$  is even (Why?). So,  $(a - c)$  is divisible by 2. This shows that R is transitive. Thus, R is an equivalence relation in Z.

Reprint 2025-26

<!-- page 4 of 17 -->

4

MATHEMATICS

In Example 5, note that all even integers are related to zero, as  $(0, \pm 2)$ ,  $(0, \pm 4)$  etc., lie in R and no odd integer is related to 0, as  $(0, \pm 1)$ ,  $(0, \pm 3)$  etc., do not lie in R. Similarly, all odd integers are related to one and no even integer is related to one. Therefore, the set E of all even integers and the set O of all odd integers are subsets of Z satisfying following conditions:

(i) All elements of E are related to each other and all elements of O are related to each other.

(ii) No element of $\mathrm{E}$ is related to any element of $\mathrm{O}$ and vice-versa.

(iii) E and O are disjoint and $\mathbf{Z} = \mathrm{E} \cup \mathrm{O}$.

The subset E is called the equivalence class containing zero and is denoted by [0]. Similarly, O is the equivalence class containing 1 and is denoted by [1]. Note that $[0] \neq [1]$, $[0] = [2r]$ and $[1] = [2r + 1]$, $r \in \mathbf{Z}$. Infact, what we have seen above is true for an arbitrary equivalence relation R in a set X. Given an arbitrary equivalence relation R in an arbitrary set X, R divides X into mutually disjoint subsets $\mathrm{A}_i$ called partitions or subdivisions of X satisfying:

(i) all elements of $\mathrm{A}_i$ are related to each other, for all $i$,

(ii) no element of $\mathrm{A}_i$ is related to any element of $\mathrm{A}_i$, $i \neq j$.

(iii) $\cup \mathrm{A}_j = \mathrm{X}$ and $\mathrm{A}_i\cap \mathrm{A}_j = \phi ,i\neq j.$

The subsets  $A_{i}$  are called equivalence classes. The interesting part of the situation is that we can go reverse also. For example, consider a subdivision of the set Z given by three mutually disjoint subsets  $A_{1}, A_{2}$  and  $A_{3}$  whose union is Z with

$$
\mathrm{A} _ {1} = \{x \in \mathbf {Z}: x \text {is a multiple of} 3 \} = \{\dots , - 6, - 3, 0, 3, 6, \dots \}
$$

$$
\mathrm{A} _ {2} = \{x \in \mathbf {Z}: x - 1 \text {is a multiple of} 3 \} = \{\dots , - 5, - 2, 1, 4, 7, \dots \}
$$

$$
\mathrm{A} _ {3} = \{x \in \mathbf {Z}: x - 2 \text {is a multiple of} 3 \} = \{\dots , - 4, - 1, 2, 5, 8, \dots \}
$$

Define a relation R in Z given by  $R = \{(a, b) : 3 \text{ divides } a - b\}$ . Following the arguments similar to those used in Example 5, we can show that R is an equivalence relation. Also,  $A_{1}$  coincides with the set of all integers in Z which are related to zero,  $A_{2}$  coincides with the set of all integers which are related to 1 and  $A_{3}$  coincides with the set of all integers in Z which are related to 2. Thus,  $A_{1} = [0]$ ,  $A_{2} = [1]$  and  $A_{3} = [2]$ . In fact,  $A_{1} = [3r]$ ,  $A_{2} = [3r + 1]$  and  $A_{3} = [3r + 2]$ , for all  $r \in Z$ .

Example 6 Let R be the relation defined in the set $\mathrm{A} = \{1, 2, 3, 4, 5, 6, 7\}$ by $\mathrm{R} = \{(a, b) : \text{both } a \text{ and } b \text{ are either odd or even}\}$. Show that R is an equivalence relation. Further, show that all the elements of the subset $\{1, 3, 5, 7\}$ are related to each other and all the elements of the subset $\{2, 4, 6\}$ are related to each other, but no element of the subset $\{1, 3, 5, 7\}$ is related to any element of the subset $\{2, 4, 6\}$.

Reprint 2025-26

<!-- page 5 of 17 -->

RELATIONS AND FUNCTIONS

5

Solution Given any element $a$ in A, both $a$ and $a$ must be either odd or even, so that $(a, a) \in \mathrm{R}$. Further, $(a, b) \in \mathrm{R} \Rightarrow$ both $a$ and $b$ must be either odd or even $\Rightarrow (b, a) \in \mathrm{R}$. Similarly, $(a, b) \in \mathrm{R}$ and $(b, c) \in \mathrm{R} \Rightarrow$ all elements $a, b, c$, must be either even or odd simultaneously $\Rightarrow (a, c) \in \mathrm{R}$. Hence, R is an equivalence relation. Further, all the elements of $\{1, 3, 5, 7\}$ are related to each other, as all the elements of this subset are odd. Similarly, all the elements of the subset $\{2, 4, 6\}$ are related to each other, as all of them are even. Also, no element of the subset $\{1, 3, 5, 7\}$ can be related to any element of $\{2, 4, 6\}$, as elements of $\{1, 3, 5, 7\}$ are odd, while elements of $\{2, 4, 6\}$ are even.

## EXERCISE 1.1

1. Determine whether each of the following relations are reflexive, symmetric and transitive:

(i) Relation R in the set $\mathrm{A} = \{1, 2, 3, ..., 13, 14\}$ defined as

$$
R = \{(x, y): 3 x - y = 0 \}
$$

(ii) Relation R in the set $\mathbf{N}$ of natural numbers defined as

$$
\mathrm{R} = \{(x, y): y = x + 5 \text {and} x <   4 \}
$$

(iii) Relation R in the set $\mathrm{A} = \{1, 2, 3, 4, 5, 6\}$ as

$$
\mathrm{R} = \{(x, y): y \text {is divisible by} x \}
$$

(iv) Relation R in the set $\mathbf{Z}$ of all integers defined as

$$
\mathrm{R} = \{(x, y): x - y \text {is an integer}
$$

(v) Relation R in the set A of human beings in a town at a particular time given by

(a) $R = \{(x,y):x$ and $y$ work at the same place}

(b) $\mathrm{R} = \{(x,y):x\text{ and } y\text{ live in the same locality}\}$

(c) $R = \{(x, y) : x \text{ is exactly } 7 \, \text{cm taller than } y\}$

(d) $R = \{(x,y):x$ is wife of $y\}$

(e) $R = \{(x,y):x$ is father of $y\}$

2. Show that the relation $\mathbf{R}$ in the set $\mathbf{R}$ of real numbers, defined as

$R = \{(a, b) : a \leq b^2\}$ is neither reflexive nor symmetric nor transitive.

3. Check whether the relation R defined in the set $\{1, 2, 3, 4, 5, 6\}$ as

$\mathrm{R} = \{(a,b):b = a + 1\}$ is reflexive, symmetric or transitive.

4. Show that the relation R in R defined as  $\mathrm{R} = \{(a, b) : a \leq b\}$ , is reflexive and transitive but not symmetric.

5. Check whether the relation R in R defined by  $\mathrm{R} = \{(a, b) : a \leq b^{3}\}$  is reflexive, symmetric or transitive.

Reprint 2025-26

<!-- page 6 of 17 -->

6

MATHEMATICS

6. Show that the relation R in the set  $\{1, 2, 3\}$  given by  $\mathrm{R} = \{(1, 2), (2, 1)\}$  is symmetric but neither reflexive nor transitive.

7. Show that the relation R in the set A of all the books in a library of a college, given by  $R = \{(x, y) : x \text{ and } y \text{ have same number of pages}\}$  is an equivalence relation.

8. Show that the relation R in the set $\mathrm{A} = \{1,2,3,4,5\}$ given by

$R = \{(a, b) : |a - b| \text{ is even}\}$, is an equivalence relation. Show that all the elements of $\{1, 3, 5\}$ are related to each other and all the elements of $\{2, 4\}$ are related to each other. But no element of $\{1, 3, 5\}$ is related to any element of $\{2, 4\}$.

9. Show that each of the relation $\mathbf{R}$ in the set $\mathrm{A} = \{x \in \mathbf{Z} : 0 \leq x \leq 12\}$, given by

(i) $\mathrm{R} = \{(a,b):|a - b|\text{ is a multiple of } 4\}$

(ii) $\mathrm{R} = \{(a,b):a = b\}$

is an equivalence relation. Find the set of all elements related to 1 in each case.

10. Give an example of a relation. Which is

(i) Symmetric but neither reflexive nor transitive.

(ii) Transitive but neither reflexive nor symmetric.

(iii) Reflexive and symmetric but not transitive.

(iv) Reflexive and transitive but not symmetric.

(v) Symmetric and transitive but not reflexive.

11. Show that the relation R in the set A of points in a plane given by  $R = \{(P, Q) : \text{distance of the point P from the origin is same as the distance of the point Q from the origin}\}$ , is an equivalence relation. Further, show that the set of all points related to a point  $P \neq (0, 0)$  is the circle passing through P with origin as centre.

12. Show that the relation R defined in the set A of all triangles as  $\mathrm{R} = \{(T_{1}, T_{2}) : T_{1}$  is similar to  $T_{2}\}$ , is equivalence relation. Consider three right angle triangles  $T_{1}$  with sides 3, 4, 5,  $T_{2}$  with sides 5, 12, 13 and  $T_{3}$  with sides 6, 8, 10. Which triangles among  $T_{1}$ ,  $T_{2}$  and  $T_{3}$  are related?

13. Show that the relation R defined in the set A of all polygons as $\mathrm{R} = \{(P_1, P_2) : P_1 \text{ and } P_2 \text{ have same number of sides}\}$, is an equivalence relation. What is the set of all elements in A related to the right angle triangle T with sides 3, 4 and 5?

14. Let L be the set of all lines in XY plane and R be the relation in L defined as  $\mathrm{R} = \{(\mathrm{L}_{1}, \mathrm{L}_{2}) : \mathrm{L}_{1} \text{ is parallel to } \mathrm{L}_{2}\}$ . Show that R is an equivalence relation. Find the set of all lines related to the line  $y = 2x + 4$ .

Reprint 2025-26

<!-- page 7 of 17 -->

RELATIONS AND FUNCTIONS

7

15. Let R be the relation in the set  $\{1, 2, 3, 4\}$  given by  $R = \{(1, 2), (2, 2), (1, 1), (4, 4), (1, 3), (3, 3), (3, 2)\}$ . Choose the correct answer.

(A) R is reflexive and symmetric but not transitive.

(B) R is reflexive and transitive but not symmetric.

(C) R is symmetric and transitive but not reflexive.

(D) R is an equivalence relation.

16. Let R be the relation in the set N given by  $R = \{(a, b) : a = b - 2, b > 6\}$ . Choose the correct answer.
(A)  $(2, 4) \in \mathrm{R}$   (B)  $(3, 8) \in \mathrm{R}$  (C)  $(6, 8) \in \mathrm{R}$  (D)  $(8, 7) \in \mathrm{R}$

## 1.3 Types of Functions

The notion of a function along with some special functions like identity function, constant function, polynomial function, rational function, modulus function, signum function etc. along with their graphs have been given in Class XI.

Addition, subtraction, multiplication and division of two functions have also been studied. As the concept of function is of paramount importance in mathematics and among other disciplines as well, we would like to extend our study about function from where we finished earlier. In this section, we would like to study different types of functions.

Consider the functions $f_{1}, f_{2}, f_{3}$ and $f_{4}$ given by the following diagrams.

In Fig 1.2, we observe that the images of distinct elements of $\mathrm{X}_1$ under the function $f_1$ are distinct, but the image of two distinct elements 1 and 2 of $\mathrm{X}_1$ under $f_2$ is same, namely $b$. Further, there are some elements like $e$ and $f$ in $\mathrm{X}_2$ which are not images of any element of $\mathrm{X}_1$ under $f_1$, while all elements of $\mathrm{X}_3$ are images of some elements of $\mathrm{X}_1$ under $f_3$. The above observations lead to the following definitions:

Definition 5 A function $f: \mathrm{X} \to \mathrm{Y}$ is defined to be one-one (or injective), if the images of distinct elements of $\mathrm{X}$ under $f$ are distinct, i.e., for every $x_1, x_2 \in \mathrm{X}, f(x_1) = f(x_2)$ implies $x_1 = x_2$. Otherwise, $f$ is called many-one.

The function $f_{1}$ and $f_{4}$ in Fig 1.2 (i) and (iv) are one-one and the function $f_{2}$ and $f_{3}$ in Fig 1.2 (ii) and (iii) are many-one.

Definition 6 A function $f: X \to Y$ is said to be onto (or surjective), if every element of $Y$ is the image of some element of $X$ under $f$, i.e., for every $y \in Y$, there exists an element $x$ in $X$ such that $f(x) = y$.

The function $f_{3}$ and $f_{4}$ in Fig 1.2 (iii), (iv) are onto and the function $f_{1}$ in Fig 1.2 (i) is not onto as elements e, f in $X_{2}$ are not the image of any element in $X_{1}$ under $f_{1}$.

Reprint 2025-26

<!-- page 8 of 17 -->

8

MATHEMATICS

![Image block](doc:348d763/tier:standard/page:8/block:3)

(i)

![Image block](doc:348d763/tier:standard/page:8/block:5)

(ii)

![Image block](doc:348d763/tier:standard/page:8/block:7)

![Image block](doc:348d763/tier:standard/page:8/block:8)

Fig 1.2 (i) to (iv)

Remark $f\colon \mathrm{X}\to \mathrm{Y}$ is onto if and only if Range of $f = \mathrm{Y}$.

Definition 7 A function $f: X \to Y$ is said to be one-one and onto (or bijective), if $f$ is both one-one and onto.

The function $f_{4}$ in Fig 1,2 (iv) is one-one and onto.

Example 7 Let A be the set of all 50 students of Class X in a school. Let $f \colon \mathrm{A} \to \mathbf{N}$ be function defined by $f(x) =$ roll number of the student $x$. Show that $f$ is one-one but not onto.

Solution No two different students of the class can have same roll number. Therefore, $f$ must be one-one. We can assume without any loss of generality that roll numbers of students are from 1 to 50. This implies that 51 in $\mathbf{N}$ is not roll number of any student of the class, so that 51 can not be image of any element of $\mathrm{X}$ under $f$. Hence, $f$ is not onto.

Example 8 Show that the function $f \colon \mathbf{N} \to \mathbf{N}$, given by $f(x) = 2x$, is one-one but not onto.

Solution The function $f$ is one-one, for $f(x_{1}) = f(x_{2}) \Rightarrow 2x_{1} = 2x_{2} \Rightarrow x_{1} = x_{2}$. Further, $f$ is not onto, as for $1 \in \mathbf{N}$, there does not exist any $x$ in $\mathbf{N}$ such that $f(x) = 2x = 1$.

Reprint 2025-26

<!-- page 9 of 17 -->

RELATIONS AND FUNCTIONS

9

Example 9 Prove that the function $f: \mathbf{R} \to \mathbf{R}$, given by $f(x) = 2x$, is one-one and onto. Solution $f$ is one-one, as $f(x_1) = f(x_2) \Rightarrow 2x_1 = 2x_2 \Rightarrow x_1 = x_2$. Also, given any real number $y$ in R, there exists $\frac{y}{2}$ in R such that $f(\frac{y}{2}) = 2 \cdot (\frac{y}{2}) = y$. Hence, $f$ is onto.

![Image block](doc:348d763/tier:standard/page:9/block:4)

Fig 1.3

Example 10 Show that the function $f \colon \mathbf{N} \to \mathbf{N}$, given by $f(1) = f(2) = 1$ and $f(x) = x - 1$, for every $x > 2$, is onto but not one-one.

Solution $f$ is not one-one, as $f(1) = f(2) = 1$. But $f$ is onto, as given any $y \in \mathbf{N}$, $y \neq 1$, we can choose $x$ as $y + 1$ such that $f(y + 1) = y + 1 - 1 = y$. Also for $1 \in \mathbf{N}$, we have $f(1) = 1$.

Example 11 Show that the function $f: \mathbf{R} \to \mathbf{R}$, defined as $f(x) = x^2$, is neither one-one nor onto.

Solution Since $f(-1) = 1 = f(1)$, $f$ is not one-one. Also, the element -2 in the co-domain $\mathbf{R}$ is not image of any element $x$ in the domain $\mathbf{R}$ (Why?). Therefore $f$ is not onto.

Example 12 Show that $f\colon \mathbf{N}\to \mathbf{N}$, given by

$$
f (x) = \begin{array}{l} x + 1, \text {if} x \text {is odd}, \\ x - 1, \text {if} x \text {is even} \end{array}
$$

is both one-one and onto.

![Image block](doc:348d763/tier:standard/page:9/block:13)

The image of 1 and $-1$ under $f$ is 1.

Fig 1.4

Reprint 2025-26

<!-- page 10 of 17 -->

10

MATHEMATICS

Solution Suppose $f(x_{1}) = f(x_{2})$. Note that if $x_{1}$ is odd and $x_{2}$ is even, then we will have $x_{1} + 1 = x_{2} - 1$, i.e., $x_{2} - x_{1} = 2$ which is impossible. Similarly, the possibility of $x_{1}$ being even and $x_{2}$ being odd can also be ruled out, using the similar argument. Therefore, both $x_{1}$ and $x_{2}$ must be either odd or even. Suppose both $x_{1}$ and $x_{2}$ are odd. Then $f(x_{1}) = f(x_{2}) \Rightarrow x_{1} + 1 = x_{2} + 1 \Rightarrow x_{1} = x_{2}$. Similarly, if both $x_{1}$ and $x_{2}$ are even, then also $f(x_{1}) = f(x_{2}) \Rightarrow x_{1} - 1 = x_{2} - 1 \Rightarrow x_{1} = x_{2}$. Thus, $f$ is one-one. Also, any odd number $2r + 1$ in the co-domain $\mathbf{N}$ is the image of $2r + 2$ in the domain $\mathbf{N}$ and any even number $2r$ in the co-domain $\mathbf{N}$ is the image of $2r - 1$ in the domain $\mathbf{N}$. Thus, $f$ is onto.

Example 13 Show that an onto function $f \colon \{1,2,3\} \to \{1,2,3\}$ is always one-one.

Solution Suppose $f$ is not one-one. Then there exists two elements, say 1 and 2 in the domain whose image in the co-domain is same. Also, the image of 3 under $f$ can be only one element. Therefore, the range set can have at the most two elements of the co-domain $\{1, 2, 3\}$, showing that $f$ is not onto, a contradiction. Hence, $f$ must be one-one.

Example 14 Show that a one-one function $f\colon \{1,2,3\} \to \{1,2,3\}$ must be onto.

Solution Since $f$ is one-one, three elements of $\{1, 2, 3\}$ must be taken to 3 different elements of the co-domain $\{1, 2, 3\}$ under $f$. Hence, $f$ has to be onto.

Remark The results mentioned in Examples 13 and 14 are also true for an arbitrary finite set X, i.e., a one-one function $f: \mathrm{X} \to \mathrm{X}$ is necessarily onto and an onto map $f: \mathrm{X} \to \mathrm{X}$ is necessarily one-one, for every finite set X. In contrast to this, Examples 8 and 10 show that for an infinite set, this may not be true. In fact, this is a characteristic difference between a finite and an infinite set.

## EXERCISE 1.2

1. Show that the function $f: \mathbf{R}_{*} \to \mathbf{R}_{*}$ defined by $f(x) = \frac{1}{x}$ is one-one and onto, where $\mathbf{R}_{*}$ is the set of all non-zero real numbers. Is the result true, if the domain $\mathbf{R}_{*}$ is replaced by $\mathbf{N}$ with co-domain being same as $\mathbf{R}_{*}$?

2. Check the injectivity and surjectivity of the following functions:

(i) $f:\mathbf{N}\to \mathbf{N}$ given by $f(x) = x^{2}$

(ii) $f\colon \mathbf{Z}\to \mathbf{Z}$ given by $f(x) = x^{2}$

(iii) $f\colon \mathbf{R}\to \mathbf{R}$ given by $f(x) = x^{2}$

(iv) $f\colon \mathbf{N}\to \mathbf{N}$ given by $f(x) = x^{3}$

(v) $f\colon \mathbf{Z}\to \mathbf{Z}$ given by $f(x) = x^{3}$

3. Prove that the Greatest Integer Function $f\colon \mathbf{R}\to \mathbf{R}$, given by $f(x) = [x]$, is neither one-one nor onto, where $[x]$ denotes the greatest integer less than or equal to $x$.

Reprint 2025-26

<!-- page 11 of 17 -->

RELATIONS AND FUNCTIONS

11

4. Show that the Modulus Function $f: \mathbf{R} \to \mathbf{R}$, given by $f(x) = |x|$, is neither one-one nor onto, where $|x|$ is $x$, if $x$ is positive or 0 and $|x|$ is $-x$, if $x$ is negative.

5. Show that the Signum Function $f\colon \mathbf{R}\to \mathbf{R}$, given by

$$
f (x) = \left\{ \begin{array}{l} 1, \text {if} x > 0 \\ 0, \text {if} x = 0 \\ 1, \text {if} x <   0 \end{array} \right.
$$

is neither one-one nor onto.

6. Let $A = \{1, 2, 3\}$, $B = \{4, 5, 6, 7\}$ and let $f = \{(1, 4), (2, 5), (3, 6)\}$ be a function from A to B. Show that $f$ is one-one.

7. In each of the following cases, state whether the function is one-one, onto or bijective. Justify your answer.

(i) $f\colon \mathbf{R}\to \mathbf{R}$ defined by $f(x) = 3 - 4x$

(ii) $f\colon \mathbf{R}\to \mathbf{R}$ defined by $f(x) = 1 + x^{2}$

8. Let A and B be sets. Show that  $f: A \times B \rightarrow B \times A$  such that  $f(a, b) = (b, a)$  is bijective function.

9. Let $f: \mathbf{N} \to \mathbf{N}$ be defined by $f(n) = \begin{cases} \frac{n + 1}{2}, & \text{if } n \text{ is odd} \\ \frac{n}{2}, & \text{if } n \text{ is even} \end{cases}$ for all $n \in \mathbf{N}$.

State whether the function $f$ is bijective. Justify your answer.

10. Let $\mathrm{A} = \mathbf{R} - \{3\}$ and $\mathrm{B} = \mathbf{R} - \{1\}$. Consider the function $f: \mathrm{A} \to \mathrm{B}$ defined by $f(x) = \left(\frac{x - 2}{x - 3}\right)$. Is $f$ one-one and onto? Justify your answer.

11. Let $f: \mathbf{R} \to \mathbf{R}$ be defined as $f(x) = x^4$. Choose the correct answer.
(A) $f$ is one-one onto (B) $f$ is many-one onto
(C) $f$ is one-one but not onto (D) $f$ is neither one-one nor onto.

12. Let $f: \mathbf{R} \to \mathbf{R}$ be defined as $f(x) = 3x$. Choose the correct answer.
(A) $f$ is one-one onto (B) $f$ is many-one onto
(C) $f$ is one-one but not onto (D) $f$ is neither one-one nor onto.

Reprint 2025-26

<!-- page 12 of 17 -->

12

MATHEMATICS

## 1.4 Composition of Functions and Invertible Function

Definition 8 Let $f: \mathrm{A} \rightarrow \mathrm{B}$ and $g: \mathrm{B} \rightarrow \mathrm{C}$ be two functions. Then the composition of $f$ and $g$, denoted by gof, is defined as the function gof: $\mathrm{A} \rightarrow \mathrm{C}$ given by

$$
g o f (x) = g (f (x)), \forall x \in \mathrm{A}.
$$

![Image block](doc:348d763/tier:standard/page:12/block:6)

Fig 1.5

Example 15 Let $f:\{2,3,4,5\}\to\{3,4,5,9\}$ and $g:\{3,4,5,9\}\to\{7,11,15\}$ be functions defined as $f(2)=3$, $f(3)=4$, $f(4)=f(5)=5$ and $g(3)=g(4)=7$ and $g(5)=g(9)=11$. Find gof.

Solution We have $gof(2) = g(f(2)) = g(3) = 7$, $gof(3) = g(f(3)) = g(4) = 7$, $gof(4) = g(f(4)) = g(5) = 11$ and $gof(5) = g(5) = 11$.

Example 16 Find gof and fog, if $f: \mathbf{R} \to \mathbf{R}$ and $g: \mathbf{R} \to \mathbf{R}$ are given by $f(x) = \cos x$ and $g(x) = 3x^2$. Show that gof ≠ fog.

Solution We have  $gof(x) = g(f(x)) = g(\cos x) = 3 (\cos x)^{2} = 3 \cos^{2} x$ . Similarly,  $fog(x) = f(g(x)) = f(3x^{2}) = \cos(3x^{2})$ . Note that  $3\cos^{2} x \neq \cos 3x^{2}$ , for x = 0. Hence,  $gof \neq fog$ .

Definition 9 A function $f \colon \mathrm{X} \to \mathrm{Y}$ is defined to be invertible, if there exists a function $g \colon \mathrm{Y} \to \mathrm{X}$ such that $gof = \mathrm{I}_{\mathrm{X}}$ and $fog = \mathrm{I}_{\mathrm{Y}}$. The function $g$ is called the inverse off and is denoted by $f^{-1}$.

Thus, if f is invertible, then f must be one-one and onto and conversely, if f is one-one and onto, then f must be invertible. This fact significantly helps for proving a function f to be invertible by showing that f is one-one and onto, specially when the actual inverse of f is not to be determined.

Example 17 Let $f: \mathbf{N} \to \mathbf{Y}$ be a function defined as $f(x) = 4x + 3$, where, $\mathbf{Y} = \{y \in \mathbf{N}: y = 4x + 3 \text{ for some } x \in \mathbf{N}\}$. Show that $f$ is invertible. Find the inverse.

Solution Consider an arbitrary element $y$ of $\mathbf{Y}$. By the definition of $\mathbf{Y}, y = 4x + 3$, for some $x$ in the domain $\mathbf{N}$. This shows that $x = \frac{(y - 3)}{4}$. Define $g: \mathbf{Y} \to \mathbf{N}$ by

Reprint 2025-26

<!-- page 13 of 17 -->

RELATIONS AND FUNCTIONS

13

$$
g (y) = \frac {(y - 3)}{4}. \text {Now,} g o f (x) = g (f (x)) = g (4 x + 3) = \frac {(4 x + 3 - 3)}{4} = x \text {and}
$$

$fog(y) = f(g(y)) = f\left(\frac{(y-3)}{4}\right) = \frac{4(y-3)}{4} + 3 = y - 3 + 3 = y.$ This shows that $gof = I_N$ and $fog = I_Y$, which implies that $f$ is invertible and $g$ is the inverse of $f$.

## Miscellaneous Examples

Example 18 If $\mathrm{R}_1$ and $\mathrm{R}_2$ are equivalence relations in a set A, show that $\mathrm{R}_1 \cap \mathrm{R}_2$ is also an equivalence relation.

Solution Since  $R_{1}$  and  $R_{2}$  are equivalence relations,  $(a, a) \in \mathrm{R}_{1}$ , and  $(a, a) \in \mathrm{R}_{2} \forall a \in \mathrm{A}$ . This implies that  $(a, a) \in \mathrm{R}_{1} \cap \mathrm{R}_{2}, \forall a$ , showing  $R_{1} \cap R_{2}$  is reflexive. Further,  $(a, b) \in \mathrm{R}_{1} \cap \mathrm{R}_{2} \Rightarrow (a, b) \in \mathrm{R}_{1}$  and  $(a, b) \in \mathrm{R}_{2} \Rightarrow (b, a) \in \mathrm{R}_{1}$  and  $(b, a) \in \mathrm{R}_{2} \Rightarrow (b, a) \in \mathrm{R}_{1} \cap \mathrm{R}_{2}$ , hence,  $R_{1} \cap R_{2}$  is symmetric. Similarly,  $(a, b) \in \mathrm{R}_{1} \cap \mathrm{R}_{2}$  and  $(b, c) \in \mathrm{R}_{1} \cap \mathrm{R}_{2} \Rightarrow (a, c) \in \mathrm{R}_{1}$  and  $(a, c) \in \mathrm{R}_{2} \Rightarrow (a, c) \in \mathrm{R}_{1} \cap \mathrm{R}_{2}$ . This shows that  $R_{1} \cap R_{2}$  is transitive. Thus,  $R_{1} \cap R_{2}$  is an equivalence relation.

Example 19 Let R be a relation on the set A of ordered pairs of positive integers defined by  $(x,y)$  R  $(u,v)$  if and only if xv = yu. Show that R is an equivalence relation.

Solution Clearly, $(x,y)$ R $(x,y)$, $\forall (x,y)\in A$, since $xy = yx$. This shows that R is reflexive. Further, $(x,y)$ R $(u,v)\Rightarrow xv = yu\Rightarrow uy = vx$ and hence $(u,v)$ R $(x,y)$. This shows that R is symmetric. Similarly, $(x,y)$ R $(u,v)$ and $(u,v)$ R $(a,b)\Rightarrow xv = yu$ and $ub = va\Rightarrow xv\frac{a}{u} = yu\frac{a}{u}\Rightarrow xv\frac{b}{v} = yu\frac{a}{u}\Rightarrow xb = ya$ and hence $(x,y)$ R $(a,b)$. Thus, R is transitive. Thus, R is an equivalence relation.

Example 20 Let $\mathrm{X} = \{1, 2, 3, 4, 5, 6, 7, 8, 9\}$. Let $\mathrm{R}_1$ be a relation in $\mathrm{X}$ given by $\mathrm{R}_1 = \{(x, y) : x - y \text{ is divisible by } 3\}$ and $\mathrm{R}_2$ be another relation on $\mathrm{X}$ given by $\mathrm{R}_2 = \{(x, y) : \{x, y\} \subset \{1, 4, 7\}\}$ or $\{x, y\} \subset \{2, 5, 8\}$ or $\{x, y\} \subset \{3, 6, 9\}\}$. Show that $\mathrm{R}_1 = \mathrm{R}_2$.

Solution Note that the characteristic of sets $\{1, 4, 7\}$, $\{2, 5, 8\}$ and $\{3, 6, 9\}$ is that difference between any two elements of these sets is a multiple of 3. Therefore, $(x, y) \in \mathrm{R}_1 \Rightarrow x - y$ is a multiple of $3 \Rightarrow \{x, y\} \subset \{1, 4, 7\}$ or $\{x, y\} \subset \{2, 5, 8\}$ or $\{x, y\} \subset \{3, 6, 9\} \Rightarrow (x, y) \in \mathrm{R}_2$. Hence, $\mathrm{R}_1 \subset \mathrm{R}_2$. Similarly, $\{x, y\} \in \mathrm{R}_2 \Rightarrow \{x, y\}$

Reprint 2025-26

<!-- page 14 of 17 -->

14

MATHEMATICS

$\subset \{1,4,7\}$ or $\{x,y\} \subset \{2,5,8\}$ or $\{x,y\} \subset \{3,6,9\} \Rightarrow x - y$ is divisible by $3\Rightarrow \{x,y\} \in \mathrm{R}_1$. This shows that $\mathrm{R}_2\subset \mathrm{R}_1$. Hence, $\mathrm{R}_1 = \mathrm{R}_2$.

Example 21 Let $f: X \to Y$ be a function. Define a relation R in X given by $R = \{(a, b): f(a) = f(b)\}$. Examine whether R is an equivalence relation or not.

Solution For every $a \in X$, $(a, a) \in \mathbb{R}$, since $f(a) = f(a)$, showing that $\mathbb{R}$ is reflexive. Similarly, $(a, b) \in \mathbb{R} \Rightarrow f(a) = f(b) \Rightarrow f(b) = f(a) \Rightarrow (b, a) \in \mathbb{R}$. Therefore, $\mathbb{R}$ is symmetric. Further, $(a, b) \in \mathbb{R}$ and $(b, c) \in \mathbb{R} \Rightarrow f(a) = f(b)$ and $f(b) = f(c) \Rightarrow f(a) = f(c) \Rightarrow (a, c) \in \mathbb{R}$, which implies that $\mathbb{R}$ is transitive. Hence, $\mathbb{R}$ is an equivalence relation.

Example 22 Find the number of all one-one functions from set $\mathrm{A} = \{1,2,3\}$ to itself.

Solution One-one function from $\{1, 2, 3\}$ to itself is simply a permutation on three symbols $1, 2, 3$. Therefore, total number of one-one maps from $\{1, 2, 3\}$ to itself is same as total number of permutations on three symbols $1, 2, 3$ which is $3! = 6$.

Example 23 Let $\mathrm{A} = \{1, 2, 3\}$. Then show that the number of relations containing (1, 2) and (2, 3) which are reflexive and transitive but not symmetric is three.

Solution The smallest relation  $R_{1}$  containing (1, 2) and (2, 3) which is reflexive and transitive but not symmetric is  $\{(1, 1), (2, 2), (3, 3), (1, 2), (2, 3), (1, 3)\}$ . Now, if we add the pair (2, 1) to  $R_{1}$  to get  $R_{2}$ , then the relation  $R_{2}$  will be reflexive, transitive but not symmetric. Similarly, we can obtain  $R_{3}$  by adding (3, 2) to  $R_{1}$  to get the desired relation. However, we can not add two pairs (2, 1), (3, 2) or single pair (3, 1) to  $R_{1}$  at a time, as by doing so, we will be forced to add the remaining pair in order to maintain transitivity and in the process, the relation will become symmetric also which is not required. Thus, the total number of desired relations is three.

Example 24 Show that the number of equivalence relation in the set $\{1, 2, 3\}$ containing $(1, 2)$ and $(2, 1)$ is two.

Solution The smallest equivalence relation  $R_{1}$  containing  $(1, 2)$  and  $(2, 1)$  is  $\{(1, 1), (2, 2), (3, 3), (1, 2), (2, 1)\}$ . Now we are left with only 4 pairs namely  $(2, 3)$ ,  $(3, 2)$ ,  $(1, 3)$  and  $(3, 1)$ . If we add any one, say  $(2, 3)$  to  $R_{1}$ , then for symmetry we must add  $(3, 2)$  also and now for transitivity we are forced to add  $(1, 3)$  and  $(3, 1)$ . Thus, the only equivalence relation bigger than  $R_{1}$  is the universal relation. This shows that the total number of equivalence relations containing  $(1, 2)$  and  $(2, 1)$  is two.

Example 25 Consider the identity function $\mathrm{I}_{\mathbf{N}}: \mathbf{N} \to \mathbf{N}$ defined as $\mathrm{I}_{\mathbf{N}}(x) = x \forall x \in \mathbf{N}$. Show that although $\mathrm{I}_{\mathbf{N}}$ is onto but $\mathrm{I}_{\mathbf{N}} + \mathrm{I}_{\mathbf{N}}: \mathbf{N} \to \mathbf{N}$ defined as

$$
(\mathrm{I} _ {\mathrm{N}} + \mathrm{I} _ {\mathrm{N}}) (x) = \mathrm{I} _ {\mathrm{N}} (x) + \mathrm{I} _ {\mathrm{N}} (x) = x + x = 2 x \text {is not onto.}
$$

Reprint 2025-26

<!-- page 15 of 17 -->

RELATIONS AND FUNCTIONS

15

Solution Clearly  $I_{N}$  is onto. But  $I_{N} + I_{N}$  is not onto, as we can find an element 3 in the co-domain N such that there does not exist any x in the domain N with  $(\mathrm{I}_{\mathrm{N}} + \mathrm{I}_{\mathrm{N}})(x) = 2x = 3$ .

Example 26 Consider a function $f: \left[0, \frac{\pi}{2}\right] \to \mathbf{R}$ given by $f(x) = \sin x$ and $g: \left[0, \frac{\pi}{2}\right] \to \mathbf{R}$ given by $g(x) = \cos x$. Show that $f$ and $g$ are one-one, but $f + g$ is not one-one.

Solution Since for any two distinct elements $x_{1}$ and $x_{2}$ in $\left[0, \frac{\pi}{2}\right]$, $\sin x_{1} \neq \sin x_{2}$ and $\cos x_{1} \neq \cos x_{2}$, both $f$ and $g$ must be one-one. But $(f + g)(0) = \sin 0 + \cos 0 = 1$ and $(f + g)\left(\frac{\pi}{2}\right) = \sin \frac{\pi}{2} + \cos \frac{\pi}{2} = 1$. Therefore, $f + g$ is not one-one.

## Miscellaneous Exercise on Chapter 1

1. Show that the function $f \colon \mathbf{R} \to \{x \in \mathbf{R} : -1 < x < 1\}$ defined by $f(x) = \frac{x}{1 + |x|}$, $x \in \mathbf{R}$ is one one and onto function.

2. Show that the function $f\colon \mathbf{R}\to \mathbf{R}$ given by $f(x) = x^3$ is injective.

3. Given a non empty set $\mathrm{X}$, consider $\mathrm{P(X)}$ which is the set of all subsets of $\mathrm{X}$. Define the relation $\mathrm{R}$ in $\mathrm{P(X)}$ as follows: For subsets $\mathrm{A}, \mathrm{B}$ in $\mathrm{P(X)}$, ARB if and only if $\mathrm{A} \subset \mathrm{B}$. Is $\mathrm{R}$ an equivalence relation on $\mathrm{P(X)}$? Justify your answer.

4. Find the number of all onto functions from the set $\{1, 2, 3, \dots, n\}$ to itself.

5. Let $\mathrm{A} = \{-1, 0, 1, 2\}$, $\mathrm{B} = \{-4, -2, 0, 2\}$ and $f, g: \mathrm{A} \to \mathrm{B}$ be functions defined by $f(x) = x^2 - x$, $x \in \mathrm{A}$ and $g(x) = 2 \left| x - \frac{1}{2} \right| - 1$, $x \in \mathrm{A}$. Are $f$ and $g$ equal? Justify your answer. (Hint: One may note that two functions $f: \mathrm{A} \to \mathrm{B}$ and $g: \mathrm{A} \to \mathrm{B}$ such that $f(a) = g(a) \forall a \in \mathrm{A}$, are called equal functions).

Reprint 2025-26

<!-- page 16 of 17 -->

16

MATHEMATICS

6. Let $A = \{1, 2, 3\}$. Then number of relations containing (1, 2) and (1, 3) which are reflexive and symmetric but not transitive is
(A) 1 (B) 2 (C) 3 (D) 4

7. Let $A = \{1, 2, 3\}$. Then number of equivalence relations containing (1, 2) is (A) 1 (B) 2 (C) 3 (D) 4

## Summary

In this chapter, we studied different types of relations and equivalence relation, composition of functions, invertible functions and binary operations. The main features of this chapter are as follows:

Empty relation is the relation R in X given by  $R = \phi \subset X \times X$ .

◆ Universal relation is the relation R in X given by  $R = X \times X$ .

Reflexive relation R in X is a relation with $(a, a) \in \mathbb{R} \forall a \in X$.

Symmetric relation R in X is a relation satisfying $(a, b) \in \mathbb{R}$ implies $(b, a) \in \mathbb{R}$.

Transitive relation R in X is a relation satisfying  $(a, b) \in \mathrm{R}$  and  $(b, c) \in \mathrm{R}$  implies that  $(a, c) \in \mathrm{R}$ .

Equivalence relation R in X is a relation which is reflexive, symmetric and transitive.

Equivalence class [a] containing $a \in X$ for an equivalence relation R in X is the subset of X containing all elements $b$ related to $a$.

A function $f\colon X\to Y$ is one-one (or injective) if

$$
f (x _ {1}) = f (x _ {2}) \Rightarrow x _ {1} = x _ {2} \forall x _ {1}, x _ {2} \in \mathrm{X}.
$$

A function $f: \mathrm{X} \to \mathrm{Y}$ is onto (or surjective) if given any $y \in \mathrm{Y}, \exists x \in \mathrm{X}$ such that $f(x) = y$.

A function $f\colon X \to Y$ is one-one and onto (or bijective), if $f$ is both one-one and onto.

Given a finite set $X$, a function $f\colon X \to X$ is one-one (respectively onto) if and only if $f$ is onto (respectively one-one). This is the characteristic property of a finite set. This is not true for infinite set

Reprint 2025-26

<!-- page 17 of 17 -->

RELATIONS AND FUNCTIONS

17

## Historical Note

The concept of function has evolved over a long period of time starting from R. Descartes (1596-1650), who used the word ‘function’ in his manuscript “Geometrie” in 1637 to mean some positive integral power  $x^{n}$  of a variable x while studying geometrical curves like hyperbola, parabola and ellipse. James Gregory (1636-1675) in his work “Vera Circuli et Hyperbolae Quadratura” (1667) considered function as a quantity obtained from other quantities by successive use of algebraic operations or by any other operations. Later G. W. Leibnitz (1646-1716) in his manuscript “Methodus tangentium inversa, seu de functionibus” written in 1673 used the word ‘function’ to mean a quantity varying from point to point on a curve such as the coordinates of a point on the curve, the slope of the curve, the tangent and the normal to the curve at a point. However, in his manuscript “Historia” (1714), Leibnitz used the word ‘function’ to mean quantities that depend on a variable. He was the first to use the phrase ‘function of x’. John Bernoulli (1667-1748) used the notation  $\phi x$  for the first time in 1718 to indicate a function of x. But the general adoption of symbols like f, F,  $\phi$ ,  $\psi$  ... to represent functions was made by Leonhard Euler (1707-1783) in 1734 in the first part of his manuscript “Analysis Infinitorium”. Later on, Joseph Louis Lagrange (1736-1813) published his manuscripts “Theorie des functions analytiques” in 1793, where he discussed about analytic function and used the notion  $f(x)$ ,  $F(x)$ ,  $\phi(x)$  etc. for different function of x. Subsequently, Lejeunne Dirichlet (1805-1859) gave the definition of function which was being used till the set theoretic definition of function presently used, was given after set theory was developed by Georg Cantor (1845-1918). The set theoretic definition of function known to us presently is simply an abstraction of the definition given by Dirichlet in a rigorous manner.

Reprint 2025-26