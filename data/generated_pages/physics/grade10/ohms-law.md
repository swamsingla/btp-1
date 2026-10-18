---
{
  "concept": "Ohm's Law",
  "slug": "ohms-law",
  "grade": 10,
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
    "completion_tokens": 1430,
    "prompt_tokens": 4348,
    "total_tokens": 5778,
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
  "generated_at": "2026-10-18T05:57:16",
  "source_grade": 10,
  "grade_delta": 0,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g10_science_chapter11_008",
      "chapter": "chapter11",
      "section": "11.4 OHM'S LAW"
    },
    {
      "ref": "S2",
      "passage_id": "g10_science_chapter11_009",
      "chapter": "chapter11",
      "section": "11.4 OHM'S LAW — Activity 11.1"
    },
    {
      "ref": "S3",
      "passage_id": "g10_science_chapter11_010",
      "chapter": "chapter11",
      "section": "11.4 OHM'S LAW — Activity 11.1"
    },
    {
      "ref": "S4",
      "passage_id": "g10_science_chapter11_011",
      "chapter": "chapter11",
      "section": "11.4 OHM'S LAW — Activity 11.1"
    },
    {
      "ref": "S5",
      "passage_id": "g10_science_chapter11_012",
      "chapter": "chapter11",
      "section": "11.4 OHM'S LAW — Activity 11.2"
    },
    {
      "ref": "S6",
      "passage_id": "g10_science_chapter11_013",
      "chapter": "chapter11",
      "section": "11.4 OHM'S LAW — Activity 11.2"
    }
  ],
  "citation_check": {
    "cited": [
      "3",
      "4",
      "5"
    ],
    "invented_citations": [],
    "unused_sources": [
      "1",
      "2",
      "6"
    ],
    "explanatory_paragraphs_without_a_citation": 1,
    "words": 1084,
    "target_words": [
      1000,
      1350
    ],
    "untraceable_sections": 0,
    "ok": true,
    "structural_problems": []
  },
  "terms": [
    "ohm's law",
    "potential difference",
    "current",
    "resistance",
    "ohm",
    "conductor",
    "resistor",
    "insulator",
    "variable resistance",
    "rheostat"
  ]
}
---

# Ohm's Law

Have you ever wondered how the current through a wire depends on the voltage applied across it? The answer lies in a fundamental principle of physics known as Ohm's law. This law relates the electric current through a conductor to the potential difference across it. Understanding this relationship is essential for designing circuits and choosing the right components for everyday appliances.

## The Basic Relationship

In 1827, a German physicist named Georg Simon Ohm discovered a simple but powerful rule about electricity. He found that the potential difference across a metallic wire is directly proportional to the current flowing through it, as long as the temperature remains the same. This means that if you increase the voltage, the current increases by the exact same factor. 

This relationship is written as $V \propto I$. We can turn this proportionality into an exact equation by introducing a constant of proportionality. This constant is called resistance, represented by the letter $R$ and measured in ohms (symbol $\Omega$, the Greek letter omega). The equation becomes $V = IR$. 

To understand this better, imagine pouring water through a pipe. If the water pressure is low, only a small amount of water flows out. If you increase the pressure, more water flows. Resistance is simply the friction inside the pipe that slows the water down. In electronics, resistance is the property of a conductor that resists the flow of electric charges.

## Measuring Resistance

From the equation $V = IR$, we can rearrange it to solve for resistance. By dividing the potential difference by the current, we find the resistance of the material. The formula is $R = V / I$.

The unit of resistance is the ohm ($\Omega$). We define one ohm as the resistance of a conductor when a potential difference of exactly 1 volt produces a current of exactly 1 ampere. This means that 1 ohm equals 1 volt divided by 1 ampere.

## Factors Affecting Current

Ohm's law also shows us how current changes when we change the resistance. If we rearrange the formula to solve for current, we get $I = V / R$. This equation tells us that the current through a resistor is inversely proportional to its resistance. 

This is a crucial concept in practical electronics. If you double the resistance in a circuit, the current flowing through it will be cut in half, assuming the voltage stays the same. Conversely, if you halve the resistance, the current will double. 

In everyday life, we use this principle constantly. When you dim a light in your house, you are increasing the resistance in the circuit to reduce the current. A component specifically designed to regulate current without changing the voltage source is called a variable resistance. A common device used to change the resistance in a circuit is called a rheostat.

## Conductors and Insulators

Not all materials behave the same way when electricity passes through them. In a famous classroom activity, students connect different components in a circuit to see how much current flows through them. 

When a nichrome wire is connected in the circuit, a certain amount of current flows. When a torch bulb is connected, the current is different. When a 10-watt bulb is connected, the current is different again. 

Why do these readings differ? The answer lies in the resistance of the material. Certain components offer an easy path for the flow of electric current, while others strongly resist it. 

To understand this, we must look at what happens inside a conductor. The motion of electrons in an electric circuit constitutes an electric current. However, these electrons are not completely free to move. They are restrained by the attraction of the atoms among which they move. 

This atomic attraction acts like a drag on the electrons, retarding their motion through the conductor. This drag is what we call resistance. A component of a given size that offers a low resistance is a good conductor, like copper. A conductor having some appreciable resistance is called a resistor, like nichrome. A component of identical size that offers a higher resistance is a poor conductor. An insulator of the same size offers even higher resistance, blocking the flow of current almost entirely.

## Worked example

Let us apply these rules to a practical problem. Imagine you have a nichrome wire connected to a battery. You measure the potential difference across the wire and find it to be 4 volts. You also measure the current flowing through the wire and find it to be 0.8 amperes. 

To find the resistance of the wire, you use the formula $R = V / I$. 

Substituting the values, we get:
$R = \frac{4}{0.8}$

$R = 5 \Omega$

This means the nichrome wire has a resistance of 5 ohms. 

Now, let us imagine you replace the nichrome wire with a torch bulb. You keep the battery the same, so the voltage remains 4 volts. However, you measure the current and find it is now only 0.2 amperes. 

Using the same formula, $R = \frac{4}{0.2}$

$R = 20 \Omega$

This shows that the torch bulb has a much higher resistance than the nichrome wire. Because of this higher resistance, less current is able to flow through the circuit.

## Key points

- Ohm's law states that the potential difference across a conductor is directly proportional to the current through it, provided the temperature remains constant.
- The relationship is expressed by the equation $V = IR$, where $V$ is potential difference, $I$ is current, and $R$ is resistance.
- Resistance is the property of a conductor that resists the flow of electric charges, and its SI unit is the ohm ($\Omega$).
- The formula $R = V / I$ allows us to calculate the resistance of a material if we know the voltage and current.
- Current is inversely proportional to resistance, as shown by the formula $I = V / R$.
- Different materials, such as nichrome, torch bulbs, and 10-watt bulbs, offer different levels of resistance to the flow of current.
- The motion of electrons is retarded by the attraction of atoms within the conductor, which creates the resistance.
- A good conductor offers low resistance, a resistor offers appreciable resistance, and an insulator offers very high resistance.