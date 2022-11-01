import os
import pandas as pd
import numpy as np


file_name = r"C:\\Users\\ReSEC2021\Downloads\\FiddlerTempRno6mV6.txt"
folder =  r"C:\\Users\\ReSEC2021\Downloads"

data = pd.read_csv(file_name,sep="\s+", engine= 'python')
print(data)

data["Date_rep"]= data['dateTime'].str.zfill(5)
data

data["DateTime"]= data.Time + " " + data.Date_rep + ':00'
data

dat = list(data.columns.values)
print(dat)

data = data.reindex(columns=[ 'DateTime','wtr_1.0', 'wtr_2.0', 'wtr_3.0', 'wtr_4.0', 'wtr_6.0', 'wtr_7.0'])
print(data)

data.to_csv(os.path.join(folder,"test_file_3.txt"), sep='\t', index=False)