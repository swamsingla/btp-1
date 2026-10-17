---
{
  "concept": "Division of Algebraic Expressions",
  "slug": "division-of-polynomials",
  "grade": 8,
  "language": "hi",
  "hand_edited": "2026-10-13: line-by-line hand audit against the English tagged copy, edited directly in both copies: made the long-division stopping rule precise (remainder is 0 or has a lower power of x than the divisor), translated the English words left inside the check formula, common factor worded as ubhayanishth, headings and spelling made consistent with the other pages",
  "subject": "maths",
  "area": "Algebra",
  "model": "sarvam-105b",
  "settings": {
    "temperature": 0.3,
    "max_tokens": 8000,
    "reasoning_effort": "none"
  },
  "usage": {
    "completion_tokens": 1496,
    "prompt_tokens": 1823,
    "total_tokens": 3319,
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
  "generated_at": "2026-10-13T04:40:04",
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
    "words": 840,
    "target_words": [
      950,
      1300
    ],
    "untraceable_sections": 3,
    "ok": true,
    "tags_vs_english": "4/4",
    "localisation_problems": [],
    "not_harvestable": [
      "brackets: 5/10 declared terms are not bracketed with their English word (['binomial', 'algebraic identity', 'dividend', 'divisor'])"
    ]
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

# बीजगणितीय व्यंजकों का विभाजन

बीजगणितीय व्यंजकों को जोड़ा, घटाया, गुणा और विभाजित किया जा सकता है। एक बीजगणितीय व्यंजक को दूसरे से विभाजित करने का अर्थ है उस व्यंजक को खोजना, जिसे भाजक से गुणा करने पर पुनः भाज्य प्राप्त हो। यह कौशल हमें व्यंजकों को सरल बनाने और समीकरणों को अधिक आसानी से हल करने में मदद करता है। इस पृष्ठ पर, भाजक कभी शून्य नहीं होता है।

## एक बहुपद (polynomial) को एकपदी (monomial) से विभाजित करना

एक बहुपद को एकपदी से विभाजित करने के लिए, बहुपद के प्रत्येक पद को एकपदी से अलग-अलग विभाजित करें, और फिर परिणामों को जोड़ें।

उदाहरण के लिए, $12x^3 - 6x^2$ को $3x$ से विभाजित करने के लिए, $12x^3$ को $3x$ से विभाजित करके $4x^2$ प्राप्त करें, और $-6x^2$ को $3x$ से विभाजित करके $-2x$ प्राप्त करें। परिणाम $4x^2 - 2x$ है।

आप भाजक से गुणा करके उत्तर की जाँच कर सकते हैं: $3x \times (4x^2 - 2x) = 12x^3 - 6x^2$, जो मूल बहुपद है।

## एक बहुपद को दूसरे बहुपद से विभाजित करना

जब भाजक में एक से अधिक पद होते हैं, तो आप दीर्घ विभाजन (long division) विधि का उपयोग कर सकते हैं, जो संख्याओं के साथ सीखे गए दीर्घ विभाजन के बहुत समान है। सबसे पहले दोनों बहुपदों को उनके पदों के साथ $x$ की घटती घातों (decreasing powers) में लिखें। फिर इन चरणों को दोहराएं: भाज्य के पहले पद को भाजक के पहले पद से विभाजित करें, परिणाम को भाजक से गुणा करें, और इसे भाज्य से घटाएं। जो बचे उसके साथ तब तक जारी रखें जब तक कि शेषफल (remainder) $0$ न हो जाए या उसमें $x$ की घात भाजक में $x$ की घात से कम न हो जाए।

उदाहरण के लिए, आइए $x^2 + 5x + 6$ को $x + 2$ से विभाजित करें।
- $x^2$ को $x$ से विभाजित करके $x$ प्राप्त करें।
- $x$ को $x + 2$ से गुणा करके $x^2 + 2x$ प्राप्त करें। इसे भाज्य से घटाने पर $3x + 6$ बचता है।
- $3x$ को $x$ से विभाजित करके $3$ प्राप्त करें।
- $3$ को $x + 2$ से गुणा करके $3x + 6$ प्राप्त करें। घटाने पर $0$ शेषफल बचता है।

इसलिए भागफल $x + 3$ है और शेषफल $0$ है।

कभी-कभी शेषफल शून्य नहीं होता है। आइए $x^2 + 3x + 5$ को $x + 1$ से विभाजित करें। $x^2$ को $x$ से विभाजित करके $x$ प्राप्त करें, फिर $x \times (x + 1) = x^2 + x$, और घटाने पर $2x + 5$ बचता है। $2x$ को $x$ से विभाजित करके $2$ प्राप्त करें, फिर $2 \times (x + 1) = 2x + 2$, और घटाने पर $3$ बचता है। भागफल $x + 2$ है और शेषफल $3$ है। शेषफल $3$ में कोई $x$ नहीं है, इसलिए हम आगे विभाजित नहीं कर सकते।

विभाजन की जाँच करने के लिए, इस संबंध का उपयोग करें:
$$ \text{भाज्य} = \text{भाजक} \times \text{भागफल} + \text{शेषफल} $$
यहाँ $(x + 1)(x + 2) + 3 = x^2 + 3x + 2 + 3 = x^2 + 3x + 5$, जो भाज्य है।

## विभाजित करने के लिए सर्वसमिकाओं (identities) का उपयोग करना

कभी-कभी विभाजन आसान हो जाता है यदि आप पहले भाज्य का गुणनखंडन (factorisation) कर लें। आप ऐसा करने के लिए बीजगणितीय सर्वसमिकाओं का उपयोग कर सकते हैं। उदाहरण के लिए, सर्वसमिका $x^2 - y^2 = (x + y)(x - y)$ दो वर्गों के अंतर (difference of two squares) के लिए उपयोगी है।

आइए $x^2 - 9$ को $x + 3$ से विभाजित करें। चूँकि $9 = 3^2$, सर्वसमिका $x^2 - 9 = (x + 3)(x - 3)$ देती है। तब
$$ \frac{x^2 - 9}{x + 3} = \frac{(x + 3)(x - 3)}{x + 3} = x - 3 $$
उभयनिष्ठ गुणनखंड $x + 3$ कट जाता है, इसलिए भागफल $x - 3$ है।

सर्वसमिका $(x + y)^2 = x^2 + 2xy + y^2$ इसी तरह काम करती है। चूँकि $x^2 + 10x + 25 = (x + 5)^2$, $x^2 + 10x + 25$ को $x + 5$ से विभाजित करने पर $x + 5$ प्राप्त होता है।

## हल किया गया उदाहरण

आइए $10x^2 - 5x$ को $5x$ से विभाजित करें।

सबसे पहले, बहुपद को दो पदों में विभाजित करें: $\frac{10x^2}{5x}$ और $\frac{-5x}{5x}$।

इसके बाद, पहले पद को विभाजित करें: $\frac{10x^2}{5x} = 2x$।

फिर, दूसरे पद को विभाजित करें: $\frac{-5x}{5x} = -1$।

अंतिम उत्तर प्राप्त करने के लिए परिणामों को मिलाएं: $2x - 1$।

जाँच: $5x \times (2x - 1) = 10x^2 - 5x$, जो मूल बहुपद है।

## मुख्य बिंदु

*   एक बहुपद को एकपदी से विभाजित करने के लिए, बहुपद के प्रत्येक पद को एकपदी से विभाजित करें।
*   एक बहुपद को दूसरे बहुपद से विभाजित करने के लिए, दीर्घ विभाजन विधि का उपयोग करें।
*   बीजगणितीय सर्वसमिकाओं का उपयोग करके गुणनखंडन विभाजन प्रक्रिया को सरल बना सकता है।
*   हमेशा अपने उत्तर की जाँच करें: भाज्य = भाजक × भागफल + शेषफल।
*   यह विषय बीजगणितीय व्यंजकों के गुणनखंडन पर आधारित है, जो बीजगणितीय सर्वसमिकाओं का उपयोग करता है।