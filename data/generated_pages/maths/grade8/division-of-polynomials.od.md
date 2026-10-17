---
{
  "concept": "Division of Algebraic Expressions",
  "slug": "division-of-polynomials",
  "grade": 8,
  "language": "od",
  "hand_edited": "2026-10-13: line-by-line hand audit against the English tagged copy, edited directly in both copies: the long-division stopping rule was reversed ('continue until the remainder is NOT zero ...') and now says continue until the remainder is 0 or has a lower power of x than the divisor, 'algebraic expressions' had been worded as 'terms' (title included), 'algebraic identities' had been worded as 'equations' and is now sarbasamika, the divisor word changed from harak (looks like the denominator word) to bhajaka, 'factorise' worded gunaniyakikarana, difference of two squares worded partthakya instead of biyoga, English words inside the formula and the key point replaced, the two fixed headings no longer carry English brackets",
  "subject": "maths",
  "area": "Algebra",
  "model": "sarvam-105b",
  "settings": {
    "temperature": 0.3,
    "max_tokens": 8000,
    "reasoning_effort": "none"
  },
  "usage": {
    "completion_tokens": 1563,
    "prompt_tokens": 1834,
    "total_tokens": 3397,
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
  "generated_at": "2026-10-13T14:21:03",
  "source_grade": 9,
  "grade_delta": 1,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g9_maths_chapter2_022",
      "chapter": "chapter2",
      "section": "2.5 Algebraic Identities"
    },
    {
      "ref": "S2",
      "passage_id": "g9_maths_chapter2_000",
      "chapter": "chapter2",
      "section": "2.1 Introduction"
    },
    {
      "ref": "S3",
      "passage_id": "g9_maths_chapter2_009",
      "chapter": "chapter2",
      "section": "2.3 Zeroes of a Polynomial"
    }
  ],
  "citation_check": {
    "cited": [
      "1"
    ],
    "invented_citations": [],
    "unused_sources": [
      "2",
      "3"
    ],
    "explanatory_paragraphs_without_a_citation": 0,
    "words": 722,
    "target_words": [
      950,
      1300
    ],
    "untraceable_sections": 3,
    "ok": true,
    "tags_vs_english": "4/4",
    "localisation_problems": []
  },
  "terms": [
    "polynomial",
    "monomial",
    "binomial",
    "factorisation",
    "algebraic identity",
    "dividend",
    "divisor",
    "quotient",
    "remainder",
    "long division"
  ]
}
---

# ବୀଜଗାଣିତିକ ଅଭିବ୍ୟକ୍ତିର ହରଣ

ବୀଜଗାଣିତିକ ଅଭିବ୍ୟକ୍ତିଗୁଡ଼ିକୁ ଯୋଗ, ବିୟୋଗ, ଗୁଣନ ଏବଂ ହରଣ କରାଯାଇପାରିବ। ଗୋଟିଏ ବୀଜଗାଣିତିକ ଅଭିବ୍ୟକ୍ତିକୁ ଅନ୍ୟ ଏକ ଅଭିବ୍ୟକ୍ତି ଦ୍ୱାରା ହରଣ କରିବାର ଅର୍ଥ ହେଉଛି ଏପରି ଏକ ଅଭିବ୍ୟକ୍ତି ଖୋଜିବା, ଯାହାକୁ ଭାଜକ (divisor) ସହିତ ଗୁଣିଲେ ଭାଜ୍ୟ (dividend) ଫେରି ପାଇବ। ଏହି କୌଶଳ ଆମକୁ ଅଭିବ୍ୟକ୍ତିଗୁଡ଼ିକୁ ସରଳ କରିବାରେ ଏବଂ ସମୀକରଣଗୁଡ଼ିକୁ ଅଧିକ ସହଜରେ ସମାଧାନ କରିବାରେ ସାହାଯ୍ୟ କରେ। ଏହି ପୃଷ୍ଠାରେ, ଭାଜକ କେବେବି ଶୂନ୍ୟ ନୁହେଁ।

## ଏକ ବହୁପଦୀ (Polynomial) କୁ ଏକପଦୀ (Monomial) ଦ୍ୱାରା ହରଣ କରିବା

ଏକ ବହୁପଦୀକୁ ଏକପଦୀ ଦ୍ୱାରା ହରଣ କରିବାକୁ, ବହୁପଦୀର ପ୍ରତ୍ୟେକ ପଦକୁ ଏକପଦୀ ଦ୍ୱାରା ଅଲଗା ଅଲଗା ହରଣ କରନ୍ତୁ ଏବଂ ତା'ପରେ ଫଳାଫଳଗୁଡ଼ିକୁ ଯୋଗ କରନ୍ତୁ।

ଉଦାହରଣ ସ୍ୱରୂପ, $12x^3 - 6x^2$ କୁ $3x$ ଦ୍ୱାରା ହରଣ କରିବାକୁ, $12x^3$ କୁ $3x$ ଦ୍ୱାରା ହରଣ କରି $4x^2$ ପାଆନ୍ତୁ, ଏବଂ $-6x^2$ କୁ $3x$ ଦ୍ୱାରା ହରଣ କରି $-2x$ ପାଆନ୍ତୁ। ଫଳାଫଳ ହେଉଛି $4x^2 - 2x$।

ଆପଣ ଭାଜକ ସହିତ ଗୁଣନ କରି ଉତ୍ତର ଯାଞ୍ଚ କରିପାରିବେ: $3x \times (4x^2 - 2x) = 12x^3 - 6x^2$, ଯାହା ମୂଳ ବହୁପଦୀ ଅଟେ।

## ଗୋଟିଏ ବହୁପଦୀକୁ ଅନ୍ୟ ଏକ ବହୁପଦୀ ଦ୍ୱାରା ହରଣ କରିବା

ଯେତେବେଳେ ଭାଜକରେ ଏକାଧିକ ପଦ ଥାଏ, ଆପଣ ଦୀର୍ଘ ବିଭାଜନ (long division) ପଦ୍ଧତି ବ୍ୟବହାର କରିପାରିବେ, ଯାହା ସଂଖ୍ୟା ସହିତ ଶିଖିଥିବା ଦୀର୍ଘ ବିଭାଜନ ସହିତ ବହୁତ ସମାନ। ପ୍ରଥମେ ଉଭୟ ବହୁପଦୀକୁ ସେମାନଙ୍କର ପଦଗୁଡ଼ିକ ସହିତ $x$ ର ହ୍ରାସମାନ ଘାତ (decreasing powers) ରେ ଲେଖନ୍ତୁ। ତା'ପରେ ଏହି ପଦକ୍ଷେପଗୁଡ଼ିକୁ ପୁନରାବୃତ୍ତି କରନ୍ତୁ: ଭାଜ୍ୟର ପ୍ରଥମ ପଦକୁ ଭାଜକର ପ୍ରଥମ ପଦ ଦ୍ୱାରା ହରଣ କରନ୍ତୁ, ଫଳାଫଳକୁ ଭାଜକ ସହିତ ଗୁଣନ କରନ୍ତୁ, ଏବଂ ଏହାକୁ ଭାଜ୍ୟରୁ ବିୟୋଗ କରନ୍ତୁ। ଅବଶିଷ୍ଟ (remainder) $0$ ହେବା କିମ୍ବା ଅବଶିଷ୍ଟରେ ଭାଜକ ଅପେକ୍ଷା $x$ ର ଘାତ କମ୍ ହେବା ପର୍ଯ୍ୟନ୍ତ, ବଳକା ଅଂଶ ସହିତ ଏହି ପ୍ରକ୍ରିୟା ଜାରି ରଖନ୍ତୁ।

ଉଦାହରଣ ସ୍ୱରୂପ, ଆସନ୍ତୁ $x^2 + 5x + 6$ କୁ $x + 2$ ଦ୍ୱାରା ହରଣ କରିବା।
- $x^2$ କୁ $x$ ଦ୍ୱାରା ହରଣ କରି $x$ ପାଆନ୍ତୁ।
- $x$ କୁ $x + 2$ ସହିତ ଗୁଣନ କରି $x^2 + 2x$ ପାଆନ୍ତୁ। ଏହାକୁ ଭାଜ୍ୟରୁ ବିୟୋଗ କଲେ $3x + 6$ ବାକି ରହିବ।
- $3x$ କୁ $x$ ଦ୍ୱାରା ହରଣ କରି $3$ ପାଆନ୍ତୁ।
- $3$ କୁ $x + 2$ ସହିତ ଗୁଣନ କରି $3x + 6$ ପାଆନ୍ତୁ। ବିୟୋଗ କଲେ $0$ ର ଅବଶିଷ୍ଟ ରହିବ।

ତେଣୁ ଭାଗଫଳ (quotient) ହେଉଛି $x + 3$ ଏବଂ ଅବଶିଷ୍ଟ ହେଉଛି $0$।

ବେଳେବେଳେ ଅବଶିଷ୍ଟ ଶୂନ୍ୟ ନଥାଏ। ଆସନ୍ତୁ $x^2 + 3x + 5$ କୁ $x + 1$ ଦ୍ୱାରା ହରଣ କରିବା। $x^2$ କୁ $x$ ଦ୍ୱାରା ହରଣ କରି $x$ ପାଆନ୍ତୁ, ତାପରେ $x \times (x + 1) = x^2 + x$, ଏବଂ ବିୟୋଗ କଲେ $2x + 5$ ବାକି ରହିବ। $2x$ କୁ $x$ ଦ୍ୱାରା ହରଣ କରି $2$ ପାଆନ୍ତୁ, ତାପରେ $2 \times (x + 1) = 2x + 2$, ଏବଂ ବିୟୋଗ କଲେ $3$ ବାକି ରହିବ। ଭାଗଫଳ ହେଉଛି $x + 2$ ଏବଂ ଅବଶିଷ୍ଟ ହେଉଛି $3$। ଅବଶିଷ୍ଟ $3$ ରେ କୌଣସି $x$ ନାହିଁ, ତେଣୁ ଆମେ ଆଉ ହରଣ କରିପାରିବା ନାହିଁ।

ଏକ ହରଣ ଯାଞ୍ଚ କରିବାକୁ, ଏହି ସମ୍ପର୍କ ବ୍ୟବହାର କରନ୍ତୁ:
$$ \text{ଭାଜ୍ୟ} = \text{ଭାଜକ} \times \text{ଭାଗଫଳ} + \text{ଅବଶିଷ୍ଟ} $$
ଏଠାରେ $(x + 1)(x + 2) + 3 = x^2 + 3x + 2 + 3 = x^2 + 3x + 5$, ଯାହା ଭାଜ୍ୟ ଅଟେ।

## ହରଣ କରିବା ପାଇଁ ସର୍ବସମିକା (Identities) ର ବ୍ୟବହାର

ବେଳେବେଳେ ଯଦି ଆପଣ ପ୍ରଥମେ ଭାଜ୍ୟକୁ ଗୁଣନୀୟକୀକରଣ (factorise) କରନ୍ତି ତେବେ ହରଣ ସହଜ ହୋଇଯାଏ। ଆପଣ ଏହା କରିବା ପାଇଁ ବୀଜଗାଣିତିକ ସର୍ବସମିକା ବ୍ୟବହାର କରିପାରିବେ। ଉଦାହରଣ ସ୍ୱରୂପ, ଦୁଇଟି ବର୍ଗର ପାର୍ଥକ୍ୟ ପାଇଁ ସର୍ବସମିକା $x^2 - y^2 = (x + y)(x - y)$ ଉପଯୋଗୀ ଅଟେ।

ଆସନ୍ତୁ $x^2 - 9$ କୁ $x + 3$ ଦ୍ୱାରା ହରଣ କରିବା। ଯେହେତୁ $9 = 3^2$, ସର୍ବସମିକାଟି $x^2 - 9 = (x + 3)(x - 3)$ ଦେଇଥାଏ। ତାପରେ
$$ \frac{x^2 - 9}{x + 3} = \frac{(x + 3)(x - 3)}{x + 3} = x - 3 $$
ସାଧାରଣ ଗୁଣନୀୟକ $x + 3$ କଟିଯାଏ, ତେଣୁ ଭାଗଫଳ ହେଉଛି $x - 3$।

ସର୍ବସମିକା $(x + y)^2 = x^2 + 2xy + y^2$ ସମାନ ଭାବରେ କାମ କରେ। ଯେହେତୁ $x^2 + 10x + 25 = (x + 5)^2$, $x^2 + 10x + 25$ କୁ $x + 5$ ଦ୍ୱାରା ହରଣ କଲେ $x + 5$ ମିଳେ।

## ସମାଧାନ କରାଯାଇଥିବା ଉଦାହରଣ

ଆସନ୍ତୁ $10x^2 - 5x$ କୁ $5x$ ଦ୍ୱାରା ହରଣ କରିବା।

ପ୍ରଥମେ, ବହୁପଦୀକୁ ଦୁଇଟି ପଦରେ ବିଭକ୍ତ କରନ୍ତୁ: $\frac{10x^2}{5x}$ ଏବଂ $\frac{-5x}{5x}$।

ତାପରେ, ପ୍ରଥମ ପଦକୁ ହରଣ କରନ୍ତୁ: $\frac{10x^2}{5x} = 2x$।

ତାପରେ, ଦ୍ୱିତୀୟ ପଦକୁ ହରଣ କରନ୍ତୁ: $\frac{-5x}{5x} = -1$।

ଚୂଡ଼ାନ୍ତ ଉତ୍ତର ପାଇବାକୁ ଫଳାଫଳଗୁଡ଼ିକୁ ମିଶାନ୍ତୁ: $2x - 1$।

ଯାଞ୍ଚ: $5x \times (2x - 1) = 10x^2 - 5x$, ଯାହା ମୂଳ ବହୁପଦୀ ଅଟେ।

## ମୁଖ୍ୟ ବିନ୍ଦୁ

*   ଏକ ବହୁପଦୀକୁ ଏକପଦୀ ଦ୍ୱାରା ହରଣ କରିବାକୁ, ବହୁପଦୀର ପ୍ରତ୍ୟେକ ପଦକୁ ଏକପଦୀ ଦ୍ୱାରା ହରଣ କରନ୍ତୁ।
*   ଏକ ବହୁପଦୀକୁ ଅନ୍ୟ ଏକ ବହୁପଦୀ ଦ୍ୱାରା ହରଣ କରିବାକୁ, ଦୀର୍ଘ ବିଭାଜନ ପଦ୍ଧତି ବ୍ୟବହାର କରନ୍ତୁ।
*   ବୀଜଗାଣିତିକ ସର୍ବସମିକା ବ୍ୟବହାର କରି ଗୁଣନୀୟକୀକରଣ କରିବା ହରଣ ପ୍ରକ୍ରିୟାକୁ ସରଳ କରିପାରେ।
*   ସର୍ବଦା ଆପଣଙ୍କର ଉତ୍ତର ଯାଞ୍ଚ କରନ୍ତୁ: ଭାଜ୍ୟ = ଭାଜକ × ଭାଗଫଳ + ଅବଶିଷ୍ଟ।
*   ଏହି ବିଷୟଟି ବୀଜଗାଣିତିକ ଅଭିବ୍ୟକ୍ତିଗୁଡ଼ିକର ଗୁଣନୀୟକୀକରଣ ଉପରେ ଆଧାରିତ, ଯାହା ବୀଜଗାଣିତିକ ସର୍ବସମିକା ବ୍ୟବହାର କରେ।