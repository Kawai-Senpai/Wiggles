from wiggles import signals as sp

#Test signal y; Making Discrete signal using wiggles
y = sp.discrete([2,-2,3,-3,4],-3)
y.name="y"

#scaling the signal 'y' by 2
y1 = y.reverse()

#comparing two signals
y.compare(y1)
