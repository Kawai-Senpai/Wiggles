from wiggles import symbols as sy 

#Given Expression
def x(t):
    return sy.unit_step(t-1)-sy.exp((-2)*(-t))

#Making time domain object
expression = sy.time_domain(x)
print("The Expression in time Domain: ",expression)

#Laplase transformation
y = expression.laplace_transform()
print("The Expression in frequency Domain is: ",y)

#Plotting the signals
expression.compare(y)