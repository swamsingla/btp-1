# Modular Arithmetic

Modular arithmetic is a way to do maths with remainders [S1]. It is the maths behind the face of a clock. When we move past 12, we start over at 1. This page shows you how to write modular arithmetic, how it works on a clock, and how you can use it to check if a number is divisible by another number.

## The Rule a ≡ b (mod n)

In modular arithmetic, two numbers are related if they leave the same remainder when you divide them by a chosen number [S1]. We write this using the symbol $\equiv$, and we say the two numbers are congruent. The chosen number is called the modulus, written as $n$ [S1]. The rule is written as $a \equiv b \pmod{n}$ [S1].

This means that if you divide $a$ and $b$ by $n$, the remainders are the same [S1]. It also means that the difference $a - b$ is a multiple of $n$ [S1]. For example, $14 \equiv 2 \pmod{12}$ [S1]. This is because $14$ and $2$ both leave a remainder of $2$ when you divide them by $12$ [S1].

## Clock Arithmetic

Clock arithmetic is a simple way to understand modular arithmetic [S1]. A clock is a circle with $12$ numbers [S1]. After $12$ comes $1$ again [S1]. This is exactly how modular arithmetic works [S1].

The modulus of a clock is $12$ [S1]. If it is $10$ o'clock now and you add $5$ hours, you do not get $15$ o'clock [S1]. You get $3$ o'clock [S1]. In modular arithmetic, we write $10 + 5 \equiv 3 \pmod{12}$ [S1]. The $12$ hours on the clock wrap around, just like the numbers in modular arithmetic [S1].

## Divisibility

You can use modular arithmetic to check if a number is divisible by another number [S1]. A number is divisible by $n$ if its remainder is $0$ [S1]. In modular arithmetic, we write this as $a \equiv 0 \pmod{n}$ [S1].

To check if a number is divisible by $2$, you only need to look at the last digit [S1]. If the last digit is $0$, $2$, $4$, $6$, or $8$, the number is divisible by $2$ [S1]. This is because any number ending in one of these digits leaves a remainder of $0$ when divided by $2$ [S1]. The reason is that $10$ is a multiple of $2$, so only the last digit can change the remainder.

To check if a number is divisible by $3$, you add all the digits together [S1]. If the sum is divisible by $3$, then the original number is also divisible by $3$ [S1]. For example, to check if $24$ is divisible by $3$, you add $2 + 4 = 6$ [S1]. Since $6$ is divisible by $3$, $24$ is also divisible by $3$ [S1]. This works because $10 \equiv 1 \pmod{3}$, so every place value ($1$, $10$, $100$ and so on) leaves a remainder of $1$ when divided by $3$, and a number leaves the same remainder as the sum of its digits.

To check if a number is divisible by $5$, you look at the last digit [S1]. If it is $0$ or $5$, the number is divisible by $5$ [S1]. This is because any number ending in $0$ or $5$ leaves a remainder of $0$ when divided by $5$ [S1].

To check if a number is divisible by $10$, you look at the last digit [S1]. If it is $0$, the number is divisible by $10$ [S1]. This is because any number ending in $0$ leaves a remainder of $0$ when divided by $10$ [S1].

## Worked example

Let us use the rules from the previous section to check a number [S1]. Consider the number $340$ [S1].

First, we check if it is divisible by $2$ [S1]. The last digit is $0$, which is an even number. So, $340$ is divisible by $2$ [S1].

Next, we check if it is divisible by $5$ [S1]. The last digit is $0$, which means it is divisible by $5$ [S1].

Then, we check if it is divisible by $10$ [S1]. The last digit is $0$, so it is divisible by $10$ [S1].

Finally, we check if it is divisible by $3$. We add the digits: $3 + 4 + 0 = 7$. Since $7$ is not divisible by $3$, $340$ is not divisible by $3$. In fact, $340 = 3 \times 113 + 1$, so $340 \equiv 1 \pmod{3}$.

## Key points

* Modular arithmetic is a way to do maths with remainders [S1].
* The rule $a \equiv b \pmod{n}$ means $a$ and $b$ leave the same remainder when divided by $n$ [S1].
* Clock arithmetic is an example of modular arithmetic with a modulus of $12$ [S1].
* You can use modular arithmetic to check if a number is divisible by $2$, $3$, $5$, or $10$ [S1].
* A number is divisible by $2$ if its last digit is even [S1].
* A number is divisible by $5$ if its last digit is $0$ or $5$, and divisible by $10$ if its last digit is $0$ [S1].
* To check if a number is divisible by $3$, add all its digits together [S1].

<!-- TERMS: modular arithmetic, modulus, clock arithmetic, divisibility, remainder, HCF, LCM, congruence, Highest Common Factor, least common multiple -->