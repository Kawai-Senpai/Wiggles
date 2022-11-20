from sympy.functions import *
from wiggles.symbols import *
import numpy as np
import sympy.core.numbers as symnum
import sympy.functions as symfun

def unit_step(n):
    return Heaviside(n)

def unit_impulse(n, sympy_repr = 1):
    out = DiracDelta(n)

    if(sympy_repr==0):
        if type(out) in [symnum.Infinity,symnum.ComplexInfinity,symnum.NegativeInfinity]:
                    out = np.inf
        elif out == symfun.DiracDelta(0):
                    out = 1
        try:
            out = float(out)
        except:
            out = np.nan
    
    return out

def exp(n):
    return exp(n)

def sin(n):
    return symfun.sin(n)

def cos(n):
    return symfun.cos(n)