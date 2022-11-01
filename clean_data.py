import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pymannkendall as mk
from scipy import stats
from statsmodels.tsa.seasonal import seasonal_decompose

data = r"C:\Users\ReSEC2021\OneDrive - Wilfrid Laurier University\Projects\Lake_Temperature\Data\CSV\indi_lake_temps\Landing_Lake.csv"

df = pd.read_csv(data)

df['Dates'] = df['Year'].astype(str)+'-'+df['Month'].astype(str)+'-'+df['Day'].astype(str)
df['Dates']= pd.to_datetime(df['Dates'])
df['month'] = pd.DatetimeIndex(df['Dates']).month
df['year'] = pd.DatetimeIndex(df['Dates']).year

years = df['year'].unique()
df.set_index('Dates', inplace= True)

df = df[~df.index.duplicated()]

# Remove outliers
def is_outlier(s):
    lower_limi = s.quantile(0.25)
    upper_limi = s.quantile(0.75)

    iqr = upper_limi - lower_limi

    lower_limit = lower_limi - (1.5 * iqr)
    upper_limit = upper_limi + (1.5 * iqr)

    return ~s.between(lower_limit, upper_limit)


df = df[~df.groupby('month')['Mean_Temperature'].apply(is_outlier)]
print(df)

#decompose = seasonal_decompose(df['Mean_Temperature'],model='additive', period=50)
#decompose.plot()
df = df[df['Max_Pixel_Temperature']>-25]
df = df.resample("M").mean()
#df = df.resample("Y").mean()
df = df[df['month'] == 8]

df = df.dropna()
print(df)

#df = df[pd.to_datetime(df['Date']).dt.month == 5]


decompose = seasonal_decompose(df['Mean_Temperature'],model='additive', period=7)
decompose.plot()

fig, axes = plt.subplots(1, 2, figsize=(20,7), dpi= 80)
myplot =sns.boxplot(x='year', y='Mean_Temperature', data=df, ax=axes[0])
myplot2 = sns.boxplot(x='month', y='Mean_Temperature', data=df.loc[~df.year.isin([1984, 2020]), :])

plt.show()

