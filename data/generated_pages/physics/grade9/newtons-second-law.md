---
{
  "concept": "Newton's Second Law of Motion",
  "slug": "newtons-second-law",
  "grade": 9,
  "language": "en",
  "subject": "physics",
  "area": "Mechanics",
  "model": "sarvam-105b",
  "settings": {
    "temperature": 0.3,
    "max_tokens": 8000,
    "reasoning_effort": "none"
  },
  "usage": {
    "completion_tokens": 1619,
    "prompt_tokens": 5377,
    "total_tokens": 6996,
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
  "generated_at": "2026-10-17T15:47:34",
  "source_grade": 9,
  "grade_delta": 0,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g9_science_chapter8_014",
      "chapter": "chapter8",
      "section": "8.4 Second Law of Motion"
    },
    {
      "ref": "S2",
      "passage_id": "g9_science_chapter8_016",
      "chapter": "chapter8",
      "section": "8.4.1 MATHEMATICAL FORMULATION OF SECOND LAW OF MOTION"
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
    "words": 1065,
    "target_words": [
      1000,
      1350
    ],
    "untraceable_sections": 0,
    "ok": true,
    "structural_problems": [
      "arithmetic: '1 = 2     * 5  = 10       .' -- 1 is 1, the page writes 2     * 5",
      "arithmetic: '2 = 4     * 2  = 8       .' -- 2 is 2, the page writes 4     * 2"
    ]
  },
  "terms": [
    "force",
    "mass",
    "acceleration",
    "momentum",
    "newton",
    "unbalanced force"
  ]
}
---

# Newton's Second Law of Motion

Newton's Second Law of Motion tells us exactly how much force is needed to make an object speed up, slow down, or change its direction. It connects the push or pull on an object to how heavy the object is and how quickly it changes its speed. Understanding this rule is the foundation of physics because it allows us to calculate the exact forces acting on everything from a cricket ball to a motorcar.

## What the Law States
The second law of motion states that the rate of change of momentum of an object is proportional to the applied unbalanced force in the direction of force. Momentum is a property of an object that combines its mass and its velocity. The formula for momentum is $p = m v$. Because a force changes an object's velocity, it naturally produces a change in momentum. The law explains that the faster you want to change an object's momentum, the greater the force you must apply.

## The Mathematical Formulation
To use this law in calculations, we write it as an equation. Suppose an object of mass, $m$ is moving along a straight line with an initial velocity, $u$. If a constant force, $F$ acts on it for a time, $t$, it accelerates to a final velocity, $v$. The initial momentum is $p_{1} = m u$ and the final momentum is $p_{2} = m v$. The change in momentum is $p_{2} - p_{1}$, which simplifies to $m \times (v - u)$. The rate of change of momentum is therefore $\frac{m \times (v - u)}{t}$, and the applied force is proportional to this rate:

$$
F \propto \frac {m \times (v - u)}{t}
$$

We know that acceleration is defined as the rate of change of velocity, which is $a = \frac{v - u}{t}$. By substituting this into our force equation, we get $F \propto m a$. The constant of proportionality, $k$, is set to 1 to match our standard units, giving us the famous formula:

$$
F = m a
$$

The unit of force is chosen so that one unit of force produces an acceleration of $1 \, m \, s^{-2}$ in an object of $1 \, kg$ mass. This unit is the newton, which has the symbol N.

## Understanding the Units
The equation $F = m a$ shows that force is measured in kilogram-metre per second squared, or newtons. Mass is measured in kilograms (kg), and acceleration is measured in metres per second squared ($m \, s^{-2}$). This means that if you have a 1 kg object and you want to accelerate it at $1 \, m \, s^{-2}$, you need to apply exactly 1 newton of force. This relationship gives us a practical method to measure the force acting on an object.

## Force, Mass and Acceleration

Because $a = F/m$, the acceleration depends on both the force and the mass. For the same mass, doubling the force doubles the acceleration. For the same force, doubling the mass halves the acceleration. For example, a force of $10 \, \text{N}$ acting on a $2 \, \text{kg}$ trolley gives an acceleration of $10/2 = 5 \, \text{m s}^{-2}$, while the same force acting on a $4 \, \text{kg}$ trolley gives only $10/4 = 2.5 \, \text{m s}^{-2}$. This is why it is much harder to get a heavily loaded cart moving than an empty one.

## Everyday Applications
You can see this law in action every day. When a fielder catches a fast-moving cricket ball, they gradually pull their hands backwards with the moving ball. By doing so, the fielder increases the time during which the ball's velocity decreases to zero. This increases the time interval $t$, which decreases the acceleration of the ball, reducing the impact and preventing a painful catch. If the ball were stopped suddenly, its high velocity would drop to zero in a very short interval of time, resulting in a large rate of change of momentum and a large force on the fielder's palm.

Similarly, in a high jump event, athletes are made to fall on a cushioned bed or a sand bed. This increases the time of the athlete's fall to stop after making the jump, which decreases the rate of change of momentum and hence the force.

## Worked Example
Let us apply the rule $F = m a$ to a practical scenario. Imagine a motorcar moving with a velocity of $108 \, \text{km/h}$. It takes $4 \, \text{s}$ to stop after the brakes are applied. We want to calculate the force exerted by the brakes on the motorcar if its total mass along with the passengers is $1000 \, \text{kg}$.

First, we convert the initial velocity to metres per second:
$$
u = 108 \, \text{km/h} = 108 \times \frac{1000 \, \text{m}}{(60 \times 60) \, \text{s}} = 30 \, \text{m} \, s^{-1}
$$
The final velocity is $v = 0 \, \text{m} \, s^{-1}$. The time taken to stop the motorcar is $t = 4 \, \text{s}$.

Using the formula $F = \frac{m(v - u)}{t}$:
$$
F = \frac{1000 \, \text{kg} \times (0 - 30 \, \text{m} \, s^{-1})}{4 \, \text{s}} = -7500 \, \text{kg} \, \text{m} \, s^{-2}
$$
The magnitude of the force is $7500 \, \text{N}$. The negative sign tells us that the force exerted by the brakes is opposite to the direction of motion of the motorcar.

## Comparing Different Scenarios
The second law also helps us compare different situations. For example, which would require a greater force — accelerating a $2 \, \text{kg}$ mass at $5 \, m \, s^{-2}$ or a $4 \, \text{kg}$ mass at $2 \, m \, s^{-2}$?

Using $F = m a$:
For the first case: $F_1 = 2 \, \text{kg} \times 5 \, \text{m} \, s^{-2} = 10 \, \text{N}$.
For the second case: $F_2 = 4 \, \text{kg} \times 2 \, \text{m} \, s^{-2} = 8 \, \text{N}$.
Since $F_1 > F_2$, accelerating the $2 \, \text{kg}$ mass at $5 \, m \, s^{-2}$ requires a greater force.

## Key points
- The second law states that the rate of change of momentum is proportional to the applied unbalanced force.
- The mathematical formula is $F = m a$, where $F$ is force, $m$ is mass, and $a$ is acceleration.
- The unit of force is the newton (N), which is equal to $1 \, \text{kg} \, \text{m} \, s^{-2}$.
- Increasing the time of impact decreases the force experienced, as seen when a fielder pulls their hands back while catching a ball.
- The law allows us to calculate the exact magnitude and direction of forces acting on moving objects.