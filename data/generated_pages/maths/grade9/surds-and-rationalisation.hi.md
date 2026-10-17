---
{
  "concept": "Surds and Rationalisation",
  "slug": "surds-and-rationalisation",
  "grade": 9,
  "language": "hi",
  "subject": "maths",
  "area": "Number Systems",
  "hand_edited": "2026-10-17: The generated Hindi left the title, headings and most terms (irrational, rational, square root, identity, distributive law, denominator, rationalise, real number, non-zero) in English. Rewritten by hand from the audited English page: Hindi headings and terms with the English in brackets at first use; same 32 citation tags in the same order. Title is given as 'aparimey vargmool aur har ka parimeyikaran' because 'surd' is not a word of the Grade 9 book.",
  "model": "sarvam-105b",
  "settings": {
    "temperature": 0.3,
    "max_tokens": 8000,
    "reasoning_effort": "none"
  },
  "usage": {
    "completion_tokens": 2689,
    "prompt_tokens": 3048,
    "total_tokens": 5737,
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
  "generated_at": "2026-10-17T05:28:52",
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
    "words": 1138,
    "target_words": [
      1000,
      1350
    ],
    "untraceable_sections": 0,
    "ok": true,
    "tags_vs_english": "32/32",
    "localisation_problems": []
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

# अपरिमेय वर्गमूल और हर का परिमेयीकरण (Surds and Rationalisation)

यह पृष्ठ उन व्यंजकों के बारे में है जिनमें $\sqrt{2}$ और $\sqrt{3}$ जैसे अपरिमेय वर्गमूल (irrational square roots) होते हैं। हम देखेंगे कि जब ऐसी संख्याओं को जोड़ा, गुणा और भाग किया जाता है तो क्या होता है, वर्गमूलों की सर्वसमिकाएँ (identities) व्यंजकों को सरल बनाने में हमारी कैसे मदद करती हैं, और वर्गमूल वाले हर का परिमेयीकरण (rationalising the denominator) कैसे किया जाता है।

## अपरिमेय वर्गमूल

किसी संख्या को अपरिमेय (irrational) कहा जाता है यदि उसे $\frac{p}{q}$ के रूप में नहीं लिखा जा सकता, जहाँ $p$ और $q$ पूर्णांक हैं और $q \neq 0$। कुछ उदाहरण $\sqrt{2}$, $\sqrt{3}$, $\sqrt{15}$ और $\pi$ हैं।

जब हम $\sqrt{}$ चिह्न का उपयोग करते हैं, तो हम मान लेते हैं कि वह संख्या का धनात्मक वर्गमूल (square root) है। इसलिए $\sqrt{4}=2$, यद्यपि 2 और $-2$ दोनों 4 के वर्गमूल हैं। वास्तविक संख्या (real number) $a > 0$ के लिए, $\sqrt{a} = b$ का अर्थ है $b^2 = a$ और $b > 0$।

## अपरिमेय संख्याओं पर संक्रियाएँ

अपरिमेय संख्याओं का योग, अंतर, भागफल और गुणनफल सदैव अपरिमेय नहीं होता। उदाहरण के लिए, $\left(\sqrt{6}\right)+\left(-\sqrt{6}\right)$, $\left(\sqrt{2}\right)-\left(\sqrt{2}\right)$, $\left(\sqrt{3}\right)\cdot\left(\sqrt{3}\right)$ और $\frac{\sqrt{17}}{\sqrt{17}}$ सभी परिमेय हैं।

अब एक परिमेय संख्या को एक अपरिमेय संख्या के साथ लीजिए। चूँकि $\sqrt{3}$ का दशमलव विस्तार असांत अनावर्ती है, इसलिए यही बात $2 + \sqrt{3}$ और $2\sqrt{3}$ के लिए भी सत्य है। अतः $2 + \sqrt{3}$ और $2\sqrt{3}$ दोनों अपरिमेय संख्याएँ हैं।

इस प्रकार के उदाहरण हमें निम्नलिखित तथ्यों तक ले जाते हैं, जो सत्य हैं:

*   एक परिमेय संख्या और एक अपरिमेय संख्या का योग या अंतर अपरिमेय होता है।
*   एक अशून्य परिमेय संख्या और एक अपरिमेय संख्या का गुणनफल या भागफल अपरिमेय होता है।
*   यदि हम दो अपरिमेय संख्याओं को जोड़ें, घटाएँ, गुणा करें या भाग दें, तो परिणाम परिमेय या अपरिमेय हो सकता है।

हम किसी संख्या को दशमलव के रूप में लिखकर उसकी जाँच कर सकते हैं। $\sqrt{5} = 2.236\ldots$, $\sqrt{2} = 1.4142\ldots$ और $\pi = 3.1415\ldots$ लेने पर हमें $7\sqrt{5} = 15.652\ldots$, $\frac{7}{\sqrt{5}} = \frac{7\sqrt{5}}{\sqrt{5}\sqrt{5}} = \frac{7\sqrt{5}}{5} = 3.1304\ldots$, $\sqrt{2} + 21 = 22.4142\ldots$ और $\pi - 2 = 1.1415\ldots$ प्राप्त होते हैं। ये सभी असांत अनावर्ती दशमलव हैं, इसलिए ये सभी अपरिमेय संख्याएँ हैं।

अपरिमेय संख्याओं को किस प्रकार जोड़ा, गुणा और भाग किया जाता है, यह यहाँ दिया गया है:

*   $2\sqrt{2} + 5\sqrt{3}$ और $\sqrt{2} - 3\sqrt{3}$ को जोड़िए। समान पदों को एक साथ लेने पर $\left(2\sqrt{2} + \sqrt{2}\right) + \left(5\sqrt{3} - 3\sqrt{3}\right) = (2 + 1)\sqrt{2} + (5 - 3)\sqrt{3} = 3\sqrt{2} + 2\sqrt{3}$।
*   $6\sqrt{5}$ को $2\sqrt{5}$ से गुणा कीजिए। हमें $6 \times 2 \times \sqrt{5} \times \sqrt{5} = 12 \times 5 = 60$ प्राप्त होता है।
*   $8\sqrt{15}$ को $2\sqrt{3}$ से भाग दीजिए। $\sqrt{15} = \sqrt{3} \times \sqrt{5}$ लिखने पर हमें $\frac{8\sqrt{3} \times \sqrt{5}}{2\sqrt{3}} = 4\sqrt{5}$ प्राप्त होता है।

## वर्गमूलों की सर्वसमिकाएँ

वर्गमूलों से संबंधित कुछ सर्वसमिकाएँ अनेक प्रकार से उपयोगी होती हैं। शेष सर्वसमिकाएँ वास्तविक संख्याओं के योग पर गुणन के वितरण नियम से, और किन्हीं वास्तविक संख्याओं $x$ तथा $y$ के लिए सर्वसमिका $(x + y)(x - y) = x^{2} - y^{2}$ से प्राप्त होती हैं। मान लीजिए $a$ और $b$ धनात्मक वास्तविक संख्याएँ हैं। तब:

(i) $\sqrt{ab} = \sqrt{a}\sqrt{b}$

(ii) $\sqrt{\frac{a}{b}} = \frac{\sqrt{a}}{\sqrt{b}}$

(iii) $\left(\sqrt{a} + \sqrt{b}\right)\left(\sqrt{a} - \sqrt{b}\right) = a - b$

(iv) $\left(a + \sqrt{b}\right)\left(a - \sqrt{b}\right) = a^2 - b$

(v) $\left(\sqrt{a} + \sqrt{b}\right)\left(\sqrt{c} + \sqrt{d}\right) = \sqrt{ac} + \sqrt{ad} + \sqrt{bc} + \sqrt{bd}$

(vi) $\left(\sqrt{a} + \sqrt{b}\right)^2 = a + 2\sqrt{ab} + b$

यहाँ "सरल करना" का अर्थ है कि व्यंजक को एक परिमेय और एक अपरिमेय संख्या के योग के रूप में लिखा जाए। आइए सर्वसमिकाओं का उपयोग करके कुछ व्यंजकों को सरल करें।

*   $\left(5+\sqrt{7}\right)\left(2+\sqrt{5}\right) = 10 + 5\sqrt{5} + 2\sqrt{7} + \sqrt{35}$, वितरण नियम से।
*   $\left(5 + \sqrt{5}\right)\left(5 - \sqrt{5}\right) = 5^2 - \left(\sqrt{5}\right)^2 = 25 - 5 = 20$, सर्वसमिका (iv) से।
*   $\left(\sqrt{3} + \sqrt{7}\right)^2 = \left(\sqrt{3}\right)^2 + 2\sqrt{3}\sqrt{7} + \left(\sqrt{7}\right)^2 = 3 + 2\sqrt{21} + 7 = 10 + 2\sqrt{21}$, सर्वसमिका (vi) से।
*   $\left(\sqrt{11} - \sqrt{7}\right)\left(\sqrt{11} + \sqrt{7}\right) = \left(\sqrt{11}\right)^2 - \left(\sqrt{7}\right)^2 = 11 - 7 = 4$, सर्वसमिका (iii) से।

## हर का परिमेयीकरण

$\frac{1}{\sqrt{2}}$ को देखिए। यह अपरिमेय है, और यदि इसका हर (denominator) परिमेय संख्या हो तो इसे सँभालना आसान हो सकता है। हर का परिमेयीकरण करने का अर्थ है हर को परिमेय संख्या में बदल देना। ऐसा करने के लिए हमें वर्गमूलों वाली सर्वसमिकाओं की आवश्यकता होती है।

हम $\frac{1}{\sqrt{2}}$ को एक ऐसे तुल्य व्यंजक के रूप में लिखना चाहते हैं जिसका हर परिमेय संख्या हो। हम जानते हैं कि $\sqrt{2} \cdot \sqrt{2}$ परिमेय है। हम यह भी जानते हैं कि $\frac{1}{\sqrt{2}}$ को $\frac{\sqrt{2}}{\sqrt{2}}$ से गुणा करने पर एक तुल्य व्यंजक मिलता है, क्योंकि $\frac{\sqrt{2}}{\sqrt{2}} = 1$। इन दोनों तथ्यों को साथ रखने पर $\frac{1}{\sqrt{2}} = \frac{1}{\sqrt{2}} \times \frac{\sqrt{2}}{\sqrt{2}} = \frac{\sqrt{2}}{2}$। इस रूप में $\frac{1}{\sqrt{2}}$ को संख्या रेखा पर दर्शाना आसान है, क्योंकि यह 0 और $\sqrt{2}$ के ठीक बीच में है।

जब हर में दो पद हों, तो हम उन्हीं दो पदों से गुणा और भाग करते हैं, जिनके बीच का चिह्न बदल दिया गया हो, ताकि कोई सर्वसमिका हर से वर्गमूल हटा दे। $\frac{1}{2 + \sqrt{3}}$ का परिमेयीकरण करने के लिए हम सर्वसमिका (iv) का उपयोग करते हैं और $2 - \sqrt{3}$ से गुणा और भाग करते हैं:

$\frac{1}{2 + \sqrt{3}}\times \frac{2 - \sqrt{3}}{2 - \sqrt{3}} = \frac{2 - \sqrt{3}}{4 - 3} = 2 - \sqrt{3}$।

इसी प्रकार, $\frac{1}{7 + 3\sqrt{2}}$ का परिमेयीकरण करने के लिए हम $7 - 3\sqrt{2}$ से गुणा और भाग करते हैं, जिससे $\frac{7 - 3\sqrt{2}}{49 - 18} = \frac{7 - 3\sqrt{2}}{31}$ प्राप्त होता है।

अतः जब किसी व्यंजक के हर में वर्गमूल वाला पद हो, तब उसे ऐसे तुल्य व्यंजक में बदलना जिसका हर परिमेय संख्या हो, हर का परिमेयीकरण कहलाता है।

## हल किया गया उदाहरण

$\frac{5}{\sqrt{3} - \sqrt{5}}$ के हर का परिमेयीकरण कीजिए। यहाँ हम सर्वसमिका (iii), $\left(\sqrt{a} + \sqrt{b}\right)\left(\sqrt{a} - \sqrt{b}\right) = a - b$, का उपयोग $a = 3$ और $b = 5$ लेकर करते हैं, इसलिए हम $\sqrt{3} + \sqrt{5}$ से गुणा और भाग करते हैं।

$\frac{5}{\sqrt{3} - \sqrt{5}} = \frac{5}{\sqrt{3} - \sqrt{5}} \times \frac{\sqrt{3} + \sqrt{5}}{\sqrt{3} + \sqrt{5}} = \frac{5\left(\sqrt{3} + \sqrt{5}\right)}{3 - 5} = \left(\frac{-5}{2}\right)\left(\sqrt{3} + \sqrt{5}\right)$।

## मुख्य बिंदु

*   दो अपरिमेय संख्याओं का योग, अंतर, भागफल और गुणनफल परिमेय या अपरिमेय हो सकता है।
*   एक परिमेय संख्या और एक अपरिमेय संख्या का योग या अंतर अपरिमेय होता है।
*   एक अशून्य परिमेय संख्या और एक अपरिमेय संख्या का गुणनफल या भागफल अपरिमेय होता है।
*   $\left(\sqrt{a} + \sqrt{b}\right)\left(\sqrt{a} - \sqrt{b}\right) = a - b$ और $\left(a + \sqrt{b}\right)\left(a - \sqrt{b}\right) = a^2 - b$ जैसी सर्वसमिकाएँ वर्गमूल वाले व्यंजकों को सरल बनाने में हमारी मदद करती हैं।
*   हर का परिमेयीकरण करने का अर्थ है हर में वर्गमूल वाले व्यंजक को ऐसे तुल्य व्यंजक में बदलना जिसका हर परिमेय संख्या हो।
