---
{
  "concept": "Collision Theory",
  "slug": "collision-theory",
  "grade": 12,
  "language": "en",
  "subject": "chemistry",
  "area": "Chemical Kinetics",
  "model": "sarvam-105b",
  "settings": {
    "temperature": 0.3,
    "max_tokens": 8000,
    "reasoning_effort": "none"
  },
  "usage": {
    "completion_tokens": 1740,
    "prompt_tokens": 5927,
    "total_tokens": 7667,
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
  "generated_at": "2026-10-08T08:16:56",
  "source_grade": 12,
  "grade_delta": 0,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g12_chemistry_part1_chapter3_039",
      "chapter": "chapter3",
      "section": "3.5 Collision Theory of Chemical Reactions"
    },
    {
      "ref": "S2",
      "passage_id": "g12_chemistry_part1_chapter4_010",
      "chapter": "chapter4",
      "section": "4.3.1 Physical Properties"
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
    "words": 1249,
    "target_words": [
      1050,
      1450
    ],
    "untraceable_sections": 0,
    "ok": true,
    "structural_problems": [],
    "grounding": {
      "cited_sentences": 21,
      "checked": 21,
      "not_judgeable_mostly_maths": 0,
      "cites_a_source_never_given": 0,
      "unsupported": [
        {
          "claim": "However, collision theory, developed by Max Trautz and William Lewis in 1916-1918, provides a deeper understanding of the energetic and mechanistic aspects of these reactions .",
          "cites": [
            "S1"
          ],
          "support_probability": 0.09
        },
        {
          "claim": "It is based on the kinetic theory of gases, which assumes that reactant molecules behave as hard spheres moving randomly in space .",
          "cites": [
            "S1"
          ],
          "support_probability": 0.057
        },
        {
          "claim": "For instance, in the formation of methanol from bromoethane, the molecules must collide in a way that allows the hydroxyl group to approach the carbon atom from the correct angle .",
          "cites": [
            "S1"
          ],
          "support_probability": 0.062
        }
      ],
      "unsupported_fraction": 0.143,
      "threshold": 0.5,
      "max_unsupported_fraction": 0.34
    },
    "verification": {
      "verdict": "spiralled",
      "checks": 1,
      "tokens": 9903
    }
  },
  "terms": [
    "collision frequency",
    "activation energy",
    "threshold energy",
    "effective collisions",
    "steric factor",
    "arrhenius equation"
  ]
}
---

# Collision Theory

Collision theory is a fundamental concept in chemistry that explains how chemical reactions actually occur at the molecular level. You may already know that the rate of a chemical reaction depends on factors like temperature and concentration. However, collision theory, developed by Max Trautz and William Lewis in 1916-1918, provides a deeper understanding of the energetic and mechanistic aspects of these reactions. It is based on the kinetic theory of gases, which assumes that reactant molecules behave as hard spheres moving randomly in space. When these molecules collide with each other, they might react to form products, but only if certain conditions are met. Understanding these conditions helps us predict how fast a reaction will proceed and why some reactions happen instantly while others take a very long time.

## The Collision Frequency

According to collision theory, a chemical reaction occurs only when molecules collide with each other. The number of collisions per second per unit volume of the reaction mixture is known as the collision frequency, denoted by the symbol $Z$. For a bimolecular elementary reaction, such as $A + B \rightarrow$ Products, the rate of reaction can be expressed as $\text{Rate} = Z_{AB} e^{-E_a / RT}$. Here, $Z_{AB}$ represents the collision frequency of the reactants A and B, and the exponential term $e^{-E_a / RT}$ represents the fraction of molecules that possess enough energy to overcome the activation barrier. 

The collision frequency $Z_{AB}$ is directly related to the pre-exponential factor $A$ in the Arrhenius equation. This means that a higher collision frequency generally leads to a faster reaction rate, assuming all other factors remain constant. However, not every collision results in a chemical reaction. This brings us to the critical concept of activation energy.

## Activation Energy

Activation energy, often denoted as $E_a$, is the minimum amount of energy required for a reaction to occur. Even when molecules collide, they will not react unless they possess sufficient kinetic energy, which is referred to as the threshold energy. The threshold energy is defined as the activation energy plus the energy possessed by the reacting species. 

The exponential term $e^{-E_a / RT}$ in the rate equation represents the fraction of molecules that have energies equal to or greater than the activation energy $E_a$. This fraction is highly sensitive to temperature. As the temperature $T$ increases, the value of $e^{-E_a / RT}$ increases, meaning a larger fraction of molecules can overcome the activation barrier. This explains why reactions generally proceed faster at higher temperatures. It is important to note that while the Arrhenius equation is widely applicable, collision theory provides a more detailed mechanistic insight into why the rate constant has the specific value it does.

## Effective Collisions

For a collision to be successful, it must be an effective collision. An effective collision occurs when molecules collide with sufficient kinetic energy (the threshold energy) and proper orientation. Proper orientation means that the molecules must be aligned in a specific way to facilitate the breaking of bonds between the reacting species and the formation of new bonds to create products. 

If the molecules collide with insufficient energy or in the wrong orientation, they will simply bounce back without any chemical change. For example, the formation of methanol from bromoethane depends critically on the orientation of the reactant molecules. Proper orientation leads to bond formation, whereas improper orientation results in the molecules bouncing off each other. To account for this, collision theory introduces another factor called the probability or steric factor, denoted by $P$. This factor takes into account the fact that molecules must be properly oriented for a reaction to occur.

## The Role of the Steric Factor

The steric factor $P$ is a dimensionless number between 0 and 1 that represents the fraction of collisions that have the correct orientation for a reaction to occur. The overall rate of reaction is then given by the equation $\text{Rate} = P Z_{AB} e^{-E_a / RT}$. This equation shows that the rate of a chemical reaction is determined by three main factors: the collision frequency $Z_{AB}$, the activation energy $E_a$, and the steric factor $P$. 

The steric factor highlights that chemical reactions are not just about energy; they are also about geometry. Molecules have specific shapes and functional groups, and these must align correctly for a reaction to proceed. For instance, in the formation of methanol from bromoethane, the molecules must collide in a way that allows the hydroxyl group to approach the carbon atom from the correct angle. If the orientation is incorrect, the molecules will simply bounce off each other, and no products will be formed.

## Limitations of Collision Theory

While collision theory provides valuable insights, it does have certain limitations. It considers atoms and molecules to be hard spheres and ignores their structural aspects. This simplification works reasonably well for reactions involving atomic species or simple molecules, but for complex molecules, significant deviations are observed. 

For complex molecules, the assumption that all collisions are equally likely to be effective is not accurate. The internal structure of the molecules, including bond angles and electron distributions, plays a crucial role in determining the steric factor. Therefore, collision theory is most applicable to simple reactions and provides a foundational understanding of chemical kinetics. You will study more advanced theories and details about this theory in your higher classes.

## Worked Example

Consider a bimolecular elementary reaction between molecules A and B. The collision frequency $Z_{AB}$ is $10^9 \, \text{M}^{-1} \text{s}^{-1}$. The activation energy $E_a$ is $50 \, \text{kJ mol}^{-1}$, and the temperature $T$ is $300 \, \text{K}$. The steric factor $P$ is $0.1$. 

First, we calculate the fraction of molecules with sufficient energy using the exponential term. The gas constant $R$ is $8.314 \, \text{J mol}^{-1} \text{K}^{-1}$. The exponent is $-E_a / RT = -50000 / (8.314 \times 300) \approx -20.05$. The exponential term $e^{-20.05}$ is approximately $2.0 \times 10^{-9}$.

Next, we calculate the rate of reaction using the formula $\text{Rate} = P Z_{AB} e^{-E_a / RT}$. Substituting the values, we get $\text{Rate} = 0.1 \times 10^9 \times 2.0 \times 10^{-9} = 0.2 \, \text{M s}^{-1}$. 

This example illustrates how the rate of reaction is influenced by the collision frequency, activation energy, and steric factor. A higher activation energy or a lower steric factor would result in a slower reaction rate, while a higher temperature would increase the fraction of molecules with sufficient energy, thereby increasing the rate.

## Key points

- Collision theory explains that chemical reactions occur when reactant molecules collide with each other.
- The collision frequency $Z_{AB}$ is the number of collisions per second per unit volume of the reaction mixture.
- Activation energy $E_a$ is the minimum energy required for a reaction to occur, and the fraction of molecules with sufficient energy is given by $e^{-E_a / RT}$.
- Effective collisions require both sufficient kinetic energy (threshold energy) and proper orientation of the molecules.
- The steric factor $P$ accounts for the fraction of collisions that have the correct orientation for a reaction to occur.
- The rate of reaction is given by $\text{Rate} = P Z_{AB} e^{-E_a / RT}$.
- Collision theory considers molecules as hard spheres and ignores their structural aspects, which limits its applicability to complex molecules.