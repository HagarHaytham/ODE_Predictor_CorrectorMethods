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
    f=eval(equation,{'__builtins__': None},
    {'x': x,'y':y,'cos':cos,'sin':sin,'tan':tan,'acos':acos,'asin':asin,
     'atan':atan,'exp':exp,'pow':pow, 'sqrt': sqrt,'log10':log10,'log':log, #ln
     'fabs':fabs,'radians':radians,'degrees':degrees,'cosh':cosh,'acosh':acosh,
     'sinh':sinh,'asinh':asinh,'tanh':tanh,'atanh':atanh,'pi':pi,'e':e})
    return f
        
