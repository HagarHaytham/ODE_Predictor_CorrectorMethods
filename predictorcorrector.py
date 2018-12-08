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
from milnes import Milnes 

# assume for now we take number of itteration as input
def PredictorCorrector(Xpoints,Ypoints,equation,x,technique,itterations):
    output=0
    if technique=="Milne's":
        output=Milnes(Xpoints,Ypoints,equation,x,itterations) # here we should call Milne's function technique
    elif technique=="AdamsBashforth":
        output=2
    elif technique=="AdamsMoulton":
        output=3
    elif technique=="Adams":
        output=4
    return output

        


xs=[-3,-2,-1,0]
ys=[-4.547302,-2.30616,-0.3929953,2]
x=1
itt=2
eq="4*exp(0.8*x) -0.5*y"
out=PredictorCorrector(xs,ys,eq,x,"Milne's",itt)
print (out)