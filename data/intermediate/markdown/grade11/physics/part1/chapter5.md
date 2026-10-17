<!-- page 1 of 21 -->

11086CH06

CHAPTER FIVE

# WORK, ENERGY AND POWER

## 5.1 INTRODUCTION

5.1 Introduction

5.2 Notions of work and kinetic energy : The work-energy theorem

5.3 Work

5.4 Kinetic energy

5.5 Work done by a variable force

5.6 The work-energy theorem for a variable force

5.7 The concept of potential energy

5.8 The conservation of mechanical energy

5.9 The potential energy of a spring

5.10 Power

5.11 Collisions

Summary Points to ponder Exercises

The terms ‘work’, ‘energy’ and ‘power’ are frequently used in everyday language. A farmer ploughing the field, a construction worker carrying bricks, a student studying for a competitive examination, an artist painting a beautiful landscape, all are said to be working. In physics, however, the word ‘Work’ covers a definite and precise meaning. Somebody who has the capacity to work for 14-16 hours a day is said to have a large stamina or energy. We admire a long distance runner for her stamina or energy. Energy is thus our capacity to do work. In Physics too, the term ‘energy’ is related to work in this sense, but as said above the term ‘work’ itself is defined much more precisely. The word ‘power’ is used in everyday life with different shades of meaning. In karate or boxing we talk of ‘powerful’ punches. These are delivered at a great speed. This shade of meaning is close to the meaning of the word ‘power’ used in physics. We shall find that there is at best a loose correlation between the physical definitions and the physiological pictures these terms generate in our minds. The aim of this chapter is to develop an understanding of these three physical quantities. Before we proceed to this task, we need to develop a mathematical prerequisite, namely the scalar product of two vectors.

## 5.1.1 The Scalar Product

We have learnt about vectors and their use in Chapter 3. Physical quantities like displacement, velocity, acceleration, force etc. are vectors. We have also learnt how vectors are added or subtracted. We now need to know how vectors are multiplied. There are two ways of multiplying vectors which we shall come across: one way known as the scalar product gives a scalar from two vectors and the other known as the vector product produces a new vector from two vectors. We shall look at the vector product in Chapter 6. Here we take up the scalar product of two vectors. The scalar product or dot product of any two vectors A and B, denoted as A·B (read

Reprint 2025-26

<!-- page 2 of 21 -->

72

PHYSICS

A dot B) is defined as

$$
\mathbf {A} \cdot \mathbf {B} = A B \cos \theta\tag{5.1a}
$$

where  $\theta$  is the angle between the two vectors as shown in Fig. 5.1(a). Since A, B and  $\cos\theta$  are scalars, the dot product of A and B is a scalar quantity. Each vector, A and B, has a direction but their scalar product does not have a direction.

From Eq. (5.1a), we have

$$
\begin{array}{r} \mathbf {A} \cdot \mathbf {B} = A (B \cos \theta) \\ = B (A \cos \theta) \end{array}\tag{i}
$$

Or,

Geometrically, $B$ cos $\theta$ is the projection of $\mathbf{B}$ onto $\mathbf{A}$ in Fig.5.1 (b) and $A$ cos $\theta$ is the projection of $\mathbf{A}$ onto $\mathbf{B}$ in Fig. 5.1 (c). So, $\mathbf{A} \cdot \mathbf{B}$ is the product of the magnitude of $\mathbf{A}$ and the component of $\mathbf{B}$ along $\mathbf{A}$. Alternatively, it is the product of the magnitude of $\mathbf{B}$ and the component of $\mathbf{A}$ along $\mathbf{B}$.

Equation (5.1a) shows that the scalar product follows the commutative law :

$$
\mathbf {A} \cdot \mathbf {B} = \mathbf {B} \cdot \mathbf {A}
$$

Scalar product obeys the distributive law:

$$
\mathbf {A} \cdot (\mathbf {B} + \mathbf {C}) = \mathbf {A} \cdot \mathbf {B} + \mathbf {A} \cdot \mathbf {C}
$$

Further, $\mathbf{A}\cdot (\lambda \mathbf{B}) = \lambda (\mathbf{A}\cdot \mathbf{B})$

where $\lambda$ is a real number.

The proofs of the above equations are left to you as an exercise.

For unit vectors $\hat{\mathbf{i}},\hat{\mathbf{j}},\hat{\mathbf{k}}$ we have

$$
\begin{array}{l} \hat {\mathbf {i}} \cdot \hat {\mathbf {i}} = \hat {\mathbf {j}} \cdot \hat {\mathbf {j}} = \hat {\mathbf {k}} \cdot \hat {\mathbf {k}} = 1 \\ \hat {\mathbf {i}} \cdot \hat {\mathbf {j}} = \hat {\mathbf {j}} \cdot \hat {\mathbf {k}} = \hat {\mathbf {k}} \cdot \hat {\mathbf {i}} = 0 \end{array}
$$

Given two vectors

$$
\mathbf {A} = A _ {x} \hat {\mathbf {i}} + A _ {y} \hat {\mathbf {j}} + A _ {z} \hat {\mathbf {k}}
$$

$$
\mathbf {B} = B _ {x} \hat {\mathbf {i}} + B _ {y} \hat {\mathbf {j}} + B _ {z} \hat {\mathbf {k}}
$$

their scalar product is

$$
\mathbf {A} \cdot \mathbf {B} = \left(A _ {x} \hat {\mathbf {i}} + A _ {y} \hat {\mathbf {j}} + A _ {z} \hat {\mathbf {k}}\right) \cdot \left(B _ {x} \hat {\mathbf {i}} + B _ {y} \hat {\mathbf {j}} + B _ {z} \hat {\mathbf {k}}\right)
$$

$$
= A _ {x} B _ {x} + A _ {y} B _ {y} + A _ {z} B _ {z}\tag{5.1b}
$$

From the definition of scalar product and (Eq. 5.1b) we have :

$$
\mathbf {A} \cdot \mathbf {A} = A _ {x} A _ {x} + A _ {y} A _ {y} + A _ {z} A _ {z}
$$

$$
A ^ {2} = A _ {x} ^ {2} + A _ {y} ^ {2} + A _ {z} ^ {2}\tag{5.1c}
$$

since $\mathbf{A}\cdot \mathbf{A} = |\mathbf{A}||\mathbf{A}|\cos 0 = A^2$

(ii) $\mathbf{A}\cdot \mathbf{B} = 0$ , if A and B are perpendicular.

<div class="docvortex-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Example 5.1 Find the angle between force $\mathbf{F} = (3\hat{\mathbf{i}} + 4\hat{\mathbf{j}} - 5\hat{\mathbf{k}})$ unit and displacement $\mathbf{d} = (5\hat{\mathbf{i}} + 4\hat{\mathbf{j}} + 3\hat{\mathbf{k}})$ unit. Also find the projection of $\mathbf{F}$ on $\mathbf{d}$.
</div>

$$
\begin{array}{r l} \textbf {A n s w e r} \mathbf {F} \cdot \mathbf {d} & = F _ {x} d _ {x} + F _ {y} d _ {y} + F _ {z} d _ {z} \\ & = 3 (5) + 4 (4) + (- 5) (3) \\ & = 1 6 \text {unit} \end{array}
$$

$$
\begin{array}{r l} \text {Now} \mathbf {F} \cdot \mathbf {F} & = F ^ {2} = F _ {x} ^ {2} + F _ {y} ^ {2} + F _ {z} ^ {2} \\ & = 9 + 1 6 + 2 5 \\ & = 5 0 \text {unit} \end{array}
$$

![Image block](doc:281a2b5/tier:standard/page:2/block:33)

$$
\begin{array}{r l} \text {and} \mathbf {d} \cdot \mathbf {d} & = d ^ {2} = d _ {x} ^ {2} + d _ {y} ^ {2} + d _ {z} ^ {2} \\ & = 2 5 + 1 6 + 9 \\ & = 5 0 \text {unit} \end{array}
$$

$$
\begin{array}{r l} \therefore \cos \theta & = \frac {1 6}{\sqrt {5 0} \sqrt {5 0}} = \frac {1 6}{5 0} = 0. 3 2, \\ & \theta = \cos^ {- 1} 0. 3 2 \end{array}
$$

(a)

![Image block](doc:281a2b5/tier:standard/page:2/block:37)

(b)

![Image block](doc:281a2b5/tier:standard/page:2/block:39)

(c)

Fig. 5.1 (a) The scalar product of two vectors A and B is a scalar : A·B = A B cos θ. (b) B cos θ is the projection of B onto A. (c) A cos θ is the projection of A onto B.

Reprint 2025-26

<!-- page 3 of 21 -->

WORK, ENERGY AND POWER

73

## 5.2 NOTIONS OF WORK AND KINETIC ENERGY: THE WORK-ENERGY THEOREM

The following relation for rectilinear motion under constant acceleration $a$ has been encountered in Chapter 3,

$$
v ^ {2} - u ^ {2} = 2 a s\tag{5.2}
$$

where $u$ and $v$ are the initial and final speeds and $s$ the distance traversed. Multiplying both sides by $m/2$, we have

$$
\frac {1}{2} m v ^ {2} - \frac {1}{2} m u ^ {2} = m a s = F s\tag{5.2a}
$$

where the last step follows from Newton's Second Law. We can generalise Eq. (5.2) to three dimensions by employing vectors

$$
v ^2 - u^2 = 2 \text{ a.d}
$$

Here $\mathbf{a}$ and $\mathbf{d}$ are acceleration and displacement vectors of the object respectively.

Once again multiplying both sides by $m / 2$, we obtain

$$
\frac {1}{2} m v ^ {2} - \frac {1}{2} m u ^ {2} = m \mathbf {a}. \mathbf {d} = \mathbf {F}. \mathbf {d}\tag{5.2b}
$$

The above equation provides a motivation for the definitions of work and kinetic energy. The left side of the equation is the difference in the quantity 'half the mass times the square of the speed' from its initial value to its final value. We call each of these quantities the 'kinetic energy', denoted by $K$. The right side is a product of the displacement and the component of the force along the displacement. This quantity is called 'work' and is denoted by $W$. Eq. (5.2b) is then

$$
K _ {f} - K _ {i} = W\tag{5.3}
$$

where  $K_{i}$  and  $K_{f}$  are respectively the initial and final kinetic energies of the object. Work refers to the force and the displacement over which it acts. Work is done by a force on the body over a certain displacement.

Equation (5.2) is also a special case of the work-energy (WE) theorem : The change in kinetic energy of a particle is equal to the work done on it by the net force. We shall generalise the above derivation to a varying force in a later section.

Example 5.2 It is well known that a raindrop falls under the influence of the downward gravitational force and the opposing resistive force. The latter is known

to be proportional to the speed of the drop but is otherwise undetermined. Consider a drop of mass 1.00 g falling from a height 1.00 km. It hits the ground with a speed of 50.0 m s $^{-1}$ . (a) What is the work done by the gravitational force? What is the work done by the unknown resistive force?

Answer (a) The change in kinetic energy of the drop is

$$
\begin{array}{l} \Delta K = \frac {1}{2} m v ^ {2} - 0 \\ = \frac {1}{2} \times 1 0 ^ {- 3} \times 5 0 \times 5 0 \\ = 1. 2 5 \mathrm{J} \end{array}
$$

where we have assumed that the drop is initially at rest.

Assuming that $g$ is a constant with a value $10\mathrm{m / s^2}$, the work done by the gravitational force is,

$$
\begin{array}{r l} W _ {g} & = m g h \\ & = 1 0 ^ {- 3} \times 1 0 \times 1 0 ^ {3} \\ & = 1 0. 0 \mathrm{J} \end{array}
$$

(b) From the work-energy theorem

$$
\Delta K = W _{g} + W_{r}
$$

where $W_{r}$ is the work done by the resistive force on the raindrop. Thus

$$
\begin{array}{r l} W _ {r} & = \Delta K - W _ {g} \\ & = 1. 2 5 - 1 0 \\ & = - 8. 7 5 \mathrm{J} \end{array}
$$

is negative.

## 5.3 WORK

As seen earlier, work is related to force and the displacement over which it acts. Consider a constant force F acting on an object of mass m. The object undergoes a displacement d in the positive x-direction as shown in Fig. 5.2.

![Image block](doc:281a2b5/tier:standard/page:3/block:31)

Fig. 5.2 An object undergoes a displacement d under the influence of the force F.

Reprint 2025-26

<!-- page 4 of 21 -->

74

PHYSICS

The work done by the force is defined to be the product of component of the force in the direction of the displacement and the magnitude of this displacement. Thus

$$
W = (F \cos \theta) d = \mathbf {F}. \mathbf {d}\tag{5.4}
$$

We see that if there is no displacement, there is no work done even if the force is large. Thus, when you push hard against a rigid brick wall, the force you exert on the wall does no work. Yet your muscles are alternatively contracting and relaxing and internal energy is being used up and you do get tired. Thus, the meaning of work in physics is different from its usage in everyday language.

## No work is done if :

(i) the displacement is zero as seen in the example above. A weightlifter holding a 150 kg mass steadily on his shoulder for 30 s does no work on the load during this time.

(ii) the force is zero. A block moving on a smooth horizontal table is not acted upon by a horizontal force (since there is no friction), but may undergo a large displacement.

(iii) the force and displacement are mutually perpendicular. This is so since, for $\theta = \pi / 2$ rad (= 90°), cos ($\pi / 2$) = 0. For the block moving on a smooth horizontal table, the gravitational force $mg$ does no work since it acts at right angles to the displacement. If we assume that the moon's orbits around the earth is perfectly circular then the earth's gravitational force does no work. The moon's instantaneous displacement is tangential while the earth's force is radially inwards and $\theta = \pi / 2$.

Work can be both positive and negative. If  $\theta$  is between  $0^{\circ}$  and  $90^{\circ}$ ,  $\cos\theta$  in Eq. (5.4) is positive. If  $\theta$  is between  $90^{\circ}$  and  $180^{\circ}$ ,  $\cos\theta$  is negative. In many examples the frictional force opposes displacement and  $\theta = 180^{\circ}$ . Then the work done by friction is negative ( $\cos 180^{\circ} = -1$ ).

From Eq. (5.4) it is clear that work and energy have the same dimensions,  $[ML^{2}T^{-2}]$ . The SI unit of these is joule (J), named after the famous British physicist James Prescott Joule (1811-1869). Since work and energy are so widely used as physical concepts, alternative units abound and some of these are listed in Table 5.1.

Table 5.1 Alternative Units of Work/Energy in J

| erg | $10^{-7}$ J |
| --- | --- |
| electron volt (eV) | $1.6 \times 10^{-19}$ J |
| calorie (cal) | 4.186 J |
| kilowatt hour (kWh) | $3.6 \times 10^{6}$ J |

Example 5.3 A cyclist comes to a skidding stop in 10 m. During this process, the force on the cycle due to the road is 200 N and is directly opposed to the motion. (a) How much work does the road do on the cycle? (b) How much work does the cycle do on the road?

Answer Work done on the cycle by the road is the work done by the stopping (frictional) force on the cycle due to the road.

(a) The stopping force and the displacement make an angle of $180^{\circ}$ ($\pi$ rad) with each other. Thus, work done by the road,

$$
W _ {r} = F d \cos \theta
$$

$$
= 2 0 0 \times 1 0 \times \cos \pi
$$

$$
= - 2 0 0 0 \mathrm{J}
$$

It is this negative work that brings the cycle to a halt in accordance with WE theorem.

(b) From Newton's Third Law an equal and opposite force acts on the road due to the cycle. Its magnitude is 200 N. However, the road undergoes no displacement. Thus, work done by cycle on the road is zero.

The lesson of Example 5.3 is that though the force on a body A exerted by the body B is always equal and opposite to that on B by A (Newton's Third Law); the work done on A by B is not necessarily equal and opposite to the work done on B by A.

## 5.4 KINETIC ENERGY

As noted earlier, if an object of mass $m$ has velocity $\mathbf{v}$, its kinetic energy $K$ is

$$
K = \frac {1}{2} m \mathbf {v}. \mathbf {v} = \frac {1}{2} m v ^ {2}\tag{5.5}
$$

Kinetic energy is a scalar quantity. The kinetic energy of an object is a measure of the work an

Reprint 2025-26

<!-- page 5 of 21 -->

WORK, ENERGY AND POWER

75

Table 5.2 Typical kinetic energies (K)

| Object | Mass (kg) | Speed (m s-1) | K(J) |
| --- | --- | --- | --- |
| Car | 2000 | 25 | 6.3×105 |
| Running athlete | 70 | 10 | 3.5×103 |
| Bullet | 5×10-2 | 200 | 103 |
| Stone dropped from 10 m | 1 | 14 | 102 |
| Rain drop at terminal speed | 3.5×10-5 | 9 | 1.4×10-3 |
| Air molecule | ≈10-26 | 500 | ≈10-21 |

object can do by the virtue of its motion. This notion has been intuitively known for a long time. The kinetic energy of a fast flowing stream has been used to grind corn. Sailing ships employ the kinetic energy of the wind. Table 5.2 lists the kinetic energies for various objects.

Example 5.4 In a ballistics demonstration a police officer fires a bullet of mass 50.0 g with speed 200 m s $^{-1}$ (see Table 5.2) on soft plywood of thickness 2.00 cm. The bullet emerges with only 10% of its initial kinetic energy. What is the emergent speed of the bullet?

Answer The initial kinetic energy of the bullet is  $mv^{2}/2 = 1000 \, J$ . It has a final kinetic energy of  $0.1 \times 1000 = 100 \, J$ . If  $v_{f}$  is the emergent speed of the bullet,

$$
\frac {1}{2} m v _ {f} ^ {2} = 1 0 0 \text {J}
$$

$$
\begin{array}{r} v _ {f} = \sqrt {\frac {2 \times 1 0 0 \mathrm{J}}{0 . 0 5 \mathrm{kg}}} \\ = 6 3. 2 \mathrm{ms} ^ {- 1} \end{array}
$$

The speed is reduced by approximately 68% (not 90%).

## 5.5 WORK DONE BY A VARIABLE FORCE

A constant force is rare. It is the variable force, which is more commonly encountered. Fig. 5.3 is a plot of a varying force in one dimension.

If the displacement  $\Delta x$  is small, we can take the force  $F(x)$  as approximately constant and the work done is then

$$
\Delta W = F (x) \Delta x
$$

This is illustrated in Fig. 5.3(a). Adding successive rectangular areas in Fig. 5.3(a) we get the total work done as

$$
W \cong \sum_ {x _ {i}} ^ {x _ {f}} F (x) \Delta x\tag{5.6}
$$

where the summation is from the initial position $x_{i}$ to the final position $x_{f}$.

If the displacements are allowed to approach zero, then the number of terms in the sum increases without limit, but the sum approaches a definite value equal to the area under the curve in Fig. 5.3(b). Then the work done is

$$
\begin{array}{l} W = \lim _ {\Delta x \to 0} \sum_ {x _ {i}} ^ {x _ {f}} F (x) \Delta x \\ = \int_ {x _ {i}} ^ {x _ {f}} F (x)   \mathrm{d} x \end{array}\tag{5.7}
$$

where ‘lim’ stands for the limit of the sum when  $\Delta x$  tends to zero. Thus, for a varying force the work done can be expressed as a definite integral of force over displacement (see also Appendix 3.1).

![Chart block](doc:281a2b5/tier:standard/page:5/block:21)

Fig. 5.3(a)

Reprint 2025-26

<!-- page 6 of 21 -->

76

PHYSICS

![Chart block](doc:281a2b5/tier:standard/page:6/block:3)

Fig. 5.3 (a) The shaded rectangle represents the work done by the varying force $F(x)$, over the small displacement $\Delta x$, $\Delta W = F(x)\Delta x$. (b) adding the areas of all the rectangles we find that for $\Delta x\to 0$, the area under the curve is exactly equal to the work done by $F(x)$.

Example 5.5 A woman pushes a trunk on a railway platform which has a rough surface. She applies a force of 100 N over a distance of 10 m. Thereafter, she gets progressively tired and her applied force reduces linearly with distance to 50 N. The total distance through which the trunk has been moved is 20 m. Plot the force applied by the woman and the frictional force, which is 50 N versus displacement. Calculate the work done by the two forces over 20 m.

![Chart block](doc:281a2b5/tier:standard/page:6/block:6)

Fig. 5.4 Plot of the force F applied by the woman and the opposing frictional force f versus displacement.

The plot of the applied force is shown in Fig. 5.4. At $x = 20 \, \mathrm{m}$, $F = 50 \, \mathrm{N} (\neq 0)$. We are given that the frictional force $f$ is $|\mathbf{f}| = 50 \, \mathrm{N}$. It opposes motion and acts in a direction opposite to $\mathbf{F}$. It is therefore, shown on the negative side of the force axis.

The work done by the woman is

$W_{F} \rightarrow$  area of the rectangle ABCD + area of the trapezium CEID

$$
\left| \begin{array}{l} W _ {F} = 1 0 0 \times 1 0 + \frac {1}{2} (1 0 0 + 5 0) \times 1 0 \\ = 1 0 0 0 + 7 5 0 \\ = 1 7 5 0 \mathrm{J} \end{array} \right|
$$

The work done by the frictional force is

$$
\begin{array}{c} W _ {f} \to \text {area of the rectangle AGHI} \\ W _ {f} = (- 5 0) \times 2 0 \\ = - 1 0 0 0 \mathrm{J} \end{array}
$$

The area on the negative side of the force axis has a negative sign.

## 5.6 THE WORK-ENERGY THEOREM FOR A VARIABLE FORCE

We are now familiar with the concepts of work and kinetic energy to prove the work-energy theorem for a variable force. We confine ourselves to one dimension. The time rate of change of kinetic energy is

$$
\begin{array}{l} \frac {\mathrm{d} K}{\mathrm{d} t} = \frac {\mathrm{d}}{\mathrm{d} t} \left(\frac {1}{2} m   v ^ {2}\right) \\ \quad = m \frac {\mathrm{d} v}{\mathrm{d} t} v \\ \quad = F   v \text {(from Newton's Second Law)} \\ \quad = F \frac {\mathrm{d} x}{\mathrm{d} t} \\ \mathrm{d} K = F \mathrm{d} x \end{array}
$$

Thus

Integrating from the initial position $(x_{i})$ to final position $(x_{f})$, we have

$$
\left| \int_ {K _ {i}} ^ {K _ {f}} \mathrm{d} K = \int_ {x _ {i}} ^ {x _ {f}} F \mathrm{d} x \right|
$$

where, $K_{i}$ and $K_{f}$ are the initial and final kinetic energies corresponding to $x_{i}$ and $x_{\mathrm{f}}$.

or

$$
\left| K _ {f} - K _ {i} = \int_ {x _ {i}} ^ {x _ {f}} F \mathrm{d} x \right|\tag{5.8a}
$$

From Eq. (5.7), it follows that

$$
K _ {f} - K _ {i} = W\tag{5.8b}
$$

Thus, the WE theorem is proved for a variable force.

While the WE theorem is useful in a variety of problems, it does not, in general, incorporate the complete dynamical information of Newton's second law. It is an integral form of Newton's second law. Newton's second law is a relation between acceleration and force at any instant of time. Work-energy theorem involves an integral over an interval of time. In this sense, the temporal (time) information contained in the statement of Newton's second law is ‘integrated over’ and is

Reprint 2025-26

<!-- page 7 of 21 -->

WORK, ENERGY AND POWER

77

not available explicitly. Another observation is that Newton's second law for two or three dimensions is in vector form whereas the work-energy theorem is in scalar form. In the scalar form, information with respect to directions contained in Newton's second law is not present.

<div class="docvortex-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Example 5.6 A block of mass $m = 1$ kg, moving on a horizontal surface with speed $v_{i} = 2$ m s$^{-1}$ enters a rough patch ranging from $x = 0.10$ m to $x = 2.01$ m. The retarding force $F_{r}$ on the block in this range is inversely proportional to $x$ over this range, $F_{r} = \frac{-k}{x}$ for $0.1 &lt; x &lt; 2.01$ m = 0 for $x &lt; 0.1$ m and $x &gt; 2.01$ m where $k = 0.5$ J. What is the final kinetic energy and speed $v_{f}$ of the block as it crosses this patch?
</div>

## Answer From Eq. (5.8a)

$$
\begin{array}{l} K _ {f} = K _ {i} + \int_ {0. 1} ^ {2. 0 1} \frac {(- k)}{x} \mathrm{d} x \\ = \frac {1}{2} m v _ {i} ^ {2} - k \ln (x) \Big | _ {0. 1} ^ {2. 0 1} \\ = \frac {1}{2} m v _ {i} ^ {2} - k \ln (2. 0 1 / 0. 1) \\ = 2 - 0. 5 \ln (2 0. 1) \\ = 2 - 1. 5 = 0. 5 \mathrm{J} \\ v _ {f} = \sqrt {2 K _ {f} / m} = 1 \mathrm{ms} ^ {- 1} \end{array}
$$

Here, note that $\ln$ is a symbol for the natural logarithm to the base $e$ and not the logarithm to the base 10 [ln X = log$_{e}$ X = 2.303 log$_{10}$ X].

## 5.7 THE CONCEPT OF POTENTIAL ENERGY

The word potential suggests possibility or capacity for action. The term potential energy brings to one's mind 'stored' energy. A stretched bow-string possesses potential energy. When it is released, the arrow flies off at a great speed. The earth's crust is not uniform, but has discontinuities and dislocations that are called fault lines. These fault lines in the earth's crust

are like ‘compressed springs’. They possess a large amount of potential energy. An earthquake results when these fault lines readjust. Thus, potential energy is the ‘stored energy’ by virtue of the position or configuration of a body. The body left to itself releases this stored energy in the form of kinetic energy. Let us make our notion of potential energy more concrete.

The gravitational force on a ball of mass $m$ is $mg$. $g$ may be treated as a constant near the earth surface. By 'near' we imply that the height $h$ of the ball above the earth's surface is very small compared to the earth's radius $R_E(h << R_E)$ so that we can ignore the variation of $g$ near the earth's surface\*. In what follows we have taken the upward direction to be positive. Let us raise the ball up to a height $h$. The work done by the external agency against the gravitational force is $mgh$. This work gets stored as potential energy. Gravitational potential energy of an object, as a function of the height $h$, is denoted by $V(h)$ and it is the negative of work done by the gravitational force in raising the object to that height.

$$
V (h) = m g h
$$

If $h$ is taken as a variable, it is easily seen that the gravitational force $F$ equals the negative of the derivative of $V(h)$ with respect to $h$. Thus,

$$
F = - \frac {\mathrm{d}}{\mathrm{d} h} V (h) = - m g
$$

The negative sign indicates that the gravitational force is downward. When released, the ball comes down with an increasing speed. Just before it hits the ground, its speed is given by the kinematic relation,

$$
v ^ {2} = 2 g h
$$

This equation can be written as

$$
\frac {1}{2} m v ^ {2} = m g h
$$

which shows that the gravitational potential energy of the object at height h, when the object is released, manifests itself as kinetic energy of the object on reaching the ground.

Physically, the notion of potential energy is applicable only to the class of forces where work done against the force gets ‘stored up’ as energy. When external constraints are removed, it manifests itself as kinetic energy. Mathematically, (for simplicity, in one dimension) the potential

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">\* The variation of $g$ with height is discussed in Chapter 7 on Gravitation.</span></small>

Reprint 2025-26

<!-- page 8 of 21 -->

78

PHYSICS

energy $V(x)$ is defined if the force $F(x)$ can be written as

$$
F (x) = - \frac {\mathrm{d} V}{\mathrm{d} x}
$$

This implies that

$$
\int_ {x _ {i}} ^ {x _ {f}} F (x) \mathrm{d} x = - \int_ {V _ {i}} ^ {V _ {f}} \mathrm{d} V = V _ {i} - V _ {f}
$$

The work done by a conservative force such as gravity depends on the initial and final positions only. In the previous chapter we have worked on examples dealing with inclined planes. If an object of mass m is released from rest, from the top of a smooth (frictionless) inclined plane of height h, its speed at the bottom is  $\sqrt{2gh}$  irrespective of the angle of inclination. Thus, at the bottom of the inclined plane it acquires a kinetic energy, mgh. If the work done or the kinetic energy did depend on other factors such as the velocity or the particular path taken by the object, the force would be called non-conservative.

The dimensions of potential energy are  $[ML^{2}T^{-2}]$  and the unit is joule (J), the same as kinetic energy or work. To reiterate, the change in potential energy, for a conservative force,  $\Delta V$  is equal to the negative of the work done by the force

$$
\Delta V = - F (x) \Delta x\tag{5.9}
$$

In the example of the falling ball considered in this section we saw how potential energy was converted to kinetic energy. This hints at an important principle of conservation in mechanics, which we now proceed to examine.

## 5.8 THE CONSERVATION OF MECHANICAL ENERGY

For simplicity we demonstrate this important principle for one-dimensional motion. Suppose that a body undergoes displacement $\Delta x$ under the action of a conservative force $F$. Then from the WE theorem we have,

$$
\Delta K = F (x) \Delta x
$$

If the force is conservative, the potential energy function $V(x)$ can be defined such that

$$
- \Delta V = F (x) \Delta x
$$

The above equations imply that

$$
\begin{array}{l} \Delta K + \Delta V = 0 \\ \Delta (K + V) = 0 \end{array}\tag{5.10}
$$

which means that $K + V$, the sum of the kinetic and potential energies of the body is a constant. Over the whole path, $x_{i}$ to $x_{j}$, this means that

$$
K _ {i} + V (x _ {i}) = K _ {f} + V (x _ {f})\tag{5.11}
$$

The quantity  $K + V(x)$ , is called the total mechanical energy of the system. Individually the kinetic energy K and the potential energy  $V(x)$  may vary from point to point, but the sum is a constant. The aptness of the term ‘conservative force’ is now clear.

Let us consider some of the definitions of a conservative force.

\- A force $F(x)$ is conservative if it can be derived from a scalar quantity $V(x)$ by the relation given by Eq. (5.9). The three-dimensional generalisation requires the use of a vector derivative, which is outside the scope of this book.

\- The work done by the conservative force depends only on the end points. This can be seen from the relation,

$$
W = K _ {f} - K _ {i} = V \left(x _ {i}\right) - V (x _ {f})
$$

which depends on the end points.

\- A third definition states that the work done by this force in a closed path is zero. This is once again apparent from Eq. (5.11) since $x_{i} = x_{f}$.

Thus, the principle of conservation of total mechanical energy can be stated as

The total mechanical energy of a system is conserved if the forces, doing work on it, are conservative.

The above discussion can be made more concrete by considering the example of the gravitational force once again and that of the spring force in the next section. Fig. 5.5 depicts a ball of mass m being dropped from a cliff of height H.

$$
\begin{array}{c} x \\ \hline \end{array} \begin{array}{c} \bullet \\ \downarrow \\ \nu = v _ {h} \\ h \\ \nu = v _ {f} \end{array} \begin{array}{c} \overline {{H}} \\ \hline \end{array}
$$

Fig. 5.5 The conversion of potential energy to kinetic energy for a ball of mass m dropped from a height H.

Reprint 2025-26

<!-- page 9 of 21 -->

WORK, ENERGY AND POWER

79

The total mechanical energies  $E_{0}$ ,  $E_{h}$ , and  $E_{H}$  of the ball at the indicated heights zero (ground level), h and H, are

$$
E _ {H} = m g H\tag{5.11 a}
$$

$$
E _ {h} = m g h + \frac {1}{2} m v _ {h} ^ {2}\tag{5.11 b}
$$

$$
E _ {0} = (1 / 2) m v _ {f} ^ {2}\tag{5.11 c}
$$

The constant force is a special case of a spatially dependent force $F(x)$. Hence, the mechanical energy is conserved. Thus

$$
\begin{array}{c} E _ {H} = E _ {0} \\ m g H = \frac {1}{2} m v _ {f} ^ {2} \\ v _ {f} = \sqrt {2 g H} \end{array}\tag{or,}
$$

a result that was obtained in section 5.7 for a freely falling body.

Further,

$$
E _ {H} = E _ {h}
$$

which implies,

$$
v _ {\mathrm{h}} ^ {2} = 2 g (H - h)\tag{5.11 d}
$$

and is a familiar result from kinematics.

At the height $H$, the energy is purely potential. It is partially converted to kinetic at height $h$ and is fully kinetic at ground level. This illustrates the conservation of mechanical energy.

Example 5.7 A bob of mass $m$ is suspended by a light string of length $L$. It is imparted a horizontal velocity $v_{o}$ at the lowest point A such that it completes a semi-circular trajectory in the vertical plane with the string becoming slack only on reaching the topmost point, C. This is shown in Fig. 5.6. Obtain an expression for (i) $v_{o}$; (ii) the speeds at points B and C; (iii) the ratio of the kinetic energies $(K_{B}/K_{C})$ at B and C. Comment on the nature of the trajectory of the bob after it reaches the point C.

![Image block](doc:281a2b5/tier:standard/page:9/block:17)

Fig. 5.6

Answer (i) There are two external forces on the bob : gravity and the tension (T) in the string. The latter does no work since the displacement of the bob is always normal to the string. The potential energy of the bob is thus associated with the gravitational force only. The total mechanical energy E of the system is conserved. We take the potential energy of the system to be zero at the lowest point A. Thus, at A :

$$
E = \frac {1}{2} m v _ {0} ^ {2}\tag{5.12}
$$

$$
T _ {A} - m g = \frac {m v _ {0} ^ {2}}{L} [ \text {Newton's Second Law} ]
$$

where  $T_{A}$  is the tension in the string at A. At the highest point C, the string slackens, as the tension in the string ( $T_{C}$ ) becomes zero.

Thus, at C

$$
E = \frac {1}{2} m v _ {c} ^ {2} + 2 m g L\tag{5.13}
$$

$$
m g = \frac {m v _ {c} ^ {2}}{L} \quad [ \text {Newton's Second Law} ]\tag{5.14}
$$

where $v_{C}$ is the speed at C. From Eqs. (5.13) and (5.14)

$$
E = \frac {5}{2} m g L
$$

Equating this to the energy at A

$$
\left| \begin{array}{l} \frac {5}{2} m g L = \frac {m}{2} v _ {0} ^ {2} \\ v _ {0} = \sqrt {5 g L} \end{array} \right|\tag{or,}
$$

(ii) It is clear from Eq. (5.14)

$$
v _ {C} = \sqrt {g L}
$$

At B, the energy is

$$
E = \frac {1}{2} m v _ {B} ^ {2} + m g L
$$

Equating this to the energy at A and employing the result from (i), namely  $v_{0}^{2}=5gL$ ,

$$
\begin{array}{l} \frac {1}{2} m v _ {B} ^ {2} + m g L = \frac {1}{2} m v _ {0} ^ {2} \\ = \frac {5}{2} m g L \end{array}
$$

Reprint 2025-26

<!-- page 10 of 21 -->

80

PHYSICS

$$
\therefore v _ {B} = \sqrt {3 g L}
$$

(iii) The ratio of the kinetic energies at B and C is :

$$
\frac {K _ {B}}{K _ {C}} = \frac {\frac {1}{2} m v _ {B} ^ {2}}{\frac {1}{2} m v _ {C} ^ {2}} = \frac {3}{1}
$$

At point C, the string becomes slack and the velocity of the bob is horizontal and to the left. If the connecting string is cut at this instant, the bob will execute a projectile motion with horizontal projection akin to a rock kicked horizontally from the edge of a cliff. Otherwise the bob will continue on its circular path and complete the revolution.

## 5.9 THE POTENTIAL ENERGY OF A SPRING

The spring force is an example of a variable force which is conservative. Fig. 5.7 shows a block attached to a spring and resting on a smooth horizontal surface. The other end of the spring is attached to a rigid wall. The spring is light and may be treated as massless. In an ideal spring, the spring force $F_{s}$ is proportional to $x$ where $x$ is the displacement of the block from the equilibrium position. The displacement could be either positive [Fig. 5.7(b)] or negative [Fig. 5.7(c)]. This force law for the spring is called Hooke's law and is mathematically stated as

$$
F _ {s} = - k x
$$

The constant $k$ is called the spring constant. Its unit is $\mathrm{N} \, \mathrm{m}^{-1}$. The spring is said to be stiff if $k$ is large and soft if $k$ is small.

Suppose that we pull the block outwards as in Fig. 5.7(b). If the extension is $x_{m}$, the work done by the spring force is

$$
\begin{array}{r l} W _ {s} = \int_ {0} ^ {x _ {m}} F _ {s} \mathrm{d} x & = - \int_ {0} ^ {x _ {m}} k x \mathrm{d} x \\ = - \frac {k x _ {m} ^ {2}}{2} \end{array}\tag{5.15}
$$

This expression may also be obtained by considering the area of the triangle as in Fig. 5.7(d). Note that the work done by the external pulling force F is positive since it overcomes the spring force.

$$
W = + \frac {k x _ {m} ^ {2}}{2}\tag{5.16}
$$

![Image block](doc:281a2b5/tier:standard/page:10/block:15)

![Image block](doc:281a2b5/tier:standard/page:10/block:16)

Fig. 5.7 Illustration of the spring force with a block attached to the free end of the spring. (a) The spring force $F_s$ is zero when the displacement $x$ from the equilibrium position is zero. (b) For the stretched spring $x > 0$ and $F_s < 0$ (c) For the compressed spring $x < 0$ and $F_s > 0$. (d) The plot of $F_s$ versus $x$. The area of the shaded triangle represents the work done by the spring force. Due to the opposing signs of $F_s$ and $x$, this work done is negative, $W_s = -kx_m^2 / 2$.

The same is true when the spring is compressed with a displacement $x_{c} (< 0)$. The spring force does work $W_{s} = -kx_{c}^{2} / 2$ while the

Reprint 2025-26

<!-- page 11 of 21 -->

WORK, ENERGY AND POWER

81

external force $F$ does work $+\mathrm{kx}_c^2 / 2$. If the block is moved from an initial displacement $x_i$ to a final displacement $x_f$, the work done by the spring force $W_s$ is

$$
W _ {s} = - \int_ {x _ {i}} ^ {x _ {f}} k x \mathrm{d} x \quad = \frac {k x _ {i} ^ {2}}{2} - \frac {k x _ {f} ^ {2}}{2}\tag{5.17}
$$

Thus the work done by the spring force depends only on the end points. Specifically, if the block is pulled from  $x_{i}$  and allowed to return to  $x_{i}$ ;

$$
\begin{array}{r l} W _ {s} = - \int_ {x _ {i}} ^ {x _ {i}} k x \mathrm{d} x & = \frac {k x _ {i} ^ {2}}{2} - \frac {k x _ {i} ^ {2}}{2} \\ = 0 \end{array}\tag{5.18}
$$

The work done by the spring force in a cyclic process is zero. We have explicitly demonstrated that the spring force (i) is position dependent only as first stated by Hooke,  $(F_{s} = -kx)$ ; (ii) does work which only depends on the initial and final positions, e.g. Eq. (5.17). Thus, the spring force is a conservative force.

We define the potential energy  $V(x)$  of the spring to be zero when block and spring system is in the equilibrium position. For an extension (or compression) x the above analysis suggests that

$$
V (x) = \frac {k x ^ {2}}{2}\tag{5.19}
$$

You may easily verify that $-\mathrm{d}V / \mathrm{d}x = -kx$, the spring force. If the block of mass $m$ in Fig. 5.7 is extended to $x_{m}$ and released from rest, then its total mechanical energy at any arbitrary point $x$, where $x$ lies between $-x_{m}$ and $+x_{m}$, will be given by

$$
\frac {1}{2} k x _ {m} ^ {2} = \frac {1}{2} k x ^ {2} + \frac {1}{2} m v ^ {2}
$$

where we have invoked the conservation of mechanical energy. This suggests that the speed and the kinetic energy will be maximum at the equilibrium position, x = 0, i.e.,

$$
\frac {1}{2} m v _ {m} ^ {2} = \frac {1}{2} k x _ {m} ^ {2}
$$

where $v_{m}$ is the maximum speed.

$$
v _ {m} = \sqrt {\frac {k}{m}} x _ {m}\tag{or}
$$

Note that k/m has the dimensions of  $[T^{-2}]$  and our equation is dimensionally correct. The kinetic energy gets converted to potential energy

and vice versa, however, the total mechanical energy remains constant. This is graphically depicted in Fig. 5.8.

![Image block](doc:281a2b5/tier:standard/page:11/block:18)

Fig. 5.8 Parabolic plots of the potential energy V and kinetic energy K of a block attached to a spring obeying Hooke's law. The two plots are complementary, one decreasing as the other increases. The total mechanical energy  $E = K + V$  remains constant.

Example 5.8 To simulate car accidents, auto manufacturers study the collisions of moving cars with mounted springs of different spring constants. Consider a typical simulation with a car of mass 1000 kg moving with a speed 18.0 km/h on a smooth road and colliding with a horizontally mounted spring of spring constant  $5.25 \times 10^{3}$  N m $^{-1}$ . What is the maximum compression of the spring?

Answer At maximum compression the kinetic energy of the car is converted entirely into the potential energy of the spring.

The kinetic energy of the moving car is

$$
\begin{array}{l} K = \frac {1}{2} m v ^ {2} \\ = \frac {1}{2} \times 1 0 ^ {3} \times 5 \times 5 \\ K = 1. 2 5 \times 1 0 ^ {4} \mathrm{J} \end{array}
$$

where we have converted  $18 \, km h^{-1}$  to  $5 \, m s^{-1}$  [It is useful to remember that  $36 \, km h^{-1} = 10 \, m s^{-1}$ ]. At maximum compression  $x_{m}$ , the potential energy V of the spring is equal to the kinetic energy K of the moving car from the principle of conservation of mechanical energy.

$$
V = \frac{1}{2} k x_m^2
$$

Reprint 2025-26

<!-- page 12 of 21 -->

82

PHYSICS

$$
= 1.25 \times 10^4 \text{ J}
$$

We obtain

$$
x _ {m} = 2. 0 0 \mathrm{m}
$$

We note that we have idealised the situation. The spring is considered to be massless. The surface has been considered to possess negligible friction.

We conclude this section by making a few remarks on conservative forces.

(i) Information on time is absent from the above discussions. In the example considered above, we can calculate the compression, but not the time over which the compression occurs. A solution of Newton's Second Law for this system is required for temporal information.

(ii) Not all forces are conservative. Friction, for example, is a non-conservative force. The principle of conservation of energy will have to be modified in this case. This is illustrated in Example 5.9.

(iii) The zero of the potential energy is arbitrary. It is set according to convenience. For the spring force we took $V(x) = 0$, at $x = 0$, i.e. the unstretched spring had zero potential energy. For the constant gravitational force $mg$, we took $V = 0$ on the earth's surface. In a later chapter we shall see that for the force due to the universal law of gravitation, the zero is best defined at an infinite distance from the gravitational source. However, once the zero of the potential energy is fixed in a given discussion, it must be consistently adhered to throughout the discussion. You cannot change horses in midstream!

Example 5.9 Consider Example 5.8 taking the coefficient of friction, $\mu$, to be 0.5 and calculate the maximum compression of the spring.

Answer In presence of friction, both the spring force and the frictional force act so as to oppose the compression of the spring as shown in Fig. 5.9.

We invoke the work-energy theorem, rather than the conservation of mechanical energy.

The change in kinetic energy is

![Image block](doc:281a2b5/tier:standard/page:12/block:15)

Fig. 5.9 The forces acting on the car.

$$
\Delta K = K _ {f} - K _ {i} = 0 - \frac {1}{2} m v ^ {2}
$$

The work done by the net force is

$$
W = - \frac {1}{2} k x _ {m} ^ {2} - \mu m g x _ {m}
$$

Equating we have

$$
\frac {1}{2} m v ^ {2} = \frac {1}{2} k x _ {m} ^ {2} + \mu m g x _ {m}
$$

Now  $\mu mg = 0.5 \times 10^{3} \times 10 = 5 \times 10^{3}$  N (taking  $g = 10.0 \, m s^{-2}$ ). After rearranging the above equation we obtain the following quadratic equation in the unknown  $x_{m}$ .

$$
\begin{array}{c} k x _ {m} ^ {2} + 2 \mu m g x _ {m} - m v ^ {2} = 0 \\ x _ {m} = \frac {- \mu m g + \left[ \mu^ {2} m ^ {2} g ^ {2} + m k v ^ {2} \right] ^ {1 / 2}}{k} \end{array}
$$

where we take the positive square root since $x_{m}$ is positive. Putting in numerical values we obtain

$$
x _ {m} = 1. 3 5 \mathrm{m}
$$

which, as expected, is less than the result in Example 5.8.

If the two forces on the body consist of a conservative force  $F_{c}$  and a non-conservative force  $F_{nc}$ , the conservation of mechanical energy formula will have to be modified. By the WE theorem

But

Hence,

$$
\begin{array}{c} (F _ {c} + F _ {n c}) \Delta x = \Delta K \\ F _ {c} \Delta x = - \Delta V \\ \Delta (K + V) = F _ {n c} \Delta x \\ \Delta E \quad = F _ {n c} \Delta x \end{array}
$$

where $E$ is the total mechanical energy. Over the path this assumes the form

$$
E _ {f} - E _ {i} = W _ {n c}
$$

where $W_{nc}$ is the total work done by the non-conservative forces over the path. Note that

Reprint 2025-26

<!-- page 13 of 21 -->

WORK, ENERGY AND POWER

83

unlike the conservative force,  $W_{nc}$  depends on the particular path i to f.

## 5.10 POWER

Often it is interesting to know not only the work done on an object, but also the rate at which this work is done. We say a person is physically fit if he not only climbs four floors of a building but climbs them fast. Power is defined as the time rate at which work is done or energy is transferred.

The average power of a force is defined as the ratio of the work, $W$, to the total time $t$ taken

$$
P _ {a v} = \frac {W}{t}
$$

The instantaneous power is defined as the limiting value of the average power as time interval approaches zero,

$$
P = \frac {\mathrm{d} W}{\mathrm{d} t}\tag{5.20}
$$

The work $dW$ done by a force F for a displacement $dr$ is $\mathrm{d}W = \mathbf{F}.dr$. The instantaneous power can also be expressed as

$$
\begin{array}{c} P = \mathbf {F}. \frac {\mathrm{d} \boldsymbol {r}}{\mathrm{d} t} \\ = \mathbf {F}. \mathbf {v} \end{array}\tag{5.21}
$$

where v is the instantaneous velocity when the force is F.

Power, like work and energy, is a scalar quantity. Its dimensions are  $[ML^{2}T^{-3}]$ . In the SI, its unit is called a watt (W). The watt is 1 J s $^{-1}$ . The unit of power is named after James Watt, one of the innovators of the steam engine in the eighteenth century.

There is another unit of power, namely the horse-power (hp)

$$
1 \mathrm{hp} = 7 4 6 \mathrm{W}
$$

This unit is still used to describe the output of automobiles, motorbikes, etc.

We encounter the unit watt when we buy electrical goods such as bulbs, heaters and refrigerators. A 100 watt bulb which is on for 10 hours uses 1 kilowatt hour (kWh) of energy.

$$
\begin{array}{r l} & 1 0 0 (\mathrm{watt}) \times 1 0 (\mathrm{hour}) \\ & = 1 0 0 0 \mathrm{watthour} \\ & = 1 \mathrm{kilowatthour(kWh)} \\ & = 1 0 ^ {3} (\mathrm{W}) \times 3 6 0 0 (\mathrm{s}) \\ & = 3. 6 \times 1 0 ^ {6} \mathrm{J} \end{array}
$$

Our electricity bills carry the energy consumption in units of kWh. Note that kWh is a unit of energy and not of power.

Example 5.10 An elevator can carry a maximum load of $1800\mathrm{kg}$ (elevator + passengers) is moving up with a constant speed of $2\mathrm{ms}^{-1}$. The frictional force opposing the motion is $4000\mathrm{N}$. Determine the minimum power delivered by the motor to the elevator in watts as well as in horse power.

Answer The downward force on the elevator is

$$
F = m g + F _ {f} = (1 8 0 0 \times 1 0) + 4 0 0 0 = 2 2 0 0 0 \mathrm{N}
$$

The motor must supply enough power to balance this force. Hence,

$$
P = \mathbf {F}. \mathbf {v} = 2 2 0 0 0 \times 2 = 4 4 0 0 0 \mathrm{W} = 5 9 \mathrm{hp}
$$

## 5.11 COLLISIONS

In physics we study motion (change in position). At the same time, we try to discover physical quantities, which do not change in a physical process. The laws of momentum and energy conservation are typical examples. In this section we shall apply these laws to a commonly encountered phenomena, namely collisions. Several games such as billiards, marbles or carrom involve collisions. We shall study the collision of two masses in an idealised form.

Consider two masses  $m_{1}$  and  $m_{2}$ . The particle  $m_{1}$  is moving with speed  $v_{li}$ , the subscript ‘i’ implying initial. We can cosider  $m_{2}$  to be at rest. No loss of generality is involved in making such a selection. In this situation the mass  $m_{1}$  collides with the stationary mass  $m_{2}$  and this is depicted in Fig. 5.10.

![Image block](doc:281a2b5/tier:standard/page:13/block:28)

Fig. 5.10 Collision of mass $m_1$, with a stationary mass $m_2$.

The masses  $m_{1}$  and  $m_{2}$  fly-off in different directions. We shall see that there are relationships, which connect the masses, the velocities and the angles.

Reprint 2025-26

<!-- page 14 of 21 -->

84

PHYSICS

## 5.11.1 Elastic and Inelastic Collisions

In all collisions the total linear momentum is conserved; the initial momentum of the system is equal to the final momentum of the system. One can argue this as follows. When two objects collide, the mutual impulsive forces acting over the collision time  $\Delta t$  cause a change in their respective momenta :

$$
\begin{array}{c} \Delta \mathbf {p} _ {1} = \mathbf {F} _ {1 2} \Delta t \\ \Delta \mathbf {p} _ {2} = \mathbf {F} _ {2 1} \Delta t \end{array}
$$

where  $F_{12}$  is the force exerted on the first particle by the second particle.  $F_{21}$  is likewise the force exerted on the second particle by the first particle. Now from Newton's third law,  $F_{12} = -F_{21}$ . This implies

$$
\Delta \mathbf{p}_1 + \Delta \mathbf{p}_2 = \mathbf{0}
$$

The above conclusion is true even though the forces vary in a complex fashion during the collision time  $\Delta t$ . Since the third law is true at every instant, the total impulse on the first object is equal and opposite to that on the second.

On the other hand, the total kinetic energy of the system is not necessarily conserved. The impact and deformation during collision may generate heat and sound. Part of the initial kinetic energy is transformed into other forms of energy. A useful way to visualise the deformation during collision is in terms of a 'compressed spring'. If the 'spring' connecting the two masses regains its original shape without loss in energy, then the initial kinetic energy is equal to the final kinetic energy but the kinetic energy during the collision time  $\Delta t$  is not constant. Such a collision is called an elastic collision. On the other hand the deformation may not be relieved and the two bodies could move together after the collision. A collision in which the two particles move together after the collision is called a completely inelastic collision. The intermediate case where the deformation is partly relieved and some of the initial kinetic energy is lost is more common and is appropriately called an inelastic collision.

## 5.11.2 Collisions in One Dimension

Consider first a completely inelastic collision in one dimension. Then, in Fig. 5.10,

$$
\begin{array}{l} \theta_ {1} = \theta_ {2} = 0 \\ m _ {1} v _ {1 i} = (m _ {1} + m _ {2}) v _ {f} \text {(momentum conservation)} \end{array}
$$

$$
v _ {f} = \frac {m _ {1}}{m _ {1} + m _ {2}} v _ {1 i}\tag{5.22}
$$

The loss in kinetic energy on collision is

$$
\begin{array}{r l} \Delta K & = \frac {1}{2} m _ {1} v _ {1 i} ^ {2} - \frac {1}{2} (m _ {1} + m _ {2}) v _ {f} ^ {2} \\ & = \frac {1}{2} m _ {1} v _ {1 i} ^ {2} - \frac {1}{2} \frac {m _ {1} ^ {2}}{m _ {1} + m _ {2}} v _ {1 i} ^ {2} \quad \text {[using Eq.} \\ & = \frac {1}{2} m _ {1} v _ {1 i} ^ {2} \left[ 1 - \frac {m _ {1}}{m _ {1} + m _ {2}} \right] \\ & = \frac {1}{2} \frac {m _ {1} m _ {2}}{m _ {1} + m _ {2}} v _ {1 i} ^ {2} \end{array}\tag{5.22)]}
$$

which is a positive quantity as expected.

Consider next an elastic collision. Using the above nomenclature with  $\theta_{1} = \theta_{2} = 0$ , the momentum and kinetic energy conservation equations are

$$
m _ {1} v _ {1 i} = m _ {1} v _ {1 f} + m _ {2} v _ {2 f}\tag{5.23}
$$

$$
m _ {1} v _ {1 i} ^ {2} = m _ {1} v _ {1 f} ^ {2} + m _ {2} v _ {2 f} ^ {2}\tag{5.24}
$$

From Eqs. (5.23) and (5.24) it follows that,

$$
\begin{array}{l} m _ {1} v _ {1 i} (v _ {2 f} - v _ {1 i}) = m _ {1} v _ {1 f} (v _ {2 f} - v _ {1 f}) \\ \text {or,} \quad v _ {2 f} (v _ {1 i} - v _ {1 f}) = v _ {1 i} ^ {2} - v _ {1 f} ^ {2} \\ \quad = (v _ {1 i} - v _ {1 f}) (v _ {1 i} + v _ {1 f}) \\ \text {Hence,} \quad \therefore v _ {2 f} = v _ {1 i} + v _ {1 f} \end{array}\tag{5.25}
$$

Substituting this in Eq. (5.23), we obtain

$$
\begin{array}{l} v _ {1 f} = \frac {(m _ {1} - m _ {2})}{m _ {1} + m _ {2}} v _ {1 i} \\ v _ {2 f} = \frac {2 m _ {1} v _ {1 i}}{m _ {1} + m _ {2}} \end{array}\tag{5.26}
$$

and

(5.27)

Thus, the ‘unknowns’  $\{v_{1f}, v_{2f}\}$  are obtained in terms of the ‘knowns’  $\{m_{1}, m_{2}, v_{1i}\}$ . Special cases of our analysis are interesting.

Case I : If the two masses are equal

$$
\begin{array}{l} V _ {1 f} = 0 \\ V _ {2 f} = V _ {1 i} \end{array}
$$

The first mass comes to rest and pushes off the second mass with its initial speed on collision.

Case II : If one mass dominates, e.g. $m_{2} >> m_{1}$

$$
V _ {1 f} \simeq - V _ {1 i} \quad V _ {2 f} \simeq 0
$$

The heavier mass is undisturbed while the lighter mass reverses its velocity.

Reprint 2025-26

<!-- page 15 of 21 -->

WORK, ENERGY AND POWER

85

Example 5.11 Slowing down of neutrons: In a nuclear reactor a neutron of high speed (typically $10^{7}\mathrm{ms}^{-1}$) must be slowed to $10^{3}\mathrm{ms}^{-1}$ so that it can have a high probability of interacting with isotope ${}_{92}^{235}\mathrm{U}$ and causing it to fission. Show that a neutron can lose most of its kinetic energy in an elastic collision with a light nuclei like deuterium or carbon which has a mass of only a few times the neutron mass. The material making up the light nuclei, usually heavy water $(\mathrm{D}_2\mathrm{O})$ or graphite, is called a moderator.

Answer The initial kinetic energy of the neutron is

$$
K _ {1 i} = \frac {1}{2} m _ {1} v _ {1 i} ^ {2}
$$

while its final kinetic energy from Eq. (5.26)

$$
K _ {1 f} = \frac {1}{2} m _ {1} v _ {1 f} ^ {2} = \frac {1}{2} m _ {1} \left(\frac {m _ {1} - m _ {2}}{m _ {1} + m _ {2}}\right) ^ {2} v _ {1 i} ^ {2}
$$

The fractional kinetic energy lost is

$$
f _ {1} = \frac {K _ {1 f}}{K _ {1 i}} = \left(\frac {m _ {1} - m _ {2}}{m _ {1} + m _ {2}}\right) ^ {2}
$$

while the fractional kinetic energy gained by the moderating nuclei  $K_{2f}/K_{1i}$  is

$$
\begin{array}{r l} f _ {2} & = 1 - f _ {1} \text {(elastic collision)} \\ & = \frac {4 m _ {1} m _ {2}}{\left(m _ {1} + m _ {2}\right) ^ {2}} \end{array}
$$

One can also verify this result by substituting from Eq. (5.27).

For deuterium $m_2 = 2m_1$ and we obtain $f_1 = 1/9$ while $f_2 = 8/9$. Almost $90\%$ of the neutron's energy is transferred to deuterium. For carbon $f_1 = 71.6\%$ and $f_2 = 28.4\%$. In practice, however, this number is smaller since head-on collisions are rare.

If the initial velocities and final velocities of both the bodies are along the same straight line, then it is called a one-dimensional collision, or head-on collision. In the case of small spherical bodies, this is possible if the direction of travel of body 1 passes through the centre of body 2 which is at rest. In general, the collision is two-

dimensional, where the initial velocities and the final velocities lie in a plane.

## 5.11.3 Collisions in Two Dimensions

Fig. 5.10 also depicts the collision of a moving mass $m_1$ with the stationary mass $m_2$. Linear momentum is conserved in such a collision. Since momentum is a vector this implies three equations for the three directions $\{x, y, z\}$. Consider the plane determined by the final velocity directions of $m_1$ and $m_2$ and choose it to be the $x-y$ plane. The conservation of the $z$-component of the linear momentum implies that the entire collision is in the $x-y$ plane. The $x-$ and $y$-component equations are

$$
m _ {1} v _ {1 i} = m _ {1} v _ {1 f} \cos \theta_ {1} + m _ {2} v _ {2 f} \cos \theta_ {2}\tag{5.28}
$$

$$
0 = m _ {1} v _ {1 f} \sin \theta_ {1} - m _ {2} v _ {2 f} \sin \theta_ {2}\tag{5.29}
$$

One knows  $\{m_{1}, m_{2}, v_{1f}\}$  in most situations. There are thus four unknowns  $\{v_{1f}, v_{2f}, \theta_{1} and \theta_{2}\}$ , and only two equations. If  $\theta_{1} = \theta_{2} = 0$ , we regain Eq. (5.23) for one dimensional collision.

If, further the collision is elastic,

$$
\frac {1}{2} m _ {1} v _ {1 i} ^ {2} = \frac {1}{2} m _ {1} v _ {1 f} ^ {2} + \frac {1}{2} m _ {2} v _ {2 f} ^ {2}\tag{5.30}
$$

We obtain an additional equation. That still leaves us one equation short. At least one of the four unknowns, say $\theta_{1}$, must be made known for the problem to be solvable. For example, $\theta_{1}$ can be determined by moving a detector in an angular fashion from the $x$ to the $y$ axis. Given $\{m_1, m_2, v_{lj}, \theta_1\}$ we can determine $\{v_{1f}, v_{2f}, \theta_2\}$ from Eqs. (5.28)-(5.30).

Example 5.12 Consider the collision depicted in Fig. 5.10 to be between two billiard balls with equal masses $m_1 = m_2$. The first ball is called the cue while the second ball is called the target. The billiard player wants to 'sink' the target ball in a corner pocket, which is at an angle $\theta_2 = 37$. Assume that the collision is elastic and that friction and rotational motion are not important. Obtain $\theta_1$.

Answer From momentum conservation, since the masses are equal

or

$$
\begin{array}{l} \mathbf {v} _ {1 \mathrm{i}} = \mathbf {v} _ {1 \mathrm{f}} + \mathbf {v} _ {2 \mathrm{f}} \\ v _ {1 i} ^ {2} = \left(\mathbf {v} _ {1 f} + \mathbf {v} _ {2 f}\right) \cdot \left(\mathbf {v} _ {1 f} + \mathbf {v} _ {2 f}\right) \\ = v _ {1 f} ^ {2} + v _ {2 f} ^ {2} + 2 \mathbf {v} _ {1 f}. \mathbf {v} _ {2 f} \end{array}
$$

Reprint 2025-26

<!-- page 16 of 21 -->

86

PHYSICS

$$
= \left\{v _ {1 f} ^ {2} + v _ {2 f} ^ {2} + 2 v _ {1 f} v _ {2 f} \cos \left(\theta_ {1} + 3 7 ^ {\circ}\right) \right\}\tag{5.31}
$$

Since the collision is elastic and  $m_{1}=m_{2}$  it follows from conservation of kinetic energy that

$$
v _ {1 i} ^ {2} = v _ {1 f} ^ {2} + v _ {2 f} ^ {2}\tag{5.32}
$$

Comparing Eqs. (5.31) and (5.32), we get

$$
\cos \left(\theta_ {1} + 3 7 ^ {\circ}\right) = 0\tag{or}
$$

$$
\theta_ {1} + 3 7 ^ {\circ} = 9 0 ^ {\circ}
$$

Thus, $\theta_{1} = 53^{\circ}$

This proves the following result: when two equal masses undergo a glancing elastic collision with one of them at rest, after the collision, they will move at right angles to each other.

The matter simplifies greatly if we consider spherical masses with smooth surfaces, and assume that collision takes place only when the bodies touch each other. This is what happens in the games of marbles, carrom and billiards.

In our everyday world, collisions take place only when two bodies touch each other. But consider a comet coming from far distances to the sun, or alpha particle coming towards a nucleus and going away in some direction. Here we have to deal with forces involving action at a distance. Such an event is called scattering. The velocities and directions in which the two particles go away depend on their initial velocities as well as the type of interaction between them, their masses, shapes and sizes.

## SUMMARY

1. The work-energy theorem states that the change in kinetic energy of a body is the work done by the net force on the body.

$$
K _ {f} - K _ {i} = W _ {\text {net}}
$$

2. A force is conservative if (i) work done by it on an object is path independent and depends only on the end points $\{x_i, x_j\}$, or (ii) the work done by the force is zero for an arbitrary closed path taken by the object such that it returns to its initial position.

3. For a conservative force in one dimension, we may define a potential energy function $V(x)$ such that

$$
F (x) = - \frac {\mathrm{d} V (x)}{\mathrm{d} x}
$$

or

$$
V _ {i} - V _ {f} = \int_ {x _ {i}} ^ {x _ {f}} F (x) \mathrm{d} x
$$

4. The principle of conservation of mechanical energy states that the total mechanical energy of a body remains constant if the only forces that act on the body are conservative.

5. The gravitational potential energy of a particle of mass $m$ at a height $x$ about the earth's surface is

$$
V (x) = m g x
$$

where the variation of $g$ with height is ignored.

5. The elastic potential energy of a spring of force constant $k$ and extension $x$ is

$$
V (x) = \frac {1}{2} k x ^ {2}
$$

7. The scalar or dot product of two vectors A and B is written as A.B and is a scalar quantity given by :A·B = AB cos θ, where θ is the angle between A and B. It can be positive, negative or zero depending upon the value of θ. The scalar product of two vectors can be interpreted as the product of magnitude of one vector and component of the other vector along the first vector. For unit vectors :

$$
\hat {\mathbf {i}} \cdot \hat {\mathbf {i}} = \hat {\mathbf {j}} \cdot \hat {\mathbf {j}} = \hat {\mathbf {k}} \cdot \hat {\mathbf {k}} = 1 \text {and} \hat {\mathbf {i}} \cdot \hat {\mathbf {j}} = \hat {\mathbf {j}} \cdot \hat {\mathbf {k}} = \hat {\mathbf {k}} \cdot \hat {\mathbf {i}} = 0
$$

Scalar products obey the commutative and the distributive laws.

Reprint 2025-26

<!-- page 17 of 21 -->

WORK, ENERGY AND POWER

87

| Physical Quantity | Symbol | Dimensions | Units | Remarks |
| --- | --- | --- | --- | --- |
| Work | $W$ | $[ML^{2}T^{-2}]$ | J | $W = \mathbf{F.d}$ |
| Kinetic energy | $K$ | $[ML^{2}T^{-2}]$ | J | $K = \frac{1}{2}mv^{2}$ |
| Potential energy | $V(x)$ | $[ML^{2}T^{-2}]$ | J | $F(x) = -\frac{\mathrm{d}V(x)}{\mathrm{d}x}$ |
| Mechanical energy | $E$ | $[ML^{2}T^{-2}]$ | J | $E = K + V$ |
| Spring constant | $k$ | $[MT^{-2}]$ | $N\ m^{-1}$ | $F = -kx$$V(x) = \frac{1}{2}kx^{2}$ |
| Power | $P$ | $[ML^{2}T^{-3}]$ | W | $P = \mathbf{F.v}$$P = \frac{\mathrm{d}W}{\mathrm{d}t}$ |

## POINTS TO PONDER

1. The phrase ‘calculate the work done’ is incomplete. We should refer (or imply clearly by context) to the work done by a specific force or a group of forces on a given body over a certain displacement.

2. Work done is a scalar quantity. It can be positive or negative unlike mass and kinetic energy which are positive scalar quantities. The work done by the friction or viscous force on a moving body is negative.

3. For two bodies, the sum of the mutual forces exerted between them is zero from Newton's Third Law,

$$
\mathbf {F} _ {1 2} + \mathbf {F} _ {2 1} = 0
$$

But the sum of the work done by the two forces need not always cancel, i.e.

$$
W _ {1 2} + W _ {2 1} \neq 0
$$

However, it may sometimes be true.

4. The work done by a force can be calculated sometimes even if the exact nature of the force is not known. This is clear from Example 5.2 where the WE theorem is used in such a situation.

5. The WE theorem is not independent of Newton's Second Law. The WE theorem may be viewed as a scalar form of the Second Law. The principle of conservation of mechanical energy may be viewed as a consequence of the WE theorem for conservative forces.

5. The WE theorem holds in all inertial frames. It can also be extended to non-inertial frames provided we include the pseudoforces in the calculation of the net force acting on the body under consideration.

7. The potential energy of a body subjected to a conservative force is always undetermined up to a constant. For example, the point where the potential energy is zero is a matter of choice. For the gravitational potential energy $mgh$, the zero of the potential energy is chosen to be the ground. For the spring potential energy $kx^2 / 2$, the zero of the potential energy is the equilibrium position of the oscillating mass.

8. Every force encountered in mechanics does not have an associated potential energy. For example, work done by friction over a closed path is not zero and no potential energy can be associated with friction.

9. During a collision : (a) the total linear momentum is conserved at each instant of the collision ; (b) the kinetic energy conservation (even if the collision is elastic) applies after the collision is over and does not hold at every instant of the collision. In fact the two colliding objects are deformed and may be momentarily at rest with respect to each other.

Reprint 2025-26

<!-- page 18 of 21 -->

88

PHYSICS

## EXERCISES

5.1 The sign of work done by a force on a body is important to understand. State carefully if the following quantities are positive or negative:

(a) work done by a man in lifting a bucket out of a well by means of a rope tied to the bucket.

(b) work done by gravitational force in the above case,

(c) work done by friction on a body sliding down an inclined plane,

(d) work done by an applied force on a body moving on a rough horizontal plane with uniform velocity,

(e) work done by the resistive force of air on a vibrating pendulum in bringing it to rest.

5.2 A body of mass 2 kg initially at rest moves under the action of an applied horizontal force of 7 N on a table with coefficient of kinetic friction = 0.1. Compute the

![Image block](doc:281a2b5/tier:standard/page:18/block:11)

(a) work done by the applied force in $10\mathrm{s}$,

(b) work done by friction in $10\mathrm{s}$,

(c) work done by the net force on the body in 10 s,

(d) change in kinetic energy of the body in 10 s,

![Image block](doc:281a2b5/tier:standard/page:18/block:16)

and interpret your results.

5.3 Given in Fig. 5.11 are examples of some potential energy functions in one dimension. The total energy of the particle is indicated by a cross on the ordinate axis. In each case, specify the regions, if any, in which the particle cannot be found for the given energy. Also, indicate the minimum total energy the particle must have in each case. Think of simple physical contexts for which these potential energy shapes are relevant.

![Image block](doc:281a2b5/tier:standard/page:18/block:19)

![Image block](doc:281a2b5/tier:standard/page:18/block:20)

Fig. 5.11

Reprint 2025-26

<!-- page 19 of 21 -->

WORK, ENERGY AND POWER

89

5.4 The potential energy function for a particle executing linear simple harmonic motion is given by  $V(x) = kx^{2}/2$ , where k is the force constant of the oscillator. For  $k = 0.5 N m^{-1}$ , the graph of  $V(x)$  versus x is shown in Fig. 5.12. Show that a particle of total energy 1 J moving under this potential must ‘turn back’ when it reaches  $x = \pm 2 m$ .

![Image block](doc:281a2b5/tier:standard/page:19/block:4)

## 5.5 Answer the following :

(a) The casing of a rocket in flight burns up due to friction. At whose expense is the heat energy required for burning obtained? The rocket or the atmosphere?

(b) Comets move around the sun in highly elliptical orbits. The gravitational force on the comet due to the sun is not normal to the comet's velocity

![Image block](doc:281a2b5/tier:standard/page:19/block:8)

(i)

![Image block](doc:281a2b5/tier:standard/page:19/block:10)

![Image block](doc:281a2b5/tier:standard/page:19/block:11)

Fig. 5.13

(ii)

in general. Yet the work done by the gravitational force over every complete orbit of the comet is zero. Why?

(c) An artificial satellite orbiting the earth in very thin atmosphere loses its energy gradually due to dissipation against atmospheric resistance, however small. Why then does its speed increase progressively as it comes closer and closer to the earth?

(d) In Fig. 5.13(i) the man walks $2\mathrm{m}$ carrying a mass of $15\mathrm{kg}$ on his hands. In Fig. 5.13(ii), he walks the same distance pulling the rope behind him. The rope goes over a pulley, and a mass of $15\mathrm{kg}$ hangs at its other end. In which case is the work done greater?

## 5.6 Underline the correct alternative :

(a) When a conservative force does positive work on a body, the potential energy of the body increases/decreases/remains unaltered.

(b) Work done by a body against friction always results in a loss of its kinetic/potential energy.

(c) The rate of change of total momentum of a many-particle system is proportional to the external force/sum of the internal forces on the system.

(d) In an inelastic collision of two bodies, the quantities which do not change after the collision are the total kinetic energy/total linear momentum/total energy of the system of two bodies.

## 5.7 State if each of the following statements is true or false. Give reasons for your answer.

(a) In an elastic collision of two bodies, the momentum and energy of each body is conserved.

(b) Total energy of a system is always conserved, no matter what internal and external forces on the body are present.

(c) Work done in the motion of a body over a closed loop is zero for every force in nature.

(d) In an inelastic collision, the final kinetic energy is always less than the initial kinetic energy of the system.

## 5.8 Answer carefully, with reasons :

(a) In an elastic collision of two billiard balls, is the total kinetic energy conserved during the short time of collision of the balls (i.e. when they are in contact)?

(b) Is the total linear momentum conserved during the short time of an elastic collision of two balls?

Reprint 2025-26

<!-- page 20 of 21 -->

90

PHYSICS

(c) What are the answers to (a) and (b) for an inelastic collision?

(d) If the potential energy of two billiard balls depends only on the separation distance between their centres, is the collision elastic or inelastic? (Note, we are talking here of potential energy corresponding to the force during collision, not gravitational potential energy).

5.9 A body is initially at rest. It undergoes one-dimensional motion with constant acceleration. The power delivered to it at time $t$ is proportional to (i) $t^{1/2}$ (ii) $t$ (iii) $t^{3/2}$ (iv) $t^2$

5.10 A body is moving unidirectionally under the influence of a source of constant power. Its displacement in time $t$ is proportional to (i) $t^{1/2}$ (ii) $t$ (iii) $t^{3/2}$ (iv) $t^2$

5.11 A body constrained to move along the z-axis of a coordinate system is subject to a constant force $\mathbf{F}$ given by

$$
\mathbf {F} = \hat {\mathbf {i}} + 2 \hat {\mathbf {j}} + 3 \hat {\mathbf {k}} \mathbf {N}
$$

where  $\hat{i},\hat{j},\hat{k}$  are unit vectors along the x-, y- and z-axis of the system respectively. What is the work done by this force in moving the body a distance of 4 m along the z-axis?

5.12 An electron and a proton are detected in a cosmic ray experiment, the first with kinetic energy 10 keV, and the second with 100 keV. Which is faster, the electron or the proton? Obtain the ratio of their speeds. (electron mass =  $9.11 \times 10^{-31}$  kg, proton mass =  $1.67 \times 10^{-27}$  kg,  $1 \, eV = 1.60 \times 10^{-19} \, J$ ).

5.13 A rain drop of radius 2 mm falls from a height of 500 m above the ground. It falls with decreasing acceleration (due to viscous resistance of the air) until at half its original height, it attains its maximum (terminal) speed, and moves with uniform speed thereafter. What is the work done by the gravitational force on the drop in the first and second half of its journey? What is the work done by the resistive force in the entire journey if its speed on reaching the ground is 10 m s $^{-1}$ ?

5.14 A molecule in a gas container hits a horizontal wall with speed  $200 \, m s^{-1}$  and angle  $30^{\circ}$  with the normal, and rebounds with the same speed. Is momentum conserved in the collision? Is the collision elastic or inelastic?

5.15 A pump on the ground floor of a building can pump up water to fill a tank of volume  $30 \, m^{3}$  in 15 min. If the tank is 40 m above the ground, and the efficiency of the pump is 30%, how much electric power is consumed by the pump?

5.16 Two identical ball bearings in contact with each other and resting on a frictionless table are hit head-on by another ball bearing of the same mass moving initially with a speed V. If the collision is elastic, which of the following (Fig. 5.14) is a possible result after collision?

![Image block](doc:281a2b5/tier:standard/page:20/block:15)

Fig. 5.14

(i)

(ii)

(iii)

Reprint 2025-26

<!-- page 21 of 21 -->

![Image block](doc:281a2b5/tier:standard/page:21/block:1)

WORK, ENERGY AND POWER

91

5.17 The bob A of a pendulum released from  $30^{\circ}$  to the vertical hits another bob B of the same mass at rest on a table as shown in Fig. 5.15. How high does the bob A rise after the collision? Neglect the size of the bobs and assume the collision to be elastic.

5.18 The bob of a pendulum is released from a horizontal position. If the length of the pendulum is 1.5 m, what is the speed with which the bob arrives at the lowermost point, given that it dissipated 5% of its initial energy against air resistance?

5.19 A trolley of mass 300 kg carrying a sandbag of 25 kg is moving uniformly with a speed of 27 km/h on a frictionless track. After a while, sand starts leaking out of a hole on the floor of the trolley at the rate of

![Image block](doc:281a2b5/tier:standard/page:21/block:7)

Fig. 5.15

0.05 kg s $^{-1}$ . What is the speed of the trolley after the entire sand bag is empty?

5.20 A body of mass 0.5 kg travels in a straight line with velocity $v = a x^{3/2}$ where $a = 5 \, \text{m}^{-1/2} \, \text{s}^{-1}$. What is the work done by the net force during its displacement from $x = 0$ to $x = 2 \, \text{m}$?

5.21 The blades of a windmill sweep out a circle of area $A$. (a) If the wind flows at a velocity $v$ perpendicular to the circle, what is the mass of the air passing through it in time $t$? (b) What is the kinetic energy of the air? (c) Assume that the windmill converts $25\%$ of the wind's energy into electrical energy, and that $A = 30~\mathrm{m}^2$, $v = 36~\mathrm{km / h}$ and the density of air is $1.2\mathrm{kg}\mathrm{m}^{-3}$. What is the electrical power produced?

5.22 A person trying to lose weight (dieter) lifts a 10 kg mass, one thousand times, to a height of 0.5 m each time. Assume that the potential energy lost each time she lowers the mass is dissipated. (a) How much work does she do against the gravitational force? (b) Fat supplies  $3.8 \times 10^{7}$ J of energy per kilogram which is converted to mechanical energy with a 20% efficiency rate. How much fat will the dieter use up?

5.23 A family uses 8 kW of power. (a) Direct solar energy is incident on the horizontal surface at an average rate of 200 W per square meter. If 20% of this energy can be converted to useful electrical energy, how large an area is needed to supply 8 kW? (b) Compare this area to that of the roof of a typical house.

Reprint 2025-26