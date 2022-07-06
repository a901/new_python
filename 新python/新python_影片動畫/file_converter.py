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



print("start")

ny = Image(filename ='output_fast.gif')
ny_convert = ny.convert('mp4')
ny_convert.save(filename ='out_fast.mp4')

print("end")



