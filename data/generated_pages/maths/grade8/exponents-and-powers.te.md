---
{
  "concept": "Exponents and Powers",
  "slug": "exponents-and-powers",
  "grade": 8,
  "language": "te",
  "hand_edited": "2026-10-13: line-by-line hand audit against the English page, edited directly (both published and tagged copies): wrong word for power (energy sense) replaced with ghatam, wrong Milky Way number corrected, expression-vs-equation wording",
  "subject": "maths",
  "area": "Algebra",
  "model": "sarvam-105b",
  "settings": {
    "temperature": 0.3,
    "max_tokens": 8000,
    "reasoning_effort": "none"
  },
  "usage": {
    "completion_tokens": 1478,
    "prompt_tokens": 1772,
    "total_tokens": 3250,
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
  "generated_at": "2026-10-13T00:13:29",
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
    "words": 590,
    "target_words": [
      950,
      1300
    ],
    "untraceable_sections": 1,
    "ok": true,
    "tags_vs_english": "8/8",
    "localisation_problems": [],
    "held_then_hand_fixed": "2026-10-13: the pipeline held this page (the Telugu rewrote the Milky Way distance with an extra pair of zeros); corrected to the English number by hand and published"
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

# ఘాతాంకాలు మరియు ఘాతాలు

ఘాతాంకాలు మరియు ఘాతాలు (Exponents and powers) అనేవి పదే పదే గుణకారాన్ని (repeated multiplication) చిన్న రూపంలో రాయడానికి ఒక మార్గం. $2 \times 2 \times 2 \times 2$ అని రాయడానికి బదులుగా, మనం $2^4$ అని రాయవచ్చు. మన సౌర కుటుంబంలోని గ్రహాల మధ్య ఉన్న అపారమైన దూరాలను కొలవడం నుండి భూమి ద్రవ్యరాశిని అర్థం చేసుకోవడం వరకు, రోజువారీ జీవితంలో ఈ పద్ధతి చాలా ఉపయోగపడుతుంది. ఘాతాంకాలను ఎలా ఉపయోగించాలి, వాటి నియమాలు ఏమిటి, మరియు 10 యొక్క ఘాతాలను ఉపయోగించి చాలా పెద్ద సంఖ్యలను ఎలా రాయాలి అనేది ఈ పేజీ వివరిస్తుంది.

## $a^n$ మరియు ఘాతాంకాల నియమాలను అర్థం చేసుకోవడం

$n$ ను దానితోనే $a$ సార్లు గుణించినప్పుడు మనం $n^a$ అని రాస్తాము. ఉదాహరణకు, $2^4 = 2 \times 2 \times 2 \times 2 = 16$. ఇక్కడ $2$ అనేది ఆధారం (base) మరియు $4$ అనేది ఘాతాంకం (exponent), దీనిని ఘాతం (power) అని కూడా అంటారు. ఒకే ఆధారం ఉన్న ఘాతాలను గుణించినప్పుడు, మనం వాటి ఘాతాంకాలను కలుపుతాము. దీనిని $n^a \times n^b = n^{a+b}$ గా రాస్తారు, ఇక్కడ $n \neq 0$ మరియు $a$ మరియు $b$ లు లెక్కింపు సంఖ్యలు (counting numbers). ఒక ఘాతాన్ని మరొక ఘాతానికి పెంచినప్పుడు ఘాతాంకాలను గుణిస్తాము: $(n^a)^b = n^{a \times b}$.

అదేవిధంగా, ఒకే ఆధారం ఉన్న ఘాతాలను భాగించినప్పుడు, మనం వాటి ఘాతాంకాలను తీసివేస్తాము. ఇది మనకు $n^a \div n^b = n^{a-b}$ అనే నియమాన్ని ఇస్తుంది. ఉదాహరణకు, మనం $2^4$ యూనిట్ల పొడవు గల ఒక రేఖతో ప్రారంభించి, దానిని మూడుసార్లు సగానికి తగ్గించినట్లయితే, మనకు $2^4 \div 2^3 = 2^{4-3} = 2^1 = 2$ యూనిట్లు వస్తాయి.

## శూన్య మరియు రుణ ఘాతాంకాలు

ఘాతాంకం శూన్యం లేదా రుణంగా ఉన్నప్పుడు కూడా మనం ఘాతాల విలువను కనుగొనవచ్చు. పై మరియు కింది ఘాతాంకాలు సమానంగా ఉన్నప్పుడు, భాగహార నియమం $2^0 = 2^{a-a} = 2^a \div 2^a = 1$ ఇస్తుంది. కాబట్టి, $2^0 = 1$, మరియు సాధారణంగా ఏదైనా $x \neq 0$ కి $x^0 = 1$ అవుతుంది.

ఘాతాంకం రుణంగా ఉన్నప్పుడు, ఆ ఘాతం ఒక భిన్నాన్ని సూచిస్తుంది. ఉదాహరణకు, మనం $2^4$ యూనిట్ల పొడవు గల రేఖను ఐదుసార్లు సగానికి తగ్గించినట్లయితే, మనకు $2^4 \div 2^5 = 2^{(4-5)} = 2^{-1}$ యూనిట్లు వస్తాయి. దీనిని విస్తరించినప్పుడు, ఇది $\frac{1}{2^1} = \frac{1}{2}$ కి సమానం అవుతుంది. అదేవిధంగా, $10^{-3} = \frac{1}{10^3}$ మరియు $7^{-2} = \frac{1}{7^2}$. సాధారణంగా, $n^{-a} = \frac{1}{n^a}$ మరియు $n^a = \frac{1}{n^{-a}}$, ఇక్కడ $n \neq 0$.

## 10 యొక్క ఘాతాలతో పెద్ద సంఖ్యలను రాయడం

చాలా పెద్ద సంఖ్యలను రాయడం కష్టంగా ఉండవచ్చు మరియు తప్పులకు దారితీయవచ్చు. ఉదాహరణకు, సూర్యుడికి మరియు శని గ్రహానికి మధ్య దూరం $14,33,50,00,00,000$ మీటర్లు, మరియు మన పాలపుంత (Milky Way) గెలాక్సీ కేంద్రం నుండి సూర్యుడికి దూరం $30,00,00,00,00,00,00,00,00,000$ మీటర్లు. ఈ సంఖ్యలను చదవడానికి మరియు పోల్చడానికి సులభంగా చేయడానికి, మనం శాస్త్రీయ సంజ్ఞామానాన్ని (scientific notation) ఉపయోగించవచ్చు.

శాస్త్రీయ సంజ్ఞామానంలో, మనం ఒక సంఖ్యను $x \times 10^y$ గా రాస్తాము, ఇక్కడ $1 \leq x < 10$ మరియు $y$ అనేది ఒక పూర్ణాంకం (integer). ఉదాహరణకు, $80,00,000$ ను $8 \times 10^6$ గా రాయవచ్చు. ఘాతాంకం చాలా ముఖ్యమైనది ఎందుకంటే ఆ సంఖ్య ఎంత పెద్దదో అది మనకు చెబుతుంది: $8 \times 10^6$ లో 7 అంకెలు (digits) ఉంటాయి, ఇది ఘాతాంకం కంటే ఒకటి ఎక్కువ. $2 \times 10^7$ లోని 2 ను 3 కి మార్చడం వల్ల సంఖ్య సగం పెరుగుతుంది, కానీ 7 ను 8 కి మార్చడం వల్ల అది 10 రెట్లు పెద్దది అవుతుంది.

## సాధించిన ఉదాహరణ

ఒక రాశిని (expression) సరళీకృతం చేయడానికి ఘాతాంకాల నియమాలను వర్తింపజేద్దాం. $2^{-4} \times 2^7$ రాశిని పరిశీలిద్దాం. ఒకే ఆధారం ఉన్న ఘాతాలను గుణించే నియమాన్ని ఉపయోగించి, మనం ఘాతాంకాలను కలుపుతాము: $2^{-4} \times 2^7 = 2^{-4+7} = 2^3 = 8$.

## ముఖ్య అంశాలు
- ఘాతాంకాలు $2^4 = 2 \times 2 \times 2 \times 2 = 16$ వంటి పదే పదే గుణకారాన్ని సూచిస్తాయి.
- ఒకే ఆధారం ఉన్న ఘాతాలను గుణించినప్పుడు, ఘాతాంకాలను కలపండి: $n^a \times n^b = n^{a+b}$.
- ఒకే ఆధారం ఉన్న ఘాతాలను భాగించినప్పుడు, ఘాతాంకాలను తీసివేయండి: $n^a \div n^b = n^{a-b}$.
- ఒక ఘాతాన్ని మరొక ఘాతానికి పెంచడానికి, ఘాతాంకాలను గుణించండి: $(n^a)^b = n^{a \times b}$.
- సున్నా కాని ఏ సంఖ్యనైనా సున్నా ఘాతానికి పెంచితే అది $1$ కి సమానం అవుతుంది: $n^0 = 1$.
- రుణ ఘాతాంకం విలోమాన్ని (reciprocal) సూచిస్తుంది: $n^{-a} = \frac{1}{n^a}$.
- శాస్త్రీయ సంజ్ఞామానం సంఖ్యలను $x \times 10^y$ గా రాస్తుంది, ఇక్కడ $1 \leq x < 10$ మరియు $y$ అనేది ఒక పూర్ణాంకం.
