# ----------------------------------------------------------------------------
# -*- coding: utf-8 -*-
# @Author:              Gifty Attiah
# @Date:                2021-03-29
# @Email:               geattiah@gmail.com
# @Last Modified By:    Gifty Attiah
# @Last Modified Time:  Not Tracked
# 
# PROGRAM DESCRIPTION:
# Plot of data from csv
# ----------------------------------------------------------------------------

import sys
import os
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np

data = pd.read_csv("C:/Users/ReSEC2021/Downloads/phenolo.csv",sep = ",", engine = 'python', header = 0)
print(data)

year = data['Year']
max_fu = data['Max_freezeup']
min_fu = data['Min_freezeup']

maxfup = list(zip(year,max_fu))
minfup = list(zip(year,min_fu))


x = [x[0] for x in maxfup]
y = [y[1] for y in maxfup]
y1 = [y[2] for y1 in maxfup]

#x,y = zip(*maxfup)
#x1,y1 = zip(*minfup)


fig = plt.figure() 
#set both axes since we are plotting two graphs on one
ax1 = fig.add_subplot(111, label = "1")
ax2 =fig.add_subplot(111, label="2", frame_on=False)


ax1.plot(x,y)
#ax2.plot(x,y1)
#plt.plot(x_a,y_a,y1_a)
plt.show()