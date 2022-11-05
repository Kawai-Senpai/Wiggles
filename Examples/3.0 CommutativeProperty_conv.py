from wiggles import signals as sp

#making two test signals
x1 = sp.discrete([-1,2,-3,1],-1)
x1.name="x1"
x2 = sp.discrete([3,0,1,-4],-3)
x2.name="x2"

'''
Commutative Property of Convolution:
The commutative property of convolution states that the order in which 
we convolve two signals does not change the result,
i.e.,
x1(t)*x2(t)=x2(t)*x1(t)
'''

#Calculating LHS:
lhs = x1.convolve(x2)

#Calculaing RHS:
rhs = x2.convolve(x1)

#LHS = RHS, Displaying both the signal
lhs.compare(rhs)