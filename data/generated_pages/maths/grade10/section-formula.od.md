---
{
  "concept": "Section Formula and Midpoint",
  "slug": "section-formula",
  "grade": 10,
  "language": "od",
  "subject": "maths",
  "area": "Coordinate Geometry",
  "model": "sarvam-105b",
  "settings": {
    "temperature": 0.3,
    "max_tokens": 8000,
    "reasoning_effort": "none"
  },
  "usage": {
    "completion_tokens": 1326,
    "prompt_tokens": 1689,
    "total_tokens": 3015,
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
  "generated_at": "2026-10-18T00:13:00",
  "source_grade": 10,
  "grade_delta": 0,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g10_maths_chapter7_013",
      "chapter": "chapter7",
      "section": "7.3 Section Formula"
    },
    {
      "ref": "S2",
      "passage_id": "g10_maths_chapter11_005",
      "chapter": "chapter11",
      "section": "11.1 Areas of Sector and Segment of a Circle"
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
    "words": 605,
    "target_words": [
      1000,
      1350
    ],
    "untraceable_sections": 0,
    "ok": true,
    "tags_vs_english": "16/16",
    "localisation_problems": [],
    "not_harvestable": [
      "brackets: 4/5 declared terms are not bracketed with their English word (['section formula', 'midpoint', 'internal division', 'ratio'])"
    ]
  },
  "terms": [
    "section formula",
    "midpoint",
    "internal division",
    "ratio",
    "coordinates"
  ]
}
---

# ବିଭାଜନ ସୂତ୍ର (Section Formula) ଏବଂ ମଧ୍ୟବିନ୍ଦୁ

କଳ୍ପନା କରନ୍ତୁ ଯେ ଏକ ଟେଲିଫୋନ୍ କମ୍ପାନୀ ଦୁଇଟି ସ୍ଥାନ A ଏବଂ B ମଧ୍ୟରେ ଠିକ୍ ଭାବରେ ଏକ ଟାୱାର ସ୍ଥାପନ କରିବାକୁ ଚାହୁଁଛି। ଯଦି ଟାୱାରଟି ଏପରି ସ୍ଥାନରେ ରଖାଯାଏ ଯେ B ଠାରୁ ଏହାର ଦୂରତା A ଠାରୁ ଏହାର ଦୂରତାର ଦୁଇଗୁଣ ଅଟେ, ତେବେ ଟାୱାରଟି ରେଖାଖଣ୍ଡ AB କୁ 1 : 2 ଅନୁପାତରେ ବିଭକ୍ତ କରେ। ଏହି ଟାୱାରର ସଠିକ୍ ସ୍ଥାନାଙ୍କ (coordinates) ଖୋଜିବା ପାଇଁ, ଆମକୁ ଏକ ନିର୍ଭରଯୋଗ୍ୟ ଗାଣିତିକ ପଦ୍ଧତି ଦରକାର। ଏହି ବିଷୟଟି ହେଉଛି ଏକ ନିର୍ଦ୍ଦିଷ୍ଟ ଅନୁପାତରେ, ଆଭ୍ୟନ୍ତରୀଣ କିମ୍ବା ବାହ୍ୟ ଭାବରେ, ଏକ ରେଖାଖଣ୍ଡକୁ ବିଭକ୍ତ କରୁଥିବା ବିନ୍ଦୁର ସ୍ଥାନାଙ୍କ ଖୋଜିବା ବିଷୟରେ।

## ବିଭାଜନ ସୂତ୍ର

ଯେତେବେଳେ ଏକ ବିନ୍ଦୁ P ଏକ ରେଖା ଉପରେ ଥିବା ଦୁଇଟି ବିନ୍ଦୁ A ଏବଂ B ମଧ୍ୟରେ ଥାଏ, ଏହା ରେଖାଖଣ୍ଡ AB କୁ ଆଭ୍ୟନ୍ତରୀଣ ଭାବରେ ବିଭକ୍ତ କରେ। ଧରାଯାଉ A ର ସ୍ଥାନାଙ୍କ $(x_1, y_1)$ ଏବଂ B ର ସ୍ଥାନାଙ୍କ $(x_2, y_2)$। ଯଦି P, A ଏବଂ B କୁ ଯୋଡୁଥିବା ରେଖାଖଣ୍ଡକୁ $m_1: m_2$ ଅନୁପାତରେ ଆଭ୍ୟନ୍ତରୀଣ ଭାବରେ ବିଭକ୍ତ କରେ, ତେବେ P ର ସ୍ଥାନାଙ୍କ ବିଭାଜନ ସୂତ୍ର ଦ୍ୱାରା ଦିଆଯାଏ।

ବିନ୍ଦୁ $A(x_{1}, y_{1})$ ଏବଂ $B(x_{2}, y_{2})$ କୁ ଯୋଡୁଥିବା ରେଖାଖଣ୍ଡକୁ ଆଭ୍ୟନ୍ତରୀଣ ଭାବରେ $m_{1}: m_{2}$ ଅନୁପାତରେ ବିଭକ୍ତ କରୁଥିବା ବିନ୍ଦୁ $P(x, y)$ ର ସ୍ଥାନାଙ୍କ ହେଉଛି

$$ \left(\frac {m _ {1} x _ {2} + m _ {2} x _ {1}}{m _ {1} + m _ {2}}, \frac {m _ {1} y _ {2} + m _ {2} y _ {1}}{m _ {1} + m _ {2}}\right) $$

ଏହାକୁ ବିଭାଜନ ସୂତ୍ର କୁହାଯାଏ। ଯଦି P, AB କୁ ବିଭକ୍ତ କରୁଥିବା ଅନୁପାତ $k: 1$ ହୁଏ, ତେବେ ବିନ୍ଦୁ P ର ସ୍ଥାନାଙ୍କ ହେବ

$$ \left(\frac {k x _ {2} + x _ {1}}{k + 1}, \frac {k y _ {2} + y _ {1}}{k + 1}\right). $$

## ମଧ୍ୟବିନ୍ଦୁ

ବିଭାଜନ ସୂତ୍ରର ଏକ ସ୍ୱତନ୍ତ୍ର କ୍ଷେତ୍ର ହେଉଛି ମଧ୍ୟବିନ୍ଦୁ। ଏକ ରେଖାଖଣ୍ଡର ମଧ୍ୟବିନ୍ଦୁ ରେଖାଖଣ୍ଡକୁ 1 : 1 ଅନୁପାତରେ ବିଭକ୍ତ କରେ। ତେଣୁ, ବିନ୍ଦୁ $A(x_{1}, y_{1})$ ଏବଂ $B(x_{2}, y_{2})$ କୁ ଯୋଡ଼ୁଥିବା ରେଖାଖଣ୍ଡର ମଧ୍ୟବିନ୍ଦୁ P ର ସ୍ଥାନାଙ୍କ ହେଉଛି

$$ \left(\frac {1 \cdot x _ {1} + 1 \cdot x _ {2}}{1 + 1}, \frac {1 \cdot y _ {1} + 1 \cdot y _ {2}}{1 + 1}\right) = \left(\frac {x _ {1} + x _ {2}}{2}, \frac {y _ {1} + y _ {2}}{2}\right). $$

## ସମାଧାନ କରାଯାଇଥିବା ଉଦାହରଣ

ଆସନ୍ତୁ ବିଭାଜନ ସୂତ୍ର ଉପରେ ଆଧାରିତ ଏକ ଉଦାହରଣ ସମାଧାନ କରିବା। $(4, -3)$ ଏବଂ $(8, 5)$ ବିନ୍ଦୁଗୁଡ଼ିକୁ ଯୋଡୁଥିବା ରେଖାଖଣ୍ଡକୁ $3:1$ ଅନୁପାତରେ ଆଭ୍ୟନ୍ତରୀଣ ଭାବରେ ବିଭକ୍ତ କରୁଥିବା ବିନ୍ଦୁର ସ୍ଥାନାଙ୍କ ଖୋଜନ୍ତୁ।

ଧରାଯାଉ $\mathrm{P}(x, y)$ ହେଉଛି ଆବଶ୍ୟକୀୟ ବିନ୍ଦୁ। ବିଭାଜନ ସୂତ୍ର ବ୍ୟବହାର କରି, ଆମେ ପାଇବା

$$ x = \frac {3 \times 8 + 1 \times 4}{3 + 1} = \frac {24 + 4}{4} = \frac {28}{4} = 7 $$

$$ y = \frac {3 \times 5 + 1 \times (-3)}{3 + 1} = \frac {15 - 3}{4} = \frac {12}{4} = 3 $$

ତେଣୁ, ଆବଶ୍ୟକୀୟ ବିନ୍ଦୁର ସ୍ଥାନାଙ୍କ ହେଉଛି $(7, 3)$।

## ମୁଖ୍ୟ ବିନ୍ଦୁ

*   ବିଭାଜନ ସୂତ୍ର ଦୁଇଟି ବିନ୍ଦୁ $(x_1, y_1)$ ଏବଂ $(x_2, y_2)$ କୁ ଯୋଡୁଥିବା ରେଖାଖଣ୍ଡକୁ ଏକ ନିର୍ଦ୍ଦିଷ୍ଟ ଅନୁପାତ $m_1 : m_2$ ରେ ବିଭକ୍ତ କରୁଥିବା ବିନ୍ଦୁର ସ୍ଥାନାଙ୍କ ଦିଏ।
*   ଆଭ୍ୟନ୍ତରୀଣ ବିଭାଜନ ପାଇଁ ସୂତ୍ର ହେଉଛି $\left(\frac {m _ {1} x _ {2} + m _ {2} x _ {1}}{m _ {1} + m _ {2}}, \frac {m _ {1} y _ {2} + m _ {2} y _ {1}}{m _ {1} + m _ {2}}\right)$।
*   ମଧ୍ୟବିନ୍ଦୁ ହେଉଛି ବିଭାଜନ ସୂତ୍ରର ଏକ ସ୍ୱତନ୍ତ୍ର କ୍ଷେତ୍ର ଯେଉଁଠାରେ ଅନୁପାତ ହେଉଛି $1:1$, ଯାହା ସ୍ଥାନାଙ୍କ $\left(\frac {x _ {1} + x _ {2}}{2}, \frac {y _ {1} + y _ {2}}{2}\right)$ ଦିଏ।
*   ଯଦି ଅନୁପାତ $k:1$ ଦିଆଯାଇଥାଏ, ତେବେ ବିନ୍ଦୁ P ର ସ୍ଥାନାଙ୍କ ହେବ $\left(\frac {k x _ {2} + x _ {1}}{k + 1}, \frac {k y _ {2} + y _ {1}}{k + 1}\right)$।
*   ଆପଣ ଯାଞ୍ଚ କରିପାରିବେ ଯେ ବିନ୍ଦୁରୁ ପ୍ରାନ୍ତ ବିନ୍ଦୁଗୁଡ଼ିକ ପର୍ଯ୍ୟନ୍ତ ଦୂରତାର ଅନୁପାତ ଦିଆଯାଇଥିବା ଅନୁପାତ ସହିତ ମେଳ ଖାଉଛି କି ନାହିଁ।