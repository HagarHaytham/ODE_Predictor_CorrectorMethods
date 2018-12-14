# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 19:46:24 2018

@author: hagar
"""

# input up till now is 
#1-list of x points (4 points)
#2-list of y points (4 points)
#3-equation of the ode (string)
#4-The desired technique as a string {"Milne's","AdamsBashforth","AdamsMoulton","Adams"}
#5-list of x points to caluculate at 
#6-Approx Error with default 1 so we just do 5 itterations if not given

#output
#1-list of calculated ys
#2-list of Approx Error for each y
#3-Final approx error 
from milnes import Milnes 
from adams import Adams
from adamsmoulton import AdamsMoulton
from adamsbashforth import AdamsBashforth

def PredictorCorrector(Xpoints,Ypoints,equation,technique,xs,ApproxError=1):
    ys=[]
    errors=[]
    finalerror=0
    if technique=="Milne's":
        ys,errors,finalerror=Milnes(Xpoints,Ypoints,equation,xs,ApproxError) 
    elif technique=="AdamsBashforth":
        ys,errors,finalerror=AdamsBashforth(Xpoints,Ypoints,equation,xs,ApproxError)
    elif technique=="AdamsMoulton":
        ys , errors,finalerror =AdamsMoulton(Xpoints,Ypoints,equation,xs,ApproxError)
    elif technique=="Adams":
        ys, errors, finalerror = Adams(Xpoints,Ypoints,equation,xs,ApproxError)
    return ys ,errors,finalerror

xs=[-0.1,0,0.1,0.2]
ys=[1.0047,1,1.0053,1.0229,1.05517025]
x=[0.3,0.4]
eq="x*y+x**2"
#xs=[-0.1,0,0.1,0.2]
#ys=[1.0047,1,1.0053,1.0229]
#x=0.3
#eq="x*y+x**2"
approx=0.00000000005
out ,errors,error =PredictorCorrector(xs,ys,eq,"Milne's",x,approx)
print (" Milne's      ",out,errors,error)
out ,errors,error =PredictorCorrector(xs,ys,eq,"Adams",x,approx)
print (" Adams        ",out,errors,error)
out ,errors,error = PredictorCorrector(xs,ys,eq,"AdamsMoulton",x,approx)
print (" AdamsMoulton       ",out,errors,error)
out ,errors,error = PredictorCorrector(xs,ys,eq,"AdamsBashforth",x,approx)
print (" AdamsBashforth       ",out,errors,error)