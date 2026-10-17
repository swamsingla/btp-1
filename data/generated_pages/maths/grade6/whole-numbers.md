---
{
  "concept": "Whole Numbers",
  "slug": "whole-numbers",
  "grade": 6,
  "language": "en",
  "subject": "maths",
  "area": "Number Systems",
  "model": "sarvam-105b",
  "settings": {
    "temperature": 0.3,
    "max_tokens": 8000,
    "reasoning_effort": "none"
  },
  "usage": {
    "completion_tokens": 1277,
    "prompt_tokens": 3691,
    "total_tokens": 4968,
    "completion_tokens_details": null,
    "prompt_tokens_details": null
  },
  "target_words": [
    700,
    1250
  ],
  "generated_at": "2026-10-02T19:48:48",
  "source_grade": 6,
  "grade_delta": 0,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g6_maths_chapter3_001",
      "chapter": "chapter3",
      "section": "3.1 Numbers can Tell us Things"
    },
    {
      "ref": "S2",
      "passage_id": "g6_maths_chapter3_013",
      "chapter": "chapter3",
      "section": "3.8 Mental Math"
    },
    {
      "ref": "S3",
      "passage_id": "g6_maths_chapter1_002",
      "chapter": "chapter1",
      "section": "1.2 Patterns in Numbers"
    }
  ],
  "citation_check": {
    "cited": [
      "1",
      "2",
      "3"
    ],
    "invented_citations": [],
    "unused_sources": [],
    "explanatory_paragraphs_without_a_citation": 0,
    "words": 919,
    "target_words": [
      700,
      1250
    ],
    "untraceable_sections": 0,
    "ok": true,
    "structural_problems": []
  },
  "terms": [
    "whole numbers",
    "natural numbers",
    "zero",
    "number theory",
    "number sequences",
    "counting numbers",
    "odd numbers",
    "even numbers",
    "triangular numbers",
    "squares",
    "cubes",
    "powers of 2",
    "powers of 3"
  ],
  "hand_edited": "2026-10-02: the worked example gave 0,0,1,1,0 for all three arrangements, with the three paragraphs near-identical, and contradicted the page's own rule. Rewritten by hand to 1,1,1,1,0 / 0,1,1,1,1 / 0,1,2,1,0, the last added so the '2' case the page defines is actually shown. A sentence duplicated verbatim from the body was replaced with the sequences themselves. Not regenerated, so 'words' above is the model's original count. Grade 6 word band recalibrated from 900-1250 to 700-1250 on 2026-10-02 after two full runs showed the model never reaches 900 for these concepts (see the comment on GRADE_WORDS in build_context.py); this page kept its text and had its recorded band updated to the new standard."
}
---

# Whole Numbers

Whole numbers are the numbers you use when you start counting. They are the natural numbers together with zero: 0, 1, 2, 3, and so on. You already know how to count, so you already know the basics of whole numbers. Whole numbers are important because they help us tell things about the world around us, like how many people are standing in a line, or how many of a child's neighbours are taller.

## How Whole Numbers Tell Us Things

Whole numbers can tell us about the things we see every day. Imagine a group of children standing in a line. Each child says a number. These numbers are not just random. They represent a specific rule. A child says '1' if there is only one taller child standing next to them. A child says '2' if both of the children standing next to them are taller. A child says '0' if neither of the children standing next to them are taller.

This is a way to use whole numbers to describe a situation. The numbers tell us how many taller neighbours each person has. This is an example of how whole numbers can be used to tell us things.

## Adding and Subtracting Whole Numbers

You can use whole numbers to add and subtract. This is a basic operation that you already know. When you add two whole numbers, you get another whole number. For example, $12{,}350 + 24{,}545 = 36{,}895$. When you subtract a smaller whole number from a larger one, you again get a whole number. For example, $48{,}952 - 24{,}547 = 24{,}405$.

You can also use whole numbers to make other whole numbers. You can use addition and subtraction to get the required number. For example, $39{,}800 = 40{,}000 - 800 + 300 + 300$.

## Patterns in Whole Numbers

Whole numbers can also be used to make patterns. These patterns are a part of number theory, which is the branch of mathematics that studies patterns in whole numbers. Number sequences are the most basic and among the most fascinating types of patterns that mathematicians study.

Some common patterns in whole numbers include counting numbers, odd numbers, and even numbers. Counting numbers start at 1 and go up by 1 each time: 1, 2, 3, 4, 5, 6, 7, and so on. Odd numbers start at 1 and go up by 2 each time: 1, 3, 5, 7, 9, 11, 13, and so on. Even numbers start at 2 and go up by 2 each time: 2, 4, 6, 8, 10, 12, 14, and so on.

There are also other patterns in whole numbers, like triangular numbers, squares, cubes, and powers of 2 and 3. Triangular numbers go 1, 3, 6, 10, 15, and so on, each time adding one more than was added the time before. Squares go 1, 4, 9, 16, 25, and so on. Powers of 2 go 1, 2, 4, 8, 16, 32, doubling each time.

## Worked example

Let us use whole numbers to tell us something about a situation. Imagine a group of five children standing in a line. Each child says a number based on how many taller neighbours they have.

Remember that the two children at the ends of the line have only one neighbour each, while the three children in the middle have two neighbours each.

Let us say the children are arranged from shortest to tallest. The shortest child stands at one end and has a single neighbour, who is taller, so this child says 1. The second, third and fourth children each have a shorter child on their left and a taller child on their right, so each of them also says 1. The tallest child stands at the other end, and the only neighbour is shorter, so this child says 0.

So, the sequence of numbers is 1, 1, 1, 1, 0.

Now, let us say the children are arranged from tallest to shortest. The tallest child is at one end with a shorter neighbour, so this child says 0. The next three children each have a taller child on their left and a shorter child on their right, so each says 1. The shortest child is at the far end and the only neighbour is taller, so this child says 1.

So, the sequence of numbers is 0, 1, 1, 1, 1. Reversing the order of the line reverses the sequence of numbers.

Finally, let us put the shortest child in the middle, with the children getting taller towards both ends. The child at each end has one neighbour who is shorter, so both ends say 0. The second and fourth children each have one taller neighbour towards the end of the line and one shorter neighbour towards the middle, so each says 1. The shortest child, in the middle, has two neighbours and both are taller, so this child says 2.

So, the sequence of numbers is 0, 1, 2, 1, 0. This is the only one of our three arrangements in which any child says 2, because a child says 2 only when both neighbours are taller.

## Key points

* Whole numbers are the natural numbers together with zero: 0, 1, 2, 3, and so on.
* Whole numbers can be used to tell us things about the world around us, like how many taller neighbours a person has.
* Adding two whole numbers always gives another whole number, and so does subtracting a smaller whole number from a larger one.
* Whole numbers can be used to make patterns, which are a part of number theory.
* A child at the end of a line has one neighbour, so they can only say 0 or 1; a child in the middle has two, so they can also say 2.