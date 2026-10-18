---
{
  "concept": "Resistance and Resistivity",
  "slug": "resistance-and-resistivity",
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
    "completion_tokens": 1567,
    "prompt_tokens": 5231,
    "total_tokens": 6798,
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
  "generated_at": "2026-10-18T05:58:20",
  "source_grade": 10,
  "grade_delta": 0,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g10_science_chapter11_014",
      "chapter": "chapter11",
      "section": "11.5 FACTORS ON WHICH THE RESISTANCE OF A CONDUCTOR DEPENDS — Activity 11.3"
    },
    {
      "ref": "S2",
      "passage_id": "g10_science_chapter11_015",
      "chapter": "chapter11",
      "section": "11.5 FACTORS ON WHICH THE RESISTANCE OF A CONDUCTOR DEPENDS — Activity 11.3"
    },
    {
      "ref": "S3",
      "passage_id": "g10_science_chapter11_016",
      "chapter": "chapter11",
      "section": "11.5 FACTORS ON WHICH THE RESISTANCE OF A CONDUCTOR DEPENDS — Activity 11.3"
    },
    {
      "ref": "S4",
      "passage_id": "g10_science_chapter11_017",
      "chapter": "chapter11",
      "section": "11.5 FACTORS ON WHICH THE RESISTANCE OF A CONDUCTOR DEPENDS — Activity 11.3"
    },
    {
      "ref": "S5",
      "passage_id": "g10_science_chapter11_018",
      "chapter": "chapter11",
      "section": "11.5 FACTORS ON WHICH THE RESISTANCE OF A CONDUCTOR DEPENDS — Activity 11.3"
    }
  ],
  "citation_check": {
    "cited": [
      "1",
      "2",
      "3",
      "5"
    ],
    "invented_citations": [],
    "unused_sources": [
      "4"
    ],
    "explanatory_paragraphs_without_a_citation": 0,
    "words": 1051,
    "target_words": [
      1000,
      1350
    ],
    "untraceable_sections": 0,
    "ok": true,
    "structural_problems": [
      "arithmetic: '2 = ((1)/(4))' -- 2 is 2, the page writes ((1)/(4))",
      "arithmetic: '2 = ((1)/(4)) * 4' -- 2 is 2, the page writes ((1)/(4)) * 4"
    ]
  },
  "terms": [
    "resistance",
    "resistivity",
    "conductor",
    "cross-sectional area",
    "ohm",
    "metre",
    "temperature",
    "alloy"
  ]
}
---

# Resistance and Resistivity

When electricity flows through a wire, it is not perfectly free. The wire pushes back against the flow, and this opposition is called resistance. Resistance matters because it controls how much current can pass through a circuit. A wire with high resistance allows very little current, while a wire with low resistance allows a lot of current. Understanding what causes this opposition helps us design safe and efficient electrical systems, from the wires in our homes to the heating elements in our toasters.

## The Formula for Resistance

The resistance of a uniform metallic conductor depends on three main factors. First, it depends on the length of the conductor. Second, it depends on the area of cross-section of the wire. Third, it depends on the nature of the material of the conductor. Precise measurements have shown that resistance is directly proportional to the length ($l$) and inversely proportional to the area of cross-section ($A$). Combining these two relationships gives the formula:

$$
R = \rho \frac{l}{A}
$$

where $\rho$ (rho) is a constant of proportionality called the electrical resistivity of the material. The SI unit of resistivity is $\Omega$ m. Resistivity is a characteristic property of the material, meaning it is an intrinsic measure of how strongly a material opposes the flow of electric current.

## How Length and Thickness Affect Resistance

Let us look at how the physical dimensions of a wire change its resistance. If you take a nichrome wire and double its length while keeping the thickness the same, the resistance of the wire doubles. This happens because the electrons have to travel a longer path through the material, bumping into more atoms along the way. 

On the other hand, if you keep the length the same but use a thicker wire, the resistance decreases. A thicker wire has a larger area of cross-section, which gives the electrons more space to move through the wire. Think of it like traffic on a road. A single-lane road will cause a traffic jam if too many cars try to use it. A six-lane highway, however, can easily handle the same number of cars because there is more space for them to move freely.

## How Material Affects Resistance

The material of the wire also plays a huge role in determining the resistance. Different materials have different resistivities. Metals and alloys have very low resistivity in the range of $10^{-8}$ $\Omega$ m to $10^{-6}$ $\Omega$ m. They are good conductors of electricity. For example, silver has a resistivity of $1.60 \times 10^{-8}$ $\Omega$ m, and copper has a resistivity of $1.62 \times 10^{-8}$ $\Omega$ m.

Insulators like rubber and glass have resistivity of the order of $10^{12}$ to $10^{17}$ $\Omega$ m. They are very poor conductors of electricity because their resistivity is extremely high. 

The resistivity of an alloy is generally higher than that of its constituent metals. Alloys do not oxidise (burn) readily at high temperatures. For this reason, they are commonly used in electrical heating devices, like electric iron and toasters. Tungsten is used almost exclusively for filaments of electric bulbs, whereas copper and aluminium are generally used for electrical transmission lines.

## Temperature and Resistivity

Both the resistance and resistivity of a material vary with temperature. When the temperature of a conductor increases, the atoms inside it vibrate more vigorously. This increased vibration makes it harder for the electrons to flow, which in turn increases the resistance of the material. This is why a wire can heat up when a large current passes through it, and its resistance will change as it gets hotter.

## Worked Example

Let us apply the formula for resistance to a practical situation. Imagine you have a metal wire that is 1 metre long. The diameter of the wire is 0.3 mm, and its resistance at 20°C is 26 $\Omega$. We want to find the resistivity of the metal at that temperature.

First, we need to calculate the area of cross-section of the wire. The diameter $d$ is $0.3$ mm, which is $3 \times 10^{-4}$ m. The area $A$ is given by the formula $\pi d^2 / 4$. Substituting the values, we get:

$$
A = \frac{\pi (3 \times 10^{-4})^2}{4} \approx 7.07 \times 10^{-8} \, \text{m}^2
$$

Now, we use the formula for resistivity: $\rho = RA / l$. Substituting the given values:

$$
\rho = \frac{26 \times 7.07 \times 10^{-8}}{1}
$$

$$
\rho = 1.84 \times 10^{-6} \, \Omega \text{m}
$$

The resistivity of the metal at 20°C is $1.84 \times 10^{-6}$ $\Omega$ m. This value is the resistivity of manganese.

## Worked Example: Changing the Dimensions

Let us try another example to see how changing the dimensions of a wire affects its resistance. A wire of a given material has a length $l$ and an area of cross-section $A$. This wire has a resistance of 4 $\Omega$. 

Now, we want to find the resistance of a second wire made of the same material. The second wire has a length of $l/2$ and an area of cross-section of $2A$. 

For the first wire, the resistance is given by:
$$
R_{\text{first}} = \rho \frac{l}{A} = 4 \, \Omega
$$

For the second wire, the resistance is:
$$
R_{\text{second}} = \rho \frac{l/2}{2A} = \frac{1}{4} \rho \frac{l}{A}
$$

Since $\rho l / A = 4\,\Omega$, we can substitute this into the equation for the second wire:
$$
R_{\text{second}} = \frac{1}{4} \times 4 \, \Omega = 1 \, \Omega
$$

The resistance of the new wire is $1 \, \Omega$.

## Key points

- Resistance is the opposition a conductor offers to the flow of electric current.
- Resistance depends on the length, area of cross-section, and the material of the conductor.
- The formula for resistance is $R = \rho l / A$, where $\rho$ is the resistivity.
- Metals have low resistivity and are good conductors, while insulators have very high resistivity.
- The resistivity of an alloy is generally higher than that of its constituent metals.
- Both resistance and resistivity of a material vary with temperature.