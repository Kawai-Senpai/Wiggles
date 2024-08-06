# Wiggles

Wiggles is a powerful and flexible Python library for generating, manipulating, and visualizing signals developed by *Ranit Bhowmick* & *Sayanti Chatterjee*. Whether you're working with continuous or discrete signals, Wiggles provides a wide range of functionalities to make signal processing straightforward and intuitive. It supports operations in both the time domain and frequency domain, including Fast Fourier Transform (FFT) and inverse FFT, and allows for easy conversion between different representations.

Wiggles is designed to be easy to use and integrate into your existing Python workflows, making it a valuable tool for engineers, researchers, and anyone interested in signal processing.

link : https://pypi.org/project/wiggles/

## Features
- Generation of continuous and discrete signals
- Conversion between time domain and frequency domain
- Support for common signal types like sine waves, square waves, and more
- Visualization of signals
- Export and import of signals to various formats
- Playback of signals as audio

## Installation
Ensure Python 3.10 is installed in the system and added to the system variables. Install the library through pip with the command:
```sh
pip install wiggles
```

## Getting Started
Here are examples of generating and visualizing basic signals using Wiggles.

---

## Generation of Basic Signals (Continuous and Discrete) in Python using the Custom Library Wiggles

### Sin Wave

#### Theory
A sine wave, sinusoidal wave, or just sinusoid is a mathematical curve defined in terms of the sine trigonometric function, of which it is the graph. It is a type of continuous wave and also a smooth periodic function. It occurs often in mathematics, as well as in physics, engineering, signal processing, and many other fields.

#### Expression
$$
y(t) = A \sin(\omega t + \phi) = A \sin(2 \pi f t + \phi)
$$

where:
- $A$ represents the amplitude, which is the peak deviation of the function from zero.
- $f$ represents the ordinary frequency, which is the number of oscillations (cycles) that occur each second of time.
- $\omega = 2 \pi f$ represents the angular frequency, which is the rate of change of the function argument in units of radians per second.
- $\phi$ represents the phase, which specifies (in radians) where in its cycle the oscillation is at $t = 0$. When $\phi$ is non-zero, the entire waveform appears to be shifted in time by the amount $\frac{\phi}{\omega}$ seconds. A negative value represents a delay, and a positive value represents an advance.

### Getting the Environment Ready
- Ensure Python 3.10 is installed in the system and added to the system variables.
- Install the library through pip with the command:
  ```sh
  pip install wiggles
  ```
- Use VS Code to code and test out the results.
- The code is written to find the best solution to the given problem and then is evaluated and displayed using the inbuilt `show()` or `compare()` function in Wiggles.

### Problem
Generate sine waves in Python and plot them using Wiggles.

### Program Code

```python
import math
from wiggles import signals as sp

# Adjust using these variables
A = 2
f = 5
w = 2 * f * math.pi
Q = 0

# The sin function
def sin(t):
    return A * math.sin((w * t) + Q)

# Building the continuous signal
y = sp.continuous(sin)

# Adjusting properties and displaying the continuous signal
y.name = "sin(t)"
y.show() 

# Building the discrete signal
y2 = sp.continuous(sin, step=0.01)
y2.is_descrete = True

# Adjusting properties and displaying the discrete signal
y2.name = "sin[t]"
y2.show()
```

---

### COS WAVE

#### Theory
A cosine wave is a mathematical curve defined in terms of the cosine trigonometric function, of which it is the graph. It is a type of continuous wave and also a smooth periodic function. It occurs often in mathematics, as well as in physics, engineering, signal processing, and many other fields.

#### Expression
$$
y(t) = A \cos(\omega t + \phi) = A \cos(2 \pi f t + \phi)
$$

where:
- $A$: Amplitude, the peak deviation of the function from zero.
- $f$: Ordinary frequency, the number of oscillations (cycles) that occur each second of time.
- $\omega = 2 \pi f$: Angular frequency, the rate of change of the function argument in units of radians per second.
- $\phi$: Phase, specifies (in radians) where in its cycle the oscillation is at $t = 0$. When $\phi$ is non-zero, the entire waveform appears to be shifted in time by the amount $\phi / \omega$ seconds. A negative value represents a delay, and a positive value represents an advance.

### Problem
Generate cosine waves in Python and plot them using Wiggles.

### Program Code

```python
import math
from wiggles import signals as sp

# Adjust using these variables
A = 2
f = 5
w = 2 * f * math.pi
Q = 0

# The cos function
def cos(t):
    return A * math.cos((w * t) + Q)

# Building the continuous signal
y = sp.continuous(cos)

# Adjusting properties and displaying the continuous signal
y.name = "cos(t)"
y.show() 

# Building the discrete signal
y2 = sp.continuous(cos, step=0.01)
y2.is_descrete = True

# Adjusting properties and displaying the discrete signal
y2.name = "cos[t]"
y2.show()
```

---

### EXPONENTIAL CURVE

#### Theory
The exponential function is a mathematical function denoted by $f(x) = \exp(x)$ or $e^x$ (where the argument $x$ is) written as an exponent). Unless otherwise specified, the term generally refers to the positive-valued function of a real variable, although it can be extended to the complex numbers or generalized to other mathematical objects like matrices or Lie algebras. The exponential function originated from the notion of exponentiation (repeated multiplication), but modern definitions (there are several equivalent characterizations) allow it to be rigorously extended to all real arguments, including irrational numbers.

#### Expression
$$
y(t) = A e^{-t}
$$
    
where:
- $A$: Amplitude, the peak deviation of the function from zero.
- $\omega$: Angular frequency, the rate of change of the function argument in units of radians per second.

### Problem
Generate exponentially growing and exponentially decaying waves in Python and plot them using Wiggles.

### Program Code

#### Exponentially Growing

```python
import math
from wiggles import signals as sp

# Adjust using these variables
A = 2
a = -4

# The exp function
def exp(t):
    return A * math.exp(-1 * a * t)

# Building the signal
y = sp.continuous(exp)

# Adjusting properties and displaying the signal
y.name = "Exponentially Growing"
y.show()
```

#### Exponentially Decaying

```python
from wiggles import signals as sp

# Adjust using these variables
A = 2
a = 4

# The exp function
def exp(t):
    return A * math.exp(-1 * a * t)

# Building the signal
y = sp.continuous(exp)

# Adjusting properties and displaying the signal
y.name = "Exponentially Decaying"
y.show()
```

---

## Generation of Exponentially Growing and Decaying Sinusoidal Curves in Python using the Custom Library Wiggles

### Theory
The exponential function is a mathematical function denoted by $f(x) = \exp(x)$ or $e^x$ (where the argument $x$ is written as an exponent). A sinusoidal wave, or just sinusoid, is a mathematical curve defined in terms of the sine trigonometric function.

#### Expressions
- Exponential: $y(t) = A e^{-t}$
- Sinusoidal:
  - Sine: $y(t) = A \sin(\omega t + \phi) = A \sin(2 \pi f t + \phi)$
  - Cosine: $y(t) = A \cos(\omega t + \phi) = A \cos(2 \pi f t + \phi)$

Where:
- $A$: Amplitude, the peak deviation of the function from zero.
- $f$: Ordinary frequency, the number of oscillations (cycles) that occur each second of time.
- $\omega = 2 \pi f$: Angular frequency, the rate of change of the function argument in units of radians per second.
- $\phi$: Phase, specifies (in radians) where in its cycle the oscillation is at $t = 0$.

### Problem
Generate exponentially growing and exponentially decaying sine and cosine waves in Python and plot them using Wiggles.

### Program Code

#### Exponentially Growing Sin

```python
import math
from wiggles import signals as sp

# Adjust using these variables
A = 1
a = -5
f = 7
w = 2 * f * math.pi
Q = 0

# The exp function
def exp(t):
    return A * math.exp(-1 * a * t)

# The sin function
def sin(t):
    return A * math.sin((w * t) + Q)

# Building and operating on the signal
expwave = sp.continuous(exp)
sinwave = sp.continuous(sin)
expsin = expwave * sinwave

# Adjusting properties and displaying the signal
expwave.name = "Exponentially Growing Wave"
sinwave.name = "Sin Wave"
expsin.name = "Exponentially Growing Sin"

expwave.compare(sinwave, expsin, spacing=0.407)
```

#### Exponentially Decaying Sin

```python
import math
from wiggles import signals as sp

# Adjust using these variables
A = 1
a = 5
f = 7
w = 2 * f * math.pi
Q = 0

# The exp function
def exp(t):
    return A * math.exp(-1 * a * t)

# The sin function
def sin(t):
    return A * math.sin((w * t) + Q)

# Building and operating on the signal
expwave = sp.continuous(exp)
sinwave = sp.continuous(sin)
expsin = expwave * sinwave

# Adjusting properties and displaying the signal
expwave.name = "Exponentially Decaying Wave"
sinwave.name = "Sin Wave"
expsin.name = "Exponentially Decaying Sin"

expwave.compare(sinwave, expsin, spacing=0.407)
```

#### Exponentially Growing Cos

```python
import math
from wiggles import signals as sp

# Adjust using these variables
A = 1
a = -5
f = 7
w = 2 * f * math.pi
Q = 0

# The exp function
def exp(t):
    return A * math.exp(-1 * a * t)

# The cos function
def cos(t):
    return A * math.cos((w * t) + Q)

# Building and operating on the signal
expwave = sp.continuous(exp)
coswave = sp.continuous(cos)
expsin = expwave * coswave

# Adjusting properties and displaying the signal
expwave.name = "Exponentially Growing Wave"
coswave.name = "Cos Wave"
expsin.name = "Exponentially Growing Cos"

expwave.compare(coswave, expsin, spacing=0.407)
```

#### Exponentially Decaying Cos

```python
import math
from wiggles import signals as sp

# Adjust using these variables
A = 1
a = 5
f = 7
w = 2 * f * math.pi
Q = 0

# The exp function
def exp(t):
    return A * math.exp(-1 * a * t)

# The cos function
def cos(t):
    return A * math.cos((w * t) + Q)

# Building and operating on the signal
expwave = sp.continuous(exp)
coswave = sp.continuous(cos)
expsin = expwave * coswave

# Adjusting properties and displaying the signal
expwave.name = "Decaying Growing Wave"
coswave.name = "Cos Wave"
expsin.name = "Decaying Growing Cos"

expwave.compare(coswave, expsin, spacing=0.407)
```
---

### UNIT IMPULSE WITHOUT FUNCTION

**Theory**

An ideal impulse signal is a signal that is zero everywhere but at the origin ($t = 0$), where it is infinitely high. Although, the area of the impulse is finite. The unit impulse signal is the most widely used standard signal in the analysis of signals and systems.

**Expression**

$$
\delta(t) = 
\begin{cases} 
1 & \text{for } t = 0 \\
0 & \text{else} 
\end{cases}
$$

**PROBLEM**

Generate unit impulse signal in Python and plot it using the same.

**PROGRAM CODE**

```python
from wiggles import signals as sp

# Building amplitude data for unit impulse
length = 20
y = ([0] * length) + [1] + ([0] * length)

# Making signal using the amplitude data 'y' using wiggles and displaying
unitimpulse = sp.discrete(y, -length)
unitimpulse.name = "Unit Impulse"
unitimpulse.show()
```

---

### UNIT STEP WITHOUT FUNCTION

**Theory**

The step signal or step function is a standard signal that exists only for positive time and is zero for negative time. In other words, a signal $x(t)$ is said to be a step signal if and only if it exists for $t > 0$ and is zero for $t < 0$. The step signal is an important signal used for the analysis of many systems. The step signal is equivalent to applying a signal to a system whose magnitude suddenly changes and remains constant forever after application. To obtain a signal that starts at $t = 0$, multiply the given signal with the unit step signal $u(t)$.

**Expression**

$$
u(t) = 
\begin{cases} 
1 & \text{for } t \ge 0 \\
0 & \text{for } t < 0 
\end{cases}
$$

**PROBLEM**

Generate unit step signals in Python and plot them using the same.

**PROGRAM CODE**

```python
from wiggles import signals as sp

# Building amplitude data for unit Step
length = 20
y = ([0] * length) + ([1] * length)

# Making signal using the amplitude data 'y' using wiggles
unitimpulse = sp.discrete(y, -length)

# Naming and displaying the signal
unitimpulse.name = "Unit Step"
unitimpulse.show()
```

---

### RAMP WITHOUT FUNCTION

**Theory**

A ramp function or ramp signal is a standard signal that starts at $t = 0$ and increases linearly with time. The unit ramp function has unit slope. The unit ramp signal can be obtained by integrating the unit step signal with respect to time. In other words, a unit step signal can be obtained by differentiating the unit ramp signal.

**Expression**

$$
r(t) = 
\begin{cases} 
t & \text{for } t \ge 0 \\
0 & \text{for } t < 0 
\end{cases}
$$

**PROBLEM**

Generate a ramp signal in Python and plot it using the same.

**PROGRAM CODE**

```python
from wiggles import signals as sp

# Building amplitude data for Ramp
length = 20
y = [i for i in range(length)]

# Making signal using the amplitude data 'y' using wiggles
unitimpulse = sp.discrete(y)

# Naming and displaying the signal
unitimpulse.name = "Ramp"
unitimpulse.show()
```

---
