---
{
  "concept": "Alternating Current",
  "slug": "alternating-current",
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
    "completion_tokens": 2040,
    "prompt_tokens": 7099,
    "total_tokens": 9139,
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
  "generated_at": "2026-10-08T09:13:37",
  "source_grade": 12,
  "grade_delta": 0,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g12_physics_part1_chapter7_006",
      "chapter": "chapter7",
      "section": "7.2 AC VOLTAGE APPLIED TO A RESISTOR"
    },
    {
      "ref": "S2",
      "passage_id": "g12_physics_part1_chapter7_021",
      "chapter": "chapter7",
      "section": "7.6.1 Phasor-diagram solution"
    },
    {
      "ref": "S3",
      "passage_id": "g12_physics_part1_chapter7_000",
      "chapter": "chapter7",
      "section": "7.1 INTRODUCTION"
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
    "words": 1155,
    "target_words": [
      1050,
      1450
    ],
    "untraceable_sections": 0,
    "ok": true,
    "structural_problems": [],
    "grounding": {
      "cited_sentences": 32,
      "checked": 27,
      "not_judgeable_mostly_maths": 5,
      "cites_a_source_never_given": 0,
      "unsupported": [
        {
          "claim": "Unlike direct current, which flows steadily in one direction, alternating current is the type of electricity supplied to our homes and offices, making it essential for the daily operation of almost al",
          "cites": [
            "S3"
          ],
          "support_probability": 0.15
        },
        {
          "claim": "Similarly, we define the rms voltage or effective voltage by $V = \\frac{v_m}{\\sqrt{2}} = 0.707 \\, v_m$ .",
          "cites": [
            "S1"
          ],
          "support_probability": 0.423
        },
        {
          "claim": "For example, the household line voltage of 220 V is an rms value with a peak voltage of $v_m = \\sqrt{2} V = (1.414) (220 \\mathrm{V}) = 311 \\mathrm{V}$ .",
          "cites": [
            "S1"
          ],
          "support_probability": 0.102
        },
        {
          "claim": "From previous sections, we know that the voltage across the resistor $V_R$ is parallel to the current $I$, the voltage across the capacitor $V_C$ is $\\pi/2$ behind the current, and the voltage across ",
          "cites": [
            "S2"
          ],
          "support_probability": 0.156
        },
        {
          "claim": "Since $V$ is represented as the hypotenuse of a right-triangle whose sides are $V_R$ and $(V_C + V_L)$, the pythagorean theorem gives $v_m^2 = v_{Rm}^2 + (v_{Cm} - v_{Lm})^2$ .",
          "cites": [
            "S2"
          ],
          "support_probability": 0.457
        },
        {
          "claim": "Substituting the values of $v_{Rm}$, $v_{Cm}$, and $v_{Lm}$ from Eq. (7.22) into the above equation, we have $v_m^2 = (i_m R)^2 + (i_m X_C - i_m X_L)^2$ .",
          "cites": [
            "S2"
          ],
          "support_probability": 0.291
        }
      ],
      "unsupported_fraction": 0.222,
      "threshold": 0.5,
      "max_unsupported_fraction": 0.34
    },
    "verification": {
      "verdict": "spiralled",
      "checks": 1,
      "tokens": 10128
    }
  },
  "terms": [
    "alternating current",
    "direct current",
    "resistor",
    "inductor",
    "capacitor",
    "impedance",
    "phasor",
    "rms value",
    "peak value",
    "phase angle",
    "angular frequency"
  ]
}
---

# Alternating Current

Alternating current is the flow of electric charge that periodically reverses its direction. Unlike direct current, which flows steadily in one direction, alternating current is the type of electricity supplied to our homes and offices, making it essential for the daily operation of almost all modern electrical devices. The main reason for preferring alternating current over direct current is that ac voltages can be easily and efficiently converted from one voltage to another by means of transformers, allowing electrical energy to be transmitted economically over long distances.

## AC Voltage Applied to a Resistor

When an ac source is connected to a pure resistor, the voltage and current vary sinusoidally. Let the potential difference, or ac voltage, be given by $v = v_m \sin \omega t$. Applying Kirchhoff's loop rule to the circuit, we find the current through the resistor to be $i = \frac{v_m}{R} \sin \omega t$. Since $R$ is a constant, we can write this equation as $i = i_m \sin \omega t$, where the current amplitude $i_m$ is given by $i_m = \frac{v_m}{R}$.

Equation (7.3) is Ohm's law, which for resistors, works equally well for both ac and dc voltages. The voltage across a pure resistor and the current through it are in phase with each other. This means that both $v$ and $i$ reach zero, minimum, and maximum values at the same time. Because the current varies sinusoidally with corresponding positive and negative values during each cycle, the sum of the instantaneous current values over one complete cycle is zero, and the average current is zero.

However, the fact that the average current is zero does not mean that the average power consumed is zero. As you know, Joule heating is given by $i^2 R$ and depends on $i^2$ (which is always positive whether $i$ is positive or negative) and not on $i$. Thus, there is Joule heating and dissipation of electrical energy when an ac current passes through a resistor. The instantaneous power dissipated in the resistor is $p = i^2 R = i_m^2 R \sin^2 \omega t$. The average value of $p$ over a cycle is $\overline{p} = \frac{1}{2} i_m^2 R$.

To express ac power in the same form as dc power $(P = I^2 R)$, a special value of current is defined and used. It is called, root mean square (rms) or effective current and is denoted by $I_{rms}$ or $I$. The rms current $I$ is related to the peak current $i_m$ by $I = i_m / \sqrt{2} = 0.707 \, i_m$.

In terms of $I$, the average power, denoted by $P$, is $P = \frac{1}{2} i_m^2 R = I^2 R$. Similarly, we define the rms voltage or effective voltage by $V = \frac{v_m}{\sqrt{2}} = 0.707 \, v_m$. From Eq. (7.3), we have $v_m = i_m R$ or, $\frac{v_m}{\sqrt{2}} = \frac{i_m}{\sqrt{2}} R$, or, $V = IR$. Equation (7.9) gives the relation between ac current and ac voltage and is similar to that in the dc case.

It is customary to measure and specify rms values for ac quantities. For example, the household line voltage of 220 V is an rms value with a peak voltage of $v_m = \sqrt{2} V = (1.414) (220 \mathrm{V}) = 311 \mathrm{V}$.

## AC Circuits with L and C

In a series circuit containing an inductor and a capacitor, the ac current in each element is the same at any time, having the same amplitude and phase. Let the current be $i = i_m \sin (\omega t + \phi)$, where $\phi$ is the phase difference between the voltage across the source and the current in the circuit.

From previous sections, we know that the voltage across the resistor $V_R$ is parallel to the current $I$, the voltage across the capacitor $V_C$ is $\pi/2$ behind the current, and the voltage across the inductor $V_L$ is $\pi/2$ ahead of the current. The length of these phasors or the amplitude of $V_R$, $V_C$, and $V_L$ are $v_{Rm} = i_m R$, $v_{Cm} = i_m X_C$, $v_{Lm} = i_m X_L$.

The voltage equation for the circuit can be written as $V_L + V_R + V_C = V$. Since $V_C$ and $V_L$ are always along the same line and in opposite directions, they can be combined into a single phasor $(V_C + V_L)$ which has a magnitude $|v_{Cm} - v_{Lm}|$. Since $V$ is represented as the hypotenuse of a right-triangle whose sides are $V_R$ and $(V_C + V_L)$, the pythagorean theorem gives $v_m^2 = v_{Rm}^2 + (v_{Cm} - v_{Lm})^2$. Substituting the values of $v_{Rm}$, $v_{Cm}$, and $v_{Lm}$ from Eq. (7.22) into the above equation, we have $v_m^2 = (i_m R)^2 + (i_m X_C - i_m X_L)^2$.

By analogy to the resistance in a circuit, we introduce the impedance $Z$ in an ac circuit. $Z = \sqrt{R^2 + (X_C - X_L)^2}$. The current amplitude is $i_m = \frac{v_m}{Z}$.

The phase angle $\phi$ is the angle between $V_R$ and $V$ and can be determined by $\tan \phi = \frac{v_{Cm} - v_{Lm}}{v_{Rm}}$. Using Eq. (7.22), we have $\tan \phi = \frac{X_C - X_L}{R}$.

If $X_C > X_L$, $\phi$ is positive and the circuit is predominantly capacitive. Consequently, the current in the circuit leads the source voltage. If $X_C < X_L$, $\phi$ is negative and the circuit is predominantly inductive. Consequently, the current in the circuit lags the source voltage.

## Worked example

A light bulb is rated at 100W for a 220 V supply. We are given $P = 100 \, \mathrm{W}$ and $V = 220 \, \mathrm{V}$.

(a) The resistance of the bulb is $R = \frac{V^2}{P} = \frac{(220 \mathrm{V})^2}{100 \mathrm{W}} = 484 \Omega$.

(b) The peak voltage of the source is $v_m = \sqrt{2} V = 311 \mathrm{V}$.

(c) Since $P = I V$, the rms current through the bulb is $I = \frac{P}{V} = \frac{100 \mathrm{W}}{220 \mathrm{V}} = 0.454 \mathrm{A}$.

## Key points

*   Alternating current periodically reverses its direction, unlike direct current.
*   The voltage and current are in phase with each other when an ac source is connected to a pure resistor.
*   The average current over one complete cycle is zero, but there is Joule heating and dissipation of electrical energy.
*   The rms current $I$ is related to the peak current $i_m$ by $I = i_m / \sqrt{2} = 0.707 \, i_m$.
*   The average power in an ac circuit is $P = I^2 R$.
*   The impedance $Z$ in an ac circuit is $Z = \sqrt{R^2 + (X_C - X_L)^2}$.
*   The phase angle $\phi$ in an LCR circuit is given by $\tan \phi = \frac{X_C - X_L}{R}$.