# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 20:25:13 2018

@author: hagar
"""

from point import Point 
from math import * 

def GetF(x,y,equation):# gets F some how from the equation 
    #should add all kind of functions that can be entered ,, cos ..... etc
    f=eval(equation,{'__builtins__': None}, {'x': x,'y':y,'exp':exp, 'sqrt': sqrt})
    
    #print("printing f "+str(f))
    return f

def Predictor(i,points,h):
    yp= points[i-4].y+h*(4/3)*(2*points[i-1].f -points[i-2].f + 2*points[i-3].f)
    return yp

def Corrector(i,points,h):
    yc= points[i-2].y + (h/3)*(points[i-2].f +4*points[i-1].f+ points[i].f )
    return yc
    
        
#assume given number of itterations
def Milnes (xpoints,ypoints,equation,x,itterations):
    points=[]
    for i in range (len(xpoints)):
        points.append(Point(xpoints[i],ypoints[i],GetF(xpoints[i],ypoints[i],equation)))
    
    points.append(Point(x,0,0))
    myNum = len(points)-1
    h= points[1].x-points[0].x
    points[myNum].y= Predictor(myNum,points,h)
    i=0
    while i<itterations:
        points[myNum].y=Corrector(myNum,points,h)
        points[myNum].f=GetF(points[myNum].x , points[myNum].y ,equation)
        i+=1
        
    return points[myNum].y
