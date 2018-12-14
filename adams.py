# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 20:28:21 2018

@author: hagar

"""
from pccommon import GetF
def Adams(xpoints,ypoints,equation,xvalues,stopping_criteria):
    h=xpoints[1]-xpoints[0]
    f=[]
    x=[]
    y=[]
    answers=[]
    errors=[]
    k=len(xpoints)
    eq="4*exp(0.8*x) -0.5*y"
    for i in range(k):
        value=GetF(xpoints[i],ypoints[i],equation)
        f.append(value)
        x.append(xpoints[i])
        y.append(ypoints[i])
            
    for xval in xvalues:
        n=len(f)
        i=n-1
        predictor=y[i]+(h/24)*(55*f[i]-59*f[i-1]+37*f[i-2]-9*f[i-3])
        corrector=predictor
        iteration=5
        approximate_error=100
        while ( iteration > 0 and approximate_error > stopping_criteria):
            prev_corrector=corrector
            corrector=y[i]+(h/24)*(9*corrector+19*f[i]-5*f[i-1]+f[i-2])
            approximate_error=abs( (corrector- prev_corrector) / corrector )
            iteration-=1
        value=GetF(xval,corrector,equation) 
        f.append(value)
        x.append(xval)
        y.append(corrector)
        answers.append(corrector)
        errors.append(approximate_error)
    return answers , errors
    

