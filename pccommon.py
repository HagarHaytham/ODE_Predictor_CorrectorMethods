# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 01:53:29 2018

@author: hagar
"""

from math import *

class Point:
    def __init__(self,x,y,f):
        self.x=x
        self.y=y
        self.f=f
    
def GetF(x,y,equation):
    #should add all kind of functions that can be entered ,, cos ..... etc
    f=eval(equation,{'__builtins__': None},{'cos':cos,'sin':sin,'x': x,'y':y,'exp':exp, 'sqrt': sqrt})
    return f
        
def StoppingCriteria (myApproxError,approxerror,i,itterations):
    if (approxerror==1):
        return i<itterations
    else:
        return myApproxError>approxerror