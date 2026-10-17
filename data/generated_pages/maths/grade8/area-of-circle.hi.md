---
{
  "concept": "Area of a Circle",
  "slug": "area-of-circle",
  "grade": 8,
  "language": "hi",
  "subject": "maths",
  "area": "Mensuration",
  "model": "sarvam-105b",
  "settings": {
    "temperature": 0.3,
    "max_tokens": 8000,
    "reasoning_effort": "none"
  },
  "usage": {
    "completion_tokens": 729,
    "prompt_tokens": 1189,
    "total_tokens": 1918,
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
  "generated_at": "2026-10-11T03:39:47",
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
    "words": 487,
    "target_words": [
      700,
      1250
    ],
    "untraceable_sections": 2,
    "ok": true,
    "tags_vs_english": "4/4",
    "localisation_problems": [],
    "not_harvestable": [
      "brackets: 3/7 declared terms are not bracketed with their English word (['area', 'pi', 'unit square'])"
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

# वृत्त का क्षेत्रफल

आप पहले से ही जानते हैं कि आयत (rectangle) और वर्ग (square) का क्षेत्रफल कैसे ज्ञात किया जाता है। आयत का क्षेत्रफल उसकी लंबाई और चौड़ाई को गुणा करके निकाला जाता है। वर्ग के लिए, आप बस भुजा को उसी से गुणा करते हैं। एक वृत्त गोल होता है, इसलिए आप सोच सकते हैं कि इसके क्षेत्रफल को कैसे मापा जाए। हम वृत्त से घिरे स्थान का क्षेत्रफल ज्ञात करने के लिए एक विशेष सूत्र (formula) का उपयोग करते हैं।

## सूत्र और पाई (Pi) का मान

वृत्त का क्षेत्रफल सूत्र $A = \pi r^2$ का उपयोग करके निकाला जाता है, जहाँ $A$ का अर्थ क्षेत्रफल है, $\pi$ (पाई) एक विशेष अचर संख्या है, और $r$ त्रिज्या (radius) है। त्रिज्या वृत्त के केंद्र से उसके किनारे के किसी भी बिंदु तक की दूरी है। $\pi$ का मान लगभग $3.14159...$ है, और यह एक अनंत दशमलव (non-terminating decimal) है। चूँकि $\pi$ एक अपरिमेय संख्या (irrational number) है, इसलिए स्कूल में गणना करते समय हम अक्सर इसे $3.14$ तक पूर्णांकित (round) कर देते हैं।

## त्रिज्या का वर्ग करना

सूत्र के $r^2$ भाग का अर्थ है कि आपको त्रिज्या को उसी से गुणा करना होगा। इसे त्रिज्या का वर्ग करना कहते हैं। यह कदम महत्वपूर्ण है क्योंकि वृत्त का क्षेत्रफल उसकी त्रिज्या के वर्ग के साथ बढ़ता है — यदि आप त्रिज्या को दोगुना करते हैं, तो क्षेत्रफल केवल दोगुना नहीं होता, बल्कि चार गुना बड़ा हो जाता है। 

क्षेत्रफल ज्ञात करने के लिए, आप इस वर्ग की गई त्रिज्या को $\pi$ से गुणा करते हैं। यदि त्रिज्या सेंटीमीटर में दी गई है, तो क्षेत्रफल वर्ग सेंटीमीटर ($cm^2$) में होगा। उदाहरण के लिए, यदि आपके पास 5 सेमी त्रिज्या वाला एक गोल पिज़्ज़ा है, तो आप पहले 5 का वर्ग करके 25 प्राप्त करते हैं। फिर, पिज़्ज़ा का क्षेत्रफल ज्ञात करने के लिए आप 25 को $3.14$ से गुणा करते हैं।

## हल किया गया उदाहरण

आइए 10 सेमी त्रिज्या वाले वृत्त का क्षेत्रफल ज्ञात करें। सबसे पहले, हम त्रिज्या की पहचान करते हैं, जो कि $r = 10$ है। इसके बाद, हम त्रिज्या का वर्ग करते हैं: $r^2 = 10^2 = 100$। अंत में, हम इस परिणाम को $\pi$ से गुणा करते हैं। $\pi$ के लिए $3.14$ का उपयोग करते हुए, क्षेत्रफल $3.14 \times 100 = 314$ है। इसलिए, वृत्त का क्षेत्रफल $314 \, cm^2$ है।

## मुख्य बिंदु

- वृत्त का क्षेत्रफल उसकी सीमा से घिरे स्थान का क्षेत्रफल है, जिसे सूत्र $A = \pi r^2$ का उपयोग करके निकाला जाता है।
- त्रिज्या ($r$) वृत्त के केंद्र से उसके किनारे तक की दूरी है।
- $\pi$ से गुणा करने से पहले आपको त्रिज्या को उसी से गुणा करके उसका वर्ग करना होगा।
- $\pi$ का मान एक अपरिमेय संख्या है जो लगभग $3.14159...$ के बराबर है।
- वृत्त के क्षेत्रफल की इकाई हमेशा वर्ग इकाई होती है, जैसे कि $cm^2$, क्योंकि क्षेत्रफल दो आयामों (dimensions) को मापता है।