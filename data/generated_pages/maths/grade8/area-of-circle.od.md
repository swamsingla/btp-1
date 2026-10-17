---
{
  "concept": "Area of a Circle",
  "slug": "area-of-circle",
  "grade": 8,
  "language": "od",
  "subject": "maths",
  "area": "Mensuration",
  "model": "sarvam-105b",
  "settings": {
    "temperature": 0.3,
    "max_tokens": 8000,
    "reasoning_effort": "none"
  },
  "usage": {
    "completion_tokens": 796,
    "prompt_tokens": 1188,
    "total_tokens": 1984,
    "completion_tokens_details": {
      "accepted_prediction_tokens": null,
      "audio_tokens": null,
      "reasoning_tokens": 0,
      "rejected_prediction_tokens": null
    },
    "prompt_tokens_details": null
  },
  "target_words": [
    700,
    1250
  ],
  "generated_at": "2026-10-11T05:50:30",
  "source_grade": 8,
  "grade_delta": 0,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g8_maths_part1_chapter6_029",
      "chapter": "chapter6",
      "section": "6.4 This Way or That Way, All Ways Lead to the Bay"
    },
    {
      "ref": "S2",
      "passage_id": "g8_maths_part2_chapter2_004",
      "chapter": "chapter2",
      "section": "2.3 Hypotenuse of an Isosceles Right Triangle"
    },
    {
      "ref": "S3",
      "passage_id": "g8_maths_part2_chapter7_001",
      "chapter": "chapter7",
      "section": "7.1 Rectangle and Squares"
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
    "words": 383,
    "target_words": [
      700,
      1250
    ],
    "untraceable_sections": 2,
    "ok": true,
    "tags_vs_english": "4/4",
    "localisation_problems": [],
    "not_harvestable": [
      "brackets: 7/7 declared terms are not bracketed with their English word (['area', 'radius', 'pi', 'formula'])"
    ]
  },
  "terms": [
    "area",
    "radius",
    "pi",
    "formula",
    "square",
    "unit square",
    "non-terminating decimal"
  ],
  "hand_edited": "2026-10-12: moved from Grade 7 to Grade 8 — it was written from Grade 8 textbook text. Content unchanged apart from grade labels."
}
---

# ବୃତ୍ତର କ୍ଷେତ୍ରଫଳ

ଆପଣ ଆଗରୁ ଆୟତକ୍ଷେତ୍ର ଏବଂ ବର୍ଗକ୍ଷେତ୍ରର କ୍ଷେତ୍ରଫଳ କିପରି ବାହାର କରାଯାଏ ତାହା ଜାଣିଛନ୍ତି। ଆୟତକ୍ଷେତ୍ରର କ୍ଷେତ୍ରଫଳ ହେଉଛି ଏହାର ଲମ୍ବ ଏବଂ ପ୍ରସ୍ଥର ଗୁଣଫଳ। ବର୍ଗକ୍ଷେତ୍ର ପାଇଁ, ଆପଣ କେବଳ ଏହାର ବାହୁକୁ ନିଜ ସହିତ ଗୁଣନ କରିବେ। ଗୋଟିଏ ବୃତ୍ତ ଗୋଲାକାର, ତେଣୁ ଏହାର କ୍ଷେତ୍ରଫଳ କିପରି ମାପିବେ ତାହା ଭାବିବା ସ୍ୱାଭାବିକ। ଏକ ବୃତ୍ତ ଦ୍ୱାରା ଆବଦ୍ଧ ସ୍ଥାନର କ୍ଷେତ୍ରଫଳ ବାହାର କରିବା ପାଇଁ ଆମେ ଏକ ସ୍ୱତନ୍ତ୍ର ସୂତ୍ର ବ୍ୟବହାର କରୁ।

## ସୂତ୍ର ଏବଂ ପାଇ (Pi) ର ମୂଲ୍ୟ

ବୃତ୍ତର କ୍ଷେତ୍ରଫଳ $A = \pi r^2$ ସୂତ୍ର ବ୍ୟବହାର କରି ହିସାବ କରାଯାଏ, ଯେଉଁଠାରେ $A$ ହେଉଛି କ୍ଷେତ୍ରଫଳ, $\pi$ (pi) ହେଉଛି ଏକ ସ୍ୱତନ୍ତ୍ର ସ୍ଥିରାଙ୍କ, ଏବଂ $r$ ହେଉଛି ବ୍ୟାସାର୍ଦ୍ଧ। ବ୍ୟାସାର୍ଦ୍ଧ ହେଉଛି ବୃତ୍ତର କେନ୍ଦ୍ରରୁ ଏହାର ଧାରରେ ଥିବା ଯେକୌଣସି ବିନ୍ଦୁ ପର୍ଯ୍ୟନ୍ତ ଦୂରତା। $\pi$ ର ମୂଲ୍ୟ ପ୍ରାୟ $3.14159...$ ଅଟେ, ଏବଂ ଏହା ଏକ ଅଣ-ସମାପ୍ତ ଦଶମିକ। ଯେହେତୁ $\pi$ ଏକ ଅପରିମେୟ ସଂଖ୍ୟା, ବିଦ୍ୟାଳୟରେ ହିସାବ କରିବା ସମୟରେ ଆମେ ଏହାକୁ ପ୍ରାୟତଃ $3.14$ କୁ ରାଉଣ୍ଡ୍ (round) କରିଥାଉ।

## ବ୍ୟାସାର୍ଦ୍ଧର ବର୍ଗ କରିବା

ସୂତ୍ରର $r^2$ ଅଂଶର ଅର୍ଥ ହେଉଛି ଆପଣଙ୍କୁ ବ୍ୟାସାର୍ଦ୍ଧକୁ ନିଜ ସହିତ ଗୁଣନ କରିବାକୁ ପଡିବ। ଏହାକୁ ବ୍ୟାସାର୍ଦ୍ଧର ବର୍ଗ କରିବା କୁହାଯାଏ। ଏହି ପଦକ୍ଷେପଟି ଅତ୍ୟନ୍ତ ଗୁରୁତ୍ୱପୂର୍ଣ୍ଣ କାରଣ ବୃତ୍ତର କ୍ଷେତ୍ରଫଳ ଏହାର ବ୍ୟାସାର୍ଦ୍ଧର ବର୍ଗ ସହିତ ବଢିଥାଏ — ଯଦି ଆପଣ ବ୍ୟାସାର୍ଦ୍ଧକୁ ଦୁଇଗୁଣ କରନ୍ତି, ତେବେ କ୍ଷେତ୍ରଫଳ କେବଳ ଦୁଇଗୁଣ ହୁଏ ନାହିଁ, ବରଂ ଏହା ଚାରିଗୁଣ ବଡ଼ ହୋଇଯାଏ। 

କ୍ଷେତ୍ରଫଳ ବାହାର କରିବା ପାଇଁ, ଆପଣ ଏହି ବର୍ଗ ହୋଇଥିବା ବ୍ୟାସାର୍ଦ୍ଧକୁ $\pi$ ସହିତ ଗୁଣନ କରନ୍ତି। ଯଦି ବ୍ୟାସାର୍ଦ୍ଧ ସେଣ୍ଟିମିଟରରେ ଦିଆଯାଇଥାଏ, ତେବେ କ୍ଷେତ୍ରଫଳ ବର୍ଗ ସେଣ୍ଟିମିଟର ($cm^2$) ରେ ହେବ। ଉଦାହରଣ ସ୍ୱରୂପ, ଯଦି ଆପଣଙ୍କ ପାଖରେ 5 cm ବ୍ୟାସାର୍ଦ୍ଧ ବିଶିଷ୍ଟ ଏକ ଗୋଲାକାର ପିଜ୍ଜା ଅଛି, ତେବେ ଆପଣ ପ୍ରଥମେ 25 ପାଇବା ପାଇଁ 5 ର ବର୍ଗ କରନ୍ତି। ତାପରେ, ପିଜ୍ଜାର କ୍ଷେତ୍ରଫଳ ବାହାର କରିବା ପାଇଁ ଆପଣ 25 କୁ $3.14$ ସହିତ ଗୁଣନ କରନ୍ତି।

## ସମାଧାନ କରାଯାଇଥିବା ଉଦାହରଣ

ଆସନ୍ତୁ 10 cm ବ୍ୟାସାର୍ଦ୍ଧ ବିଶିଷ୍ଟ ଏକ ବୃତ୍ତର କ୍ଷେତ୍ରଫଳ ବାହାର କରିବା। ପ୍ରଥମେ, ଆମେ ବ୍ୟାସାର୍ଦ୍ଧ ଚିହ୍ନଟ କରୁ, ଯାହା ହେଉଛି $r = 10$। ପରବର୍ତ୍ତୀ ସମୟରେ, ଆମେ ବ୍ୟାସାର୍ଦ୍ଧର ବର୍ଗ କରୁ: $r^2 = 10^2 = 100$। ଶେଷରେ, ଆମେ ଏହି ଫଳାଫଳକୁ $\pi$ ସହିତ ଗୁଣନ କରୁ। $\pi$ ପାଇଁ $3.14$ ବ୍ୟବହାର କରି, କ୍ଷେତ୍ରଫଳ ହେଉଛି $3.14 \times 100 = 314$। ତେଣୁ, ବୃତ୍ତର କ୍ଷେତ୍ରଫଳ ହେଉଛି $314 \, cm^2$।

## ମୁଖ୍ୟ ବିନ୍ଦୁ

- ବୃତ୍ତର କ୍ଷେତ୍ରଫଳ ହେଉଛି ଏହାର ସୀମା ଦ୍ୱାରା ଆବଦ୍ଧ ସ୍ଥାନ, ଯାହା $A = \pi r^2$ ସୂତ୍ର ବ୍ୟବହାର କରି ହିସାବ କରାଯାଏ।
- ବ୍ୟାସାର୍ଦ୍ଧ ($r$) ହେଉଛି ବୃତ୍ତର କେନ୍ଦ୍ରରୁ ଏହାର ଧାର ପର୍ଯ୍ୟନ୍ତ ଦୂରତା।
- $\pi$ ସହିତ ଗୁଣନ କରିବା ପୂର୍ବରୁ ଆପଣଙ୍କୁ ବ୍ୟାସାର୍ଦ୍ଧକୁ ନିଜ ସହିତ ଗୁଣନ କରି ଏହାର ବର୍ଗ କରିବାକୁ ପଡିବ।
- $\pi$ ର ମୂଲ୍ୟ ଏକ ଅପରିମେୟ ସଂଖ୍ୟା ଯାହା ପ୍ରାୟତଃ $3.14159...$ ସହିତ ସମାନ।
- ବୃତ୍ତର କ୍ଷେତ୍ରଫଳ ପାଇଁ ଏକକ ସର୍ବଦା ଏକ ବର୍ଗ ଏକକ ହୋଇଥାଏ, ଯେପରିକି $cm^2$, କାରଣ କ୍ଷେତ୍ରଫଳ ଦୁଇଟି ଆୟାମ (dimensions) ମାପିଥାଏ।