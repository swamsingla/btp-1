---
{
  "concept": "Converse of Pythagorean Theorem",
  "slug": "converse-of-pythagorean-theorem",
  "grade": 8,
  "language": "od",
  "hand_edited": "2026-10-13: line-by-line hand audit against the English tagged copy, edited directly in both copies: the last key point was garbled so that it said the congruence rule is what gets proved; it now says the converse is proved using the rule that two triangles with three pairs of equal sides are congruent. cm written se.mi.; the two fixed headings no longer carry English brackets. The rest read correctly against the English (the carpenter and frame wording, 'three sides equal in pairs', and the squaring steps were all right in this draft)",
  "subject": "maths",
  "area": "Geometry",
  "model": "sarvam-105b",
  "settings": {
    "temperature": 0.3,
    "max_tokens": 8000,
    "reasoning_effort": "none"
  },
  "usage": {
    "completion_tokens": 1401,
    "prompt_tokens": 1642,
    "total_tokens": 3043,
    "completion_tokens_details": {
      "accepted_prediction_tokens": null,
      "audio_tokens": null,
      "reasoning_tokens": 0,
      "rejected_prediction_tokens": null
    },
    "prompt_tokens_details": null
  },
  "target_words": [
    950,
    1300
  ],
  "generated_at": "2026-10-13T14:21:13",
  "source_grade": 9,
  "grade_delta": 1,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g9_maths_chapter8_009",
      "chapter": "chapter8",
      "section": "8.2 The Mid-point Theorem"
    },
    {
      "ref": "S2",
      "passage_id": "g9_maths_chapter7_017",
      "chapter": "chapter7",
      "section": "7.5 Some More Criteria for Congruence of Triangles"
    },
    {
      "ref": "S3",
      "passage_id": "g9_maths_chapter9_014",
      "chapter": "chapter9",
      "section": "9.4 Angle Subtended by an Arc of a Circle"
    }
  ],
  "citation_check": {
    "cited": [
      "2"
    ],
    "invented_citations": [],
    "unused_sources": [
      "1",
      "3"
    ],
    "explanatory_paragraphs_without_a_citation": 0,
    "words": 689,
    "target_words": [
      950,
      1300
    ],
    "untraceable_sections": 3,
    "ok": true,
    "tags_vs_english": "2/2",
    "localisation_problems": [],
    "not_harvestable": [
      "brackets: 3/5 declared terms are not bracketed with their English word (['right-angled triangle', 'congruent triangles', 'square of a number'])"
    ]
  },
  "terms": [
    "converse of pythagorean theorem",
    "hypotenuse",
    "right-angled triangle",
    "congruent triangles",
    "square of a number"
  ]
}
---

# ପାଇଥାଗୋରାସ୍ ଉପପାଦ୍ୟର ବିପରୀତ (Converse of Pythagorean Theorem)

ଆପଣ ବୋଧହୁଏ ପାଇଥାଗୋରାସ୍ ଉପପାଦ୍ୟ (Pythagorean Theorem) ବିଷୟରେ ଆଗରୁ ଜାଣିଥିବେ। ଏହା କହେ ଯେ ଯଦି ଏକ ତ୍ରିଭୁଜ ସମକୋଣୀ (right-angled) ହୋଇଥାଏ, ଯେଉଁଥିରେ ସବୁଠାରୁ ଲମ୍ବା ବାହୁ $c$ ସମକୋଣର ବିପରୀତ ଦିଗରେ ଥାଏ ଏବଂ ଅନ୍ୟ ଦୁଇଟି ବାହୁ $a$ ଓ $b$ ହୋଇଥାଏ, ତେବେ $a^2 + b^2 = c^2$ ହେବ। ପାଇଥାଗୋରାସ୍ ଉପପାଦ୍ୟର ବିପରୀତ (converse of the Pythagorean Theorem) ଏହି କଥାକୁ ଓଲଟାଇ ଦିଏ। ଏହା କହେ ଯେ ଯଦି ଆପଣ ଏକ ତ୍ରିଭୁଜର ବାହୁଗୁଡ଼ିକୁ ମାପନ୍ତି ଏବଂ ଦେଖନ୍ତି ଯେ $a^2 + b^2 = c^2$, ଯେଉଁଠାରେ $c$ ହେଉଛି ସବୁଠାରୁ ଲମ୍ବା ବାହୁ, ତେବେ ସେହି ତ୍ରିଭୁଜଟି ସମକୋଣୀ ଅଟେ। ଦୈନନ୍ଦିନ ଜୀବନରେ ଏହା ବହୁତ ଉପଯୋଗୀ। ଉଦାହରଣ ସ୍ୱରୂପ, ଜଣେ ବଢ଼େଇ କିମ୍ବା ନିର୍ମାତା ଏକ ତ୍ରିଭୁଜାକାର ଫ୍ରେମ୍‌ର ତିନୋଟି ବାହୁକୁ ମାପି ଏହି ସମୀକରଣକୁ ଯାଞ୍ଚ କରି ଏକ କୋଣ ସମ୍ପୂର୍ଣ୍ଣ ସମକୋଣ କି ନୁହେଁ ତାହା ଜାଣିପାରିବେ।

## ବିପରୀତଟି କଣ କହେ

ପାଇଥାଗୋରାସ୍ ଉପପାଦ୍ୟର ବିପରୀତ ହେଉଛି ତ୍ରିଭୁଜ ବିଷୟରେ ଏକ ନିୟମ। ଏହା କେବଳ ବାହୁଗୁଡ଼ିକୁ ମାପି ଏକ ସମକୋଣୀ ତ୍ରିଭୁଜକୁ କିପରି ଚିହ୍ନଟ କରାଯିବ ତାହା କହିଥାଏ। ଧରିନିଅନ୍ତୁ ଏକ ତ୍ରିଭୁଜର ବାହୁଗୁଡ଼ିକ ହେଉଛି $a$, $b$ ଏବଂ $c$, ଏବଂ $c$ ହେଉଛି ସବୁଠାରୁ ଲମ୍ବା ବାହୁ। ଯଦି $a^2 + b^2 = c^2$ ହୁଏ, ତେବେ ତ୍ରିଭୁଜଟି ସମକୋଣୀ ଅଟେ, ଏବଂ ସମକୋଣଟି ବାହୁ $c$ ର ବିପରୀତ ଦିଗରେ ଥିବା କୋଣ ଅଟେ। ଏକ ସମକୋଣୀ ତ୍ରିଭୁଜରେ, ସମକୋଣର ବିପରୀତ ଦିଗରେ ଥିବା ସବୁଠାରୁ ଲମ୍ବା ବାହୁକୁ କର୍ଣ୍ଣ (hypotenuse) କୁହାଯାଏ।

## ବିପରୀତଟି କାହିଁକି ସତ୍ୟ

ଏକ ତ୍ରିଭୁଜ ABC ନିଅନ୍ତୁ ଯାହାର ବାହୁଗୁଡ଼ିକ $a$, $b$ ଏବଂ $c$ ଅଟେ ଯେପରିକି $a^2 + b^2 = c^2$ ହେବ। ବର୍ତ୍ତମାନ ଏକ ଭିନ୍ନ ତ୍ରିଭୁଜ PQR ଆଙ୍କନ୍ତୁ ଯାହାର Q ଠାରେ ଏକ ସମକୋଣ ଅଛି, ଏବଂ ସମକୋଣ ପାଖରେ ଥିବା ଦୁଇଟି ବାହୁ $a$ ଏବଂ $b$ ସହିତ ସମାନ। ପାଇଥାଗୋରାସ୍ ଉପପାଦ୍ୟ ଅନୁଯାୟୀ, ଏହି ସମକୋଣୀ ତ୍ରିଭୁଜର କର୍ଣ୍ଣ PR, $PR^2 = a^2 + b^2$ କୁ ସନ୍ତୁଷ୍ଟ କରେ। କିନ୍ତୁ $a^2 + b^2 = c^2$, ତେଣୁ $PR^2 = c^2$, ଯାହାର ଅର୍ଥ ହେଉଛି $PR = c$।

ବର୍ତ୍ତମାନ ଦୁଇଟି ତ୍ରିଭୁଜର ତିନୋଟି ଯାକ ବାହୁ ଯୋଡ଼ି ଆକାରରେ ସମାନ: $a$ ଏବଂ $a$, $b$ ଏବଂ $b$, $c$ ଏବଂ $c$। ଯଦି ଗୋଟିଏ ତ୍ରିଭୁଜର ତିନୋଟି ବାହୁ ଅନ୍ୟ ଏକ ତ୍ରିଭୁଜର ତିନୋଟି ବାହୁ ସହିତ ସମାନ ହୁଏ, ତେବେ ସେହି ଦୁଇଟି ତ୍ରିଭୁଜ ସର୍ବସମ (congruent) ଅଟନ୍ତି। ତେଣୁ ତ୍ରିଭୁଜ ABC, ତ୍ରିଭୁଜ PQR ସହିତ ସର୍ବସମ ଅଟେ, ଏବଂ ବାହୁ $c$ ର ବିପରୀତ ଦିଗରେ ଥିବା ତ୍ରିଭୁଜ ABC ର କୋଣ, Q ଠାରେ ଥିବା ସମକୋଣ ସହିତ ସମାନ। ତେଣୁ ତ୍ରିଭୁଜ ABC ସମକୋଣୀ ଅଟେ।

## ଏହି ନିୟମ କିପରି ବ୍ୟବହାର କରିବେ

ଏକ ତ୍ରିଭୁଜ ସମକୋଣୀ କି ନୁହେଁ ତାହା ଯାଞ୍ଚ କରିବା ପାଇଁ ଆପଣ ବିପରୀତ (converse) ର ବ୍ୟବହାର କରିପାରିବେ। ପ୍ରଥମେ, ସବୁଠାରୁ ଲମ୍ବା ବାହୁକୁ ଚିହ୍ନଟ କରନ୍ତୁ। ଏହା ହେଉଛି ଆପଣଙ୍କର $c$। ଅନ୍ୟ ଦୁଇଟି ବାହୁ ହେଉଛି $a$ ଏବଂ $b$। ତା'ପରେ, $a$ ଏବଂ $b$ ର ଲମ୍ବକୁ ବର୍ଗ (square) କରନ୍ତୁ ଏବଂ ଏହି ଦୁଇଟି ବର୍ଗକୁ ଏକାଠି ଯୋଗ କରନ୍ତୁ। ତା'ପରେ $c$ ର ଲମ୍ବକୁ ବର୍ଗ କରନ୍ତୁ। ଯଦି ଦୁଇଟି ଫଳାଫଳ ସମାନ ହୁଏ, ତେବେ ତ୍ରିଭୁଜଟି ସମକୋଣୀ ଅଟେ। ଯଦି ସେଗୁଡ଼ିକ ସମାନ ନୁହେଁ, ତେବେ ତ୍ରିଭୁଜଟି ସମକୋଣୀ ନୁହେଁ। ସବୁଠାରୁ ଲମ୍ବା ବାହୁକୁ $c$ ଭାବରେ ବାଛିବା ଗୁରୁତ୍ୱପୂର୍ଣ୍ଣ, କାରଣ ସବୁଠାରୁ ଲମ୍ବା ବାହୁକୁ ଭିତ୍ତି କରି ହିଁ ଯାଞ୍ଚ କରାଯାଏ।

## ସମାଧାନ କରାଯାଇଥିବା ଉଦାହରଣ

ଭାବନ୍ତୁ ଯେ ଜଣେ ବଢ଼େଇ ଏକ ଝରକା ପାଇଁ ଏକ ତ୍ରିଭୁଜାକାର ଫ୍ରେମ୍ ତିଆରି କରୁଛନ୍ତି। ବାହୁଗୁଡ଼ିକର ଲମ୍ବ ହେଉଛି $6$ ସେ.ମି., $8$ ସେ.ମି. ଏବଂ $10$ ସେ.ମି.। ବଢ଼େଇ ଜାଣିବାକୁ ଚାହୁଁଛନ୍ତି ଯେ ସବୁଠାରୁ ଲମ୍ବା ବାହୁର ବିପରୀତ କୋଣଟି ଏକ ସମ୍ପୂର୍ଣ୍ଣ ସମକୋଣ କି ନୁହେଁ।

ସବୁଠାରୁ ଲମ୍ବା ବାହୁ ହେଉଛି $10$ ସେ.ମି., ତେଣୁ $c = 10$। ଅନ୍ୟ ଦୁଇଟି ବାହୁ ହେଉଛି $6$ ସେ.ମି. ଏବଂ $8$ ସେ.ମି., ତେଣୁ $a = 6$ ଏବଂ $b = 8$।
- $a^2 = 6 \times 6 = 36$
- $b^2 = 8 \times 8 = 64$
- $a^2 + b^2 = 36 + 64 = 100$
- $c^2 = 10 \times 10 = 100$

ଯେହେତୁ $a^2 + b^2 = c^2$, ତେଣୁ ତ୍ରିଭୁଜଟି ସମକୋଣୀ ଅଟେ।

ବର୍ତ୍ତମାନ $5$ ସେ.ମି., $6$ ସେ.ମି. ଏବଂ $8$ ସେ.ମି. ବାହୁ ଥିବା ଏକ ତ୍ରିଭୁଜକୁ ବିଚାର କରନ୍ତୁ। ସବୁଠାରୁ ଲମ୍ବା ବାହୁ ହେଉଛି $8$ ସେ.ମି., ତେଣୁ $c = 8$। ତେବେ $5^2 + 6^2 = 25 + 36 = 61$, ଯେତେବେଳେ କି $8^2 = 64$। ଯେହେତୁ $61 \neq 64$, ଏହି ତ୍ରିଭୁଜଟି ସମକୋଣୀ ନୁହେଁ।

## ମୁଖ୍ୟ ବିନ୍ଦୁ
- ପାଇଥାଗୋରାସ୍ ଉପପାଦ୍ୟର ବିପରୀତ କହେ ଯେ ଯଦି $a^2 + b^2 = c^2$ ହୁଏ, ଯେଉଁଠାରେ $c$ ହେଉଛି ସବୁଠାରୁ ଲମ୍ବା ବାହୁ, ତେବେ ତ୍ରିଭୁଜଟି ସମକୋଣୀ ଅଟେ।
- ସମକୋଣଟି ସବୁଠାରୁ ଲମ୍ବା ବାହୁର ବିପରୀତ ଦିଗରେ ଥାଏ, ଯାହାକି କର୍ଣ୍ଣ (hypotenuse) ଅଟେ।
- ଏକ ତ୍ରିଭୁଜକୁ ଯାଞ୍ଚ କରିବା ପାଇଁ, ଦୁଇଟି ଛୋଟ ବାହୁକୁ ବର୍ଗ କରନ୍ତୁ, ସେଗୁଡ଼ିକୁ ଯୋଗ କରନ୍ତୁ, ଏବଂ ସେହି ଯୋଗଫଳକୁ ସବୁଠାରୁ ଲମ୍ବା ବାହୁର ବର୍ଗ ସହିତ ତୁଳନା କରନ୍ତୁ।
- ଯଦି ଯୋଗଫଳ ସବୁଠାରୁ ଲମ୍ବା ବାହୁର ବର୍ଗ ସହିତ ସମାନ ନୁହେଁ, ତେବେ ତ୍ରିଭୁଜଟି ସମକୋଣୀ ନୁହେଁ।
- ତିନୋଟି ଯୋଡ଼ା ସମାନ ବାହୁ ଥିବା ଦୁଇଟି ତ୍ରିଭୁଜ ସର୍ବସମ (congruent) ଅଟନ୍ତି ବୋଲି ଥିବା ନିୟମ ବ୍ୟବହାର କରି ବିପରୀତଟିକୁ ପ୍ରମାଣ କରାଯାଇପାରିବ।