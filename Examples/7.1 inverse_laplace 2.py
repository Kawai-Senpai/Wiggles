from wiggles import symbols as sy 

#Given Expression
def x(s):
    return (10*(s**2)+4)/(s*(s+1)*(s+2)**2)

#Making frequency domain object
expression = sy.frequency_domain(x)
expression.name="X(s)"
print("The Expression in frequency Domain: ",expression)

#Inverse Laplase transformation
y = expression.inverse_laplace_transform()
y.name="x(t)"
print("The Expression in Time Domain is: ",y)

#Plotting the signals
expression.compare(y)