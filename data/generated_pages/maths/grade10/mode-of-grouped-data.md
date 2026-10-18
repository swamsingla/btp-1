---
{
  "concept": "Mode of Grouped Data",
  "slug": "mode-of-grouped-data",
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
    "completion_tokens": 1415,
    "prompt_tokens": 4196,
    "total_tokens": 5611,
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
  "generated_at": "2026-10-18T00:59:04",
  "source_grade": 10,
  "grade_delta": 0,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g10_maths_chapter13_024",
      "chapter": "chapter13",
      "section": "13.3 Mode of Grouped Data"
    },
    {
      "ref": "S2",
      "passage_id": "g10_maths_chapter13_001",
      "chapter": "chapter13",
      "section": "13.1 Introduction"
    }
  ],
  "citation_check": {
    "cited": [
      "1"
    ],
    "invented_citations": [],
    "unused_sources": [
      "2"
    ],
    "explanatory_paragraphs_without_a_citation": 2,
    "words": 981,
    "target_words": [
      1000,
      1350
    ],
    "untraceable_sections": 0,
    "ok": true,
    "structural_problems": []
  },
  "terms": [
    "mode",
    "ungrouped data",
    "modal class",
    "grouped data",
    "interpolation formula",
    "lower limit",
    "class size",
    "frequency",
    "multimodal"
  ]
}
---

# Mode of Grouped Data

In Class IX, you may have already learned how to find the mode of ungrouped data. The mode is simply the value that occurs most often. However, when data is grouped into intervals, we cannot easily tell which exact value is the mode. We can only identify the interval that occurs most frequently. This interval is called the modal class. The actual mode is a specific value inside this modal class. To find it, we use a special interpolation formula that considers the frequencies of the modal class and its neighboring classes. This method allows us to estimate the precise mode even when the raw data is hidden inside the intervals.

## The Modal Class

When data is grouped, we look at the frequency of each class interval. The interval with the highest frequency is called the modal class. For example, imagine a survey of 20 households in a locality. The data might show the number of family members in each household, grouped into intervals like 1-3, 3-5, 5-7, 7-9, and 9-11. If the highest number of families falls into the 3-5 interval, then the modal class is 3-5. It is important to note that grouped data can sometimes have more than one modal class. In such cases, the data is called multimodal. However, for the purpose of this chapter, we will only look at problems that have a single mode.

## The Interpolation Formula

Since the data is hidden inside the modal class, we cannot just pick the midpoint. Instead, we use a formula to estimate the exact mode. The formula is:

$$ \text{Mode} = l + \left(\frac {f _ {1} - f _ {0}}{2 f _ {1} - f _ {0} - f _ {2}}\right) \times h $$

Here, $l$ is the lower limit of the modal class. $h$ is the size of the class interval, which we assume to be equal for all classes. $f_{1}$ is the frequency of the modal class. $f_{0}$ is the frequency of the class immediately before the modal class. $f_{2}$ is the frequency of the class immediately after the modal class.
## Worked Example

Let us apply this formula to a practical situation. Suppose a group of students surveyed 20 households to find the number of family members in each. The frequency table looks like this:

| Family size | 1 - 3 | 3 - 5 | 5 - 7 | 7 - 9 | 9 - 11 |
| --- | --- | --- | --- | --- | --- |
| Number of families | 7 | 8 | 2 | 2 | 1 |

First, we identify the modal class. The maximum frequency is 8, which corresponds to the class interval 3 - 5. Therefore, the modal class is 3 - 5. 

Next, we extract the values for our formula. The lower limit $l$ of the modal class is 3. The class size $h$ is 2, because 5 minus 3 equals 2. The frequency $f_{1}$ of the modal class is 8. The frequency $f_{0}$ of the class preceding the modal class is 7. The frequency $f_{2}$ of the class succeeding the modal class is 2. 

Now, we substitute these values into the interpolation formula:

$$ \text{Mode} = 3 + \left(\frac {8 - 7}{2 \times 8 - 7 - 2}\right) \times 2 $$

Simplifying the numerator and the denominator:

$$ \text{Mode} = 3 + \left(\frac {1}{16 - 9}\right) \times 2 $$
$$ \text{Mode} = 3 + \left(\frac {1}{7}\right) \times 2 $$
$$ \text{Mode} = 3 + \frac {2}{7} $$
$$ \text{Mode} = 3.286 $$

Therefore, the estimated mode of the data is 3.286. This means that the most common family size in the locality is approximately 3.286 members.

## Interpreting the Mode

Once you have calculated the mode, it is useful to compare it with other measures of central tendency, such as the mean. For instance, in a mathematics examination of 30 students, the marks distribution might have a modal class of 40 - 55. Using the interpolation formula with a lower limit of 40, a class size of 15, a modal frequency of 7, a preceding frequency of 3, and a succeeding frequency of 6, the mode calculates to 52. 

If the mean marks for the same exam were 62, the mode is less than the mean. This tells us that while the average student scored 62 marks, the most common score was 52. Depending on what you want to know, you might prefer the mean or the mode. If you want to know the average marks obtained by students, you use the mean. If you want to know the marks obtained by the largest group of students, you use the mode.

## Key points

*   The mode is the value with the maximum frequency in a dataset.
*   For grouped data, we identify the interval with the highest frequency, which is the modal class.
*   The exact mode for grouped data is estimated using the interpolation formula: $\text{Mode} = l + \left(\frac {f _ {1} - f _ {0}}{2 f _ {1} - f _ {0} - f _ {2}}\right) \times h$.
*   In this formula, $l$ is the lower limit of the modal class, $h$ is the class size, $f_{1}$ is the frequency of the modal class, $f_{0}$ is the frequency of the preceding class, and $f_{2}$ is the frequency of the succeeding class.
*   The mode can be compared with the mean to understand the distribution of data, such as comparing average marks with the most common marks.