# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 20:25:13 2018

@author: hagar
"""

from pccommon import *

def MilnesPredictor(i,points,h):
    yp= points[i-4].y+h*(4/3)*(2*points[i-1].f -points[i-2].f + 2*points[i-3].f)
    return yp

def MilnesCorrector(i,points,h):
    yc= points[i-2].y + (h/3)*(points[i-2].f +4*points[i-1].f+ points[i].f )
    return yc
    
       
def Milnes (xpoints,ypoints,equation,evalxs,approxerror):
    itterations=5
    points=[]
    for i in range (len(xpoints)):
        points.append(Point(xpoints[i],ypoints[i],GetF(xpoints[i],ypoints[i],equation)))
    
    evalYs=[]
    approxErrors=[]
    for k in range (len(evalxs)):
        points.append(Point(evalxs[k],0,0))
        myNum = len(points)-1
        h= points[1].x-points[0].x
        points[myNum].y= MilnesPredictor(myNum,points,h)
        points[myNum].f=GetF(points[myNum].x , points[myNum].y ,equation)
        yPrev =points[myNum].y
        myApproxError=1
        i=0
        while StoppingCriteria(myApproxError,approxerror,i,itterations):
            points[myNum].y=MilnesCorrector(myNum,points,h)
            myApproxError = abs((points[myNum].y-yPrev)/points[myNum].y)
#            print(k," ycorrected",points[myNum].y,"yPrev",yPrev,"Error",myApproxError)
            yPrev=points[myNum].y
            points[myNum].f=GetF(points[myNum].x , points[myNum].y ,equation)
            i+=1
        evalYs.append(points[myNum].y)
        approxErrors.append(myApproxError)
    return evalYs,approxErrors,max(approxErrors)
