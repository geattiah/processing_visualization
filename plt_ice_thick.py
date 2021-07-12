
# ----------------------------------------------------------------------------
# -*- coding: utf-8 -*-
# @Author:              Gifty Attiah
# @Date:                2021-05-22
# @Email:               geattiah@gmail.com
# @Last Modified By:    Gifty Attiah
# @Last Modified Time:  Not Tracked
# 
# PROGRAM DESCRIPTION:
# Comparison plots with RMSE and MBE estimations of thickness
# ----------------------------------------------------------------------------
from matplotlib import colors
import pandas as pd
import numpy as np
import os
import csv
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from math import sqrt


#filename = r"C:\Users\ReSEC2021\OneDrive - Wilfrid Laurier University\slideanalysis\gpr_out.csv"
filename = r"C:\Users\ReSEC2021\OneDrive - Wilfrid Laurier University\slideanalysis\gsl_comp - Copy.csv"

outputfolder = r"C:\Users\ReSEC2021\OneDrive - Wilfrid Laurier University\slideanalysis"

df = pd.read_csv(filename,sep=',')
print(df)

fig, axes = plt.subplots(nrows=1,ncols=1,sharex=True,sharey=True)   
fontP = FontProperties()
fontP.set_size('small')
y = df['Measured']
x = range(23148)
y1 = df['Simulated']
x2 = df['DATE']
#x2= df['Dat'] = df.DATE.str[:5]

print(x)
p2 = plt.plot(x2, y1, 'k')
p0 = plt.scatter(x2, y, s= 50, label = 'Measured',color = 'blue')
#p1 = plt.scatter(x2, y1, s = 50, label = 'Simulated',color = 'blue')


#y = [11,20,19,17,10]
#y_bar = [12,18,19.5,18,9]
summation = 0  #variable to store the summation of differences
n = len(y) #finding total number of items in list
for i in range (0,n):  #looping through each element of the list
  difference = y[i] - y1[i]  #finding the difference between observed and predicted value
  squared_difference = difference**2  #taking square of the differene 
  summation = summation + squared_difference  #taking a sum of all the differences
MSE = summation/n  #dividing summation by total values to obtain average
rootMeanSquaredError = sqrt(MSE)
print ("The Mean Square Error is: " , MSE)
print ("The Root Mean Square Error is: " , rootMeanSquaredError)

def MBE(y_true, y_pred):
    '''
    Parameters:
        y_true (array): Array of observed values
        y_pred (array): Array of prediction values

    Returns:
        mbe (float): Biais score
    '''
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    #y_true = y_true.reshape(len(y_true),1)
    #y_pred = y_pred.reshape(len(y_pred),1)   
    diff = (y_pred-y_true)
    mbe = diff.mean()
    print('MBE = ', mbe)

MBE(y,y1)


plt.xlabel("Location - (lat,long)")
plt.title('Measured vs Simulated Ice Thickness')
plt.xticks(x2[::35],rotation = 45)
#plt.locator_params(axis='x', nbins=len(x2)/2) 
#plt.xticklabels(x[::20],rotation = 45)
#plt.xticks(np.arange(min(x), max(x)+1, 1.0))
#plt.gca().xaxis.set_major_locator(plt.MultipleLocator(1))

#plt.xticks(data.DATE[::2], rotation = 45)
#plt.locator_params(axis='x', nbins=len(x)/2)
plt.ylabel("Ice Thickness(cm)")
#plt.ylim(80,100)
#plt.legend(handles=[p0,p2], bbox_to_anchor=(1.05, 1), loc='upper left', prop=fontP)
#plt.legend(loc='upper left')
rmse = "RMSE : 2.55"
mbe = "MBE : 0.45"
#plt.text("2016-02-19", 91, rmse)
#plt.text("2016-02-19", 81, mbe)

plt.tight_layout()
figfile = os.path.join(outputfolder, 'roll_1000' + '_IC' + ".png")
plt.show()
plt.savefig(figfile)