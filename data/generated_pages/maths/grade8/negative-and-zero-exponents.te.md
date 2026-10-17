---
{
  "concept": "Negative and Zero Exponents",
  "slug": "negative-and-zero-exponents",
  "grade": 8,
  "language": "te",
  "hand_edited": "2026-10-13: line-by-line hand audit against the English page, edited directly (both published and tagged copies): base term, cancel wording, expression-vs-equation wording, units translated",
  "subject": "maths",
  "area": "Algebra",
  "model": "sarvam-105b",
  "settings": {
    "temperature": 0.3,
    "max_tokens": 8000,
    "reasoning_effort": "none"
  },
  "usage": {
    "completion_tokens": 1237,
    "prompt_tokens": 1574,
    "total_tokens": 2811,
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
  "generated_at": "2026-10-13T00:14:02",
  "source_grade": 8,
  "grade_delta": 0,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g8_maths_part1_chapter6_025",
      "chapter": "chapter6",
      "section": "6.3 Mind the Mistake, Mend the Mistake"
    },
    {
      "ref": "S2",
      "passage_id": "g8_maths_part1_chapter2_005",
      "chapter": "chapter2",
      "section": "2.2 Exponential Notation and Operations"
    },
    {
      "ref": "S3",
      "passage_id": "g8_maths_part1_chapter2_015",
      "chapter": "chapter2",
      "section": "2.3 The Other Side of Powers"
    }
  ],
  "citation_check": {
    "cited": [
      "2",
      "3"
    ],
    "invented_citations": [],
    "unused_sources": [
      "1"
    ],
    "explanatory_paragraphs_without_a_citation": 0,
    "words": 471,
    "target_words": [
      950,
      1300
    ],
    "untraceable_sections": 0,
    "ok": true,
    "tags_vs_english": "14/14",
    "localisation_problems": [],
    "not_harvestable": [
      "brackets: 3/7 declared terms are not bracketed with their English word (['base', 'exponent', 'laws of exponents'])"
    ]
  },
  "terms": [
    "exponents",
    "powers",
    "base",
    "exponent",
    "standard form",
    "scientific notation",
    "laws of exponents"
  ]
}
---

# రుణ మరియు శూన్య ఘాతాంకాలు

ఈ అధ్యాయంలో ఇంతకు ముందు మీరు ఘాతాలు (powers) మరియు ఘాతాంకాల (exponents) గురించి నేర్చుకున్నారు. $5^4$ అంటే 5 ని 4 సార్లు గుణించగా 625 వస్తుందని మీకు తెలుసు. ఘాతాంకాలు లెక్కింపు సంఖ్యలు (counting numbers) అయినప్పుడు ఘాతాలను గుణించడానికి మరియు భాగించడానికి ఘాతాంకాల నియమాలను ఎలా ఉపయోగించాలో కూడా మీకు తెలుసు. అయితే, ఒక చిన్న ఘాతాన్ని పెద్ద ఘాతంతో భాగించవలసి వచ్చినప్పుడు లేదా ఒక సంఖ్యను అదే సంఖ్యతో భాగించినప్పుడు ఏమి జరుగుతుంది? ఈ ప్రశ్నలకు సమాధానాలను ఈ పేజీ వివరిస్తుంది, శూన్య మరియు రుణ ఘాతాంకాలను మీకు పరిచయం చేస్తుంది.

## శూన్య ఘాతాంకాల నియమం

$x^a \times x^b = x^{a+b}$ మరియు $x^a \div x^b = x^{a-b}$ అని మీకు ఇప్పటికే తెలుసు. కానీ ఘాతాంకాలు సమానంగా ఉన్నప్పుడు ఏమి జరుగుతుంది? మీరు $2^4$ ని $2^4$ తో భాగిస్తే, మీకు 1 వస్తుంది, ఎందుకంటే పైన మరియు కింద ఉన్నవి కొట్టివేయబడతాయి. ఘాతాంకాల నియమాన్ని ఉపయోగించి, $2^4 \div 2^4 = 2^{4-4} = 2^0$. దీని అర్థం $2^0$ అనేది 1 కి సమానంగా ఉండాలి. ఈ నియమం ఏదైనా శూన్యేతర ఆధారం (non-zero base) $x$ మరియు ఏదైనా లెక్కింపు సంఖ్య $a$ కి వర్తిస్తుంది, కాబట్టి $x^a \div x^a = x^0 = 1$, ఇక్కడ $x \neq 0$.

## రుణ ఘాతాంకాల నియమం

మీరు $2^4$ ని $2^5$ తో భాగిస్తే ఏమి జరుగుతుంది? మీరు దాన్ని విస్తరిస్తే, మీకు $\frac{2 \times 2 \times 2 \times 2}{2 \times 2 \times 2 \times 2 \times 2}$ వస్తుంది, ఇది $\frac{1}{2}$ కి లేదా $\frac{1}{2^1}$ కి సరళీకృతం అవుతుంది. ఘాతాంకాల నియమాన్ని ఉపయోగించి, $2^4 \div 2^5 = 2^{4-5} = 2^{-1}$. కాబట్టి, $2^{-1} = \frac{1}{2}$. ఇదే తర్కం ఏదైనా రుణ ఘాతాంకానికి వర్తిస్తుంది: $10^{-3} = \frac{1}{10^3}$, $7^{-2} = \frac{1}{7^2}$, మరియు $2^{-6} = \frac{1}{2^6}$. సాధారణంగా, ఏదైనా శూన్యేతర ఆధారం $n$ మరియు ధన పూర్ణాంకం $a$ కి, $n^{-a} = \frac{1}{n^a}$. ఈ నియమం వ్యతిరేక దిశలో కూడా పనిచేస్తుంది: $10^3 = \frac{1}{10^{-3}}$ మరియు $7^2 = \frac{1}{7^{-2}}$.

## ప్రామాణిక రూపం మరియు శాస్త్రీయ సంజ్ఞామానం

సంఖ్యలు చాలా పెద్దవిగా లేదా చాలా చిన్నవిగా మారినప్పుడు, వాటిని పూర్తిగా రాయడం కష్టమవుతుంది. ఉదాహరణకు, ఒక కాగితం మందం మొదట $0.001$ సెం.మీ ఉండవచ్చు. ప్రతి మడతతో మందం రెట్టింపు అవుతుంది, కాబట్టి మీరు దానిని 7 సార్లు మడిస్తే, మందం $0.001 \times 2^7 = 0.128$ సెం.మీ అవుతుంది. ప్రామాణిక రూపం (Standard form), లేదా శాస్త్రీయ సంజ్ఞామానం (scientific notation), ఈ సంఖ్యలను సులభంగా రాయడానికి మనకు సహాయపడుతుంది. మనం $0.001$ ని $1 \times 10^{-3}$ గా రాస్తాము. ఎందుకంటే $10^{-3} = \frac{1}{10^3} = \frac{1}{1000} = 0.001$. కాబట్టి, 7 మడతల తర్వాత మందం $1 \times 10^{-3} \times 2^7$ సెం.మీ, ఇది ప్రామాణిక రూపంలో $1.28 \times 10^{-1}$ సెం.మీ అవుతుంది.

## సాధించిన ఉదాహరణ

ఈ నియమాలను ఒక సమస్యకు వర్తింపజేద్దాం. మనం $2^3 \times 2^{-5}$ అనే రాశిని సరళీకృతం చేయవలసి ఉందనుకుందాం. ఘాతాంకాల నియమాన్ని ఉపయోగించి, మనం ఘాతాంకాలను కలుపుతాము: $2^{3 + (-5)} = 2^{-2}$. మనకు రుణ ఘాతాంకం ఉంది కాబట్టి, మనం విలోమాన్ని (reciprocal) తీసుకోవడం ద్వారా దానిని ధన ఘాతాంకంగా మారుస్తాము: $2^{-2} = \frac{1}{2^2} = \frac{1}{4}$.

## ముఖ్య అంశాలు
- ఏదైనా శూన్యేతర సంఖ్యను శూన్య ఘాతానికి పెంచితే 1 వస్తుంది: $x^0 = 1$, ఇక్కడ $x \neq 0$.
- రుణ ఘాతాంకం అంటే ధన ఘాతానికి పెంచిన ఆధారం యొక్క విలోమం: $n^{-a} = \frac{1}{n^a}$, ఇక్కడ $n \neq 0$.
- ప్రామాణిక రూపం చాలా పెద్ద లేదా చాలా చిన్న సంఖ్యలను సులభంగా రాయడానికి 10 యొక్క ఘాతాలను ఉపయోగిస్తుంది.
- శూన్య మరియు రుణ ఘాతాంకాలను ఉపయోగించినప్పుడు కూడా ఘాతాంకాల నియమాలు వర్తిస్తాయి.
