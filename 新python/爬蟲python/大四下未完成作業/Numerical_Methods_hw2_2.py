# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 20:40:08 2021

@author: User
"""
import math 

import sys
 
path = sys.executable
 
print(path)

k="1"

def aa(k):
    print("sss"+k)
    
    



a0=[[6.03,1.99,3.01,1],[-4.81,9.34,0.987,1],[4.16,-1.23,1.27,1]]

a1=[[6.03,1.99,3.01,1],[-4.81,9.34,0.987,1],[4.16,-1.23,1.27,1]]

a=[[7.0,-3,4,6],[2,5,3,-5],[-3,2,6,2]]



f=4
def pr():
    print()
    for i in range(3):
        for j in range(4):
            print(round(a[i][j],10),end=" ")
        print()


def c():
    for h in range(2):
        for i in range(h+1,3):
            g=a[i][h]/a[h][h]
            g=round(g,f)
            for j in range(h,4):
                a[i][j]-=round(a[h][j]*g,f)
                a[i][j]=round(a[i][j],f)
    pr()

def ans(h):
    hh=h
    for i in range(3):
        g=a[i][3]
        for j in range(3):
            if j==i:
                continue
            g-=a[i][j]*hh[j]
        hh[i]=g/a[i][i]
    print(round(hh[0],5)," ",round(hh[1],5)," ",round(hh[2],5))
    return hh
            
pr()
k=[0,0,0]
for t in range(30):
    print("",t,":",end=" ")
    k=ans(k)







