from wiggles import symbols as sy 

#given expression
def x(s):
    return ((s**2)+(3*s)+1)/((s**3)+(4*(s**2))+(3*s))

#creating frequency domain object
expression = sy.frequency_domain(x)
expression.name="X(s)"
print("The Expression in frequency Domain: \n",expression)

'''
alternative way:
print("Poles of the expression:",expression.poles())
print("zeros of the expression:",expression.zeros())
'''

#Finding out poles and zeros and displaying
polezero = expression.roots()
print("Poles of the expression:",polezero['poles'])
print("zeros of the expression:",polezero['zeros'])