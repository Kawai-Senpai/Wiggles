from wiggles import signals as sp

#making two test signals
x = sp.discrete([-1,2,-3,1],0)
x.name="x"
y = sp.discrete([3,1,1,-4],0)
y.name="y"

#Performing operation and displaying the result
result = x/y
x.compare(y,result)
