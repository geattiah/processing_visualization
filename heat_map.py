import pandas as pd
from datetime import datetime
import calplot
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

#import calender


data = pd.read_csv(r"C:\Users\ReSEC2021\Downloads\FiddlerTempRno6mV6.txt", sep="\t",header = 0)
#print(data)

data["Month"] = data['dateTime'][5:7]
#print(data)

## ##array = data.to_numpy()
# print(array)

data['dateTime'] = pd.to_datetime(data['dateTime'], format='%Y-%m-%d %H:%M:%S.%f')
#data['dateTime']

data["year"]= pd.DatetimeIndex(data['dateTime']).year
#print(data)

data["month"]= pd.DatetimeIndex(data["dateTime"]).month
#print(data)

data["day"]= pd.DatetimeIndex(data["dateTime"]).day
#print(data)

data["hour"]= pd.DatetimeIndex(data["dateTime"]).hour
#print(data)

data["minutes"]= pd.DatetimeIndex(data["dateTime"]).minute
#print(data)

data["seconds"]= pd.DatetimeIndex(data["dateTime"]).second
#print(data)

month = []
for i in data['month']:
    month.append(i)
# print(month)

depth_1 = []
for i in data['wtr_0.0']:
    depth_1.append(i)
# print(depth_1)

depth_2 = []
for i in data['wtr_1.0']:
    depth_2.append(i)
# print(depth_2)

depth_3 = []
for i in data['wtr_2.0']:
    depth_3.append(i)
# print(depth_3)

depth_4 = []
for i in data['wtr_3.0']:
    depth_4.append(i)
# print(depth_4)

depth_5 = []
for i in data['wtr_4.0']:
    depth_5.append(i)
# print(depth_5)

depth_6 = []
for i in data['wtr_5.0']:
    depth_6.append(i)
##print(depth_6)


#mn_array= np.column_stack(month,depth_1)

a = list(zip(depth_1,depth_2,depth_3,depth_4,depth_5,depth_6))
#print(a)

##print(data)
#b = a.pivot(a,month)

sns.heatmap(a)
#g.invert_yaxis()

#plt.show()


#data.to_csv("output.csv")

#sns.set()
#temp = data.pivot("dateTime",'wtr_1.0')
#ax = sns.heatmap(temp)
#plt.show()

#idx = str(month)
#print(idx)

df = pd.DataFrame([depth_1,depth_2,depth_3,depth_4,depth_5,depth_6], columns= month, index = [1,2,3,4,5,6])

#df = pd.DataFrame(df, columns = str(month))

#corr = df.corr()
sns.heatmap(df, annot = True)

#temp = temp.pivots()

#data = data.set_index('dateTime')
#calplot.calplot(data["wtr_0.0"])
plt.show()