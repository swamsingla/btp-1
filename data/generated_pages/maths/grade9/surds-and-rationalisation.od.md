---
{
  "concept": "Surds and Rationalisation",
  "slug": "surds-and-rationalisation",
  "grade": 9,
  "language": "od",
  "hand_edited": "2026-10-17: Odia audit against the English page. Title and body used transliterations: surds / rationalisation (sards, rasanalaijesan, rasanalaij) and identities (aidentiti); now aparimeya bargamula (Surds), harara parimeyikarana and sarbasamika as on the other pages. 'Quotient' was harafala in five places (harafala is not a word; bhagafala used elsewhere); 'non-zero' was shunya-ana, now ana-shunya; 'non-terminating non-recurring' was asaranti apunarabrutti, now as on the decimal-expansions page; 'like terms' made samajatiya pada; 'equivalent expression' made samatulya; positive was yuktatmaka, now dhanatmaka. Rational / irrational (parimeya / aparimeya) were correct and not swapped, unlike the Telugu page.",
  "subject": "maths",
  "area": "Number Systems",
  "model": "sarvam-105b",
  "settings": {
    "temperature": 0.3,
    "max_tokens": 8000,
    "reasoning_effort": "none"
  },
  "usage": {
    "completion_tokens": 2839,
    "prompt_tokens": 3027,
    "total_tokens": 5866,
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
  "generated_at": "2026-10-17T06:08:56",
  "source_grade": 9,
  "grade_delta": 0,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g9_maths_chapter1_017",
      "chapter": "chapter1",
      "section": "1.4 Operations on Real Numbers"
    },
    {
      "ref": "S2",
      "passage_id": "g9_maths_chapter1_005",
      "chapter": "chapter1",
      "section": "1.2 Irrational Numbers"
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
    "words": 988,
    "target_words": [
      1000,
      1350
    ],
    "untraceable_sections": 0,
    "ok": true,
    "tags_vs_english": "32/32",
    "localisation_problems": [],
    "not_harvestable": [
      "brackets: 5/5 declared terms are not bracketed with their English word (['irrational number', 'rational number', 'square root', 'rationalising the denominator'])"
    ]
  },
  "terms": [
    "irrational number",
    "rational number",
    "square root",
    "rationalising the denominator",
    "real number"
  ]
}
---

# ଅପରିମେୟ ବର୍ଗମୂଳ (Surds) ଏବଂ ହରର ପରିମେୟୀକରଣ

ଏହି ପୃଷ୍ଠାଟି $\sqrt{2}$ ଏବଂ $\sqrt{3}$ ପରି ଅପରିମେୟ ବର୍ଗମୂଳ (irrational square roots) ଥିବା ଅଭିବ୍ୟକ୍ତିଗୁଡ଼ିକ ବିଷୟରେ ଅଟେ। ଯେତେବେଳେ ଏହିପରି ସଂଖ୍ୟାଗୁଡ଼ିକୁ ଯୋଗ, ଗୁଣନ ଏବଂ ହରଣ କରାଯାଏ ସେତେବେଳେ କଣ ହୁଏ, ବର୍ଗମୂଳ ପାଇଁ ସର୍ବସମିକା (identities) କିପରି ଆମକୁ ଅଭିବ୍ୟକ୍ତିଗୁଡ଼ିକୁ ସରଳ କରିବାରେ ସାହାଯ୍ୟ କରେ, ଏବଂ ବର୍ଗମୂଳ ଥିବା ହରକୁ କିପରି ପରିମେୟୀକରଣ (rationalise) କରାଯାଏ ତାହା ଆମେ ଦେଖିବା।

## ଅପରିମେୟ ବର୍ଗମୂଳ

ଏକ ସଂଖ୍ୟାକୁ ଅପରିମେୟ କୁହାଯାଏ ଯଦି ଏହାକୁ $\frac{p}{q}$ ଆକାରରେ ଲେଖାଯାଇପାରିବ ନାହିଁ, ଯେଉଁଠାରେ $p$ ଏବଂ $q$ ପୂର୍ଣ୍ଣସଂଖ୍ୟା ଅଟନ୍ତି ଏବଂ $q \neq 0$। କିଛି ଉଦାହରଣ ହେଉଛି $\sqrt{2}$, $\sqrt{3}$, $\sqrt{15}$ ଏବଂ $\pi$।

ଯେତେବେଳେ ଆମେ $\sqrt{}$ ପ୍ରତୀକ ବ୍ୟବହାର କରୁ, ଆମେ ମାନିନେଉ ଯେ ଏହା ସଂଖ୍ୟାର ଧନାତ୍ମକ ବର୍ଗମୂଳ ଅଟେ। ତେଣୁ $\sqrt{4}=2$, ଯଦିଓ 2 ଏବଂ $-2$ ଉଭୟ 4 ର ବର୍ଗମୂଳ ଅଟନ୍ତି। ଏକ ବାସ୍ତବ ସଂଖ୍ୟା $a > 0$ ପାଇଁ, $\sqrt{a} = b$ ର ଅର୍ଥ ହେଉଛି $b^2 = a$ ଏବଂ $b > 0$।

## ଅପରିମେୟ ସଂଖ୍ୟା ଉପରେ କ୍ରିୟା

ଅପରିମେୟ ସଂଖ୍ୟାଗୁଡ଼ିକର ଯୋଗଫଳ, ବିୟୋଗଫଳ, ଭାଗଫଳ ଏବଂ ଗୁଣଫଳ ସର୍ବଦା ଅପରିମେୟ ନୁହେଁ। ଉଦାହରଣ ସ୍ୱରୂପ, $\left(\sqrt{6}\right)+\left(-\sqrt{6}\right)$, $\left(\sqrt{2}\right)-\left(\sqrt{2}\right)$, $\left(\sqrt{3}\right)\cdot\left(\sqrt{3}\right)$ ଏବଂ $\frac{\sqrt{17}}{\sqrt{17}}$ ସବୁ ପରିମେୟ ଅଟନ୍ତି।

ବର୍ତ୍ତମାନ ଏକ ପରିମେୟ ସଂଖ୍ୟା ସହିତ ଏକ ଅପରିମେୟ ସଂଖ୍ୟା ନିଅନ୍ତୁ। ଯେହେତୁ $\sqrt{3}$ ର ଏକ ଅଣ-ସମାପ୍ତ ଅଣ-ପୁନରାବୃତ୍ତି ଦଶମିକ ବିସ୍ତାର ଅଛି, $2 + \sqrt{3}$ ଏବଂ $2\sqrt{3}$ ପାଇଁ ମଧ୍ୟ ସମାନ କଥା ସତ୍ୟ ଅଟେ। ତେଣୁ ଉଭୟ $2 + \sqrt{3}$ ଏବଂ $2\sqrt{3}$ ଅପରିମେୟ ସଂଖ୍ୟା ଅଟନ୍ତି।

ଏହିପରି ଉଦାହରଣଗୁଡ଼ିକ ନିମ୍ନଲିଖିତ ତଥ୍ୟଗୁଡ଼ିକୁ ଦର୍ଶାଏ, ଯାହା ସତ୍ୟ ଅଟେ:

*   ଏକ ପରିମେୟ ସଂଖ୍ୟା ଏବଂ ଏକ ଅପରିମେୟ ସଂଖ୍ୟାର ଯୋଗଫଳ କିମ୍ବା ବିୟୋଗଫଳ ଅପରିମେୟ ଅଟେ।
*   ଏକ ଅଣ-ଶୂନ୍ୟ ପରିମେୟ ସଂଖ୍ୟା ଏବଂ ଏକ ଅପରିମେୟ ସଂଖ୍ୟାର ଗୁଣଫଳ କିମ୍ବା ଭାଗଫଳ ଅପରିମେୟ ଅଟେ।
*   ଯଦି ଆମେ ଦୁଇଟି ଅପରିମେୟ ସଂଖ୍ୟାକୁ ଯୋଗ, ବିୟୋଗ, ଗୁଣନ କିମ୍ବା ହରଣ କରୁ, ତେବେ ଫଳାଫଳ ପରିମେୟ କିମ୍ବା ଅପରିମେୟ ହୋଇପାରେ।

ଆମେ ଏକ ସଂଖ୍ୟାକୁ ଦଶମିକ ଭାବରେ ଲେଖି ପରୀକ୍ଷା କରିପାରିବା। $\sqrt{5} = 2.236\ldots$, $\sqrt{2} = 1.4142\ldots$ ଏବଂ $\pi = 3.1415\ldots$ ବ୍ୟବହାର କରି, ଆମେ ପାଇବା $7\sqrt{5} = 15.652\ldots$, $\frac{7}{\sqrt{5}} = \frac{7\sqrt{5}}{\sqrt{5}\sqrt{5}} = \frac{7\sqrt{5}}{5} = 3.1304\ldots$, $\sqrt{2} + 21 = 22.4142\ldots$ ଏବଂ $\pi - 2 = 1.1415\ldots$। ଏସବୁ ଅଣ-ସମାପ୍ତ ଅଣ-ପୁନରାବୃତ୍ତି ଦଶମିକ ଅଟେ, ତେଣୁ ସେଗୁଡ଼ିକ ସବୁ ଅପରିମେୟ ସଂଖ୍ୟା ଅଟନ୍ତି।

ଅପରିମେୟ ସଂଖ୍ୟାଗୁଡ଼ିକୁ କିପରି ଯୋଗ, ଗୁଣନ ଏବଂ ହରଣ କରାଯାଏ ତାହା ଏଠାରେ ଦିଆଯାଇଛି:

*   $2\sqrt{2} + 5\sqrt{3}$ ଏବଂ $\sqrt{2} - 3\sqrt{3}$ ଯୋଗ କରନ୍ତୁ। ସମଜାତୀୟ ପଦଗୁଡ଼ିକୁ ଏକାଠି କରି, $\left(2\sqrt{2} + \sqrt{2}\right) + \left(5\sqrt{3} - 3\sqrt{3}\right) = (2 + 1)\sqrt{2} + (5 - 3)\sqrt{3} = 3\sqrt{2} + 2\sqrt{3}$।
*   $6\sqrt{5}$ କୁ $2\sqrt{5}$ ସହିତ ଗୁଣନ କରନ୍ତୁ। ଆମେ ପାଇବା $6 \times 2 \times \sqrt{5} \times \sqrt{5} = 12 \times 5 = 60$।
*   $8\sqrt{15}$ କୁ $2\sqrt{3}$ ଦ୍ୱାରା ହରଣ କରନ୍ତୁ। $\sqrt{15} = \sqrt{3} \times \sqrt{5}$ ଲେଖି, ଆମେ ପାଇବା $\frac{8\sqrt{3} \times \sqrt{5}}{2\sqrt{3}} = 4\sqrt{5}$।

## ବର୍ଗମୂଳ ପାଇଁ ସର୍ବସମିକା

ବର୍ଗମୂଳ ସହିତ ଜଡିତ କିଛି ସର୍ବସମିକା ବିଭିନ୍ନ ଉପାୟରେ ଉପଯୋଗୀ ଅଟେ। ବାକିଗୁଡ଼ିକ ବାସ୍ତବ ସଂଖ୍ୟାଗୁଡ଼ିକର ଯୋଗ ଉପରେ ଗୁଣନର ବିତରଣ ନିୟମରୁ, ଏବଂ ଯେକୌଣସି ବାସ୍ତବ ସଂଖ୍ୟା $x$ ଏବଂ $y$ ପାଇଁ ସର୍ବସମିକା $(x + y)(x - y) = x^{2} - y^{2}$ ରୁ ଆସିଥାଏ। ଧରାଯାଉ $a$ ଏବଂ $b$ ଧନାତ୍ମକ ବାସ୍ତବ ସଂଖ୍ୟା ଅଟନ୍ତି। ତେବେ:

(i) $\sqrt{ab} = \sqrt{a}\sqrt{b}$

(ii) $\sqrt{\frac{a}{b}} = \frac{\sqrt{a}}{\sqrt{b}}$

(iii) $\left(\sqrt{a} + \sqrt{b}\right)\left(\sqrt{a} - \sqrt{b}\right) = a - b$

(iv) $\left(a + \sqrt{b}\right)\left(a - \sqrt{b}\right) = a^2 - b$

(v) $\left(\sqrt{a} + \sqrt{b}\right)\left(\sqrt{c} + \sqrt{d}\right) = \sqrt{ac} + \sqrt{ad} + \sqrt{bc} + \sqrt{bd}$

(vi) $\left(\sqrt{a} + \sqrt{b}\right)^2 = a + 2\sqrt{ab} + b$

ଏଠାରେ "ସରଳ" (simplify) ର ଅର୍ଥ ହେଉଛି ଯେ ଅଭିବ୍ୟକ୍ତିଟି ଏକ ପରିମେୟ ଏବଂ ଏକ ଅପରିମେୟ ସଂଖ୍ୟାର ଯୋଗଫଳ ଭାବରେ ଲେଖାଯିବା ଉଚିତ୍। ଆସନ୍ତୁ ସର୍ବସମିକାଗୁଡ଼ିକ ବ୍ୟବହାର କରି କିଛି ଅଭିବ୍ୟକ୍ତିକୁ ସରଳ କରିବା।

*   $\left(5+\sqrt{7}\right)\left(2+\sqrt{5}\right) = 10 + 5\sqrt{5} + 2\sqrt{7} + \sqrt{35}$, ବିତରଣ ନିୟମ ଅନୁଯାୟୀ।
*   $\left(5 + \sqrt{5}\right)\left(5 - \sqrt{5}\right) = 5^2 - \left(\sqrt{5}\right)^2 = 25 - 5 = 20$, ସର୍ବସମିକା (iv) ଅନୁଯାୟୀ।
*   $\left(\sqrt{3} + \sqrt{7}\right)^2 = \left(\sqrt{3}\right)^2 + 2\sqrt{3}\sqrt{7} + \left(\sqrt{7}\right)^2 = 3 + 2\sqrt{21} + 7 = 10 + 2\sqrt{21}$, ସର୍ବସମିକା (vi) ଅନୁଯାୟୀ।
*   $\left(\sqrt{11} - \sqrt{7}\right)\left(\sqrt{11} + \sqrt{7}\right) = \left(\sqrt{11}\right)^2 - \left(\sqrt{7}\right)^2 = 11 - 7 = 4$, ସର୍ବସମିକା (iii) ଅନୁଯାୟୀ।

## ହରକୁ ପରିମେୟୀକରଣ କରିବା

$\frac{1}{\sqrt{2}}$ କୁ ଦେଖନ୍ତୁ। ଏହା ଅପରିମେୟ ଅଟେ, ଏବଂ ଯଦି ହର ଏକ ପରିମେୟ ସଂଖ୍ୟା ହୋଇଥାଏ ତେବେ ଏହାକୁ ପରିଚାଳନା କରିବା ସହଜ ହୋଇପାରେ। ହରକୁ ପରିମେୟୀକରଣ କରିବାର ଅର୍ଥ ହେଉଛି ହରକୁ ଏକ ପରିମେୟ ସଂଖ୍ୟାରେ ପରିଣତ କରିବା। ଏହା କରିବା ପାଇଁ, ଆମକୁ ବର୍ଗମୂଳ ସହିତ ଜଡିତ ସର୍ବସମିକାଗୁଡ଼ିକର ଆବଶ୍ୟକତା ଅଛି।

ଆମେ $\frac{1}{\sqrt{2}}$ କୁ ଏକ ସମତୁଲ୍ୟ ଅଭିବ୍ୟକ୍ତି ଭାବରେ ଲେଖିବାକୁ ଚାହୁଁ ଯେଉଁଥିରେ ହର ଏକ ପରିମେୟ ସଂଖ୍ୟା ଅଟେ। ଆମେ ଜାଣୁ ଯେ $\sqrt{2} \cdot \sqrt{2}$ ପରିମେୟ ଅଟେ। ଆମେ ମଧ୍ୟ ଜାଣୁ ଯେ $\frac{1}{\sqrt{2}}$ କୁ $\frac{\sqrt{2}}{\sqrt{2}}$ ସହିତ ଗୁଣନ କଲେ ଏକ ସମତୁଲ୍ୟ ଅଭିବ୍ୟକ୍ତି ମିଳେ, ଯେହେତୁ $\frac{\sqrt{2}}{\sqrt{2}} = 1$। ଏହି ଦୁଇଟି ତଥ୍ୟକୁ ଏକାଠି କଲେ, $\frac{1}{\sqrt{2}} = \frac{1}{\sqrt{2}} \times \frac{\sqrt{2}}{\sqrt{2}} = \frac{\sqrt{2}}{2}$। ଏହି ରୂପରେ ସଂଖ୍ୟା ରେଖାରେ $\frac{1}{\sqrt{2}}$ କୁ ଖୋଜିବା ସହଜ ଅଟେ, କାରଣ ଏହା 0 ଏବଂ $\sqrt{2}$ ମଧ୍ୟରେ ଅଧା ବାଟରେ ଅଛି।

ଯେତେବେଳେ ହରରେ ଦୁଇଟି ପଦ ଥାଏ, ଆମେ ସମାନ ଦୁଇଟି ପଦ ଦ୍ୱାରା ଗୁଣନ ଏବଂ ହରଣ କରୁ ଯେଉଁଥିରେ ସେମାନଙ୍କ ମଧ୍ୟରେ ଥିବା ଚିହ୍ନ ପରିବର୍ତ୍ତିତ ହୋଇଥାଏ, ଯାହାଫଳରେ ଏକ ସର୍ବସମିକା ହରରୁ ବର୍ଗମୂଳକୁ ହଟାଇଦିଏ। $\frac{1}{2 + \sqrt{3}}$ କୁ ପରିମେୟୀକରଣ କରିବା ପାଇଁ ଆମେ ସର୍ବସମିକା (iv) ବ୍ୟବହାର କରୁ ଏବଂ $2 - \sqrt{3}$ ଦ୍ୱାରା ଗୁଣନ ଏବଂ ହରଣ କରୁ:

$\frac{1}{2 + \sqrt{3}}\times \frac{2 - \sqrt{3}}{2 - \sqrt{3}} = \frac{2 - \sqrt{3}}{4 - 3} = 2 - \sqrt{3}$।

ସେହିପରି, $\frac{1}{7 + 3\sqrt{2}}$ କୁ ପରିମେୟୀକରଣ କରିବା ପାଇଁ ଆମେ $7 - 3\sqrt{2}$ ଦ୍ୱାରା ଗୁଣନ ଏବଂ ହରଣ କରୁ, ଯାହା ଦିଏ $\frac{7 - 3\sqrt{2}}{49 - 18} = \frac{7 - 3\sqrt{2}}{31}$।

ତେଣୁ, ଯେତେବେଳେ ଏକ ଅଭିବ୍ୟକ୍ତିର ହରରେ ବର୍ଗମୂଳ ଥିବା ଏକ ପଦ ଥାଏ, ଏହାକୁ ଏକ ସମତୁଲ୍ୟ ଅଭିବ୍ୟକ୍ତିରେ ପରିଣତ କରିବା ଯାହାର ହର ଏକ ପରିମେୟ ସଂଖ୍ୟା ଅଟେ, ତାହାକୁ ହରକୁ ପରିମେୟୀକରଣ କରିବା କୁହାଯାଏ।

## ସମାଧାନ କରାଯାଇଥିବା ଉଦାହରଣ

$\frac{5}{\sqrt{3} - \sqrt{5}}$ ର ହରକୁ ପରିମେୟୀକରଣ କରନ୍ତୁ। ଏଠାରେ ଆମେ ସର୍ବସମିକା (iii), $\left(\sqrt{a} + \sqrt{b}\right)\left(\sqrt{a} - \sqrt{b}\right) = a - b$ ବ୍ୟବହାର କରୁ, ଯେଉଁଥିରେ $a = 3$ ଏବଂ $b = 5$, ତେଣୁ ଆମେ $\sqrt{3} + \sqrt{5}$ ଦ୍ୱାରା ଗୁଣନ ଏବଂ ହରଣ କରୁ।

$\frac{5}{\sqrt{3} - \sqrt{5}} = \frac{5}{\sqrt{3} - \sqrt{5}} \times \frac{\sqrt{3} + \sqrt{5}}{\sqrt{3} + \sqrt{5}} = \frac{5\left(\sqrt{3} + \sqrt{5}\right)}{3 - 5} = \left(\frac{-5}{2}\right)\left(\sqrt{3} + \sqrt{5}\right)$।

## ମୁଖ୍ୟ ବିନ୍ଦୁ

*   ଦୁଇଟି ଅପରିମେୟ ସଂଖ୍ୟାର ଯୋଗଫଳ, ବିୟୋଗଫଳ, ଭାଗଫଳ ଏବଂ ଗୁଣଫଳ ପରିମେୟ କିମ୍ବା ଅପରିମେୟ ହୋଇପାରେ।
*   ଏକ ପରିମେୟ ସଂଖ୍ୟା ଏବଂ ଏକ ଅପରିମେୟ ସଂଖ୍ୟାର ଯୋଗଫଳ କିମ୍ବା ବିୟୋଗଫଳ ଅପରିମେୟ ଅଟେ।
*   ଏକ ଅଣ-ଶୂନ୍ୟ ପରିମେୟ ସଂଖ୍ୟା ଏବଂ ଏକ ଅପରିମେୟ ସଂଖ୍ୟାର ଗୁଣଫଳ କିମ୍ବା ଭାଗଫଳ ଅପରିମେୟ ଅଟେ।
*   $\left(\sqrt{a} + \sqrt{b}\right)\left(\sqrt{a} - \sqrt{b}\right) = a - b$ ଏବଂ $\left(a + \sqrt{b}\right)\left(a - \sqrt{b}\right) = a^2 - b$ ପରି ସର୍ବସମିକାଗୁଡ଼ିକ ବର୍ଗମୂଳ ଥିବା ଅଭିବ୍ୟକ୍ତିଗୁଡ଼ିକୁ ସରଳ କରିବାରେ ଆମକୁ ସାହାଯ୍ୟ କରେ।
*   ହରକୁ ପରିମେୟୀକରଣ କରିବାର ଅର୍ଥ ହେଉଛି ହରରେ ବର୍ଗମୂଳ ଥିବା ଏକ ଅଭିବ୍ୟକ୍ତିକୁ ଏକ ସମତୁଲ୍ୟ ଅଭିବ୍ୟକ୍ତିରେ ପରିଣତ କରିବା ଯାହାର ହର ଏକ ପରିମେୟ ସଂଖ୍ୟା ଅଟେ।