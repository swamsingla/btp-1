---
{
  "concept": "Zeroes of a Polynomial",
  "slug": "zeroes-of-a-polynomial",
  "grade": 9,
  "language": "od",
  "hand_edited": "2026-10-17: Odia audit against the English page. Polynomial, constant polynomial and linear polynomial were transliterated (palinomiala, kanastanta, liniyara) 42, 4 and 5 times; now bahupadi, sthiranka bahupadi and raikhika bahupadi as on the other Grade 9 Odia pages. 'Variable' was chalarashi (not the term used on the polynomials page), now chalaka. English added in brackets at first use. The zero / root / polynomial-equation distinction is kept as in the English.",
  "subject": "maths",
  "area": "Algebra",
  "model": "sarvam-105b",
  "settings": {
    "temperature": 0.3,
    "max_tokens": 8000,
    "reasoning_effort": "none"
  },
  "usage": {
    "completion_tokens": 1919,
    "prompt_tokens": 2141,
    "total_tokens": 4060,
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
  "generated_at": "2026-10-17T06:09:07",
  "source_grade": 9,
  "grade_delta": 0,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g9_maths_chapter2_012",
      "chapter": "chapter2",
      "section": "2.3 Zeroes of a Polynomial"
    },
    {
      "ref": "S2",
      "passage_id": "g9_maths_chapter2_014",
      "chapter": "chapter2",
      "section": "2.4 Factorisation of Polynomials"
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
    "explanatory_paragraphs_without_a_citation": 0,
    "words": 789,
    "target_words": [
      1000,
      1350
    ],
    "untraceable_sections": 0,
    "ok": true,
    "tags_vs_english": "33/33",
    "localisation_problems": []
  },
  "terms": [
    "polynomial",
    "zero of a polynomial",
    "polynomial equation",
    "root",
    "constant polynomial",
    "zero polynomial",
    "linear polynomial"
  ]
}
---

# ବହୁପଦୀର ଶୂନ୍ୟ

ଏହି ପୃଷ୍ଠାଟି ଏକ ସଂଖ୍ୟାରେ ବହୁପଦୀର (polynomial) ମୂଲ୍ୟ, ଏବଂ ସେହି ସଂଖ୍ୟାଗୁଡ଼ିକୁ ବିଚାର କରେ ଯାହା ପାଇଁ ସେହି ମୂଲ୍ୟ ଶୂନ୍ୟ ଅଟେ। ଏହି ସଂଖ୍ୟାଗୁଡ଼ିକୁ ବହୁପଦୀର ଶୂନ୍ୟ (zeroes) କୁହାଯାଏ।

## ଏକ ସଂଖ୍ୟାରେ ବହୁପଦୀର ମୂଲ୍ୟ

ବହୁପଦୀ $p(x) = 5x^{3} - 2x^{2} + 3x - 2$ କୁ ବିଚାର କରନ୍ତୁ। ଯଦି ଆମେ $p(x)$ ରେ ସବୁ ସ୍ଥାନରେ $x$ କୁ 1 ଦ୍ୱାରା ବଦଳାଇବା, ତେବେ ଆମେ ପାଇବା $p(1) = 5 \times (1)^{3} - 2 \times (1)^{2} + 3 \times (1) - 2 = 5 - 2 + 3 - 2 = 4$। ତେଣୁ ଆମେ କହୁ ଯେ $x = 1$ ରେ $p(x)$ ର ମୂଲ୍ୟ 4 ଅଟେ। ସେହିପରି, $p(0) = 5(0)^{3} - 2(0)^{2} + 3(0) - 2 = -2$।

ଏଠାରେ ଆଉ ତିନୋଟି ଉଦାହରଣ ଅଛି, ଯେଉଁଥିରେ ଚଳକ (variable) ର ଏକ ଦିଆଯାଇଥିବା ମୂଲ୍ୟରେ ବହୁପଦୀର ମୂଲ୍ୟ ଖୋଜାଯାଏ:

*   $x = 1$ ରେ $p(x) = 5x^{2} - 3x + 7$ ପାଇଁ: $p(1) = 5(1)^{2} - 3(1) + 7 = 5 - 3 + 7 = 9$।
*   $y = 2$ ରେ $q(y) = 3y^{3} - 4y + \sqrt{11}$ ପାଇଁ: $q(2) = 3(2)^{3} - 4(2) + \sqrt{11} = 24 - 8 + \sqrt{11} = 16 + \sqrt{11}$।
*   $t = a$ ରେ $p(t) = 4t^4 + 5t^3 - t^2 + 6$ ପାଇଁ: $p(a) = 4a^{4} + 5a^{3} - a^{2} + 6$।

## ବହୁପଦୀର ଶୂନ୍ୟ

ବର୍ତ୍ତମାନ ବହୁପଦୀ $p(x) = x - 1$ କୁ ବିଚାର କରନ୍ତୁ। ଏଠାରେ $p(1) = 1 - 1 = 0$। ଯେହେତୁ $p(1) = 0$, ଆମେ କହୁ ଯେ 1 ହେଉଛି ବହୁପଦୀ $p(x)$ ର ଏକ ଶୂନ୍ୟ। ସେହିପରି, 2 ହେଉଛି $q(x)$ ର ଏକ ଶୂନ୍ୟ, ଯେଉଁଠାରେ $q(x) = x - 2$।

ସାଧାରଣତଃ, ଏକ ବହୁପଦୀ $p(x)$ ର ଶୂନ୍ୟ ହେଉଛି ଏକ ସଂଖ୍ୟା $c$ ଯେପରିକି $p(c) = 0$।

## ଶୂନ୍ୟ ଏବଂ ବହୁପଦୀ ସମୀକରଣ

ବହୁପଦୀ $x - 1$ ର ଶୂନ୍ୟ ଏହାକୁ 0 ସହିତ ସମାନ କରିବା ଦ୍ୱାରା ପ୍ରାପ୍ତ ହୁଏ, ଅର୍ଥାତ୍ $x - 1 = 0$, ଯାହା $x = 1$ ଦେଇଥାଏ। ଆମେ କହୁ $p(x) = 0$ ହେଉଛି ଏକ ବହୁପଦୀ ସମୀକରଣ (polynomial equation), ଏବଂ 1 ହେଉଛି ବହୁପଦୀ ସମୀକରଣ $p(x) = 0$ ର ମୂଳ (root)। ତେଣୁ 1 ହେଉଛି ବହୁପଦୀ $x - 1$ ର ଶୂନ୍ୟ, କିମ୍ବା ବହୁପଦୀ ସମୀକରଣ $x - 1 = 0$ ର ଏକ ମୂଳ।

$p(x)$ ର ଏକ ଶୂନ୍ୟ ଖୋଜିବା ସମୀକରଣ $p(x) = 0$ ର ସମାଧାନ କରିବା ସହିତ ସମାନ। ଉଦାହରଣ ସ୍ୱରୂପ, $p(x) = 2x + 1$ ର ଏକ ଶୂନ୍ୟ ଖୋଜିବା ପାଇଁ, ଆମେ $2x + 1 = 0$ ର ସମାଧାନ କରୁ, ଯାହା $x = -\frac{1}{2}$ ଦେଇଥାଏ। ତେଣୁ $-\frac{1}{2}$ ହେଉଛି ବହୁପଦୀ $2x + 1$ ର ଏକ ଶୂନ୍ୟ।

## ରୈଖିକ ବହୁପଦୀର ଶୂନ୍ୟ

ଧରାଯାଉ $p(x) = ax + b$ ଯେଉଁଠାରେ $a \neq 0$ ଏକ ରୈଖିକ ବହୁପଦୀ (linear polynomial) ଅଟେ। $p(x)$ ର ଏକ ଶୂନ୍ୟ ଖୋଜିବା $p(x) = 0$ ର ସମାଧାନ କରିବା ସହିତ ସମାନ, ଅର୍ଥାତ୍ $a \neq 0$ ସହିତ $ax + b = 0$। ତେବେ $ax = -b$, ତେଣୁ $x = -\frac{b}{a}$। ତେଣୁ $x = -\frac{b}{a}$ ହେଉଛି $p(x)$ ର ଏକମାତ୍ର ଶୂନ୍ୟ, ଯାହାର ଅର୍ଥ ହେଉଛି ଏକ ରୈଖିକ ବହୁପଦୀର ଗୋଟିଏ ଏବଂ କେବଳ ଗୋଟିଏ ଶୂନ୍ୟ ଥାଏ। ଏହିପରି ଭାବରେ 1 ହେଉଛି $x - 1$ ର ଶୂନ୍ୟ, ଏବଂ $-2$ ହେଉଛି $x + 2$ ର ଶୂନ୍ୟ।

## ସ୍ଥିରାଙ୍କ ବହୁପଦୀର ଶୂନ୍ୟ

ସ୍ଥିରାଙ୍କ ବହୁପଦୀ (constant polynomial) 5 କୁ ବିଚାର କରନ୍ତୁ। ଏହାର କୌଣସି ଶୂନ୍ୟ ନାହିଁ, କାରଣ $5x^0$ ରେ $x$ କୁ ଯେକୌଣସି ସଂଖ୍ୟା ଦ୍ୱାରା ବଦଳାଇଲେ ମଧ୍ୟ ଆମକୁ 5 ମିଳେ। ବାସ୍ତବରେ, ଏକ ଅଣ-ଶୂନ୍ୟ ସ୍ଥିରାଙ୍କ ବହୁପଦୀର କୌଣସି ଶୂନ୍ୟ ନାହିଁ। ଶୂନ୍ୟ ବହୁପଦୀ ପାଇଁ, ନିୟମ ଅନୁଯାୟୀ, ପ୍ରତ୍ୟେକ ବାସ୍ତବ ସଂଖ୍ୟା ହେଉଛି ଏକ ଶୂନ୍ୟ।

## ଏକ ସଂଖ୍ୟା ଶୂନ୍ୟ କି ନୁହେଁ ତାହା ଯାଞ୍ଚ କରିବା

$-2$ ଏବଂ 2 ବହୁପଦୀ $x + 2$ ର ଶୂନ୍ୟ କି ନୁହେଁ ତାହା ଯାଞ୍ଚ କରିବାକୁ, ଧରାଯାଉ $p(x) = x + 2$। ତେବେ $p(2) = 2 + 2 = 4$ ଏବଂ $p(-2) = -2 + 2 = 0$। ତେଣୁ $-2$ ହେଉଛି ବହୁପଦୀ $x + 2$ ର ଏକ ଶୂନ୍ୟ, କିନ୍ତୁ 2 ନୁହେଁ।

## ପର୍ଯ୍ୟବେକ୍ଷଣ

ବହୁପଦୀର ଶୂନ୍ୟ ବିଷୟରେ ଆମର ପର୍ଯ୍ୟବେକ୍ଷଣଗୁଡ଼ିକ ହେଉଛି:

*   ଏକ ବହୁପଦୀର ଶୂନ୍ୟ 0 ହେବା ଆବଶ୍ୟକ ନୁହେଁ।
*   0 ଏକ ବହୁପଦୀର ଶୂନ୍ୟ ହୋଇପାରେ।
*   ପ୍ରତ୍ୟେକ ରୈଖିକ ବହୁପଦୀର ଗୋଟିଏ ଏବଂ କେବଳ ଗୋଟିଏ ଶୂନ୍ୟ ଥାଏ।
*   ଏକ ବହୁପଦୀର ଏକାଧିକ ଶୂନ୍ୟ ରହିପାରେ।

## ସମାଧାନ କରାଯାଇଥିବା ଉଦାହରଣ

2 ଏବଂ 0 ବହୁପଦୀ $x^{2} - 2x$ ର ଶୂନ୍ୟ କି ନୁହେଁ ତାହା ଯାଞ୍ଚ କରନ୍ତୁ। ଧରାଯାଉ $p(x) = x^{2} - 2x$। ତେବେ $p(2) = 2^{2} - 4 = 4 - 4 = 0$ ଏବଂ $p(0) = 0 - 0 = 0$। ତେଣୁ 2 ଏବଂ 0 ଉଭୟ ବହୁପଦୀ $x^{2} - 2x$ ର ଶୂନ୍ୟ ଅଟନ୍ତି। ଏହି ବହୁପଦୀ ଦର୍ଶାଏ ଯେ ଏକ ବହୁପଦୀର ଏକାଧିକ ଶୂନ୍ୟ ରହିପାରେ, ଏବଂ 0 ସେଥିମଧ୍ୟରୁ ଗୋଟିଏ ହୋଇପାରେ।

## ମୁଖ୍ୟ ବିନ୍ଦୁ

*   $x = c$ ରେ ଏକ ବହୁପଦୀ $p(x)$ ର ମୂଲ୍ୟ $p(x)$ ରେ ସବୁ ସ୍ଥାନରେ $x$ କୁ $c$ ଦ୍ୱାରା ବଦଳାଇ ମିଳିଥାଏ।
*   ଏକ ବହୁପଦୀ $p(x)$ ର ଶୂନ୍ୟ ହେଉଛି ଏକ ସଂଖ୍ୟା $c$ ଯେପରିକି $p(c) = 0$।
*   $p(x)$ ର ଏକ ଶୂନ୍ୟ ଖୋଜିବା ବହୁପଦୀ ସମୀକରଣ $p(x) = 0$ ର ସମାଧାନ କରିବା ସହିତ ସମାନ।
*   ରୈଖିକ ବହୁପଦୀ $ax + b$, ଯେଉଁଠାରେ $a \neq 0$, ର ଗୋଟିଏ ଏବଂ କେବଳ ଗୋଟିଏ ଶୂନ୍ୟ ଥାଏ, $-\frac{b}{a}$।
*   ଏକ ଅଣ-ଶୂନ୍ୟ ସ୍ଥିରାଙ୍କ ବହୁପଦୀର କୌଣସି ଶୂନ୍ୟ ନଥାଏ, ଏବଂ ନିୟମ ଅନୁଯାୟୀ ପ୍ରତ୍ୟେକ ବାସ୍ତବ ସଂଖ୍ୟା ଶୂନ୍ୟ ବହୁପଦୀର ଏକ ଶୂନ୍ୟ ଅଟେ।
*   ଏକ ବହୁପଦୀର ଏକାଧିକ ଶୂନ୍ୟ ରହିପାରେ।