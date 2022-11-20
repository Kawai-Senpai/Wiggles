from wiggles import symbols as sy 

#Given Expression
def x(s):
    return (4*(s**5)+20*(s**4)+11*(s**3)+10*(s**2)-12)/((s**4)+5*(s**3)+8*(s**2)+(4*s))

#Making frequency domain object
expression = sy.frequency_domain(x)
expression.name="X(s)"
print("The Expression in frequency Domain: \n",expression)

#Expanding and fragmenting the expression
expression.apart()
print("The Expanded and processed expression: \n",expression)

#Inverse Laplace transformation
y = expression.inverse_laplace_transform()
y.name="x(t)"
print("The Expression in Time Domain is: \n",y)
