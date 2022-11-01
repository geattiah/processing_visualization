import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pymannkendall as mk
from scipy import stats

data = r"C:\Users\ReSEC2021\OneDrive - Wilfrid Laurier University\Projects\Lake_Temperature\Data\CSV\indi_lake_temps\Ryan_Lake.csv"

df = pd.read_csv(data)

#df['Year'] = df['Year'].astype(str).str.zfill(2)
#df['Month'] = df['Month'].astype(str).str.zfill(2)
#df['Day'] = df['Day'].astype(str).str.zfill(2)

df['Dates'] = df['Year'].astype(str)+'-'+df['Month'].astype(str)+'-'+df['Day'].astype(str)
df['Dates']= pd.to_datetime(df['Dates'])




#df.plot(subplots=True, figsize=(10,12))

#df['Mean_Temperature'].plot()
#plt.show()

#print(df.head())

#df_month = df.resample("M").mean()
#print(df_month.head())

#df_month['Mean_Temperature'].plot(figsize=(8, 6))
#plt.show()
df['month'] = pd.DatetimeIndex(df['Dates']).month

df['year'] = pd.DatetimeIndex(df['Dates']).year

years = df['year'].unique()

df.set_index('Dates', inplace= True)

df = df[~df.index.duplicated()]
print(df)

# fig, axes = plt.subplots(1, 2, figsize=(20,7), dpi= 80)
# myplot =sns.boxplot(x='year', y='Mean_Temperature', data=df, ax=axes[0])
# myplot2 = sns.boxplot(x='month', y='Mean_Temperature', data=df.loc[~df.year.isin([1984, 2020]), :])
# def is_outlier(s):
#     lower_limit = s.mean() - (s.std() * 3)
#     upper_limit = s.mean() + (s.std() * 3)
#     return ~s.between(lower_limit, upper_limit)

# df = df[~df.groupby('month')['Mean_Temperature'].apply(is_outlier)]

# print(df)

# fig, axes = plt.subplots(1, 2, figsize=(20,7), dpi= 80)
# myplot =sns.boxplot(x='year', y='Mean_Temperature', data=df, ax=axes[0])
# myplot2 = sns.boxplot(x='month', y='Mean_Temperature', data=df.loc[~df.year.isin([1984, 2020]), :])

#df[df.groupby("Month").Mean_Temperature.\
      #transform(lambda x : (x<x.quantile(0.95))&(x>(x.quantile(0.05)))).eq(1)]

Q1 =  df['Mean_Temperature'].quantile(0.25)
Q3 = df['Mean_Temperature'].quantile(0.75)
IQR = Q3 - Q1

#df[(df.groupby(['month'])['Mean_Temperature'] < Q1-1.5*IQR ) | (df.groupby(['month'])['Mean_Temperature'] > Q3+1.5*IQR)]['Mean_Temperature']

def is_outlier(s):
    lower_limi = s.quantile(0.25)
    upper_limi = s.quantile(0.75)

    iqr = upper_limi - lower_limi

    lower_limit = lower_limi - (1.5 * iqr)
    upper_limit = upper_limi + (1.5 * iqr)

    return ~s.between(lower_limit, upper_limit)

df = df[~df.groupby('month')['Mean_Temperature'].apply(is_outlier)]
#df = df[df.groupby(['month'])['Mean_Temperature'].transform(stats.zscore).abs() < 3]
print(df)


fig, axes = plt.subplots(1, 2, figsize=(20,7), dpi= 80)
myplot =sns.boxplot(x='year', y='Mean_Temperature', data=df, ax=axes[0])
myplot2 = sns.boxplot(x='month', y='Mean_Temperature', data=df.loc[~df.year.isin([1984, 2020]), :])

#print(res)
# Set Title

# df1 = df['Mean_Temperature']
# print(df1.head())

# resample = df1.resample('M')
# monthly_mean = resample.mean()
# print(monthly_mean.head(13))
# monthly_mean.plot()
plt.show()
#axes.set_xticklabels(rotation=45, ha='right')

#print(df)
#plt.show()
# import calendar
# all_month_year_df = pd.pivot_table(df, values="Mean_Temperature",
#                                    index=["month"],
#                                    columns=["year"],
#                                    fill_value=0,
#                                    margins=True)
# named_index = [[calendar.month_abbr[i] if isinstance(i, int) else i for i in list(all_month_year_df.index)]] # name months
# all_month_year_df = all_month_year_df.set_index(named_index)
# print(all_month_year_df)

# ax = sns.heatmap(all_month_year_df, cmap='RdYlGn_r', robust=True, fmt='.2f', 
#                  annot=True, linewidths=.5, annot_kws={'size':5}, 
#                  cbar_kws={'shrink':.8, 'label':'Open'})                       
    
# ax.set_yticklabels(ax.get_yticklabels(), rotation=0, fontsize=10)
# ax.set_xticklabels(ax.get_xticklabels(), rotation=0, fontsize=10)
# plt.title('Average Opening', fontdict={'fontsize':18},    pad=14);
# from pylab import rcParams
# import statsmodels.api as sm

# rcParams['figure.figsize'] = 11, 9
# decomposition = sm.tsa.seasonal_decompose(df_month['Mean_Temperature'], model='Additive')
# fig = decomposition.plot()
# plt.show()
#print(mk.original_test(df['Mean_Temperature']))


#plt.show()