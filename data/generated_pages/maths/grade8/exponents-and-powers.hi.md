---
{
  "concept": "Exponents and Powers",
  "slug": "exponents-and-powers",
  "grade": 8,
  "language": "hi",
  "hand_edited": "2026-10-13: line-by-line hand audit against the English page, edited directly: untranslated scientific notation, integer and counting numbers rendered in Hindi, garbled zero-power key point rewritten.",
  "subject": "maths",
  "area": "Algebra",
  "model": "sarvam-105b",
  "settings": {
    "temperature": 0.3,
    "max_tokens": 8000,
    "reasoning_effort": "none"
  },
  "usage": {
    "completion_tokens": 1439,
    "prompt_tokens": 1789,
    "total_tokens": 3228,
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
  "generated_at": "2026-10-12T23:49:58",
  "source_grade": 8,
  "grade_delta": 0,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g8_maths_part1_chapter2_015",
      "chapter": "chapter2",
      "section": "2.3 The Other Side of Powers"
    },
    {
      "ref": "S2",
      "passage_id": "g8_maths_part1_chapter2_019",
      "chapter": "chapter2",
      "section": "2.4 Powers of 10"
    },
    {
      "ref": "S3",
      "passage_id": "g8_maths_part2_chapter2_019",
      "chapter": "chapter2",
      "section": "2.6 A Long-Standing Open Problem"
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
    "words": 768,
    "target_words": [
      950,
      1300
    ],
    "untraceable_sections": 1,
    "ok": true,
    "tags_vs_english": "8/8",
    "localisation_problems": [],
    "not_harvestable": [
      "brackets: 6/10 declared terms are not bracketed with their English word (['scientific notation', 'coefficient', 'counting numbers', 'integers'])"
    ]
  },
  "terms": [
    "exponent",
    "power",
    "base",
    "scientific notation",
    "coefficient",
    "reciprocal",
    "counting numbers",
    "integers",
    "standard form",
    "indian numerals"
  ]
}
---

# घातांक और घात

घातांक और घात बार-बार गुणा करने को छोटे रूप में लिखने का एक तरीका है। $2 \times 2 \times 2 \times 2$ लिखने के बजाय, हम $2^4$ लिख सकते हैं। यह संकेतन (notation) हमारे दैनिक जीवन में बहुत उपयोगी है, हमारे सौर मंडल में ग्रहों के बीच की विशाल दूरियों को मापने से लेकर पृथ्वी के द्रव्यमान को समझने तक। यह पृष्ठ बताएगा कि घातांकों का उपयोग कैसे करें, उनके नियम क्या हैं, और 10 की घातों का उपयोग करके बहुत बड़ी संख्याओं को कैसे लिखें।

## $a^n$ और घातांक के नियमों को समझना

हम $n$ को स्वयं से $a$ बार गुणा करने के लिए $n^a$ लिखते हैं। उदाहरण के लिए, $2^4 = 2 \times 2 \times 2 \times 2 = 16$। यहाँ $2$ आधार (base) है और $4$ घातांक (exponent) है, जिसे घात (power) भी कहा जाता है। जब हम समान आधार वाली घातों को गुणा करते हैं, तो हम उनके घातांकों को जोड़ते हैं। इसे $n^a \times n^b = n^{a+b}$ के रूप में लिखा जाता है, जहाँ $n \neq 0$ और $a$ तथा $b$ गिनती की संख्याएँ (counting numbers) हैं। एक घात की घात लेने पर घातांक गुणा हो जाते हैं: $(n^a)^b = n^{a \times b}$।

इसी तरह, जब हम समान आधार वाली घातों को विभाजित करते हैं, तो हम उनके घातांकों को घटाते हैं। इससे हमें यह नियम मिलता है: $n^a \div n^b = n^{a-b}$। उदाहरण के लिए, यदि हम $2^4$ इकाइयों की लंबाई वाली एक रेखा से शुरू करते हैं और इसे तीन बार आधा करते हैं, तो हमें $2^4 \div 2^3 = 2^{4-3} = 2^1 = 2$ इकाइयाँ मिलती हैं।

## शून्य और ऋणात्मक घातांक

जब घातांक शून्य या ऋणात्मक होता है, तब भी हम घातों का मान ज्ञात कर सकते हैं। जब ऊपर और नीचे के घातांक समान होते हैं, तो भाग का नियम हमें $2^0 = 2^{a-a} = 2^a \div 2^a = 1$ देता है। इसलिए, $2^0 = 1$, और सामान्यतः किसी भी $x \neq 0$ के लिए $x^0 = 1$ होता है।

जब घातांक ऋणात्मक होता है, तो घात एक भिन्न (fraction) को दर्शाती है। उदाहरण के लिए, यदि हम $2^4$ इकाइयों की लंबाई वाली एक रेखा को पाँच बार आधा करते हैं, तो हमें $2^4 \div 2^5 = 2^{(4-5)} = 2^{-1}$ इकाइयाँ मिलती हैं। जब इसे विस्तारित किया जाता है, तो यह $\frac{1}{2^1} = \frac{1}{2}$ के बराबर होता है। इसी तरह, $10^{-3} = \frac{1}{10^3}$ और $7^{-2} = \frac{1}{7^2}$। सामान्यतः, $n^{-a} = \frac{1}{n^a}$ और $n^a = \frac{1}{n^{-a}}$, जहाँ $n \neq 0$।

## 10 की घातों के साथ बड़ी संख्याएँ लिखना

बहुत बड़ी संख्याएँ लिखना कठिन हो सकता है और इससे गलतियाँ हो सकती हैं। उदाहरण के लिए, सूर्य और शनि के बीच की दूरी $14,33,50,00,00,000$ मीटर है, और सूर्य हमारी आकाशगंगा (Milky Way galaxy) के केंद्र से $30,00,00,00,00,00,00,00,00,000$ मीटर दूर है। इन संख्याओं को पढ़ने और उनकी तुलना करने में आसान बनाने के लिए, हम वैज्ञानिक संकेतन (scientific notation) का उपयोग कर सकते हैं।

वैज्ञानिक संकेतन में, हम एक संख्या को $x \times 10^y$ के रूप में लिखते हैं, जहाँ $1 \leq x < 10$ और $y$ एक पूर्णांक (integer) है। उदाहरण के लिए, $80,00,000$ को $8 \times 10^6$ के रूप में लिखा जा सकता है। घातांक बहुत महत्वपूर्ण है क्योंकि यह हमें बताता है कि संख्या कितनी बड़ी है: $8 \times 10^6$ में 7 अंक हैं, जो घातांक से एक अधिक है। $2 \times 10^7$ में 2 को 3 में बदलने से संख्या आधी बढ़ जाती है, लेकिन 7 को 8 में बदलने से यह 10 गुना बड़ी हो जाती है।

## हल किया गया उदाहरण

आइए एक व्यंजक (expression) को सरल बनाने के लिए घातांक के नियमों को लागू करें। व्यंजक $2^{-4} \times 2^7$ पर विचार करें। समान आधार वाली घातों को गुणा करने के नियम का उपयोग करते हुए, हम घातांकों को जोड़ते हैं: $2^{-4} \times 2^7 = 2^{-4+7} = 2^3 = 8$।

## मुख्य बिंदु
- घातांक बार-बार गुणा करने को दर्शाते हैं, जैसे कि $2^4 = 2 \times 2 \times 2 \times 2 = 16$।
- समान आधार वाली घातों को गुणा करते समय, घातांकों को जोड़ें: $n^a \times n^b = n^{a+b}$।
- समान आधार वाली घातों को विभाजित करते समय, घातांकों को घटाएँ: $n^a \div n^b = n^{a-b}$।
- एक घात की घात लेने के लिए, घातांकों को गुणा करें: $(n^a)^b = n^{a \times b}$।
- शून्य घात वाली किसी भी गैर-शून्य (non-zero) संख्या का मान $1$ होता है: $n^0 = 1$।
- एक ऋणात्मक घातांक व्युत्क्रम (reciprocal) को दर्शाता है: $n^{-a} = \frac{1}{n^a}$।
- वैज्ञानिक संकेतन संख्याओं को $x \times 10^y$ के रूप में लिखता है, जहाँ $1 \leq x < 10$ और $y$ एक पूर्णांक है।