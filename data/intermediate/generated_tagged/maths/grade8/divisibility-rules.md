
# Divisibility Rules

Divisibility rules are quick tests you can use to check whether one number divides another without actually doing the division. They are incredibly useful for simplifying fractions, finding factors, and checking your homework answers quickly. Instead of performing long division, you just look at the digits of the number, which saves a lot of time and mental energy.

## Divisibility by 10, 5, and 2

If the units digit of a number is '0', then it is divisible by 10. We can understand why this works by looking at the general form of a number. Any number can be written in general as ...dcba, where the letter-numbers $a$, $b$, $c$ and $d$ represent the units, tens, hundreds and thousands digit, respectively. As a sum of place values, this number is —
$$
\ldots + 1 0 0 0 d + 1 0 0 c + 1 0 b + a.
$$
We know that each place value, with the exception of the units place, is a multiple of 10. So, $10b$, $100c$, ... all will be multiples of 10. Hence, the number will be divisible by 10 if and only if the units digit $a$ is 0 [S2].

For divisibility by 5 and 2, you only need to look at the units digit. If the units digit is 0 or 5, the number is divisible by 5. If the units digit is even (0, 2, 4, 6, or 8), the number is divisible by 2 [S2].

## Divisibility by 9

A number is divisible by 9 if and only if the sum of its digits is divisible by 9. We can add the digits of a number repeatedly until we get a single digit. This single digit is the remainder when the number is divided by 9 [S3].

This works because each place value is one more than a multiple of 9. For example:
$$
1 = 0 + 1 \\
10 = 9 + 1 \\
100 = 99 + 1
$$
Each digit thus denotes the remainder when the corresponding place value is divided by 9. For example, to find the remainder of 7309 when divided by 9, we can just add all the digits— $7 + 3 + 0 + 9$ —to get 19. This can be seen as follows:
$$
7 \times 1000 + 3 \times 100 + 0 \times 10 + 9 \times 1
$$
$$
= 7 \times (999 + 1) + 3 \times (99 + 1) + 0 \times (9 + 1) + 9 \times (0 + 1)
$$
$$
= (7 \times 999 + 3 \times 99 + 0 \times 9 + 9 \times 0) + (7 \times 1 + 3 \times 1 + 0 \times 1 + 9 \times 1)
$$
$$
= (7 \times 999 + 3 \times 99 + 0 \times 9 + 9 \times 0) + (7 + 3 + 0 + 9)
$$
This is a multiple of 9, so we only need to consider the sum of the digits [S3, S6].

## Worked example

Let's apply the rule for 9 to the number 427. We add the digits: $4 + 2 + 7 = 13$. We can make one more group of 9 with 13, leaving a remainder of 4. Therefore, $427 \div 9$ gives a remainder of 4 [S6].

## Divisibility by 4, 8, and 5

For divisibility by 4, you need to look at the last two digits of the number. If the number formed by the last two digits is divisible by 4, then the whole number is divisible by 4.

For divisibility by 8, you need to look at the last three digits of the number. If the number formed by the last three digits is divisible by 8, then the whole number is divisible by 8.

For divisibility by 5, you just need to look at the units digit. If the units digit is 0 or 5, the number is divisible by 5.

## Key points

*   Divisibility rules are quick tests to check if one number divides another without doing the division.
*   For 10, 5, and 2, you only need to look at the units digit.
*   For 9, you add the digits of the number repeatedly until you get a single digit.
*   For 4, 8, and 5, you look at the last two or three digits of the number.
*   Learning maths is not just about knowing some shortcuts and following procedures but about understanding 'why' something works.