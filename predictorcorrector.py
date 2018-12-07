# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 19:46:24 2018

@author: hagar
"""

# input up till now is 
#1-list of points 
#2-equation of the ode
#3-The desired technique as a string
#4-The point to caluculate at 

#May be 
#5-no of itterations and we should calculte the error in this case ?

def PredictorCorrector(Xpoints,Ypoints,equation,technique,x):
    output=0
    if technique=="Milne's":
        output=1 # here we should call Milne's function technique
    elif technique=="AdamsBashforth":
        output=2
    elif technique=="AdamsMoulton":
        output=3
    elif technique=="Adams":
        output=4
    return output

        