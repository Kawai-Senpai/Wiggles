import wiggles.signals as sp

#generating unit impulse signal
us=sp.unit_impulse()
us.name="unit impulse"

#performing operation
x=(2*us.TimeShift(2))-us.TimeShift(-4)
x.name="result"

#Trimming and Displaying result
x.trim()
us.compare(x,x,x)