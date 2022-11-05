import math
from wiggles import signals as sp

#Adjust using these variables
A = 2
a = 4

#The exp function
def exp(t):
    return A*math.exp(-1*a*t)

#building the signal
y = sp.continuous(exp)

#Adjusting properties and displaying the signal
y.name="Exponentially Decaying"
y.show() 

