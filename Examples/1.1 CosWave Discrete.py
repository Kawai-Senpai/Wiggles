import math
from wiggles import signals as sp

#Adjust using these variables
A = 2
f = 5
w = 2*f*math.pi
Q= 0

#The cos function
def cos(t):
    return A*math.cos((w*t)+Q)

#building the signal
y = sp.continuous(cos)

#Adjusting properties and displaying the signal
y.name="cos(t)"
y.show() 

#building the Discrete signal
y2 = sp.continuous(cos,step=0.01)
y2.is_descrete=True

#Adjusting properties and displaying the Discrete signal
y2.name="cos[t]"
y2.show() 

