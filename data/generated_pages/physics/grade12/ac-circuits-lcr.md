---
{
  "concept": "LCR Circuits and Resonance",
  "slug": "ac-circuits-lcr",
  "grade": 12,
  "language": "en",
  "subject": "physics",
  "area": "Electricity and Magnetism",
  "model": "sarvam-105b",
  "settings": {
    "temperature": 0.3,
    "max_tokens": 8000,
    "reasoning_effort": "none"
  },
  "usage": {
    "completion_tokens": 1685,
    "prompt_tokens": 6275,
    "total_tokens": 7960,
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
  "generated_at": "2026-10-08T08:09:28",
  "source_grade": 12,
  "grade_delta": 0,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g12_physics_part1_chapter7_021",
      "chapter": "chapter7",
      "section": "7.6.1 Phasor-diagram solution"
    },
    {
      "ref": "S2",
      "passage_id": "g12_physics_part1_chapter7_024",
      "chapter": "chapter7",
      "section": "7.6.2 Resonance"
    },
    {
      "ref": "S3",
      "passage_id": "g12_physics_part1_chapter7_017",
      "chapter": "chapter7",
      "section": "7.6 AC VOLTAGE APPLIED TO A SERIES LCR CIRCUIT"
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
    "explanatory_paragraphs_without_a_citation": 3,
    "words": 950,
    "target_words": [
      1050,
      1450
    ],
    "untraceable_sections": 0,
    "ok": true,
    "structural_problems": [],
    "grounding": {
      "cited_sentences": 7,
      "checked": 4,
      "not_judgeable_mostly_maths": 3,
      "cites_a_source_never_given": 0,
      "unsupported": [],
      "unsupported_fraction": 0.0,
      "threshold": 0.5,
      "max_unsupported_fraction": 0.34
    },
    "verification": {
      "verdict": "spiralled",
      "checks": 1,
      "tokens": 9907
    }
  },
  "terms": [
    "impedance",
    "phase angle",
    "power factor",
    "resonant frequency",
    "reactance",
    "phasor",
    "lcr circuit",
    "series circuit",
    "alternating current"
  ]
}
---

# LCR Circuits and Resonance

LCR circuits are the backbone of modern electronics. From the tuning knobs on your radio to the filters in your smartphone, these circuits control how alternating current (AC) flows. Understanding how resistors, inductors, and capacitors interact in an AC circuit is essential for any physicist. This page explains the concepts of impedance and phase in series LCR circuits, and how these circuits behave at resonance.

## Impedance in a Series LCR Circuit

In a series LCR circuit, the resistor, inductor, and capacitor are connected end-to-end. Because they are in series, the AC current in each element is the same at any time, having the same amplitude and phase. Let the current be $i = i_{m} \sin (\omega t + \phi)$, where $\phi$ is the phase difference between the voltage across the source and the current in the circuit.

The voltage across the resistor ($V_R$), inductor ($V_L$), and capacitor ($V_C$) do not all share the same phase as the current. The voltage across the resistor is parallel to the current phasor $I$. The voltage across the capacitor is $\pi/2$ behind the current, and the voltage across the inductor is $\pi/2$ ahead of the current. The amplitudes of these voltages are given by $v_{Rm} = i_{m} R$, $v_{Cm} = i_{m} X_{C}$, and $v_{Lm} = i_{m} X_{L}$.

The total voltage equation for the circuit is $v_{L} + v_{R} + v_{C} = v$. Using phasor diagrams, this translates to the vector sum $\mathbf{V}_{\mathbf{L}} + \mathbf{V}_{\mathbf{R}} + \mathbf{V}_{\mathbf{C}} = \mathbf{V}$. Since $V_L$ and $V_C$ are always along the same line but in opposite directions, they can be combined into a single phasor. The Pythagorean theorem gives the relationship $v_{m}^{2} = v_{R m}^{2} + (v_{C m} - v_{L m})^{2}$.

Substituting the values, we get $i_{m}^{2} = \frac{v_{m}^{2}}{R^{2} + (X_{C} - X_{L})^{2}}$. By analogy to resistance in a DC circuit, we introduce the impedance $Z$ in an AC circuit. The impedance is $Z = \sqrt{R^{2} + (X_{C} - X_{L})^{2}}$.

## Phase Angle and Power Factor

The phase angle $\phi$ is the angle between the resistor voltage $V_R$ and the total source voltage $V$. From the impedance diagram, we find that $\tan \phi = \frac{v_{Cm} - v_{Lm}}{v_{Rm}}$. Using the definitions of $X_C$ and $X_L$, we have $\tan \phi = \frac{X_C - X_L}{R}$.

The sign of $\phi$ tells us whether the circuit is predominantly capacitive or inductive. If $X_{C} > X_{L}$, $\phi$ is positive and the circuit is predominantly capacitive. Consequently, the current in the circuit leads the source voltage. If $X_{C} < X_{L}$, $\phi$ is negative and the circuit is predominantly inductive. Consequently, the current in the circuit lags the source voltage.

The power factor of the circuit is the cosine of the phase angle, $\cos \phi$. It represents the fraction of the total power that is actually dissipated by the resistor. A high power factor means the circuit is using its energy efficiently.

## Resonance Frequency

Resonance is a fascinating phenomenon that occurs in LCR circuits. If the driving frequency $\omega$ is varied, then at a particular frequency $\omega_{0}$, $X_{c} = X_{L}$. At this point, the impedance is minimum, $Z = \sqrt{R^{2} + 0^{2}} = R$. This frequency is called the resonant frequency.

Setting $X_{c} = X_{L}$ gives $\frac{1}{\omega_{0} C} = \omega_{0} L$. Solving for $\omega_{0}$ yields $\omega_{0} = \frac{1}{\sqrt{L C}}$.

At the resonant frequency, the current amplitude is maximum, $i_{m} = v_{m}/R$. This means the total source voltage appears across the resistor. It is important to note that resonance is exhibited by a circuit only if both L and C are present. Only then do the voltages across L and C cancel each other (both being out of phase), and the current amplitude is $v_{m}/R$.

## Worked Example

Let us apply these rules to a practical scenario. Suppose we have a resistor of 200 Ω and a capacitor of 15.0 μF connected in series to a 220 V, 50 Hz AC source.

First, we calculate the impedance of the circuit. The capacitive reactance is $X_{C} = \frac{1}{2 \pi \nu C} = \frac{1}{2 \times 3.14 \times 50 \times 15.0 \times 10^{-6}} \approx 212.3 \, \Omega$. The impedance is $Z = \sqrt{R^{2} + X_{C}^{2}} = \sqrt{200^{2} + 212.3^{2}} \approx 291.7 \, \Omega$.

The current in the circuit is $I = \frac{V}{Z} = \frac{220}{291.7} \approx 0.755 \, \text{A}$.

Next, we calculate the voltage across the resistor and the capacitor. $V_{R} = I R = 0.755 \times 200 = 151 \, \text{V}$. $V_{C} = I X_{C} = 0.755 \times 212.3 \approx 160.3 \, \text{V}$.

The algebraic sum of these voltages is 311.3 V, which is more than the source voltage of 220 V. How do we resolve this paradox? The two voltages are not in the same phase. They are out of phase by ninety degrees. Therefore, the total voltage must be obtained using the Pythagorean theorem: $V_{R+C} = \sqrt{V_{R}^{2} + V_{C}^{2}} = \sqrt{151^{2} + 160.3^{2}} \approx 220 \, \text{V}$.

## Key points

*   Impedance ($Z$) is the total opposition to current flow in an AC circuit, given by $Z = \sqrt{R^{2} + (X_{C} - X_{L})^{2}}$.
*   The phase angle $\phi$ is given by $\tan \phi = \frac{X_{C} - X_{L}}{R}$, determining whether the current leads or lags the voltage.
*   Resonance occurs at $\omega_{0} = \frac{1}{\sqrt{L C}}$, where the impedance is minimum ($Z = R$) and the current amplitude is maximum.
*   The power factor is $\cos \phi$, representing the efficiency of power usage in the circuit.
*   At resonance, the voltages across the inductor and capacitor cancel each other out, leaving only the resistor voltage to oppose the source.