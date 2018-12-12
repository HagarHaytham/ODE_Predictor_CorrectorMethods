# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 20:28:21 2018

@author: hagar

"""
from math import *
def Adams(xpoints,ypoints,equation,x,stopping_criteria):
    h=xpoints[1]-xpoints[0]
    f=[]
    n=len(xpoints)
    for i in range(n):
        value=get_value(xpoints[i],ypoints[i],equation)
        f.append(value)
    i=n-1
    predictor=ypoints[i]+(h/24)*(55*f[i]-59*f[i-1]+37*f[i-2]-9*f[i-3])
    corrector=predictor
    iteration=5
    approximate_error=100
    while ( iteration > 0 and approximate_error > stopping_criteria):
        prev_corrector=corrector
        corrector=ypoints[i]+(h/24)*(9*corrector+19*f[i]-5*f[i-1]+f[i-2])
        approximate_error=abs( (corrector- prev_corrector) / corrector )
        iteration-=1
    return corrector , approximate_error
    

def get_value(x,y,equation):
        f=eval(equation,{'__builtins__': None}, {'cos':cos,'sin':sin,'x': x,'y':y,'exp':exp, 'sqrt': sqrt})
        return f
