from wiggles import symbols as sy 

#Given Expression
def x(t):
    return sy.unit_impulse(t)+sy.exp((-3)*t)

#Making time domain object
expression = sy.time_domain(x)
expression.name="x(t)"
print("The Expression in time Domain: ",expression)

#Converting to a continuous signal (a 'wiggles' signal type object)
pl1 = expression.to_continuous()

#computing the Laplase transform
y = expression.laplace_transform()
y.name="X(s)"
print("The Expression in frequency Domain is: ",y)

#Converting to a continuous signal (a 'wiggles' signal type object)
pl2 = y.to_continuous(stop=300,step=0.1)

pl1.compare(pl2)