
# Euclidean Algorithm

The Euclidean Algorithm is a fast way to find the Highest Common Factor (HCF) of two numbers. Instead of writing out all the factors, you use repeated division to get the answer quickly. This method is very useful when you have large numbers, because listing all the factors can take a very long time.

## The Idea of Repeated Division

To find the HCF of two numbers, you divide the larger number by the smaller number. The remainder from this division is important. If the remainder is zero, then the smaller number is the HCF. If the remainder is not zero, you take the smaller number and divide it by the remainder. You keep doing this until the remainder is zero. The last non-zero remainder is the HCF [S1].

## Step-by-Step Process

Here is how you do it. Let us find the HCF of 56 and 12.

First, divide 56 by 12.
$56 = 12 \times 4 + 8$
The remainder is 8.

Next, divide 12 by 8.
$12 = 8 \times 1 + 4$
The remainder is 4.

Then, divide 8 by 4.
$8 = 4 \times 2 + 0$
The remainder is 0.

Since the remainder is 0, we stop. The last non-zero remainder is 4. So, the HCF of 56 and 12 is 4.

## Why This Works

This method works because the HCF of two numbers is the same as the HCF of the smaller number and the remainder [S1]. When you divide a number, the remainder is always smaller than the number you are dividing by. By repeating this process, the numbers get smaller and smaller very quickly. This makes it much easier to find the HCF without making mistakes.

## Worked example

Let us find the HCF of 100 and 36.

First, divide 100 by 36.
$100 = 36 \times 2 + 28$
The remainder is 28.

Next, divide 36 by 28.
$36 = 28 \times 1 + 8$
The remainder is 8.

Then, divide 28 by 8.
$28 = 8 \times 3 + 4$
The remainder is 4.

Finally, divide 8 by 4.
$8 = 4 \times 2 + 0$
The remainder is 0.

The last non-zero remainder is 4. Therefore, the HCF of 100 and 36 is 4.

## Key points
* The Euclidean Algorithm finds the HCF using repeated division.
* Divide the larger number by the smaller number and note the remainder.
* If the remainder is zero, the smaller number is the HCF.
* If the remainder is not zero, divide the smaller number by the remainder and repeat.
* The last non-zero remainder is the HCF of the original two numbers.
<!-- TERMS: Highest Common Factor, remainder, division, factors -->