from wiggles import signals as sp

#making two test signals (Starting from different index)
x1 = sp.discrete([-1,2,-3,1],-1)
x1.name="x1"
x2 = sp.discrete([3,0,1,-4],-3)
x2.name="x2"

#Performing convolution and displaying the result
result = x1.convolve(x2)
x1.compare(x2,result)
