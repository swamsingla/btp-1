<!-- page 1 of 35 -->

CHAPTER SIX

11086CH07

# SYSTEMS OF PARTICLES AND ROTATIONAL MOTION

6.1 Introduction

6.2 Centre of mass

6.3 Motion of centre of mass

6.4 Linear momentum of a system of particles

6.5 Vector product of two vectors

6.6 Angular velocity and its relation with linear velocity

6.7 Torque and angular momentum

6.8 Equilibrium of a rigid body

6.9 Moment of inertia

6.10 Kinematics of rotational motion about a fixed axis

6.11 Dynamics of rotational motion about a fixed axis

6.12 Angular momentum in case of rotation about a fixed axis

Summary Points to Ponder Exercises

## 6.1 INTRODUCTION

In the earlier chapters we primarily considered the motion of a single particle. (A particle is ideally represented as a point mass having no size.) We applied the results of our study even to the motion of bodies of finite size, assuming that motion of such bodies can be described in terms of the motion of a particle.

Any real body which we encounter in daily life has a finite size. In dealing with the motion of extended bodies (bodies of finite size) often the idealised model of a particle is inadequate. In this chapter we shall try to go beyond this inadequacy. We shall attempt to build an understanding of the motion of extended bodies. An extended body, in the first place, is a system of particles. We shall begin with the consideration of motion of the system as a whole. The centre of mass of a system of particles will be a key concept here. We shall discuss the motion of the centre of mass of a system of particles and usefulness of this concept in understanding the motion of extended bodies.

A large class of problems with extended bodies can be solved by considering them to be rigid bodies. Ideally a rigid body is a body with a perfectly definite and unchanging shape. The distances between all pairs of particles of such a body do not change. It is evident from this definition of a rigid body that no real body is truly rigid, since real bodies deform under the influence of forces. But in many situations the deformations are negligible. In a number of situations involving bodies such as wheels, tops, steel beams, molecules and planets on the other hand, we can ignore that they warp (twist out of shape), bend or vibrate and treat them as rigid.

## 6.1.1 What kind of motion can a rigid body have?

Let us try to explore this question by taking some examples of the motion of rigid bodies. Let us begin with a rectangular

Reprint 2025-26

<!-- page 2 of 35 -->

SYSTEMS OF PARTICLES AND ROTATIONAL MOTION

93

![Image block](doc:bba3640/tier:standard/page:2/block:3)

Fig 6.1 Translational (sliding) motion of a block down an inclined plane.

$$
P _ {2}
$$

$$
\left| P _ {l} \right|
$$

block sliding down an inclined plane without any sidewise movement. The block is taken as a rigid body. Its motion down the plane is such that all the particles of the body are moving together, i.e. they have the same velocity at any instant of time. The rigid body here is in pure translational motion (Fig. 6.1).

In pure translational motion at any instant of time, all particles of the body have the same velocity.

Consider now the rolling motion of a solid metallic or wooden cylinder down the same inclined plane (Fig. 6.2). The rigid body in this problem, namely the cylinder, shifts from the top to the bottom of the inclined plane, and thus, seems to have translational motion. But as Fig. 6.2 shows, all its particles are not moving with the same velocity at any instant. The body, therefore, is not in pure translational motion. Its motion is translational plus ‘something else.’

![Image block](doc:bba3640/tier:standard/page:2/block:10)

Fig. 6.2 Rolling motion of a cylinder. It is not pure translational motion. Points  $P_{1}$ ,  $P_{2}$ ,  $P_{3}$  and  $P_{4}$  have different velocities (shown by arrows) at any instant of time. In fact, the velocity of the point of contact  $P_{3}$  is zero at any instant, if the cylinder rolls without slipping.

In order to understand what this ‘something else’ is, let us take a rigid body so constrained that it cannot have translational motion. The

most common way to constrain a rigid body so that it does not have translational motion is to fix it along a straight line. The only possible motion of such a rigid body is rotation. The line or fixed axis about which the body is rotating is its axis of rotation. If you look around, you will come across many examples of rotation about an axis, a ceiling fan, a potter's wheel, a giant wheel in a fair, a merry-go-round and so on (Fig 6.3(a) and (b)).

![Image block](doc:bba3640/tier:standard/page:2/block:14)

Fig. 6.3 Rotation about a fixed axis (a) A ceiling fan (b) A potter's wheel.

Let us try to understand what rotation is, what characterises rotation. You may notice that in rotation of a rigid body about a fixed axis,

Reprint 2025-26

<!-- page 3 of 35 -->

94

PHYSICS

![Image block](doc:bba3640/tier:standard/page:3/block:3)

Fig. 6.4 A rigid body rotation about the z-axis (Each point of the body such as $P_{1}$ or $P_{2}$ describes a circle with its centre ($C_{1}$ or $C_{2}$) on the axis of rotation. The radius of the circle ($r_{1}$ or $r_{2}$) is the perpendicular distance of the point ($P_{1}$ or $P_{2}$) from the axis. A point on the axis like $P_{3}$ remains stationary).

every particle of the body moves in a circle, which lies in a plane perpendicular to the axis and has its centre on the axis. Fig. 6.4 shows the rotational motion of a rigid body about a fixed axis (the z-axis of the frame of reference). Let  $P_{1}$  be a particle of the rigid body, arbitrarily chosen and at a distance  $r_{1}$  from fixed axis. The particle  $P_{1}$  describes a circle of radius  $r_{1}$  with its centre  $C_{1}$  on the fixed axis. The circle lies in a plane perpendicular to the axis. The figure also shows another particle  $P_{2}$  of the rigid body,  $P_{2}$  is at a distance  $r_{2}$  from the fixed axis. The particle  $P_{2}$  moves in a circle of radius  $r_{2}$  and with centre  $C_{2}$  on the axis. This circle, too, lies in a plane perpendicular to the axis. Note that the circles described by  $P_{1}$  and  $P_{2}$  may lie in different planes; both these planes, however, are perpendicular to the fixed axis. For any particle on the axis like  $P_{3}$, r = 0. Any such particle remains stationary while the body rotates. This is expected since the axis of rotation is fixed.

![Image block](doc:bba3640/tier:standard/page:3/block:6)

Fig. 6.5 (a) A spinning top
(The point of contact of the top with the ground, its tip O, is fixed.)
Axis of oscillation

![Image block](doc:bba3640/tier:standard/page:3/block:8)

Fig. 6.5 (b) An oscillating table fan with rotating blades. The pivot of the fan, point O, is fixed. The blades of the fan are under rotational motion, whereas, the axis of rotation of the fan blades is oscillating.

In some examples of rotation, however, the axis may not be fixed. A prominent example of this kind of rotation is a top spinning in place [Fig. 6.5(a)]. (We assume that the top does not slip from place to place and so does not have translational motion.) We know from experience that the axis of such a spinning top moves around the vertical through its point of contact with the ground, sweeping out a cone as shown in Fig. 6.5(a). (This movement of the axis of the top around the vertical is termed precession.) Note, the point of contact of the top with ground is fixed. The axis of rotation of the top at any instant passes through the point of contact. Another simple example of this kind of rotation is the oscillating table fan or a pedestal fan [Fig.6.5(b)]. You may have observed that the

Reprint 2025-26

<!-- page 4 of 35 -->

SYSTEMS OF PARTICLES AND ROTATIONAL MOTION

95

axis of rotation of such a fan has an oscillating (sidewise) movement in a horizontal plane about the vertical through the point at which the axis is pivoted (point O in Fig. 6.5(b)).

While the fan rotates and its axis moves sidewise, this point is fixed. Thus, in more general cases of rotation, such as the rotation of a top or a pedestal fan, one point and not one line, of the rigid body is fixed. In this case the axis is not fixed, though it always passes through the fixed point. In our study, however, we mostly deal with the simpler and special case of rotation in which one line (i.e. the axis) is fixed.

![Image block](doc:bba3640/tier:standard/page:4/block:5)

Fig. 6.6(a) Motion of a rigid body which is pure translation.

![Image block](doc:bba3640/tier:standard/page:4/block:7)

Fig. 6.6(b) Motion of a rigid body which is a combination of translation and rotation.

Fig 6.6 (a) and 6.6 (b) illustrate different motions of the same body. Note P is an arbitrary point of the body; O is the centre of mass of the body, which is defined in the next section. Suffice to say here that the trajectories of O are the translational trajectories  $Tr_{1}$  and  $Tr_{2}$  of the body. The positions O and P at three different instants of time are shown by  $O_{1}$ ,  $O_{2}$ , and  $O_{3}$ , and  $P_{1}$ ,  $P_{2}$  and  $P_{3}$ , respectively, in both Figs. 6.6 (a) and (b). As seen from Fig. 6.6(a), at any instant the velocities of any particles like O and P of the body are the same in pure translation. Notice, in this case the orientation of OP, i.e. the angle OP makes with a fixed direction, say the horizontal, remains the same, i.e.  $\alpha_{1} = \alpha_{2} = \alpha_{3}$ . Fig. 6.6 (b) illustrates a case of combination of translation and rotation. In this case, at any instants the velocities of O and P differ. Also,  $\alpha_{1}$ ,  $\alpha_{2}$  and  $\alpha_{3}$  may all be different.

Thus, for us rotation will be about a fixed axis only unless stated otherwise.

The rolling motion of a cylinder down an inclined plane is a combination of rotation about a fixed axis and translation. Thus, the 'something else' in the case of rolling motion which we referred to earlier is rotational motion. You will find Fig. 6.6(a) and (b) instructive from this point of view. Both these figures show motion of the same body along identical translational trajectory. In one case, Fig. 6.6(a), the motion is a pure translation; in the other case [Fig. 6.6(b)] it is a combination of translation and rotation. (You may try to reproduce the two types of motion shown, using a rigid object like a heavy book.)

We now recapitulate the most important observations of the present section: The motion of a rigid body which is not pivoted or fixed in some way is either a pure translation or a combination of translation and rotation. The motion of a rigid body which is pivoted or fixed in some way is rotation. The rotation may be about an axis that is fixed (e.g. a ceiling fan) or moving (e.g. an oscillating table fan [Fig.6.5(b)]). We shall, in the present chapter, consider rotational motion about a fixed axis only.

## 6.2 CENTRE OF MASS

We shall first see what the centre of mass of a system of particles is and then discuss its significance. For simplicity we shall start with a two particle system. We shall take the line joining the two particles to be the $x$-axis.

![Image block](doc:bba3640/tier:standard/page:4/block:15)

Fig. 6.7

Let the distances of the two particles be  $x_{1}$  and  $x_{2}$  respectively from some origin O. Let  $m_{1}$  and  $m_{2}$  be respectively the masses of the two

Reprint 2025-26

<!-- page 5 of 35 -->

96

PHYSICS

particles. The centre of mass of the system is that point C which is at a distance X from O, where X is given by

$$
X = \frac {m _ {1} x _ {1} + m _ {2} x _ {2}}{m _ {1} + m _ {2}}\tag{6.1}
$$

In Eq. (6.1), $X$ can be regarded as the mass-weighted mean of $x_{1}$ and $x_{2}$. If the two particles have the same mass $m_{1} = m_{2} = m$, then

$$
X = \frac {m x _ {1} + m x _ {2}}{2 m} = \frac {x _ {1} + x _ {2}}{2}
$$

Thus, for two particles of equal mass the centre of mass lies exactly midway between them.

If we have n particles of masses  $m_{1}$ ,  $m_{2}$ , ... $m_{n}$  respectively, along a straight line taken as the x-axis, then by definition the position of the centre of the mass of the system of particles is given by.

$$
X = \frac {m _ {1} x _ {1} + m _ {2} x _ {2} + \dots + m _ {n} x _ {n}}{m _ {1} + m _ {2} + \dots + m _ {n}} = \frac {\sum_ {i = 1} ^ {n} m _ {i} x _ {i}}{\sum_ {i = 1} ^ {n} m _ {i}} = \frac {\sum_ {i} m _ {i} x _ {i}}{\sum_ {i} m _ {i}}\tag{6.2}
$$

where  $x_{1}, x_{2}, \ldots, x_{n}$  are the distances of the particles from the origin; X is also measured from the same origin. The symbol  $\sum$  (the Greek letter sigma) denotes summation, in this case over n particles. The sum

$$
\sum m _ {i} = M
$$

is the total mass of the system.

Suppose that we have three particles, not lying in a straight line. We may define $x$- and $y$-axes in the plane in which the particles lie and represent the positions of the three particles by coordinates $(x_1, y_1)$, $(x_2, y_2)$ and $(x_3, y_3)$ respectively. Let the masses of the three particles be $m_1$, $m_2$ and $m_3$ respectively. The centre of mass C of the system of the three particles is defined and located by the coordinates $(X, Y)$ given by

$$
X = \frac {m _ {1} x _ {1} + m _ {2} x _ {2} + m _ {3} x _ {3}}{m _ {1} + m _ {2} + m _ {3}}\tag{6.3a}
$$

$$
Y = \frac {m _ {1} y _ {1} + m _ {2} y _ {2} + m _ {3} y _ {3}}{m _ {1} + m _ {2} + m _ {3}}\tag{6.3b}
$$

For the particles of equal mass  $m = m_{1} = m_{2} = m_{3}$ ,

$$
X = \frac {m (x _ {1} + x _ {2} + x _ {3})}{3 m} = \frac {x _ {1} + x _ {2} + x _ {3}}{3}
$$

$$
Y = \frac {m (y _ {1} + y _ {2} + y _ {3})}{3 m} = \frac {y _ {1} + y _ {2} + y _ {3}}{3}
$$

Thus, for three particles of equal mass, the centre of mass coincides with the centroid of the triangle formed by the particles.

Results of Eqs. (6.3a) and (6.3b) are generalised easily to a system of n particles, not necessarily lying in a plane, but distributed in space. The centre of mass of such a system is at  $(X, Y, Z)$ , where

$$
X = \frac {\sum m _ {i} x _ {i}}{M}\tag{6.4a}
$$

$$
Y = \frac {\sum m _ {i} y _ {i}}{M}\tag{6.4b}
$$

$$
\text {and} Z = \frac {\sum m _ {i} z _ {i}}{M}\tag{6.4c}
$$

Here $M = \sum m_{i}$ is the total mass of the system. The index $i$ runs from 1 to $n$; $m_{i}$ is the mass of the $t^{\text{th}}$ particle and the position of the $t^{\text{th}}$ particle is given by $(x_{\mathrm{i}}, y_{\mathrm{i}}, z_{\mathrm{i}})$.

Eqs. (6.4a), (6.4b) and (6.4c) can be combined into one equation using the notation of position vectors. Let  $r_{i}$  be the position vector of the  $i^{th}$  particle and R be the position vector of the centre of mass:

$$
\begin{array}{l} \mathbf {r} _ {i} = x _ {i} \hat {\mathbf {i}} + y _ {i} \hat {\mathbf {j}} + z _ {i} \hat {\mathbf {k}} \\ \mathbf {R} = X \hat {\mathbf {i}} + Y \hat {\mathbf {j}} + Z \hat {\mathbf {k}} \end{array}
$$

$$
\mathbf {R} = \frac {\sum m _ {i} \mathbf {r} _ {i}}{M}\tag{6.4d}
$$

The sum on the right hand side is a vector sum.

Note the economy of expressions we achieve by use of vectors. If the origin of the frame of reference (the coordinate system) is chosen to be the centre of mass then  $\sum m_{i}r_{i}=0$  for the given system of particles.

A rigid body, such as a metre stick or a flywheel, is a system of closely packed particles; Eqs. (6.4a), (6.4b), (6.4c) and (6.4d) are therefore, applicable to a rigid body. The number of particles (atoms or molecules) in such a body is so large that it is impossible to carry out the summations over individual particles in these equations. Since the spacing of the particles is

Reprint 2025-26

<!-- page 6 of 35 -->

SYSTEMS OF PARTICLES AND ROTATIONAL MOTION

97

small, we can treat the body as a continuous distribution of mass. We subdivide the body into $n$ small elements of mass; $\Delta m_{1}, \Delta m_{2}... \Delta m_{n}$; the $i^{\mathrm{th}}$ element $\Delta m_{i}$ is taken to be located about the point $(x_{i}, y_{i}, z_{i})$. The coordinates of the centre of mass are then approximately given by

$$
X = \frac {\sum (\Delta m _ {i}) x _ {i}}{\sum \Delta m _ {i}}, Y = \frac {\sum (\Delta m _ {i}) y _ {i}}{\sum \Delta m _ {i}}, Z = \frac {\sum (\Delta m _ {i}) z _ {i}}{\sum \Delta m _ {i}}
$$

As we make n bigger and bigger and each  $\Delta m_{i}$  smaller and smaller, these expressions become exact. In that case, we denote the sums over i by integrals. Thus,

$$
\sum \Delta m _ {i} \rightarrow \int \mathrm{d} m = M,
$$

$$
\sum (\Delta m _ {i}) x _ {i} \to \int x   \mathrm{d} m,
$$

$$
\sum (\Delta m _ {i}) y _ {i} \rightarrow \int y \mathrm{d} m,
$$

$$
\text {and} \quad \sum (\Delta m _ {i}) z _ {i} \to \int z \mathrm{d} m
$$

Here $M$ is the total mass of the body. The coordinates of the centre of mass now are

$$
X = \frac {1}{M} \int x \mathrm{d} m, Y = \frac {1}{M} \int y \mathrm{d} m \text {and} Z = \frac {1}{M} \int z \mathrm{d} m\tag{6.5a}
$$

The vector expression equivalent to these three scalar expressions is

$$
\mathbf {R} = \frac {1}{M} \int \mathbf {r} \mathrm{d} m\tag{6.5b}
$$

If we choose, the centre of mass as the origin of our coordinate system,

$$
\mathbf {R} = \mathbf {0}
$$

$$
\text {i.e.,} \int \mathbf {r}   \mathrm{d} m = \mathbf {0}
$$

$$
\text {or} \int x \mathrm{d} m = \int y \mathrm{d} m = \int z \mathrm{d} m = 0\tag{6.6}
$$

Often we have to calculate the centre of mass of homogeneous bodies of regular shapes like rings, discs, spheres, rods etc. (By a homogeneous body we mean a body with uniformly distributed mass.) By using symmetry consideration, we can easily show that the centres of mass of these bodies lie at their geometric centres.

![Image block](doc:bba3640/tier:standard/page:6/block:19)

Fig. 6.8 Determining the CM of a thin rod.

Let us consider a thin rod, whose width and breath (in case the cross section of the rod is rectangular) or radius (in case the cross section of the rod is cylindrical) is much smaller than its length. Taking the origin to be at the geometric centre of the rod and x-axis to be along the length of the rod, we can say that on account of reflection symmetry, for every element dm of the rod at x, there is an element of the same mass dm located at -x (Fig. 6.8).

The net contribution of every such pair to the integral and hence the integral  $\int x \, dm$  itself is zero. From Eq. (6.6), the point for which the integral itself is zero, is the centre of mass. Thus, the centre of mass of a homogenous thin rod coincides with its geometric centre. This can be understood on the basis of reflection symmetry.

The same symmetry argument will apply to homogeneous rings, discs, spheres, or even thick rods of circular or rectangular cross section. For all such bodies you will realise that for every element dm at a point  $(x, y, z)$  one can always take an element of the same mass at the point  $(-x, -y, -z)$ . (In other words, the origin is a point of reflection symmetry for these bodies.) As a result, the integrals in Eq. (6.5 a) all are zero. This means that for all the above bodies, their centre of mass coincides with their geometric centre.

Example 6.1 Find the centre of mass of three particles at the vertices of an equilateral triangle. The masses of the particles are 100g, 150g, and 200g respectively. Each side of the equilateral triangle is 0.5m long.

![Image block](doc:bba3640/tier:standard/page:6/block:25)

Reprint 2025-26

<!-- page 7 of 35 -->

98

PHYSICS

With the x-and y-axes chosen as shown in Fig. 6.9, the coordinates of points O, A and B forming the equilateral triangle are respectively (0,0), (0.5,0), (0.25,0.25 $\sqrt{3}$ ). Let the masses 100 g, 150 g and 200 g be located at O, A and B be respectively. Then,

$$
\begin{array}{l} X = \frac {m _ {1} x _ {1} + m _ {2} x _ {2} + m _ {3} x _ {3}}{m _ {1} + m _ {2} + m _ {3}} \\ = \frac {1 0 0 (0) + 1 5 0 (0 . 5) + 2 0 0 (0 . 2 5) \quad \mathrm{gm}}{(1 0 0 + 1 5 0 + 2 0 0) \quad \mathrm{g}} \\ \qquad = \frac {7 5 + 5 0}{4 5 0} \mathrm{m} = \frac {1 2 5}{4 5 0} \mathrm{m} = \frac {5}{1 8} \mathrm{m} \\ Y = \frac {1 0 0 (0) + 1 5 0 (0) + 2 0 0 (0 . 2 5 \sqrt {3}) \quad \mathrm{gm}}{4 5 0 \mathrm{g}} \\ \qquad = \frac {5 0 \sqrt {3}}{4 5 0} \mathrm{m} = \frac {\sqrt {3}}{9} \mathrm{m} = \frac {1}{3 \sqrt {3}} \mathrm{m} \end{array}
$$

The centre of mass C is shown in the figure. Note that it is not the geometric centre of the triangle OAB. Why?

Example 6.2 Find the centre of mass of a triangular lamina.

Answer The lamina ( $\Delta$ LMN) may be subdivided into narrow strips each parallel to the base (MN) as shown in Fig. 6.10

![Image block](doc:bba3640/tier:standard/page:7/block:8)

Fig. 6.10

By symmetry each strip has its centre of mass at its midpoint. If we join the midpoint of all the strips we get the median LP. The centre of mass of the triangle as a whole therefore, has to lie on the median LP. Similarly, we can argue that it lies on the median MQ and NR. This means the centre of mass lies on the point of

concurrence of the medians, i.e. on the centroid G of the triangle.

Example 6.3 Find the centre of mass of a uniform L-shaped lamina (a thin flat plate) with dimensions as shown. The mass of the lamina is $3\mathrm{kg}$.

Answer Choosing the X and Y axes as shown in Fig. 6.11 we have the coordinates of the vertices of the L-shaped lamina as given in the figure. We can think of the L-shape to consist of 3 squares each of length 1m. The mass of each square is 1kg, since the lamina is uniform. The centres of mass  $C_{1}$ ,  $C_{2}$  and  $C_{3}$  of the squares are, by symmetry, their geometric centres and have coordinates (1/2, 1/2), (3/2, 1/2), (1/2, 3/2) respectively. We take the masses of the squares to be concentrated at these points. The centre of mass of the whole L shape (X, Y) is the centre of mass of these mass points.

![Image block](doc:bba3640/tier:standard/page:7/block:14)

Fig. 6.11

Hence

$$
X = \frac {\left[ 1 (1 / 2) + 1 (3 / 2) + 1 (1 / 2) \right] \mathrm{kg} \mathrm{m}}{(1 + 1 + 1) \mathrm{kg}} = \frac {5}{6} \mathrm{m}
$$

$$
Y = \frac {\left[ 1 (1 / 2) + 1 (1 / 2) + 1 (3 / 2) \right] \mathrm{kg} \mathrm{m}}{(1 + 1 + 1) \mathrm{kg}} = \frac {5}{6} \mathrm{m}
$$

The centre of mass of the L-shape lies on the line OD. We could have guessed this without calculations. Can you tell why? Suppose, the three squares that make up the L shaped lamina

Reprint 2025-26

<!-- page 8 of 35 -->

SYSTEMS OF PARTICLES AND ROTATIONAL MOTION

99

of Fig. 6.11 had different masses. How will you then determine the centre of mass of the lamina?

## 6.3 MOTION OF CENTRE OF MASS

Equipped with the definition of the centre of mass, we are now in a position to discuss its physical importance for a system of n particles. We may rewrite Eq.(6.4d) as

$$
M \mathbf {R} = \sum m _ {i} \mathbf {r} _ {i} = m _ {1} \mathbf {r} _ {1} + m _ {2} \mathbf {r} _ {2} + \ldots + m _ {n} \mathbf {r} _ {n}\tag{6.7}
$$

Differentiating the two sides of the equation with respect to time we get

$$
M \frac {\mathrm{d} \mathbf {R}}{\mathrm{d} t} = m _ {1} \frac {\mathrm{d} \mathbf {r} _ {1}}{\mathrm{d} t} + m _ {2} \frac {\mathrm{d} \mathbf {r} _ {2}}{\mathrm{d} t} + \dots + m _ {n} \frac {\mathrm{d} \mathbf {r} _ {n}}{\mathrm{d} t}
$$

$$
\begin{array}{l} \text {or} \\ M \mathbf {V} = m _ {1} \mathbf {v} _ {1} + m _ {2} \mathbf {v} _ {2} + \dots + m _ {n} \mathbf {v} _ {n} \end{array}\tag{6.8}
$$

where $\mathbf{v}_1 (= \mathrm{d}\mathbf{r}_1 / \mathrm{d}t)$ is the velocity of the first particle $\mathbf{v}_2 (= \mathrm{d}\mathbf{r}_2 / \mathrm{d}t)$ is the velocity of the second particle etc. and $\mathbf{V} = \mathrm{d}\mathbf{R} / \mathrm{d}t$ is the velocity of the centre of mass. Note that we assumed the masses $m_1, m_2, \ldots$ etc. do not change in time. We have therefore, treated them as constants in differentiating the equations with respect to time.

Differentiating Eq.(6.8) with respect to time, we obtain

$$
M \frac {\mathrm{d} \mathbf {V}}{\mathrm{d} t} = m _ {1} \frac {\mathrm{d} \mathbf {v} _ {1}}{\mathrm{d} t} + m _ {2} \frac {\mathrm{d} \mathbf {v} _ {2}}{\mathrm{d} t} + \dots + m _ {n} \frac {\mathrm{d} \mathbf {v} _ {n}}{\mathrm{d} t}
$$

or

$$
M \mathbf {A} = m _ {1} \mathbf {a} _ {1} + m _ {2} \mathbf {a} _ {2} + \dots + m _ {n} \mathbf {a} _ {n}\tag{6.9}
$$

where  $\mathbf{a}_{1}(=\mathrm{d}\mathbf{v}_{1}/\mathrm{d}t)$  is the acceleration of the first particle,  $\mathbf{a}_{2}(=\mathrm{d}\mathbf{v}_{2}/\mathrm{d}t)$  is the acceleration of the second particle etc. and  $\mathbf{A}(=\mathrm{d}\mathbf{V}/\mathrm{d}t)$  is the acceleration of the centre of mass of the system of particles.

Now, from Newton's second law, the force acting on the first particle is given by  $F_{1}=m_{1}a_{1}$ . The force acting on the second particle is given by  $F_{2}=m_{2}a_{2}$  and so on. Eq. (6.9) may be written as

$$
M \mathbf {A} = \mathbf {F} _ {1} + \mathbf {F} _ {2} + \dots + \mathbf {F} _ {n}\tag{6.10}
$$

Thus, the total mass of a system of particles times the acceleration of its centre of mass is the vector sum of all the forces acting on the system of particles.

Note when we talk of the force $\mathbf{F}_1$ on the first particle, it is not a single force, but the vector sum of all the forces on the first particle; likewise for the second particle etc. Among these forces on each particle there will be external forces exerted by bodies outside the system and also internal forces exerted by the particles on one another. We know from Newton's third law that these internal forces occur in equal and opposite pairs and in the sum of forces of Eq. (6.10), their contribution is zero. Only the external forces contribute to the equation. We can then rewrite Eq. (6.10) as

$$
M \mathbf {A} = \mathbf {F} _ {\text {ext}}\tag{6.11}
$$

where  $F_{ext}$  represents the sum of all external forces acting on the particles of the system.

Eq. (6.11) states that the centre of mass of a system of particles moves as if all the mass of the system was concentrated at the centre of mass and all the external forces were applied at that point.

Notice, to determine the motion of the centre of mass no knowledge of internal forces of the system of particles is required; for this purpose we need to know only the external forces.

To obtain Eq. (6.11) we did not need to specify the nature of the system of particles. The system may be a collection of particles in which there may be all kinds of internal motions, or it may be a rigid body which has either pure translational motion or a combination of translational and rotational motion. Whatever is the system and the motion of its individual particles, the centre of mass moves according to Eq. (6.11).

Instead of treating extended bodies as single particles as we have done in earlier chapters, we can now treat them as systems of particles. We can obtain the translational component of their motion, i.e. the motion of the centre of mass of the system, by taking the mass of the whole system to be concentrated at the centre of mass and all the external forces on the system to be acting at the centre of mass.

This is the procedure that we followed earlier in analysing forces on bodies and solving

Reprint 2025-26

<!-- page 9 of 35 -->

100

PHYSICS

problems without explicitly outlining and justifying the procedure. We now realise that in earlier studies we assumed, without saying so, that rotational motion and/or internal motion of the particles were either absent or negligible. We no longer need to do this. We have not only found the justification of the procedure we followed earlier; but we also have found how to describe and separate the translational motion of (1) a rigid body which may be rotating as well, or (2) a system of particles with all kinds of internal motion.

![Image block](doc:bba3640/tier:standard/page:9/block:4)

Fig. 6.12 The centre of mass of the fragments of the projectile continues along the same parabolic path which it would have followed if there were no explosion.

Figure 6.12 is a good illustration of Eq. (6.11). A projectile, following the usual parabolic trajectory, explodes into fragments midway in air. The forces leading to the explosion are internal forces. They contribute nothing to the motion of the centre of mass. The total external force, namely, the force of gravity acting on the body, is the same before and after the explosion. The centre of mass under the influence of the external force continues, therefore, along the same parabolic trajectory as it would have followed if there were no explosion.

## 6.4 LINEAR MOMENTUM OF A SYSTEM OF PARTICLES

Let us recall that the linear momentum of a particle is defined as

$$
\mathbf {p} = m \mathbf {v}\tag{6.12}
$$

Let us also recall that Newton's second law written in symbolic form for a single particle is

$$
\mathbf {F} = \frac {\mathrm{d} \mathbf {p}}{\mathrm{d} t}\tag{6.13}
$$

where $\mathbf{F}$ is the force on the particle. Let us consider a system of $n$ particles with masses $m_{1}, m_{2}, \ldots, m_{n}$ respectively and velocities $\mathbf{v}_{1}, \mathbf{v}_{2}, \ldots, \mathbf{v}_{n}$ respectively. The particles may be interacting and have external forces acting on them. The linear momentum of the first particle is $m_{1} \mathbf{v}_{1}$, of the second particle is $m_{2} \mathbf{v}_{2}$ and so on.

For the system of n particles, the linear momentum of the system is defined to be the vector sum of all individual particles of the system,

$$
\begin{array}{l} \mathbf {P} = \mathbf {p} _ {1} + \mathbf {p} _ {2} + \dots + \mathbf {p} _ {n} \\ = m _ {1} \mathbf {v} _ {1} + m _ {2} \mathbf {v} _ {2} + \dots + m _ {n} \mathbf {v} _ {n} \\ \text {Comparing this with Eq. (6.8)} \end{array}
$$

$$
\mathbf {P} = M \mathbf {V}\tag{6.14}
$$

(6.15)

Thus, the total momentum of a system of particles is equal to the product of the total mass of the system and the velocity of its centre of mass. Differentiating Eq. (6.15) with respect to time,

$$
\frac {\mathrm{d} \mathbf {P}}{\mathrm{d} t} = M \frac {\mathrm{d} \mathbf {V}}{\mathrm{d} t} = M \mathbf {A}\tag{6.16}
$$

Comparing Eq.(6.16) and Eq. (6.11),

$$
\frac {\mathrm{d} \mathbf {P}}{\mathrm{d} t} = \mathbf {F} _ {e x t}\tag{6.17}
$$

This is the statement of Newton's second law of motion extended to a system of particles.

Suppose now, that the sum of external forces acting on a system of particles is zero. Then from Eq.(6.17)

$$
\frac {\mathrm{d} \mathbf {P}}{\mathrm{d} t} = 0 \quad \text {or} \quad \mathbf {P} = \text {Constant}\tag{6.18a}
$$

Thus, when the total external force acting on a system of particles is zero, the total linear momentum of the system is constant. This is the law of conservation of the total linear momentum of a system of particles. Because of Eq. (6.15), this also means that when the total external force on the system is zero the velocity of the centre of mass remains constant. (We assume throughout the discussion on systems of particles in this chapter that the total mass of the system remains constant.)

Note that on account of the internal forces, i.e. the forces exerted by the particles on one another, the individual particles may have

Reprint 2025-26

<!-- page 10 of 35 -->

SYSTEMS OF PARTICLES AND ROTATIONAL MOTION

101

complicated trajectories. Yet, if the total external force acting on the system is zero, the centre of mass moves with a constant velocity, i.e., moves uniformly in a straight line like a free particle.

The vector Eq. (6.18a) is equivalent to three scalar equations,

$$
P _ {x} = c _ {l}, P _ {y} = c _ {2} \text {and} P _ {z} = c _ {3}\tag{6.18b}
$$

Here $P_x, \bar{P}_y$ and $P_z$ are the components of the total linear momentum vector P along the x-, y- and z-axes respectively; $c_1, c_2$ and $c_3$ are constants.

![Image block](doc:bba3640/tier:standard/page:10/block:7)

Fig. 6.13 (a) A heavy nucleus radium (Ra) splits into a lighter nucleus radon (Rn) and an alpha particle (nucleus of helium atom). The CM of the system is in uniform motion.

(b) The same splitting of the heavy nucleus radium (Ra) with the centre of mass at rest. The two product particles fly back to back.

As an example, let us consider the radioactive decay of a moving unstable particle, like the nucleus of radium. A radium nucleus disintegrates into a nucleus of radon and an alpha particle. The forces leading to the decay are internal to the system and the external forces on the system are negligible. So the total linear momentum of the system is the same before and after decay. The two particles produced in the decay, the radon nucleus and the alpha particle, move in different directions in such a way that their centre of mass moves along the same path along which the original decaying radium nucleus was moving [Fig. 6.13(a)].

If we observe the decay from the frame of reference in which the centre of mass is at rest, the motion of the particles involved in the decay looks particularly simple; the product particles

![Image block](doc:bba3640/tier:standard/page:10/block:12)

Fig. 6.14 (a) Trajectories of two stars, $S_{1}$ (dotted line) and $S_{2}$ (solid line) forming a binary system with their centre of mass $C$ in uniform motion.

(b) The same binary system, with the centre of mass $C$ at rest.

move back to back with their centre of mass remaining at rest as shown in Fig.6.13 (b).

In many problems on the system of particles, as in the above radioactive decay problem, it is convenient to work in the centre of mass frame rather than in the laboratory frame of reference.

In astronomy, binary (double) stars is a common occurrence. If there are no external forces, the centre of mass of a double star moves like a free particle, as shown in Fig.6.14(a). The trajectories of the two stars of equal mass are also shown in the figure; they look complicated. If we go to the centre of mass frame, then we find that there the two stars are moving in a circle, about the centre of mass, which is at rest. Note that the position of the stars have to be diametrically opposite to each other [Fig. 6.14(b)]. Thus in our frame of reference, the trajectories of the stars are a combination of (i) uniform motion in a straight line of the centre of mass and (ii) circular orbits of the stars about the centre of mass.

As can be seen from the two examples, separating the motion of different parts of a system into motion of the centre of mass and motion about the centre of mass is a very useful technique that helps in understanding the motion of the system.

## 6.5 VECTOR PRODUCT OF TWO VECTORS

We are already familiar with vectors and their use in physics. In chapter 5 (Work, Energy, Power) we defined the scalar product of two vectors. An important physical quantity, work, is defined as a scalar product of two vector quantities, force and displacement.

Reprint 2025-26

<!-- page 11 of 35 -->

102

PHYSICS

We shall now define another product of two vectors. This product is a vector. Two important quantities in the study of rotational motion, namely, moment of a force and angular momentum, are defined as vector products.

## Definition of Vector Product

A vector product of two vectors $\mathbf{a}$ and $\mathbf{b}$ is a vector $\mathbf{c}$ such that

(i) magnitude of $\mathbf{c} = c = ab\sin \theta$ where a and b are magnitudes of $\mathbf{a}$ and $\mathbf{b}$ and $\theta$ is the angle between the two vectors.

(ii) $\mathbf{c}$ is perpendicular to the plane containing $\mathbf{a}$ and $\mathbf{b}$.

(iii) if we take a right handed screw with its head lying in the plane of a and b and the screw perpendicular to this plane, and if we turn the head in the direction from a to b, then the tip of the screw advances in the direction of c. This right handed screw rule is illustrated in Fig. 6.15a.

Alternatively, if one curls up the fingers of right hand around a line perpendicular to the plane of the vectors a and b and if the fingers are curled up in the direction from a to b, then the stretched thumb points in the direction of c, as shown in Fig. 6.15b.

![Image block](doc:bba3640/tier:standard/page:11/block:10)

(a)

![Image block](doc:bba3640/tier:standard/page:11/block:12)

(b)

Fig. 6.15 (a) Rule of the right handed screw for defining the direction of the vector product of two vectors.

(b) Rule of the right hand for defining the direction of the vector product.

A simpler version of the right hand rule is the following : Open up your right hand palm and curl the fingers pointing from a to b. Your stretched thumb points in the direction of c.

It should be remembered that there are two angles between any two vectors $\mathbf{a}$ and $\mathbf{b}$. In Fig. 6.15 (a) or (b) they correspond to $\theta$ (as shown) and $(360^{\circ} - \theta)$. While applying either of the above rules, the rotation should be taken through the smaller angle $(< 180^{\circ})$ between $\mathbf{a}$ and $\mathbf{b}$. It is $\theta$ here.

Because of the cross $(\times)$ used to denote the vector product, it is also referred to as cross product.

\- Note that scalar product of two vectors is commutative as said earlier, $\mathbf{a.b} = \mathbf{b.a}$

The vector product, however, is not commutative, i.e. $\mathbf{a} \times \mathbf{b} \neq \mathbf{b} \times \mathbf{a}$

The magnitude of both  $a \times b$  and  $b \times a$  is the same ( $ab \sin \theta$ ); also, both of them are perpendicular to the plane of a and b. But the rotation of the right-handed screw in case of  $a \times b$  is from a to b, whereas in case of  $b \times a$  it is from b to a. This means the two vectors are in opposite directions. We have

$$
\mathbf {a} \times \mathbf {b} = - \mathbf {b} \times \mathbf {a}
$$

\- Another interesting property of a vector product is its behaviour under reflection. Under reflection (i.e. on taking the plane mirror image) we have $x \to -x, y \to -y$ and $z \to -z$. As a result all the components of a vector change sign and thus $a \to -a$, $b \to -b$. What happens to $\mathbf{a} \times \mathbf{b}$ under reflection?

$$
\mathbf {a} \times \mathbf {b} \rightarrow (- \mathbf {a}) \times (- \mathbf {b}) = \mathbf {a} \times \mathbf {b}
$$

Thus, $\mathbf{a} \times \mathbf{b}$ does not change sign under reflection.

\- Both scalar and vector products are distributive with respect to vector addition. Thus,

$$
\begin{array}{c} \mathbf {a}. (\mathbf {b} + \mathbf {c}) = \mathbf {a}. \mathbf {b} + \mathbf {a}. \mathbf {c} \\ \mathbf {a} \times (\mathbf {b} + \mathbf {c}) = \mathbf {a} \times \mathbf {b} + \mathbf {a} \times \mathbf {c} \end{array}
$$

\- We may write $\mathbf{c} = \mathbf{a} \times \mathbf{b}$ in the component form. For this we first need to obtain some elementary cross products:

(i) $\mathbf{a} \times \mathbf{a} = \mathbf{0}$ (0 is a null vector, i.e. a vector with zero magnitude)

This follows since magnitude of  $a \times a$  is  $a^{2} \sin 0^{\circ} = 0$ .

Reprint 2025-26

<!-- page 12 of 35 -->

SYSTEMS OF PARTICLES AND ROTATIONAL MOTION

103

From this follow the results

$$
(\mathrm{i}) \hat {\mathbf {i}} \times \hat {\mathbf {i}} = \mathbf {0}, \hat {\mathbf {j}} \times \hat {\mathbf {j}} = \mathbf {0}, \hat {\mathbf {k}} \times \hat {\mathbf {k}} = \mathbf {0}
$$

(ii) $\hat{\mathbf{i}}\times \hat{\mathbf{j}} = \hat{\mathbf{k}}$

Note that the magnitude of $\hat{\mathbf{i}}\times \hat{\mathbf{j}}$ is $\sin 90^{\circ}$ or 1, since $\hat{\mathbf{i}}$ and $\hat{\mathbf{j}}$ both have unit magnitude and the angle between them is $90^{\circ}$. Thus, $\hat{\mathbf{i}}\times \hat{\mathbf{j}}$ is a unit vector. A unit vector perpendicular to the plane of $\hat{\mathbf{i}}$ and $\hat{\mathbf{j}}$ and related to them by the right hand screw rule is $\hat{\mathbf{k}}$. Hence, the above result. You may verify similarly,

$$
\hat {\mathbf {j}} \times \hat {\mathbf {k}} = \hat {\mathbf {i}} \quad \text {and} \quad \hat {\mathbf {k}} \times \hat {\mathbf {i}} = \hat {\mathbf {j}}
$$

From the rule for commutation of the cross product, it follows:

$$
\hat {\mathbf {j}} \times \hat {\mathbf {i}} = - \hat {\mathbf {k}}, \quad \hat {\mathbf {k}} \times \hat {\mathbf {j}} = - \hat {\mathbf {i}}, \quad \hat {\mathbf {i}} \times \hat {\mathbf {k}} = - \hat {\mathbf {j}}
$$

Note if  $\hat{i},\hat{j},\hat{k}$  occur cyclically in the above vector product relation, the vector product is positive. If  $\hat{i},\hat{j},\hat{k}$  do not occur in cyclic order, the vector product is negative.

Now,

$$
\begin{array}{l} \mathbf {a} \times \mathbf {b} = (a _ {x} \hat {\mathbf {i}} + a _ {y} \hat {\mathbf {j}} + a _ {z} \hat {\mathbf {k}}) \times (b _ {x} \hat {\mathbf {i}} + b _ {y} \hat {\mathbf {j}} + b _ {z} \hat {\mathbf {k}}) \\ = a _ {x} b _ {y} \hat {\mathbf {k}} - a _ {x} b _ {z} \hat {\mathbf {j}} - a _ {y} b _ {x} \hat {\mathbf {k}} + a _ {y} b _ {z} \hat {\mathbf {i}} + a _ {z} b _ {x} \hat {\mathbf {j}} - a _ {z} b _ {y} \hat {\mathbf {i}} \\ = (a _ {y} b _ {z} - a _ {z} b _ {y}) \mathbf {i} + (a _ {z} b _ {x} - a _ {x} b _ {z}) \mathbf {j} + (a _ {x} b _ {y} - a _ {y} b _ {x}) \mathbf {k} \end{array}
$$

We have used the elementary cross products in obtaining the above relation. The expression for  $a \times b$  can be put in a determinant form which is easy to remember.

$$
\mathbf {a} \times \mathbf {b} = \left| \begin{array}{c c c} \hat {\mathbf {i}} & \hat {\mathbf {j}} & \hat {\mathbf {k}} \\ a _ {x} & a _ {y} & a _ {z} \\ b _ {x} & b _ {y} & b _ {z} \end{array} \right|
$$

Example 6.4 Find the scalar and vector products of two vectors. $\mathbf{a} = (3\hat{\mathbf{i}} - 4\hat{\mathbf{j}} + 5\hat{\mathbf{k}})$ and $\mathbf{b} = (-2\hat{\mathbf{i}} + \hat{\mathbf{j}} + 3\hat{\mathbf{k}})$

Answer

$$
\begin{array}{r l} \mathbf {a} \cdot \mathbf {b} & = (3 \hat {\mathbf {i}} - 4 \hat {\mathbf {j}} + 5 \hat {\mathbf {k}}) \cdot (- 2 \hat {\mathbf {i}} + \hat {\mathbf {j}} - 3 \hat {\mathbf {k}}) \\ & = - 6 - 4 - 1 5 \\ & = - 2 5 \end{array}
$$

$$
\mathbf {a} \times \mathbf {b} = \left| \begin{array}{c c c} \hat {\mathbf {i}} & \hat {\mathbf {j}} & \hat {\mathbf {k}} \\ 3 & - 4 & 5 \\ - 2 & 1 & - 3 \end{array} \right| = 7 \hat {\mathbf {i}} - \hat {\mathbf {j}} - 5 \hat {\mathbf {k}}
$$

Note $\mathbf{b}\times \mathbf{a} = -7\hat{\mathbf{i}} +\hat{\mathbf{j}} +5\hat{\mathbf{k}}$

## 6.6 ANGULAR VELOCITY AND ITS RELATION WITH LINEAR VELOCITY

In this section we shall study what is angular velocity and its role in rotational motion. We have seen that every particle of a rotating body moves in a circle. The linear velocity of the particle is related to the angular velocity. The relation between these two quantities involves a vector product which we learnt about in the last section.

Let us go back to Fig. 6.4. As said above, in rotational motion of a rigid body about a fixed axis, every particle of the body moves in a circle,

![Image block](doc:bba3640/tier:standard/page:12/block:23)

Fig. 6.16 Rotation about a fixed axis. (A particle (P) of the rigid body rotating about the fixed (z-) axis moves in a circle with centre (C) on the axis.)

which lies in a plane perpendicular to the axis and has its centre on the axis. In Fig. 6.16 we redraw Fig. 6.4, showing a typical particle (at a point P) of the rigid body rotating about a fixed axis (taken as the z-axis). The particle describes

Reprint 2025-26

<!-- page 13 of 35 -->

104

PHYSICS

a circle with a centre C on the axis. The radius of the circle is r, the perpendicular distance of the point P from the axis. We also show the linear velocity vector v of the particle at P. It is along the tangent at P to the circle.

Let P' be the position of the particle after an interval of time  $\Delta t$  (Fig. 6.16). The angle PCP' describes the angular displacement  $\Delta\theta$  of the particle in time  $\Delta t$ . The average angular velocity of the particle over the interval  $\Delta t$  is  $\Delta\theta/\Delta t$ . As  $\Delta t$  tends to zero (i.e. takes smaller and smaller values), the ratio  $\Delta\theta/\Delta t$  approaches a limit which is the instantaneous angular velocity  $d\theta/dt$  of the particle at the position P. We denote the instantaneous angular velocity by  $\omega$  (the Greek letter omega). We know from our study of circular motion that the magnitude of linear velocity v of a particle moving in a circle is related to the angular velocity of the particle  $\omega$  by the simple relation  $\upsilon=\omega r$ , where r is the radius of the circle.

We observe that at any given instant the relation $v = \omega r$ applies to all particles of the rigid body. Thus for a particle at a perpendicular distance $r_i$ from the fixed axis, the linear velocity at a given instant $v_i$ is given by

$$
\boldsymbol {v} _ {i} = \omega \boldsymbol {r} _ {i}\tag{6.19}
$$

The index $i$ runs from 1 to $n$, where $n$ is the total number of particles of the body.

For particles on the axis, r = 0, and hence  $v = \omega r = 0$ . Thus, particles on the axis are stationary. This verifies that the axis is fixed.

Note that we use the same angular velocity $\omega$ for all the particles. We therefore, refer to $\omega$ as the angular velocity of the whole body.

We have characterised pure translation of a body by all parts of the body having the same velocity at any instant of time. Similarly, we may characterise pure rotation by all parts of the body having the same angular velocity at any instant of time. Note that this characterisation of the rotation of a rigid body about a fixed axis is just another way of saying as in Sec. 6.1 that each particle of the body moves in a circle, which lies in a plane perpendicular to the axis and has the centre on the axis.

In our discussion so far the angular velocity appears to be a scalar. In fact, it is a vector. We shall not justify this fact, but we shall accept it. For rotation about a fixed axis, the angular velocity vector lies along the axis of rotation,

and points out in the direction in which a right handed screw would advance, if the head of the screw is rotated with the body. (See Fig. 6.17a).

The magnitude of this vector is  $\omega = d\theta/dt$  referred as above.

![Image block](doc:bba3640/tier:standard/page:13/block:14)

Fig. 6.17 (a) If the head of a right handed screw rotates with the body, the screw advances in the direction of the angular velocity $\omega$. If the sense (clockwise or anticlockwise) of rotation of the body changes, so does the direction of $\omega$.

![Image block](doc:bba3640/tier:standard/page:13/block:16)

Fig. 6.17 (b) The angular velocity vector $\omega$ is directed along the fixed axis as shown. The linear velocity of the particle at $P$ is $\mathbf{v} = \boldsymbol{\omega} \times \mathbf{r}$. It is perpendicular to both $\omega$ and $\mathbf{r}$ and is directed along the tangent to the circle described by the particle.

We shall now look at what the vector product  $\omega \times r$  corresponds to. Refer to Fig. 6.17(b) which is a part of Fig. 6.16 reproduced to show the path of the particle P. The figure shows the vector  $\omega$  directed along the fixed  $(z-)$  axis and also the position vector r = OP of the particle at P of the rigid body with respect to the origin O. Note that the origin is chosen to be on the axis of rotation.

Reprint 2025-26

<!-- page 14 of 35 -->

SYSTEMS OF PARTICLES AND ROTATIONAL MOTION

105

Now  $\omega \times r = \omega \times OP = \omega \times (OC + CP)$ 
But  $\omega \times OC = 0$  as  $\omega$  is along OC
Hence  $\omega \times r = \omega \times CP$

The vector $\omega \times \mathbf{CP}$ is perpendicular to $\omega$, i.e. to the $z$-axis and also to $\mathbf{CP}$, the radius of the circle described by the particle at P. It is therefore, along the tangent to the circle at P. Also, the magnitude of $\omega \times \mathbf{CP}$ is $\omega$ (CP) since $\omega$ and $\mathbf{CP}$ are perpendicular to each other. We shall denote $\mathbf{CP}$ by $\mathbf{r}_{\perp}$ and not by $\mathbf{r}$, as we did earlier.

Thus,  $\omega \times r$  is a vector of magnitude  $\omega r_{\perp}$  and is along the tangent to the circle described by the particle at P. The linear velocity vector v at P has the same magnitude and direction. Thus,

$$
\mathbf {v} = \boldsymbol {\omega} \times \mathbf {r}\tag{6.20}
$$

In fact, the relation, Eq. (6.20), holds good even for rotation of a rigid body with one point fixed, such as the rotation of the top [Fig. 6.6(a)]. In this case r represents the position vector of the particle with respect to the fixed point taken as the origin.

We note that for rotation about a fixed axis, the direction of the vector  $\omega$  does not change with time. Its magnitude may, however, change from instant to instant. For the more general rotation, both the magnitude and the direction of  $\omega$  may change from instant to instant.

## 6.6.1 Angular acceleration

You may have noticed that we are developing the study of rotational motion along the lines of the study of translational motion with which we are already familiar. Analogous to the kinetic variables of linear displacement (s) and velocity (v) in translational motion, we have angular displacement ( $\theta$ ) and angular velocity ( $\omega$ ) in rotational motion. It is then natural to define in rotational motion the concept of angular acceleration in analogy with linear acceleration defined as the time rate of change of velocity in translational motion. We define angular acceleration  $\alpha$  as the time rate of change of angular velocity. Thus,

$$
\boldsymbol {\alpha} = \frac {\mathrm{d} \boldsymbol {\omega}}{\mathrm{d} t}\tag{6.21}
$$

If the axis of rotation is fixed, the direction of  $\omega$  and hence, that of  $\alpha$  is fixed. In this case the vector equation reduces to a scalar equation

$$
\alpha = \frac {\mathrm{d} \omega}{\mathrm{d} t}\tag{6.22}
$$

## 6.7 TORQUE AND ANGULAR MOMENTUM

In this section, we shall acquaint ourselves with two physical quantities (torque and angular momentum) which are defined as vector products of two vectors. These as we shall see, are especially important in the discussion of motion of systems of particles, particularly rigid bodies.

## 6.7.1 Moment of force (Torque)

We have learnt that the motion of a rigid body, in general, is a combination of rotation and translation. If the body is fixed at a point or along a line, it has only rotational motion. We know that force is needed to change the translational state of a body, i.e. to produce linear acceleration. We may then ask, what is the analogue of force in the case of rotational motion? To look into the question in a concrete situation let us take the example of opening or closing of a door. A door is a rigid body which can rotate about a fixed vertical axis passing through the hinges. What makes the door rotate? It is clear that unless a force is applied the door does not rotate. But any force does not do the job. A force applied to the hinge line cannot produce any rotation at all, whereas a force of given magnitude applied at right angles to the door at its outer edge is most effective in producing rotation. It is not the force alone, but how and where the force is applied is important in rotational motion.

The rotational analogue of force in linear motion is moment of force. It is also referred to as torque or couple. (We shall use the words moment of force and torque interchangeably.) We shall first define the moment of force for the special case of a single particle. Later on we shall extend the concept to systems of particles including rigid bodies. We shall also relate it to a change in the state of rotational motion, i.e. is angular acceleration of a rigid body.

Reprint 2025-26

<!-- page 15 of 35 -->

106

PHYSICS

![Image block](doc:bba3640/tier:standard/page:15/block:3)

Fig. 6.18 $\tau = \mathbf{r} \times \mathbf{F}$, $\tau$ is perpendicular to the plane containing $\mathbf{r}$ and $\mathbf{F}$, and its direction is given by the right handed screw rule.

If a force acts on a single particle at a point P whose position with respect to the origin O is given by the position vector r (Fig. 6.18), the moment of the force acting on the particle with respect to the origin O is defined as the vector product

$$
\boldsymbol {\tau} = \mathbf {r} \times \mathbf {F}\tag{6.23}
$$

The moment of force (or torque) is a vector quantity. The symbol  $\tau$  stands for the Greek letter tau. The magnitude of  $\tau$  is

$$
\tau = r F \sin \theta\tag{6.24a}
$$

where r is the magnitude of the position vector r, i.e. the length OP, F is the magnitude of force F and  $\theta$  is the angle between r and F as shown.

Moment of force has dimensions  $M L^{2} T^{-2}$ . Its dimensions are the same as those of work or energy. It is, however, a very different physical quantity than work. Moment of a force is a vector, while work is a scalar. The SI unit of moment of force is newton metre (N m). The magnitude of the moment of force may be written

$$
\tau = (r \sin \theta) F = r _ {\perp} F\tag{6.24b}
$$

$$
\text {or} \tau = r F \sin \theta = r F _ {\perp}\tag{6.24c}
$$

where $r_{\perp} = r\sin \theta$ is the perpendicular distance

of the line of action of $\mathbf{F}$ from the origin and $F_{\perp}(= F\sin \theta)$ is the component of $\mathbf{F}$ in the direction perpendicular to $\mathbf{r}$. Note that $\tau = 0$ if $r = 0$, $F = 0$ or $\theta = 0^{\circ}$ or $180^{\circ}$. Thus, the moment of a force vanishes if either the magnitude of the force is zero, or if the line of action of the force passes through the origin.

One may note that since  $r \times F$  is a vector product, properties of a vector product of two vectors apply to it. If the direction of F is reversed, the direction of the moment of force is reversed. If directions of both r and F are reversed, the direction of the moment of force remains the same.

## 6.7.2 Angular momentum of a particle

Just as the moment of a force is the rotational analogue of force in linear motion, the quantity angular momentum is the rotational analogue of linear momentum. We shall first define angular momentum for the special case of a single particle and look at its usefulness in the context of single particle motion. We shall then extend the definition of angular momentum to systems of particles including rigid bodies.

Like moment of a force, angular momentum is also a vector product. It could also be referred to as moment of (linear) momentum. From this term one could guess how angular momentum is defined.

Consider a particle of mass m and linear momentum p at a position r relative to the origin O. The angular momentum l of the particle with respect to the origin O is defined to be

$$
l = \mathbf {r} \times \mathbf {p}\tag{6.25a}
$$

The magnitude of the angular momentum vector is

$$
l = r p \sin \theta\tag{6.26a}
$$

where $p$ is the magnitude of $\mathbf{p}$ and $\theta$ is the angle between $\mathbf{r}$ and $\mathbf{p}$. We may write

$$
l = r p _ {\perp} \text {or} r _ {\perp} p\tag{6.26b}
$$

where $r_{\perp} (= r \sin \theta)$ is the perpendicular distance of the directional line of $\mathbf{p}$ from the origin and $p_{\perp} (= p \sin \theta)$ is the component of $\mathbf{p}$ in a direction perpendicular to $\mathbf{r}$. We expect the angular momentum to be zero ($l = 0$), if the linear momentum vanishes ($p = 0$), if the particle is at the origin ($r = 0$), or if the directional line of $\mathbf{p}$ passes through the origin $\theta = 0^{\circ}$ or $180^{\circ}$.

Reprint 2025-26

<!-- page 16 of 35 -->

![Image block](doc:bba3640/tier:standard/page:16/block:1)

SYSTEMS OF PARTICLES AND ROTATIONAL MOTION

107

The physical quantities, moment of a force and angular momentum, have an important relation between them. It is the rotational analogue of the relation between force and linear momentum. For deriving the relation in the context of a single particle, we differentiate  $l = r \times p$  with respect to time,

$$
\frac {\mathrm{d} \boldsymbol {l}}{\mathrm{d} t} = \frac {\mathrm{d}}{\mathrm{d} t} (\boldsymbol {\mathbf {r}} \times \boldsymbol {\mathbf {p}})
$$

Applying the product rule for differentiation to the right hand side,

$$
\frac {\mathrm{d}}{\mathrm{d} t} (\mathbf {r} \times \mathbf {p}) = \frac {\mathrm{d} \mathbf {r}}{\mathrm{d} t} \times \mathbf {p} + \mathbf {r} \times \frac {\mathrm{d} \mathbf {p}}{\mathrm{d} t}
$$

Now, the velocity of the particle is $\mathbf{v} = d\mathbf{x} / dt$ and $\mathbf{p} = m\mathbf{v}$

$$
\text {Because of this} \frac {\mathrm{d} \mathbf {r}}{\mathrm{d} t} \times \mathbf {p} = \mathbf {v} \times m \mathbf {v} = 0,
$$

as the vector product of two parallel vectors vanishes. Further, since $\mathrm{d}\mathbf{p} / \mathrm{d}t = \mathbf{F}$,

$$
\mathbf {r} \times \frac {\mathrm{d} \mathbf {p}}{\mathrm{d} t} = \mathbf {r} \times \mathbf {F} = \mathbf {t}
$$

$$
\text {Hence} \frac {\mathrm{d}}{\mathrm{d} t} (\mathbf {r} \times \mathbf {p}) = \tau
$$

$$
\text {or} \frac {\mathrm{d} \boldsymbol {l}}{\mathrm{d} t} = \boldsymbol {\tau}\tag{6.27}
$$

Thus, the time rate of change of the angular momentum of a particle is equal to the torque acting on it. This is the rotational analogue of the equation $\mathbf{F} = \mathrm{d}\mathbf{p} / \mathrm{d}t$, which expresses Newton's second law for the translational motion of a single particle.

## Torque and angular momentum for a system of particles

To get the total angular momentum of a system of particles about a given point we need to add vectorially the angular momenta of individual particles. Thus, for a system of n particles,

$$
\boldsymbol {L} = \boldsymbol {l} _ {1} + \boldsymbol {l} _ {2} + \dots + \boldsymbol {l} _ {n} = \sum_ {i = 1} ^ {n} \boldsymbol {l} _ {i}
$$

The angular momentum of the  $i^{th}$  particle is given by

$$
\boldsymbol {l} _ {i} = \mathbf {r} _ {i} \quad \mathbf {p} _ {i}
$$

where  $r_{i}$  is the position vector of the  $i^{th}$  particle with respect to a given origin and  $\mathbf{p} = (m_{i}\mathbf{v}_{i})$  is the linear momentum of the particle. (The

## An experiment with the bicycle rim

Take a bicycle rim and extend its axle on both sides. Tie two strings at both ends A and B, as shown in the adjoining figure. Hold both the strings together in

one hand such that the rim is vertical. If you leave one string, the rim will tilt. Now keeping the rim in vertical position with both the strings in one hand, put the wheel in fast rotation around the axle with the other hand. Then leave one string, say B, from your hand, and observe what happens.

The rim keeps rotating in a vertical plane and the plane of rotation turns around the string A which you are holding. We say that the axis of rotation of the rim or equivalently its angular momentum precesses about the string A.

The rotating rim gives rise to an angular momentum. Determine the direction of this angular momentum. When you are holding the rotating rim with string A, a torque is generated. (We leave it to you to find out how the torque is generated and what its direction is.) The effect of the torque on the angular momentum is to make it precess around an axis perpendicular to both the angular momentum and the torque. Verify all these statements.

particle has mass  $m_{i}$  and velocity  $v_{i}$ . We may write the total angular momentum of a system of particles as

$$
\left| \mathbf {L} = \sum \boldsymbol {l} _ {i} = \sum_ {i} \mathbf {r} _ {i} \times \mathbf {p} _ {i} \right|\tag{6.25b}
$$

This is a generalisation of the definition of angular momentum (Eq. 6.25a) for a single particle to a system of particles.

Using Eqs. (6.23) and (6.25b), we get

Reprint 2025-26

<!-- page 17 of 35 -->

108

PHYSICS

$$
\left| \frac {\mathrm{d} \boldsymbol {L}}{\mathrm{d} t} = \frac {\mathrm{d}}{\mathrm{d} t} \left(\Sigma \boldsymbol {l} _ {i}\right) = \sum_ {i} \frac {\mathrm{d} \boldsymbol {l}}{\mathrm{d} t} = \sum_ {i} \tau_ {i} \right|\tag{6.28a}
$$

where $\tau_{i}$ is the torque acting on the $i^{\mathrm{th}}$ particle;

$$
\boldsymbol {\tau} _ {i} = \mathbf {r} _ {i} \times \mathbf {F} _ {i}
$$

The force  $F_{i}$  on the  $i^{th}$  particle is the vector sum of external forces  $F_{i}^{ext}$  acting on the particle and the internal forces  $F_{i}^{int}$  exerted on it by the other particles of the system. We may therefore separate the contribution of the external and the internal forces to the total torque

$\tau = \sum_{i}\tau_{i} = \sum_{i}\mathbf{r}_{i}\times \mathbf{F}_{i}$ as

$$
\tau = \tau_ {e x t} + \tau_ {\text {int}},
$$

where

$$
\boldsymbol {\tau} _ {e x t} = \sum_ {i} \mathbf {r} _ {i} \times \mathbf {F} _ {i} ^ {e x t}
$$

and

$$
\boldsymbol {\tau} _ {\mathrm{int}} = \sum_ {i} \mathbf {r} _ {i} \times \mathbf {F} _ {i} ^ {\mathrm{int}}
$$

We shall assume not only Newton's third law of motion, i.e. the forces between any two particles of the system are equal and opposite, but also that these forces are directed along the line joining the two particles. In this case the contribution of the internal forces to the total torque on the system is zero, since the torque resulting from each action-reaction pair of forces is zero. We thus have, $\tau_{\mathrm{int}} = 0$ and therefore $\tau = \tau_{\mathrm{ext}}$.

Since  $\tau=\sum\tau_{i}$ , it follows from Eq. (6.28a) that

$$
\frac {\mathrm{d} \mathbf {L}}{\mathrm{d} t} = \boldsymbol {\tau} _ {e x t}\tag{6.28 b}
$$

Thus, the time rate of the total angular momentum of a system of particles about a point (taken as the origin of our frame of reference) is equal to the sum of the external torques (i.e. the torques due to external forces) acting on the system taken about the same point. Eq. (6.28 b) is the generalisation of the single particle case of Eq. (6.23) to a system of particles. Note that when we have only one particle, there are no internal forces or torques. Eq.(6.28 b) is the rotational analogue of

$$
\frac {\mathrm{d} \mathbf {P}}{\mathrm{d} t} = \mathbf {F} _ {e x t}\tag{6.17}
$$

Note that like Eq.(6.17), Eq.(6.28b) holds good for any system of particles, whether it is a rigid body or its individual particles have all kinds of internal motion.

## Conservation of angular momentum

If $\pmb{\tau}_{\mathrm{ext}} = \mathbf{0}$, Eq. (6.28b) reduces to

$$
\frac {\mathrm{d} \mathbf {L}}{\mathrm{d} t} = 0
$$

$$
\text {or} \quad \mathbf {L} = \text {constant}.\tag{6.29a}
$$

Thus, if the total external torque on a system of particles is zero, then the total angular momentum of the system is conserved, i.e. remains constant. Eq. (6.29a) is equivalent to three scalar equations,

$$
\left| L _ {x} = K _ {1}, L _ {v} = K _ {2} \text {and} L _ {z} = K _ {3} \right.\tag{6.29 b}
$$

Here $K_{1}, K_{2}$ and $K_{3}$ are constants; $L_{x}, L_{y}$ and $L_{z}$ are the components of the total angular momentum vector $\mathbf{L}$ along the $x, y$ and $z$ axes respectively. The statement that the total angular momentum is conserved means that each of these three components is conserved.

Eq. (6.29a) is the rotational analogue of Eq. (6.18a), i.e. the conservation law of the total linear momentum for a system of particles. Like Eq. (6.18a), it has applications in many practical situations. We shall look at a few of the interesting applications later on in this chapter.

Example 6.5 Find the torque of a force $7\tilde{\mathbf{i}} + 3\tilde{\mathbf{j}} - 5\tilde{\mathbf{k}}$ about the origin. The force acts on a particle whose position vector is $\tilde{\mathbf{i}} - \tilde{\mathbf{j}} + \tilde{\mathbf{k}}$.

Answer Here $\mathbf{r} = \hat{\mathbf{i}} -\hat{\mathbf{j}} +\hat{\mathbf{k}}$

and $\mathbf{F} = 7\mathbf{i} + 3\mathbf{j} - 5\mathbf{k}$.

We shall use the determinant rule to find the torque  $\tau = r \times F$

$$
\tau = \left| \begin{array}{c c c} \hat {\mathbf {i}} & \hat {\mathbf {j}} & \hat {\mathbf {k}} \\ 1 & - 1 & 1 \\ 7 & 3 & - 5 \end{array} \right| = (5 - 3) \hat {\mathbf {i}} - (- 5 - 7) \hat {\mathbf {j}} + (3 - (- 7)) \hat {\mathbf {k}}
$$

$$
\text {or} \tau = 2 \hat {\mathbf {i}} + 1 2 \hat {\mathbf {j}} + 1 0 \hat {\mathbf {k}}
$$

Example 6.6 Show that the angular momentum about any point of a single particle moving with constant velocity remains constant throughout the motion.

Reprint 2025-26

<!-- page 18 of 35 -->

SYSTEMS OF PARTICLES AND ROTATIONAL MOTION

109

Answer Let the particle with velocity v be at point P at some instant t. We want to calculate the angular momentum of the particle about an arbitrary point O.

![Image block](doc:bba3640/tier:standard/page:18/block:4)

The angular momentum is  $l = r \times m v$ . Its magnitude is  $m v r \sin \theta$ , where  $\theta$  is the angle between r and v as shown in Fig. 6.19. Although the particle changes position with time, the line of direction of v remains the same and hence  $O M = r \sin \theta$ . is a constant.

Further, the direction of 1 is perpendicular to the plane of r and v. It is into the page of the figure. This direction does not change with time.

Thus, 1 remains the same in magnitude and direction and is therefore conserved. Is there any external torque on the particle?

## 6.8 EQUILIBRIUM OF A RIGID BODY

We are now going to concentrate on the motion of rigid bodies rather than on the motion of general systems of particles.

We shall recapitulate what effect the external forces have on a rigid body. (Henceforth we shall omit the adjective ‘external’ because unless stated otherwise, we shall deal with only external forces and torques.) The forces change the translational state of the motion of the rigid body, i.e. they change its total linear momentum in accordance with Eq. (6.17). But this is not the only effect the forces have. The total torque on the body may not vanish. Such a torque changes the rotational state of motion of the rigid body, i.e. it changes the total angular momentum of the body in accordance with Eq. (6.28 b).

A rigid body is said to be in mechanical equilibrium, if both its linear momentum and angular momentum are not changing with time, or equivalently, the body has neither linear

acceleration nor angular acceleration. This means (1) the total force, i.e. the vector sum of the forces, on the rigid body is zero;

$$
\mathbf {F} _ {1} + \mathbf {F} _ {2} + \ldots + \mathbf {F} _ {n} = \sum_ {i = 1} ^ {n} \mathbf {F} _ {i} = \mathbf {0}\tag{6.30a}
$$

If the total force on the body is zero, then the total linear momentum of the body does not change with time. Eq. (6.30a) gives the condition for the translational equilibrium of the body.

(2) The total torque, i.e. the vector sum of the torques on the rigid body is zero,

$$
\boldsymbol {\tau} _ {1} + \boldsymbol {\tau} _ {2} + \dots + \boldsymbol {\tau} _ {n} = \sum_ {i = 1} ^ {n} \boldsymbol {\tau} _ {i} = \mathbf {0}\tag{6.30b}
$$

If the total torque on the rigid body is zero, the total angular momentum of the body does not change with time. Eq. (6.30 b) gives the condition for the rotational equilibrium of the body.

One may raise a question, whether the rotational equilibrium condition [Eq. 6.30(b)] remains valid, if the origin with respect to which the torques are taken is shifted. One can show that if the translational equilibrium condition [Eq. 6.30(a)] holds for a rigid body, then such a shift of origin does not matter, i.e. the rotational equilibrium condition is independent of the location of the origin about which the torques are taken. Example 6.7 gives a proof of this result in a special case of a couple, i.e. two forces acting on a rigid body in translational equilibrium. The generalisation of this result to n forces is left as an exercise.

Eq. (6.30a) and Eq. (6.30b), both, are vector equations. They are equivalent to three scalar equations each. Eq. (6.30a) corresponds to

$$
\sum_ {i = 1} ^ {n} F _ {i x} = 0, \sum_ {i = 1} ^ {n} F _ {i y} = 0 \text {and} \sum_ {i = 1} ^ {n} F _ {i z} = 0\tag{6.31a}
$$

where  $F_{ix}$ ,  $F_{iy}$  and  $F_{iz}$  are respectively the x, y and z components of the forces  $F_{i}$ . Similarly, Eq. (6.30b) is equivalent to three scalar equations

$$
\sum_ {i = 1} ^ {n} \tau_ {i x} = 0, \sum_ {i = 1} ^ {n} \tau_ {i y} = 0 \text {and} \sum_ {i = 1} ^ {n} \tau_ {i z} = 0\tag{6.31b}
$$

where $\tau_{ix},\tau_{iy}$ and $\tau_{iz}$ are respectively the $x,y$ and $z$ components of the torque $\pmb{\tau}_j$

Eq. (6.31a) and (6.31b) give six independent conditions to be satisfied for mechanical

Reprint 2025-26

<!-- page 19 of 35 -->

110

PHYSICS

equilibrium of a rigid body. In a number of problems all the forces acting on the body are coplanar. Then we need only three conditions to be satisfied for mechanical equilibrium. Two of these conditions correspond to translational equilibrium; the sum of the components of the forces along any two perpendicular axes in the plane must be zero. The third condition corresponds to rotational equilibrium. The sum of the components of the torques along any axis perpendicular to the plane of the forces must be zero.

The conditions of equilibrium of a rigid body may be compared with those for a particle, which we considered in earlier chapters. Since consideration of rotational motion does not apply to a particle, only the conditions for translational equilibrium (Eq. 6.30 a) apply to a particle. Thus, for equilibrium of a particle the vector sum of all the forces on it must be zero. Since all these forces act on the single particle, they must be concurrent. Equilibrium under concurrent forces was discussed in the earlier chapters.

A body may be in partial equilibrium, i.e., it may be in translational equilibrium and not in rotational equilibrium, or it may be in rotational equilibrium and not in translational equilibrium.

Consider a light (i.e. of negligible mass) rod (AB) as shown in Fig. 6.20(a). At the two ends (A and B) of which two parallel forces, both equal in magnitude and acting along same direction are applied perpendicular to the rod.

![Image block](doc:bba3640/tier:standard/page:19/block:7)

Let C be the midpoint of AB, CA = CB = a. the moment of the forces at A and B will both be equal in magnitude (aF), but opposite in sense as shown. The net moment on the rod will be zero. The system will be in rotational equilibrium, but it will not be in translational equilibrium;  $\sum F \neq 0$

![Image block](doc:bba3640/tier:standard/page:19/block:9)

Fig. 6.20 (b)

The force at B in Fig. 6.20(a) is reversed in Fig. 6.20(b). Thus, we have the same rod with two forces of equal magnitude but acting in opposite directions applied perpendicular to the rod, one at end A and the other at end B. Here the moments of both the forces are equal, but they are not opposite; they act in the same sense and cause anticlockwise rotation of the rod. The total force on the body is zero; so the body is in translational equilibrium; but it is not in rotational equilibrium. Although the rod is not fixed in any way, it undergoes pure rotation (i.e. rotation without translation).

A pair of forces of equal magnitude but acting in opposite directions with different lines of action is known as a couple or torque. A couple produces rotation without translation.

When we open the lid of a bottle by turning it, our fingers are applying a couple to the lid [Fig. 6.21(a)]. Another known example is a compass needle in the earth's magnetic field as shown in the Fig. 6.21(b). The earth's magnetic field exerts equal forces on the north and south poles. The force on the North Pole is towards the north, and the force on the South Pole is toward the south. Except when the needle points in the north-south direction; the two forces do not have the same line of action. Thus there is a couple acting on the needle due to the earth's magnetic field.

![Image block](doc:bba3640/tier:standard/page:19/block:14)

Fig. 6.21(a) Our fingers apply a couple to turn the lid.

Reprint 2025-26

<!-- page 20 of 35 -->

SYSTEMS OF PARTICLES AND ROTATIONAL MOTION

111

![Image block](doc:bba3640/tier:standard/page:20/block:3)

Fig. 6.21(b) The Earth's magnetic field exerts equal and opposite forces on the poles of a compass needle. These two forces form a couple.

Example 6.7 Show that moment of a couple does not depend on the point about which you take the moments.

Answer

![Image block](doc:bba3640/tier:standard/page:20/block:7)

Fig. 6.22

Consider a couple as shown in Fig. 6.22 acting on a rigid body. The forces $\mathbf{F}$ and -$\mathbf{F}$ act respectively at points B and A. These points have position vectors $\mathbf{r}_1$ and $\mathbf{r}_2$ with respect to origin O. Let us take the moments of the forces about the origin.

The moment of the couple = sum of the moments of the two forces making the couple

$$
= \mathbf {r} _ {1} \times (- \mathbf {F}) + \mathbf {r} _ {2} \times \mathbf {F}
$$

$$
= \mathbf {r} _ {2} \times \mathbf {F} - \mathbf {r} _ {1} \times \mathbf {F}
$$

$$
= (\bar {\mathbf {r}} _ {2} - \mathbf {r} _ {1}) \times \bar {\mathbf {F}}
$$

But $\mathbf{r}_1 + \mathbf{AB} = \mathbf{r}_2$, and hence $\mathbf{AB} = \mathbf{r}_2 - \mathbf{r}_1$.

The moment of the couple, therefore, is $\mathbf{AB} \times \mathbf{F}$.

Clearly this is independent of the origin, the point about which we took the moments of the forces.

## 6.8.1 Principle of moments

An ideal lever is essentially a light (i.e. of negligible mass) rod pivoted at a point along its

length. This point is called the fulcrum. A seesaw on the children's playground is a typical example of a lever. Two forces $F_{1}$ and $F_{2}$, parallel to each other and usually perpendicular to the lever, as shown here, act on the lever at distances $d_{1}$ and $d_{2}$ respectively from the fulcrum as shown in Fig. 6.23.

![Image block](doc:bba3640/tier:standard/page:20/block:20)

Fig. 6.23

The lever is a system in mechanical equilibrium. Let R be the reaction of the support at the fulcrum; R is directed opposite to the forces  $F_{1}$  and  $F_{2}$ . For translational equilibrium,

$$
R - F _ {1} - F _ {2} = 0\tag{i}
$$

For considering rotational equilibrium we take the moments about the fulcrum; the sum of moments must be zero,

$$
d _ {1} F _ {1} - d _ {2} F _ {2} = 0\tag{ii}
$$

Normally the anticlockwise (clockwise) moments are taken to be positive (negative). Note R acts at the fulcrum itself and has zero moment about the fulcrum.

In the case of the lever force $F_{1}$ is usually some weight to be lifted. It is called the load and its distance from the fulcrum $d_{1}$ is called the load arm. Force $F_{2}$ is the effort applied to lift the load; distance $d_{2}$ of the effort from the fulcrum is the effort arm.

Eq. (ii) can be written as

$$
d _ {1} F _ {1} = \mathrm{d} _ {2} F _ {2}\tag{6.32a}
$$

or load arm $\times$ load $=$ effort arm $\times$ effort

The above equation expresses the principle of moments for a lever. Incidentally the ratio  $F_{1}/F_{2}$  is called the Mechanical Advantage (M.A.);

$$
\mathrm{M.A.} = \frac {F _ {1}}{F _ {2}} = \frac {d _ {2}}{d _ {1}}\tag{6.32b}
$$

If the effort arm  $d_{2}$  is larger than the load arm, the mechanical advantage is greater than one. Mechanical advantage greater than one means that a small effort can be used to lift a large load. There are several examples of a lever around you besides the see-saw. The beam of a balance is a lever. Try to find more such

Reprint 2025-26

<!-- page 21 of 35 -->

112

PHYSICS

examples and identify the fulcrum, the effort and effort arm, and the load and the load arm of the lever in each case.

You may easily show that the principle of moment holds even when the parallel forces  $F_{1}$  and  $F_{2}$  are not perpendicular, but act at some angle, to the lever.

## 6.8.2 Centre of gravity

Many of you may have the experience of balancing your notebook on the tip of a finger. Figure 6.24 illustrates a similar experiment that you can easily perform. Take an irregular-shaped cardboard having mass M and a narrow tipped object like a pencil. You can locate by trial and error a point G on the cardboard where it can be balanced on the tip of the pencil. (The cardboard remains horizontal in this position.) This point of balance is the centre of gravity (CG) of the cardboard. The tip of the pencil provides a vertically upward force due to which the cardboard is in mechanical equilibrium. As shown in the Fig. 6.24, the reaction of the tip is equal and opposite to Mg and hence the cardboard is in translational equilibrium. It is also in rotational equilibrium; if it were not so, due to the unbalanced torque it would tilt and fall. There are torques on the card board due to the forces of gravity like  $m_{1}g$ ,  $m_{2}g$  .... etc, acting on the individual particles that make up the cardboard.

![Image block](doc:bba3640/tier:standard/page:21/block:7)

Fig. 6.24 Balancing a cardboard on the tip of a pencil. The point of support, G, is the centre of gravity.

The CG of the cardboard is so located that the total torque on it due to the forces $m_1 \mathbf{g}$, $m_2 \mathbf{g}$ .... etc. is zero.

If  $r_{i}$  is the position vector of the ith particle of an extended body with respect to its CG, then the torque about the CG, due to the force of gravity on the particle is  $\tau_{i} = r_{i} \times m_{i} g$ . The total gravitational torque about the CG is zero, i.e.

$$
\boldsymbol {\tau} _ {g} = \sum \boldsymbol {\tau} _ {i} = \sum \mathbf {r} _ {i} \times m _ {i} \mathbf {g} = \mathbf {0}\tag{6.33}
$$

We may therefore, define the CG of a body as that point where the total gravitational torque on the body is zero.

We notice that in Eq. (6.33), $\mathbf{g}$ is the same for all particles, and hence it comes out of the summation. This gives, since $\mathbf{g}$ is non-zero,

$\sum m_{i}\mathbf{r}_{i} = \mathbf{0}$. Remember that the position vectors $(\mathbf{r}_j)$ are taken with respect to the CG. Now, in accordance with the reasoning given below Eq. (6.4a) in Sec. 6.2, if the sum is zero, the origin must be the centre of mass of the body. Thus, the centre of gravity of the body coincides with the centre of mass in uniform gravity or gravity-

![Image block](doc:bba3640/tier:standard/page:21/block:15)

Fig. 6.25 Determining the centre of gravity of a body of irregular shape. The centre of gravity G lies on the vertical  $AA_{1}$  through the point of suspension of the body A.

Reprint 2025-26

<!-- page 22 of 35 -->

SYSTEMS OF PARTICLES AND ROTATIONAL MOTION

113

free space. We note that this is true because the body being small, g does not vary from one point of the body to the other. If the body is so extended that g varies from part to part of the body, then the centre of gravity and centre of mass will not coincide. Basically, the two are different concepts. The centre of mass has nothing to do with gravity. It depends only on the distribution of mass of the body.

In Sec. 6.2 we found out the position of the centre of mass of several regular, homogeneous objects. Obviously the method used there gives us also the centre of gravity of these bodies, if they are small enough.

Figure 6.25 illustrates another way of determining the CG of an irregular shaped body like a cardboard. If you suspend the body from some point like A, the vertical line through A passes through the CG. We mark the vertical $\mathrm{AA}_1$. We then suspend the body through other points like B and C. The intersection of the verticals gives the CG. Explain why the method works. Since the body is small enough, the method allows us to determine also its centre of mass.

Example 6.8 A metal bar 70 cm long and 4.00 kg in mass supported on two knife-edges placed 10 cm from each end. A 6.00 kg load is suspended at 30 cm from one end. Find the reactions at the knife-edges. (Assume the bar to be of uniform cross section and homogeneous.)

![Image block](doc:bba3640/tier:standard/page:22/block:7)

Figure 6.26 shows the rod AB, the positions of the knife edges  $K_{1}$  and  $K_{2}$ , the centre of gravity of the rod at G and the suspended load at P.

Note the weight of the rod W acts at its centre of gravity G. The rod is uniform in cross section and homogeneous; hence G is at the centre of the rod; AB = 70 cm. AG = 35 cm, AP

$= 30 \mathrm{~cm}, \mathrm{PG} = 5 \mathrm{~cm}, \mathrm{AK}_{1} = \mathrm{BK}_{2} = 10 \mathrm{~cm}$ and $\mathrm{K}_{1} \mathrm{G} = \mathrm{K}_{2} \mathrm{G} = 25 \mathrm{~cm}$. Also, $W =$ weight of the rod $= 4.00 \mathrm{~kg}$ and $W_{1} =$ suspended load $= 6.00 \mathrm{~kg}; R_{1}$ and $R_{2}$ are the normal reactions of the support at the knife edges.

For translational equilibrium of the rod,

$$
R _ {1} + R _ {2} - W _ {1} - W = 0\tag{i}
$$

Note $W_{1}$ and $W$ act vertically down and $R_{1}$ and $R_{2}$ act vertically up.

For considering rotational equilibrium, we take moments of the forces. A convenient point to take moments about is G. The moments of  $R_{2}$  and  $W_{1}$  are anticlockwise (+ve), whereas the moment of  $R_{1}$  is clockwise (-ve).

For rotational equilibrium,

$$
- R _ {1} \left(\mathrm{K} _ {1} \mathrm{G}\right) + W _ {1} (\mathrm{PG}) + R _ {2} \left(\mathrm{K} _ {2} \mathrm{G}\right) = 0\tag{ii}
$$

It is given that  $W = 4.00g N$  and  $W_{1} = 6.00g N$ , where g = acceleration due to gravity. We take  $g = 9.8 m/s^{2}$ .

With numerical values inserted, from (i)

$$
\begin{array}{r l} & R _ {1} + R _ {2} - 4. 0 0 g - 6. 0 0 g = 0 \\ & \text {or} R _ {1} + R _ {2} = 1 0. 0 0 g \mathrm{N} \\ & \quad = 9 8. 0 0 \mathrm{N} \end{array}\tag{iii}
$$

From (ii), $-0.25 R_{1} + 0.05 W_{1} + 0.25 R_{2} = 0$ or $R_{1} - R_{2} = 1.2g\mathrm{N} = 11.76\mathrm{N}$ (iv) From (iii) and (iv), $R_{1} = 54.88\mathrm{N}$,

$$
R _ {2} = 4 3. 1 2 \mathrm{N}
$$

Thus the reactions of the support are about 55 N at  $K_{1}$  and 43 N at  $K_{2}$ .

Example 6.9 A 3m long ladder weighing 20 kg leans on a frictionless wall. Its feet rest on the floor 1 m from the wall as shown in Fig.6.27. Find the reaction forces of the wall and the floor.

Answer

![Image block](doc:bba3640/tier:standard/page:22/block:25)

Fig. 6.27

Reprint 2025-26

<!-- page 23 of 35 -->

114

PHYSICS

The ladder AB is 3 m long, its foot A is at distance AC = 1 m from the wall. From Pythagoras theorem, BC =  $2\sqrt{2}$  m. The forces on the ladder are its weight W acting at its centre of gravity D, reaction forces  $F_{1}$  and  $F_{2}$  of the wall and the floor respectively. Force  $F_{1}$  is perpendicular to the wall, since the wall is frictionless. Force  $F_{2}$  is resolved into two components, the normal reaction N and the force of friction F. Note that F prevents the ladder from sliding away from the wall and is therefore directed toward the wall.

For translational equilibrium, taking the forces in the vertical direction,

$$
N - W = 0\tag{i}
$$

Taking the forces in the horizontal direction,

$$
F - F _ {1} = 0\tag{ii}
$$

For rotational equilibrium, taking the moments of the forces about A,

$$
2 \sqrt {2} F _ {1} - (1 / 2) W = 0\tag{iii}
$$

$$
\begin{array}{l l} \text {Now} & W = 2 0 \mathrm{g} = 2 0 \quad 9. 8 \mathrm{N} = 1 9 6. 0 \mathrm{N} \\ \text {From (i)} & N = 1 9 6. 0 \mathrm{N} \end{array}
$$

From (iii) $F_{1} = W / 4\sqrt{2} = 196.0 / 4\sqrt{2} = 34.6\mathrm{N}$

From (ii) $F = F_{1} = 34.6\mathrm{N}$

$$
F _ {2} = \sqrt {F ^ {2} + N ^ {2}} = 1 9 9. 0 \mathrm{N}
$$

The force $F_{2}$ makes an angle $\alpha$ with the horizontal,

$$
\tan \alpha = N / F = 4 \sqrt {2}, \alpha = \tan^ {- 1} (4 \sqrt {2}) \approx 80^\circ
$$

## 6.9 MOMENT OF INERTIA

We have already mentioned that we are developing the study of rotational motion parallel to the study of translational motion with which we are familiar. We have yet to answer one major question in this connection. What is the analogue of mass in rotational motion? We shall attempt to answer this question in the present section. To keep the discussion simple, we shall consider rotation about a fixed axis only. Let us try to get an expression for the kinetic energy of a rotating body. We know that for a body rotating about a fixed axis, each particle of the body moves in a circle with linear velocity given by Eq. (6.19). (Refer to Fig. 6.16). For a particle at a distance

from the axis, the linear velocity is  $v_{i} = r_{i}\omega$ . The kinetic energy of motion of this particle is

$$
k _ {i} = \frac {1}{2} m _ {i} v _ {i} ^ {2} = \frac {1}{2} m _ {i} r _ {i} ^ {2} \omega^ {2}
$$

where  $m_{i}$  is the mass of the particle. The total kinetic energy K of the body is then given by the sum of the kinetic energies of individual particles,

$$
K = \sum_ {i = 1} ^ {n} k _ {i} = \frac {1}{2} \sum_ {i = 1} ^ {n} (m _ {i} r _ {i} ^ {2} \omega^ {2})
$$

Here n is the number of particles in the body. Note  $\omega$  is the same for all particles. Hence, taking  $\omega$  out of the sum,

$$
K = \frac {1}{2} \omega^ {2} (\sum_ {i = 1} ^ {n} m _ {i} r _ {i} ^ {2})
$$

We define a new parameter characterising the rigid body, called the moment of inertia I, given by

$$
I = \sum_ {i = 1} ^ {n} m _ {i} r _ {i} ^ {2}\tag{6.34}
$$

With this definition,

$$
K = \frac {1}{2} I \omega^ {2}\tag{6.35}
$$

Note that the parameter I is independent of the magnitude of the angular velocity. It is a characteristic of the rigid body and the axis about which it rotates.

Compare Eq. (6.35) for the kinetic energy of a rotating body with the expression for the kinetic energy of a body in linear (translational) motion,

$$
K = \frac {1}{2} m v ^ {2}
$$

Here, m is the mass of the body and v is its velocity. We have already noted the analogy between angular velocity  $\omega$  (in respect of rotational motion about a fixed axis) and linear velocity v (in respect of linear motion). It is then evident that the parameter, moment of inertia I, is the desired rotational analogue of mass in linear motion. In rotation (about a fixed axis), the moment of inertia plays a similar role as mass does in linear motion.

We now apply the definition Eq. (6.34), to calculate the moment of inertia in two simple cases.

Reprint 2025-26

<!-- page 24 of 35 -->

SYSTEMS OF PARTICLES AND ROTATIONAL MOTION

115

(a) Consider a thin ring of radius R and mass M, rotating in its own plane around its centre with angular velocity  $\omega$ . Each mass element of the ring is at a distance R from the axis, and moves with a speed  $R\omega$ . The kinetic energy is therefore,

$$
K = \frac {1}{2} M \upsilon^ {2} = \frac {1}{2} M R ^ {2} \omega^ {2}
$$

Comparing with Eq. (6.35) we get  $I = MR^{2}$  for the ring.

![Image block](doc:bba3640/tier:standard/page:24/block:6)

Fig. 6.28 A light rod of length 1 with a pair of masses rotating about an axis through the centre of mass of the system and perpendicular to the rod. The total mass of the system is M.

(b) Next, take a rigid rod of negligible mass of length of length $I$ with a pair of small masses, rotating about an axis through the centre of mass perpendicular to the rod (Fig. 6.28). Each mass $M/2$ is at a distance $I/2$ from the axis. The moment of inertia of the masses is therefore given by

$$
(M / 2) (I / 2) ^ {2} + (M / 2) (I / 2) ^ {2}
$$

Thus, for the pair of masses, rotating about the axis through the centre of mass perpendicular to the rod

$$
I = M I ^ {2} / 4
$$

Table 6.1 simply gives the moment of inertia of various familiar regular shaped bodies about specific axes. (The derivations of these expressions are beyond the scope of this textbook and you will study them in higher classes.)

As the mass of a body resists a change in its state of linear motion, it is a measure of its inertia in linear motion. Similarly, as the moment of inertia about a given axis of rotation resists a

change in its rotational motion, it can be regarded as a measure of rotational inertia of the body; it is a measure of the way in which different parts of the body are distributed at different distances from the axis. Unlike the mass of a body, the moment of inertia is not a fixed quantity but depends on distribution of mass about the axis of rotation, and the orientation and position of the axis of rotation with respect to the body as a whole. As a measure of the way in which the mass of a rotating rigid body is distributed with respect to the axis of rotation, we can define a new parameter, the radius of gyration. It is related to the moment of inertia and the total mass of the body.

Notice from the Table 6.1 that in all cases, we can write  $I = Mk^{2}$ , where k has the dimension of length. For a rod, about the perpendicular axis at its midpoint,  $k^{2} = L^{2}/12$ , i.e.  $k = L/\sqrt{12}$ . Similarly, k = R/2 for the circular disc about its diameter. The length k is a geometric property of the body and axis of rotation. It is called the radius of gyration. The radius of gyration of a body about an axis may be defined as the distance from the axis of a mass point whose mass is equal to the mass of the whole body and whose moment of inertia is equal to the moment of inertia of the body about the axis.

Thus, the moment of inertia of a rigid body depends on the mass of the body, its shape and size; distribution of mass about the axis of rotation, and the position and orientation of the axis of rotation.

From the definition, Eq. (6.34), we can infer that the dimensions of moments of inertia are  $ML^{2}$  and its SI units are kg m $^{2}$ .

The property of this extremely important quantity I, as a measure of rotational inertia of the body, has been put to a great practical use. The machines, such as steam engine and the automobile engine, etc., that produce rotational motion have a disc with a large moment of inertia, called a flywheel. Because of its large moment of inertia, the flywheel resists the sudden increase or decrease of the speed of the vehicle. It allows a gradual change in the speed and prevents jerky motions, thereby ensuring a smooth ride for the passengers on the vehicle.

Reprint 2025-26

<!-- page 25 of 35 -->

116

PHYSICS

Table 6.1 Moments of inertia of some regular shaped bodies about specific axes

| Z | Body | Axis | Figure | I |
| --- | --- | --- | --- | --- |
| (1) | Thin circular ring, radius R | Perpendicular to plane, at centre |  | $MR^2$ |
| (2) | Thin circular ring, radius R | Diameter |  | $MR^2/2$ |
| (3) | Thin rod, length L | Perpendicular to rod, at mid point |  | $ML^2/12$ |
| (4) | Circular disc, radius R | Perpendicular to disc at centre |  | $MR^2/2$ |
| (5) | Circular disc, radius R | Diameter |  | $MR^2/4$ |
| (6) | Hollow cylinder, radius R | Axis of cylinder |  | $MR^2$ |
| (7) | Solid cylinder, radius R | Axis of cylinder |  | $MR^2/2$ |
| (8) | Solid sphere, radius R | Diameter |  | $2MR^2/5$ |

## 6.10 KINEMATICS OF ROTATIONAL MOTION ABOUT A FIXED AXIS

We have already indicated the analogy between rotational motion and translational motion. For example, the angular velocity $\omega$ plays the same role in rotation as the linear velocity $\nu$ in

translation. We wish to take this analogy further. In doing so we shall restrict the discussion only to rotation about fixed axis. This case of motion involves only one degree of freedom, i.e., needs only one independent variable to describe the motion. This in translation corresponds to linear

Reprint 2025-26

<!-- page 26 of 35 -->

SYSTEMS OF PARTICLES AND ROTATIONAL MOTION

117

motion. This section is limited only to kinematics. We shall turn to dynamics in later sections.

We recall that for specifying the angular displacement of the rotating body we take any particle like P (Fig.6.29) of the body. Its angular displacement  $\theta$  in the plane it moves is the angular displacement of the whole body;  $\theta$  is measured from a fixed direction in the plane of motion of P, which we take to be the  $x'$ -axis, chosen parallel to the x-axis. Note, as shown, the axis of rotation is the z-axis and the plane of the motion of the particle is the x-y plane. Fig. 6.29 also shows  $\theta_{0}$ , the angular displacement at t=0.

We also recall that the angular velocity is the time rate of change of angular displacement,  $\omega = d\theta/dt$ . Note since the axis of rotation is fixed, there is no need to treat angular velocity as a vector. Further, the angular acceleration,  $\alpha = d\omega/dt$ .

The kinematical quantities in rotational motion, angular displacement ( $\theta$ ), angular velocity ( $\omega$ ) and angular acceleration ( $\alpha$ ) respectively are analogous to kinematic quantities in linear motion, displacement (x), velocity (v) and acceleration (a). We know the kinematical equations of linear motion with uniform (i.e. constant) acceleration:

$$
v = v _ {0} + a t\tag{a}
$$

$$
x = x _ {0} + v _ {0} t + \frac {1}{2} a t ^ {2}
$$

$$
\upsilon^ {2} = \upsilon_ {0} ^ {2} + 2 a x
$$

![Image block](doc:bba3640/tier:standard/page:26/block:10)

(b)

where $x_0 =$ initial displacement and $v_0 =$ initial velocity. The word 'initial' refers to values of the quantities at $t = 0$

The corresponding kinematic equations for rotational motion with uniform angular acceleration are:

$$
\omega = \omega_ {0} + \alpha t\tag{6.36}
$$

$$
\theta = \theta_ {0} + \omega_ {0} t + \frac {1}{2} \alpha t ^ {2}\tag{6.37}
$$

$$
\text {and} \omega^ {2} = \omega_ {0} ^ {2} + 2 \alpha (\theta - \theta_ {0})\tag{6.38}
$$

where  $\theta_{0}=$  initial angular displacement of the rotating body, and  $\omega_{0}=$  initial angular velocity of the body.

![Image block](doc:bba3640/tier:standard/page:26/block:18)

Fig.6.29 Specifying the angular position of a rigid body.

Example 6.10 Obtain Eq. (6.36) from first principles.

Answer The angular acceleration is uniform, hence

$$
\frac {\mathrm{d} \omega}{\mathrm{d} t} = \alpha = \text {constant}\tag{i}
$$

Integrating this equation,

$$
\omega = \int \alpha \mathrm{d} t + c
$$

$= \alpha t + c$ (as $\alpha$ is constant)

$$
\text {At} t = O, \omega = \omega_ {0} (\text {given})
$$

From (i) we get at $t = 0$, $\omega = c = \omega_0$

Thus, $\omega = \alpha t + \omega_0$ as required.

With the definition of  $\omega = d\theta/dt$  we may integrate Eq. (6.36) to get Eq. (6.37). This derivation and the derivation of Eq. (6.38) is left as an exercise.

Example 6.11 The angular speed of a motor wheel is increased from 1200 rpm to 3120 rpm in 16 seconds. (i) What is its angular acceleration, assuming the acceleration to be uniform? (ii) How many revolutions does the engine make during this time?

## Answer

(i) We shall use $\omega = \omega_0 + \alpha t$

$\omega_0 =$ initial angular speed in rad/s

Reprint 2025-26

<!-- page 27 of 35 -->

118

PHYSICS

$= 2\pi \times$ angular speed in rev/s

$$
\left| \begin{array}{l} = \frac {2 \pi \times \text {angular speed in rev / min}}{6 0 \mathrm{s} / \mathrm{min}} \\ = \frac {2 \pi \times 1 2 0 0}{6 0} \mathrm{rad/s} \\ = 4 0 \pi \mathrm{rad/s} \\ \text {Similarly} \omega = \text {final angular speed in rad / s} \\ = \frac {2 \pi \times 3 1 2 0}{6 0} \mathrm{rad/s} \\ = 2 \pi \times 5 2 \mathrm{rad/s} \\ = 1 0 4 \pi \mathrm{rad/s} \end{array} \right|
$$

∴ Angular acceleration

$$
\alpha = \frac {\omega - \omega_ {0}}{t} \quad = 4 \pi \mathrm{rad/s} ^ {2}
$$

The angular acceleration of the engine $= 4\pi \mathrm{rad} / \mathrm{s}^2$

(ii) The angular displacement in time $t$ is given by

$$
\begin{array}{c} \theta = \omega_ {0} t + \frac {1}{2} \alpha t ^ {2} \\ = (4 0 \pi \times 1 6 + \frac {1}{2} \times 4 \pi \times 1 6 ^ {2}) \text {rad} \\ = (6 4 0 \pi + 5 1 2 \pi) \text {rad} \\ = 1 1 5 2 \pi \text {rad} \end{array}
$$

Number of revolutions =  $\frac{1152\pi}{2\pi}=576$

## 6.11 DYNAMICS OF ROTATIONAL MOTION ABOUT A FIXED AXIS

Table 6.2 lists quantities associated with linear motion and their analogues in rotational motion. We have already compared kinematics of the two motions. Also, we know that in rotational motion moment of inertia and torque play the same role as mass and force respectively in linear motion. Given this we should be able to guess what the other analogues indicated in the table are. For example, we know that in linear motion, work done is given by F dx, in rotational motion about a fixed axis it should be  $\tau d\theta$ , since we already know the correspondence  $dx \rightarrow d\theta$  and  $F \rightarrow \tau$ .

It is, however, necessary that these correspondences are established on sound dynamical considerations. This is what we now turn to.

Before we begin, we note a simplification that arises in the case of rotational motion about a fixed axis. Since the axis is fixed, only those components of torques, which are along the direction of the fixed axis need to be considered in our discussion. Only these components can cause the body to rotate about the axis. A component of the torque perpendicular to the axis of rotation will tend to turn the axis from its position. We specifically assume that there will arise necessary forces of constraint to cancel the effect of the perpendicular components of the (external) torques, so that the fixed position of the axis will be maintained. The perpendicular components of the torques, therefore need not be taken into account. This means that for our calculation of torques on a rigid body:

(1) We need to consider only those forces that lie in planes perpendicular to the axis. Forces which are parallel to the axis will give torques perpendicular to the axis and need not be taken into account.

(2) We need to consider only those components of the position vectors which are perpendicular to the axis. Components of position vectors along the axis will result in torques perpendicular to the axis and need not be taken into account.

Work done by a torque

![Image block](doc:bba3640/tier:standard/page:27/block:18)

Fig. 6.30 Work done by a force $\mathbf{F}_{1}$ acting on a particle of a body rotating about a fixed axis; the particle describes a circular path with centre $C$ on the axis; arc $\mathrm{P}_1\mathrm{P}'_1(\mathrm{ds}_1)$ gives the displacement of the particle.

Reprint 2025-26

<!-- page 28 of 35 -->

SYSTEMS OF PARTICLES AND ROTATIONAL MOTION

119

Table 6.2 Comparison of Translational and Rotational Motion

<table><tr><td colspan="2">Linear Motion</td><td>Rotational Motion about a Fixed Axis</td></tr><tr><td>1</td><td>Displacement x</td><td>Angular displacement  $\theta$ </td></tr><tr><td>2</td><td>Velocity  $v = dx/dt$ </td><td>Angular velocity  $\omega = d\theta/dt$ </td></tr><tr><td>3</td><td>Acceleration  $a = dv/dt$ </td><td>Angular acceleration  $\alpha = d\omega/dt$ </td></tr><tr><td>4</td><td>Mass M</td><td>Moment of inertia I</td></tr><tr><td>5</td><td>Force  $F = Ma$ </td><td>Torque  $\tau = I \alpha$ </td></tr><tr><td>6</td><td>Work  $dW = F ds$ </td><td>Work  $W = \tau d\theta$ </td></tr><tr><td>7</td><td>Kinetic energy  $K = Mv^{2}/2$ </td><td>Kinetic energy  $K = I\omega^{2}/2$ </td></tr><tr><td>8</td><td>Power  $P = F v$ </td><td>Power  $P = \tau\omega$ </td></tr><tr><td>9</td><td>Linear momentum  $p = Mv$ </td><td>Angular momentum  $L = I\omega$ </td></tr></table>

Figure 6.30 shows a cross-section of a rigid body rotating about a fixed axis, which is taken as the z-axis (perpendicular to the plane of the page; see Fig. 6.29). As said above we need to consider only those forces which lie in planes perpendicular to the axis. Let  $F_{1}$  be one such typical force acting as shown on a particle of the body at point  $P_{1}$  with its line of action in a plane perpendicular to the axis. For convenience we call this to be the  $x^{\prime}-y^{\prime}$  plane (coincident with the plane of the page). The particle at  $P_{1}$  describes a circular path of radius  $r_{1}$  with centre C on the axis;  $CP_{1}=r_{1}$ .

In time $\Delta t$, the point moves to the position $P_1'$. The displacement of the particle $ds_1$, therefore, has magnitude $ds_1 = r_1d\theta$ and direction tangential at $P_1$ to the circular path as shown. Here $d\theta$ is the angular displacement of the particle, $d\theta = \angle P_1CP_1'$. The work done by the force on the particle is

$\mathrm{d}W_{1} = \mathbf{F}_{1}$. $\mathrm{d}\mathbf{s}_{1} = F_{1}\mathrm{d}s_{1}\cos \phi_{1} = F_{1}(r_{1}\mathrm{d}\theta)\sin \alpha_{1}$ where $\phi_{1}$ is the angle between $\mathbf{F}_{1}$ and the tangent at $P_{1}$, and $\alpha_{1}$ is the angle between $\mathbf{F}_{1}$ and the radius vector $\mathbf{OP}_{1}$; $\phi_{1} + \alpha_{1} = 90^{\circ}$.

The torque due to $\mathbf{F}_1$ about the origin is $\mathbf{OP}_1 \times \mathbf{F}_1$. Now $\mathbf{OP}_1 = \mathbf{OC} + \mathbf{OP}_1$. [Refer to Fig. 6.17(b).] Since $\mathbf{OC}$ is along the axis, the torque resulting from it is excluded from our consideration. The effective torque due to $\mathbf{F}_1$ is $\boldsymbol{\tau}_1 = \mathbf{CP} \times \mathbf{F}_1$; it is directed along the axis of rotation and has a magnitude $\tau_1 = r_1 F_1 \sin \alpha$, Therefore,

$$
\mathrm{d} W _ {1} = \tau_ {1} \mathrm{d} \theta
$$

If there are more than one forces acting on the body, the work done by all of them can be added to give the total work done on the body. Denoting the magnitudes of the torques due to the different forces as  $\tau_{1}$ ,  $\tau_{2}$ , ... etc,

$$
\mathrm{d} W = (\tau_ {1} + \tau_ {2} + \dots) \mathrm{d} \theta
$$

Remember, the forces giving rise to the torques act on different particles, but the angular displacement  $d\theta$  is the same for all particles. Since all the torques considered are parallel to the fixed axis, the magnitude  $\tau$  of the total torque is just the algebraic sum of the magnitudes of the torques, i.e.,  $\tau = \tau_{1} + \tau_{2} + \ldots$ . We, therefore, have

$$
\mathrm{d} W = \tau \mathrm{d} \theta\tag{6.39}
$$

This expression gives the work done by the total (external) torque  $\tau$  which acts on the body rotating about a fixed axis. Its similarity with the corresponding expression

$$
\mathrm{d} W = F \mathrm{d} s
$$

for linear (translational) motion is obvious.

Dividing both sides of Eq. (6.39) by dt gives

$$
P = \frac {\mathrm{d} W}{\mathrm{d} t} = \tau \frac {\mathrm{d} \theta}{\mathrm{d} t} = \tau \omega
$$

$$
\text {or} P = \tau \omega\tag{6.40}
$$

This is the instantaneous power. Compare this expression for power in the case of rotational motion about a fixed axis with that of power in the case of linear motion,

$$
P = F v
$$

In a perfectly rigid body there is no internal motion. The work done by external torques is

Reprint 2025-26

<!-- page 29 of 35 -->

120

PHYSICS

therefore, not dissipated and goes on to increase the kinetic energy of the body. The rate at which work is done on the body is given by Eq. (6.40). This is to be equated to the rate at which kinetic energy increases. The rate of increase of kinetic energy is

$$
\frac {\mathrm{d}}{\mathrm{d} t} \left(\frac {I \omega^ {2}}{2}\right) = I \frac {(2 \omega)}{2} \frac {\mathrm{d} \omega}{\mathrm{d} t}
$$

We assume that the moment of inertia does not change with time. This means that the mass of the body does not change, the body remains rigid and also the axis does not change its position with respect to the body.

Since $\alpha = \mathrm{d}\omega /\mathrm{d}t$ , we get

$$
\frac {\mathrm{d}}{\mathrm{d} t} \left(\frac {I \omega^ {2}}{2}\right) = I \omega \alpha
$$

Equating rates of work done and of increase in kinetic energy,

$$
\tau \omega = I \omega \alpha
$$

$$
\tau = I \alpha\tag{6.41}
$$

Eq. (6.41) is similar to Newton's second law for linear motion expressed symbolically as

$$
F = m a
$$

Just as force produces acceleration, torque produces angular acceleration in a body. The angular acceleration is directly proportional to the applied torque and is inversely proportional to the moment of inertia of the body. In this respect, Eq.(6.41) can be called Newton's second law for rotational motion about a fixed axis.

Example 6.12 A cord of negligible mass is wound round the rim of a fly wheel of mass 20 kg and radius 20 cm. A steady pull of 25 N is applied on the cord as shown in Fig. 6.31. The flywheel is mounted on a horizontal axle with frictionless bearings.

(a) Compute the angular acceleration of the wheel.

(b) Find the work done by the pull, when $2\mathrm{m}$ of the cord is unwound.

(c) Find also the kinetic energy of the wheel at this point. Assume that the wheel starts from rest.

(d) Compare answers to parts (b) and (c).

Answer

![Image block](doc:bba3640/tier:standard/page:29/block:20)

$$
\text {Fig. 6.31}
$$

(a) We use $I\alpha = \tau$

the torque $\tau = FR$ $= 25\times 0.20\mathrm{Nm}$ (as $R = 0.20\mathrm{m}$) $= 5.0\mathrm{Nm}$

$I =$ Moment of inertia of flywheel about its

$$
\text {axis} = \frac {M R ^ {2}}{2}
$$

$$
\frac {2 0 . 0 \times (0 . 2) ^ {2}}{2} = 0. 4 \mathrm{kgm} ^ {2}
$$

$\alpha =$ angular acceleration

$$
= 5. 0 \mathrm{Nm} / 0. 4 \mathrm{kgm} ^ {2} = 1 2. 5 \mathrm{s} ^ {- 2}
$$

(b) Work done by the pull unwinding 2m of the cord

$$
= 25\ \text{N} \times 2\text{m} = 50\ \text{J}
$$

(c) Let $\omega$ be the final angular velocity. The kinetic energy gained $= \frac{1}{2} I\omega^2$,

since the wheel starts from rest. Now,

$$
\omega^ {2} = \omega_ {0} ^ {2} + 2 \alpha \theta , \quad \omega_ {0} = 0
$$

The angular displacement $\theta =$ length of unwound string / radius of wheel $= 2\mathrm{m} / 0.2\mathrm{m} = 10$ rad

$$
\omega^ {2} = 2 \times 1 2. 5 \times 1 0. 0 = 2 5 0 (\mathrm{rad/s}) ^ {2}
$$

$$
\therefore \mathrm{K.E.gained} = \frac{1}{2}\times 0.4\times 250 = 50\mathrm{J}
$$

(d) The answers are the same, i.e. the kinetic energy gained by the wheel = work done by the force. There is no loss of energy due to friction.

Reprint 2025-26

<!-- page 30 of 35 -->

SYSTEMS OF PARTICLES AND ROTATIONAL MOTION

121

## 6.12 ANGULAR MOMENTUM IN CASE OF ROTATION ABOUT A FIXED AXIS

We have studied in section 6.7, the angular momentum of a system of particles. We already know from there that the time rate of total angular momentum of a system of particles about a point is equal to the total external torque on the system taken about the same point. When the total external torque is zero, the total angular momentum of the system is conserved.

We now wish to study the angular momentum in the special case of rotation about a fixed axis. The general expression for the total angular momentum of the system of n particles is

$$
\mathbf {L} = \sum_ {i = 1} ^ {N} \mathbf {r} _ {i} \times \mathbf {p} _ {i}\tag{6.25b}
$$

We first consider the angular momentum of a typical particle of the rotating rigid body. We then sum up the contributions of individual particles to get L of the whole body.

For a typical particle  $l = r \times p$ . As seen in the last section  $r = OP = OC + CP$  [Fig. 6.17(b)]. With  $p = m v$ ,

$$
\boldsymbol {l} = (\boldsymbol {\mathbf {O C}} \times m \boldsymbol {\mathbf {v}}) + (\boldsymbol {\mathbf {C P}} \times m \boldsymbol {\mathbf {v}})
$$

The magnitude of the linear velocity $\mathbf{v}$ of the particle at P is given by $v = \omega r_{\perp}$ where $r_{\perp}$ is the length of CP or the perpendicular distance of P from the axis of rotation. Further, $\mathbf{v}$ is tangential at P to the circle which the particle describes. Using the right-hand rule one can check that $\mathbf{CP} \times \mathbf{v}$ is parallel to the fixed axis. The unit vector along the fixed axis (chosen as the $z$-axis) is $\hat{\mathbf{k}}$. Hence

$$
\begin{array}{l} \mathbf {C P} \times m \mathbf {v} = r _ {\perp} (m v) \hat {\mathbf {k}} \\ = m r _ {\perp} ^ {2} \omega \hat {\mathbf {k}} \quad (\text {since} v = \omega r _ {\perp}) \end{array}
$$

Similarly, we can check that  $OC \times v$  is perpendicular to the fixed axis. Let us denote the part of l along the fixed axis (i.e. the z-axis) by  $l_{z}$ , then

$$
\boldsymbol {l} _ {z} = \mathbf {C P} \times m \mathbf {v} = m r _ {\perp} ^ {2} \omega \hat {\mathbf {k}}
$$

and $\pmb{l} = \pmb{l}_{z} + \mathbf{O}\mathbf{C}\times m\mathbf{v}$

We note that  $l_{z}$  is parallel to the fixed axis, but l is not. In general, for a particle, the angular momentum l is not along the axis of rotation, i.e. for a particle, l and  $\omega$  are not necessarily parallel. Compare this with the corresponding fact in translation. For a particle, p and v are always parallel to each other.

For computing the total angular momentum of the whole rigid body, we add up the contribution of each particle of the body.

$$
\text {Thus} \quad \mathbf {L} = \sum \boldsymbol {l} _ {i} = \sum \boldsymbol {l} _ {i z} + \sum \mathbf {O C} _ {i} \times m _ {i} \mathbf {v} _ {i}
$$

We denote by  $L_{\perp}$  and  $L_{z}$  the components of L respectively perpendicular to the z-axis and along the z-axis;

$$
\mathbf {L} _ {\perp} = \sum \mathbf {O C} _ {i} \times m _ {i} \mathbf {v} _ {i}\tag{6.42a}
$$

where  $m_{i}$  and  $v_{i}$  are respectively the mass and the velocity of the  $i^{th}$  particle and  $C_{i}$  is the centre of the circle described by the particle;

$$
\mathbf {L} _ {z} = \sum \boldsymbol {l} _ {i z} = \left(\sum_ {i} m _ {i} r _ {i} ^ {2}\right) w \mathbf {k}
$$

or $\mathbf{L}_{z} = I\omega \hat{\mathbf{k}}$

(6.42b)

The last step follows since the perpendicular distance of the  $i^{th}$  particle from the axis is  $r_{i}$ ; and by definition the moment of inertia of the body about the axis of rotation is  $I = \sum m_{i} r_{i}^{2}$ .

Note  $L = L_{z} + L_{\perp}$

(6.42c)

The rigid bodies which we have mainly considered in this chapter are symmetric about the axis of rotation, i.e. the axis of rotation is one of their symmetry axes. For such bodies, for a given $\mathbf{OC}_i$, for every particle which has a velocity $\mathbf{v}_i$, there is another particle of velocity $-\mathbf{v}_i$ located diametrically opposite on the circle with centre $C_i$ described by the particle. Together such pairs will contribute zero to $\mathbf{L}_{\perp}$ and as a result for symmetric bodies $\mathbf{L}_{\perp}$ is zero, and hence

$$
\mathbf {L} = \mathbf {L} _ {\mathrm{z}} = I \omega \hat {\mathbf {k}}\tag{6.42d}
$$

For bodies, which are not symmetric about the axis of rotation, L is not equal to  $L_{z}$  and hence L does not lie along the axis of rotation.

Referring to Table 6.1, can you tell in which cases $\mathbf{L} = \mathbf{L}_{z}$ will not apply?

Let us differentiate Eq. (6.42b). Since  $\hat{k}$  is a fixed (constant) vector, we get

$$
\frac {\mathrm{d}}{\mathrm{d} t} \left(\mathbf {L} _ {z}\right) = \left(\frac {\mathrm{d}}{\mathrm{d} t} (I \omega)\right) \hat {\mathbf {k}}
$$

Now, Eq. (6.28b) states

$$
\frac {\mathrm{d} \mathbf {L}}{\mathrm{d} t} = \boldsymbol {\tau}
$$

Reprint 2025-26

<!-- page 31 of 35 -->

122

PHYSICS

As we have seen in the last section, only those components of the external torques which are along the axis of rotation, need to be taken into account, when we discuss rotation about a fixed axis. This means we can take $\boldsymbol{\tau} = \tau\hat{\mathbf{k}}$. Since $\mathbf{L} = \mathbf{L}_{z} + \mathbf{L}_{\perp}$ and the direction of $\mathbf{L}_{z}$ (vector $\hat{\mathbf{k}}$) is fixed, it follows that for rotation about a fixed axis,

$$
\frac {\mathrm{d} \mathbf {L} _ {z}}{\mathrm{d} t} = \tau \hat {\mathbf {k}}\tag{6.43a}
$$

$$
\text {and} \frac {\mathrm{d} \mathbf {L} _ {\perp}}{\mathrm{d} t} = 0\tag{6.43b}
$$

Thus, for rotation about a fixed axis, the component of angular momentum perpendicular to the fixed axis is constant. As  $L_{z}=I\omega\hat{k}$ , we get from Eq. (6.43a),

$$
\frac {\mathrm{d}}{\mathrm{d} t} (I \omega) = \tau\tag{6.43c}
$$

If the moment of inertia $I$ does not change with time,

$$
\frac {\mathrm{d}}{\mathrm{d} t} (I \omega) = I \frac {\mathrm{d} \omega}{\mathrm{d} t} = I \alpha
$$

and we get from Eq. (6.43c),

$$
\tau = I \alpha\tag{6.41}
$$

![Image block](doc:bba3640/tier:standard/page:31/block:12)

Fig 6.32 (a) A demonstration of conservation of angular momentum. A girl sits on a swivel chair and stretches her arms/brings her arms closer to the body.

We have already derived this equation using the work - kinetic energy route.

## 6.12.1 Conservation of angular momentum

We are now in a position to revisit the principle of conservation of angular momentum in the context of rotation about a fixed axis. From Eq. (6.43c), if the external torque is zero,

$$
L _ {z} = I \omega = \text {constant}\tag{6.44}
$$

For symmetric bodies, from Eq. (6.42d),  $L_{z}$  may be replaced by L.(L and  $L_{z}$  are respectively the magnitudes of L and  $L_{z}$ .)

This then is the required form, for fixed axis rotation, of Eq. (6.29a), which expresses the general law of conservation of angular momentum of a system of particles. Eq. (6.44) applies to many situations that we come across in daily life. You may do this experiment with your friend. Sit on a swivel chair (a chair with a seat, free to rotate about a pivot) with your arms folded and feet not resting on, i.e., away from, the ground. Ask your friend to rotate the chair rapidly. While the chair is rotating with considerable angular speed stretch your arms horizontally. What happens? Your angular speed is reduced. If you bring back your arms closer to your body, the angular speed increases again. This is a situation where the principle of conservation of angular momentum is applicable. If friction in the rotational

![Image block](doc:bba3640/tier:standard/page:31/block:20)

Fig 6.32 (b) An acrobat employing the principle of conservation of angular momentum in her performance.

Reprint 2025-26

<!-- page 32 of 35 -->

SYSTEMS OF PARTICLES AND ROTATIONAL MOTION

123

mechanism is neglected, there is no external torque about the axis of rotation of the chair and hence  $I\omega$  is constant. Stretching the arms increases I about the axis of rotation, resulting in decreasing the angular speed  $\omega$ . Bringing the arms closer to the body has the opposite effect.

A circus acrobat and a diver take advantage of this principle. Also, skaters and classical, Indian or western, dancers performing a pirouette (a spinning about a tip-top) on the toes of one foot display ‘mastery’ over this principle. Can you explain?

## SUMMARY

1. Ideally, a rigid body is one for which the distances between different particles of the body do not change, even though there are forces on them.

2. A rigid body fixed at one point or along a line can have only rotational motion. A rigid body not fixed in some way can have either pure translational motion or a combination of translational and rotational motions.

3. In rotation about a fixed axis, every particle of the rigid body moves in a circle which lies in a plane perpendicular to the axis and has its centre on the axis. Every Point in the rotating rigid body has the same angular velocity at any instant of time.

4. In pure translation, every particle of the body moves with the same velocity at any instant of time.

5. Angular velocity is a vector. Its magnitude is $\omega = d\theta / dt$ and it is directed along the axis of rotation. For rotation about a fixed axis, this vector $\omega$ has a fixed direction.

6. The vector or cross product of two vector $\mathbf{a}$ and $\mathbf{b}$ is a vector written as $\mathbf{a} \times \mathbf{b}$. The magnitude of this vector is $ab\sin\theta$ and its direction is given by the right handed screw or the right hand rule.

7. The linear velocity of a particle of a rigid body rotating about a fixed axis is given by $\mathbf{v} = \boldsymbol{\omega} \times \mathbf{r}$, where $\mathbf{r}$ is the position vector of the particle with respect to an origin along the fixed axis. The relation applies even to more general rotation of a rigid body with one point fixed. In that case $\mathbf{r}$ is the position vector of the particle with respect to the fixed point taken as the origin.

8. The centre of mass of a system of $n$ particles is defined as the point whose position vector is

$$
\mathbf {R} = \frac {\sum m _ {i} \mathbf {r} _ {i}}{M}
$$

9. Velocity of the centre of mass of a system of particles is given by $\mathbf{V} = \mathbf{P} / M$, where $\mathbf{P}$ is the linear momentum of the system. The centre of mass moves as if all the mass of the system is concentrated at this point and all the external forces act at it. If the total external force on the system is zero, then the total linear momentum of the system is constant.

10. The angular momentum of a system of $n$ particles about the origin is

$$
\mathbf {L} = \sum_ {i = 1} ^ {n} \mathbf {r} _ {i} \times \mathbf {p} _ {i}
$$

The torque or moment of force on a system of $n$ particles about the origin is

$$
\boldsymbol {\tau} = \sum_ {1} \mathbf {r} _ {i} \times \mathbf {F} _ {i}
$$

The force  $F_{i}$  acting on the  $I^{th}$  particle includes the external as well as internal forces. Assuming Newton's third law of motion and that forces between any two particles act along the line joining the particles, we can show  $\tau_{int} = 0$  and

Reprint 2025-26

<!-- page 33 of 35 -->

124

PHYSICS

$$
\frac {d \mathbf {L}}{d t} = \boldsymbol {\tau} _ {e x t}
$$

11. A rigid body is in mechanical equilibrium if

(1) it is in translational equilibrium, i.e., the total external force on it is zero :  $\sum F_{i}=0$ , and

(2) it is in rotational equilibrium, i.e. the total external torque on it is zero : $\sum \tau_{i} = \sum \mathbf{r}_{i} \times \mathbf{F}_{i} = \mathbf{0}$.

12. The centre of gravity of an extended body is that point where the total gravitational torque on the body is zero.

13. The moment of inertia of a rigid body about an axis is defined by the formula $I = \sum m_i r_i^2$ where $r_i$ is the perpendicular distance of the $i$th point of the body from the axis. The kinetic energy of rotation is $K = \frac{1}{2} I\omega^2$.

| Quantity | Symbols | Dimensions | Units | Remarks |
| --- | --- | --- | --- | --- |
| Angular velocity | ω | $[T^{-1}]$ | rad $s^{-}$ | $v = \omega \times r$ |
| Angular momentum | L | $[ML^{2} T^{-1}]$ | J s | $L = r \times p$ |
| Torque | τ | $[ML^{2} T^{-2}]$ | N m | $\tau = r \times F$ |
| Moment of inertia | I | $[ML^{2}]$ | kg $m^{2}$ | $I = \sum m_{t}r_{l}^{2}$ |

## POINTS TO PONDER

1. To determine the motion of the centre of mass of a system no knowledge of internal forces of the system is required. For this purpose we need to know only the external forces on the body.

2. Separating the motion of a system of particles as the motion of the centre of mass, (i.e., the translational motion of the system) and motion about (i.e. relative to) the centre of mass of the system is a useful technique in dynamics of a system of particles. One example of this technique is separating the kinetic energy of a system of particles $K$ as the kinetic energy of the system about its centre of mass $K'$ and the kinetic energy of the centre of mass $MV^2 / 2$,

$$
K = K ^{\prime} + MV^{2} / 2
$$

3. Newton's Second Law for finite sized bodies (or systems of particles) is based in Newton's Second Law and also Newton's Third Law for particles.

4. To establish that the time rate of change of the total angular momentum of a system of particles is the total external torque in the system, we need not only Newton's second law for particles, but also Newton's third law with the provision that the forces between any two particles act along the line joining the particles.

5. The vanishing of the total external force and the vanishing of the total external torque are independent conditions. We can have one without the other. In a couple, total external force is zero, but total torque is non-zero.

6. The total torque on a system is independent of the origin if the total external force is zero.

7. The centre of gravity of a body coincides with its centre of mass only if the gravitational field does not vary from one part of the body to the other.

Reprint 2025-26

<!-- page 34 of 35 -->

SYSTEMS OF PARTICLES AND ROTATIONAL MOTION

125

8. The angular momentum $\mathbf{L}$ and the angular velocity $\omega$ are not necessarily parallel vectors. However, for the simpler situations discussed in this chapter when rotation is about a fixed axis which is an axis of symmetry of the rigid body, the relation $\mathbf{L} = I\omega$ holds good, where $I$ is the moment of the inertia of the body about the rotation axis.

## EXERCISES

6.1 Give the location of the centre of mass of a (i) sphere, (ii) cylinder, (iii) ring, and (iv) cube, each of uniform mass density. Does the centre of mass of a body necessarily lie inside the body?

6.2 In the HCl molecule, the separation between the nuclei of the two atoms is about  $1.27 \AA (1 \AA = 10^{-10} m)$ . Find the approximate location of the CM of the molecule, given that a chlorine atom is about 35.5 times as massive as a hydrogen atom and nearly all the mass of an atom is concentrated in its nucleus.

6.3 A child sits stationary at one end of a long trolley moving uniformly with a speed $V$ on a smooth horizontal floor. If the child gets up and runs about on the trolley in any manner, what is the speed of the CM of the (trolley + child) system?

6.4 Show that the area of the triangle contained between the vectors $\mathbf{a}$ and $\mathbf{b}$ is one half of the magnitude of $\mathbf{a} \times \mathbf{b}$.

6.5 Show that $\mathbf{a} \cdot (\mathbf{b} \times \mathbf{c})$ is equal in magnitude to the volume of the parallelepiped formed on the three vectors, $\mathbf{a}, \mathbf{b}$ and $\mathbf{c}$.

6.6 Find the components along the $x, y, z$ axes of the angular momentum $\mathbf{l}$ of a particle, whose position vector is $\mathbf{r}$ with components $x, y, z$ and momentum is $\mathbf{p}$ with components $p_x, p_y$ and $p_z$. Show that if the particle moves only in the $x-y$ plane the angular momentum has only a $z$-component.

6.7 Two particles, each of mass m and speed v, travel in opposite directions along parallel lines separated by a distance d. Show that the angular momentum vector of the two particle system is the same whatever be the point about which the angular momentum is taken.

6.8 A non-uniform bar of weight W is suspended at rest by two strings of negligible weight as shown in Fig.6.33. The angles made by the strings with the vertical are  $36.9^{\circ}$  and  $53.1^{\circ}$  respectively. The bar is 2 m long. Calculate the distance d of the centre of gravity of the bar from its left end.

![Image block](doc:bba3640/tier:standard/page:34/block:13)

Fig. 6.33

6.9 A car weighs 1800 kg. The distance between its front and back axles is 1.8 m. Its centre of gravity is 1.05 m behind the front axle. Determine the force exerted by the level ground on each front wheel and each back wheel.

Reprint 2025-26

<!-- page 35 of 35 -->

126

PHYSICS

6.10 Torques of equal magnitude are applied to a hollow cylinder and a solid sphere, both having the same mass and radius. The cylinder is free to rotate about its standard axis of symmetry, and the sphere is free to rotate about an axis passing through its centre. Which of the two will acquire a greater angular speed after a given time.

6.11 A solid cylinder of mass 20 kg rotates about its axis with angular speed 100 rad s $^{-1}$ . The radius of the cylinder is 0.25 m. What is the kinetic energy associated with the rotation of the cylinder? What is the magnitude of angular momentum of the cylinder about its axis?

6.12 (a) A child stands at the centre of a turntable with his two arms outstretched. The turntable is set rotating with an angular speed of 40 rev/min. How much is the angular speed of the child if he folds his hands back and thereby reduces his moment of inertia to 2/5 times the initial value? Assume that the turntable rotates without friction.

(b) Show that the child's new kinetic energy of rotation is more than the initial kinetic energy of rotation. How do you account for this increase in kinetic energy?

6.13 A rope of negligible mass is wound round a hollow cylinder of mass 3 kg and radius 40 cm. What is the angular acceleration of the cylinder if the rope is pulled with a force of 30 N? What is the linear acceleration of the rope? Assume that there is no slipping.

6.14 To maintain a rotor at a uniform angular speed of 200 rad s $^{-1}$ , an engine needs to transmit a torque of 180 N m. What is the power required by the engine? (Note: uniform angular velocity in the absence of friction implies zero torque. In practice, applied torque is needed to counter frictional torque). Assume that the engine is 100% efficient.

6.15 From a uniform disk of radius R, a circular hole of radius R/2 is cut out. The centre of the hole is at R/2 from the centre of the original disc. Locate the centre of gravity of the resulting flat body.

6.16 A metre stick is balanced on a knife edge at its centre. When two coins, each of mass 5 g are put one on top of the other at the 12.0 cm mark, the stick is found to be balanced at 45.0 cm. What is the mass of the metre stick?

6.17 The oxygen molecule has a mass of  $5.30 \times 10^{-26}$  kg and a moment of inertia of  $1.94 \times 10^{-46}$  kg m $^{2}$  about an axis through its centre perpendicular to the lines joining the two atoms. Suppose the mean speed of such a molecule in a gas is 500 m/s and that its kinetic energy of rotation is two thirds of its kinetic energy of translation. Find the average angular velocity of the molecule.

Reprint 2025-26