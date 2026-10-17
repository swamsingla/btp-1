---
{
  "concept": "Equations of Motion",
  "slug": "equations-of-motion",
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
    "completion_tokens": 1516,
    "prompt_tokens": 6595,
    "total_tokens": 8111,
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
  "generated_at": "2026-10-17T15:47:05",
  "source_grade": 9,
  "grade_delta": 0,
  "sources": [
    {
      "ref": "S1",
      "passage_id": "g9_science_chapter7_028",
      "chapter": "chapter7",
      "section": "7.5 Equations of Motion"
    },
    {
      "ref": "S2",
      "passage_id": "g9_science_chapter7_018",
      "chapter": "chapter7",
      "section": "7.4 Graphical Representation of Motion"
    },
    {
      "ref": "S3",
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
    "unused_sources": [
      "3"
    ],
    "explanatory_paragraphs_without_a_citation": 1,
    "words": 1059,
    "target_words": [
      1000,
      1350
    ],
    "untraceable_sections": 0,
    "ok": true,
    "structural_problems": []
  },
  "terms": [
    "uniform acceleration",
    "initial velocity",
    "final velocity",
    "acceleration",
    "distance",
    "time",
    "velocity-time graph",
    "area under the graph",
    "slope of the graph"
  ]
}
---

# Equations of Motion

When an object moves along a straight line with uniform acceleration, it is possible to relate its velocity, acceleration during motion and the distance covered by it in a certain time interval by a set of equations known as the equations of motion. These three equations are powerful because they allow you to calculate exactly how an object's speed changes over time without having to draw a graph every time you need an answer. For example, if you are calculating the stopping distance of a bus on a highway, these formulas give you the exact distance covered before the vehicle comes to a complete halt.

## The Three Equations

When an object moves with uniform acceleration, it means its speed increases or decreases by the exact same amount every second. To use the equations, we assign variables to the basic properties of the motion. The initial velocity is the speed at the very beginning of the journey and is represented by the letter $u$. The final velocity, which is the speed at the very end of the interval, is represented by $v$. The acceleration, or the rate at which the speed changes, is represented by $a$, and the total time taken is represented by $t$. Finally, the total distance covered during this time is represented by $s$.

The first equation relates the final velocity to the initial velocity, acceleration, and time. It is written as $v = u + at$. This equation is incredibly useful when you know the starting speed, the acceleration, and the duration of the trip, and you want to find out how fast the object is moving at the end.

The second equation relates the distance covered to the initial velocity, acceleration, and time. It is written as $s = ut + \frac{1}{2}at^2$. This formula is essential for finding out exactly how far an object has traveled during a specific period of uniform acceleration.

The third equation relates the final velocity and the initial velocity directly to the acceleration and the distance traveled, completely eliminating the time variable. It is written as $v^2 = u^2 + 2as$. This equation is extremely helpful when you know the starting speed, the acceleration, and the distance covered, and you need to find the final speed without knowing exactly how many seconds the journey took.

## Graphical Derivation

We can derive these equations by looking at the motion of an object on a velocity-time graph. On this graph, the vertical axis represents the velocity of the object, and the horizontal axis represents the time elapsed.

When an object moves with uniform acceleration, the line on the graph is a straight line that slopes upwards if the object is speeding up, or slopes downwards if it is slowing down. The area under this straight-line graph represents the total distance traveled by the object.

To find the area under the graph, we can use simple geometry. The graph forms a rectangle and a triangle. The area of the rectangle is the base times the height, which is $ut$. The area of the triangle is one-half times the base times the height, which is $\frac{1}{2}at^2$. Adding these two areas together gives the total distance, which is $s = ut + \frac{1}{2}at^2$. This is the second equation of motion.

We can also find the final velocity using the graph. The slope of the line on the graph is the acceleration. The change in velocity over time is $v - u$, and the time taken is $t$. Therefore, the slope is $\frac{v - u}{t}$, which is equal to the acceleration $a$. Rearranging this gives the first equation, $v = u + at$.

To get the third equation, we use a geometric property of the graph. The area under the graph can also be calculated as the average velocity multiplied by the time. The average velocity is $\frac{u + v}{2}$. Multiplying this by the time $t$ gives the distance: $s = \frac{u + v}{2} \times t$. Since we know $t = \frac{v - u}{a}$, we can substitute this into the equation to get $s = \frac{(u + v)(v - u)}{2a}$. Simplifying the numerator gives $v^2 - u^2$, leading to the third equation, $v^2 = u^2 + 2as$.

## Worked Example

Let us apply these equations to a real-world scenario. Imagine a racing car that starts from rest, meaning its initial velocity $u$ is $0 \, \text{m s}^{-1}$. The car accelerates uniformly at $4 \, \text{m s}^{-2}$ for a duration of $10$ seconds. 

First, let us find the final velocity of the car using the first equation, $v = u + at$. Substituting the values, we get $v = 0 + (4 \times 10)$, which means the final velocity $v$ is $40 \, \text{m s}^{-1}$.

Next, let us calculate the distance the car covers during this time using the second equation, $s = ut + \frac{1}{2}at^2$. Substituting the values, we get $s = (0 \times 10) + \frac{1}{2} \times 4 \times (10)^2$. This simplifies to $s = 0 + \frac{1}{2} \times 4 \times 100$, which means the distance $s$ is $200 \, \text{m}$.

Finally, let us verify our answer using the third equation, $v^2 = u^2 + 2as$. Substituting the values, we get $40^2 = 0^2 + 2 \times 4 \times 200$. This simplifies to $1600 = 1600$, which confirms that our calculations are correct.

## A Braking Example

A bus travelling at $20 \, \text{m s}^{-1}$ is brought to rest by brakes that give it a uniform retardation of $5 \, \text{m s}^{-2}$. The acceleration is therefore $a = -5 \, \text{m s}^{-2}$, with $u = 20 \, \text{m s}^{-1}$ and $v = 0$. Here the time is not given, so the third equation is the best choice: $0 = 20^2 + 2 \times (-5) \times s$, which gives $10 s = 400$ and $s = 40 \, \text{m}$. The bus travels $40 \, \text{m}$ before stopping. We can check this with the first equation, $0 = 20 + (-5)t$, which gives $t = 4 \, \text{s}$, and then with the second equation, $s = 20 \times 4 + \frac{1}{2} \times (-5) \times 4^2 = 80 - 40 = 40 \, \text{m}$.

## Key points

*   Equations of motion are used to describe the motion of an object moving along a straight line with uniform acceleration.
*   The three primary equations are $v = u + at$, $s = ut + \frac{1}{2}at^2$, and $v^2 = u^2 + 2as$.
*   These equations can be derived using the geometric properties of a straight-line velocity-time graph, where the area under the line represents the distance traveled.
*   The variables $u$, $v$, $a$, $t$, and $s$ represent initial velocity, final velocity, acceleration, time, and distance, respectively.
*   Equations of motion are fundamental for solving practical problems, such as calculating the stopping distance of a vehicle or the acceleration of a moving train.