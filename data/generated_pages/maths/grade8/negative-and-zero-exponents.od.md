---
{
  "concept": "Negative and Zero Exponents",
  "slug": "negative-and-zero-exponents",
  "grade": 8,
  "language": "od",
  "hand_edited": "2026-10-13: line-by-line hand audit against the English page, edited directly (tagged copy; published body rebuilt from it): power/exponent terms separated, transliterated base/reciprocal/expression replaced, units",
  "subject": "maths",
  "area": "Algebra",
  "model": "sarvam-105b",
  "settings": {
    "temperature": 0.3,
    "max_tokens": 8000,
    "reasoning_effort": "none"
  },
  "usage": {
    "completion_tokens": 1224,
    "prompt_tokens": 1579,
    "total_tokens": 2803,
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
  "generated_at": "2026-10-13T01:20:14",
  "source_grade": 8,
  "grade_delta": 0,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g8_maths_part1_chapter6_025",
      "chapter": "chapter6",
      "section": "6.3 Mind the Mistake, Mend the Mistake"
    },
    {
      "ref": "S2",
      "passage_id": "g8_maths_part1_chapter2_005",
      "chapter": "chapter2",
      "section": "2.2 Exponential Notation and Operations"
    },
    {
      "ref": "S3",
      "passage_id": "g8_maths_part1_chapter2_015",
      "chapter": "chapter2",
      "section": "2.3 The Other Side of Powers"
    }
  ],
  "citation_check": {
    "cited": [
      "2",
      "3"
    ],
    "invented_citations": [],
    "unused_sources": [
      "1"
    ],
    "explanatory_paragraphs_without_a_citation": 0,
    "words": 541,
    "target_words": [
      950,
      1300
    ],
    "untraceable_sections": 0,
    "ok": true,
    "tags_vs_english": "14/14",
    "localisation_problems": []
  },
  "terms": [
    "exponents",
    "powers",
    "base",
    "exponent",
    "standard form",
    "scientific notation",
    "laws of exponents"
  ]
}
---

# ଶୂନ୍ୟ ଏବଂ ଋଣାତ୍ମକ ଘାତାଙ୍କ

ଏହି ଅଧ୍ୟାୟର ପୂର୍ବରୁ ଆପଣ ଘାତାଙ୍କ (exponents) ଏବଂ ଘାତ (powers) ବିଷୟରେ ଶିଖିଥିଲେ। ଆପଣ ଜାଣନ୍ତି ଯେ $5^4$ ର ଅର୍ଥ ହେଉଛି 5 କୁ ନିଜ ସହିତ 4 ଥର ଗୁଣିବା, ଯାହା 625 ସହ ସମାନ। ଘାତାଙ୍କଗୁଡ଼ିକ ଗଣନ ସଂଖ୍ୟା (counting numbers) ହୋଇଥିଲେ, ଘାତାଙ୍କର ନିୟମ (laws of exponents) ବ୍ୟବହାର କରି ଘାତଗୁଡ଼ିକୁ କିପରି ଗୁଣିବେ ଏବଂ ଭାଗ କରିବେ ତାହା ମଧ୍ୟ ଆପଣ ଜାଣନ୍ତି। ତେବେ, ଯେତେବେଳେ ଆପଣଙ୍କୁ ଏକ ଛୋଟ ଘାତକୁ ଏକ ବଡ଼ ଘାତ ଦ୍ୱାରା ଭାଗ କରିବାକୁ ପଡ଼େ, କିମ୍ବା ଏକ ସଂଖ୍ୟାକୁ ନିଜ ଦ୍ୱାରା ଭାଗ କରାଯାଏ, ସେତେବେଳେ କ'ଣ ହୁଏ? ଏହି ପୃଷ୍ଠା ଏହି ପ୍ରଶ୍ନଗୁଡ଼ିକର ଉତ୍ତର ଖୋଜେ ଏବଂ ଆପଣଙ୍କୁ ଶୂନ୍ୟ ଓ ଋଣାତ୍ମକ ଘାତାଙ୍କ ସହିତ ପରିଚିତ କରାଏ।

## ଶୂନ୍ୟ ଘାତାଙ୍କର ନିୟମ

ଆପଣ ଆଗରୁ ଜାଣିଛନ୍ତି ଯେ $x^a \times x^b = x^{a+b}$ ଏବଂ $x^a \div x^b = x^{a-b}$। କିନ୍ତୁ ଘାତାଙ୍କଗୁଡ଼ିକ ସମାନ ହେଲେ କ'ଣ ହୁଏ? ଯଦି ଆପଣ $2^4$ କୁ $2^4$ ଦ୍ୱାରା ଭାଗ କରନ୍ତି, ତେବେ ଆପଣ 1 ପାଆନ୍ତି, କାରଣ ଉପର ଏବଂ ତଳ କଟିଯାଏ। ଘାତାଙ୍କର ନିୟମ ବ୍ୟବହାର କରି, $2^4 \div 2^4 = 2^{4-4} = 2^0$। ଏହାର ଅର୍ଥ $2^0$ ନିଶ୍ଚିତ ଭାବରେ 1 ସହ ସମାନ। ଏହି ନିୟମ ଶୂନ୍ୟ ନୁହେଁ ଏପରି ଯେକୌଣସି ଆଧାର (base) $x$ ଏବଂ ଯେକୌଣସି ଗଣନ ସଂଖ୍ୟା $a$ ପାଇଁ ସତ୍ୟ, ତେଣୁ $x^a \div x^a = x^0 = 1$, ଯେଉଁଠାରେ $x \neq 0$।

## ଋଣାତ୍ମକ ଘାତାଙ୍କର ନିୟମ

ଯଦି ଆପଣ $2^4$ କୁ $2^5$ ଦ୍ୱାରା ଭାଗ କରନ୍ତି ତେବେ କ'ଣ ହୁଏ? ଯଦି ଆପଣ ଏହାକୁ ବିସ୍ତାର କରନ୍ତି, ତେବେ ଆପଣ $\frac{2 \times 2 \times 2 \times 2}{2 \times 2 \times 2 \times 2 \times 2}$ ପାଆନ୍ତି, ଯାହା ସରଳ ହୋଇ $\frac{1}{2}$, ଅର୍ଥାତ୍ $\frac{1}{2^1}$ ହୁଏ। ଘାତାଙ୍କର ନିୟମ ବ୍ୟବହାର କରି, $2^4 \div 2^5 = 2^{4-5} = 2^{-1}$। ତେଣୁ, $2^{-1} = \frac{1}{2}$। ଯେକୌଣସି ଋଣାତ୍ମକ ଘାତାଙ୍କ ପାଇଁ ସମାନ ଯୁକ୍ତି ଲାଗୁ ହୁଏ: $10^{-3} = \frac{1}{10^3}$, $7^{-2} = \frac{1}{7^2}$, ଏବଂ $2^{-6} = \frac{1}{2^6}$। ସାଧାରଣତଃ, ଶୂନ୍ୟ ନୁହେଁ ଏପରି ଯେକୌଣସି ଆଧାର $n$ ଏବଂ ଧନାତ୍ମକ ପୂର୍ଣ୍ଣସଂଖ୍ୟା $a$ ପାଇଁ, $n^{-a} = \frac{1}{n^a}$। ନିୟମଟି ଓଲଟା ଭାବରେ ମଧ୍ୟ କାମ କରେ: $10^3 = \frac{1}{10^{-3}}$ ଏବଂ $7^2 = \frac{1}{7^{-2}}$।

## ମାନକ ରୂପ ଏବଂ ବୈଜ୍ଞାନିକ ସଙ୍କେତ

ସଂଖ୍ୟାଗୁଡ଼ିକ ବହୁତ ବଡ଼ କିମ୍ବା ବହୁତ ଛୋଟ ହେଲେ, ସେଗୁଡ଼ିକୁ ପୂରା ଲେଖିବା କଷ୍ଟକର ହୋଇଯାଏ। ଉଦାହରଣ ସ୍ୱରୂପ, ଏକ କାଗଜ ଖଣ୍ଡର ପ୍ରାରମ୍ଭିକ ମୋଟେଇ $0.001$ ସେ.ମି. ହୋଇପାରେ। ପ୍ରତ୍ୟେକ ଭାଙ୍ଗରେ ମୋଟେଇ ଦ୍ୱିଗୁଣିତ ହୁଏ, ତେଣୁ ଯଦି ଆପଣ ଏହାକୁ 7 ଥର ଭାଙ୍ଗନ୍ତି, ତେବେ ମୋଟେଇ $0.001 \times 2^7 = 0.128$ ସେ.ମି. ହୋଇଯାଏ। ମାନକ ରୂପ (standard form), ଅର୍ଥାତ୍ ବୈଜ୍ଞାନିକ ସଙ୍କେତ (scientific notation), ଆମକୁ ଏହି ସଂଖ୍ୟାଗୁଡ଼ିକୁ ସହଜରେ ଲେଖିବାରେ ସାହାଯ୍ୟ କରେ। ଆମେ $0.001$ କୁ $1 \times 10^{-3}$ ଭାବରେ ଲେଖୁ। ଏହାର କାରଣ $10^{-3} = \frac{1}{10^3} = \frac{1}{1000} = 0.001$। ତେଣୁ, 7 ଥର ଭାଙ୍ଗିବା ପରେ ମୋଟେଇ ହେଉଛି $1 \times 10^{-3} \times 2^7$ ସେ.ମି., ଯାହା ମାନକ ରୂପରେ $1.28 \times 10^{-1}$ ସେ.ମି. ଅଟେ।

## ସମାଧାନ କରାଯାଇଥିବା ଉଦାହରଣ

ଆସନ୍ତୁ ଏହି ନିୟମଗୁଡ଼ିକୁ ଏକ ସମସ୍ୟାରେ ପ୍ରୟୋଗ କରିବା। ଧରିନିଅନ୍ତୁ ଆମକୁ $2^3 \times 2^{-5}$ ରାଶିକୁ ସରଳ କରିବାକୁ ପଡ଼ିବ। ଘାତାଙ୍କର ନିୟମ ବ୍ୟବହାର କରି, ଆମେ ଘାତାଙ୍କଗୁଡ଼ିକୁ ଯୋଗ କରୁ: $2^{3 + (-5)} = 2^{-2}$। ଯେହେତୁ ଆମ ପାଖରେ ଏକ ଋଣାତ୍ମକ ଘାତାଙ୍କ ଅଛି, ଆମେ ବ୍ୟୁତ୍କ୍ରମ (reciprocal) ନେଇ ଏହାକୁ ଏକ ଧନାତ୍ମକ ଘାତାଙ୍କରେ ପରିଣତ କରୁ: $2^{-2} = \frac{1}{2^2} = \frac{1}{4}$।

## ମୁଖ୍ୟ ବିନ୍ଦୁ
- ଶୂନ୍ୟ ଘାତରେ ଥିବା ଶୂନ୍ୟ ନୁହେଁ ଏପରି ଯେକୌଣସି ସଂଖ୍ୟା 1 ସହ ସମାନ ହୁଏ: $x^0 = 1$, ଯେଉଁଠାରେ $x \neq 0$।
- ଏକ ଋଣାତ୍ମକ ଘାତାଙ୍କର ଅର୍ଥ ହେଉଛି ଆଧାରକୁ ଧନାତ୍ମକ ଘାତାଙ୍କରେ ଉଠାଇ ତାହାର ବ୍ୟୁତ୍କ୍ରମ ନେବା: $n^{-a} = \frac{1}{n^a}$, ଯେଉଁଠାରେ $n \neq 0$।
- ବହୁତ ବଡ଼ କିମ୍ବା ବହୁତ ଛୋଟ ସଂଖ୍ୟାଗୁଡ଼ିକୁ ସହଜରେ ଲେଖିବା ପାଇଁ ମାନକ ରୂପ 10 ର ଘାତ ବ୍ୟବହାର କରେ।
- ଶୂନ୍ୟ ଏବଂ ଋଣାତ୍ମକ ଘାତାଙ୍କ ବ୍ୟବହାର କଲେ ମଧ୍ୟ ଘାତାଙ୍କର ନିୟମ ଲାଗୁ ହୁଏ।
