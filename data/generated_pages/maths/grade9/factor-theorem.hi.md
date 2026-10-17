---
{
  "concept": "Factor Theorem",
  "slug": "factor-theorem",
  "grade": 9,
  "language": "hi",
  "hand_edited": "2026-10-17: Hindi audit against the English page. 'Splitting the middle term' was rendered as 'vibhajan' (division); now 'madhya pad ko todna'. Grammar slip (a ki kisi maan) fixed, 'linear term' heading made 'linear expression'. In the tagged copy the citation tags moved to the end of the sentence (they sat before the verb).",
  "subject": "maths",
  "area": "Algebra",
  "model": "sarvam-105b",
  "settings": {
    "temperature": 0.3,
    "max_tokens": 8000,
    "reasoning_effort": "none"
  },
  "usage": {
    "completion_tokens": 2222,
    "prompt_tokens": 2550,
    "total_tokens": 4772,
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
  "generated_at": "2026-10-17T05:29:59",
  "source_grade": 9,
  "grade_delta": 0,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g9_maths_chapter2_014",
      "chapter": "chapter2",
      "section": "2.4 Factorisation of Polynomials"
    },
    {
      "ref": "S2",
      "passage_id": "g9_maths_chapter2_012",
      "chapter": "chapter2",
      "section": "2.3 Zeroes of a Polynomial"
    },
    {
      "ref": "S3",
      "passage_id": "g9_maths_chapter1_026",
      "chapter": "chapter1",
      "section": "1.5 Laws of Exponents for Real Numbers"
    }
  ],
  "citation_check": {
    "cited": [
      "1",
      "2"
    ],
    "invented_citations": [],
    "unused_sources": [
      "3"
    ],
    "explanatory_paragraphs_without_a_citation": 0,
    "words": 1159,
    "target_words": [
      1000,
      1350
    ],
    "untraceable_sections": 0,
    "ok": true,
    "tags_vs_english": "37/37",
    "localisation_problems": [],
    "not_harvestable": [
      "brackets: 4/9 declared terms are not bracketed with their English word (['polynomial equation', 'root', 'quadratic polynomial', 'cubic polynomial'])"
    ]
  },
  "terms": [
    "zero of a polynomial",
    "factor",
    "factor theorem",
    "remainder theorem",
    "polynomial equation",
    "root",
    "linear polynomial",
    "quadratic polynomial",
    "cubic polynomial"
  ]
}
---

# गुणनखंड प्रमेय (Factor Theorem)

बहुपद का शून्य (zero of a polynomial) एक संख्या $c$ है जिसके लिए $p(c) = 0$ होता है। उदाहरण के लिए, बहुपद $x - 1$ का शून्य 1 है क्योंकि $p(1) = 1 - 1 = 0$। गुणनखंड प्रमेय (Factor Theorem) इन शून्यों और बहुपद के गुणनखंडों (factors) के बीच एक सीधा संबंध देता है। यदि $p(x)$ एक बहुपद है और $a$ कोई वास्तविक संख्या है, तो $x - a$, $p(x)$ का एक गुणनखंड (factor) तभी होगा जब $p(a) = 0$। इसका अर्थ है कि हम यह जांच कर सकते हैं कि $x - a$, $p(x)$ का गुणनखंड है या नहीं, यह देखकर कि क्या $p(a) = 0$ है।

## प्रमेय का कथन

गुणनखंड प्रमेय एक बहुपद के शून्यों को उसके गुणनखंडों से जोड़ता है। यह बताता है कि $n \geq 1$ घात (degree) वाले बहुपद $p(x)$ और एक वास्तविक संख्या $a$ के लिए, $x - a$, $p(x)$ का एक गुणनखंड है यदि $p(a) = 0$ है, और $p(a) = 0$ है यदि $x - a$, $p(x)$ का एक गुणनखंड है। यह दोनों तरह से काम करता है। यदि $a$ के किसी मान के लिए $p(a) = 0$ है, तो $x - a$, $p(x)$ का एक गुणनखंड है।

## शेषफल प्रमेय का उपयोग

शेषफल प्रमेय (Remainder Theorem) का उपयोग करके गुणनखंड प्रमेय को सिद्ध किया जाता है। शेषफल प्रमेय हमें बताता है कि $p(x) = (x - a)q(x) + p(a)$। यदि $p(a) = 0$ है, तो समीकरण $p(x) = (x - a)q(x)$ बन जाता है। यह दर्शाता है कि $x - a$, $p(x)$ का एक गुणनखंड है। इसके विपरीत, यदि $x - a$, $p(x)$ का एक गुणनखंड है, तो किसी बहुपद $g(x)$ के लिए $p(x) = (x - a)g(x)$। यदि हम इस समीकरण में $x = a$ रखते हैं, तो हमें $p(a) = (a - a)g(a) = 0 \times g(a) = 0$ मिलता है।

## शून्य ज्ञात करना

गुणनखंड प्रमेय का उपयोग करने के लिए, हमें बहुपद के शून्यों की आवश्यकता होती है। एक बहुपद $p(x)$ का शून्य एक संख्या $c$ है जिसके लिए $p(c) = 0$ होता है। एक रैखिक बहुपद (linear polynomial) के लिए, ठीक एक शून्य होता है। हालांकि, एक बहुपद के एक से अधिक शून्य हो सकते हैं। उदाहरण के लिए, बहुपद $x^2 - 2x$ के शून्य 2 और 0 हैं क्योंकि $p(2) = 2^2 - 2 \times 2 = 0$ और $p(0) = 0^2 - 2 \times 0 = 0$।

## यह जांचना कि क्या कोई रैखिक व्यंजक एक गुणनखंड है

गुणनखंड प्रमेय का उपयोग यह जांचने के लिए किया जा सकता है कि क्या कोई रैखिक व्यंजक (linear expression) किसी बहुपद का एक गुणनखंड है। उदाहरण के लिए, यह जांचने के लिए कि क्या $x + 2$, $x^3 + 3x^2 + 5x + 6$ का एक गुणनखंड है, हम $x + 2$ का शून्य ज्ञात करते हैं, जो -2 है। मान लीजिए $p(x) = x^3 + 3x^2 + 5x + 6$ है। तब, $p(-2) = (-2)^3 + 3(-2)^2 + 5(-2) + 6 = -8 + 12 - 10 + 6 = 0$। चूँकि $p(-2) = 0$ है, इसलिए गुणनखंड प्रमेय के अनुसार, $x + 2$, $x^3 + 3x^2 + 5x + 6$ का एक गुणनखंड है।

## किसी अचर (Constant) का मान ज्ञात करना

गुणनखंड प्रमेय का उपयोग किसी बहुपद में किसी अचर (constant) का मान ज्ञात करने के लिए भी किया जा सकता है। उदाहरण के लिए, यदि $x - 1$, $p(x) = 4x^3 + 3x^2 - 4x + k$ का एक गुणनखंड है, तो $p(1) = 0$ होगा। अब, $p(1) = 4(1)^3 + 3(1)^2 - 4(1) + k = 4 + 3 - 4 + k = 0$, जिससे $k = -3$ प्राप्त होता है।

## द्विघात बहुपदों के गुणनखंड निकालना

गुणनखंड प्रमेय का उपयोग द्विघात बहुपदों (quadratic polynomials) के गुणनखंड निकालने के लिए किया जा सकता है। उदाहरण के लिए, $y^2 - 5y + 6$ के गुणनखंड निकालने के लिए, हम $p(y) = y^2 - 5y + 6$ लेते हैं। यदि $p(y) = (y - a)(y - b)$ है, तो अचर पद (constant term) $ab$ है, इसलिए $ab = 6$ है और हम 6 के गुणनखंडों को देखते हैं। हम पाते हैं कि $p(2) = 2^2 - 5(2) + 6 = 4 - 10 + 6 = 0$, इसलिए $y - 2$, $p(y)$ का एक गुणनखंड है। साथ ही, $p(3) = 3^2 - 5(3) + 6 = 9 - 15 + 6 = 0$, इसलिए $y - 3$ भी $y^2 - 5y + 6$ का एक गुणनखंड है। अतः, $y^2 - 5y + 6 = (y - 2)(y - 3)$।

## त्रिघात बहुपदों के गुणनखंड निकालना

त्रिघात बहुपदों (cubic polynomials) के लिए, शुरुआत में मध्य पद को तोड़ने की विधि (splitting method) उपयुक्त नहीं है, इसलिए हमें पहले कम से कम एक गुणनखंड ज्ञात करना होगा। उदाहरण के लिए, $x^3 - 23x^2 + 142x - 120$ के गुणनखंड निकालने के लिए, हम $p(x) = x^3 - 23x^2 + 142x - 120$ लेते हैं। हम -120 के गुणनखंड खोजते हैं और उन्हें आज़मा कर देखते हैं। हम पाते हैं कि $p(1) = 1^3 - 23(1)^2 + 142(1) - 120 = 1 - 23 + 142 - 120 = 0$। इसलिए, $x - 1$, $p(x)$ का एक गुणनखंड है।

अब हम $p(x) = (x - 1)(x^2 - 22x + 120)$ लिख सकते हैं। हम द्विघात भाग के गुणनखंड मध्य पद को तोड़कर या फिर से गुणनखंड प्रमेय का उपयोग करके निकाल सकते हैं। मध्य पद को तोड़ने पर, हमें $x^2 - 22x + 120 = x^2 - 12x - 10x + 120 = x(x - 12) - 10(x - 12) = (x - 10)(x - 12)$ मिलता है। अतः, $x^3 - 23x^2 + 142x - 120 = (x - 1)(x - 10)(x - 12)$।

## हल किया गया उदाहरण (Worked example)

आइए एक नए बहुपद पर गुणनखंड प्रमेय लागू करें। $p(x) = x^2 - 7x + 12$ पर विचार करें। हम यह जांचना चाहते हैं कि क्या $x - 3$, $p(x)$ का एक गुणनखंड है। $x - 3$ का शून्य 3 है। हम $p(3) = 3^2 - 7(3) + 12 = 9 - 21 + 12 = 0$ की गणना करते हैं। चूँकि $p(3) = 0$ है, इसलिए गुणनखंड प्रमेय के अनुसार, $x - 3$, $p(x)$ का एक गुणनखंड है। $p(x)$ को $x - 3$ से विभाजित करने पर दूसरा गुणनखंड $x - 4$ मिलता है, इसलिए $x^2 - 7x + 12 = (x - 3)(x - 4)$।

## मुख्य बिंदु (Key points)

- एक बहुपद $p(x)$ का शून्य एक संख्या $c$ है जिसके लिए $p(c) = 0$ होता है।
- यदि $p(a) = 0$ है, तो $x - a$, $p(x)$ का एक गुणनखंड है।
- यदि $x - a$, $p(x)$ का एक गुणनखंड है, तो $p(a) = 0$ होगा।
- गुणनखंड प्रमेय को शेषफल प्रमेय का उपयोग करके सिद्ध किया जाता है, जिसके अनुसार $p(x) = (x - a)q(x) + p(a)$ होता है।
- गुणनखंड प्रमेय का उपयोग द्विघात और त्रिघात बहुपदों के शून्यों को ज्ञात करके उनके गुणनखंड निकालने के लिए किया जा सकता है।