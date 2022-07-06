# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 03:32:30 2021

@author: a4691
"""
from matplotlib import pyplot as plt
import random
import numpy as np
import scipy.stats
from scipy.stats import norm
import pandas as pd

def Normal_distribution():   #iq 標準差 與 語言比例 top 20 trending videos language in asian countries
    mean, sigma = 100, 15
    x = mean + sigma * np.random.randn(10000)
    x=[]
    y=[]
    for i in range(-45,45):
        x0 = mean +i# random.randrange(-20,20)
        # y0=norm.pdf((x0-100)/sigma)   #标准正态分布
        #if i>0 :
        y0=1-norm.cdf((x0-mean)/sigma)   #
       # else:  y0=norm.cdf((x0-mean)/sigma)   #
            
        print("x0=",x0," y0=",y0)
        x.append(x0)
        y.append(y0)
   # n, bins, patches = plt.hist(x, 50, normed=1, facecolor='g', alpha=0.75)
    #plt.subplot(2,2,1)
    plt.xlabel('Values')
    plt.ylabel('Probability')
    plt.title('random Gaussian Distribution')
    plt.bar(x, y)   #.plot 折線圖
    plt.axis([50, 150, 0, 1])
    plt.savefig('iq_plt.png')
    
    plt.show()
     
    df = pd.DataFrame([
    ['Czech Republic', 10228744], ['France', 61083916], ['Germany', 82400996],
    ['Greece', 10706290], ['Italy', 58147733], ['Netherlands', 16570613],
    ['Poland', 38518241], ['Portugal', 10642836]], columns=['country', 'pop'])
    #plt.pie(df['pop'], labels=df['country'],colors = colors, autopct='%1.2f%%')
   
    
    colors = ['red', 'green', 'lightcoral', 'lightskyblue', 'lavender','brown' ,'blue','gold','yellowgreen','cyan',"yellow"]
    la=['English','Thai','Japanese',"Korean","Filipino/Philippine languages","Malay",
        "Mandarin","Tamil","Cantonese"]
    
#  第一圓餅圖    
    plt.figure(dpi=300)
    da=[1,0,28,1,0,0]
    ti="Japan"
    language=[]
    co=[]
    data=[]
    for i in range(4):  
        if da[i]>0:     
            language.append(la[i])
            co.append(colors[i])
            data.append(da[i])
    plt.subplot(2,2,1) # 分割圖 2行 2列 當前第2個位置
    plt.pie(data, labels=language,colors =co, autopct='%1.2f%%') # 圓餅圖
    plt.title(ti)

#  第一圓餅圖    
    da=[7,0,0,5,17,0,1,0]#17 7  5 1
    ti="Philippine"
    language=[]
    co=[]
    data=[]
    for i in range(8):  
        if da[i]>0:     
            language.append(la[i])
            co.append(colors[i])
            data.append(da[i])
    plt.subplot(2,2,2) # 分割圖 2行 2列 當前第2個位置
    plt.pie(data, labels=language,colors =co, autopct='%1.2f%%') # 圓餅圖
    plt.title(ti)    


    la=['English','Thai','Japanese',"Korean","Filipino/Philippine languages","Malay",
        "Mandarin","Tamil","Cantonese"]
 
#  第三圓餅圖    
    da=[5,0,0,3,0,16,4,2]   #youtube vertical video 16 5 4 3 2 
    ti="Malaysia"
    language=[]
    co=[]
    data=[]
    for i in range(8):  
        if da[i]>0:     
            language.append(la[i])
            co.append(colors[i])
            data.append(da[i])
    plt.subplot(2,2,3) # 分割圖 2行 2列 當前第2個位置
    plt.pie(data, labels=language,colors =co, autopct='%1.2f%%') # 圓餅圖
    plt.title(ti)      

#  第三圓餅圖    
    da=[1,0,0,29,0,0,0,0]   #youtube vertical video 16 5 4 3 2 
    ti="Kerean"
    language=[]
    co=[]
    data=[]
    for i in range(8):  
        if da[i]>0:     
            language.append(la[i])
            co.append(colors[i])
            data.append(da[i])
    plt.subplot(2,2,4) # 分割圖 2行 2列 當前第2個位置
    plt.pie(data, labels=language,colors =co, autopct='%1.2f%%') # 圓餅圖
    plt.title(ti) 

    plt.savefig('yt01.png')
    plt.show()



#  第一圓餅圖    
    da=[0,0,0,0,0,0,30,0]#17 7  5 1
    ti="Taiwan"
    language=[]
    co=[]
    data=[]
    for i in range(8):  
        if da[i]>0:     
            language.append(la[i])
            co.append(colors[i])
            data.append(da[i])
    plt.subplot(2,2,1) # 分割圖 2行 2列 當前第2個位置
    plt.pie(data, labels=language,colors =co, autopct='%1.2f%%') # 圓餅圖
    plt.title(ti)    


    la=['English','Thai','Japanese',"Korean","Filipino/Philippine languages","Malay",
        "Mandarin","Tamil","Cantonese","Hindu","Vietnamese"]
    
 
#  第三圓餅圖    
    da=[0,0,0,1,0,0,3,0,26,0]   #youtube vertical video 26 3 1
    ti="Hong Kong"
    language=[]
    co=[]
    data=[]
    for i in range(10):  
        if da[i]>0:     
            language.append(la[i])
            co.append(colors[i])
            data.append(da[i])
    plt.subplot(2,2,2) # 分割圖 2行 2列 當前第2個位置
    plt.pie(data, labels=language,colors =co, autopct='%1.2f%%') # 圓餅圖
    plt.title(ti)      

#  第三圓餅圖    
    da=[11,0,0,5,0,4,6,3,0,1]   #11 c6 m4 t3 k5 h1
    ti="Singapore"
    language=[]
    co=[]
    data=[]
    for i in range(10):  
        if da[i]>0:     
            language.append(la[i])
            co.append(colors[i])
            data.append(da[i])
    plt.subplot(2,2,3) # 分割圖 2行 2列 當前第2個位置
    plt.pie(data, labels=language,colors =co, autopct='%1.2f%%') # 圓餅圖
    plt.title(ti) 


    da=[0,0,0,1,0,0,0,0,0,0,29]   #11 c6 m4 t3 k5 h1
    ti="Vietnam"
    language=[]
    co=[]
    data=[]
    for i in range(11):  
        if da[i]>0:     
            language.append(la[i])
            co.append(colors[i])
            data.append(da[i])
    plt.subplot(2,2,4) # 分割圖 2行 2列 當前第2個位置
    plt.pie(data, labels=language,colors =co, autopct='%1.2f%%') # 圓餅圖
    plt.title(ti) 

    
    plt.savefig('yt02.png',transparent=True)
    #plt.show()    
    
    
Normal_distribution()

    
def plt():  
        
    xx=[8,16,32,1024,8192,65536,4194304,134217728,536870912,1073741824 ]
    yy=[0.000001706,0.000001032,0.000001068,0.000002530,0.000012470
        ,0.000006879,0.000677733,0.025973167,0.101467126,0.233626252]
    
    
    x2=[8, 16384,16777216,67108864,134217728,268435456,536870912,1073741824 ]
    y2=[0.000000457,0.000003465,0.006285481,0.026389170,0.039899451,0.107264209,0.195144642,0.336236576]
  
    
    x=[256,1000,10000,100000]
    y=[39.76,108.98,294.37,371.1]
    y2=[56.75,153.84,397.63,452.93]
    y3=[70.95,192.51,486.58,553.54]
    
    x=[1000,10000,100000]
    y=[29.36,48.42,65.79]
    y2=[46.73,69.32,111.76]
    y3=[66.89,138.72,285.95]
    
    
    plt.plot(x,y,marker = "o") 
    plt.plot(x,y2,marker = "o") 
    plt.plot(x,y3,marker = "o")  
    
    plt.xlabel("maxIteration")
    plt.ylabel("speedup")
            
    plt.savefig('plt.png')
          
    plt.show()
    
    print("kkk")
    
    byte=1073741824
    
    time=0.233626252
    
    b=byte/1024/1024/time
    print("b=",b)
    
    bb=1073741824
    bb=bb/1024/1024/1024
    print(bb)



def scatter0():
    plt.xlim(630, 650)
    plt.ylim(505, 525)
    xx=[1,2,3]
    yy=[2,3,4]
    plt.scatter(xx, yy, c='red')
             
    plt.savefig('plt.png')
      
    plt.show()
    

