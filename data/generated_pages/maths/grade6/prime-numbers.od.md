---
{
  "concept": "Prime Numbers",
  "slug": "prime-numbers",
  "grade": 6,
  "language": "od",
  "subject": "maths",
  "area": "Number Theory",
  "model": "sarvam-105b",
  "settings": {
    "temperature": 0.3,
    "max_tokens": 8000,
    "reasoning_effort": "none"
  },
  "usage": {
    "completion_tokens": 1061,
    "prompt_tokens": 1365,
    "total_tokens": 2426,
    "completion_tokens_details": null,
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cached_tokens": 1344
    }
  },
  "target_words": [
    700,
    1250
  ],
  "generated_at": "2026-10-03T03:15:48",
  "source_grade": 7,
  "grade_delta": 1,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g7_maths_part2_chapter3_003",
      "chapter": "chapter3",
      "section": "3.1 The Greatest of All"
    }
  ],
  "citation_check": {
    "cited": [
      "1"
    ],
    "invented_citations": [],
    "unused_sources": [],
    "explanatory_paragraphs_without_a_citation": 0,
    "words": 552,
    "target_words": [
      700,
      1250
    ],
    "untraceable_sections": 0,
    "ok": true,
    "tags_vs_english": "17/17",
    "localisation_problems": [],
    "not_harvestable": [
      "brackets: 4/4 declared terms are not bracketed with their English word (['prime number', 'prime factorisation', 'factors', 'composite factors'])"
    ]
  },
  "terms": [
    "prime number",
    "prime factorisation",
    "factors",
    "composite factors"
  ],
  "hand_edited": "Released on 2026-10-03 after the localisation gate was corrected: formula parity now compares distinct formulas with citation tags and trailing punctuation stripped (it had been comparing multisets and failing on a full stop inside the dollars), and a missing English bracket is now advisory rather than blocking, since it only stops build_glossary.py harvesting the rendering and cannot mislead a reader. Source tags, numbers, formulas, section count and every pinned term were verified on this page."
}
---

# ମୌଳିକ ସଂଖ୍ୟା

ମୌଳିକ ସଂଖ୍ୟାଗୁଡ଼ିକ ହେଉଛି 1 ଠାରୁ ବଡ଼ ସ୍ୱତନ୍ତ୍ର ପୂର୍ଣ୍ଣ ସଂଖ୍ୟା ଯାହାର ଠିକ୍ ଦୁଇଟି ଭିନ୍ନ ଗୁଣନୀୟକ ଥାଏ। କେବଳ 1 ଏବଂ ସେହି ସଂଖ୍ୟା ନିଜେ ଏହାକୁ ସମାନ ଭାବରେ ଭାଗ କରିପାରନ୍ତି। ଏଗୁଡ଼ିକ ଗୁରୁତ୍ୱପୂର୍ଣ୍ଣ କାରଣ ଅନ୍ୟ ପ୍ରତ୍ୟେକ ପୂର୍ଣ୍ଣ ସଂଖ୍ୟା ମୌଳିକ ସଂଖ୍ୟାଗୁଡ଼ିକୁ ଏକାଠି ଗୁଣନ କରି ଗଠନ କରାଯାଇପାରିବ। ଏହା ସେଗୁଡ଼ିକୁ ସମସ୍ତ ସଂଖ୍ୟାର ମୂଳ ଆଧାର କରିଥାଏ।

## ଏକ ସଂଖ୍ୟାକୁ କ'ଣ ମୌଳିକ କରେ
ଏକ ମୌଳିକ ସଂଖ୍ୟା ହେଉଛି 1 ଠାରୁ ବଡ଼ ଏକ ସଂଖ୍ୟା ଯାହାର କେବଳ 1 ଏବଂ ସେହି ସଂଖ୍ୟା ନିଜେ ଏହାର ଗୁଣନୀୟକ ଅଟେ। ଉଦାହରଣ ସ୍ୱରୂପ, 7 ହେଉଛି ଏକ ମୌଳିକ ସଂଖ୍ୟା। କେବଳ 1 ଏବଂ 7 ହିଁ 7 କୁ ସମାନ ଭାବରେ ଭାଗ କରିପାରିବେ। 4 ସଂଖ୍ୟାଟି ଏକ ମୌଳିକ ସଂଖ୍ୟା ନୁହେଁ କାରଣ ଏହାକୁ 1, 2, ଏବଂ 4 ଦ୍ୱାରା ସମାନ ଭାବରେ ଭାଗ କରାଯାଇପାରିବ। ଯେହେତୁ 4 ର ଦୁଇଟିରୁ ଅଧିକ ଗୁଣନୀୟକ ଅଛି, ଏହା ମୌଳିକ ନୁହେଁ। 2 ହେଉଛି ଏକମାତ୍ର ଯୁଗ୍ମ ମୌଳିକ ସଂଖ୍ୟା।

## ମୌଳିକ ଗୁଣନୀୟକରଣ

ମୌଳିକ ଗୁଣନୀୟକରଣ ହେଉଛି ଏକ ସଂଖ୍ୟାକୁ ମୌଳିକ ସଂଖ୍ୟାଗୁଡ଼ିକର ଗୁଣଫଳ ଭାବରେ ଭାଙ୍ଗିବା ପ୍ରକ୍ରିୟା। କେବଳ ମୌଳିକ ସଂଖ୍ୟା ବାକି ରହିବା ପର୍ଯ୍ୟନ୍ତ ଆପଣ ଯୌଗିକ ଗୁଣନୀୟକଗୁଡ଼ିକୁ ପୁନର୍ବାର ଲେଖିବା ଜାରି ରଖନ୍ତି। ଉଦାହରଣ ସ୍ୱରୂପ, 90 ସଂଖ୍ୟାକୁ ମୌଳିକ ଗୁଣନୀୟକରେ ଭାଙ୍ଗି ଦିଆଯାଇପାରିବ। ଆମେ 90 କୁ $3 \times 3 \times 2 \times 5$ ଭାବରେ ଲେଖିପାରିବା। 90 ସଂଖ୍ୟାକୁ $3 \times 30$ କିମ୍ବା $2 \times 45$ ଭାବରେ ମଧ୍ୟ ଗୁଣନୀୟକରଣ କରାଯାଇପାରିବ। ଆଶ୍ଚର୍ଯ୍ୟଜନକ ଭାବରେ, ଫଳାଫଳ ମୌଳିକ ଗୁଣନୀୟକଗୁଡ଼ିକ ସର୍ବଦା ସମାନ ରହିଥାଏ, ବୋଧହୁଏ କେବଳ ସେମାନଙ୍କର କ୍ରମ ପରିବର୍ତ୍ତନ ହୋଇଥାଏ। ଉଦାହରଣ ସ୍ୱରୂପ, ଯଦି ଆମେ $3 \times 30$ କୁ ଆହୁରି ଗୁଣନୀୟକରଣ କରିବାକୁ ବିଚାର କରୁ, ତେବେ ଆମେ ପାଇବା $90 = 3 \times 30 = 3 \times 2 \times 15 = 3 \times 2 \times 3 \times 5$। ଆମେ ସମାନ ମୌଳିକ ଗୁଣନୀୟକରେ ପହଞ୍ଚିଛୁ, କେବଳ ଏକ ଭିନ୍ନ କ୍ରମରେ। ଧ୍ୟାନ ଦିଅନ୍ତୁ ଯେ ଏକ ମୌଳିକ ସଂଖ୍ୟାର ମୌଳିକ ଗୁଣନୀୟକରଣ ହେଉଛି ସେହି ମୌଳିକ ସଂଖ୍ୟା ନିଜେ।

## ଗୁଣନୀୟକ ଖୋଜିବା ପାଇଁ ମୌଳିକ ଗୁଣନୀୟକରଣର ବ୍ୟବହାର

ଏକ ସଂଖ୍ୟାର ମୌଳିକ ଗୁଣନୀୟକରଣରୁ, ଆମେ ଏହାର ସମସ୍ତ ଗୁଣନୀୟକ ଗଠନ କରିପାରିବା। ସେହି ଗୁଣନୀୟକରଣର ଯେକୌଣସି 'ଉପ-ଅଂଶ' — ସେହି ମୌଳିକ ଗୁଣନୀୟକଗୁଡ଼ିକର ଯେକୌଣସି ସମୂହକୁ ଏକାଠି ଗୁଣନ କରାଯାଇଥିବା — ସେହି ସଂଖ୍ୟାର ଏକ ଗୁଣନୀୟକ ଅଟେ।

840 ସଂଖ୍ୟାକୁ ବିଚାର କରନ୍ତୁ, ଯାହାର ମୌଳିକ ଗୁଣନୀୟକରଣ ହେଉଛି $2 \times 2 \times 2 \times 3 \times 5 \times 7$। ଥରକେ ଗୋଟିଏ ମୌଳିକ ସଂଖ୍ୟା ନେଲେ 2, 3, 5 ଏବଂ 7 ଗୁଣନୀୟକ ମିଳେ। ଥରକେ ଦୁଇଟି ନେଲେ $2 \times 2 = 4$, $2 \times 3 = 6$, $3 \times 5 = 15$ ଏବଂ $5 \times 7 = 35$ ଭଳି ଗୁଣନୀୟକ ମିଳେ। ଥରକେ ତିନୋଟି ନେଲେ $2 \times 2 \times 2 = 8$, $2 \times 3 \times 5 = 30$ ଏବଂ $3 \times 5 \times 7 = 105$ ମିଳେ। ଛଅଟି ଯାକ ନେଲେ 840 ନିଜେ ମିଳେ, ଏବଂ ଗୋଟିଏ ବି ନନେଲେ 1 ମିଳେ, ଯାହା ପ୍ରତ୍ୟେକ ସଂଖ୍ୟାର ଏକ ଗୁଣନୀୟକ ଅଟେ।

ଏକ ଛୋଟ ସଂଖ୍ୟା ସହିତ ଆମେ ଏହି ଉପାୟରେ ପ୍ରତ୍ୟେକ ଗୁଣନୀୟକକୁ ନଛାଡ଼ି ତାଲିକାଭୁକ୍ତ କରିପାରିବା। 225 ର ମୌଳିକ ଗୁଣନୀୟକରଣ ହେଉଛି $3 \times 3 \times 5 \times 5$। ଥରକେ ଗୋଟିଏ ମୌଳିକ ସଂଖ୍ୟା ନେଲେ 3 ଏବଂ 5 ମିଳେ। ଥରକେ ଦୁଇଟି ନେଲେ $3 \times 3 = 9$, $3 \times 5 = 15$ ଏବଂ $5 \times 5 = 25$ ମିଳେ। ଥରକେ ତିନୋଟି ନେଲେ $3 \times 3 \times 5 = 45$ ଏବଂ $3 \times 5 \times 5 = 75$ ମିଳେ। ଚାରୋଟି ଯାକ ନେଲେ $3 \times 3 \times 5 \times 5 = 225$ ମିଳେ। ଏହି ତାଲିକାରେ 1 ଯୋଗ କଲେ, 225 ର ଗୁଣନୀୟକଗୁଡ଼ିକ ହେଉଛି 1, 3, 5, 9, 15, 25, 45, 75 ଏବଂ 225।

## ସମାଧାନ କରାଯାଇଥିବା ଉଦାହରଣ
ଆସନ୍ତୁ 30 ସଂଖ୍ୟାର ମୌଳିକ ଗୁଣନୀୟକରଣ ଖୋଜିବା। ଆମେ ହରଣ ପଦ୍ଧତି ବ୍ୟବହାର କରିପାରିବା। ଆମେ 30 କୁ ସବୁଠାରୁ ଛୋଟ ମୌଳିକ ସଂଖ୍ୟା, ଯାହାକି 2, ଦ୍ୱାରା ଭାଗ କରୁ। ଏହା ଆମକୁ 15 ଦେଇଥାଏ। ତାପରେ ଆମେ 15 କୁ ପରବର୍ତ୍ତୀ ସବୁଠାରୁ ଛୋଟ ମୌଳିକ ସଂଖ୍ୟା, ଯାହାକି 3, ଦ୍ୱାରା ଭାଗ କରୁ। ଏହା ଆମକୁ 5 ଦେଇଥାଏ। ଆମେ ଏକ ମୌଳିକ ସଂଖ୍ୟାରେ ପହଞ୍ଚିବା ପରେ ଅଟକିଯାଉ। 30 ର ମୌଳିକ ଗୁଣନୀୟକରଣ ହେଉଛି $2 \times 3 \times 5$।

## ମୁଖ୍ୟ ବିନ୍ଦୁ
- ଏକ ମୌଳିକ ସଂଖ୍ୟା ହେଉଛି 1 ଠାରୁ ବଡ଼ ଏକ ସଂଖ୍ୟା ଯାହାର କେବଳ 1 ଏବଂ ସେହି ସଂଖ୍ୟା ନିଜେ ଏହାର ଗୁଣନୀୟକ ଅଟେ।
- ମୌଳିକ ଗୁଣନୀୟକରଣ ହେଉଛି ଏକ ସଂଖ୍ୟାକୁ ମୌଳିକ ସଂଖ୍ୟାଗୁଡ଼ିକର ଗୁଣଫଳ ଭାବରେ ଭାଙ୍ଗିବା ପ୍ରକ୍ରିୟା।
- ଫଳାଫଳ ମୌଳିକ ଗୁଣନୀୟକଗୁଡ଼ିକ ସର୍ବଦା ସମାନ ରହିଥାଏ, ବୋଧହୁଏ କେବଳ ସେମାନଙ୍କର କ୍ରମ ପରିବର୍ତ୍ତନ ହୋଇଥାଏ।
- ଏକ ସଂଖ୍ୟାର ମୌଳିକ ଗୁଣନୀୟକରଣରୁ, ଆମେ ଏହାର ସମସ୍ତ ଗୁଣନୀୟକ ଗଠନ କରିପାରିବା।
- ଏକ ମୌଳିକ ସଂଖ୍ୟାର ମୌଳିକ ଗୁଣନୀୟକରଣ ହେଉଛି ସେହି ମୌଳିକ ସଂଖ୍ୟା ନିଜେ।