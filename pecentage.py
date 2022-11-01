from matplotlib.colors import Normalize
from numpy.core.numeric import True_
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pymannkendall as mk


data = r"C:\Users\ReSEC2021\Downloads\lake_trends\Thomas Lake.csv"

df = pd.read_csv(data)\

print(df)

criteria = [df['Pixel_Percent'].between(0, 10), df['Pixel_Percent'].between(10, 20), df['Pixel_Percent'].between(20, 30),df['Pixel_Percent'].between(30, 40),df['Pixel_Percent'].between(40, 50),
 df['Pixel_Percent'].between(50, 60),  df['Pixel_Percent'].between(60, 70),  df['Pixel_Percent'].between(70, 80), df['Pixel_Percent'].between(80, 90), df['Pixel_Percent'].between(90, 100)
 ]
values = ["0-10", "10-20", '20-30', '30-40', '40-50','50-60','60-70', '70-80', '80-90', '90-100']

df['b'] = np.select(criteria, values, 0)
print(df)

df['count'] = df['b'].map(df['b'].value_counts())
df['percentage'] = (df['count'] / df['count'].sum()) * 100


print(df)

df = df.loc[df['b'] != '0-10']

#df.apply(lambda d: pd.value_counts(d, normalize=True)).plot(kind = 'barh')

df.b.value_counts().sort_values().plot(kind = 'barh')
plt.title('Percentage of Recovered Pixels- Thomas Lake (1984-2021)')
plt.xlabel("Number of Lakes Specific Temperature Extracted")
plt.ylabel("Range of Pecentage of Pixel")
plt.show()
