---
{
  "concept": "Section Formula and Midpoint",
  "slug": "section-formula",
  "grade": 10,
  "language": "te",
  "subject": "maths",
  "area": "Coordinate Geometry",
  "model": "sarvam-105b",
  "settings": {
    "temperature": 0.3,
    "max_tokens": 8000,
    "reasoning_effort": "none"
  },
  "usage": {
    "completion_tokens": 1357,
    "prompt_tokens": 1684,
    "total_tokens": 3041,
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
  "generated_at": "2026-10-17T23:15:54",
  "source_grade": 10,
  "grade_delta": 0,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g10_maths_chapter7_013",
      "chapter": "chapter7",
      "section": "7.3 Section Formula"
    },
    {
      "ref": "S2",
      "passage_id": "g10_maths_chapter11_005",
      "chapter": "chapter11",
      "section": "11.1 Areas of Sector and Segment of a Circle"
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
    "words": 580,
    "target_words": [
      1000,
      1350
    ],
    "untraceable_sections": 0,
    "ok": true,
    "tags_vs_english": "16/16",
    "localisation_problems": []
  },
  "terms": [
    "section formula",
    "midpoint",
    "internal division",
    "ratio",
    "coordinates"
  ]
}
---

# విభజన సూత్రం మరియు మధ్య బిందువు

ఒక టెలిఫోన్ కంపెనీ A, B అనే రెండు ప్రదేశాల మధ్య ఒక రిలే టవర్‌ను ఏర్పాటు చేయాలనుకుంటోందని ఊహించుకోండి. ఆ టవర్‌కు B నుండి ఉన్న దూరం, A నుండి ఉన్న దూరానికి రెట్టింపు ఉండేలా ఏర్పాటు చేస్తే, ఆ టవర్ AB రేఖాఖండాన్ని 1 : 2 నిష్పత్తిలో విభజిస్తుంది. ఈ టవర్ యొక్క కచ్చితమైన నిరూపకాలను (coordinates) కనుగొనడానికి మనకు ఒక గణిత పద్ధతి అవసరం. ఒక రేఖాఖండాన్ని ఇచ్చిన నిష్పత్తిలో అంతర్గతంగా విభజించే బిందువు యొక్క నిరూపకాలను కనుగొనడం గురించే ఈ అంశం.

## విభజన సూత్రం (Section Formula)

ఒక రేఖపై ఉన్న A, B బిందువుల మధ్యలో P అనే బిందువు ఉన్నప్పుడు, అది AB రేఖాఖండాన్ని అంతర్గతంగా విభజిస్తుంది. A యొక్క నిరూపకాలు $(x_1, y_1)$, B యొక్క నిరూపకాలు $(x_2, y_2)$ అనుకుందాం. P అనేది A, B లను కలిపే రేఖాఖండాన్ని $m_1: m_2$ నిష్పత్తిలో అంతర్గతంగా విభజిస్తే, P యొక్క నిరూపకాలను విభజన సూత్రం ఇస్తుంది.

$A(x_{1}, y_{1})$, $B(x_{2}, y_{2})$ బిందువులను కలిపే రేఖాఖండాన్ని $m_{1}: m_{2}$ నిష్పత్తిలో అంతర్గతంగా విభజించే $P(x, y)$ బిందువు యొక్క నిరూపకాలు

$$
\left(\frac{m_{1} x_{2} + m_{2} x_{1}}{m_{1} + m_{2}}, \frac{m_{1} y_{2} + m_{2} y_{1}}{m_{1} + m_{2}}\right)
$$

దీనిని విభజన సూత్రం (section formula) అంటారు. P అనేది AB ని విభజించే నిష్పత్తి $k:1$ అయితే, P బిందువు యొక్క నిరూపకాలు

$$
\left(\frac{k x_{2} + x_{1}}{k + 1}, \frac{k y_{2} + y_{1}}{k + 1}\right)
$$

## మధ్య బిందువు

మధ్య బిందువు (midpoint) అనేది విభజన సూత్రం యొక్క ఒక ప్రత్యేక సందర్భం. ఒక రేఖాఖండం యొక్క మధ్య బిందువు ఆ రేఖాఖండాన్ని 1 : 1 నిష్పత్తిలో విభజిస్తుంది. కాబట్టి $A(x_{1}, y_{1})$, $B(x_{2}, y_{2})$ బిందువులను కలిపే రేఖాఖండం యొక్క మధ్య బిందువు P యొక్క నిరూపకాలు

$$
\left(\frac{1 \cdot x_{1} + 1 \cdot x_{2}}{1 + 1}, \frac{1 \cdot y_{1} + 1 \cdot y_{2}}{1 + 1}\right) = \left(\frac{x_{1} + x_{2}}{2}, \frac{y_{1} + y_{2}}{2}\right)
$$

## సాధించిన ఉదాహరణ

$(4, -3)$, $(8, 5)$ బిందువులను కలిపే రేఖాఖండాన్ని $3:1$ నిష్పత్తిలో అంతర్గతంగా విభజించే బిందువు యొక్క నిరూపకాలను కనుగొనండి.

కావలసిన బిందువు $\mathrm{P}(x, y)$ అనుకుందాం. విభజన సూత్రం ప్రకారం

$$
x = \frac{3 \times 8 + 1 \times 4}{3 + 1} = \frac{24 + 4}{4} = \frac{28}{4} = 7
$$

$$
y = \frac{3 \times 5 + 1 \times (-3)}{3 + 1} = \frac{15 - 3}{4} = \frac{12}{4} = 3
$$

కాబట్టి కావలసిన బిందువు యొక్క నిరూపకాలు $(7, 3)$.

## ముఖ్య అంశాలు

*   రెండు బిందువులు $(x_1, y_1)$, $(x_2, y_2)$ లను కలిపే రేఖాఖండాన్ని ఇచ్చిన నిష్పత్తి $m_1 : m_2$ లో విభజించే బిందువు యొక్క నిరూపకాలను విభజన సూత్రం ఇస్తుంది.
*   అంతర్గత విభజన (internal division) సూత్రం $\left(\frac{m_{1} x_{2} + m_{2} x_{1}}{m_{1} + m_{2}}, \frac{m_{1} y_{2} + m_{2} y_{1}}{m_{1} + m_{2}}\right)$.
*   మధ్య బిందువు అనేది విభజన సూత్రం యొక్క ఒక ప్రత్యేక సందర్భం; ఇక్కడ నిష్పత్తి $1:1$, నిరూపకాలు $\left(\frac{x_{1} + x_{2}}{2}, \frac{y_{1} + y_{2}}{2}\right)$.
*   నిష్పత్తి $k:1$ గా ఇస్తే, P బిందువు యొక్క నిరూపకాలు $\left(\frac{k x_{2} + x_{1}}{k + 1}, \frac{k y_{2} + y_{1}}{k + 1}\right)$ అవుతాయి.
*   బిందువు నుండి రెండు అంత్య బిందువులకు ఉన్న దూరాల నిష్పత్తి ఇచ్చిన నిష్పత్తికి సమానమో కాదో చూసి మీ సమాధానాన్ని సరిచూడవచ్చు.
