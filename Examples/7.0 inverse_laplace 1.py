from wiggles import symbols as sy 

#Given Expression
def x(s):
    return ((s**3)+(2*s)+6)/(s*(s+3)*(s+1)**2)

#Making frequency domain object
expression = sy.frequency_domain(x)
expression.name="X(s)"
print("The Expression in frequency Domain: ",expression)

#Inverse Laplace transformation
y = expression.inverse_laplace_transform()
y.name="x(t)"
print("The Expression in Time Domain is: ",y)

#Plotting the signals
expression.compare(y)