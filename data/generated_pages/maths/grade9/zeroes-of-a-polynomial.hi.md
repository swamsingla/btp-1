---
{
  "concept": "Zeroes of a Polynomial",
  "slug": "zeroes-of-a-polynomial",
  "grade": 9,
  "language": "hi",
  "subject": "maths",
  "area": "Algebra",
  "hand_edited": "2026-10-17: The generated Hindi left the title, headings and most terms (polynomial, zero, equation, linear, constant, variable, real number) in English. Rewritten by hand from the audited English page with Hindi terms and the English in brackets at first use; same 33 citation tags in the same order. Terms: bahupad, shunya (zero of a polynomial), mool (root), rekhik, achar, ashunya.",
  "model": "sarvam-105b",
  "settings": {
    "temperature": 0.3,
    "max_tokens": 8000,
    "reasoning_effort": "none"
  },
  "usage": {
    "completion_tokens": 1688,
    "prompt_tokens": 2146,
    "total_tokens": 3834,
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
  "generated_at": "2026-10-17T05:29:31",
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
    "words": 903,
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

# बहुपद के शून्य (Zeroes of a Polynomial)

यह पृष्ठ किसी संख्या पर बहुपद (polynomial) के मान को देखता है, और उन संख्याओं को भी जिनके लिए वह मान शून्य होता है। इन संख्याओं को बहुपद के शून्य (zeroes) कहा जाता है।

## किसी संख्या पर बहुपद का मान

बहुपद $p(x) = 5x^{3} - 2x^{2} + 3x - 2$ पर विचार कीजिए। यदि हम $p(x)$ में हर जगह $x$ के स्थान पर 1 रख दें, तो हमें $p(1) = 5 \times (1)^{3} - 2 \times (1)^{2} + 3 \times (1) - 2 = 5 - 2 + 3 - 2 = 4$ मिलता है। इसलिए हम कहते हैं कि $x = 1$ पर $p(x)$ का मान 4 है। इसी प्रकार, $p(0) = 5(0)^{3} - 2(0)^{2} + 3(0) - 2 = -2$।

यहाँ तीन और उदाहरण हैं, जिनमें चर (variable) के दिए गए मान पर बहुपद का मान ज्ञात किया गया है:

*   $x = 1$ पर $p(x) = 5x^{2} - 3x + 7$ के लिए: $p(1) = 5(1)^{2} - 3(1) + 7 = 5 - 3 + 7 = 9$।
*   $y = 2$ पर $q(y) = 3y^{3} - 4y + \sqrt{11}$ के लिए: $q(2) = 3(2)^{3} - 4(2) + \sqrt{11} = 24 - 8 + \sqrt{11} = 16 + \sqrt{11}$।
*   $t = a$ पर $p(t) = 4t^4 + 5t^3 - t^2 + 6$ के लिए: $p(a) = 4a^{4} + 5a^{3} - a^{2} + 6$।

## बहुपद का शून्य

अब बहुपद $p(x) = x - 1$ पर विचार कीजिए। यहाँ $p(1) = 1 - 1 = 0$ है। चूँकि $p(1) = 0$ है, इसलिए हम कहते हैं कि 1 बहुपद $p(x)$ का एक शून्य है। इसी प्रकार, 2 बहुपद $q(x) = x - 2$ का एक शून्य है।

सामान्यतः, बहुपद $p(x)$ का शून्य एक ऐसी संख्या $c$ है जिसके लिए $p(c) = 0$ होता है।

## शून्य और बहुपद समीकरण

बहुपद $x - 1$ का शून्य इसे 0 के बराबर रखकर प्राप्त होता है, अर्थात् $x - 1 = 0$, जिससे $x = 1$ मिलता है। हम कहते हैं कि $p(x) = 0$ एक बहुपद समीकरण (polynomial equation) है, और 1 इस बहुपद समीकरण $p(x) = 0$ का मूल (root) है। अतः 1 बहुपद $x - 1$ का शून्य है, या बहुपद समीकरण $x - 1 = 0$ का मूल है।

$p(x)$ का शून्य ज्ञात करना समीकरण $p(x) = 0$ को हल करने के समान है। उदाहरण के लिए, $p(x) = 2x + 1$ का शून्य ज्ञात करने के लिए हम $2x + 1 = 0$ को हल करते हैं, जिससे $x = -\frac{1}{2}$ मिलता है। अतः $-\frac{1}{2}$ बहुपद $2x + 1$ का एक शून्य है।

## रैखिक बहुपद का शून्य

मान लीजिए $p(x) = ax + b$, जहाँ $a \neq 0$, एक रैखिक बहुपद (linear polynomial) है। $p(x)$ का शून्य ज्ञात करना $p(x) = 0$ को हल करने के बराबर है, अर्थात् $ax + b = 0$ को हल करना, जहाँ $a \neq 0$। तब $ax = -b$, अतः $x = -\frac{b}{a}$। इसलिए $x = -\frac{b}{a}$ ही $p(x)$ का एकमात्र शून्य है, जिसका अर्थ है कि रैखिक बहुपद का एक और केवल एक शून्य होता है। इस प्रकार 1, $x - 1$ का शून्य है और $-2$, $x + 2$ का शून्य है।

## अचर बहुपदों के शून्य

अचर बहुपद (constant polynomial) 5 पर विचार कीजिए। इसका कोई शून्य नहीं है, क्योंकि $5x^0$ में $x$ के स्थान पर कोई भी संख्या रखने पर भी हमें 5 ही मिलता है। वास्तव में, अशून्य अचर बहुपद का कोई शून्य नहीं होता। शून्य बहुपद (zero polynomial) के लिए, परिपाटी के अनुसार, प्रत्येक वास्तविक संख्या एक शून्य है।

## जाँच: कोई संख्या शून्य है या नहीं

यह जाँचने के लिए कि $-2$ और 2 बहुपद $x + 2$ के शून्य हैं या नहीं, मान लीजिए $p(x) = x + 2$। तब $p(2) = 2 + 2 = 4$ और $p(-2) = -2 + 2 = 0$। इसलिए $-2$ बहुपद $x + 2$ का शून्य है, पर 2 नहीं है।

## अवलोकन

बहुपदों के शून्यों के बारे में हमारे अवलोकन ये हैं:

*   बहुपद का शून्य 0 ही हो, यह आवश्यक नहीं है।
*   0 किसी बहुपद का शून्य हो सकता है।
*   प्रत्येक रैखिक बहुपद का एक और केवल एक शून्य होता है।
*   किसी बहुपद के एक से अधिक शून्य हो सकते हैं।

## हल किया गया उदाहरण

जाँचिए कि क्या 2 और 0 बहुपद $x^{2} - 2x$ के शून्य हैं। मान लीजिए $p(x) = x^{2} - 2x$। तब $p(2) = 2^{2} - 4 = 4 - 4 = 0$ और $p(0) = 0 - 0 = 0$। अतः 2 और 0 दोनों बहुपद $x^{2} - 2x$ के शून्य हैं। यह बहुपद दिखाता है कि किसी बहुपद के एक से अधिक शून्य हो सकते हैं, और 0 उनमें से एक हो सकता है।

## मुख्य बिंदु

*   $x = c$ पर बहुपद $p(x)$ का मान $p(x)$ में हर जगह $x$ के स्थान पर $c$ रखकर ज्ञात किया जाता है।
*   बहुपद $p(x)$ का शून्य एक ऐसी संख्या $c$ है जिसके लिए $p(c) = 0$ होता है।
*   $p(x)$ का शून्य ज्ञात करना बहुपद समीकरण $p(x) = 0$ को हल करने के समान है।
*   $a \neq 0$ वाले रैखिक बहुपद $ax + b$ का एक और केवल एक शून्य होता है, $-\frac{b}{a}$।
*   अशून्य अचर बहुपद का कोई शून्य नहीं होता, और परिपाटी के अनुसार प्रत्येक वास्तविक संख्या शून्य बहुपद का शून्य है।
*   किसी बहुपद के एक से अधिक शून्य हो सकते हैं।
