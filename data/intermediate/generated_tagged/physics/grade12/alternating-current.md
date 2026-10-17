# Alternating Current

Alternating current is the flow of electric charge that periodically reverses its direction. Unlike direct current, which flows steadily in one direction, alternating current is the type of electricity supplied to our homes and offices, making it essential for the daily operation of almost all modern electrical devices [S3]. The main reason for preferring alternating current over direct current is that ac voltages can be easily and efficiently converted from one voltage to another by means of transformers, allowing electrical energy to be transmitted economically over long distances [S3].

## AC Voltage Applied to a Resistor

When an ac source is connected to a pure resistor, the voltage and current vary sinusoidally. Let the potential difference, or ac voltage, be given by $v = v_m \sin \omega t$ [S1]. Applying Kirchhoff's loop rule to the circuit, we find the current through the resistor to be $i = \frac{v_m}{R} \sin \omega t$ [S1]. Since $R$ is a constant, we can write this equation as $i = i_m \sin \omega t$, where the current amplitude $i_m$ is given by $i_m = \frac{v_m}{R}$ [S1].

Equation (7.3) is Ohm's law, which for resistors, works equally well for both ac and dc voltages [S1]. The voltage across a pure resistor and the current through it are in phase with each other. This means that both $v$ and $i$ reach zero, minimum, and maximum values at the same time [S1]. Because the current varies sinusoidally with corresponding positive and negative values during each cycle, the sum of the instantaneous current values over one complete cycle is zero, and the average current is zero [S1].

However, the fact that the average current is zero does not mean that the average power consumed is zero. As you know, Joule heating is given by $i^2 R$ and depends on $i^2$ (which is always positive whether $i$ is positive or negative) and not on $i$ [S1]. Thus, there is Joule heating and dissipation of electrical energy when an ac current passes through a resistor. The instantaneous power dissipated in the resistor is $p = i^2 R = i_m^2 R \sin^2 \omega t$ [S1]. The average value of $p$ over a cycle is $\overline{p} = \frac{1}{2} i_m^2 R$ [S1].

To express ac power in the same form as dc power $(P = I^2 R)$, a special value of current is defined and used. It is called, root mean square (rms) or effective current and is denoted by $I_{rms}$ or $I$ [S1]. The rms current $I$ is related to the peak current $i_m$ by $I = i_m / \sqrt{2} = 0.707 \, i_m$ [S1].

In terms of $I$, the average power, denoted by $P$, is $P = \frac{1}{2} i_m^2 R = I^2 R$ [S1]. Similarly, we define the rms voltage or effective voltage by $V = \frac{v_m}{\sqrt{2}} = 0.707 \, v_m$ [S1]. From Eq. (7.3), we have $v_m = i_m R$ or, $\frac{v_m}{\sqrt{2}} = \frac{i_m}{\sqrt{2}} R$, or, $V = IR$ [S1]. Equation (7.9) gives the relation between ac current and ac voltage and is similar to that in the dc case [S1].

It is customary to measure and specify rms values for ac quantities. For example, the household line voltage of 220 V is an rms value with a peak voltage of $v_m = \sqrt{2} V = (1.414) (220 \mathrm{V}) = 311 \mathrm{V}$ [S1].

## AC Circuits with L and C

In a series circuit containing an inductor and a capacitor, the ac current in each element is the same at any time, having the same amplitude and phase [S2]. Let the current be $i = i_m \sin (\omega t + \phi)$, where $\phi$ is the phase difference between the voltage across the source and the current in the circuit [S2].

From previous sections, we know that the voltage across the resistor $V_R$ is parallel to the current $I$, the voltage across the capacitor $V_C$ is $\pi/2$ behind the current, and the voltage across the inductor $V_L$ is $\pi/2$ ahead of the current [S2]. The length of these phasors or the amplitude of $V_R$, $V_C$, and $V_L$ are $v_{Rm} = i_m R$, $v_{Cm} = i_m X_C$, $v_{Lm} = i_m X_L$ [S2].

The voltage equation for the circuit can be written as $V_L + V_R + V_C = V$ [S2]. Since $V_C$ and $V_L$ are always along the same line and in opposite directions, they can be combined into a single phasor $(V_C + V_L)$ which has a magnitude $|v_{Cm} - v_{Lm}|$ [S2]. Since $V$ is represented as the hypotenuse of a right-triangle whose sides are $V_R$ and $(V_C + V_L)$, the pythagorean theorem gives $v_m^2 = v_{Rm}^2 + (v_{Cm} - v_{Lm})^2$ [S2]. Substituting the values of $v_{Rm}$, $v_{Cm}$, and $v_{Lm}$ from Eq. (7.22) into the above equation, we have $v_m^2 = (i_m R)^2 + (i_m X_C - i_m X_L)^2$ [S2].

By analogy to the resistance in a circuit, we introduce the impedance $Z$ in an ac circuit [S2]. $Z = \sqrt{R^2 + (X_C - X_L)^2}$ [S2]. The current amplitude is $i_m = \frac{v_m}{Z}$ [S2].

The phase angle $\phi$ is the angle between $V_R$ and $V$ and can be determined by $\tan \phi = \frac{v_{Cm} - v_{Lm}}{v_{Rm}}$ [S2]. Using Eq. (7.22), we have $\tan \phi = \frac{X_C - X_L}{R}$ [S2].

If $X_C > X_L$, $\phi$ is positive and the circuit is predominantly capacitive. Consequently, the current in the circuit leads the source voltage [S2]. If $X_C < X_L$, $\phi$ is negative and the circuit is predominantly inductive. Consequently, the current in the circuit lags the source voltage [S2].

## Worked example

A light bulb is rated at 100W for a 220 V supply. We are given $P = 100 \, \mathrm{W}$ and $V = 220 \, \mathrm{V}$.

(a) The resistance of the bulb is $R = \frac{V^2}{P} = \frac{(220 \mathrm{V})^2}{100 \mathrm{W}} = 484 \Omega$ [S1].

(b) The peak voltage of the source is $v_m = \sqrt{2} V = 311 \mathrm{V}$ [S1].

(c) Since $P = I V$, the rms current through the bulb is $I = \frac{P}{V} = \frac{100 \mathrm{W}}{220 \mathrm{V}} = 0.454 \mathrm{A}$ [S1].

## Key points

*   Alternating current periodically reverses its direction, unlike direct current [S3].
*   The voltage and current are in phase with each other when an ac source is connected to a pure resistor [S1].
*   The average current over one complete cycle is zero, but there is Joule heating and dissipation of electrical energy [S1].
*   The rms current $I$ is related to the peak current $i_m$ by $I = i_m / \sqrt{2} = 0.707 \, i_m$ [S1].
*   The average power in an ac circuit is $P = I^2 R$ [S1].
*   The impedance $Z$ in an ac circuit is $Z = \sqrt{R^2 + (X_C - X_L)^2}$ [S2].
*   The phase angle $\phi$ in an LCR circuit is given by $\tan \phi = \frac{X_C - X_L}{R}$ [S2].

<!-- TERMS: alternating current, direct current, resistor, inductor, capacitor, impedance, phasor, rms value, peak value, phase angle, angular frequency -->