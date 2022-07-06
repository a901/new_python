# -*- coding: utf-8 -*-
"""
Created on 5/18, 2022

@author: a4691

分段長條圖

預設資料 wiki各國語言



"""
from matplotlib import pyplot as plt

from matplotlib import animation as pan
import random
import numpy as np
import scipy.stats
from scipy.stats import norm
import pandas as pd
from wand.image import Image
import imageio





m=7

def barh(k):   #主函式
    mean, sigma = 100, 15
    
    
    
    x=[]
    y=[]
    x2=[]
    plt.figure(figsize=(50,15))
    #plt.clf()
    
    plt.title('Wikipedia Page Views Per Country - Sep 2018 ~ 30 Sep 2018',fontsize=25)
    plt.xlabel('Monthly requests per person',fontsize=30)
   # plt.ylabel('Country / Total monthly requests',fontsize=30)
    
    name0=['United States(#1, 3.2B)','Japan(#2, 1.1B)','Germany(#3, 907M)',"United Kingdom(#4, 748M)","India(#5, 73.4M)",
    "France(#6, 570M)","Russia(#7, 546M)","         Italy(#8, 532M)","Canada(#9, 387M)","       Brazil(#10, 319M)",
    "Mexico(#11, 282M)","Netherlands(#12, 279M)","Spain(#13, 275M)","         Iran(#14, 260M)","Poland(#15, 249M)",
    "Australia(#16, 224M)", "Taiwan(#17, 217M)", "China(#18, 196M)","    Indonesia(#19, 190M)","Ukraine(#20, 177M)",
    
    "Pakistan(#21, 164M)","Seweden(#22, 144M)","Argentina(#23, 142M)","  Philippines(#24, 119M)","Colombia(#25, 112M)",
    "Hong Kong(#26, 102M)","South Korea(#27, 98.7M)"," Switzerland(#28, 94.8M)","Thailand(#29, 93.1M)","Austria(#30, 89.9M)",
    "Finland(#31, 88.3M)","Malaysia(#32, 83.2M)","Belgiun(#33, 81.7M)","     Vietnam(#34, 78.8M)","Isreal(#35, 78.1M)",
    "Czechia(#36, 72.2M)","Chile(#37, 67.1M)","   Singapore(#38, 65.8M)","Peru(#39, 65.7M)","Norway(#40, 61.2M)",
    
    "Ireland(#41, 59.5M)","Greece(#42, 57.5M)","Saudi Arabia(#43, 56.3M)","Hungary(#44, 55.3M)","Denmark(#45, 55.2M)",
    "Romania(#46, 53.9M)","Kazakhstan(#47, 49.4)","South Africa(#48, 45.4M)","Portugal(#49, 44.5M)","Egypt(#50, 40.4M)",
    "Unknown(#51, 39.7M)","New Zealand(#52, 39.2M)","      Serbia(#53, 38.8M)","UAE(#54, 37.9M)","Morocco(#55, 37.6M)",
    "Bulgaria(#56, 35.9M)","Nigeria(#57, 33.0M)","Belarus(#58, 32.2M)","Dominican Rep.(#59, 30.1M)","Croatia(#60, 29.9M)",
    
    "Bangladesh(#61, 29.1M)","Ecuador(#62, 28.3M)","   Venezuela(#63, 27.0M)","Algeria(#64, 26.6M)","Slovakia(#65, 23.0M)",
    
           
    ]
    
    long=[9.7, 8.5, 11.0, 11.3, 0.6,
          8.5, 3.7, 8.8, 10.4, 1.5,
          2.3, 16.2, 5.9, 3.2, 6.5,
          9.0, 9.2 ,0.1, 0.7, 4.2,
          
          0.8, 14.1, 3.2, 1.1, 2.2,
          13.8, 1.9, 11.2, 1.3, 10.2,
          16.0, 2.6, 7.2, 0.8, 8.8,
          6.8, 3.8, 11.7, 2.1, 11.5,
          
          12.4, 5.3, 1.7, 5.7, 9.5,
          2.7, 2.7, 0.8, 4.3, 0.4,
          0, 8.0, 5.5, 4.0, 1.1,
          5.1, 0.2, 3.4, 3.0, 7.2,
          
          0.2, 1.7, 0.9, 0.6, 4.2,
         
          ] 
    en=[92.3, 3.7, 18.7, 94.0, 86.4,
        14.8, 13.6, 10.2, 84.8, 13.8,
        11.6, 55.5, 16.2, 68.7, 15.0,
        94.6, 9.2, 67.1, 34.6, 17.7,
        
        97.4, 35.3, 12.9, 90.0, 8.3,
        26.2, 24.9, 23.4, 25.8, 17.4,
        32.9, 68.8, 27.7, 23.7, 29.3,
        22.6, 12.7, 82.0, 9.9, 44.2,
        
        84.4, 48.6, 29.3, 29.2, 49.8,
        45.1, 5.9, 92.8, 38.0, 33.3,
        57.2, 94.7, 42.6, 71.2, 15.9,
        43.2, 96.9, 9.1, 9.6, 50.3,
        
        76.5, 9.2, 14.0, 11.7, 34.5, 
        
        
        ]
    long2=[1,2,3,4,5,6,7,8]
    plt.axis([0, 16.5, 0, 8])#x y軸 範圍
    
    for i in range(k,k+m):
        j=k+m-1-i
        x0 = (i+1)
        y0=j+1     
        x20=(i+1)*2
        print("x0=",x0," y0=",y0)
        
        x.append(long[i]*en[i]/100)
        x2.append(long[i]*(100)/100)
        
        y.append(y0)

    
    
    plt.barh(y, x2, color='grey', label='Other versions',height=0.8)  # 水平長條圖 。 垂直長條圖為 bar
    plt.barh(y, x,color='red', label='English version' ,height=0.8)
    
    #plt.bar(x, history_scores, color='green', label='History', bottom=math_scores)
    name=name0[k:k+m]
    plt.yticks(y, name,fontsize=30)
    plt.tick_params(axis="x",labelsize=35)

    
    
    plt.legend(bbox_to_anchor=(1,1), loc='upper left',fontsize=25) #右上方圖利    
    filename = "f" + str(k) + ".png"
    plt.savefig(filename)
    plt.show()                        # 顯示 ***********************************************
    
    
    
    
 
#fig0=plt.figure(figsize=(20,15))
#ani = pan.FuncAnimation(fig0,barh,interval=1200,frames=range(10),blit=True)
#ani.save("barh4.gif",writer='imagemagick')
plt.show() 
   

images = []

n=65+1-m
#把一開始儲存檔案名稱的列表叫出，逐一存入圖片列表
for i in range(n):
    j=n-1-i
    barh(i)
    print("i=",i)
    
    
for i in range(n):
    
    filename = "f" + str(i) + ".png"
    images.append(imageio.imread(filename))

imageio.mimsave('output_fast.gif', images, fps=0.9)#fps每秒帧數

    

