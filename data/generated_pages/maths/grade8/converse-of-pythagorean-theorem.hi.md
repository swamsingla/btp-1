---
{
  "concept": "Converse of Pythagorean Theorem",
  "slug": "converse-of-pythagorean-theorem",
  "grade": 8,
  "language": "hi",
  "hand_edited": "2026-10-13: line-by-line hand audit against the English tagged copy, edited directly in both copies: fixed the congruence key point (it said three equal sides; it means three pairs of equal corresponding sides), fixed the garbled right-angle-opposite-c sentence and the hypotenuse definition, builder and frame worded in Hindi, units translated to sem",
  "subject": "maths",
  "area": "Geometry",
  "model": "sarvam-105b",
  "settings": {
    "temperature": 0.3,
    "max_tokens": 8000,
    "reasoning_effort": "none"
  },
  "usage": {
    "completion_tokens": 1294,
    "prompt_tokens": 1635,
    "total_tokens": 2929,
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
  "generated_at": "2026-10-13T04:40:12",
  "source_grade": 9,
  "grade_delta": 1,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g9_maths_chapter8_009",
      "chapter": "chapter8",
      "section": "8.2 The Mid-point Theorem"
    },
    {
      "ref": "S2",
      "passage_id": "g9_maths_chapter7_017",
      "chapter": "chapter7",
      "section": "7.5 Some More Criteria for Congruence of Triangles"
    },
    {
      "ref": "S3",
      "passage_id": "g9_maths_chapter9_014",
      "chapter": "chapter9",
      "section": "9.4 Angle Subtended by an Arc of a Circle"
    }
  ],
  "citation_check": {
    "cited": [
      "2"
    ],
    "invented_citations": [],
    "unused_sources": [
      "1",
      "3"
    ],
    "explanatory_paragraphs_without_a_citation": 0,
    "words": 787,
    "target_words": [
      950,
      1300
    ],
    "untraceable_sections": 3,
    "ok": true,
    "tags_vs_english": "2/2",
    "localisation_problems": [],
    "not_harvestable": [
      "brackets: 3/5 declared terms are not bracketed with their English word (['converse of pythagorean theorem', 'congruent triangles', 'square of a number'])"
    ]
  },
  "terms": [
    "converse of pythagorean theorem",
    "hypotenuse",
    "right-angled triangle",
    "congruent triangles",
    "square of a number"
  ]
}
---

# पाइथागोरस प्रमेय का विलोम

आप शायद पाइथागोरस प्रमेय को पहले से ही जानते हों। यह आपको बताता है कि यदि कोई त्रिभुज समकोण त्रिभुज (right-angled triangle) है, जिसकी सबसे लंबी भुजा $c$ समकोण के सम्मुख है और अन्य दो भुजाएँ $a$ और $b$ हैं, तो $a^2 + b^2 = c^2$ होगा। पाइथागोरस प्रमेय का विलोम (converse of the Pythagorean theorem) इस कथन को उल्टा कर देता है। यह कहता है कि यदि आप किसी त्रिभुज की भुजाओं को मापते हैं और पाते हैं कि $a^2 + b^2 = c^2$ है, जहाँ $c$ सबसे लंबी भुजा है, तो वह त्रिभुज समकोण त्रिभुज होता है। यह रोज़मर्रा की ज़िंदगी में बहुत उपयोगी है। उदाहरण के लिए, एक बढ़ई या राजमिस्त्री किसी त्रिकोणीय ढाँचे की तीनों भुजाओं को माप सकता है और यह पता लगाने के लिए इस समीकरण की जाँच कर सकता है कि कोई कोना एकदम सटीक समकोण है या नहीं।

## विलोम क्या कहता है

पाइथागोरस प्रमेय का विलोम त्रिभुजों के बारे में एक नियम है। यह आपको बताता है कि केवल भुजाओं को मापकर समकोण त्रिभुज की पहचान कैसे करें। मान लीजिए एक त्रिभुज की भुजाएँ $a$, $b$ और $c$ हैं, और $c$ सबसे लंबी भुजा है। यदि $a^2 + b^2 = c^2$ है, तो त्रिभुज समकोण है, और समकोण वही कोण है जो भुजा $c$ के सम्मुख है। एक समकोण त्रिभुज में, समकोण के सम्मुख वाली सबसे लंबी भुजा को कर्ण (hypotenuse) कहा जाता है।

## विलोम सत्य क्यों है

एक त्रिभुज ABC लीजिए जिसकी भुजाएँ $a$, $b$ और $c$ इस प्रकार हैं कि $a^2 + b^2 = c^2$। अब एक अलग त्रिभुज PQR खींचिए जिसका समकोण Q पर है, और समकोण से जुड़ी दो भुजाएँ $a$ और $b$ के बराबर हैं। पाइथागोरस प्रमेय के अनुसार, इस समकोण त्रिभुज का कर्ण PR, $PR^2 = a^2 + b^2$ को संतुष्ट करता है। लेकिन $a^2 + b^2 = c^2$ है, इसलिए $PR^2 = c^2$ होगा, जिसका अर्थ है $PR = c$।

अब दोनों त्रिभुजों की तीनों भुजाएँ क्रमशः बराबर हैं: $a$ और $a$, $b$ और $b$, $c$ और $c$। यदि एक त्रिभुज की तीन भुजाएँ दूसरे त्रिभुज की तीन भुजाओं के बराबर हैं, तो दोनों त्रिभुज सर्वांगसम (congruent) होते हैं। इसलिए त्रिभुज ABC, त्रिभुज PQR के सर्वांगसम है, और त्रिभुज ABC का वह कोण जो भुजा $c$ के सम्मुख है, Q पर स्थित समकोण के बराबर है। अतः त्रिभुज ABC समकोण है।

## नियम का उपयोग कैसे करें

आप इस विलोम का उपयोग यह जाँचने के लिए कर सकते हैं कि कोई त्रिभुज समकोण है या नहीं। सबसे पहले, सबसे लंबी भुजा की पहचान करें। इसे $c$ मानिए। अन्य दो भुजाएँ $a$ और $b$ हैं। इसके बाद, $a$ और $b$ की लंबाइयों का वर्ग करें और इन दोनों वर्गों को एक साथ जोड़ें। फिर $c$ की लंबाई का वर्ग करें। यदि दोनों परिणाम बराबर हैं, तो त्रिभुज समकोण है। यदि वे बराबर नहीं हैं, तो त्रिभुज समकोण नहीं है। सबसे लंबी भुजा को $c$ के रूप में चुनना महत्वपूर्ण है, क्योंकि जाँच सबसे लंबी भुजा के आधार पर की जाती है।

## हल किया गया उदाहरण

कल्पना कीजिए कि एक बढ़ई खिड़की के लिए एक त्रिकोणीय ढाँचा बना रहा है। भुजाओं की लंबाइयाँ $6$ सेमी, $8$ सेमी और $10$ सेमी हैं। बढ़ई यह जानना चाहता है कि क्या सबसे लंबी भुजा के सम्मुख वाला कोना एकदम सटीक समकोण है।

सबसे लंबी भुजा $10$ सेमी है, इसलिए $c = 10$। अन्य दो भुजाएँ $6$ सेमी और $8$ सेमी हैं, इसलिए $a = 6$ और $b = 8$।
- $a^2 = 6 \times 6 = 36$
- $b^2 = 8 \times 8 = 64$
- $a^2 + b^2 = 36 + 64 = 100$
- $c^2 = 10 \times 10 = 100$

चूँकि $a^2 + b^2 = c^2$ है, इसलिए त्रिभुज समकोण है।

अब $5$ सेमी, $6$ सेमी और $8$ सेमी भुजाओं वाले एक त्रिभुज पर विचार करें। सबसे लंबी भुजा $8$ सेमी है, इसलिए $c = 8$। फिर $5^2 + 6^2 = 25 + 36 = 61$, जबकि $8^2 = 64$। चूँकि $61 \neq 64$ है, इसलिए यह त्रिभुज समकोण नहीं है।

## मुख्य बिंदु
- पाइथागोरस प्रमेय का विलोम कहता है कि यदि $a^2 + b^2 = c^2$ है, जहाँ $c$ सबसे लंबी भुजा है, तो त्रिभुज समकोण होता है।
- समकोण सबसे लंबी भुजा के सम्मुख होता है, जो कर्ण है।
- किसी त्रिभुज की जाँच करने के लिए, दो छोटी भुजाओं का वर्ग करें, उन्हें जोड़ें, और योग की तुलना सबसे लंबी भुजा के वर्ग से करें।
- यदि योग सबसे लंबी भुजा के वर्ग के बराबर नहीं है, तो त्रिभुज समकोण नहीं है।
- इस विलोम को इस नियम का उपयोग करके सिद्ध किया जा सकता है कि जिन दो त्रिभुजों की तीनों संगत भुजाएँ बराबर हों, वे सर्वांगसम होते हैं।