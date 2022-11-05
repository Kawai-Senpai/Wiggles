import math
from wiggles import signals as sp

#Adjust using these variables
A = 1
a = -5
f = 7
w = 2*f*math.pi
Q= 0

#The exp function
def exp(t):
    return A*math.exp(-1*a*t)

#The cos function
def cos(t):
    return A*math.cos((w*t)+Q)

#building and operating on the signal
expwave = sp.continuous(exp)
sinwave = sp.continuous(cos)
expsin = expwave*sinwave

#Adjusting properties and displaying the signal
expwave.name = "Exponentially Growing Wave"
sinwave.name = "Cos Wave"
expsin.name = "Exponentially Growing Cos"

expwave.compare(sinwave,expsin,spacing=0.407) 

