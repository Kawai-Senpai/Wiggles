from wiggles import signals as sp

#making two test signals
x1 = sp.discrete([-1,2,-3,1],-1)
x1.name="x1"
x2 = sp.discrete([3,0,1,-4],-3)
x2.name="x2"
x3 = sp.discrete([5,6,7,8],-2)
x3.name="x3"

'''
Distributive Property of Convolution:
The distributive property of convolution states that 
if there are three signals x1(t),x2(t)and x3(t), 
then the convolution of x1(t) is distributive over the addition,
x1(t)*[x2(t)+x3(t)] = [x1(t)*x2(t)]+[x1(t)*x3(t)]
'''

#Calculating LHS:
lhs = x1.convolve(x2+x3)

#Calculaing RHS:
rhs = (x1.convolve(x2))+(x1.convolve(x3))

#LHS = RHS, Displaying both the signal
lhs.compare(rhs)
