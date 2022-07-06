# -*- coding: utf-8 -*-
"""
Created on 5/18, 2022

@author: a4691

分段長條圖

預設資料 wiki各國語言



"""


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

import pandas as pd
from wand.image import Image
import imageio




fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], 'ro',animated=True)

def init():
    ax.set_xlim(-np.pi,np.pi)
    ax.set_ylim(-1, 1)
    return ln,

def update(frame):
    xdata.append(frame)
    ydata.append(np.sin(frame))
    ln.set_data(xdata, ydata)
    return ln,

anim = animation.FuncAnimation(fig, update, frames=np.linspace(-np.pi,np.pi, 90),interval=10,
                    init_func=init,blit=True)

anim.save('test_animation.gif',writer='imagemagick')
plt.show()


print("start")

ny = Image(filename ='output.gif')
ny_convert = ny.convert('mp4')
ny_convert.save(filename ='out.mp4')

print("end")



