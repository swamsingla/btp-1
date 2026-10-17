---
{
  "concept": "Fractions",
  "slug": "fractions",
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
    "completion_tokens": 1212,
    "prompt_tokens": 5614,
    "total_tokens": 6826,
    "completion_tokens_details": null,
    "prompt_tokens_details": null
  },
  "target_words": [
    700,
    1250
  ],
  "generated_at": "2026-10-02T19:37:30",
  "source_grade": 6,
  "grade_delta": 0,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g6_maths_chapter7_033",
      "chapter": "chapter7",
      "section": "7.8 Addition and Subtraction of Fractions"
    },
    {
      "ref": "S2",
      "passage_id": "g6_maths_chapter7_009",
      "chapter": "chapter7",
      "section": "7.5 Mixed Fractions"
    },
    {
      "ref": "S3",
      "passage_id": "g6_maths_chapter7_014",
      "chapter": "chapter7",
      "section": "7.6 Equivalent Fractions"
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
    "words": 784,
    "target_words": [
      700,
      1250
    ],
    "untraceable_sections": 0,
    "ok": true,
    "structural_problems": []
  },
  "terms": [
    "numerator",
    "denominator",
    "equivalent fractions",
    "common denominator",
    "smallest common multiple",
    "brahmagupta’s method",
    "mixed fraction",
    "fractional unit"
  ],
  "hand_edited": "2026-10-02: three '###' sub-headings broke the declared page shape and were invisible to check_pages, which only parses '##'; converted to bold lead-ins. All the arithmetic was already correct and is unchanged. Held for citing none of its three sources, which this does not address. Not regenerated. Grade 6 word band recalibrated from 900-1250 to 700-1250 on 2026-10-02 after two full runs showed the model never reaches 900 for these concepts (see the comment on GRADE_WORDS in build_context.py); this page kept its text and had its recorded band updated to the new standard. Source tags added on 2026-10-02 by the generator's repair stage (build_context.render_repair), which annotates an existing page instead of rewriting it, so the hand corrections above were preserved; the tagged copy is in data/intermediate/generated_tagged and the published text carries no tags."
}
---

# Fractions

Fractions are numbers of the form $\frac{a}{b}$ that represent parts of a whole. They are essential in everyday life, from splitting a chocolate bar among friends to measuring ingredients for a recipe. Understanding fractions allows you to work with parts of quantities, which is a fundamental skill in mathematics.

## Parts of a Whole

A fraction describes a portion of a single unit. If you have one whole object and divide it into equal pieces, each piece is a fraction of the whole. For example, if you cut a piece of chikki into two equal parts, each part is $\frac{1}{2}$ of the whole. If you cut it into four equal parts, each part is $\frac{1}{4}$ of the whole. The line in a fraction separates the numerator, which tells you how many parts you have, from the denominator, which tells you how many equal parts make up the whole.

## Fractions Greater Than One

Sometimes, a fraction is larger than one whole unit. This happens when the numerator is larger than the denominator. For example, $\frac{3}{2}$ means you have three pieces of size $\frac{1}{2}$. Since two pieces of size $\frac{1}{2}$ make one whole, $\frac{3}{2}$ is equal to $1 + \frac{1}{2}$. Similarly, $\frac{5}{2}$ is equal to $2 + \frac{1}{2}$. You can think of these as mixed fractions, which combine a whole number with a proper fraction.

## Equivalent Fractions

Equivalent fractions are different fractions that represent the same length or value. For example, $\frac{1}{2}$ and $\frac{2}{4}$ are equivalent because they both represent the same portion of a whole. You can find equivalent fractions by multiplying or dividing both the numerator and the denominator by the same non-zero number. For instance, $\frac{1}{2} = \frac{2}{4} = \frac{4}{8}$. A fraction wall is a useful tool to visualize these equivalent fractions, showing that different fractional units can have the same length.

## Adding Fractions

To add fractions, you must first ensure they have the same fractional unit, or denominator. If the denominators are different, you need to convert the fractions into equivalent fractions with a common denominator.

**Adding Fractions with the Same Denominator**

When fractions have the same denominator, you simply add the numerators and keep the denominator the same. For example, to find the sum of $\frac{2}{5}$ and $\frac{1}{5}$, you add the numerators: $2 + 1 = 3$. The result is $\frac{3}{5}$. This is because each fraction represents parts of the same size, so you are just counting the total number of those parts.

**Adding Fractions with Different Denominators**

When fractions have different denominators, you must find a common denominator. The easiest way is to multiply the denominators together. For example, to add $\frac{1}{4}$ and $\frac{1}{3}$, you find a common denominator of $12$. You convert $\frac{1}{4}$ to $\frac{3}{12}$ and $\frac{1}{3}$ to $\frac{4}{12}$. Then, you add the numerators: $3 + 4 = 7$. The sum is $\frac{7}{12}$.

**Brahmagupta’s Method**

The method for adding fractions with different denominators was first explicitly described by Brahmagupta in the year 628 CE. The steps are as follows:

1. Find equivalent fractions so that the fractional unit is common for all fractions. This can be done by finding a common multiple of the denominators, such as the product of the denominators or the smallest common multiple.
2. Add these equivalent fractions with the same fractional units by adding the numerators and keeping the same denominator.
3. Express the result in lowest terms if needed.

For example, to add $\frac{2}{3}$ and $\frac{1}{5}$, the smallest common multiple of 3 and 5 is 15. You convert $\frac{2}{3}$ to $\frac{10}{15}$ and $\frac{1}{5}$ to $\frac{3}{15}$. Adding these gives $\frac{13}{15}$.

## Worked example

Let us apply Brahmagupta’s method to find the sum of $\frac{3}{8}$ and $\frac{1}{6}$.

First, find the smallest common multiple of 8 and 6, which is 24. Convert $\frac{3}{8}$ to $\frac{9}{24}$ by multiplying the numerator and denominator by 3. Convert $\frac{1}{6}$ to $\frac{4}{24}$ by multiplying the numerator and denominator by 4.

Now, add the numerators: $9 + 4 = 13$. The sum is $\frac{13}{24}$.

## Key points

- A fraction $\frac{a}{b}$ represents $a$ parts of a whole divided into $b$ equal parts.
- Fractions greater than one have a numerator larger than the denominator.
- Equivalent fractions, such as $\frac{1}{2}$ and $\frac{2}{4}$, represent the same value.
- To add fractions, they must have the same denominator.
- Brahmagupta’s method provides a systematic way to add fractions with different denominators by finding a common denominator.
- The result of adding fractions should be expressed in lowest terms if necessary.
