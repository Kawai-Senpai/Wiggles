import sympy as sym
from sympy.abc import s,t,x,k
import sympy.integrals as integrals
import copy
import random
from signals import *

#Useful utility functions to enable addition, sub, etc
class utilities():

    def make_name(self):
        return random.randint(0,100)

    def process(self):
        self.expression = sym.expand(self.expression)
        self.expression = sym.apart(self.expression)
        
    def __repr__(self):
        print(self.expression)

    def __str__(self):
        return str(self.expression)

    def __add__(self,n):

        change = copy.deepcopy(self)
        change.expression = change.expression+n
        return change
    
    def __radd__(self,n):
        
        change = copy.deepcopy(self)
        change.expression = n+change.expression
        return change

    def __pow__(self,n):

        change = copy.deepcopy(self)
        change.expression = change.expression**n
        return change
    
    def __rpow__(self,n):
        
        change = copy.deepcopy(self)
        change.expression = n**change.expression
        return change
    
    def __sub__(self,n):

        change = copy.deepcopy(self)
        change.expression = change.expression-n
        return change
    
    def __rsub__(self,n):
        
        change = copy.deepcopy(self)
        change.expression = n-change.expression
        return change

    def __mul__(self,n):

        change = copy.deepcopy(self)
        change.expression = change.expression*n
        return change
    
    def __rmul__(self,n):
        
        change = copy.deepcopy(self)
        change.expression = n*change.expression
        return change

    def __truediv__(self,n):

        change = copy.deepcopy(self)
        change.expression = change.expression/n
        return change
    
    def __rtruediv__(self,n):
        
        change = copy.deepcopy(self)
        change.expression = n/change.expression
        return change
    
#To easily make equations in time domain
class time_domain(utilities):

    #Class variables used for different visual and operational settings
    name = ""

    def __init__(self,func=None,sympy_exp=None,name=chr(random.randint(ord('a'), ord('z')))):

        self.name = name

        if(sympy_exp==None and func!=None):
            self.expression = func(t)
        elif(sympy_exp!=None and func==None):
            self.expression = sympy_exp
        else:
            print("Incorect parameters. Either Provide a function or an sympy expression")

    def __getitem__(self,key):
        return self.evaluate(t,key)
    
    def evaluate(self,variable,value=None):
        if value != None:
            return sym.N(self.expression.subs(variable,value))
        else:
            return sym.N(self.expression.subs(variable))

    def quick_evaluate(self,key):
        return self.evaluate(t,key)

    def laplace_transform(self):

        self.process()
        llt = integrals.laplace_transform(self.expression,t,s)
        if(type(llt) == tuple):
            temp = frequency_domain(sympy_exp=(llt[0]))
            temp.aoc = llt[1:3]
        else:
            temp = frequency_domain(sympy_exp=llt)
        return temp

    def fourier_transform(self):
        
        llt = integrals.fourier_transform(self.expression,t,s)
        if(type(llt) == tuple):
            temp = frequency_domain(sympy_exp=(llt[0]))
            temp.aoc = llt[1:3]
        else:
            temp = frequency_domain(sympy_exp=llt)
        return temp

    def to_continuous(self,start=0,stop=1,step=0.001):
        change = continuous(func=self.quick_evaluate,start=start,stop=stop,step=step)
        change.name = self.name
        change.domain = 'frequency'
        return change

#To easily make equations in time domain
class frequency_domain(utilities):

    #Class variables used for different visual and operational settings
    name = ""

    def __init__(self,func=None,sympy_exp=None,name=chr(random.randint(ord('a'), ord('z')))):

        self.name = name

        if(sympy_exp==None and func!=None):
            self.expression = func(s)
        elif(sympy_exp!=None and func==None):
            self.expression = sympy_exp
        else:
            print("Incorect parameters. Either Provide a function or an sympy expression")

    def __getitem__(self,key):
        return self.evaluate(s,key)

    def evaluate(self,variable,value=None):
        if value != None:
            return sym.N(self.expression.subs(variable,value))
        else:
            return sym.N(self.expression.subs(variable))
    
    def quick_evaluate(self,key):
        return self.evaluate(s,key)

    def inverse_laplace_transform(self):
        
        self.process()
        llt =  integrals.inverse_laplace_transform(self.expression,s,t)
        temp = time_domain(sympy_exp=llt)
        return temp

    def inverse_fourier_transform(self):
        
        self.process()
        llt =  integrals.inverse_fourier_transform(self.expression,s,t)
        temp = time_domain(sympy_exp=llt)
        return temp

    def to_continuous(self,start=0,stop=10,step=0.01):
        change = continuous(func=self.quick_evaluate,start=start,stop=stop,step=step,name=self.name)
        change.xlabel= "frequency"
        change.domain = 'frequency'
        return change


def gg(n):
    return (10*(n**2)+4)/(n*(n+1)*(n+2)**2)

def test(n):
    return sym.exp(-n**2)

a = time_domain(test)
fr = a.fourier_transform()
print(fr)
(fr.to_continuous(start=-1)).show()
