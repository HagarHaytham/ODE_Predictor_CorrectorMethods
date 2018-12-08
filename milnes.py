# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 20:25:13 2018

@author: hagar
"""

import point 
import math 

def GetF(x,y,equation):# gets F some how from the equation 
    # we will figure out that later XD
    #pass
    
    #working on a dummy  equation just to check the output
    f=4*math.exp(0.8*x) -0.5*y
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
        points.append(point.Point(xpoints[i],ypoints[i],GetF(xpoints[i],ypoints[i],equation)))
    
    points.append(point.Point(x,0,0))
    myNum = len(points)-1
    h= points[1].x-points[0].x
    points[myNum].y= Predictor(myNum,points,h)
    i=0
    while i<itterations:
        points[myNum].y=Corrector(myNum,points,h)
        points[myNum].f=GetF(points[myNum].x , points[myNum].y ,equation)
        i+=1
        
    return points[myNum].y
    
#x=[-3,-2,-1,0]
#y=[-4.547302,-2.30616,-0.3929953,2]
#out=Milnes(x,y,"anything",1,2)
#print (out)