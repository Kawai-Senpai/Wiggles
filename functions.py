from sympy.functions import *
from wiggles.symbols import *
import numpy as np
import sympy.core.numbers as symnum
import sympy.functions as symfun
import pickle

#Exports Wiggles type signal to a file
def export_wiggles(wiggles_obj, file_path):
    with open(file_path, 'wb') as f:
        pickle.dump(wiggles_obj, f)

#Imports Wiggles type signal from a file
def import_wiggles(file_path):
    with open(file_path, 'rb') as f:
        wiggles_obj = pickle.load(f)
    return wiggles_obj

#Easily create a symbolic unit_step (Heaviside) in sympy or symbols wiggles format
def unit_step(n):
    return Heaviside(n)

#Easily create a symbolic unit_impulse (DiracDelta) in sympy or symbols wiggles format, here with error handling
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

#Easily create a symbolic exp function in sympy or symbols wiggles format
def exp(n):
    return exp(n)

#Easily create a symbolic sin function in sympy or symbols wiggles format
def sin(n):
    return symfun.sin(n)

#Easily create a symbolic cos function in sympy or symbols wiggles format
def cos(n):
    return symfun.cos(n)