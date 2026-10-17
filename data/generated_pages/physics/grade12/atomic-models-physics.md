---
{
  "concept": "Atomic Models (Physics)",
  "slug": "atomic-models-physics",
  "grade": 12,
  "language": "en",
  "subject": "physics",
  "area": "Modern Physics",
  "model": "sarvam-105b",
  "settings": {
    "temperature": 0.3,
    "max_tokens": 8000,
    "reasoning_effort": "none"
  },
  "usage": {
    "completion_tokens": 1976,
    "prompt_tokens": 5970,
    "total_tokens": 7946,
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
  "generated_at": "2026-10-08T08:19:16",
  "source_grade": 12,
  "grade_delta": 0,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g12_physics_part2_chapter5_007",
      "chapter": "chapter5",
      "section": "13.3 SIZE OF THE NUCLEUS"
    },
    {
      "ref": "S2",
      "passage_id": "g12_physics_part2_chapter4_004",
      "chapter": "chapter4",
      "section": "12.2 ALPHA-PARTICLE SCATTERING AND"
    },
    {
      "ref": "S3",
      "passage_id": "g12_physics_part2_chapter4_025",
      "chapter": "chapter4",
      "section": "12.6 DE BROGLIE'S EXPLANATION OF BOHR'S SECOND POSTULATE OF QUANTISATION"
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
    "explanatory_paragraphs_without_a_citation": 3,
    "words": 1247,
    "target_words": [
      1050,
      1450
    ],
    "untraceable_sections": 1,
    "ok": true,
    "structural_problems": [],
    "grounding": {
      "cited_sentences": 11,
      "checked": 9,
      "not_judgeable_mostly_maths": 2,
      "cites_a_source_never_given": 0,
      "unsupported": [],
      "unsupported_fraction": 0.0,
      "threshold": 0.5,
      "max_unsupported_fraction": 0.34
    },
    "verification": {
      "verdict": "spiralled",
      "checks": 1,
      "tokens": 10146
    }
  },
  "terms": [
    "alpha-particle",
    "atomic nucleus",
    "coulomb repulsive force",
    "de broglie wavelength",
    "electron",
    "geiger-marsden experiment",
    "gold foil",
    "hydrogenic atoms",
    "mass number",
    "nuclear density",
    "nuclear model",
    "plum pudding model",
    "quantisation",
    "radius of nucleus",
    "rutherford's nuclear model",
    "thomson's model"
  ]
}
---

# Atomic Models (Physics)

Understanding the structure of the atom is one of the most important milestones in modern physics. For a long time, scientists believed atoms were indivisible, but experiments in the early twentieth century revealed that atoms are actually complex systems made of smaller particles. This chapter explores three major models of the atom: Thomson's plum pudding model, Rutherford's nuclear model, and Bohr's quantized model. These models help us understand how electrons behave and how atoms interact with radiation.

## Thomson's Model
J.J. Thomson was the first to propose a detailed structure for the atom. In his model, the atom was visualized as a uniform, positively charged sphere. Embedded within this sphere were negatively charged electrons, much like plums in a pudding. This model was a significant step forward because it introduced the idea that atoms were divisible and contained both positive and negative charges. However, this model could not explain the results of later experiments involving the scattering of alpha particles.

## Rutherford's Nuclear Model
In 1911, Ernst Rutherford proposed a revolutionary new model based on the famous Geiger-Marsden experiment. In this experiment, a beam of 5.5 MeV alpha-particles was directed at a thin gold foil. Rutherford argued that to deflect an alpha-particle backwards, it must experience a large repulsive force. This force could only be provided if the greater part of the mass of the atom and its positive charge were concentrated tightly at its centre. This led to the concept of the atomic nucleus. In Rutherford's nuclear model of the atom, the entire positive charge and most of the mass of the atom are concentrated in the nucleus with the electrons some distance away. The electrons would be moving in orbits about the nucleus just as the planets do around the sun.

The scattering of alpha-particles by a gold sheet could be understood by Rutherford by assuming that the Coulomb repulsive force was solely responsible for scattering. Since the positive charge is confined to the nucleus, the actual size of the nucleus has to be less than $4.0\times 10^{-14}\mathrm{m}$. The scattering data can be analysed by employing Rutherford's nuclear model of the atom. As the gold foil is very thin, it can be assumed that alpha-particles will suffer not more than one scattering during their passage through it. Therefore, computation of the trajectory of an alpha-particle scattered by a single nucleus is enough. The magnitude of this force is given by

$$
F = \frac {1}{4 \pi \varepsilon_ {0}} \frac {(2 e) (Z e)}{r ^ {2}}\tag{12.1}
$$

where $r$ is the distance between the alpha-particle and the nucleus.

## Bohr's Model
Niels Bohr introduced a model that addressed some of the shortcomings of Rutherford's model. Bohr proposed that electrons move in specific, quantized orbits around the nucleus. The angular momentum of the electron orbiting around the nucleus is quantised (that is, $L_{n} = nh/2\pi$ ; $n = 1, 2, 3 \dots$). Why should the angular momentum have only those values that are integral multiples of $h/2\pi$? The French physicist Louis de Broglie explained this puzzle in 1923. De Broglie argued that the electron in its circular orbit, as proposed by Bohr, must be seen as a particle wave. In analogy to waves travelling on a string, particle waves too can lead to standing waves under resonant conditions. For an electron moving in $n^{th}$ circular orbit of radius $r_{n}$, the total distance is the circumference of the orbit, $2\pi r_{n}$. Thus

$$
2 \pi r _ {n} = n \lambda , \quad n = 1, 2, 3 \dots\tag{12.12}
$$

From Chapter 11, we have $\lambda=h/p$, where $p$ is the magnitude of the electron's momentum. If the speed of the electron is much less than the speed of light, the momentum is $mv_{n}$. Thus, $\lambda=h/mv_{n}$. From Eq. (12.12), we have

$$
2 \pi r _ {n} = n h / m v _ {n} \quad \text{or} \quad m v _ {n} r _ {n} = n h / 2 \pi
$$

This is the quantum condition proposed by Bohr for the angular momentum of the electron.

Bohr's model, involving classical trajectory picture (planet-like electron orbiting the nucleus), correctly predicts the gross features of the hydrogenic atoms, in particular, the frequencies of the radiation emitted or selectively absorbed. This model however has many limitations. The Bohr model is applicable to hydrogenic atoms. It cannot be extended even to mere two electron atoms such as helium. The analysis of atoms with more than one electron was attempted on the lines of Bohr's model for hydrogenic atoms but did not meet with any success. Difficulty lies in the fact that each electron interacts not only with the positively charged nucleus but also with all other electrons.

## Size and Density of the Nucleus
By performing scattering experiments in which fast electrons, instead of alpha-particles, are projectiles that bombard targets made up of various elements, the sizes of nuclei of various elements have been accurately measured. It has been found that a nucleus of mass number $A$ has a radius

$$
R = R _ {0} A ^ {1 / 3}\tag{13.5}
$$

where $R_{0}=1.2\times10^{-15}$ m (=1.2 fm; $1\,fm=10^{-15}\,m$). This means the volume of the nucleus, which is proportional to $R^{3}$, is proportional to $A$. Thus the density of nucleus is a constant, independent of $A$, for all nuclei. Different nuclei are like a drop of liquid of constant density. The density of nuclear matter is approximately $2.3\times10^{17}\,kg\,m^{-3}$. This density is very large compared to ordinary matter, say water, which is $10^{3}\,kg\,m^{-3}$. This is understandable, as we have already seen that most of the atom is empty. Ordinary matter consisting of atoms has a large amount of empty space.

## Worked example
The radius of a nucleus can be calculated using the formula $R = R_{0} A^{1/3}$, where $R_0 = 1.2 \times 10^{-15}$ m and $A$ is the mass number. Let us consider a nucleus of iron, which has a mass number $A = 56$. The radius of the iron nucleus is $R = 1.2 \times 10^{-15} \times 56^{1/3} = 1.2 \times 10^{-15} \times 3.83 \approx 4.6 \times 10^{-15}$ m.

Now, let us calculate the density of the iron nucleus. The mass of the iron nucleus is $m = 55.85 \times 9.27 \times 10^{-26}$ kg $\approx 5.18 \times 10^{-25}$ kg. The volume of the nucleus is $V = \frac{4}{3} \pi R^3 = \frac{4}{3} \pi (4.6 \times 10^{-15})^3 \approx 3.99 \times 10^{-43}$ m³. The density of the nucleus is $\rho = \frac{m}{V} = \frac{5.18 \times 10^{-25}}{3.99 \times 10^{-43}} \approx 1.3 \times 10^{18}$ kg/m³. This is comparable to the density of nuclear matter, which is approximately $2.3 \times 10^{17}\,kg\,m^{-3}$.

## Key points
*   Thomson's model proposed a uniform, positively charged sphere with embedded electrons.
*   Rutherford's nuclear model, based on the Geiger-Marsden experiment, established that the positive charge and most of the mass are concentrated in a small nucleus.
*   Bohr's model introduced quantized electron orbits to explain the emission spectrum of hydrogen.
*   De Broglie's hypothesis explained the quantization of angular momentum as a result of standing waves.
*   The radius of a nucleus is given by $R = R_0 A^{1/3}$, and its density is approximately constant at $2.3 \times 10^{17}\,kg\,m^{-3}$.