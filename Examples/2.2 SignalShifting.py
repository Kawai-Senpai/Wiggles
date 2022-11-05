from wiggles import signals as sp

#Test signal y; Making Discrete signal using wiggles
y = sp.discrete([2,-2,3,-3,4],-3)
y.name="y"

#shifting the signal 'y' by 1
y1 = y.TimeShift(1)

#comparing two signals
y.compare(y1)
