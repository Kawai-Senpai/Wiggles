import math
from wiggles import signals as sp

#Adjust using these variables
A = 2
f = 5
w = 2*f*math.pi
Q= 0

#The sin function
def sin(t):
    return A*math.sin((w*t)+Q)

#building the signal
y = sp.continuous(sin)

#Adjusting properties and displaying the signal
y.name="sin(t)"
y.show() 

