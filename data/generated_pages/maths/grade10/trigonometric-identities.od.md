---
{
  "concept": "Trigonometric Identities",
  "slug": "trigonometric-identities",
  "grade": 10,
  "language": "od",
  "subject": "maths",
  "area": "Trigonometry",
  "model": "sarvam-105b",
  "settings": {
    "temperature": 0.3,
    "max_tokens": 8000,
    "reasoning_effort": "none"
  },
  "usage": {
    "completion_tokens": 1770,
    "prompt_tokens": 1903,
    "total_tokens": 3673,
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
  "generated_at": "2026-10-18T00:13:34",
  "source_grade": 10,
  "grade_delta": 0,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g10_maths_chapter8_022",
      "chapter": "chapter8",
      "section": "8.4 Trigonometric Identities"
    },
    {
      "ref": "S2",
      "passage_id": "g10_maths_chapter8_010",
      "chapter": "chapter8",
      "section": "8.2 Trigonometric Ratios"
    }
  ],
  "citation_check": {
    "cited": [
      "1",
      "2"
    ],
    "invented_citations": [],
    "unused_sources": [],
    "explanatory_paragraphs_without_a_citation": 0,
    "words": 862,
    "target_words": [
      1000,
      1350
    ],
    "untraceable_sections": 1,
    "ok": true,
    "tags_vs_english": "16/16",
    "localisation_problems": []
  },
  "terms": [
    "trigonometric identity",
    "trigonometric ratios",
    "sine",
    "cosine",
    "tangent",
    "secant",
    "cosecant",
    "cotangent",
    "pythagorean theorem"
  ]
}
---

# ତ୍ରିକୋଣମିତିକ ସର୍ବସମିକା (Trigonometric Identities)

ସର୍ବସମିକା (identity) ହେଉଛି ଏପରି ଏକ ସମୀକରଣ ଯାହା ଏହାର ଚଳରାଶିଗୁଡ଼ିକର ସମସ୍ତ ସମ୍ଭାବ୍ୟ ମୂଲ୍ୟ ପାଇଁ ସତ୍ୟ। ସେହିପରି, ତ୍ରିକୋଣମିତିକ ସର୍ବସମିକା (trigonometric identity) ହେଉଛି ଏକ କୋଣର ତ୍ରିକୋଣମିତିକ ଅନୁପାତ (trigonometric ratios) ଥିବା ଏକ ସମୀକରଣ ଯାହା ସେହି କୋଣର ପ୍ରତ୍ୟେକ ମୂଲ୍ୟ ପାଇଁ ସତ୍ୟ। ଏହି ସର୍ବସମିକାଗୁଡ଼ିକ ତ୍ରିକୋଣମିତିର ମୌଳିକ ଆଧାର। ସେଗୁଡ଼ିକ ଗୋଟିଏ ତ୍ରିକୋଣମିତିକ ଅନୁପାତକୁ ଅନ୍ୟ ଏକ ଅନୁପାତ ମାଧ୍ୟମରେ ପ୍ରକାଶ କରିବାକୁ ଦିଏ। ଯଦି ଆମେ ଏକ କୋଣର ଗୋଟିଏ ଅନୁପାତର ମୂଲ୍ୟ ଜାଣୁ, ତେବେ ଏହି ସର୍ବସମିକାଗୁଡ଼ିକ ଦ୍ୱାରା ସେହି କୋଣର ଅନ୍ୟ ସମସ୍ତ ଅନୁପାତର ସଠିକ୍ ମୂଲ୍ୟ ବାହାର କରିପାରିବା।

## ପାଇଥାଗୋରାସ୍ ଉପପାଦ୍ୟ ଆଧାରିତ

ସବୁଠାରୁ ଗୁରୁତ୍ୱପୂର୍ଣ୍ଣ ତ୍ରିକୋଣମିତିକ ସର୍ବସମିକାଗୁଡ଼ିକ ସିଧାସଳଖ ପାଇଥାଗୋରାସ୍ ଉପପାଦ୍ୟ (Pythagorean theorem) ରୁ ଆସିଛି। $B$ ଠାରେ ସମକୋଣ ଥିବା ଏକ ସମକୋଣୀ ତ୍ରିଭୁଜକୁ ବିଚାର କରନ୍ତୁ। ପାଇଥାଗୋରାସ୍ ଉପପାଦ୍ୟ ଅନୁସାରେ, କର୍ଣ୍ଣ (hypotenuse) ର ବର୍ଗ ଅନ୍ୟ ଦୁଇ ବାହୁର ବର୍ଗର ସମଷ୍ଟି ସହ ସମାନ:
$$
AB^2 + BC^2 = AC^2
$$

ସମ୍ପୂର୍ଣ୍ଣ ସମୀକରଣକୁ $AC^2$ ଦ୍ୱାରା ଭାଗ କଲେ
$$
\left(\frac{AB}{AC}\right)^2 + \left(\frac{BC}{AC}\right)^2 = 1
$$
ମିଳେ, ଅର୍ଥାତ୍
$$
\cos^2 A + \sin^2 A = 1
$$
ଏହା ପ୍ରଥମ ମୌଳିକ ସର୍ବସମିକା, ଯାହା ପ୍ରତ୍ୟେକ ସୂକ୍ଷ୍ମକୋଣ $A$ ପାଇଁ ସତ୍ୟ।

## ଦ୍ୱିତୀୟ ଏବଂ ତୃତୀୟ ସର୍ବସମିକା

ପାଇଥାଗୋରାସ୍ ସମୀକରଣକୁ ପ୍ରଥମେ କୋଣ $A$ ର ସଂଲଗ୍ନ ବାହୁର ବର୍ଗ ଦ୍ୱାରା, ଏବଂ ତା'ପରେ କୋଣ $A$ ର ସମ୍ମୁଖ ବାହୁର ବର୍ଗ ଦ୍ୱାରା ଭାଗ କରି ଆହୁରି ଦୁଇଟି ସର୍ବସମିକା ପାଇପାରିବା।

$AB^2 + BC^2 = AC^2$ କୁ $AB^2$ ଦ୍ୱାରା ଭାଗ କଲେ ଦ୍ୱିତୀୟ ସର୍ବସମିକା ମିଳେ:
$$
1 + \tan^2 A = \sec^2 A
$$
$BC^2$ ଦ୍ୱାରା ଭାଗ କଲେ ତୃତୀୟ ସର୍ବସମିକା ମିଳେ:
$$
\cot^2 A + 1 = \csc^2 A
$$

ଏଠାରେ $\tan$ ଟ୍ୟାନଜେଣ୍ଟ (tangent), $\sec$ ସିକାଣ୍ଟ (secant), $\cot$ କୋଟ୍ୟାନଜେଣ୍ଟ (cotangent), $\csc$ କୋସେକାଣ୍ଟ (cosecant); $\sin$ ସାଇନ୍ (sine), $\cos$ କୋସାଇନ୍ (cosine)।

## ସର୍ବସମିକା ଦ୍ୱାରା ଅଜଣା ଅନୁପାତ ବାହାର କରିବା

ତ୍ରିକୋଣମିତିକ ଅନୁପାତର ସଠିକ୍ ମୂଲ୍ୟ ବାହାର କରିବାକୁ ହେଲେ ଏହି ସର୍ବସମିକାଗୁଡ଼ିକ ବହୁତ ଉପଯୋଗୀ। ଧରାଯାଉ $\tan A = \frac{1}{\sqrt{3}}$ ଦିଆଯାଇଛି।

ଦ୍ୱିତୀୟ ସର୍ବସମିକା ଦ୍ୱାରା $\sec A$ ବାହାର କରିପାରିବା:
$$
\sec^2 A = 1 + \tan^2 A = 1 + \frac{1}{3} = \frac{4}{3}, \quad \text{ତେଣୁ} \quad \sec A = \frac{2}{\sqrt{3}}
$$

ସିକାଣ୍ଟର ବ୍ୟୁତ୍କ୍ରମ (reciprocal) ନେଲେ କୋସାଇନ୍ ମିଳେ: $\cos A = \frac{\sqrt{3}}{2}$।

ଶେଷରେ, ପ୍ରଥମ ସର୍ବସମିକା ଦ୍ୱାରା $\sin A$ ବାହାର କରୁ:
$$
\sin^2 A = 1 - \cos^2 A = 1 - \frac{3}{4} = \frac{1}{4}, \quad \text{ତେଣୁ} \quad \sin A = \frac{1}{2}
$$
ଏଥିରୁ $\csc A = 2$ ମିଳେ।

## ସାଇନ୍ ମାଧ୍ୟମରେ ଅନୁପାତ ପ୍ରକାଶ

ପ୍ରଥମ ସର୍ବସମିକା ବ୍ୟବହାର କରି, ଅନ୍ୟ ଅନୁପାତଗୁଡ଼ିକୁ କେବଳ କୋଣର ସାଇନ୍ ମାଧ୍ୟମରେ ମଧ୍ୟ ଲେଖିପାରିବା। ସର୍ବସମିକାକୁ ପୁନର୍ବିନ୍ୟାସ କଲେ $\cos^2 A = 1 - \sin^2 A$ ମିଳେ।

ଉଭୟ ପାର୍ଶ୍ୱର ବର୍ଗମୂଳ ନେଲେ, ସୂକ୍ଷ୍ମକୋଣ ପାଇଁ $\cos A$ ଧନାତ୍ମକ ହୋଇଥିବାରୁ,
$$
\cos A = \sqrt{1 - \sin^2 A}
$$
ମିଳେ।

ଏହାଦ୍ୱାରା
$$
\tan A = \frac{\sin A}{\sqrt{1 - \sin^2 A}}, \qquad \sec A = \frac{1}{\sqrt{1 - \sin^2 A}}
$$
ଲେଖିପାରିବା।

## ଅଧିକ ଜଟିଳ ସର୍ବସମିକା ପ୍ରମାଣ

ଏହି ମୌଳିକ ସର୍ବସମିକାଗୁଡ଼ିକ ଦ୍ୱାରା ଅଧିକ ଜଟିଳ ତ୍ରିକୋଣମିତିକ ସମୀକରଣ ମଧ୍ୟ ପ୍ରମାଣ କରିପାରିବା। ଉଦାହରଣ ସ୍ୱରୂପ,
$$
\sec A \, (1 - \sin A)(\sec A + \tan A) = 1
$$
ବୋଲି ପ୍ରମାଣ କରିପାରିବା।

ସିକାଣ୍ଟ ଓ ଟ୍ୟାନଜେଣ୍ଟକୁ ସାଇନ୍ ଓ କୋସାଇନ୍ ମାଧ୍ୟମରେ ଲେଖି, ଶେଷ ବନ୍ଧନୀକୁ ଗୋଟିଏ ଭଗ୍ନାଂଶରେ ମିଶାଉ:
$$
\text{ବାମ ପାର୍ଶ୍ୱ} = \frac{1}{\cos A} (1 - \sin A) \left(\frac{1}{\cos A} + \frac{\sin A}{\cos A}\right) = \frac{(1 - \sin A)(1 + \sin A)}{\cos^2 A} = \frac{1 - \sin^2 A}{\cos^2 A}
$$

ପ୍ରଥମ ସର୍ବସମିକାରୁ $1 - \sin^2 A = \cos^2 A$। ଏହାକୁ ପ୍ରତିସ୍ଥାପନ କଲେ $\frac{\cos^2 A}{\cos^2 A} = 1 = \text{ଡାହାଣ ପାର୍ଶ୍ୱ}$ ମିଳେ।

## ସମାଧାନ କରାଯାଇଥିବା ଉଦାହରଣ

$\tan A = \frac{4}{3}$ ହେଉଥିବା ସୂକ୍ଷ୍ମକୋଣ $A$ ର ତ୍ରିକୋଣମିତିକ ଅନୁପାତଗୁଡ଼ିକର ସଠିକ୍ ମୂଲ୍ୟ ସର୍ବସମିକା ଦ୍ୱାରା ବାହାର କରିବା।

ପ୍ରଥମେ ଦ୍ୱିତୀୟ ସର୍ବସମିକା ଦ୍ୱାରା $\sec A$ ବାହାର କରୁ:
$$
\sec^2 A = 1 + \tan^2 A = 1 + \frac{16}{9} = \frac{25}{9}, \quad \text{ତେଣୁ} \quad \sec A = \frac{5}{3}
$$

ତା'ପରେ ସିକାଣ୍ଟର ବ୍ୟୁତ୍କ୍ରମ ନେଇ $\cos A$ ବାହାର କରୁ: $\cos A = \frac{3}{5}$।

ଶେଷରେ ପ୍ରଥମ ସର୍ବସମିକା ଦ୍ୱାରା $\sin A$ ବାହାର କରୁ:
$$
\sin^2 A = 1 - \cos^2 A = 1 - \frac{9}{25} = \frac{16}{25}, \quad \text{ତେଣୁ} \quad \sin A = \frac{4}{5}
$$

ବାକି ଅନୁପାତଗୁଡ଼ିକ ଏଗୁଡ଼ିକର ବ୍ୟୁତ୍କ୍ରମ: $\cot A = \frac{3}{4}$ ଏବଂ $\csc A = \frac{5}{4}$।

## ମୁଖ୍ୟ ବିନ୍ଦୁ

*   ତ୍ରିକୋଣମିତିକ ସର୍ବସମିକା ହେଉଛି ତ୍ରିକୋଣମିତିକ ଅନୁପାତ ଥିବା ଏକ ସମୀକରଣ ଯାହା କୋଣର ସମସ୍ତ ମୂଲ୍ୟ ପାଇଁ ସତ୍ୟ।
*   ତିନୋଟି ମୌଳିକ ସର୍ବସମିକା ହେଉଛି $\sin^2\theta + \cos^2\theta = 1$, $1 + \tan^2\theta = \sec^2\theta$, ଏବଂ $1 + \cot^2\theta = \csc^2\theta$।
*   ଏହି ସର୍ବସମିକାଗୁଡ଼ିକ ଦ୍ୱାରା ଯେକୌଣସି ଗୋଟିଏ ତ୍ରିକୋଣମିତିକ ଅନୁପାତକୁ ଅନ୍ୟ ଏକ ଅନୁପାତ ମାଧ୍ୟମରେ ପ୍ରକାଶ କରିପାରିବା।
*   ସଂଜ୍ଞାଗୁଡ଼ିକୁ ପ୍ରତିସ୍ଥାପନ କରି ଓ ସରଳ କରି ଅଧିକ ଜଟିଳ ତ୍ରିକୋଣମିତିକ ସମୀକରଣ ମଧ୍ୟ ପ୍ରମାଣ କରିପାରିବା।
*   ଧ୍ୟାନ ଦିଅନ୍ତୁ ଯେ $\tan A = \frac{\sin A}{\cos A}$ ଏବଂ $\cot A = \frac{\cos A}{\sin A}$, ଯାହା ରାଶିଗୁଡ଼ିକୁ ପୁନର୍ବାର ଲେଖିବାରେ ସାହାଯ୍ୟ କରେ।
