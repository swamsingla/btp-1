---
{
  "concept": "Median of Grouped Data",
  "slug": "median-of-grouped-data",
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
    "completion_tokens": 1714,
    "prompt_tokens": 6960,
    "total_tokens": 8674,
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
  "generated_at": "2026-10-18T00:58:55",
  "source_grade": 10,
  "grade_delta": 0,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g10_maths_chapter13_039",
      "chapter": "chapter13",
      "section": "13.4 Median of Grouped Data"
    }
  ],
  "citation_check": {
    "cited": [
      "1"
    ],
    "invented_citations": [],
    "unused_sources": [],
    "explanatory_paragraphs_without_a_citation": 4,
    "words": 1060,
    "target_words": [
      1000,
      1350
    ],
    "untraceable_sections": 1,
    "ok": true,
    "structural_problems": []
  },
  "terms": [
    "median",
    "grouped data",
    "median class",
    "cumulative frequency",
    "interpolation formula",
    "ogive"
  ]
}
---

# Median of Grouped Data

The median is a measure of central tendency which gives the value of the middle-most observation in the data. When data is grouped into class intervals, we do not have the exact individual scores, so we must estimate where the middle value lies within a specific range. This process is essential because raw scores are often unavailable, and we need a representative value that splits the distribution into two equal halves, with 50% of the observations below and 50% above it.

## The Median Class

In grouped data, the middle observation does not correspond to a single exact number but falls inside a specific class interval. To locate this interval, we calculate the cumulative frequency of each class and compare it with half of the total number of observations, $\frac{n}{2}$. The class whose cumulative frequency is greater than (and nearest to) $\frac{n}{2}$ is called the median class. 

For example, consider a survey of the heights (in cm) of 51 girls of Class X. The cumulative frequencies for the class intervals are as follows:

| Class intervals | Frequency | Cumulative frequency |
| --- | --- | --- |
| Below 140 | 4 | 4 |
| 140 - 145 | 7 | 11 |
| 145 - 150 | 18 | 29 |
| 150 - 155 | 11 | 40 |
| 155 - 160 | 6 | 46 |
| 160 - 165 | 5 | 51 |

Here, $n = 51$, so $\frac{n}{2} = \frac{51}{2} = 25.5$. This observation lies in the class 145 - 150. Therefore, 145 - 150 is the median class.

## Interpolation Formula

Once the median class is identified, we use the interpolation formula to estimate the exact median value. The formula is:

$$ \text{Median} = l + \left(\frac {\frac {n}{2} - \mathrm{cf}}{f}\right) \times h $$

In this formula, $l$ is the lower limit of the median class, $n$ is the number of observations, $\mathrm{cf}$ is the cumulative frequency of the class preceding the median class, $f$ is the frequency of the median class, and $h$ is the class size (assuming class size to be equal). 

Applying this to the height example, where $l = 145$, $\mathrm{cf} = 11$, $f = 18$, and $h = 5$, we calculate:

$$ \text{Median} = 145 + \left(\frac {25.5 - 11}{18}\right) \times 5 = 145 + \frac {72.5}{18} = 149.03 $$

So, the median height of the girls is $149.03\mathrm{cm}$. This means that the height of about 50% of the girls is less than this height, and 50% are taller than this height.

## Graphical Method via Ogives

Another way to find the median of grouped data is by using a graphical method through ogives. An ogive is a curve representing the cumulative frequency distribution of a dataset. To construct an ogive, we plot the upper limits of the class intervals on the horizontal axis and their corresponding cumulative frequencies on the vertical axis. We then join the plotted points with a smooth curve to get the less-than type ogive.

To find the median graphically, we locate the point on the vertical axis that corresponds to half of the total cumulative frequency, which is $\frac{n}{2}$. From this point, we draw a horizontal line to intersect the ogive curve. From the point of intersection, we drop a perpendicular to the horizontal axis. The value on the horizontal axis at this point is the median. This graphical method provides a visual estimation of the median and is particularly useful when dealing with large datasets.

## Worked example

Suppose the marks obtained by 53 students of a class in an examination out of 100 are grouped as follows:

| Marks | Number of students |
| --- | --- |
| 0 - 10 | 5 |
| 10 - 20 | 3 |
| 20 - 30 | 4 |
| 30 - 40 | 3 |
| 40 - 50 | 3 |
| 50 - 60 | 4 |
| 60 - 70 | 7 |
| 70 - 80 | 9 |
| 80 - 90 | 7 |
| 90 - 100 | 8 |

The cumulative frequency table is:

| Marks | Number of students (f) | Cumulative frequency (cf) |
| --- | --- | --- |
| 0 - 10 | 5 | 5 |
| 10 - 20 | 3 | 8 |
| 20 - 30 | 4 | 12 |
| 30 - 40 | 3 | 15 |
| 40 - 50 | 3 | 18 |
| 50 - 60 | 4 | 22 |
| 60 - 70 | 7 | 29 |
| 70 - 80 | 9 | 38 |
| 80 - 90 | 7 | 45 |
| 90 - 100 | 8 | 53 |

Here, $n = 53$, so $\frac{n}{2} = 26.5$. The class whose cumulative frequency is greater than (and nearest to) $26.5$ is $60 - 70$. Therefore, $60 - 70$ is the median class. We have $l = 60$, $\mathrm{cf} = 22$, $f = 7$, and $h = 10$. Using the formula:

$$ \text{Median} = 60 + \left(\frac {26.5 - 22}{7}\right) \times 10 = 60 + \frac {45}{7} = 66.4 $$

So, about half the students have scored marks less than $66.4$, and the other half have scored marks more than $66.4$.

## Key points

*   The median is the middle-most observation in a dataset, giving the value that divides the data into two equal halves.
*   For grouped data, the class interval containing the middle observation is identified as the median class.
*   The interpolation formula $l + \left(\frac {\frac {n}{2} - \mathrm{cf}}{f}\right) \times h$ is used to estimate the exact median value from the median class.
*   The graphical method involves plotting an ogive using the cumulative frequency distribution to visually estimate the median.
*   The median conveys that about 50% of the observations lie below it and 50% lie above it.