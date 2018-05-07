
import csv
import numpy as np
import pandas as pd
import datetime as dt


db = pd.read_csv('Sykt_temp_data_cleaned.csv', encoding='cp1251')

#print(db.axes[1][1:])
print(db.head(0).columns)

db = db.set_index(pd.DatetimeIndex(db['time']))
print(db['Температура воздуха по сухому терм-ру'].mean())
print(db.loc['1966-01-02']['Температура воздуха по сухому терм-ру'])

print(db.loc['1966-01-02']['Температура воздуха по сухому терм-ру'].min())
print(db.loc['1966-01-02']['Температура воздуха по сухому терм-ру'].max())
print(db['Температура воздуха по сухому терм-ру'].loc['1966-01-02'].mean(axis=0))

db1 = pd.DataFrame(db.index.date).drop_duplicates()
db1.rename(columns={0: 'time'}, inplace=True)
db1 = db1.set_index(pd.DatetimeIndex(db1['time']))
#db1['Температура воздуха по сухому терм-ру'] = db['Температура воздуха по сухому терм-ру'].loc[db1.index].mean(axis=0)
#db1['new'] = db1.apply(lambda row: db['Температура воздуха по сухому терм-ру'].loc[row['time']].mean(axis=0), axis=1)
print(db1)




#db.to_csv('Sykt_temp_data_cleaned.csv', encoding='cp1251')

