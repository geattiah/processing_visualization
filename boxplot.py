# ----------------------------------------------------------------------------
# -*- coding: utf-8 -*-
# @Author:              Gifty Attiah
# @Date:                2021-05-11
# @Email:               geattiah@gmail.com
# @Last Modified By:    Gifty Attiah
# @Last Modified Time:  Not Tracked
# 
# PROGRAM DESCRIPTION:
# Boxplot of lake temperature
# ----------------------------------------------------------------------------

import csv
from PIL import Image
from matplotlib import colors
import pandas as pd
import numpy 
import os
import matplotlib.pyplot as plt
from matplotlib import rc,rcParams
import matplotlib.lines as mlines

csv_file = pd.read_csv(r"C:\Users\ReSEC2021\OneDrive - Wilfrid Laurier University\Arc_Analysis\box_plot\All_Tem.csv")
print(csv_file)
folder = r"C:\Users\ReSEC2021\OneDrive - Wilfrid Laurier University\Arc_Analysis\box_plot"
boxprops = dict(linestyle='-', linewidth=2, color='k')
medianprops = dict(linestyle='-', linewidth=2, color='b')
whiskerprops=dict(linestyle='-', linewidth=2)
color=dict(boxes='k', whiskers='k', medians='k', caps='k')
capprops=dict(linestyle='-', linewidth=2)
flierprops=dict(linestyle='-', linewidth=2)

boxplot = csv_file.boxplot(column=['Long','Frame', 'Stewart','Grace'],boxprops=boxprops,medianprops=medianprops,capprops=capprops,flierprops=flierprops,whiskerprops=whiskerprops, fontsize = 14,color=color,showfliers=False)



#box = plt.boxplot(d)

# for _, line_list in box.items():
#     for line in line_list:
#         line.set_color('black')

plt.plot(1, -15.8,'*', c= "r", markersize=12)
plt.plot(2, -15.8,'*', c= "r",markersize=12)
plt.plot(3, -15.8,'*', c= "r",markersize=12)
plt.plot(4, -15.8,'*', c= "r",markersize=15)
plt.plot(edgecolor='b',linewidth=3)
#plt.gca().invert_yaxis()
#plt.legend(['single element'])
#plt.title("Distribution of Temperature on Lakes")
#plt.legend(["Station Data"], loc ="upper right")
plt.xticks(fontsize = 14,weight='bold')
blue_star = mlines.Line2D([], [], color='red', marker='*', linestyle='None',
                        markersize=10, label='Station Temperature')
#plt.legend(handles=[blue_star])
#plt.ylabel("Temperature (°C)",fontsize = 14)
#plt.xlabel("Lake Name")
rc('text', usetex=True)
rc('axes', linewidth=2)
rc('font', weight='bold')

win = plt.gcf().canvas.manager.window

win.lift()
win.attributes("-topmost", True)
win.attributes("-transparentcolor", "white")


plt.grid(False)
plt.savefig(os.path.join(folder,'demo.png'),transparent=True)
plt.show()
