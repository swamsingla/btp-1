---
{
  "concept": "Palindromic Numbers",
  "slug": "palindromic-numbers",
  "grade": 6,
  "language": "en",
  "subject": "maths",
  "area": "Number Theory",
  "model": "sarvam-105b",
  "settings": {
    "temperature": 0.3,
    "max_tokens": 8000,
    "reasoning_effort": "none"
  },
  "usage": {
    "completion_tokens": 1493,
    "prompt_tokens": 3424,
    "total_tokens": 4917,
    "completion_tokens_details": null,
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cached_tokens": 192
    }
  },
  "target_words": [
    700,
    1250
  ],
  "generated_at": "2026-10-02T19:42:22",
  "source_grade": 6,
  "grade_delta": 0,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g6_maths_chapter3_009",
      "chapter": "chapter3",
      "section": "3.5 Pretty Palindromic Patterns"
    },
    {
      "ref": "S2",
      "passage_id": "g6_maths_chapter5_025",
      "chapter": "chapter5",
      "section": "5.6 Fun with numbers"
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
      "3"
    ],
    "invented_citations": [],
    "unused_sources": [
      "2"
    ],
    "explanatory_paragraphs_without_a_citation": 4,
    "words": 938,
    "target_words": [
      700,
      1250
    ],
    "untraceable_sections": 0,
    "ok": true,
    "structural_problems": []
  },
  "terms": [
    "palindrome",
    "palindromic number",
    "reverse-and-add",
    "number theory",
    "whole numbers"
  ],
  "hand_edited": "2026-10-02: the page asked 'Are there numbers for which you do not reach a palindrome at all?' and answered 'This is a great question to explore', which the brief forbids; it now states that every two-digit number reaches one and that 196 is the smallest number for which none has ever been found. It also claimed 56 needs 'several steps', but 56 + 65 = 121 is a palindrome in one step; replaced with 89 and 98, which need 24. Not regenerated. Grade 6 word band recalibrated from 900-1250 to 700-1250 on 2026-10-02 after two full runs showed the model never reaches 900 for these concepts (see the comment on GRADE_WORDS in build_context.py); this page kept its text and had its recorded band updated to the new standard."
}
---

# Palindromic Numbers

Have you ever looked at a word in a mirror and noticed it looked exactly the same as the word in front of you? In mathematics, we have a similar idea with numbers. A number that reads the exact same from left to right and from right to left is called a palindrome, or a palindromic number. These numbers are fascinating because they show a perfect balance. Just like a reflection in a mirror, the digits are arranged symmetrically. Understanding palindromic numbers helps us explore how digits can be arranged to create beautiful patterns, which is a very important part of number theory, the branch of mathematics that studies patterns in whole numbers.

## What Makes a Number a Palindrome?

To understand palindromic numbers, we first need to look at the digits that make up the number. A palindrome is a number that reads the same from left to right and from right to left. For example, the number $848$ reads as $848$ whether you start from the left or the right. The same is true for $575$ and $797$. These numbers are symmetrical. 

You can also make palindromes using specific digits. For instance, the numbers $121$, $313$, and $222$ are examples of palindromes using the digits $1$, $2$, and $3$. If you want to write all possible 3-digit palindromes using these digits, you need to make sure the first and the last digits are the same. 

## Building Palindromes with Three Digits

When you build a 3-digit palindrome, the first digit and the last digit must be identical. The middle digit can be anything. Let us look at the digits $1$, $2$, and $3$. If you choose $1$ for the first and last position, you can put $1$, $2$, or $3$ in the middle. This gives you $111$, $121$, and $131$. If you choose $2$ for the first and last position, you get $212$, $222$, and $232$. If you choose $3$ for the first and last position, you get $313$, $323$, and $333$. These are all the possible 3-digit palindromes using the digits $1$, $2$, and $3$.

## Reverse-and-Add Patterns

Now, let us look at a fun way to create palindromes. This is called the reverse-and-add process. The rule is simple: start with a number. Add this number to its reverse. If the result is a palindrome, you are done. If it is not a palindrome, you repeat the steps of reversing the digits and adding.

Let us try this with the number $34$. The reverse of $34$ is $43$. When you add them together, $34 + 43 = 77$. The number $77$ is a palindrome, so we stop here. 

Let us try another number, $29$. The reverse of $29$ is $92$. When you add them together, $29 + 92 = 121$. The number $121$ is a palindrome, so we stop here.

Let us try $48$. The reverse of $48$ is $84$. When you add them together, $48 + 84 = 132$. The number $132$ is not a palindrome. So, we repeat the steps. The reverse of $132$ is $231$. When you add them together, $132 + 231 = 363$. The number $363$ is a palindrome, so we stop here.

## Exploring the Process

You can try this procedure for other numbers too. For example, let us start with $76$. The reverse of $76$ is $67$. When you add them together, $76 + 67 = 143$. The number $143$ is not a palindrome. So, we repeat the steps. The reverse of $143$ is $341$. When you add them together, $143 + 341 = 484$. The number $484$ is a palindrome, so we stop here.

Some starting numbers need the process repeated many more times. Among the two-digit numbers the slowest are $89$ and $98$, which need 24 rounds of reversing and adding before a palindrome finally appears. That is a reminder that a short chain like $34 \rightarrow 77$ is luck, not the rule.

Every two-digit number does reach a palindrome in the end. For larger numbers the answer is not known. The smallest number for which nobody has ever found a palindrome is $196$: it has been reversed and added millions of times without one appearing, and yet no one has proved that it never will. So this is a question you can state in one line in Grade 6 and that mathematicians still cannot answer. 

## Worked Example

Let us look at a worked example to make sure we understand the rule. Let us start with the number $87$. 

First, we reverse the digits to get $78$. 
Next, we add them together: $87 + 78 = 165$. 
The number $165$ is not a palindrome. So, we repeat the steps. 
We reverse $165$ to get $561$. 
We add them together: $165 + 561 = 726$. 
The number $726$ is not a palindrome. So, we repeat the steps again. 
We reverse $726$ to get $627$. 
We add them together: $726 + 627 = 1353$. 
The number $1353$ is not a palindrome. So, we repeat the steps again. 
We reverse $1353$ to get $3531$. 
We add them together: $1353 + 3531 = 4884$. 
The number $4884$ is a palindrome, so we stop here.

## Key points

*   A palindrome, or a palindromic number, is a number that reads the same from left to right and from right to left.
*   To build a 3-digit palindrome, the first and the last digits must be identical, while the middle digit can be any digit.
*   The reverse-and-add process involves adding a number to its reverse and repeating the steps until a palindrome is reached.
*   The branch of mathematics that studies patterns in whole numbers is called number theory.
*   Every two-digit number reaches a palindrome eventually, but the number of steps varies a lot: $34$ takes one step while $89$ takes 24.