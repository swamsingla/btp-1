<!-- page 1 of 32 -->

110785415

11076CH15

Chapter

13

# STATISTICS

❖ “Statistics may be rightly called the science of averages and their estimates.” – A.L.BOWLEY & A.L. BODDINGTON ❖

## 13.1 Introduction

We know that statistics deals with data collected for specific purposes. We can make decisions about the data by analysing and interpreting it. In earlier classes, we have studied methods of representing data graphically and in tabular form. This representation reveals certain salient features or characteristics of the data. We have also studied the methods of finding a representative value for the given data. This value is called the measure of central tendency. Recall mean (arithmetic mean), median and mode are three measures of central tendency. A measure of central tendency gives us a rough idea where data points are centred. But, in order to make better interpretation from the

![Image block](doc:a82387d/tier:standard/page:1/block:9)

Karl Pearson (1857-1936)

data, we should also have an idea how the data are scattered or how much they are bunched around a measure of central tendency.

Consider now the runs scored by two batsmen in their last ten matches as follows:

Batsman A : 30, 91, 0, 64, 42, 80, 30, 5, 117, 71

Batsman B : 53, 46, 48, 50, 53, 53, 58, 60, 57, 52

Clearly, the mean and median of the data are

|  | Batsman A | Batsman B |
| --- | --- | --- |
| Mean | 53 | 53 |
| Median | 53 | 53 |

Recall that, we calculate the mean of a data (denoted by  $\bar{x}$ ) by dividing the sum of the observations by the number of observations, i.e.,

Reprint 2025-26

<!-- page 2 of 32 -->

![Image block](doc:a82387d/tier:standard/page:2/block:1)

258

MATHEMATICS

$$
\overline {{x}} = \frac {1}{n} \sum_ {i = 1} ^ {n} x _ {i}
$$

Also, the median is obtained by first arranging the data in ascending or descending order and applying the following rule.

If the number of observations is odd, then the median is $\left(\frac{n + 1}{2}\right)^{\mathrm{th}}$ observation.

If the number of observations is even, then median is the mean of $\left(\frac{n}{2}\right)^{\text{th}}$ and $\left(\frac{n}{2} + 1\right)^{\text{th}}$ observations.

We find that the mean and median of the runs scored by both the batsmen A and B are same i.e., 53. Can we say that the performance of two players is same? Clearly No, because the variability in the scores of batsman A is from 0 (minimum) to 117 (maximum). Whereas, the range of the runs scored by batsman B is from 46 to 60.

Let us now plot the above scores as dots on a number line. We find the following diagrams:

For batsman A

Fig 13.2

We can see that the dots corresponding to batsman B are close to each other and are clustering around the measure of central tendency (mean and median), while those corresponding to batsman A are scattered or more spread out.

Thus, the measures of central tendency are not sufficient to give complete information about a given data. Variability is another factor which is required to be studied under statistics. Like ‘measures of central tendency’ we want to have a single number to describe variability. This single number is called a ‘measure of dispersion’. In this Chapter, we shall learn some of the important measures of dispersion and their methods of calculation for ungrouped and grouped data.

Reprint 2025-26

<!-- page 3 of 32 -->

STATISTICS

259

## 13.2 Measures of Dispersion

The dispersion or scatter in a data is measured on the basis of the observations and the types of the measure of central tendency, used there. There are following measures of dispersion:

(i) Range, (ii) Quartile deviation, (iii) Mean deviation, (iv) Standard deviation.

In this Chapter, we shall study all of these measures of dispersion except the quartile deviation.

## 13.3 Range

Recall that, in the example of runs scored by two batsmen A and B, we had some idea of variability in the scores on the basis of minimum and maximum runs in each series. To obtain a single number for this, we find the difference of maximum and minimum values of each series. This difference is called the ‘Range’ of the data.

In case of batsman A, Range = 117 - 0 = 117 and for batsman B, Range = 60 - 46 = 14. Clearly, Range of A > Range of B. Therefore, the scores are scattered or dispersed in case of A while for B these are close to each other.

Thus, Range of a series = Maximum value - Minimum value.

The range of data gives us a rough idea of variability or scatter but does not tell about the dispersion of the data from a measure of central tendency. For this purpose, we need some other measure of variability. Clearly, such measure must depend upon the difference (or deviation) of the values from the central tendency.

The important measures of dispersion, which depend upon the deviations of the observations from a central tendency are mean deviation and standard deviation. Let us discuss them in detail.

## 13.4 Mean Deviation

Recall that the deviation of an observation x from a fixed value ‘a’ is the difference x - a. In order to find the dispersion of values of x from a central value ‘a’, we find the deviations about a. An absolute measure of dispersion is the mean of these deviations. To find the mean, we must obtain the sum of the deviations. But, we know that a measure of central tendency lies between the maximum and the minimum values of the set of observations. Therefore, some of the deviations will be negative and some positive. Thus, the sum of deviations may vanish. Moreover, the sum of the deviations from mean ( $\bar{x}$ ) is zero.

Also

$$
\text {Mean of deviations} = \frac {\text {Sum of deviations}}{\text {Number of observations}} = \frac {0}{n} = 0
$$

Thus, finding the mean of deviations about mean is not of any use for us, as far as the measure of dispersion is concerned.

Reprint 2025-26

<!-- page 4 of 32 -->

260

MATHEMATICS

Remember that, in finding a suitable measure of dispersion, we require the distance of each value from a central tendency or a fixed number ‘a’. Recall, that the absolute value of the difference of two numbers gives the distance between the numbers when represented on a number line. Thus, to find the measure of dispersion from a fixed number ‘a’ we may take the mean of the absolute values of the deviations from the central value. This mean is called the ‘mean deviation’. Thus mean deviation about a central value ‘a’ is the mean of the absolute values of the deviations of the observations from ‘a’. The mean deviation from ‘a’ is denoted as M.D. (a). Therefore,

$$
\text {M.D.} (a) = \frac {\text {Sum of absolute values of deviations from 'a'}}{\text {Number of observations}}
$$

Remark Mean deviation may be obtained from any measure of central tendency. However, mean deviation from mean and median are commonly used in statistical studies.

Let us now learn how to calculate mean deviation about mean and mean deviation about median for various types of data

13.4.1 Mean deviation for ungrouped data Let $n$ observations be $x_{1}, x_{2}, x_{3}, \ldots, x_{n}$. The following steps are involved in the calculation of mean deviation about mean or median:

Step 1 Calculate the measure of central tendency about which we are to find the mean deviation. Let it be ‘a’.

Step 2 Find the deviation of each $x_{i}$ from $a$, i.e., $x_{1} - a, x_{2} - a, x_{3} - a, \ldots, x_{n} - a$

Step 3 Find the absolute values of the deviations, i.e., drop the minus sign $(-)$, if it is

there, i.e.,

$$
\left| x _ {1} - a \right|, \left| x _ {2} - a \right|, \left| x _ {3} - a \right|, \dots , \left| x _ {n} - a \right|
$$

Step 4 Find the mean of the absolute values of the deviations. This mean is the mean deviation about $a$, i.e.,

$$
\text {M.D.} (a) = \frac {\sum_ {i = 1} ^ {n} \left| x _ {i} - a \right|}{n}\left. \right\}
$$

Thus

$$
\text {M.D.} (\bar {x}) = \frac {1}{n} \sum_ {i = 1} ^ {n} \left| x _ {i} - \bar {x} \right|, \text {where} \bar {x} = \text {Mean}
$$

and

$$
\text {M.D. (M)} = \frac {1}{n} \sum_ {i = 1} ^ {n} \left| x _ {i} - \mathrm{M} \right|, \text {where M = Median}
$$

Reprint 2025-26

<!-- page 5 of 32 -->

STATISTICS

261

Note In this Chapter, we shall use the symbol M to denote median unless stated otherwise. Let us now illustrate the steps of the above method in following examples.

Example 1 Find the mean deviation about the mean for the following data:

$$
6, 7, 1 0, 1 2, 1 3, 4, 8, 1 2
$$

Solution We proceed step-wise and get the following:

Step 1 Mean of the given data is

$$
\overline {{x}} = \frac {6 + 7 + 1 0 + 1 2 + 1 3 + 4 + 8 + 1 2}{8} = \frac {7 2}{8} = 9
$$

Step 2 The deviations of the respective observations from the mean $\overline{x}$, i.e., $x_{i} - \overline{x}$ are

$$
6 - 9, 7 - 9, 1 0 - 9, 1 2 - 9, 1 3 - 9, 4 - 9, 8 - 9, 1 2 - 9,
$$

or $-3, -2, 1, 3, 4, -5, -1, 3$

Step 3 The absolute values of the deviations, i.e., $\left|x_{i} - \overline{x}\right|$ are

3, 2, 1, 3, 4, 5, 1, 3

Step 4 The required mean deviation about the mean is

$$
\begin{array}{r l} \text {M.D.} (\bar {x}) & = \frac {\sum_ {i = 1} ^ {8} \left| x _ {i} - \bar {x} \right|}{8} \\ & = \frac {3 + 2 + 1 + 3 + 4 + 5 + 1 + 3}{8} = \frac {2 2}{8} = 2. 7 5 \end{array}
$$

Note Instead of carrying out the steps every time, we can carry on calculation, step-wise without referring to steps.

Example 2 Find the mean deviation about the mean for the following data : 12, 3, 18, 17, 4, 9, 17, 19, 20, 15, 8, 17, 2, 3, 16, 11, 3, 1, 0, 5

Solution We have to first find the mean $(\bar{x})$ of the given data

$$
\overline {{x}} = \frac {1}{2 0} \sum_ {i = 1} ^ {2 0} x _ {i} = \frac {2 0 0}{2 0} = 1 0
$$

Reprint 2025-26

<!-- page 6 of 32 -->

262

MATHEMATICS

The respective absolute values of the deviations from mean, i.e., $\left|x_i - \overline{x}\right|$ are 2, 7, 8, 7, 6, 1, 7, 9, 10, 5, 2, 7, 8, 7, 6, 1, 7, 9, 10, 5

Therefore

$$
\left| \sum_ {i = 1} ^ {2 0} \left| x _ {i} - \bar {x} \right| = 1 2 4 \right|
$$

and

$$
\mathrm{M.D.} (\bar {x}) = \frac {1 2 4}{2 0} = 6. 2
$$

Example 3 Find the mean deviation about the median for the following data: 3, 9, 5, 3, 12, 10, 18, 4, 7, 19, 21.

Solution Here the number of observations is 11 which is odd. Arranging the data into ascending order, we have 3, 3, 4, 5, 7, 9, 10, 12, 18, 19, 21

Now Median $= \left(\frac{11 + 1}{2}\right)^{\text{th}}$ or $6^{\text{th}}$ observation $= 9$

The absolute values of the respective deviations from the median, i.e., $|x_i - \mathbf{M}|$ are 6, 6, 5, 4, 2, 0, 1, 3, 9, 10, 12

Therefore

$$
\sum_ {i = 1} ^ {1 1} \left| x _ {i} - \mathrm{M} \right| = 5 8
$$

and

$$
\text {M.D.} (\mathrm{M}) = \frac {1}{1 1} \sum_ {i = 1} ^ {1 1} \left| x _ {i} - \mathrm{M} \right| = \frac {1}{1 1} \times 5 8 = 5. 2 7
$$

13.4.2 Mean deviation for grouped data We know that data can be grouped into two ways :

(a) Discrete frequency distribution,

(b) Continuous frequency distribution.

Let us discuss the method of finding mean deviation for both types of the data.

(a) Discrete frequency distribution Let the given data consist of n distinct values  $x_{1}, x_{2}, \ldots, x_{n}$  occurring with frequencies  $f_{1}, f_{2}, \ldots, f_{n}$  respectively. This data can be represented in the tabular form as given below, and is called discrete frequency distribution:

$$
\left| \begin{array}{c c c c} x: x _ {1} & x _ {2} & x _ {3} \dots x _ {n} \end{array} \right|
$$

$$
f: f _ {1} \quad f _ {2} \quad f _ {3} \dots f _ {n}
$$

Reprint 2025-26

<!-- page 7 of 32 -->

STATISTICS

263

## (i) Mean deviation about mean

First of all we find the mean $\overline{x}$ of the given data by using the formula

$$
\overline {{x}} = \frac {\sum_ {i = 1} ^ {n} x _ {i} f _ {i}}{\sum_ {i = 1} ^ {n} f _ {i}} = \frac {1}{N} \sum_ {i = 1} ^ {n} x _ {i} f _ {i},
$$

where $\sum_{i=1}^{n} x_i f_i$ denotes the sum of the products of observations $x_i$ with their respective

frequencies $f_{i}$ and $N = \sum_{i=1}^{n} f_{i}$ is the sum of the frequencies.

Then, we find the deviations of observations $x_{i}$ from the mean $\overline{x}$ and take their absolute values, i.e., $|x_{i} - \overline{x}|$ for all $i = 1, 2, \dots, n$.

After this, find the mean of the absolute values of the deviations, which is the required mean deviation about the mean. Thus

$$
\text {M.D.} (\bar {x}) = \frac {\sum_ {i = 1} ^ {n} f _ {i} \left| x _ {i} - \bar {x} \right|}{\sum_ {i = 1} ^ {n} f _ {i}} = \frac {1}{N} \sum_ {i = 1} ^ {n} f _ {i} \left| x _ {i} - \bar {x} \right|
$$

(ii) Mean deviation about median To find mean deviation about median, we find the median of the given discrete frequency distribution. For this the observations are arranged in ascending order. After this the cumulative frequencies are obtained. Then, we identify

the observation whose cumulative frequency is equal to or just greater than  $\frac{N}{2}$ , where

N is the sum of frequencies. This value of the observation lies in the middle of the data, therefore, it is the required median. After finding median, we obtain the mean of the absolute values of the deviations from median. Thus,

$$
\text {M.D.(M)} = \frac {1}{\mathrm{N}} \sum_ {i = 1} ^ {n} f _ {i} \left| x _ {i} - \mathrm{M} \right|
$$

Example 4 Find mean deviation about the mean for the following data :

| $x_{i}$ | 2 | 5 | 6 | 8 | 10 | 12 |
| --- | --- | --- | --- | --- | --- | --- |
| $f_{i}$ | 2 | 8 | 10 | 7 | 8 | 5 |

Reprint 2025-26

<!-- page 8 of 32 -->

264

MATHEMATICS

Solution Let us make a Table 13.1 of the given data and append other columns after calculations.

Table 13.1

| $x_{i}$ | $f_{i}$ | $f_{i}x_{i}$ | $\|x_{i}-\overline{x}\|$ | $f_{i}\|x_{i}-\overline{x}\|$ |
| --- | --- | --- | --- | --- |
| 2 | 2 | 4 | 5.5 | 11 |
| 5 | 8 | 40 | 2.5 | 20 |
| 6 | 10 | 60 | 1.5 | 15 |
| 8 | 7 | 56 | 0.5 | 3.5 |
| 10 | 8 | 80 | 2.5 | 20 |
| 12 | 5 | 60 | 4.5 | 22.5 |
|  | 40 | 300 |  | 92 |

$$
\mathrm{N} = \sum_ {i = 1} ^ {6} f _ {i} = 4 0, \quad \sum_ {i = 1} ^ {6} f _ {i} x _ {i} = 3 0 0, \quad \sum_ {i = 1} ^ {6} f _ {i} \left| x _ {i} - \bar {x} \right| = 9 2
$$

Therefore

$$
\overline {{x}} = \frac {1}{\mathrm{N}} \sum_ {i = 1} ^ {6} f _ {i} x _ {i} = \frac {1}{4 0} \times 3 0 0 = 7. 5
$$

and

$$
\text {M.D.} (\bar {x}) = \frac {1}{N} \sum_ {i = 1} ^ {6} f _ {i} \left| x _ {i} - \bar {x} \right| = \frac {1}{4 0} \times 9 2 = 2. 3
$$

Example 5 Find the mean deviation about the median for the following data:

| $x_{i}$ | 3 | 6 | 9 | 12 | 13 | 15 | 21 | 22 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $f_{i}$ | 3 | 4 | 5 | 2 | 4 | 5 | 4 | 3 |

Solution The given observations are already in ascending order. Adding a row corresponding to cumulative frequencies to the given data, we get (Table 13.2).

Table 13.2

| $x_{i}$ | 3 | 6 | 9 | 12 | 13 | 15 | 21 | 22 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $f_{i}$ | 3 | 4 | 5 | 2 | 4 | 5 | 4 | 3 |
| c.f. | 3 | 7 | 12 | 14 | 18 | 23 | 27 | 30 |

Now, $N = 30$ which is even.

Reprint 2025-26

<!-- page 9 of 32 -->

STATISTICS

265

Median is the mean of the $15^{\text{th}}$ and $16^{\text{th}}$ observations. Both of these observations lie in the cumulative frequency 18, for which the corresponding observation is 13.

Therefore, Median M =  $\frac{15^{th} observation + 16^{th} observation}{2}$  =  $\frac{13 + 13}{2}$  = 13

Now, absolute values of the deviations from median, i.e., $|x_{i} - \mathbf{M}|$ are shown in Table 13.3.

Table 13.3

| $\|x_i - M\|$ | 10 | 7 | 4 | 1 | 0 | 2 | 8 | 9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $f_i$ | 3 | 4 | 5 | 2 | 4 | 5 | 4 | 3 |
| $f_i \|x_i - M\|$ | 30 | 28 | 20 | 2 | 0 | 10 | 32 | 27 |

We have

$$
\sum_ {i = 1} ^ {8} f _ {i} = 3 0 \quad \text {and} \sum_ {i = 1} ^ {8} f _ {i} \left| x _ {i} - \mathrm{M} \right| = 1 4 9
$$

Therefore

$$
\text {M.D.} (\mathrm{M}) = \frac {1}{\mathrm{N}} \sum_ {i = 1} ^ {8} f _ {i} \left| x _ {i} - \mathrm{M} \right|
$$

$$
= \frac {1}{3 0} \times 1 4 9 = 4. 9 7.
$$

(b) Continuous frequency distribution A continuous frequency distribution is a series in which the data are classified into different class-intervals without gaps along with their respective frequencies.

For example, marks obtained by 100 students are presented in a continuous frequency distribution as follows :

| Marks obtained | 0-10 | 10-20 | 20-30 | 30-40 | 40-50 | 50-60 |
| --- | --- | --- | --- | --- | --- | --- |
| Number of Students | 12 | 18 | 27 | 20 | 17 | 6 |

(i) Mean deviation about mean While calculating the mean of a continuous frequency distribution, we had made the assumption that the frequency in each class is centred at its mid-point. Here also, we write the mid-point of each given class and proceed further as for a discrete frequency distribution to find the mean deviation.

Let us take the following example.

Reprint 2025-26

<!-- page 10 of 32 -->

266

MATHEMATICS

Example 6 Find the mean deviation about the mean for the following data.

| Marks obtained | 10-20 | 20-30 | 30-40 | 40-50 | 50-60 | 60-70 | 70-80 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Number of students | 2 | 3 | 8 | 14 | 8 | 3 | 2 |

Solution We make the following Table 13.4 from the given data :

Table 13.4

| Marks obtained | Number of students$f_i$ | Mid-points$x_i$ | $f_i x_i$ | $\|x_i - \bar{x}\|$ | $f_i \|x_i - \bar{x}\|$ |
| --- | --- | --- | --- | --- | --- |
| 10-20 | 2 | 15 | 30 | 30 | 60 |
| 20-30 | 3 | 25 | 75 | 20 | 60 |
| 30-40 | 8 | 35 | 280 | 10 | 80 |
| 40-50 | 14 | 45 | 630 | 0 | 0 |
| 50-60 | 8 | 55 | 440 | 10 | 80 |
| 60-70 | 3 | 65 | 195 | 20 | 60 |
| 70-80 | 2 | 75 | 150 | 30 | 60 |
|  | 40 |  | 1800 |  | 400 |

Here

$$
\mathrm{N} = \sum_ {i = 1} ^ {7} f _ {i} = 4 0, \sum_ {i = 1} ^ {7} f _ {i} x _ {i} = 1 8 0 0, \sum_ {i = 1} ^ {7} f _ {i} \left| x _ {i} - \bar {x} \right| = 4 0 0
$$

Therefore

$$
\overline {{x}} = \frac {1}{\mathrm{N}} \sum_ {i = 1} ^ {7} f _ {i} x _ {i} = \frac {1 8 0 0}{4 0} = 4 5
$$

and

$$
\mathrm{M.D.} (\bar {x}) = \frac {1}{\mathrm{N}} \sum_ {i = 1} ^ {7} f _ {i} \left| x _ {i} - \bar {x} \right| = \frac {1}{4 0} \times 4 0 0 = 1 0
$$

Shortcut method for calculating mean deviation about mean We can avoid the tedious calculations of computing  $\bar{x}$  by following step-deviation method. Recall that in this method, we take an assumed mean which is in the middle or just close to it in the data. Then deviations of the observations (or mid-points of classes) are taken from the

Reprint 2025-26

<!-- page 11 of 32 -->

STATISTICS

267

assumed mean. This is nothing but the shifting of origin from zero to the assumed mean on the number line, as shown in Fig 13.3

![Image block](doc:a82387d/tier:standard/page:11/block:4)

Fig 13.3

If there is a common factor of all the deviations, we divide them by this common factor to further simplify the deviations. These are known as step-deviations. The process of taking step-deviations is the change of scale on the number line as shown in Fig 13.4

![Image block](doc:a82387d/tier:standard/page:11/block:7)

The deviations and step-deviations reduce the size of the observations, so that the computations viz. multiplication, etc., become simpler. Let, the new variable be denoted by $d_{i} = \frac{x_{i} - a}{h}$, where 'a' is the assumed mean and h is the common factor. Then, the mean $\overline{x}$ by step-deviation method is given by

$$
\bar {x} = a + \frac {\sum_ {i = 1} ^ {n} f _ {i} d _ {i}}{\mathrm{N}} \times h
$$

Let us take the data of Example 6 and find the mean deviation by using step-deviation method.

Reprint 2025-26

<!-- page 12 of 32 -->

268

MATHEMATICS

Take the assumed mean $a = 45$ and $h = 10$, and form the following Table 13.5.

Table 13.5

| Marks obtained | Number of students | Mid-points | $d_i = \frac{x_i - 45}{10}$ | $f_i d_i$ | $\|x_i - \bar{x}\|$ | $f_i \|x_i - \bar{x}\|$ |
| --- | --- | --- | --- | --- | --- | --- |
|  | $f_i$ | $x_i$ |  |  |  |  |
| 10-20 | 2 | 15 | -3 | -6 | 30 | 60 |
| 20-30 | 3 | 25 | -2 | -6 | 20 | 60 |
| 30-40 | 8 | 35 | -1 | -8 | 10 | 80 |
| 40-50 | 14 | 45 | 0 | 0 | 0 | 0 |
| 50-60 | 8 | 55 | 1 | 8 | 10 | 80 |
| 60-70 | 3 | 65 | 2 | 6 | 20 | 60 |
| 70-80 | 2 | 75 | 3 | 6 | 30 | 60 |
|  | 40 |  |  | 0 |  | 400 |

Therefore

$$
\bar {x} = a + \frac {\sum_ {i = 1} ^ {7} f _ {i} d _ {i}}{\mathrm{N}} \times h
$$

$$
= 4 5 + \frac {0}{4 0} \times 1 0 = 4 5
$$

and

$$
\text {M.D.} (\bar {x}) = \frac {1}{\mathrm{N}} \sum_ {i = 1} ^ {7} f _ {i} \left| x _ {i} - \bar {x} \right| = \frac {4 0 0}{4 0} = 1 0
$$

Note The step deviation method is applied to compute  $\bar{x}$ . Rest of the procedure is same.

(ii) Mean deviation about median The process of finding the mean deviation about median for a continuous frequency distribution is similar as we did for mean deviation about the mean. The only difference lies in the replacement of the mean by median while taking deviations.

Let us recall the process of finding median for a continuous frequency distribution.

The data is first arranged in ascending order. Then, the median of continuous frequency distribution is obtained by first identifying the class in which median lies (median class) and then applying the formula

Reprint 2025-26

<!-- page 13 of 32 -->

STATISTICS

269

$$
\text {Median} = l + \frac {\frac {\mathrm{N}}{2} - \mathrm{C}}{f} \times h
$$

where median class is the class interval whose cumulative frequency is just greater than or equal to $\frac{\mathrm{N}}{2}$, $\mathrm{N}$ is the sum of frequencies, $l, f, h$ and $\mathrm{C}$ are, respectively the lower limit, the frequency, the width of the median class and $\mathrm{C}$ the cumulative frequency of the class just preceding the median class. After finding the median, the absolute values of the deviations of mid-point $x_{i}$ of each class from the median i.e., $|x_{i} - \mathrm{M}|$ are obtained.

Then

$$
\mathrm{M.D.} (\mathrm{M}) = \frac {1}{\mathrm{N}} \sum_ {i = 1} ^ {n} f _ {i} \left| x _ {i} - \mathrm{M} \right|
$$

The process is illustrated in the following example:

Example 7 Calculate the mean deviation about median for the following data :

| Class | 0-10 | 10-20 | 20-30 | 30-40 | 40-50 | 50-60 |
| --- | --- | --- | --- | --- | --- | --- |
| Frequency | 6 | 7 | 15 | 16 | 4 | 2 |

Solution Form the following Table 13.6 from the given data :

![Image block](doc:a82387d/tier:standard/page:13/block:11)

Table 13.6

| Class | Frequency | Cumulative frequency | Mid-points | $\left\| {x}_{i} - \text{Med.}\right\|$ | ${f}_{i}\left\| {{x}_{i} - \text{Med.}}\right\|$ |
| --- | --- | --- | --- | --- | --- |
|  | ${f}_{i}$ | (c.f.) | ${x}_{i}$ |  |  |
| 0-10 | 6 | 6 | 5 | 23 | 138 |
| 10-20 | 7 | 13 | 15 | 13 | 91 |
| 20-30 | 15 | 28 | 25 | 3 | 45 |
| 30-40 | 16 | 44 | 35 | 7 | 112 |
| 40-50 | 4 | 48 | 45 | 17 | 68 |
| 50-60 | 2 | 50 | 55 | 27 | 54 |
|  | 50 |  |  |  | 508 |

Reprint 2025-26

<!-- page 14 of 32 -->

270

MATHEMATICS

The class interval containing  $\frac{N^{th}}{2}$  or  $25^{th}$  item is 20-30. Therefore, 20–30 is the median class. We know that

$$
\text {Median} = l + \frac {\frac {\mathrm{N}}{2} - \mathrm{C}}{f} \times h
$$

Here $l = 20$, $C = 13$, $f = 15$, $h = 10$ and $N = 50$

Therefore,

$$
\text {Median} = 2 0 + \frac {2 5 - 1 3}{1 5} \times 1 0 = 2 0 + 8 = 2 8
$$

Thus, Mean deviation about median is given by

$$
\mathrm{M.D.} (\mathrm{M}) = \frac {1}{\mathrm{N}} \sum_ {i = 1} ^ {6} f _ {i} \left| x _ {i} - \mathrm{M} \right| = \frac {1}{5 0} \times 5 0 8 = 1 0. 1 6
$$

## EXERCISE 13.1

Find the mean deviation about the mean for the data in Exercises 1 and 2.

1. 4,7,8,9,10,12,13,17

2. 38,70,48,40,42,55,63,46,54,44

Find the mean deviation about the median for the data in Exercises 3 and 4.

3. 13, 17, 16, 14, 11, 13, 10, 16, 11, 18, 12, 17

4. 36, 72, 46, 42, 60, 45, 53, 46, 51, 49

Find the mean deviation about the mean for the data in Exercises 5 and 6.

| 5. | $x_{i}$ 5 | 10 | 15 | 20 | 25 |
| --- | --- | --- | --- | --- | --- |
|  | $f_{i}$ 7 | 4 | 6 | 3 | 5 |
| 6. | $x_{i}$ 10 | 30 | 50 | 70 | 90 |
|  | $f_{i}$ 4 | 24 | 28 | 16 | 8 |

Find the mean deviation about the median for the data in Exercises 7 and 8.

| 7. | $x_{i}$ 5 | 7 | 9 | 10 | 12 | 15 |
| --- | --- | --- | --- | --- | --- | --- |
|  | $f_{i}$ 8 | 6 | 2 | 2 | 2 | 6 |
| 8. | $x_{i}$ 15 | 21 | 27 | 30 | 35 |  |
|  | $f_{i}$ 3 | 5 | 6 | 7 | 8 |  |

Reprint 2025-26

<!-- page 15 of 32 -->

STATISTICS

271

Find the mean deviation about the mean for the data in Exercises 9 and 10.

| Income per day in ₹ | 0-100 | 100-200 | 200-300 | 300-400 | 400-500 | 500-600 | 600-700 | 700-800 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Number of persons | 4 | 8 | 9 | 10 | 7 | 5 | 4 | 3 |

| Height in cms | 95-105 | 105-115 | 115-125 | 125-135 | 135-145 | 145-155 |
| --- | --- | --- | --- | --- | --- | --- |
| Number of boys | 9 | 13 | 26 | 30 | 12 | 10 |

11. Find the mean deviation about median for the following data :

| Marks | 0-10 | 10-20 | 20-30 | 30-40 | 40-50 | 50-60 |
| --- | --- | --- | --- | --- | --- | --- |
| Number of Girls | 6 | 8 | 14 | 16 | 4 | 2 |

12. Calculate the mean deviation about median age for the age distribution of 100 persons given below:

| Age (in years) | 16-20 | 21-25 | 26-30 | 31-35 | 36-40 | 41-45 | 46-50 | 51-55 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Number | 5 | 6 | 12 | 14 | 26 | 12 | 16 | 9 |

[Hint Convert the given data into continuous frequency distribution by subtracting 0.5 from the lower limit and adding 0.5 to the upper limit of each class interval]

13.4.3 Limitations of mean deviation In a series, where the degree of variability is very high, the median is not a representative central tendency. Thus, the mean deviation about median calculated for such series can not be fully relied.

The sum of the deviations from the mean (minus signs ignored) is more than the sum of the deviations from median. Therefore, the mean deviation about the mean is not very scientific. Thus, in many cases, mean deviation may give unsatisfactory results. Also mean deviation is calculated on the basis of absolute values of the deviations and therefore, cannot be subjected to further algebraic treatment. This implies that we must have some other measure of dispersion. Standard deviation is such a measure of dispersion.

## 13.5 Variance and Standard Deviation

Recall that while calculating mean deviation about mean or median, the absolute values of the deviations were taken. The absolute values were taken to give meaning to the mean deviation, otherwise the deviations may cancel among themselves.

Another way to overcome this difficulty which arose due to the signs of deviations, is to take squares of all the deviations. Obviously all these squares of deviations are

Reprint 2025-26

<!-- page 16 of 32 -->

272

MATHEMATICS

non-negative. Let $x_{1}, x_{2}, x_{3}, \ldots, x_{n}$ be $n$ observations and $\overline{x}$ be their mean. Then

$$
(x _ {1} - \bar {x}) ^ {2} + (x _ {2} - \bar {x}) ^ {2} + \dots .. + (x _ {n} - \bar {x}) ^ {2} = \underset {i = 1} {\overset {n} {\longrightarrow}} (x _ {i} - \bar {x}) ^ {2}.
$$

If this sum is zero, then each $(x_{i} - \overline{x})$ has to be zero. This implies that there is no dispersion at all as all observations are equal to the mean $\overline{x}$.

If $\sum_{i=1}^{n}(x_i - \bar{x})^2$ is small, this indicates that the observations $x_1, x_2, x_3, \ldots, x_n$ are close to the mean $\bar{x}$ and therefore, there is a lower degree of dispersion. On the contrary, if this sum is large, there is a higher degree of dispersion of the observations from the mean $\bar{x}$. Can we thus say that the sum $\sum_{i=1}^{n}(x_i - \bar{x})^2$ is a reasonable indicator of the degree of dispersion or scatter?

Let us take the set A of six observations 5, 15, 25, 35, 45, 55. The mean of the observations is $\overline{x} = 30$. The sum of squares of deviations from $\overline{x}$ for this set is

$$
\begin{array}{r l} \sum_ {i = 1} ^ {6} (x _ {i} - \bar {x}) ^ {2} & = (5 - 3 0) ^ {2} + (1 5 - 3 0) ^ {2} + (2 5 - 3 0) ^ {2} + (3 5 - 3 0) ^ {2} + (4 5 - 3 0) ^ {2} + (5 5 - 3 0) ^ {2} \\ & = 6 2 5 + 2 2 5 + 2 5 + 2 5 + 2 2 5 + 6 2 5 = 1 7 5 0 \end{array}
$$

Let us now take another set B of 31 observations 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45. The mean of these observations is $\bar{y} = 30$

Note that both the sets A and B of observations have a mean of 30.

Now, the sum of squares of deviations of observations for set B from the mean  $\bar{y}$  is given by

$$
\begin{array}{r l} \sum_ {i = 1} ^ {3 1} (y _ {i} - \bar {y}) ^ {2} & = (1 5 - 3 0) ^ {2} + (1 6 - 3 0) ^ {2} + (1 7 - 3 0) ^ {2} + \dots + (4 4 - 3 0) ^ {2} + (4 5 - 3 0) ^ {2} \\ & = (- 1 5) ^ {2} + (- 1 4) ^ {2} + \dots + (- 1) ^ {2} + 0 ^ {2} + 1 ^ {2} + 2 ^ {2} + 3 ^ {2} + \dots + 1 4 ^ {2} + 1 5 ^ {2} \\ & = 2 [ 1 5 ^ {2} + 1 4 ^ {2} + \dots + 1 ^ {2} ] \\ & = 2 \times \frac {1 5 \times (1 5 + 1) (3 0 + 1)}{6} = 5 \times 1 6 \times 3 1 = 2 4 8 0 \end{array}
$$

(Because sum of squares of first $n$ natural numbers $= \frac{n(n + 1)(2n + 1)}{6}$. Here $n = 15$)

Reprint 2025-26

<!-- page 17 of 32 -->

STATISTICS

273

If $\sum_{i=1}^{n}(x_i - \overline{x})^2$ is simply our measure of dispersion or scatter about mean, we

will tend to say that the set A of six observations has a lesser dispersion about the mean than the set B of 31 observations, even though the observations in set A are more scattered from the mean (the range of deviations being from -25 to 25) than in the set B (where the range of deviations is from -15 to 15).

This is also clear from the following diagrams.

For the set $A$, we have

![Image block](doc:a82387d/tier:standard/page:17/block:7)

Fig 13.5

For the set $\mathrm{B}$, we have

![Image block](doc:a82387d/tier:standard/page:17/block:10)

Fig 13.6

Thus, we can say that the sum of squares of deviations from the mean is not a proper measure of dispersion. To overcome this difficulty we take the mean of the squares of the deviations, i.e., we take $\frac{1}{n}\sum_{i=1}^{n}(x_i - \overline{x})^2$. In case of the set A, we have Mean $= \frac{1}{6} \times 1750 = 291.67$ and in case of the set B, it is $\frac{1}{31} \times 2480 = 80$.

This indicates that the scatter or dispersion is more in set A than the scatter or dispersion in set B, which confirms with the geometrical representation of the two sets.

Thus, we can take $\frac{1}{n}\sum (x_i - \bar{x})^2$ as a quantity which leads to a proper measure of dispersion. This number, i.e., mean of the squares of the deviations from mean is called the variance and is denoted by $\sigma^2$ (read as sigma square). Therefore, the variance of $n$ observations $x_1, x_2, \ldots, x_n$ is given by

Reprint 2025-26

<!-- page 18 of 32 -->

274

MATHEMATICS

$$
\sigma^ {2} = \frac {1}{n} \sum_ {i = 1} ^ {n} (x _ {i} - \bar {x}) ^ {2}
$$

13.5.1 Standard Deviation In the calculation of variance, we find that the units of individual observations $x_{i}$ and the unit of their mean $\overline{x}$ are different from that of variance, since variance involves the sum of squares of $(x_{i} - \overline{x})$. For this reason, the proper measure of dispersion about the mean of a set of observations is expressed as positive square-root of the variance and is called standard deviation. Therefore, the standard deviation, usually denoted by $\sigma$, is given by

$$
\sigma = \sqrt {\frac {1}{n} \sum_ {i = 1} ^ {n} (x _ {i} - \bar {x}) ^ {2}}\tag{... (1}
$$

Let us take the following example to illustrate the calculation of variance and hence, standard deviation of ungrouped data.

Example 8 Find the variance of the following data:

$$
6, 8, 1 0, 1 2, 1 4, 1 6, 1 8, 2 0, 2 2, 2 4
$$

Solution From the given data we can form the following Table 13.7. The mean is calculated by step-deviation method taking 14 as assumed mean. The number of observations is n = 10

Table 13.7

| $x_{i}$ | $d_{i} = \frac{x_{i} - 14}{2}$ | Deviations from mean$(x_{i} - \bar{x})$ | $(x_{i} - \bar{x})$ |
| --- | --- | --- | --- |
| 6 | -4 | -9 | 81 |
| 8 | -3 | -7 | 49 |
| 10 | -2 | -5 | 25 |
| 12 | -1 | -3 | 9 |
| 14 | 0 | -1 | 1 |
| 16 | 1 | 1 | 1 |
| 18 | 2 | 3 | 9 |
| 20 | 3 | 5 | 25 |
| 22 | 4 | 7 | 49 |
| 24 | 5 | 9 | 81 |
|  | 5 |  | 330 |

Reprint 2025-26

<!-- page 19 of 32 -->

STATISTICS

275

Therefore

$$
\text {Mean} \bar {x} = \text {assumed mean} + \frac {\sum_ {i = 1} ^ {n} d _ {i}}{n} \times h = 1 4 + \frac {5}{1 0} \times 2 = 1 5
$$

and Variance $(\sigma^2) = \frac{1}{n}\sum_{i=1}^{10}(x_i - \overline{x})^2 = \frac{1}{10}\times 330 = 33$

Thus Standard deviation $(\sigma) = \sqrt{33} = 5.74$

13.5.2 Standard deviation of a discrete frequency distribution Let the given discrete frequency distribution be

$$
\left| \begin{array}{c c c c c} x: & x _ {1}, & x _ {2}, & x _ {3}, \dots , x _ {n} \\ & f: & f _ {1}, & f _ {2}, & f _ {3}, \dots , f _ {n} \end{array} \right|
$$

In this case standard deviation $(\sigma) = \sqrt{\frac{1}{N}\sum_{i=1}^{n}f_{i}(x_{i} - \bar{x})^{2}}$

(2)

where $\mathrm{N} = \sum_{i=1}^{n} f_i$.

Let us take up following example.

Example 9 Find the variance and standard deviation for the following data:

| $x_{i}$ | 4 | 8 | 11 | 17 | 20 | 24 | 32 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| $f_{i}$ | 3 | 5 | 9 | 5 | 4 | 3 | 1 |

Solution Presenting the data in tabular form (Table 13.8), we get

Table 13.8

| $x_{i}$ | $f_{i}$ | $f_{i}x_{i}$ | $x_{i}-\bar{x}$ | $(x_{i}-\bar{x})^{2}$ | $f_{i}(x_{i}-\bar{x})^{2}$ |
| --- | --- | --- | --- | --- | --- |
| 4 | 3 | 12 | -10 | 100 | 300 |
| 8 | 5 | 40 | -6 | 36 | 180 |
| 11 | 9 | 99 | -3 | 9 | 81 |
| 17 | 5 | 85 | 3 | 9 | 45 |
| 20 | 4 | 80 | 6 | 36 | 144 |
| 24 | 3 | 72 | 10 | 100 | 300 |
| 32 | 1 | 32 | 18 | 324 | 324 |
|  | 30 | 420 |  |  | 1374 |

Reprint 2025-26

<!-- page 20 of 32 -->

276

MATHEMATICS

$$
\mathrm{N} = 3 0, \sum_ {i = 1} ^ {7} f _ {i} x _ {i} = 4 2 0, \sum_ {i = 1} ^ {7} f _ {i} \left(x _ {i} - \bar {x}\right) ^ {2} = 1 3 7 4
$$

Therefore

$$
\overline {{x}} = \frac {\sum_ {i = 1} ^ {7} f _ {i} x _ {i}}{\mathrm{N}} = \frac {1}{3 0} \times 4 2 0 = 1 4
$$

Hence

$$
\begin{array}{r l} \text {variance} (\sigma^ {2}) & = \frac {1}{N} \sum_ {i = 1} ^ {7} f _ {i} (x _ {i} - \overline {{x}}) ^ {2} \\ & = \frac {1}{3 0} \times 1 3 7 4 = 4 5. 8 \end{array}
$$

and

Standard deviation $(\sigma) = \sqrt{45.8} = 6.77$

13.5.3 Standard deviation of a continuous frequency distribution The given continuous frequency distribution can be represented as a discrete frequency distribution by replacing each class by its mid-point. Then, the standard deviation is calculated by the technique adopted in the case of a discrete frequency distribution.

If there is a frequency distribution of $n$ classes each class defined by its mid-point $x_{i}$ with frequency $f_{i}$, the standard deviation will be obtained by the formula

$$
\sigma = \sqrt {\frac {1}{N} \sum_ {i = 1} ^ {n} f _ {i} (x _ {i} - \overline {{x}}) ^ {2}},
$$

where  $\bar{x}$  is the mean of the distribution and  $N = \sum_{i=1}^{n} f_{i}$ .

Another formula for standard deviation We know that

Variance

$$
\begin{array}{l} \text {e} (\sigma^ {2}) = \frac {1}{N} \sum_ {i = 1} ^ {n} f _ {i} (x _ {i} - \bar {x}) ^ {2} = \frac {1}{N} \sum_ {i = 1} ^ {n} f _ {i} (x _ {i} ^ {2} + \bar {x} ^ {2} - 2 \bar {x} x _ {i}) \\ = \frac {1}{N} \left[ \sum_ {i = 1} ^ {n} f _ {i} x _ {i} ^ {2} + \sum_ {i = 1} ^ {n} \bar {x} ^ {2} f _ {i} - \sum_ {i = 1} ^ {n} 2 \bar {x} f _ {i} x _ {i} \right] \\ = \frac {1}{N} \left[ \sum_ {i = 1} ^ {n} f _ {i} x _ {i} ^ {2} + \bar {x} ^ {2} \sum_ {i = 1} ^ {n} f _ {i} - 2 \bar {x} \sum_ {i = 1} ^ {n} x _ {i} f _ {i} \right] \end{array}
$$

Reprint 2025-26

<!-- page 21 of 32 -->

... (3)

STATISTICS

277

$$
\begin{array}{l} = \frac {1}{\mathrm{N}} \int_ {i = 1} ^ {n} f _ {i} x _ {i} ^ {2} + \bar {x} ^ {2} \mathrm{N} - 2 \bar {x}. \mathrm{N} \bar {x} \quad \left[ \text {Here} \frac {1}{\mathrm{N}} \sum_ {i = 1} ^ {n} x _ {i} f _ {i} = \bar {x} \text {or} \sum_ {i = 1} ^ {n} x _ {i} f _ {i} = \mathrm{N} \bar {x} \right] \\ = \frac {1}{\mathrm{N}} \quad \sum_ {i = 1} ^ {n} f _ {i} x _ {i} ^ {2} + \bar {x} ^ {2} - 2 \bar {x} ^ {2} = \frac {1}{\mathrm{N}} \quad \sum_ {i = 1} ^ {n} f _ {i} x _ {i} ^ {2} - \bar {x} ^ {2} \end{array}
$$

or

$$
\sigma^ {2} = \frac {1}{\mathrm{N}} \sum_ {i - 1} ^ {n} f _ {i} x _ {i} ^ {2} - \left(\frac {\sum_ {i = 1} ^ {n} f _ {i} x _ {i}}{\mathrm{N}}\right) ^ {2} = \frac {1}{\mathrm{N} ^ {2}} \left[ \mathrm{N} \sum_ {i = 1} ^ {n} f _ {i} x _ {i} ^ {2} - \left(\sum_ {i = 1} ^ {n} f _ {i} x _ {i}\right) ^ {2} \right]
$$

Thus, standard deviation $(\sigma) = \frac{1}{N}\sqrt{N\sum_{i=1}^{n}f_{i}x_{i}^{2}-\left(\sum_{i=1}^{n}f_{i}x_{i}\right)^{2}}$

Example 10 Calculate the mean, variance and standard deviation for the following distribution :

| Class | 30-40 | 40-50 | 50-60 | 60-70 | 70-80 | 80-90 | 90-100 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Frequency | 3 | 7 | 12 | 15 | 8 | 3 | 2 |

Solution From the given data, we construct the following Table 13.9.

Table 13.9

| Class | Frequency$(f_i)$ | Mid-point$(x_i)$ | $f_i x_i$ | $(x_i - \bar{x})^2$ | $f_i (x_i - \bar{x})^2$ |
| --- | --- | --- | --- | --- | --- |
| 30-40 | 3 | 35 | 105 | 729 | 2187 |
| 40-50 | 7 | 45 | 315 | 289 | 2023 |
| 50-60 | 12 | 55 | 660 | 49 | 588 |
| 60-70 | 15 | 65 | 975 | 9 | 135 |
| 70-80 | 8 | 75 | 600 | 169 | 1352 |
| 80-90 | 3 | 85 | 255 | 529 | 1587 |
| 90-100 | 2 | 95 | 190 | 1089 | 2178 |
|  | 50 |  | 3100 |  | 10050 |

Reprint 2025-26

<!-- page 22 of 32 -->

278

MATHEMATICS

Thus

Mean

$$
\overline {{x}} = \frac {1}{\mathrm{N}} \sum_ {i = 1} ^ {7} f _ {i} x _ {i} = \frac {3 1 0 0}{5 0} = 6 2
$$

$$
\begin{array}{r l} \text {Variance} \left(\sigma^ {2}\right) & = \frac {1}{N} \sum_ {i = 1} ^ {7} f _ {i} (x _ {i} - \bar {x}) ^ {2} \\ & = \frac {1}{5 0} \times 1 0 0 5 0 = 2 0 1 \end{array}
$$

and Standard deviation ( $\sigma$ ) =  $\sqrt{201}$  = 14.18

Example 11 Find the standard deviation for the following data :

| $x_{i}$ | 3 | 8 | 13 | 18 | 23 |
| --- | --- | --- | --- | --- | --- |
| $f_{i}$ | 7 | 10 | 15 | 10 | 6 |

Solution Let us form the following Table 13,10:

Table 13.10

| $x_{i}$ | $f_{i}$ | $f_{i}x_{i}$ | $x_{i}^{2}$ | $f_{i}x_{i}^{2}$ |
| --- | --- | --- | --- | --- |
| 3 | 7 | 21 | 9 | 63 |
| 8 | 10 | 80 | 64 | 640 |
| 13 | 15 | 195 | 169 | 2535 |
| 18 | 10 | 180 | 324 | 3240 |
| 23 | 6 | 138 | 529 | 3174 |
|  | 48 | 614 |  | 9652 |

Now, by formula (3), we have

$$
\begin{array}{r l} \sigma & = \frac {1}{N} \sqrt {N \sum f _ {i} x _ {i} ^ {2} - \left(\sum f _ {i} x _ {i}\right) ^ {2}} \\ & = \frac {1}{4 8} \sqrt {4 8 \times 9 6 5 2 - (6 1 4) ^ {2}} \\ & = \frac {1}{4 8} \sqrt {4 6 3 2 9 6 - 3 7 6 9 9 6} \end{array}
$$

Reprint 2025-26

<!-- page 23 of 32 -->

STATISTICS

279

$$
= \frac {1}{4 8} \times 2 9 3. 7 7 = 6. 1 2
$$

Therefore, Standard deviation $(\sigma) = 6.12$

13.5.4. Shortcut method to find variance and standard deviation Sometimes the values of  $x_{i}$  in a discrete distribution or the mid points  $x_{i}$  of different classes in a continuous distribution are large and so the calculation of mean and variance becomes tedious and time consuming. By using step-deviation method, it is possible to simplify the procedure.

Let the assumed mean be ‘A’ and the scale be reduced to  $\frac{1}{h}$  times (h being the width of class-intervals). Let the step-deviations or the new values be  $y_{i}$ .

i.e.

$$
y _ {i} = \frac {x _ {i} - \mathrm{A}}{h} \text {or} x _ {i} = \mathrm{A} + h y _ {i}\tag{1}
$$

We know that

$$
\overline {{x}} = \frac {\sum_ {i = 1} ^ {n} f _ {i} x _ {i}}{\mathrm{N}}\tag{... (2}
$$

Replacing $x_{i}$ from (1) in (2), we get

$$
\begin{array}{l} \overline {{x}} = \frac {\sum_ {i = 1} ^ {n} f _ {i} (\mathrm{A} + h y _ {i})}{\mathrm{N}} \\ = \frac {1}{\mathrm{N}} \left(\sum_ {i = 1} ^ {n} f _ {i} \mathrm{A} + \sum_ {i = 1} ^ {n} h f _ {i} y _ {i}\right) = \frac {1}{\mathrm{N}} \left(\mathrm{A} \sum_ {i = 1} ^ {n} f _ {i} + h \sum_ {i = 1} ^ {n} f _ {i} y _ {i}\right) \\ = \mathrm{A}. \frac {\mathrm{N}}{\mathrm{N}} + h \frac {\sum_ {i = 1} ^ {n} f _ {i} y _ {i}}{\mathrm{N}} \end{array}\quad \left(\text {because} \sum_ {i = 1} ^ {n} f _ {i} = \mathrm{N}\right)
$$

Thus

$$
\bar {x} = \mathrm{A} + h \bar {y}\tag{... (3}
$$

Now

$$
\sigma_ {x} ^ {2} = \frac {1}{\mathrm{N}} \sum_ {i = 1} ^ {n} f _ {i} (x _ {i} - \bar {x}) ^ {2}
$$

$$
= \frac {1}{\mathrm{N}} \sum_ {i = 1} ^ {n} f _ {i} \left(\mathrm{A} + h y _ {i} - \mathrm{A} - h \bar {y}\right) ^ {2}
$$

(Using (1) and (3))

Reprint 2025-26

<!-- page 24 of 32 -->

... (4)

280

MATHEMATICS

$$
\begin{array}{l} = \frac {1}{\mathrm{N}} \sum_ {i = 1} ^ {n} f _ {i} h ^ {2} (y _ {i} - \bar {y}) ^ {2} \\ = \frac {h ^ {2}}{\mathrm{N}} \sum_ {i = 1} ^ {n} f _ {i} (y _ {i} - \bar {y}) ^ {2} = h ^ {2} \times \text {variance of the variable} y _ {i} \end{array}
$$

i.e.

$$
\sigma_ {x} ^ {2} = h ^ {2} \sigma_ {y} ^ {2}
$$

or

$$
\sigma_ {x} = h \sigma_ {y}
$$

From (3) and (4), we have

$$
\sigma_ {x} = \frac {h}{N} \sqrt {N \sum_ {i = 1} ^ {n} f _ {i} y _ {i} ^ {2} - \left(\sum_ {i = 1} ^ {n} f _ {i} y _ {i}\right) ^ {2}}\tag{5}
$$

Let us solve Example 11 by the short-cut method and using formula (5)

Examples 12 Calculate mean, variance and standard deviation for the following distribution.

| Classes | 30-40 | 40-50 | 50-60 | 60-70 | 70-80 | 80-90 | 90-100 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Frequency | 3 | 7 | 12 | 15 | 8 | 3 | 2 |

Solution Let the assumed mean $\mathrm{A} = 65$. Here $h = 10$

We obtain the following Table 13.11 from the given data :

Table 13.11

| Class | Frequency | Mid-point | $y_i = \frac{x_i - 65}{10}$ | $y_i^2$ | $f_i y_i$ | $f_i y_i^2$ |
| --- | --- | --- | --- | --- | --- | --- |
|  | $f_i$ | $x_i$ |  |  |  |  |
| 30-40 | 3 | 35 | -3 | 9 | -9 | 27 |
| 40-50 | 7 | 45 | -2 | 4 | -14 | 28 |
| 50-60 | 12 | 55 | -1 | 1 | -12 | 12 |
| 60-70 | 15 | 65 | 0 | 0 | 0 | 0 |
| 70-80 | 8 | 75 | 1 | 1 | 8 | 8 |
| 80-90 | 3 | 85 | 2 | 4 | 6 | 12 |
| 90-100 | 2 | 95 | 3 | 9 | 6 | 18 |
|  | N=50 |  |  |  | -15 | 105 |

Reprint 2025-26

<!-- page 25 of 32 -->

STATISTICS

281

Therefore

$$
\overline {{x}} = \mathrm{A} + \frac {\sum f _ {i} y _ {i}}{5 0} \times h = 6 5 - \frac {1 5}{5 0} \times 1 0 = 6 2
$$

Variance

$$
\begin{array}{r l} \sigma^ {2} & = \frac {h ^ {2}}{\mathrm{N} ^ {2}} \left[ \mathrm{N} \Sigma f _ {i} y _ {i} ^ {2} - \left(\Sigma f _ {i} y _ {i}\right) ^ {2} \right] \\ & = \frac {(1 0) ^ {2}}{(5 0) ^ {2}} \left[ 5 0 \times 1 0 5 - (- 1 5) ^ {2} \right] \\ & = \frac {1}{2 5} [ 5 2 5 0 - 2 2 5 ] = 2 0 1 \end{array}
$$

and standard deviation $(\sigma) = \sqrt{201} = 14.18$

## EXERCISE 13.2

Find the mean and variance for each of the data in Exercies 1 to 5.

1. 6,7,10,12,13,4,8,12

2. First $n$ natural numbers

3. First 10 multiples of 3

4.

| $x_{i}$ | 6 | 10 | 14 | 18 | 24 | 28 | 30 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| $f_{i}$ | 2 | 4 | 7 | 12 | 8 | 4 | 3 |

| $x_{i}$ | 92 | 93 | 97 | 98 | 102 | 104 | 109 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| $f_{i}$ | 3 | 2 | 3 | 2 | 6 | 3 | 3 |

6. Find the mean and standard deviation using short-cut method.

| $x_{i}$ | 60 | 61 | 62 | 63 | 64 | 65 | 66 | 67 | 68 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $f_{i}$ | 2 | 1 | 12 | 29 | 25 | 12 | 10 | 4 | 5 |

Find the mean and variance for the following frequency distributions in Exercises 7 and 8.

7.

| Classes | 0-30 | 30-60 | 60-90 | 90-120 | 120-150 | 150-180 | 180-210 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Frequencies | 2 | 3 | 5 | 10 | 3 | 5 | 2 |

Reprint 2025-26

<!-- page 26 of 32 -->

282

MATHEMATICS

8.

| Classes | 0-10 | 10-20 | 20-30 | 30-40 | 40-50 |
| --- | --- | --- | --- | --- | --- |
| Frequencies | 5 | 8 | 15 | 16 | 6 |

9. Find the mean, variance and standard deviation using short-cut method

| Height in cms | 70-75 | 75-80 | 80-85 | 85-90 | 90-95 | 95-100 | 100-105 | 105-110 | 110-115 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| No. of children | 3 | 4 | 7 | 7 | 15 | 9 | 6 | 6 | 3 |

10. The diameters of circles (in mm) drawn in a design are given below:

| Diameters | 33-36 | 37-40 | 41-44 | 45-48 | 49-52 |
| --- | --- | --- | --- | --- | --- |
| No. of circles | 15 | 17 | 21 | 22 | 25 |

Calculate the standard deviation and mean diameter of the circles.

[ Hint First make the data continuous by making the classes as 32.5-36.5, 36.5-40.5, 40.5-44.5, 44.5 - 48.5, 48.5 - 52.5 and then proceed.]

## Miscellaneous Examples

Example 13 The variance of 20 observations is 5. If each observation is multiplied by 2, find the new variance of the resulting observations.

Solution Let the observations be $x_{1}, x_{2}, \ldots, x_{20}$ and $\overline{x}$ be their mean. Given that variance = 5 and $n = 20$. We know that

$$
\text {Variance} \left(\sigma^ {2}\right) = \frac {1}{n} \sum_ {i = 1} ^ {2 0} (x _ {i} - \bar {x}) ^ {2}, \text {i.e.,} 5 = \frac {1}{2 0} \sum_ {i = 1} ^ {2 0} (x _ {i} - \bar {x}) ^ {2}
$$

or

$$
\left. \sum_ {i = 1} ^ {2 0} \left(x _ {i} - \bar {x}\right) ^ {2} = 1 0 0 \right|
$$

If each observation is multiplied by 2, and the new resulting observations are $y_{i}$, then

$$
y _ {\mathrm{i}} = 2 x _ {\mathrm{i}} \text {i.e.,} x _ {\mathrm{i}} = \frac {1}{2} y _ {i}
$$

Reprint 2025-26

<!-- page 27 of 32 -->

STATISTICS

283

Therefore

$$
\overline {{y}} = \frac {1}{n} \sum_ {i = 1} ^ {2 0} y _ {i} = \frac {1}{2 0} \sum_ {i = 1} ^ {2 0} 2 x _ {i} = 2. \frac {1}{2 0} \sum_ {i = 1} ^ {2 0} x _ {i}
$$

i.e.

$$
\left| \begin{array}{l l} \bar {y} = 2 \bar {x} & \text {or} \quad \bar {x} = \frac {1}{2} \bar {y} \end{array} \right|
$$

Substituting the values of $x_{i}$ and $\overline{x}$ in (1), we get

$$
\sum_ {i = 1} ^ {2 0} \left(\frac {1}{2} y _ {i} - \frac {1}{2} \bar {y}\right) ^ {2} = 1 0 0, \text {i.e.,} \sum_ {i = 1} ^ {2 0} (y _ {i} - \bar {y}) ^ {2} = 4 0 0
$$

Thus the variance of new observations $= \frac{1}{20} \times 400 = 20 = 2^2 \times 5$

Note The reader may note that if each observation is multiplied by a constant $k$, the variance of the resulting observations becomes $k^2$ times the original variance.

Example14 The mean of 5 observations is 4.4 and their variance is 8.24. If three of the observations are 1, 2 and 6, find the other two observations.

Solution Let the other two observations be $x$ and $y$.

Therefore, the series is 1, 2, 6, x, y.

Now

$$
\text {Mean} \bar {x} = 4. 4 = \frac {1 + 2 + 6 + x + y}{5}
$$

or

$$
2 2 = 9 + x + y
$$

Therefore

$$
x + y = 1 3\tag{... (1}
$$

Also

$$
\text {variance} = 8. 2 4 = \frac {1}{n} \sum_ {i = 1} ^ {5} \left(x _ {i} - \bar {x}\right) ^ {2}
$$

$$
\text {i.e.} 8. 2 4 = \frac {1}{5} \left[ (3. 4) ^ {2} + (2. 4) ^ {2} + (1. 6) ^ {2} + x ^ {2} + y ^ {2} - 2 \times 4. 4 (x + y) + 2 \times (4. 4) ^ {2} \right]
$$

$$
\text {or} 4 1. 2 0 = 1 1. 5 6 + 5. 7 6 + 2. 5 6 + x ^ {2} + y ^ {2} - 8. 8 \times 1 3 + 3 8. 7 2
$$

Therefore

$$
x ^ {2} + y ^ {2} = 9 7\tag{... (2}
$$

But from (1), we have

$$
x ^ {2} + y ^ {2} + 2 x y = 1 6 9\tag{... (3}
$$

From (2) and (3), we have

$$
2 x y = 7 2\tag{... (4}
$$

Subtracting (4) from (2), we get

Reprint 2025-26

<!-- page 28 of 32 -->

284

MATHEMATICS

or

$$
\begin{array}{l} x ^ {2} + y ^ {2} - 2 x y = 9 7 - 7 2 \text {i.e.} (x - y) ^ {2} = 2 5 \\ x - y = \pm 5 \end{array}\tag{... (5}
$$

So, from (1) and (5), we get

$$
x = 9, y = 4 \text {when} x - y = 5
$$

$$
x = 4, y = 9 \text {when} x - y = - 5
$$

Thus, the remaining observations are 4 and 9.

Example 15 If each of the observation $x_{1}, x_{2}, \ldots, x_{n}$ is increased by 'a', where $a$ is a negative or positive number, show that the variance remains unchanged.

Solution Let $\overline{x}$ be the mean of $x_{1}, x_{2}, \ldots, x_{n}$. Then the variance is given by

$$
\sigma_ {1} ^ {2} = \frac {1}{n} \sum_ {i = 1} ^ {n} (x _ {i} - \bar {x}) ^ {2}
$$

If 'a is added to each observation, the new observations will be

$$
y _ {i} = x _ {\mathrm{i}} + a\tag{... (1}
$$

Let the mean of the new observations be $\bar{y}$. Then

$$
\begin{array}{r l} \overline {{y}} & = \frac {1}{n} \sum_ {i = 1} ^ {n} y _ {i} = \frac {1}{n} \sum_ {i = 1} ^ {n} (x _ {i} + a) \\ & = \frac {1}{n} \left[ \sum_ {i = 1} ^ {n} x _ {i} + \sum_ {i = 1} ^ {n} a \right] = \frac {1}{n} \sum_ {i = 1} ^ {n} x _ {i} + \frac {n a}{n} = \overline {{x}} + a \end{array}
$$

i.e.

$$
\bar {y} = \bar {x} + a\tag{... (2}
$$

Thus, the variance of the new observations

$$
\begin{array}{r l} \sigma_ {2} ^ {2} & = \frac {1}{n} \sum_ {i = 1} ^ {n} (y _ {i} - \bar {y}) ^ {2} = \frac {1}{n} \sum_ {i = 1} ^ {n} (x _ {i} + a - \bar {x} - a) ^ {2} \\ & = \frac {1}{n} \sum_ {i = 1} ^ {n} (x _ {i} - \bar {x}) ^ {2} = \sigma_ {1} ^ {2} \end{array}
$$

[Using (1) and (2)]

Thus, the variance of the new observations is same as that of the original observations.

Note We may note that adding (or subtracting) a positive number to (or from) each observation of a group does not affect the variance.

Example 16 The mean and standard deviation of 100 observations were calculated as 40 and 5.1, respectively by a student who took by mistake 50 instead of 40 for one observation. What are the correct mean and standard deviation?

Reprint 2025-26

<!-- page 29 of 32 -->

STATISTICS

285

Solution Given that number of observations $(n) = 100$

Incorrect mean $(\overline{x}) = 40,$

Incorrect standard deviation $(\sigma) = 5.1$

We know that $\bar{x} = \frac{1}{n}\sum_{i = 1}^{n}x_{i}$

i.e.

$$
\left| 4 0 = \frac {1}{1 0 0} \sum_ {i = 1} ^ {1 0 0} x _ {i} \quad \text {or} \quad \sum_ {i = 1} ^ {1 0 0} x _ {i} = 4 0 0 0 \right|
$$

i.e. Incorrect sum of observations $= 4000$

Thus the correct sum of observations = Incorrect sum - 50 + 40
= 4000 - 50 + 40 = 3990

Hence

$$
\text {Correct mean} = \frac {\text {correct sum}}{1 0 0} = \frac {3 9 9 0}{1 0 0} = 3 9. 9
$$

Also

Standard deviation $\sigma$

$$
= \sqrt {\frac {1}{n} \sum_ {i = 1} ^ {n} x _ {i} ^ {2} - \frac {1}{n ^ {2}} \left(\sum_ {i = 1} ^ {n} x _ {i}\right) ^ {2}}
$$

$$
= \sqrt {\frac {1}{n} \sum_ {i = 1} ^ {n} x _ {i} ^ {2} - (\bar {x}) ^ {2}}
$$

i.e.

$$
5. 1 = \sqrt {\frac {1}{1 0 0} \times \text {Incorrect} \sum_ {i = 1} ^ {n} x _ {i} ^ {2} - (4 0) ^ {2}}
$$

or

$$
2 6. 0 1 = \frac {1}{1 0 0} \times \text {Incorrect} \sum_ {i = 1} ^ {n} x _ {i} ^ {2} - 1 6 0 0
$$

Therefore

$$
\text {Incorrect} \sum_ {i = 1} ^ {n} x _ {i} ^ {2} = 1 0 0 (2 6. 0 1 + 1 6 0 0) = 1 6 2 6 0 1
$$

Now

$$
\begin{array}{r l} \text {Correct} & \sum_ {i = 1} ^ {n} x _ {i} ^ {2} = \text {Incorrect} \sum_ {i = 1} ^ {n} x _ {i} ^ {2} - (5 0) ^ {2} + (4 0) ^ {2} \\ & = 1 6 2 6 0 1 - 2 5 0 0 + 1 6 0 0 = 1 6 1 7 0 1 \end{array}
$$

Therefore Correct standard deviation

Reprint 2025-26

<!-- page 30 of 32 -->

286

MATHEMATICS

$$
\begin{array}{l} = \sqrt {\frac {\text {Correct} \sum x _ {i} ^ {2}}{n} - (\text {Correct mean}) ^ {2}} \\ = \sqrt {\frac {1 6 1 7 0 1}{1 0 0} - (3 9 . 9) ^ {2}} \\ = \sqrt {1 6 1 7 . 0 1 - 1 5 9 2 . 0 1} = \sqrt {2 5} = 5 \end{array}
$$

## Miscellaneous Exercise On Chapter 13

1. The mean and variance of eight observations are 9 and 9.25, respectively. If six of the observations are 6, 7, 10, 12, 12 and 13, find the remaining two observations.

2. The mean and variance of 7 observations are 8 and 16, respectively. If five of the observations are 2, 4, 10, 12, 14. Find the remaining two observations.

3. The mean and standard deviation of six observations are 8 and 4, respectively. If each observation is multiplied by 3, find the new mean and new standard deviation of the resulting observations.

4. Given that $\overline{x}$ is the mean and $\sigma^2$ is the variance of $n$ observations $x_1, x_2, \ldots, x_n$. Prove that the mean and variance of the observations $ax_1, ax_2, ax_3, \ldots, ax_n$ are $a\overline{x}$ and $a^2\sigma^2$, respectively, ($a \neq 0$).

5. The mean and standard deviation of 20 observations are found to be 10 and 2, respectively. On rechecking, it was found that an observation 8 was incorrect. Calculate the correct mean and standard deviation in each of the following cases: (i) If wrong item is omitted. (ii) If it is replaced by 12.

6. The mean and standard deviation of a group of 100 observations were found to be 20 and 3, respectively. Later on it was found that three observations were incorrect, which were recorded as 21, 21 and 18. Find the mean and standard deviation if the incorrect observations are omitted.

## Summary

\- Measures of dispersion Range, Quartile deviation, mean deviation, variance, standard deviation are measures of dispersion.

Range = Maximum Value - Minimum Value

◆ Mean deviation for ungrouped data

$$
\text {M.D.} (\bar {x}) = \frac {\sum \left| x _ {i} - \bar {x} \right|}{n}, \quad \text {M.D. (M)} = \frac {\sum \left| x _ {i} - \mathrm{M} \right|}{n}\left. \right\}
$$

Reprint 2025-26

<!-- page 31 of 32 -->

STATISTICS

287

Mean deviation for grouped data

$$
\text {M.D.} (\bar {x}) = \frac {\sum f _ {i} \left| x _ {i} \quad \bar {x} \right|}{\mathrm{N}}, \quad \text {M.D.} (\mathrm{M}) = \frac {\sum f _ {i} \left| x _ {i} \quad \mathrm{M} \right|}{\mathrm{N}}, \text {where} \mathrm{N} = \sum f _ {i}
$$

$\diamond$ Variance and standard deviation for ungrouped data

$$
\sigma^ {2} = \frac {1}{n} \sum \left(x _ {i} - \bar {x}\right) ^ {2}, \quad \sigma = \sqrt {\frac {1}{n} \sum \left(x _ {i} - \bar {x}\right) ^ {2}}
$$

\- Variance and standard deviation of a discrete frequency distribution

$$
\sigma^ {2} = \frac {1}{\mathrm{N}} \sum f _ {i} \left(x _ {i} - \bar {x}\right) ^ {2}, \quad \sigma = \sqrt {\frac {1}{\mathrm{N}} \sum f _ {i} \left(x _ {i} - \bar {x}\right) ^ {2}}
$$

\- Variance and standard deviation of a continuous frequency distribution

$$
\sigma^ {2} = \frac {1}{\mathrm{N}} \sum f _ {i} \left(x _ {i} - \bar {x}\right) ^ {2}, \quad \sigma = \frac {1}{\mathrm{N}} \sqrt {\mathrm{N} \sum f _ {i} x _ {i} ^ {2} - \left(\sum f _ {i} x _ {i}\right) ^ {2}}
$$

◆ Shortcut method to find variance and standard deviation.

$$
\sigma^ {2} = \frac {h ^ {2}}{\mathrm{N} ^ {2}} \left[ \mathrm{N} \sum f _ {i} y _ {i} ^ {2} - \left(\sum f _ {i} y _ {i}\right) ^ {2} \right], \sigma = \frac {h}{\mathrm{N}} \sqrt {\mathrm{N} \sum f _ {i} y _ {i} ^ {2} - \left(\sum f _ {i} y _ {i}\right) ^ {2}},
$$

where  $y_{i} = \frac{x_{i} - A}{h}$

## Historical Note

‘Statistics’ is derived from the Latin word ‘status’ which means a political state. This suggests that statistics is as old as human civilisation. In the year 3050 B.C., perhaps the first census was held in Egypt. In India also, about 2000 years ago, we had an efficient system of collecting administrative statistics, particularly, during the regime of Chandra Gupta Maurya (324-300 B.C.). The system of collecting data related to births and deaths is mentioned in Kautilya’s Arthshastra (around 300 B.C.) A detailed account of administrative surveys conducted during Akbar’s regime is given in Ain-I-Akbari written by Abul Fazl.

Captain John Graunt of London (1620-1674) is known as father of vital statistics due to his studies on statistics of births and deaths. Jacob Bernoulli (1654-1705) stated the Law of Large numbers in his book “Ars Conjectandi”, published in 1713.

Reprint 2025-26

<!-- page 32 of 32 -->

288

MATHEMATICS

The theoretical development of statistics came during the mid seventeenth century and continued after that with the introduction of theory of games and chance (i.e., probability). Francis Galton (1822-1921), an Englishman, pioneered the use of statistical methods, in the field of Biometry. Karl Pearson (1857-1936) contributed a lot to the development of statistical studies with his discovery of Chi square test and foundation of statistical laboratory in England (1911). Sir Ronald A. Fisher (1890-1962), known as the Father of modern statistics, applied it to various diversified fields such as Genetics, Biometry, Education, Agriculture, etc.

Reprint 2025-26