---
{
  "concept": "Kite and Trapezium Properties",
  "slug": "kite-and-trapezium",
  "grade": 8,
  "language": "hi",
  "hand_edited": "2026-10-13: line-by-line hand audit against the English page, edited directly: parallel spelling mixed within the page standardised, transversal rendered with the grade 6-7 term, cm unit translated, 'one pair' grammar and summary sentence fixed.",
  "subject": "maths",
  "area": "Geometry",
  "model": "sarvam-105b",
  "settings": {
    "temperature": 0.3,
    "max_tokens": 8000,
    "reasoning_effort": "none"
  },
  "usage": {
    "completion_tokens": 1933,
    "prompt_tokens": 2049,
    "total_tokens": 3982,
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
  "generated_at": "2026-10-12T23:50:17",
  "source_grade": 8,
  "grade_delta": 0,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g8_maths_part1_chapter4_025",
      "chapter": "chapter4",
      "section": "4.6 Kite and Trapezium"
    },
    {
      "ref": "S2",
      "passage_id": "g8_maths_part1_chapter4_016",
      "chapter": "chapter4",
      "section": "4.3 More Quadrilaterals with Parallel Opposite Sides"
    },
    {
      "ref": "S3",
      "passage_id": "g8_maths_part1_chapter4_021",
      "chapter": "chapter4",
      "section": "4.4 Quadrilaterals with Equal Sidelengths"
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
    "words": 1016,
    "target_words": [
      950,
      1300
    ],
    "untraceable_sections": 1,
    "ok": true,
    "tags_vs_english": "9/9",
    "localisation_problems": [],
    "not_harvestable": [
      "brackets: 4/9 declared terms are not bracketed with their English word (['isosceles trapezium', 'diagonal', 'parallel sides', 'congruent triangles'])"
    ]
  },
  "terms": [
    "kite",
    "trapezium",
    "isosceles trapezium",
    "adjacent sides",
    "diagonal",
    "bisect",
    "transversal",
    "parallel sides",
    "congruent triangles"
  ]
}
---

# पतंग और समलंब के गुण

आपने पहले ही कई प्रकार के चतुर्भुजों जैसे कि वर्ग, आयत और समानांतर चतुर्भुज का अध्ययन किया है। इन सभी आकृतियों में समानांतर आमने-सामने की भुजाओं के जोड़े होते हैं। लेकिन सभी चतुर्भुज इस तरह व्यवहार नहीं करते हैं। इस पृष्ठ में, हम दो अन्य दिलचस्प चतुर्भुजों के बारे में जानेंगे: पतंग (kite) और समलंब (trapezium)। एक पतंग में कोई समानांतर भुजाएँ नहीं होती हैं, और एक समलंब में केवल एक जोड़ी समानांतर भुजाओं की ही गारंटी होती है।

## पतंग क्या है?

पतंग एक चतुर्भुज है जिसे $ABCD$ के रूप में दर्शाया जा सकता है जहाँ $AB = BC$, और $CD = DA$। इसका मतलब है कि आसन्न भुजाओं (adjacent sides) के दो जोड़े समान हैं।
**गुण 1:** एक पतंग में, विकर्ण $BD$, $\angle ABC$ और $\angle ADC$ को समद्विभाजित (bisect) करता है, और यह विकर्ण $AC$ को समद्विभाजित करता है, अर्थात, $AO = OC$, और इसके लंबवत (perpendicular) है।

ऐसा क्यों है, यह देखने के लिए मान लें कि विकर्ण $O$ पर मिलते हैं। पहले $\Delta ABD$ और $\Delta CBD$ पर विचार करें। हमारे पास $AB = CB$ और $AD = CD$ है, और $BD$ दोनों त्रिभुजों के लिए सामान्य है। इसलिए भुजा-भुजा-भुजा (SSS) शर्त द्वारा $\Delta ABD \cong \Delta CBD$ है। इस प्रकार $\angle ABD = \angle CBD$ और $\angle ADB = \angle CDB$, जिसका अर्थ है कि विकर्ण $BD$, $\angle ABC$ और $\angle ADC$ को समद्विभाजित करता है। अब $\Delta AOB$ और $\Delta COB$ पर विचार करें। हमारे पास $AB = CB$, $\angle ABO = \angle CBO$, और $BO$ सामान्य है, इसलिए भुजा-कोण-भुजा (SAS) शर्त द्वारा $\Delta AOB \cong \Delta COB$ है। अतः $AO = OC$ और $\angle AOB = \angle COB$ है। ये दोनों कोण एक सरल कोण (straight angle) बनाते हैं, इसलिए उनका योग $180^{\circ}$ होता है, और प्रत्येक $90^{\circ}$ है।

**हल किया गया उदाहरण:** एक पतंग $ABCD$ में जहाँ $AB = BC$ और $CD = DA$ है, मान लें कि $\angle ABD = 35^{\circ}$ है। चूँकि विकर्ण $BD$, $\angle ABC$ को समद्विभाजित करता है, $\angle CBD = 35^{\circ}$ और $\angle ABC = 70^{\circ}$ है। विकर्ण $O$ पर समकोण पर मिलते हैं, इसलिए $\Delta AOB$ में, $\angle BAO = 180^{\circ} - 90^{\circ} - 35^{\circ} = 55^{\circ}$ है।

## समलंब क्या है?

समलंब एक चतुर्भुज है जिसमें समानांतर आमने-सामने की भुजाओं का कम से कम एक जोड़ा होता है। यह एक समानांतर चतुर्भुज से अलग है, जिसमें समानांतर आमने-सामने की भुजाओं के दो जोड़े होते हैं।

**गुण 1:** एक समलंब में, प्रत्येक गैर-समानांतर भुजा के सिरों पर दो कोणों का योग $180^{\circ}$ होता है।

यदि $PQ$, $SR$ के समानांतर है, तो $\angle S + \angle P = 180^{\circ}$ और $\angle R + \angle Q = 180^{\circ}$ होता है। ऐसा इसलिए है क्योंकि ये कोण दो समानांतर रेखाओं को पार करने वाले तिर्यक रेखा (transversal) के एक ही तरफ के आंतरिक कोण हैं।

**हल किया गया उदाहरण:** एक समलंब $PQRS$ में जहाँ $PQ \parallel SR$ है, मान लें कि $\angle P = 110^{\circ}$ और $\angle Q = 80^{\circ}$ है। चूँकि $\angle S + \angle P = 180^{\circ}$, $\angle S = 180^{\circ} - 110^{\circ} = 70^{\circ}$ है। चूँकि $\angle R + \angle Q = 180^{\circ}$, $\angle R = 180^{\circ} - 80^{\circ} = 100^{\circ}$ है। चारों कोणों का योग $110^{\circ} + 80^{\circ} + 70^{\circ} + 100^{\circ} = 360^{\circ}$ होता है।

## समद्विबाहु समलंब क्या है?

जब एक समलंब की गैर-समानांतर भुजाओं की लंबाई समान होती है, तो उस समलंब को समद्विबाहु समलंब कहा जाता है।

**गुण 2:** एक समद्विबाहु समलंब में, समान भुजाओं के आमने-सामने के कोण समान होते हैं।

ऐसा क्यों है, यह देखने के लिए एक समद्विबाहु समलंब $UVWX$ पर विचार करें जहाँ $UV$, $XW$ के समानांतर है। $UV$ पर लंबवत रेखाखंड $XY$ और $WZ$ खींचें। चूँकि $XY$ और $WZ$ समानांतर रेखाओं $UV$ और $XW$ पर लंबवत हैं, चतुर्भुज $XWZY$ एक आयत है। इसका मतलब है कि $XY = WZ$ है। अब, $\Delta UXY$ और $\Delta VWZ$ पर विचार करें। हमारे पास $UX = VW$ (समान गैर-समानांतर भुजाएँ), $XY = WZ$, और $\angle UYX = \angle VZW = 90^{\circ}$ है। इसलिए, समकोण-कर्ण-भुजा (RHS) सर्वांगसमता शर्त द्वारा $\Delta UXY \cong \Delta VWZ$ है। यह साबित करता है कि $\angle U = \angle V$ है।

**हल किया गया उदाहरण:** एक समद्विबाहु समलंब में 8 सेमी की समान गैर-समानांतर भुजाएँ हैं। इन भुजाओं के आमने-सामने के कोण, $\angle U$ और $\angle V$, दोनों $100^{\circ}$ हैं (यहाँ $UV$ छोटी समानांतर भुजा है)। शेष कोण प्रत्येक $80^{\circ}$ होने चाहिए, क्योंकि $\angle U + \angle X = 180^{\circ}$ और $\angle V + \angle W = 180^{\circ}$ है।

## गुणों का सारांश

पतंग और समलंब की तुलना अन्य चतुर्भुजों से करना सहायक है। समानांतर चतुर्भुजों में समानांतर आमने-सामने की भुजाएँ होती हैं, और एक आयत एक विशेष प्रकार का समानांतर चतुर्भुज है जिसमें सभी कोण $90^{\circ}$ के बराबर होते हैं। एक समचतुर्भुज (rhombus) एक चतुर्भुज है जिसमें सभी भुजाओं की लंबाई समान होती है। प्रत्येक समचतुर्भुज एक समानांतर चतुर्भुज भी होता है, और समानांतर चतुर्भुज के गुण समचतुर्भुज के लिए भी सत्य होते हैं।

एक पतंग में आसन्न समान भुजाओं के दो जोड़े होते हैं और यह आम तौर पर एक समानांतर चतुर्भुज नहीं होता है (एक समचतुर्भुज एक पतंग और एक समानांतर चतुर्भुज दोनों होता है)। एक समलंब के लिए समानांतर आमने-सामने की भुजाओं का केवल एक जोड़ा होना पर्याप्त है। एक समद्विबाहु समलंब एक विशेष मामला है जहाँ गैर-समानांतर भुजाएँ समान होती हैं, जिससे आधार कोण भी समान हो जाते हैं।

## मुख्य बिंदु

*   एक पतंग एक चतुर्भुज है जिसमें आसन्न समान भुजाओं के दो जोड़े होते हैं, $AB = BC$ और $CD = DA$।
*   एक पतंग $ABCD$ में जहाँ $AB = BC$ और $CD = DA$ है, विकर्ण $BD$, $B$ और $D$ पर कोणों को समद्विभाजित करता है, और दूसरे विकर्ण $AC$ को समकोण पर समद्विभाजित करता है।
*   एक समलंब में समानांतर आमने-सामने की भुजाओं का कम से कम एक जोड़ा होता है।
*   एक समलंब में, प्रत्येक गैर-समानांतर भुजा के सिरों पर दो कोणों का योग $180^{\circ}$ होता है।
*   एक समद्विबाहु समलंब में समान गैर-समानांतर भुजाएँ होती हैं, और इन भुजाओं के आमने-सामने के कोण समान होते हैं।