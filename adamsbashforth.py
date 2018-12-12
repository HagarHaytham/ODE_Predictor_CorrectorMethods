# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 20:27:05 2018

@author: hagar
"""
from point import Point 
from math import * 
import numpy as np

def GetF(x,y,equation):# gets F some how from the equation 
    #should add all kind of functions that can be entered ,, cos ..... etc
    f=eval(equation,{'__builtins__': None}, {'x': x,'y':y,'exp':exp, 'sqrt': sqrt})
    
    #print("printing f "+str(f))
    return f

#assume x after the last point in table
def AdamsBashforth(xpoints,ypoints,equation,x,error):
    points=[]
    f=[]
    y0 = 0
    y = 0
    matrix= np.zeros((5,5))
    #calculate f
    for i in range (len(xpoints)):
        tempF = GetF(xpoints[i],ypoints[i],equation)
        points.append(Point(xpoints[i],ypoints[i],tempF))
        f.append(tempF)
    for i in range (5-len(f)):
        f.append(0)
    #step
    h = abs(points[1].x-points[0].x)
    matrix[0] = f
    
    for j in range (1,len(xpoints)):
        for k in range (0,len(xpoints)-j):
            matrix[j][k] = matrix[j-1][k+1]-matrix[j-1][k]
            
    for i in range (5): #iterations
        print("matrix1: " , matrix)
        if i == 0:
            y0 = points[-1].y
            y = y0+h*(points[-1].f+0.5*matrix[1][len(xpoints)-2]+(5/12)*matrix[2][len(xpoints)-3]+ (3/8)*matrix[3][len(xpoints)-4]+ (251/720)*matrix[4][len(xpoints)-5])
            #put y in the table
            print("y: ", points[-1].f)
            matrix[0][len(xpoints)] = GetF(x,y,equation)
            
        #calculate all new values in the table
        for j in range (0,len(xpoints)-1):
                matrix[j+1][-j-2] = matrix[j][-j-1]-matrix[j][-j-2]
                
        print("matrix3: " , matrix)
        #Assume f1 hya l f kol marra bt7sbha ??
        y = y0+h*(matrix[0][len(xpoints)-1]-0.5*matrix[1][len(xpoints)-2]-(1/12)*matrix[2][len(xpoints)-3]-(1/24)*matrix[3][len(xpoints)-5]-(19/720)*matrix[4][len(xpoints)-5])

        matrix[0][len(xpoints)] = GetF(x,y,equation)
        
            
AdamsBashforth([-0.1,0,0.1,0.2],[1.0047,1,1.0053,1.0229],"x*y+x**2",0.3,0)
                
