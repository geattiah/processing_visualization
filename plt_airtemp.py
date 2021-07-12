import sys
import os
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np

#data = pd.read_csv("C:/Users/ReSEC2021/Downloads/phenolo.csv",sep = ",", engine = 'python', header = 0)
jan = pd.read_csv(r"C:\Users\ReSEC2021\OneDrive - Wilfrid Laurier University\Arc_Analysis\text_temp\_01.csv")
print(jan)

x = jan['Grid']
x1 = jan['Temp']
y = range(1,2479)

plt.scatter(x,x1, s=5, c='g') 
#plt.plot(x1)
plt.show()
