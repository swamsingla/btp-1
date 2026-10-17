---
{
  "concept": "Data Representation — Grouped Data",
  "slug": "data-representation-grouped",
  "grade": 9,
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
    "completion_tokens": 1083,
    "prompt_tokens": 6500,
    "total_tokens": 7583,
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
  "generated_at": "2026-10-17T06:35:16",
  "source_grade": 9,
  "grade_delta": 0,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g9_maths_chapter12_007",
      "chapter": "chapter12",
      "section": "12.1 Graphical Representation of Data"
    }
  ],
  "citation_check": {
    "cited": [],
    "invented_citations": [],
    "unused_sources": [
      "1"
    ],
    "explanatory_paragraphs_without_a_citation": 4,
    "words": 859,
    "target_words": [
      1000,
      1350
    ],
    "untraceable_sections": 4,
    "ok": false,
    "structural_problems": []
  },
  "terms": [
    "grouped data",
    "continuous class intervals",
    "frequency distribution table",
    "bar graph",
    "histogram",
    "frequency polygon",
    "class intervals",
    "class size",
    "frequency",
    "class-mark",
    "mid-points",
    "rectangular bars",
    "horizontal axis",
    "vertical axis",
    "variable",
    "value",
    "proportional"
  ]
}
---

# Data Representation — Grouped Data

When you look at a long list of numbers, it can be hard to see what is happening. For example, if you have a list of the heights of all 200 students in a school, you might struggle to find the average height or see which height is most common. To make this easier, we group the data into intervals, like 150 cm to 155 cm, and count how many students fall into each interval. This grouped data is much easier to read. However, to make it even easier to understand at a glance, we use pictures. These pictures help us compare the data quickly and show us the shape of the numbers.

## Bar Graphs

You may already know how to make a bar graph. A bar graph is a picture that shows data using bars of equal width. There are equal gaps between the bars. The bars are drawn on one axis, usually the horizontal axis, and the values are shown on the other axis, usually the vertical axis. The height of each bar depends on the value of the data. For example, if you want to show the monthly expenses of a family, you can draw a bar for each expense, like groceries, rent, or education. The height of the bar shows how much money is spent on that item. Because the bars are separated, it is easy to compare the different expenses.

## Histograms

A histogram is very similar to a bar graph, but it is used for continuous class intervals, which are groups of numbers that flow one after another without gaps, like 30.5 to 35.5 kg. In a histogram, we draw rectangles instead of separate bars. The width of each rectangle is equal to the class size. The height of the rectangle is equal to the frequency, which is the number of items in that group. Because there are no gaps between the rectangles, the graph looks like a solid shape. In a histogram, the area of each rectangle is proportional to the frequency. This means that if one group has twice as many items as another, its rectangle will have twice the area.

## Histograms of Varying Widths

Sometimes, the class intervals are not the same size. For example, a teacher might group test scores as 0 to 20, 20 to 30, 30 to 40, and then one wide last group of 40 to 100. When the widths of the rectangles are not equal, we cannot just draw the height equal to the frequency. If we do, the graph will give a misleading picture. The area of the rectangle must still be proportional to the frequency. To fix this, we calculate an adjusted length for each rectangle. We pick the smallest class size, and for every class we multiply its frequency by (smallest class size ÷ that class's size) to get the length of its rectangle. For example, if the smallest class size is 10 and another class has size 20, we multiply its frequency by 10/20, that is, we divide it by 2, to get the correct length.

## Frequency Polygons

A frequency polygon is another way to show grouped data. To make one, we join the midpoints of the upper sides of the rectangles in a histogram with straight lines. To complete the shape, we imagine two extra intervals with a frequency of zero before the first group and after the last group. We then join these points to the ends of our line. Frequency polygons are very useful when the data is continuous and very large. They are also very helpful when you want to compare two different sets of data, like the test scores of two different classes, on the same graph.

## Worked example

Let us say you have the following grouped data for the ages of people in a park:
- 10 to 20 years: 5 people
- 20 to 30 years: 15 people
- 30 to 40 years: 10 people
- 40 to 50 years: 8 people

To make a histogram, you would draw rectangles with widths of 10 years. The height of the first rectangle would be 5, the second would be 15, and so on. To make a frequency polygon, you would find the midpoints of these intervals: 15, 25, 35, and 45. You would then plot these points on a graph with the frequencies on the vertical axis. Finally, you would join these points with straight lines and add two extra points with a frequency of zero, one at the midpoint 5 of the imaginary interval 0 to 10 before the first group, and one at the midpoint 55 of the imaginary interval 50 to 60 after the last group.

## Key points
- A bar graph uses bars with equal width and equal gaps to show discrete data.
- A histogram uses rectangles without gaps to show continuous grouped data.
- In a histogram with equal widths, the height of the rectangle shows the frequency.
- In a histogram with varying widths, the area of the rectangle must show the frequency, so the height is adjusted.
- A frequency polygon is made by joining the midpoints of the top edges of the histogram rectangles.