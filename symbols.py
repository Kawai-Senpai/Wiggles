import sympy as sym
from sympy.abc import s,t
import sympy.integrals as integrals
from sympy.functions import *
import copy
import random
from wiggles.signals import *

def unit_step(n):
    return Heaviside(n)

def unit_impulse(n):
    return DiracDelta(n)

def exp(n):
    return sym.exp(n)

def sin(n):
    return symfun.sin(n)

def cos(n):
    return symfun.cos(n)

#Useful utility functions to enable addition, sub, etc
class utilities():

    def make_name(self):
        return random.randint(0,100)

    def process(self):
        self.expression = sym.expand(self.expression)
        self.expression = sym.apart(self.expression)
        
    def expand(self):
        self.expression = sym.expand(self.expression)
    
    def apart(self):
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
    
    def show(self):
        (self.to_continuous()).show()

    def compare(self,obj,obj1=None,obj2=None,obj3=None,obj4=None,spacing=None):
        
        if(obj1!=None):
            self.to_continuous().compare(obj.to_continuous(),obj1.to_continuous(),spacing)
        elif(obj2!=None):
            self.to_continuous().compare(obj.to_continuous(),obj1.to_continuous(),obj2.to_continuous(),spacing)
        elif(obj3!=None):
            self.to_continuous().compare(obj.to_continuous(),obj1.to_continuous(),obj2.to_continuous(),obj3.to_continuous(),spacing)
        elif(obj4!=None):
            self.to_continuous().compare(obj.to_continuous(),obj1.to_continuous(),obj2.to_continuous(),obj3.to_continuous(),obj4.to_continuous(),spacing)
        else:
            self.to_continuous().compare(obj.to_continuous(),spacing)

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

    def laplace_transform(self,process=0):

        if(process==1):
            self.process()
        llt = integrals.laplace_transform(self.expression,t,s)
        if(type(llt) == tuple):
            temp = frequency_domain(sympy_exp=(llt[0]))
            temp.residue = llt[1:3]
        else:
            temp = frequency_domain(sympy_exp=llt)
        return temp

    def fourier_transform(self,process=0):
        
        if(process==1):
            self.process()
        llt = integrals.fourier_transform(self.expression,t,s)
        if(type(llt) == tuple):
            temp = frequency_domain(sympy_exp=(llt[0]))
            temp.residue = llt[1:3]
        else:
            temp = frequency_domain(sympy_exp=llt)
        return temp

    def to_continuous(self,start=0,stop=1,step=0.001):
        change = continuous(func=self.quick_evaluate,start=start,stop=stop,step=step)
        change.name = self.name
        change.domain = 'frequency'
        return change

    def solve(self,equals=0):
        return sym.solve(self.expression-equals, t)

    def poles(self):
        return sym.solve((self.expression)**-1, t)

    def zeros(self):
        return sym.solve(self.expression, t)

    def roots(self):
        dic = {'zeros':self.zeros(),'poles':self.poles()}
        return dic

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

    def inverse_laplace_transform(self,process=0):
        
        if(process==1):
            self.process()
        llt =  integrals.inverse_laplace_transform(self.expression,s,t)
        temp = time_domain(sympy_exp=llt)
        return temp

    def inverse_fourier_transform(self,process=0):
        
        if(process==1):
            self.process()
        llt =  integrals.inverse_fourier_transform(self.expression,s,t)
        temp = time_domain(sympy_exp=llt)
        return temp

    def to_continuous(self,start=0,stop=1,step=0.001):
        change = continuous(func=self.quick_evaluate,start=start,stop=stop,step=step,name=self.name)
        change.xlabel= "frequency"
        change.domain = 'frequency'
        return change

    def solve(self,equals=0):
        return sym.solve(self.expression-equals, s)

    def poles(self):
        return sym.solve((self.expression)**-1, s)

    def zeros(self):
        return sym.solve(self.expression, s)

    def roots(self):
        dic = {'zeros':self.zeros(),'poles':self.poles()}
        return dic


