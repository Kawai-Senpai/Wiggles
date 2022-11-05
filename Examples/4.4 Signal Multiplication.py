from wiggles import signals as sp

#making two test signals (Starting from different index)
x = sp.discrete([-1,2,-3,1],-1)
x.name="x"
y = sp.discrete([3,0,1,-4],-3)
y.name="y"

#Performing operation and displaying the result
result = x*y
x.compare(y,result)
