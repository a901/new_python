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
    
    
aa("11")

print("normal point error: ",round(2.4566666,5),"")


a0=[[6.03,1.99,3.01,1],[-4.81,9.34,0.987,1],[4.16,-1.23,1.27,1]]

a=[[6.03,1.99,3.01,1],[-4.81,9.34,0.987,1],[4.16,-1.23,1.27,1]]

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

def ans():
    h=[0,0,0]
    for i in range(3):
        x=2-i
        g=0
        for j in range(x+1,3):
            g+=round(a[x][j]*h[j],f)
        g=a[x][3]-g
        g=round(g,f)
        h[x]=round(g/a[x][x],f)
        h[x]=round(h[x],f)
    print()
    print(round(h[0],2)," ",round(h[1],2)," ",round(h[2],2))
    


pr()
c()
ans()







