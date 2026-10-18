---
{
  "concept": "Mean of Grouped Data",
  "slug": "mean-of-grouped-data",
  "grade": 10,
  "language": "en",
  "subject": "maths",
  "area": "Statistics",
  "model": "sarvam-105b",
  "settings": {
    "temperature": 0.3,
    "max_tokens": 8000,
    "reasoning_effort": "none"
  },
  "usage": {
    "completion_tokens": 3062,
    "prompt_tokens": 6999,
    "total_tokens": 10061,
    "completion_tokens_details": {
      "accepted_prediction_tokens": null,
      "audio_tokens": null,
      "reasoning_tokens": 0,
      "rejected_prediction_tokens": null
    },
    "prompt_tokens_details": null
  },
  "target_words": [
    1000,
    1350
  ],
  "generated_at": "2026-10-18T00:58:44",
  "source_grade": 10,
  "grade_delta": 0,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g10_maths_chapter13_011",
      "chapter": "chapter13",
      "section": "13.2 Mean of Grouped Data"
    },
    {
      "ref": "S2",
      "passage_id": "g10_maths_chapter13_001",
      "chapter": "chapter13",
      "section": "13.1 Introduction"
    }
  ],
  "citation_check": {
    "cited": [],
    "invented_citations": [],
    "unused_sources": [
      "1",
      "2"
    ],
    "explanatory_paragraphs_without_a_citation": 11,
    "words": 1734,
    "target_words": [
      1000,
      1350
    ],
    "untraceable_sections": 3,
    "ok": false,
    "structural_problems": []
  },
  "terms": [
    "class mark",
    "class interval",
    "assumed mean",
    "step-deviation",
    "direct method",
    "grouped data",
    "frequency",
    "deviation"
  ]
}
---

# Mean of Grouped Data

In your previous classes, you learned how to calculate the mean of ungrouped data by adding all the values and dividing by the total number of observations. However, in real-life situations, data is often so large that it needs to be condensed into grouped data, such as class intervals. To find the mean of grouped data, we cannot use the exact individual values. Instead, we use a representative value for each class interval, which is the class mark. The mean of grouped data is an approximate value, calculated by assuming that the frequencies of each class interval are centered around its class mark.

## The Direct Method

To find the mean of grouped data, we first need to determine the class mark for each class interval. The class mark, or mid-point, is found by taking the average of the upper and lower limits of the class interval.

$$ \text{Class mark} = \frac {\text{Upper class limit} + \text{Lower class limit}}{2} $$

Once we have the class marks, we can use the same formula as for ungrouped data, where the class mark serves as the observation $x_i$ and the frequency of the class serves as $f_i$.

$$ \bar{x} = \frac{\Sigma f_{i} x_{i}}{\Sigma f_{i}} $$

For example, consider the following grouped frequency distribution table of marks obtained by 30 students:

| Class interval | Number of students ($f_i$) | Class mark ($x_i$) | $f_i x_i$ |
| --- | --- | --- | --- |
| 10 - 25 | 2 | 17.5 | 35.0 |
| 25 - 40 | 3 | 32.5 | 97.5 |
| 40 - 55 | 7 | 47.5 | 332.5 |
| 55 - 70 | 6 | 62.5 | 375.0 |
| 70 - 85 | 6 | 77.5 | 465.0 |
| 85 - 100 | 6 | 92.5 | 555.0 |
| Total | $\Sigma f_i = 30$ |  | $\Sigma f_i x_i = 1860.0$ |

The sum of the values in the last column gives us $\Sigma f_{i}x_{i}$. So, the mean $\overline{x}$ of the given data is given by

$$ \overline {{x}} = \frac {\Sigma f _ {i} x _ {i}}{\Sigma f _ {i}} = \frac {1860.0}{30} = 62 $$

This new method of finding the mean is known as the Direct Method.

## The Assumed Mean Method

Sometimes, when the numerical values of $x_{i}$ and $f_{i}$ are large, finding the product of $x_{i}$ and $f_{i}$ becomes tedious and time-consuming. To simplify the calculations, we can use the Assumed Mean Method.

The first step is to choose one of the $x_{i}$'s as the assumed mean, and denote it by 'a'. To further reduce our calculation work, we may take 'a' to be that $x_{i}$ which lies in the centre of $x_{1}, x_{2}, \ldots, x_{n}$.

The next step is to find the difference $d_{i}$ between $a$ and each of the $x_{i}$'s, that is, the deviation of 'a' from each of the $x_{i}$'s.

$$ d _ {i} = x _ {i} - a $$

The third step is to find the product of $d_{i}$ with the corresponding $f_{i}$, and take the sum of all the $f_{i}d_{i}$'s.

The relation between the mean of the deviations, $\bar{d}$, and the mean, $\overline{x}$, is given by:

$$ \overline {{x}} = a + \overline {{d}} $$

i.e.,

$$ \overline {{x}} = a + \frac {\Sigma f _ {i} d _ {i}}{\Sigma f _ {i}} $$

For example, let us take $a = 47.5$ for the table above. The calculations are shown in the following table:

| Class interval | Number of students ($f_i$) | Class mark ($x_i$) | $d_i = x_i - 47.5$ | $f_i d_i$ |
| --- | --- | --- | --- | --- |
| 10 - 25 | 2 | 17.5 | -30 | -60 |
| 25 - 40 | 3 | 32.5 | -15 | -45 |
| 40 - 55 | 7 | 47.5 | 0 | 0 |
| 55 - 70 | 6 | 62.5 | 15 | 90 |
| 70 - 85 | 6 | 77.5 | 30 | 180 |
| 85 - 100 | 6 | 92.5 | 45 | 270 |
| Total | $\Sigma f_i = 30$ | | | $\Sigma f_i d_i = 435$ |

Substituting the values of $a$, $\Sigma f_{i}d_{i}$ and $\Sigma f_{i}$ from the table, we get

$$ \overline {{x}} = 47.5 + \frac {435}{30} = 47.5 + 14.5 = 62 $$

Therefore, the mean of the marks obtained by the students is 62. The method discussed above is called the Assumed Mean Method.

## The Step-Deviation Method

Observe that in the Assumed Mean Method, the values in the $d_i$ column are all multiples of 15. So, if we divide all the $d_i$ values by 15, we would get smaller numbers to multiply with $f_{i}$. (Here, 15 is the class size of each class interval.)

So, let $u_{i} = \frac{x_{i} - a}{h}$, where $a$ is the assumed mean and $h$ is the class size.

Now, we calculate $u_{i}$ in this way and continue as before (i.e., find $f_{i}u_{i}$ and then $\Sigma f_{i}u_{i}$).

The relation between the mean of the step-deviations, $\bar{u}$, and the mean, $\overline{x}$, is given by:

$$ \overline {{x}} = a + h \overline {{u}} $$

i.e.,

$$ \overline {{x}} = a + h \left(\frac {\Sigma f _ {i} u _ {i}}{\Sigma f _ {i}}\right) $$

Taking $h = 15$, let us form the following table:

| Class interval | $f_i$ | $x_i$ | $d_i = x_i - a$ | $u_i = \frac{x_i - a}{h}$ | $f_i u_i$ |
| --- | --- | --- | --- | --- | --- |
| 10 - 25 | 2 | 17.5 | -30 | -2 | -4 |
| 25 - 40 | 3 | 32.5 | -15 | -1 | -3 |
| 40 - 55 | 7 | 47.5 | 0 | 0 | 0 |
| 55 - 70 | 6 | 62.5 | 15 | 1 | 6 |
| 70 - 85 | 6 | 77.5 | 30 | 2 | 12 |
| 85 - 100 | 6 | 92.5 | 45 | 3 | 18 |
| Total | $\Sigma f_i = 30$ | | | | $\Sigma f_i u_i = 29$ |

Substituting the values of $a$, $h$, $\Sigma f_{i}u_{i}$ and $\Sigma f_{i}$ from the table, we get

$$ \overline {{x}} = 47.5 + 15 \times \left(\frac {29}{30}\right) = 47.5 + 14.5 = 62 $$

So, the mean marks obtained by a student is 62. The method discussed above is called the Step-deviation method.

## Worked example

Let us apply the Step-deviation method to a new example. The table below gives the percentage distribution of female teachers in the primary schools of rural areas of various states and union territories (U.T.) of India.

| Percentage of female teachers | 15 - 25 | 25 - 35 | 35 - 45 | 45 - 55 | 55 - 65 | 65 - 75 | 75 - 85 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Number of States/U.T. | 6 | 11 | 7 | 4 | 4 | 2 | 1 |

Let us find the class marks, $x_{i}$, of each class, and put them in a column:

| Percentage of female teachers | Number of States /U.T. ($f_i$) | $x_i$ |
| --- | --- | --- |
| 15 - 25 | 6 | 20 |
| 25 - 35 | 11 | 30 |
| 35 - 45 | 7 | 40 |
| 45 - 55 | 4 | 50 |
| 55 - 65 | 4 | 60 |
| 65 - 75 | 2 | 70 |
| 75 - 85 | 1 | 80 |

Here we take $a = 50$ and $h = 10$, so that $u_{i} = \frac{x_{i} - 50}{10}$.

We now find $u_{i}$ and $f_{i}u_{i}$ and put them in a table:

| Percentage of female teachers | $f_i$ | $x_i$ | $u_i = \frac{x_i - 50}{10}$ | $f_i u_i$ |
| --- | --- | --- | --- | --- |
| 15 - 25 | 6 | 20 | -3 | -18 |
| 25 - 35 | 11 | 30 | -2 | -22 |
| 35 - 45 | 7 | 40 | -1 | -7 |
| 45 - 55 | 4 | 50 | 0 | 0 |
| 55 - 65 | 4 | 60 | 1 | 4 |
| 65 - 75 | 2 | 70 | 2 | 4 |
| 75 - 85 | 1 | 80 | 3 | 3 |
| Total | $\Sigma f_i = 35$ | | | $\Sigma f_i u_i = -36$ |

Substituting the values of $a$, $h$, $\Sigma f_{i}u_{i}$ and $\Sigma f_{i}$ from the table, we get

$$ \overline {{x}} = 50 + 10 \times \left(\frac {-36}{35}\right) = 50 - 10.29 = 39.71 $$

So, the mean percentage of female teachers in the primary schools of rural areas is 39.71.

## Key points

- The mean of grouped data is an approximate value, calculated by assuming that the frequencies of each class interval are centered around its class mark.
- The Direct Method uses the formula $\bar{x} = \frac{\Sigma f_{i} x_{i}}{\Sigma f_{i}}$ to find the mean of grouped data.
- The Assumed Mean Method simplifies the calculations by using an assumed mean 'a' and the formula $\overline {{x}} = a + \frac {\Sigma f _ {i} d _ {i}}{\Sigma f _ {i}}$.
- The Step-deviation method further simplifies the calculations by using the step-deviation $u_{i} = \frac{x_{i} - a}{h}$ and the formula $\overline {{x}} = a + h \left(\frac {\Sigma f _ {i} u _ {i}}{\Sigma f _ {i}}\right)$.
- The mean obtained by all the three methods is the same.
- The assumed mean method and step-deviation method are just simplified forms of the direct method.