# Wiggles

![Wiggles Cover](https://github.com/Kawai-Senpai/Wiggles/blob/55f78889b24160cd0e8dba1eedece0550df09ec5/Assets/Wiggles%20Cover%20Image.png)

[Wiggles](https://pypi.org/project/wiggles/) is a powerful and flexible Python library for generating, manipulating, and visualizing signals developed by [*Ranit Bhowmick*](https://www.linkedin.com/in/ranitbhowmick/) & [*Sayanti Chatterjee*](https://www.linkedin.com/in/sayantichatterjee/). Whether you're working with continuous or discrete signals, Wiggles provides a wide range of functionalities to make signal processing straightforward and intuitive. It supports operations in both the time domain and frequency domain, including Fast Fourier Transform (FFT) and inverse FFT, and allows for easy conversion between different representations.

Wiggles is designed to be easy to use and integrate into your existing Python workflows, making it a valuable tool for engineers, researchers, and anyone interested in signal processing.

• [Download Wiggles](https://pypi.org/project/wiggles/)

• [Wiggles Documentation (With Images)](https://github.com/Kawai-Senpai/wiggles/tree/8d3cb835b1c2561db5d24dbe7295803c8b1f879a/Documentation)

• [Example Codes](https://github.com/Kawai-Senpai/wiggles/tree/8d3cb835b1c2561db5d24dbe7295803c8b1f879a/Examples)

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

### UNIT IMPULSE WITH FUNCTION

**Theory**

An ideal impulse signal is a signal that is zero everywhere but at the origin ($t = 0$), where it is infinitely high. Although the area of the impulse is finite, the unit impulse signal is widely used in the analysis of signals and systems.

**Expression**

$$
\delta(t) = 
\begin{cases} 
1 & \text{for } t = 0 \\
0 & \text{else} 
\end{cases}
$$

**PROBLEM**

Generate unit impulse signals using user-defined functions in Python and plot them.

**PROGRAM CODE**

```python
from wiggles import signals as sp

# Making signal using the abstracted user-defined function
unitimpulse = sp.unit_impulse(-20, 20)
unitimpulse.name = "Unit Impulse"
unitimpulse.show()
```

---

### UNIT STEP WITH FUNCTION

**Theory**

The step signal or step function is a standard signal that exists only for positive time and is zero for negative time. In other words, a signal $x(t)$ is a step signal if and only if it exists for $t > 0$ and is zero for $t < 0$. The step signal is crucial for analyzing many systems. To obtain a signal that starts at $t = 0$, multiply the given signal with the unit step signal $u(t)$.

**Expression**

$$
u(t) = 
\begin{cases} 
1 & \text{for } t \ge 0 \\
0 & \text{for } t < 0 
\end{cases}
$$

**PROBLEM**

Generate unit step signals in Python using user-defined functions and plot and display the signal.

**PROGRAM CODE**

```python
from wiggles import signals as sp

# Making signal using the inbuilt function we developed in wiggles and displaying it
unitstep = sp.unit_step(-20, 20)
unitstep.name = "Unit Step"
unitstep.show()
```

---

## Basic Operations on Signals in Python

### SIGNAL SHIFTING

**Theory**

Shifting means moving a signal either in the time domain or in the amplitude domain. This can be categorized into:

- **Time Shifting**: Movement in the time domain. If $k$ is positive, the signal shifts left; if $k$ is negative, the signal shifts right.

**Expression**

$$
x(t) \rightarrow y(t + k)
$$

**PROBLEM**

Time shift a test signal by a specific value and display it in a subplot to study the change and compare.

**PROGRAM CODE**

```python
from wiggles import signals as sp

# Test signal y; Making discrete signal using wiggles
y = sp.discrete([2, -2, 3, -3, 4], -3)
y.name = "y"

# Shifting the signal 'y' by 1
y1 = y.TimeShift(1)

# Comparing two signals
y.compare(y1)
```

---

### SIGNAL SCALING

**Theory**

Time scaling involves multiplying the time axis of a signal by a constant. This process can result in:

- **Time Compression**: If $\alpha > 1$, the signal is compressed in time by a factor of $\alpha$.
- **Time Expansion**: If $\alpha < 1$, the signal is expanded in time by a factor of $\alpha$.

**Expression**

$$
x(t) \rightarrow y(t) = x(\alpha t)
$$

**PROBLEM**

Time scale a test signal by a specific value and display it in a subplot to study the change and compare.

**PROGRAM CODE**

```python
from wiggles import signals as sp

# Test signal y; Making discrete signal using wiggles
y = sp.discrete([2, -2, 3, -3, 4], -3)
y.name = "y"

# Scaling the signal 'y' by 2
y1 = y.TimeScale(2)

# Comparing two signals
y.compare(y1)
```

---

### SIGNAL REVERSAL

**Theory**

Time reversal involves multiplying the time variable by -1, which produces a mirror image of the signal about the Y-axis.

**Expression**

$$
x(t) \rightarrow y(t) = x(-t)
$$

**PROBLEM**

Time reverse a test signal by a specific value and display it in a subplot to study the change and compare.

**PROGRAM CODE**

```python
from wiggles import signals as sp

# Test signal y; Making discrete signal using wiggles
y = sp.discrete([2, -2, 3, -3, 4], -3)
y.name = "y"

# Reversing the signal 'y'
y1 = y.reverse()

# Comparing two signals
y.compare(y1)
```

---

## Implementing and performing convolution

### CONVOLUTION SAME INDEX

**Theory**

Convolution is a mathematical tool for combining two signals to produce a third signal. It is crucial in signal processing as it relates the input signal and the impulse response of the system to generate the output signal. For continuous signals, convolution involves integrating the product of the signals over time.

**Expression**

$$
y(t) = x(t) * h(t) \equiv \int_{-\infty}^{\infty} x(\tau) h(t - \tau) \, d\tau
$$

**PROBLEM**

Perform convolution between two signals starting from the same index and display the results.

**PROGRAM CODE**

```python
from wiggles import signals as sp

# Creating two test signals (Starting from the same index)
x1 = sp.discrete([-1, 2, -3, 1], -1)
x1.name = "x1"
x2 = sp.discrete([3, 0, 1, -4], -1)
x2.name = "x2"

# Performing convolution and displaying the result
result = x1.convolve(x2)
x1.compare(x2, result)
```

---

### CONVOLUTION DIFFERENT INDEX

**Theory**

Convolution combines two signals to produce a third signal, relating the input signal and the impulse response to generate the output signal. For continuous signals, it involves integrating the product of the signals over time.

**Expression**

$$
y(t) = x(t) * h(t) \equiv \int_{-\infty}^{\infty} x(\tau) h(t - \tau) \, d\tau
$$

**PROBLEM**

Perform convolution between two signals starting from different indices and display the results.

**PROGRAM CODE**

```python
from wiggles import signals as sp

# Creating two test signals (Starting from different index)
x1 = sp.discrete([-1, 2, -3, 1], -1)
x1.name = "x1"
x2 = sp.discrete([3, 0, 1, -4], -3)
x2.name = "x2"

# Performing convolution and displaying the result
result = x1.convolve(x2)
x1.compare(x2, result)
```

---

## Implementing and verifying different properties of convolution

### COMMUTATIVE PROPERTY

**Theory**

The commutative property of convolution states that the order in which two signals are convolved does not affect the result. This means:

**Expression**

$$
x_1(t) * x_2(t) = x_2(t) * x_1(t)
$$

**PROBLEM**

Implement and verify the commutative property of convolution.

**PROGRAM CODE**

```python
from wiggles import signals as sp

# Creating two test signals
x1 = sp.discrete([-1, 2, -3, 1], -1)
x1.name = "x1"
x2 = sp.discrete([3, 0, 1, -4], -3)
x2.name = "x2"

'''
Commutative Property of Convolution:
The commutative property of convolution states that the order in which
we convolve two signals does not change the result,
i.e.,
x1(t) * x2(t) = x2(t) * x1(t)
'''

# Calculating LHS:
lhs = x1.convolve(x2)

# Calculating RHS:
rhs = x2.convolve(x1)

# Displaying both results
lhs.compare(rhs)
```

---

### DISTRIBUTIVE PROPERTY

**Theory**

The distributive property of convolution states that convolution distributes over addition. For three signals \(x_1(t)\), \(x_2(t)\), and \(x_3(t)\), this means:

**Expression**

$$
x_1(t) * [x_2(t) + x_3(t)] = [x_1(t) * x_2(t)] + [x_1(t) * x_3(t)]
$$

**PROBLEM**

Implement and verify the distributive property of convolution.

**PROGRAM CODE**

```python
from wiggles import signals as sp

# Creating three test signals
x1 = sp.discrete([-1, 2, -3, 1], -1)
x1.name = "x1"
x2 = sp.discrete([3, 0, 1, -4], -3)
x2.name = "x2"
x3 = sp.discrete([5, 6, 7, 8], -2)
x3.name = "x3"

'''
Distributive Property of Convolution:
The distributive property of convolution states that
if there are three signals x1(t), x2(t), and x3(t),
then the convolution of x1(t) is distributive over the addition,
i.e.,
x1(t) * [x2(t) + x3(t)] = [x1(t) * x2(t)] + [x1(t) * x3(t)]
'''

# Calculating LHS:
lhs = x1.convolve(x2 + x3)

# Calculating RHS:
rhs = (x1.convolve(x2)) + (x1.convolve(x3))

# Displaying both results
lhs.compare(rhs)
```

---

### ASSOCIATIVE PROPERTY

**Theory**

The associative property of convolution states that the grouping of signals in convolution does not affect the result. This means:

**Expression**

$$
x_1(t) * [x_2(t) * x_3(t)] = [x_1(t) * x_2(t)] * x_3(t)
$$

**PROBLEM**

Implement and verify the associative property of convolution.

**PROGRAM CODE**

```python
from wiggles import signals as sp

# Creating three test signals
x1 = sp.discrete([-1, 2, -3, 1], -1)
x1.name = "x1"
x2 = sp.discrete([3, 0, 1, -4], -3)
x2.name = "x2"
x3 = sp.discrete([5, 6, 7, 8], -2)
x3.name = "x3"

'''
Associative Property of Convolution:
The associative property of convolution states that the way in which
the signals are grouped in a convolution does not change the result,
i.e.,
x1(t) * [x2(t) * x3(t)] = [x1(t) * x2(t)] * x3(t)
'''

# Calculating LHS:
lhs = x1.convolve(x2.convolve(x3))

# Calculating RHS:
rhs = (x1.convolve(x2)).convolve(x3)

# Displaying both results
lhs.compare(rhs)
```

---

## Performing Operations Like Addition, Subtraction and Multiplication on Signals

### ADDITION

**Theory**

The sum of two discrete time signals \(x_1[n]\) and \(x_2[n]\) can be obtained by adding their values at every instant of time.

**PROBLEM**

Implement and verify the result after adding two discrete signals.

**PROGRAM CODE**

```python
from wiggles import signals as sp

# Creating two test signals
x = sp.discrete([-1, 2, -3, 1], -1)
x.name = "x"
y = sp.discrete([3, 0, 1, -4], -3)
y.name = "y"

# Performing operation and displaying the result
result = x + y
x.compare(y, result)
```

---

### SUBTRACTION

**Theory**

The difference of two discrete time signals \(x_1[n]\) and \(x_2[n]\) can be obtained by subtracting their values at every instant of time.

**PROBLEM**

Implement and verify the result after subtracting two discrete signals.

**PROGRAM CODE**

```python
from wiggles import signals as sp

# Creating two test signals
x = sp.discrete([-1, 2, -3, 1], -1)
x.name = "x"
y = sp.discrete([3, 0, 1, -4], -3)
y.name = "y"

# Performing operation and displaying the result
result = x - y
x.compare(y, result)
```

---

### MULTIPLICATION

**Theory**

The multiplication of two discrete time signals \(x_1[n]\) and \(x_2[n]\) can be obtained by multiplying their values at every instant of time.

**PROBLEM**

Implement and verify the result after multiplying two discrete signals.

**PROGRAM CODE**

```python
from wiggles import signals as sp

# Creating two test signals
x = sp.discrete([-1, 2, -3, 1], -1)
x.name = "x"
y = sp.discrete([3, 0, 1, -4], -3)
y.name = "y"

# Performing operation and displaying the result
result = x * y
x.compare(y, result)
```

---

### DIVISION

**Theory**

The division of two discrete time signals \(x_1[n]\) and \(x_2[n]\) can be obtained by dividing their values at every instant of time.

**PROBLEM**

Implement and verify the result after dividing two discrete signals.

**PROGRAM CODE**

```python
from wiggles import signals as sp

# Creating two test signals
x = sp.discrete([-1, 2, -3, 1], 0)
x.name = "x"
y = sp.discrete([3, 1, 1, -4], 0)
y.name = "y"

# Performing operation and displaying the result
result = x / y
x.compare(y, result)
```

---

## Computing and displaying even and odd components of a signal

### EVEN COMPONENT

**Theory**

A signal is said to be an even signal if it is symmetrical about the vertical axis or time origin. Every signal need not be purely even or purely odd; instead, it can be expressed as the sum of even and odd components. The even component of any signal can be calculated by:

$$
x_e(t) = \frac{1}{2} \left[ x(t) + x(-t) \right]
$$

**PROBLEM**

Implement and verify the calculation of the even component of a signal.

**PROGRAM CODE**

```python
from wiggles import signals as sp

# Creating a test signal
x = sp.discrete([-1, 8, -3, 4], 0)
x.name = "x"

# Finding the even component and displaying the result
component = x.even_component()
component.name = "Even Component"
x.compare(component)
```

---

### ODD COMPONENT

**Theory**

A signal is said to be an odd signal if it is anti-symmetrical about the vertical axis. Every signal need not be purely even or purely odd; instead, it can be expressed as the sum of even and odd components. The odd component of any signal can be calculated by:

$$
x_o(t) = \frac{1}{2} \left[ x(t) - x(-t) \right]
$$

**PROBLEM**

Implement and verify the calculation of the odd component of a signal.

**PROGRAM CODE**

```python
from wiggles import signals as sp

# Creating a test signal
x = sp.discrete([-1, 8, -3, 4], 0)
x.name = "x"

# Finding the odd component and displaying the result
component = x.odd_component()
component.name = "Odd Component"
x.compare(component)
```

---

### VERIFICATION

**Theory**

Every signal need not be purely even or purely odd; instead, it can be expressed as the sum of even and odd components:

$$
x(t) = x_e(t) + x_o(t)
$$

Where:
- \(x_e(t)\) is the even component of the signal
- \(x_o(t)\) is the odd component of the signal

**PROBLEM**

Verify by adding the even and odd components of the signal to retrieve the original signal.

**PROGRAM CODE**

```python
from wiggles import signals as sp

# Creating a test signal
x = sp.discrete([-1, 8, -3, 4], 0)
x.name = "x"

# Finding the even component
even = x.even_component()
even.name = "Even Component"

# Finding the odd component
odd = x.odd_component()
odd.name = "Odd Component"

# Adding the two components
'''
Since:
Every signal need not be either purely even or purely odd,
but it can be expressed as the sum of even and odd components.
x(t) = x_e(t) + x_o(t)
Where:
  x_e(t) is the even component of the signal,
  x_o(t) is the odd component of the signal.
'''
verify = even + odd
verify.trim()

# Displaying the results
x.compare(even, odd, verify)
```

---

## Generation of different types of signals, using basic operations

### USING UNIT IMPULSE

**PROBLEM**

Generation of different types of signals using operations involving unit impulse signals. Given:

$$
x[n] = 2 \cdot \delta[n + 2] - \delta[n - 4]
$$

Where \( -5 < n < 5 \).

**Getting the environment ready**

Python 3.10 is installed in the system and added to the system variables. The library is installed through pip with the command `pip install wiggles`. VS Code is used for coding and testing. The code is evaluated and displayed using the `show()` or `compare()` function in Wiggles.

**PROGRAM CODE**

```python
from wiggles import signals as sp

# Generating unit impulse signal
us = sp.unit_impulse()
us.name = "unit impulse"

# Performing operation
x = (2 * us.TimeShift(2)) - us.TimeShift(-4)
x.name = "result"

# Trimming and displaying result
x.trim()
us.compare(x)
```

---

### USING UNIT STEP

**PROBLEM**

Generation of different types of signals using operations involving unit step signals. Given:

$$
x[n] = n \cdot [u[n] - u[n - 10]] + 10 \cdot e^{-0.3[n - 10]} \cdot [u[n - 10] - u[n - 20]]
$$

Where \( 0 \leq n \leq 20 \).

**Getting the environment ready**

Python 3.10 is installed in the system and added to the system variables. The library is installed through pip with the command `pip install wiggles`. VS Code is used for coding and testing. The code is evaluated and displayed using the `show()` or `compare()` function in Wiggles.

**PROGRAM CODE**

```python
from wiggles import signals as sp
import numpy as np
import math

# Generating unit step signal
u = sp.unit_step(21)
u.name = "unit step"

# Generating array as desired
n = sp.array(np.arange(0, 21, 1))
n.name = "array"

# Performing operation
x = (n * (u - u.TimeShift(-10))) + (10 * (math.e ** (-0.3 * (n - 10)))) * (u.TimeShift(-10) - u.TimeShift(-20))
x.trim()
x.name = "result"

# Trimming and displaying result
u.compare(n, x)
```

---

### USING ANOTHER SIGNAL

**PROBLEM**

Generation of different types of signals using operations involving other signals. Given:

$$
x[n] = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1]
$$

Starting index = -2

Determine and plot the following sequences:

1. $$ x_1[n] = 2 \cdot x[n - 5] - 3 \cdot x[n + 4] $$
2. $$ x_2[n] = x[3 - n] + x[n] \cdot x[n - 2] $$

**Getting the environment ready**

Python 3.10 is installed in the system and added to the system variables. The library is installed through pip with the command `pip install wiggles`. VS Code is used for coding and testing. The code is evaluated and displayed using the `show()` or `compare()` function in Wiggles.

**PROGRAM CODE**

```python
from wiggles import signals as sp

# Generating wiggles wave using the given amplitude data
x = sp.discrete([1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1], -2)
x.name = "x"

# Operation 1 (a)
x1 = (2 * x.TimeShift(-5)) - (3 * x.TimeShift(4))
x1.name = "operation 1"

# Operation 2 (b)
x2 = x.operate(-1, 3) + (x * x.TimeShift(-2))
x2.name = "operation 2"

# Displaying the result
x.compare(x1, x2)
```

---

## Finding the laplace transform and inverse laplace transform

### LAPLACE TRANSFORM

**Theory**

A function is said to be a piecewise continuous function if it has a finite number of breaks and it does not blow up to infinity anywhere. The Laplace transform of a function \( f(t) \), represented as \( L\{f(t)\} \) or \( F(s) \), is defined by the integral transform:

$$
F(s) = \int_{0}^{\infty} f(t) \cdot e^{-st} \, dt
$$

where \( s = \sigma + j\omega \) is a complex variable.

**Getting the environment ready**

Python 3.10 is installed in the system and added to the system variables. The library is installed through pip with the command `pip install wiggles`. VS Code is used for coding and testing. The code is evaluated and displayed using the `show()` or `compare()` function in Wiggles.

**PROBLEM**

Find the Laplace transform of the following signals:

1. \( x(t) = 2 \cdot \delta(t) + e^{-3t} \)
2. \( x(t) = u(t-1) - 2e^{-t} \)

**PROGRAM CODE 1**

```python
from wiggles import symbols as sy

# Given Expression
def x(t):
    return sy.unit_impulse(t) + sy.exp(-3 * t)

# Making time domain object
expression = sy.time_domain(x)
print("The Expression in time Domain: ", expression)

# Laplace transformation
y = expression.laplace_transform()
print("The Expression in frequency Domain is: ", y)
```

**PROGRAM CODE 2**

```python
from wiggles import symbols as sy

# Given Expression
def x(t):
    return sy.unit_step(t - 1) - sy.exp(-2 * (-t))

# Making time domain object
expression = sy.time_domain(x)
print("The Expression in time Domain: ", expression)

# Laplace transformation
y = expression.laplace_transform()
print("The Expression in frequency Domain is: ", y)
```

---

### INVERSE LAPLACE TRANSFORM

**Theory**

The inverse Laplace transform of a function \( F(s) \) is given by:

$$
f(t) = \frac{1}{2\pi i} \int_{T - i\infty}^{T + i\infty} F(s) \cdot e^{st} \, ds
$$

where the integration is along the vertical line \( \text{Re}(s) = \gamma \) in the complex plane, with \( \gamma \) being greater than the real part of all singularities of \( F(s) \).

**Getting the environment ready**

Python 3.10 is installed in the system and added to the system variables. The library is installed through pip with the command `pip install wiggles`. VS Code is used for coding and testing. The code is evaluated and displayed using the `show()` or `compare()` function in Wiggles.

**PROBLEM A**

Find the inverse Laplace transform of the following signals:

1. \( X(s) = \frac{10s^2 + 4}{s(s + 1)(s + 2)^2} \)
2. \( X(s) = \frac{s^3 + 2s + 6}{s(s + 3)(s + 1)^2} \)

**PROGRAM CODE 1**

```python
from wiggles import symbols as sy

# Given Expression
def x(s):
    return (10 * s**2 + 4) / (s * (s + 1) * (s + 2)**2)

# Making frequency domain object
expression = sy.frequency_domain(x)
expression.name = "X(s)"
print("The Expression in frequency Domain: ", expression)

# Inverse Laplace transformation
y = expression.inverse_laplace_transform()
y.name = "x(t)"
print("The Expression in Time Domain is: ", y)
```

**PROGRAM CODE 2**

```python
from wiggles import symbols as sy

# Given Expression
def x(s):
    return (s**3 + 2 * s + 6) / (s * (s + 3) * (s + 1)**2)

# Making frequency domain object
expression = sy.frequency_domain(x)
expression.name = "X(s)"
print("The Expression in frequency Domain: ", expression)

# Inverse Laplace transformation
y = expression.inverse_laplace_transform()
y.name = "x(t)"
print("The Expression in Time Domain is: ", y)
```

**PROBLEM B**

Use commands to fragment the expression and find the inverse Laplace transform:

Given:

$$
X(s) = \frac{4s^5 + 20s^4 + 11s^3 + 10s^2 - 12}{s^4 + 5s^3 + 8s^2 + 4s}
$$

**PROGRAM CODE 1**

```python
from wiggles import symbols as sy

# Given Expression
def x(s):
    return (4 * s**5 + 20 * s**4 + 11 * s**3 + 10 * s**2 - 12) / (s**4 + 5 * s**3 + 8 * s**2 + 4 * s)

# Making frequency domain object
expression = sy.frequency_domain(x)
expression.name = "X(s)"
print("The Expression in frequency Domain: \n", expression)

# Expanding and fragmenting the expression
expression.apart()
print("The Expanded and processed expression: \n", expression)

# Inverse Laplace transformation
y = expression.inverse_laplace_transform()
y.name = "x(t)"
print("The Expression in Time Domain is: \n", y)
```

---

### POLES AND ZEROS

**Theory**

The zeros are the roots of the numerator, and the poles are the roots of the denominator of a transfer function.

**Getting the environment ready**

Python 3.10 is installed in the system and added to the system variables. The library is installed through pip with the command `pip install wiggles`. VS Code is used for coding and testing. The code is evaluated and displayed using the `show()` or `compare()` function in Wiggles.

**PROBLEM**

Find the roots of the numerator and the denominator to compute the poles and the zeros of the expression:

Given:

$$
X(s) = \frac{s^2 + 3s + 1}{s^3 + 4s^2 + 3s}
$$

**PROGRAM CODE**

```python
from wiggles import symbols as sy

# Given Expression
def x(s):
    return (s**2 + 3 * s + 1) / (s**3 + 4 * s**2 + 3 * s)

# Creating frequency domain object
expression = sy.frequency_domain(x)
expression.name = "X(s)"
print("The Expression in frequency Domain: \n", expression)

# Finding out poles and zeros and displaying
polezero = expression.roots()
print("Poles of the expression:", polezero['poles'])
print("Zeros of the expression:", polezero['zeros'])
```
