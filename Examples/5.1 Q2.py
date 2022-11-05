import wiggles.signals as sp     
import numpy as np
import math

#generating unit step signal
u=sp.unit_step(21)
u.name="unit step"

#generating array as desired
n=sp.array(np.arange(0,21,1))
n.name="array"

#performing operation
x=(n*(u-u.TimeShift(-10)))+(10*(math.e**(-0.3*(n-10))))*(u.TimeShift(-10)-u.TimeShift(-20))
x.trim()
x.name="result"

#Trimming and Displaying result
u.compare(n,x)


