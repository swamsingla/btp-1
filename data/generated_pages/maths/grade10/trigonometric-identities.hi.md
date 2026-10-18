---
{
  "concept": "Trigonometric Identities",
  "slug": "trigonometric-identities",
  "grade": 10,
  "language": "hi",
  "subject": "maths",
  "area": "Trigonometry",
  "model": "sarvam-105b",
  "settings": {
    "temperature": 0.3,
    "max_tokens": 8000,
    "reasoning_effort": "none"
  },
  "usage": {
    "completion_tokens": 1682,
    "prompt_tokens": 1903,
    "total_tokens": 3585,
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
  "generated_at": "2026-10-17T22:58:12",
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
    "words": 1107,
    "target_words": [
      1000,
      1350
    ],
    "untraceable_sections": 1,
    "ok": true,
    "tags_vs_english": "16/16",
    "localisation_problems": [],
    "not_harvestable": [
      "brackets: 8/9 declared terms are not bracketed with their English word (['trigonometric identity', 'sine', 'cosine', 'tangent'])"
    ]
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

# त्रिकोणमितीय सर्वसमिकाएँ

सर्वसमिका (identity) एक ऐसा समीकरण है जो इसके चरों के सभी संभव मानों के लिए सत्य होता है। इसी प्रकार, त्रिकोणमितीय सर्वसमिका (trigonometric identity) किसी कोण के त्रिकोणमितीय अनुपातों से जुड़ा ऐसा समीकरण है जो उस कोण के हर मान के लिए सत्य होता है। ये सर्वसमिकाएँ त्रिकोणमिति की बुनियादी इकाइयाँ हैं। इनसे हम एक त्रिकोणमितीय अनुपात को दूसरे के पदों में व्यक्त कर सकते हैं। यदि हम किसी कोण के एक अनुपात का मान जानते हैं, तो इन सर्वसमिकाओं की सहायता से उसी कोण के अन्य सभी अनुपातों के सटीक मान ज्ञात कर सकते हैं।

## पाइथागोरस प्रमेय पर आधारित आधार

सबसे महत्वपूर्ण त्रिकोणमितीय सर्वसमिकाएँ सीधे पाइथागोरस प्रमेय से प्राप्त होती हैं। एक समकोण त्रिभुज पर विचार करें जिसमें समकोण शीर्ष $B$ पर है। पाइथागोरस प्रमेय के अनुसार, कर्ण का वर्ग अन्य दो भुजाओं के वर्गों के योग के बराबर होता है:
$$
AB^2 + BC^2 = AC^2
$$

यदि हम पूरे समीकरण को $AC^2$ से भाग दें, तो हमें
$$
\left(\frac{AB}{AC}\right)^2 + \left(\frac{BC}{AC}\right)^2 = 1
$$
मिलता है, जो
$$
\cos^2 A + \sin^2 A = 1
$$
के बराबर है। यह पहली मूलभूत सर्वसमिका है, और यह प्रत्येक न्यून कोण $A$ के लिए सत्य है।

## दूसरी और तीसरी सर्वसमिकाएँ

पाइथागोरस समीकरण को पहले कोण $A$ की सन्निकट भुजा के वर्ग से, और फिर कोण $A$ की विपरीत भुजा के वर्ग से भाग देकर हम दो और सर्वसमिकाएँ प्राप्त कर सकते हैं।

$AB^2 + BC^2 = AC^2$ को $AB^2$ से भाग देने पर दूसरी सर्वसमिका मिलती है:
$$
1 + \tan^2 A = \sec^2 A
$$
$BC^2$ से भाग देने पर तीसरी सर्वसमिका मिलती है:
$$
\cot^2 A + 1 = \csc^2 A
$$

यहाँ $\tan$ स्पर्शज्या (tangent), $\sec$ सेकेंट (secant), $\cot$ कोटैंजेंट (cotangent) और $\csc$ कोसेकेंट (cosecant) को दर्शाते हैं; $\sin$ ज्या (sine) और $\cos$ कोज्या (cosine) हैं।

## सर्वसमिकाओं से छूटे हुए अनुपात ज्ञात करना

जब हमें त्रिकोणमितीय अनुपातों के सटीक मान ज्ञात करने हों, तब ये सर्वसमिकाएँ बहुत उपयोगी होती हैं। मान लीजिए $\tan A = \frac{1}{\sqrt{3}}$ दिया है।

दूसरी सर्वसमिका से हम $\sec A$ ज्ञात कर सकते हैं:
$$
\sec^2 A = 1 + \tan^2 A = 1 + \frac{1}{3} = \frac{4}{3}, \quad \text{अतः} \quad \sec A = \frac{2}{\sqrt{3}}
$$

सेकेंट का व्युत्क्रम लेकर हमें कोण $A$ की कोज्या मिलती है: $\cos A = \frac{\sqrt{3}}{2}$।

अंत में, पहली सर्वसमिका से हम $\sin A$ ज्ञात करते हैं:
$$
\sin^2 A = 1 - \cos^2 A = 1 - \frac{3}{4} = \frac{1}{4}, \quad \text{अतः} \quad \sin A = \frac{1}{2}
$$
इससे $\csc A = 2$ प्राप्त होता है।

## अनुपातों को ज्या के पदों में व्यक्त करना

पहली सर्वसमिका का उपयोग करके हम अन्य अनुपातों को केवल किसी कोण की ज्या के पदों में भी लिख सकते हैं। सर्वसमिका को पुनर्व्यवस्थित करने पर $\cos^2 A = 1 - \sin^2 A$ मिलता है।

दोनों पक्षों का वर्गमूल लेने पर, और यह याद रखते हुए कि न्यून कोण के लिए $\cos A$ धनात्मक होता है, हमें
$$
\cos A = \sqrt{1 - \sin^2 A}
$$
मिलता है।

इसकी सहायता से हम लिख सकते हैं
$$
\tan A = \frac{\sin A}{\sqrt{1 - \sin^2 A}}, \qquad \sec A = \frac{1}{\sqrt{1 - \sin^2 A}}
$$

## अधिक जटिल सर्वसमिकाओं को सिद्ध करना

इन मूल सर्वसमिकाओं की सहायता से अधिक जटिल त्रिकोणमितीय समीकरण भी सिद्ध किए जा सकते हैं। उदाहरण के लिए, हम सिद्ध कर सकते हैं कि
$$
\sec A \, (1 - \sin A)(\sec A + \tan A) = 1
$$

हम सेकेंट और स्पर्शज्या को ज्या और कोज्या के पदों में लिखते हैं, और अंतिम कोष्ठक को एक भिन्न में मिला देते हैं:
$$
\text{बायाँ पक्ष} = \frac{1}{\cos A} (1 - \sin A) \left(\frac{1}{\cos A} + \frac{\sin A}{\cos A}\right) = \frac{(1 - \sin A)(1 + \sin A)}{\cos^2 A} = \frac{1 - \sin^2 A}{\cos^2 A}
$$

पहली सर्वसमिका से $1 - \sin^2 A = \cos^2 A$ है। इसे रखने पर हमें $\frac{\cos^2 A}{\cos^2 A} = 1 = \text{दायाँ पक्ष}$ मिलता है।

## हल किया गया उदाहरण

आइए सर्वसमिकाओं की सहायता से एक न्यून कोण $A$ के त्रिकोणमितीय अनुपातों के सटीक मान ज्ञात करें, जहाँ $\tan A = \frac{4}{3}$ है।

सबसे पहले, दूसरी सर्वसमिका से $\sec A$ ज्ञात करते हैं:
$$
\sec^2 A = 1 + \tan^2 A = 1 + \frac{16}{9} = \frac{25}{9}, \quad \text{अतः} \quad \sec A = \frac{5}{3}
$$

इसके बाद, सेकेंट का व्युत्क्रम लेकर $\cos A$ ज्ञात करते हैं: $\cos A = \frac{3}{5}$।

अंत में, पहली सर्वसमिका से $\sin A$ ज्ञात करते हैं:
$$
\sin^2 A = 1 - \cos^2 A = 1 - \frac{9}{25} = \frac{16}{25}, \quad \text{अतः} \quad \sin A = \frac{4}{5}
$$

शेष अनुपात इनके व्युत्क्रम हैं: $\cot A = \frac{3}{4}$ और $\csc A = \frac{5}{4}$।

## मुख्य बिंदु

*   त्रिकोणमितीय सर्वसमिका त्रिकोणमितीय अनुपातों से जुड़ा ऐसा समीकरण है जो कोण के सभी मानों के लिए सत्य होता है।
*   तीन मूलभूत सर्वसमिकाएँ $\sin^2\theta + \cos^2\theta = 1$, $1 + \tan^2\theta = \sec^2\theta$ और $1 + \cot^2\theta = \csc^2\theta$ हैं।
*   इन सर्वसमिकाओं से किसी भी एक त्रिकोणमितीय अनुपात को दूसरे के पदों में व्यक्त किया जा सकता है।
*   मूल परिभाषाओं को रखकर और सरल करके इनसे अधिक जटिल त्रिकोणमितीय समीकरण भी सिद्ध किए जाते हैं।
*   ध्यान दें कि $\tan A = \frac{\sin A}{\cos A}$ और $\cot A = \frac{\cos A}{\sin A}$ है, जो व्यंजकों को फिर से लिखने में मदद करता है।
