# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 20:25:13 2018

@author: hagar
"""

from pccommon import Point 
from pccommon import GetF

def Predictor(i,points,h):
    yp= points[i-4].y+h*(4/3)*(2*points[i-1].f -points[i-2].f + 2*points[i-3].f)
    return yp

def Corrector(i,points,h):
    yc= points[i-2].y + (h/3)*(points[i-2].f +4*points[i-1].f+ points[i].f )
    return yc
    
def StoppingCriteria (myApproxError,approxerror,i,itterations):
    if (approxerror==1):
        return i<itterations
    else:
        return myApproxError>approxerror
       
def Milnes (xpoints,ypoints,equation,x,approxerror):
    itterations=5
    points=[]
    for i in range (len(xpoints)):
        points.append(Point(xpoints[i],ypoints[i],GetF(xpoints[i],ypoints[i],equation)))
    
    points.append(Point(x,0,0))
    myNum = len(points)-1
    h= points[1].x-points[0].x
    points[myNum].y= Predictor(myNum,points,h)
    yPrev = Predictor(myNum,points,h)
    myApproxError=1.0
    i=0
    while StoppingCriteria(myApproxError,approxerror,i,itterations)==True:
        points[myNum].y=Corrector(myNum,points,h)
        myApproxError = abs((points[myNum].y-yPrev)/points[myNum].y)
        #print("ycorrected",points[myNum].y,"yPrev",yPrev,"Error",myApproxError)
        yPrev=Corrector(myNum,points,h)
        points[myNum].f=GetF(points[myNum].x , points[myNum].y ,equation)
        i+=1
    return points[myNum].y,myApproxError
