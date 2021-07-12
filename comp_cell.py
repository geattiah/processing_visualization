import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import os
import csv

file_name = (r"C:\Users\ReSEC2021\Downloads\gpr.csv")

outputfolder = (r"C:\Users\ReSEC2021\Downloads\plots")

filename = pd.read_csv(r"C:\Users\ReSEC2021\Downloads\gpr_lat_lon.csv")
#filename['Rolling'] = filename['GPR_Th'].rolling(window=100).mean()
#print(filename)

data = filename.loc[(filename["GPR_Th"] >= 80)]
data = data.loc[(data["GPR_Th"] <= 140)]

with open(os.path.join(outputfolder,'gpr_m')+".csv", 'w', newline = '') as table:
    writer = csv.writer(table)
    writer.writerow(['Lat','Long','Lat_Long','GPR','0p','25p','50p','75p','100p'])

    unique = data["Lon"].unique()
    #print(unique)

    for i in unique:
        a = data[data['Lon']==i]
        print(a)
        gpr = (a['GPR_Th'].mean()).round(2)
        #print(gpr)
        p0 = (a['0p'].mean()).round(2)
        #print(p0)
        p25 = (a['25p'].mean()).round(2)
        #print(p25)
        p50 = (a['50p'].mean()).round(2)
        #print(p50)
        p75 = (a['75p'].mean()).round(2)
        #print(p75)
        p100 = (a['100p'].mean()).round(2)
        #print(p100)
        lat = (a['Lat'].mean()).round(2)
        #print(lat)
        lon = (a['Lon'].mean()).round(2)
        #print(lon)
        lat_lon = "("+(str(lat)+","+str(lon))+")"
        #print(lat_lon)

        writer.writerow([lat, lon, lat_lon, gpr, p0, p25, p50, p75, p100])

        
    