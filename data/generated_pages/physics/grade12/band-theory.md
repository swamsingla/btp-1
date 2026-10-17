---
{
  "concept": "Band Theory of Solids",
  "slug": "band-theory",
  "grade": 12,
  "language": "en",
  "subject": "physics",
  "area": "Solid State",
  "model": "sarvam-105b",
  "settings": {
    "temperature": 0.3,
    "max_tokens": 8000,
    "reasoning_effort": "none"
  },
  "usage": {
    "completion_tokens": 1347,
    "prompt_tokens": 5662,
    "total_tokens": 7009,
    "completion_tokens_details": {
      "accepted_prediction_tokens": null,
      "audio_tokens": null,
      "reasoning_tokens": 0,
      "rejected_prediction_tokens": null
    },
    "prompt_tokens_details": null
  },
  "target_words": [
    1050,
    1450
  ],
  "generated_at": "2026-10-08T08:40:42",
  "source_grade": 12,
  "grade_delta": 0,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g12_physics_part2_chapter6_007",
      "chapter": "chapter6",
      "section": "14.2 CLASSIFICATION OF METALS, CONDUCTORS AND SEMICONDUCTORS"
    },
    {
      "ref": "S2",
      "passage_id": "g12_physics_part2_chapter6_008",
      "chapter": "chapter6",
      "section": "14.3 INTRINSIC SEMICONDUCTOR"
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
    "words": 1064,
    "target_words": [
      1050,
      1450
    ],
    "untraceable_sections": 0,
    "ok": true,
    "structural_problems": [],
    "grounding": {
      "cited_sentences": 17,
      "checked": 17,
      "not_judgeable_mostly_maths": 0,
      "cites_a_source_never_given": 0,
      "unsupported": [
        {
          "claim": "There are no electrons in the conduction band, and therefore no electrical conduction is possible .",
          "cites": [
            "S1"
          ],
          "support_probability": 0.12
        }
      ],
      "unsupported_fraction": 0.059,
      "threshold": 0.5,
      "max_unsupported_fraction": 0.34
    },
    "verification": {
      "verdict": "spiralled",
      "checks": 1,
      "tokens": 9501
    }
  },
  "terms": [
    "energy bands",
    "valence band",
    "conduction band",
    "band gap",
    "intrinsic semiconductor",
    "covalent bond",
    "hole",
    "electron-hole pair"
  ]
}
---

# Band Theory of Solids

The behaviour of electricity in a solid depends on how its electrons are arranged. In an isolated atom, electrons occupy specific energy levels. When atoms come together to form a crystal, their outer electron orbits overlap and interact. This interaction changes the nature of electron motion completely. The result is the formation of energy bands. Understanding these bands explains why some solids conduct electricity, while others do not.

## Formation of Energy Bands

In an isolated atom, the energy of an electron is determined by its orbit. When atoms come together to form a solid, the outer orbits of electrons from neighbouring atoms come very close or overlap. This makes the nature of electron motion in a solid very different from that in an isolated atom. Inside the crystal, each electron has a unique position and no two electrons see exactly the same pattern of surrounding charges. Because of this, each electron will have a different energy level. These different energy levels with continuous energy variation form what are called energy bands. 

The energy band which includes the energy levels of the valence electrons is called the valence band. The energy band above the valence band is called the conduction band. With no external energy, all the valence electrons will reside in the valence band. The conduction band is normally empty.

## Classification of Solids by Band Structure

The way the conduction band and valence band are arranged determines if a material is a conductor, semiconductor, or insulator.

### Conductors

A metal can exist when the conduction band is partially filled or when the conduction and valence bands overlap. When there is overlap, electrons from the valence band can easily move into the conduction band. This situation makes a large number of electrons available for electrical conduction. When the valence band is partially empty, electrons from its lower level can move to higher level making conduction possible. Therefore, the resistance of such materials is low or the conductivity is high.

### Insulators

In this case, a large band gap $E_{g}$ exists. There are no electrons in the conduction band, and therefore no electrical conduction is possible. The energy gap is so large that electrons cannot be excited from the valence band to the conduction band by thermal excitation.

### Semiconductors

Here a finite but small band gap exists. Because of the small band gap, at room temperature some electrons from the valence band can acquire enough energy to cross the energy gap and enter the conduction band. These electrons can move in the conduction band. Hence, the resistance of semiconductors is not as high as that of the insulators.

## Intrinsic Semiconductors

We shall take the most common case of Ge and Si. These structures are called the diamond-like structures. Each atom is surrounded by four nearest neighbours. Silicon and Germanium have four valence electrons. In its crystalline structure, every Si or Ge atom tends to share one of its four valence electrons with each of its four nearest neighbour atoms, and also to take share of one electron from each such neighbour. These shared electron pairs are referred to as forming a covalent bond or simply a valence bond. 

At absolute zero temperature, an intrinsic semiconductor behaves like an insulator. As the temperature increases, more thermal energy becomes available to these electrons and some of these electrons may break-away (becoming free electrons contributing to conduction). The thermal energy effectively ionises only a few atoms in the crystalline lattice and creates a vacancy in the bond. The neighbourhood, from which the free electron (with charge -q) has come out leaves a vacancy with an effective charge (+q). This vacancy with the effective positive electronic charge is called a hole. The hole behaves as an apparent free particle with effective positive charge.

In intrinsic semiconductors, the number of free electrons is equal to the number of holes.
$$ n _ {e} = n _ {h} = n _ {i} \tag{14.1} $$
where $n_i$ is called intrinsic carrier concentration. The total current is the sum of the electron current and the hole current:
$$ I = I _ {e} + I _ {h} \tag{14.2} $$
At equilibrium, the rate of generation is equal to the rate of recombination of charge carriers.

## Worked example

Consider a piece of silicon at room temperature. Each silicon atom has four valence electrons. In a crystal containing $10^{28}$ atoms, there are $4 \times 10^{28}$ valence electrons in total. The maximum possible number of electrons in the outer orbit is 8. So, for the $4N$ valence electrons there are $8N$ available energy states. At the distance between the atoms in the crystal lattices of Si, the energy band of these $8N$ states is split apart into two which are separated by an energy gap $E_{g}$. The lower band is the valence band. The other band consisting of $4N$ energy states is the conduction band.

Since silicon is an intrinsic semiconductor with a small band gap, at room temperature some electrons from the valence band can acquire enough energy to cross the energy gap and enter the conduction band. This creates free electrons and an equal number of holes in the valence band. These electrons and holes can move independently and contribute to the total electrical current.

## Key points

- Energy bands form when atoms come together to form a solid and their outer electron orbits overlap.
- The lower band is called the valence band and the upper band is called the conduction band.
- Metals have overlapping or partially filled conduction bands, giving them high conductivity.
- Insulators have a large band gap, preventing electrons from moving to the conduction band.
- Semiconductors have a small band gap, allowing some electrons to move to the conduction band at room temperature.
- In intrinsic semiconductors, the number of free electrons equals the number of holes.
- The total current in a semiconductor is the sum of electron current and hole current.
- At equilibrium, the rate of generation of charge carriers equals the rate of recombination.