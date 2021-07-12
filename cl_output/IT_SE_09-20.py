import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import os

folder = (r'C:\Users\Cristian\Desktop\Datasets\GSL Final SE\CSV\09-20')
outputfolder = 'C:\\Users\\Cristian\\Desktop\\Datasets\\GSL Final SE\\CSV\\09-20\\Graphs'

# data = pd.read_csv(r'C:\Users\Cristian\Desktop\Datasets\GSL Final NW\03-04.csv')

for filename in os.listdir(folder):
    fig, axes = plt.subplots(nrows=1,ncols=1,sharex=True,sharey=True)
    dat = os.path.join(folder,filename)
    data = pd.read_csv(dat)

# print(data.columns)

# print(data["DATE"])
##Get ice thickness as %

    data['SE_Ice_Thickness'] = data['SE_Ice_Thickness'].div(100)
    # print(data)
    
    
    ##plotTh0
    # fig0 = plt.figure(0)    
    
    fontP = FontProperties()
    fontP.set_size('small')
    p0, = plt.plot(data["DATE"],data["m_12_2_Th"], 'b', label="m_12")
    p1, = plt.plot(data["m_15_2_Th"], 'm' , label="m_15")
    p2, = plt.plot(data["m_17_2_Th"], 'y', label="m_17")
    p3, = plt.plot(data["m_20_2_Th"], 'g',label="m_20")
    p4, = plt.plot(data["SE_Ice_Thickness"],'r', label="inSitu")
    plt.xlabel("Date")
    plt.title('20' + (str(filename)[-10:-6]) + '20' + (str(filename)[-6:-4]))  
    plt.xticks(data.DATE[::2], rotation = 45)
    plt.ylabel("Ice Thickness (m)")
    # plt.legend(handles=[p0, p1, p2, p3, p4], title='Legend', bbox_to_anchor=(1.05, 1), loc='upper left', prop=fontP)
    plt.legend(loc='upper left')
    plt.tight_layout()
    figfile = os.path.join(outputfolder, (str(filename)[-10:-4]) + "_IT" + ".png")
    plt.savefig(figfile)
    
        