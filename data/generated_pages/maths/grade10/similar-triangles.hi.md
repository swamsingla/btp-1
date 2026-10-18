---
{
  "concept": "Similar Triangles",
  "slug": "similar-triangles",
  "grade": 10,
  "language": "hi",
  "subject": "maths",
  "area": "Geometry",
  "model": "sarvam-105b",
  "settings": {
    "temperature": 0.3,
    "max_tokens": 8000,
    "reasoning_effort": "none"
  },
  "usage": {
    "completion_tokens": 1253,
    "prompt_tokens": 1579,
    "total_tokens": 2832,
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
  "generated_at": "2026-10-17T22:56:28",
  "source_grade": 10,
  "grade_delta": 0,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g10_maths_chapter6_021",
      "chapter": "chapter6",
      "section": "6.4 Criteria for Similarity of Triangles"
    }
  ],
  "citation_check": {
    "cited": [
      "1"
    ],
    "invented_citations": [],
    "unused_sources": [],
    "explanatory_paragraphs_without_a_citation": 0,
    "words": 746,
    "target_words": [
      1000,
      1350
    ],
    "untraceable_sections": 0,
    "ok": true,
    "tags_vs_english": "20/20",
    "localisation_problems": [],
    "not_harvestable": [
      "brackets: 5/8 declared terms are not bracketed with their English word (['similarity', 'scale factor', 'aa similarity', 'sss similarity'])"
    ]
  },
  "terms": [
    "similarity",
    "corresponding sides",
    "corresponding angles",
    "scale factor",
    "aa similarity",
    "sss similarity",
    "sas similarity",
    "proportional"
  ]
}
---

# समरूप त्रिभुज

समरूप त्रिभुज ज्यामिति का एक महत्वपूर्ण आधार हैं, जो उन आकृतियों का वर्णन करते हैं जिनकी आकृति (shape) बिल्कुल समान होती है लेकिन माप (size) में भिन्न हो सकती है। जब दो त्रिभुज समरूप होते हैं, तो उनके संगत कोण (corresponding angles) बराबर होते हैं और उनकी संगत भुजाएं (corresponding sides) एक ही अनुपात (ratio) या समानुपात (proportion) में होती हैं। यह अवधारणा आवश्यक है क्योंकि यह हमें पैमाने, दूरी और ऊंचाई से जुड़ी जटिल समस्याओं को एक सुसंगत अनुपात के माध्यम से ज्ञात मापों से जोड़कर हल करने की अनुमति देती है।

## प्रतीकात्मक निरूपण

जब यह बताया जाता है कि दो त्रिभुज समरूप हैं, तो शीर्षों (vertices) का क्रम मायने रखता है। यह दर्शाने के लिए कि एक त्रिभुज दूसरे के समरूप है, प्रतीक ‘$\sim$’ का उपयोग किया जाता है। उदाहरण के लिए, यदि $\Delta$ ABC, $\Delta$ DEF के समरूप है, तो इसका अर्थ है कि शीर्ष A, शीर्ष D से मेल खाता है, B, E से मेल खाता है, और C, F से मेल खाता है। परिणामस्वरूप, समरूपता को $\Delta$ ABC $\sim$ $\Delta$ DEF के रूप में लिखा जाता है और 'त्रिभुज ABC त्रिभुज DEF के समरूप है' के रूप में पढ़ा जाता है। प्रतीकात्मक कथन लिखते समय इस सही शीर्ष पत्राचार को बनाए रखना महत्वपूर्ण है। आप शायद पहले से ही जानते होंगे कि सर्वांगसमता (congruence) 'सर्वांगसम है' के लिए प्रतीक ‘$\cong$’ का उपयोग करती है, लेकिन यहाँ समरूपता के लिए प्रतीक $\sim$ है।

## AAA (या AA) समरूपता मानदंड

AAA मानदंड बताता है कि यदि दो त्रिभुजों के संगत कोण बराबर हैं, तो उनकी संगत भुजाएं एक ही अनुपात में होती हैं। इसका मतलब है कि यदि $\angle A = \angle D$, $\angle B = \angle E$, और $\angle C = \angle F$ है, तो $\frac{\mathrm{AB}}{\mathrm{DE}} = \frac{\mathrm{BC}}{\mathrm{EF}} = \frac{\mathrm{CA}}{\mathrm{FD}}$। त्रिभुज के कोण योग गुण के कारण, यह जानना पर्याप्त है कि दो कोण बराबर हैं, क्योंकि तीसरा कोण स्वचालित रूप से बराबर होगा, जिससे AA मानदंड प्राप्त होता है।

## SSS समरूपता मानदंड

SSS मानदंड बताता है कि यदि एक त्रिभुज की भुजाएं दूसरे त्रिभुज की भुजाओं के समानुपाती (proportional) हैं, तो उनके संगत कोण बराबर होते हैं। उदाहरण के लिए, यदि $\frac{\mathrm{AB}}{\mathrm{DE}} = \frac{\mathrm{BC}}{\mathrm{EF}} = \frac{\mathrm{CA}}{\mathrm{FD}}$ है, तो $\Delta$ ABC $\sim$ $\Delta$ DEF। यह मानदंड सीधे तौर पर यह दर्शाता है कि संगत कोण समान होने चाहिए, जिससे दो त्रिभुज समरूप हो जाते हैं।

## SAS समरूपता मानदंड

SAS मानदंड बताता है कि यदि एक त्रिभुज का एक कोण दूसरे त्रिभुज के एक कोण के बराबर है और इन कोणों को बनाने वाली भुजाएं समानुपाती हैं, तो दो त्रिभुज समरूप होते हैं। उदाहरण के लिए, यदि $\frac{\mathrm{AB}}{\mathrm{DE}} = \frac{\mathrm{AC}}{\mathrm{DF}}$ और $\angle \mathrm{A} = \angle \mathrm{D}$ है, तो $\Delta$ ABC $\sim$ $\Delta$ DEF।

## हल किया गया उदाहरण

AA मानदंड के एक व्यावहारिक अनुप्रयोग पर विचार करें। कल्पना करें कि एक लड़की एक लैंप-पोस्ट से दूर जा रही है। लैंप-पोस्ट AB जमीन से 3.6 m ऊपर है, और लड़की CD की ऊंचाई 0.9 m है। यदि लड़की 1.2 m/s की गति से चलती है, तो हम 4 सेकंड के बाद उसकी परछाई DE की लंबाई ज्ञात कर सकते हैं। सबसे पहले, लड़की द्वारा चली गई दूरी की गणना करें: $1.2 \times 4 = 4.8$ m। $\Delta$ ABE और $\Delta$ CDE में, $\angle$ B और $\angle$ D दोनों $90^\circ$ हैं क्योंकि लैंप-पोस्ट और लड़की दोनों जमीन के लंबवत खड़े हैं, और $\angle$ E दोनों त्रिभुजों में एक ही कोण है। इसलिए, AA समरूपता मानदंड के अनुसार, $\Delta$ ABE $\sim$ $\Delta$ CDE। समानुपाती भुजाओं का उपयोग करते हुए, हम समीकरण $\frac{4.8 + x}{x} = \frac{3.6}{0.9}$ बनाते हैं। $x$ के लिए हल करने पर, हमें $4.8 + x = 4x$ मिलता है, जो सरल होकर $3x = 4.8$ हो जाता है, जिससे $x = 1.6$ प्राप्त होता है। इस प्रकार, 4 सेकंड के बाद उसकी परछाई की लंबाई 1.6 m है।

## मुख्य बिंदु
- समरूप त्रिभुजों में समान संगत कोण और समानुपाती संगत भुजाएं होती हैं।
- समरूपता कथन में शीर्षों का क्रम सही पत्राचार को दर्शाना चाहिए।
- AAA (या AA), SAS, और SSS समरूपता साबित करने के तीन मानदंड हैं।
- AA मानदंड के लिए, समरूपता स्थापित करने के लिए दो समान कोण पर्याप्त हैं।
- SSS मानदंड के लिए, समानुपाती भुजाएं समान संगत कोणों की गारंटी देती हैं।
- SAS मानदंड के लिए, एक कोण का बराबर होना और उस कोण को बनाने वाली भुजाओं का समानुपाती होना समरूपता स्थापित करता है।