import matplotlib.pyplot as plt
import pandas as pd
url = 'https://raw.githubusercontent.com/ehmatthes/pcc_2e/raw/master/chapter_16/the_csv_file_format/data/sitka_weather_07-2018_simple.csv'
df_sitka = pd.read_csv(url)
df_sitka['PRCP'].plot(kind="hist",bins=50,figsize=(6,4)) #histogram
df_sitka.plot(x='DATE', y='PRCP', kind='scatter', \
figsize=(6,5), \
title='RainFall in 2018') #scatter
df_sitka.boxplot(column='PRCP', by='TMAX', figsize=(10,6)) #boxplot
df_sitka[['DATE','PRCP']].groupby('DATE').mean().sort_values(by='PRCP', ascending=False).plot.bar(figsize=(10,6), rot=10, title='Average Rain fall in stations wrt DATE') #bargraph
df_sitka[['TMAX','PRCP']].groupby('TMAX').mean().sort_values(by='PRCP', ascending=False). \
plot.bar(figsize=(10,6), rot=10, title='Average Rain fall in stations wrt DATE')