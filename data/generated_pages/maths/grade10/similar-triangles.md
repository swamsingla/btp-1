---
{
  "concept": "Similar Triangles",
  "slug": "similar-triangles",
  "grade": 10,
  "language": "en",
  "subject": "maths",
  "area": "Geometry",
  "model": "sarvam-105b",
  "settings": {
    "temperature": 0.3,
    "max_tokens": 8000,
    "reasoning_effort": "none"
  },
  "usage": {
    "completion_tokens": 1041,
    "prompt_tokens": 8451,
    "total_tokens": 9492,
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
  "generated_at": "2026-10-17T22:05:58",
  "source_grade": 10,
  "grade_delta": 0,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g10_maths_chapter6_021",
      "chapter": "chapter6",
      "section": "6.4 Criteria for Similarity of Triangles"
    }
  ],
  "citation_check": {
    "cited": [
      "1"
    ],
    "invented_citations": [],
    "unused_sources": [],
    "explanatory_paragraphs_without_a_citation": 0,
    "words": 669,
    "target_words": [
      1000,
      1350
    ],
    "untraceable_sections": 0,
    "ok": true,
    "structural_problems": [
      "length: 669 words, under 1000"
    ]
  },
  "terms": [
    "similarity",
    "corresponding sides",
    "corresponding angles",
    "scale factor",
    "aa similarity",
    "sss similarity",
    "sas similarity",
    "proportional"
  ]
}
---

# Similar Triangles

Similar triangles are a cornerstone of geometry, describing shapes that have the exact same form but may differ in size. When two triangles are similar, their corresponding angles are equal and their corresponding sides are in the same ratio or proportion. This concept is essential because it allows us to solve complex problems involving scale, distance, and height by relating them to known measurements through a consistent ratio.

## What Does Similar Mean?

Two figures are similar if they have the same shape, even when their sizes differ. An enlarged photograph is similar to the original, and any two circles are similar, as are any two squares. Similar figures are not the same as congruent figures: congruent figures have the same shape and the same size, so every pair of congruent figures is similar, but not the other way round.

For polygons with more than three sides, equal angles alone are not enough. A square and a rectangle that is not a square have all angles equal to $90^\circ$, but their sides are not in the same ratio, so they are not similar. Triangles are special, as the criteria below show.

## Symbolic Representation

When stating that two triangles are similar, the order of the vertices matters. The symbol ‘$\sim$’ is used to denote that one triangle is similar to another. For instance, if $\Delta$ ABC is similar to $\Delta$ DEF, the correspondence means that vertex A matches vertex D, B matches E, and C matches F. Consequently, the similarity is written as $\Delta$ ABC $\sim$ $\Delta$ DEF and read as 'triangle ABC is similar to triangle DEF'. It is crucial to maintain this correct vertex correspondence when writing symbolic statements. You may already know that congruence uses the symbol ‘$\cong$’ for 'is congruent to', but here the symbol is $\sim$ for similarity.

## The AAA (or AA) Similarity Criterion

The AAA criterion states that if the corresponding angles of two triangles are equal, then their corresponding sides are in the same ratio. This means that if $\angle A = \angle D$, $\angle B = \angle E$, and $\angle C = \angle F$, then $\frac{\mathrm{AB}}{\mathrm{DE}} = \frac{\mathrm{BC}}{\mathrm{EF}} = \frac{\mathrm{CA}}{\mathrm{FD}}$. Because of the angle sum property of a triangle, it is sufficient to know that two angles are equal, as the third will automatically be equal, leading to the AA criterion.

## The SSS Similarity Criterion

The SSS criterion states that if the sides of one triangle are proportional to the sides of another triangle, then their corresponding angles are equal. For example, if $\frac{\mathrm{AB}}{\mathrm{DE}} = \frac{\mathrm{BC}}{\mathrm{EF}} = \frac{\mathrm{CA}}{\mathrm{FD}}$, then $\Delta$ ABC $\sim$ $\Delta$ DEF. This criterion directly implies that the corresponding angles must be equal, making the two triangles similar.

## The SAS Similarity Criterion

The SAS criterion states that if one angle of a triangle is equal to one angle of another triangle and the sides including these angles are proportional, then the two triangles are similar. For instance, if $\frac{\mathrm{AB}}{\mathrm{DE}} = \frac{\mathrm{AC}}{\mathrm{DF}}$ and $\angle \mathrm{A} = \angle \mathrm{D}$, then $\Delta$ ABC $\sim$ $\Delta$ DEF.

## Worked example

Consider a practical application of the AA criterion. Imagine a girl walking away from a lamp-post. The lamp-post AB is 3.6 m above the ground, with B at its foot, and the girl CD is 0.9 m tall, with D at her feet. If the girl walks at a speed of 1.2 m/s, we can find the length of her shadow DE after 4 seconds, where E is the tip of the shadow on the ground. First, calculate the distance the girl walked from the foot of the lamp-post: $BD = 1.2 \times 4 = 4.8$ m. Let the shadow length $DE = x$ metres, so $BE = 4.8 + x$. In $\Delta$ ABE and $\Delta$ CDE, $\angle$ B and $\angle$ D are both $90^\circ$ because both the lamp-post and the girl are standing vertical to the ground, and $\angle$ E is the same angle in both triangles. Therefore, by the AA similarity criterion, $\Delta$ ABE $\sim$ $\Delta$ CDE. Using the proportional sides, we set up the equation $\frac{4.8 + x}{x} = \frac{3.6}{0.9}$. Solving for $x$, we get $4.8 + x = 4x$, which simplifies to $3x = 4.8$, yielding $x = 1.6$. Thus, the length of her shadow after 4 seconds is 1.6 m.

## Using the SSS and SAS Criteria

Example (SSS): Triangle $ABC$ has sides $AB = 3$ cm, $BC = 4$ cm and $CA = 5$ cm, and triangle $DEF$ has sides $DE = 6$ cm, $EF = 8$ cm and $FD = 10$ cm. Then $\frac{AB}{DE} = \frac{3}{6} = \frac{1}{2}$, $\frac{BC}{EF} = \frac{4}{8} = \frac{1}{2}$ and $\frac{CA}{FD} = \frac{5}{10} = \frac{1}{2}$. The three ratios are equal, so $\Delta ABC \sim \Delta DEF$ by the SSS criterion.

Example (SAS): In triangle $ABC$, $AB = 4$ cm, $AC = 6$ cm and $\angle A = 50^\circ$. In triangle $DEF$, $DE = 8$ cm, $DF = 12$ cm and $\angle D = 50^\circ$. Then $\frac{AB}{DE} = \frac{4}{8} = \frac{1}{2}$ and $\frac{AC}{DF} = \frac{6}{12} = \frac{1}{2}$, and the angles between these sides are equal. So $\Delta ABC \sim \Delta DEF$ by the SAS criterion.

## Key points
- Similar triangles have equal corresponding angles and proportional corresponding sides.
- The order of vertices in the similarity statement must reflect the correct correspondence.
- The AAA (or AA), SAS, and SSS are the three criteria for proving similarity.
- For the AA criterion, two equal angles are sufficient to establish similarity.
- For the SSS criterion, proportional sides guarantee equal corresponding angles.
- For the SAS criterion, one equal angle and proportional surrounding sides establish similarity.