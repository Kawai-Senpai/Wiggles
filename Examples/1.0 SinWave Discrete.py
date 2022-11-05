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

#building the Discrete signal
y2 = sp.continuous(sin,step=0.01)
y2.is_descrete=True

#Adjusting properties and displaying the Discrete signal
y2.name="sin[t]"
y2.show() 

