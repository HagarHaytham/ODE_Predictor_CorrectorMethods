# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 20:27:05 2018

@author: hagar
"""
from pccommon import Point 
from pccommon import GetF
import numpy as np


#assume x after the last point in table ##Error
def AdamsBashforth(xpoints,ypoints,equation,xs,error):
    points=[] #contains all given points
    f=[] #all calculated f(x,y)
    y0 = 0
    yCorrect = 0
    yPredict = 0
    iterations = 5
    #result
    evalYs=[] 
    approxErrors=[]
    #Table: 1st row: f, 2nd row: delta f ...
    matrix= np.zeros((5,6)) #check ?? 5/6

    #calculate f for the given points
    for i in range (len(xpoints)):
        tempF = GetF(xpoints[i],ypoints[i],equation)
        points.append(Point(xpoints[i],ypoints[i],tempF))
        f.append(tempF)
    for i in range (6-len(f)):
        f.append(0)

    #step
    h = abs(points[1].x-points[0].x)

    for l in range (0,len(xs)):
        #Fill the table with intial values 
        matrix[0] = f
        for j in range (1,len(xpoints)):
            for k in range (0,len(xpoints)-j):
                matrix[j][k] = matrix[j-1][k+1]-matrix[j-1][k]

        for i in range (iterations):
            yPrevious = yCorrect
            if i == 0:
                y0 = points[-1].y
                yPredict = y0+h*(points[-1].f+0.5*matrix[1][len(xpoints)-2]+(float(5)/12)*matrix[2][len(xpoints)-3]+ (float(3)/8)*matrix[3][len(xpoints)-4]+ (float(251)/720)*matrix[4][len(xpoints)-5])
                yPrevious = yPredict
                #put f(x,y) in the table
                matrix[0][len(xpoints)] = GetF(xs[l],yPredict,equation)
                
            #calculate all new values in the table
            for j in range (0,len(xpoints)-1):
                    matrix[j+1][len(xpoints)-j-1] = matrix[j][len(xpoints)-j]-matrix[j][len(xpoints)-j-1]

            yCorrect = y0+h*(matrix[0][len(xpoints)]-0.5*matrix[1][len(xpoints)-1]-(float(1)/12)*matrix[2][len(xpoints)-2]-(float(1)/24)*matrix[3][len(xpoints)-3]-(float(19)/720)*matrix[4][len(xpoints)-4])
            #check stopping criteria
            if (abs((yCorrect-yPrevious)/yCorrect*1.0))*100.0 <= error:
                break
            matrix[0][len(xpoints)] = GetF(xs[l],yCorrect,equation)
        #put calculated values in table
        xpoints.append(xs[l])
        ypoints.append(yCorrect)
        if len(xpoints) > 5:
            xpoints.pop(0)
            ypoints.pop(0)
            f.pop(0)
            f.append(GetF(xs[l],yCorrect,equation))
        else: 
            f[len(xpoints)-1]=(GetF(xs[l],yCorrect,equation))
        evalYs.append(yCorrect)
        approxErrors.append((abs((yCorrect-yPrevious)/yCorrect*1.0))*100.0)
    return evalYs,approxErrors,max(approxErrors)

            

                
