---
{
  "concept": "Pressure in Fluids",
  "slug": "fluid-pressure",
  "grade": 8,
  "language": "te",
  "hand_edited": "2026-10-13: line-by-line hand audit against the English tagged copy. Main fix: the generator used the one word 'dravam' for both 'fluid' and 'liquid', so 'a fluid is any substance that can flow; this includes both liquids and gases' read as 'a liquid ... includes both liquids and gases', and the title and a heading came out identical. Now fluid = pravaahi (with the English in brackets at first use and in the key point), liquid = dravam, gas = vaayuvu. Also: 'confined' rendered 'parimitamaina' (limited), now 'moosi unna'; 'hull' rendered 'paibhaagam' (top part), now 'bayati kavacham'; 'weight' rendered 'bhaaram' (burden), now 'baruvu'; 'sides' rendered 'anchulu' (edges), now 'pakkalu'; 'tight-fitting lid' rendered 'gatti' (hard), now 'bigutuga amare'; 'Water is a fluid we see every day' lost the word fluid. The English page is thin (about 430 words) and this translation inherits that.",
  "subject": "physics",
  "area": "Fluid Mechanics",
  "model": "sarvam-105b",
  "settings": {
    "temperature": 0.3,
    "max_tokens": 8000,
    "reasoning_effort": "none"
  },
  "usage": {
    "completion_tokens": 695,
    "prompt_tokens": 1099,
    "total_tokens": 1794,
    "completion_tokens_details": {
      "accepted_prediction_tokens": null,
      "audio_tokens": null,
      "reasoning_tokens": 0,
      "rejected_prediction_tokens": null
    },
    "prompt_tokens_details": null
  },
  "target_words": [
    350,
    675
  ],
  "generated_at": "2026-10-13T21:15:48",
  "source_grade": 9,
  "grade_delta": 1,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g9_science_chapter9_024",
      "chapter": "chapter9",
      "section": "9.5.1 PRESSURE IN FLUIDS"
    },
    {
      "ref": "S2",
      "passage_id": "g9_science_chapter1_024",
      "chapter": "chapter1",
      "section": "1.4.2 EFFECT OF CHANGE OF PRESSURE"
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
    "words": 329,
    "target_words": [
      350,
      675
    ],
    "untraceable_sections": 1,
    "ok": true,
    "tags_vs_english": "8/8",
    "localisation_problems": [],
    "not_harvestable": [
      "brackets: 6/6 declared terms are not bracketed with their English word (['pressure', 'fluid', 'liquid', 'gas'])"
    ]
  },
  "terms": [
    "pressure",
    "fluid",
    "liquid",
    "gas",
    "pascal's law",
    "confined mass"
  ]
}
---

# ప్రవాహులలో పీడనం

బరువైన ఒక ఘన వస్తువు తన బరువుతో టేబుల్ మీద కిందికి నెడుతుందని మీకు ఇప్పటికే తెలుసు. ప్రవాహులు (fluids) ఘనపదార్థాల కంటే భిన్నంగా ఉంటాయి, కానీ వాటికి కూడా బరువు ఉంటుంది. ఒక ప్రవాహిని ఒక పాత్రలో ఉంచినప్పుడు, అది ఆ పాత్ర అడుగు భాగాన్ని మరియు పక్కలను నెడుతుంది. ఈ నెట్టడం వల్ల ఉపరితలంపై ఉన్న ప్రతి యూనిట్ వైశాల్యంపై ప్రయోగించబడే బలాన్ని పీడనం అంటారు. నీటి పంపు ఎలా పనిచేస్తుంది లేదా లోతైన సముద్రంలో వెళ్లే జలాంతర్గామికి చాలా బలమైన బయటి కవచం (hull) ఎందుకు అవసరం అవుతుంది లాంటి రోజువారీ విషయాలను అర్థం చేసుకోవడానికి ప్రవాహులు ఎలా నెడతాయో తెలుసుకోవడం చాలా ముఖ్యం.

## ప్రవాహులు అంటే ఏమిటి?

సులభంగా ప్రవహించగల ఏ పదార్థాన్నైనా ప్రవాహి (fluid) అంటారు. ఇందులో ద్రవాలు (liquids) మరియు వాయువులు (gases) రెండూ ఉంటాయి. ప్రవాహులకు బరువు ఉంటుంది కాబట్టి, అవి ఉన్న పాత్ర అడుగు భాగంపై మరియు గోడలపై పీడనాన్ని ప్రయోగిస్తాయి. ఒక ఘన పదార్థం తన బరువుతో ఉపరితలంపై పీడనాన్ని ప్రయోగించినట్లే ఇది కూడా ఉంటుంది.

## ద్రవాలలో పీడనం

నీరు మనం ప్రతిరోజూ చూసే ఒక ప్రవాహి. మీరు ఒక గ్లాసులో నీరు పోసినప్పుడు, నీరు ఆ గ్లాసును నెడుతుంది. ఒక ద్రవం ప్రయోగించే పీడనం అది ఎంత లోతులో ఉందనే దానిపై ఆధారపడి ఉంటుంది. మీరు ద్రవంలో ఎంత లోతుకు వెళితే, పీడనం అంత పెరుగుతుంది. ఎందుకంటే మీ పైన ఎక్కువ ద్రవం ఉంటుంది, ఇది మొత్తం బరువును మరియు నెట్టే బలాన్ని పెంచుతుంది.

## పాస్కల్ నియమం

పాస్కల్ నియమం (Pascal's law) మూసి ఉన్న ప్రవాహిలో పీడనం ఎలా పనిచేస్తుందనే దాని గురించి మనకు ఒక ముఖ్యమైన విషయాన్ని చెబుతుంది. ఈ నియమం ప్రకారం, మూసి ఉన్న ప్రవాహిలో ప్రయోగించబడిన పీడనం అన్ని దిశలలోనూ తగ్గకుండా ప్రసారం చేయబడుతుంది. అంటే మీరు ఒక చోట ప్రవాహిని నెట్టితే, ఆ పీడనం అన్ని దిశలలో సమానంగా వ్యాపిస్తుంది. అది ప్రవాహి గుండా వెళుతున్నప్పుడు బలహీనపడదు.

## సాధించిన ఉదాహరణ

ఒక సాధారణ పరిస్థితిలో ఈ నియమం ఎలా పనిచేస్తుందో చూద్దాం. పూర్తిగా నీటితో నిండిన, మీరు కిందికి నొక్కగలిగే, బిగుతుగా అమరే మూత ఉన్న ఒక మూసిన పాత్రను ఊహించుకోండి. మీరు మూతను నొక్కినప్పుడు, మీరు నీటిపై పీడనాన్ని ప్రయోగిస్తారు. పాస్కల్ నియమం ప్రకారం, ఈ పీడనం అన్ని దిశలలోనూ తగ్గకుండా (చిన్నగా మారకుండా) ప్రసారం చేయబడుతుంది. కాబట్టి అదే పీడనం ఎలాంటి బలాన్ని కోల్పోకుండా పాత్ర అడుగు భాగానికి మరియు పక్కలకు చేరుకుంటుంది.

## ముఖ్య అంశాలు

*   ద్రవాలు మరియు వాయువులు ప్రవహించగలవు కాబట్టి వాటన్నింటినీ ప్రవాహులు (fluids) అంటారు.
*   ప్రవాహులకు బరువు ఉంటుంది, కాబట్టి అవి ఉన్న పాత్ర అడుగు భాగంపై మరియు గోడలపై పీడనాన్ని ప్రయోగిస్తాయి.
*   మూసి ఉన్న ప్రవాహిలో ప్రయోగించబడిన పీడనం అన్ని దిశలలోనూ తగ్గకుండా ప్రసారం చేయబడుతుంది.
*   ద్రవం లోతు పెరిగే కొద్దీ ద్రవం ప్రయోగించే పీడనం పెరుగుతుంది.
*   పీడనం అనేది ఉపరితలంపై ఉన్న ప్రతి యూనిట్ వైశాల్యంపై పనిచేసే బలం.