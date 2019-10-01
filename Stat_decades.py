import csv
import numpy as np
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt


db = pd.read_csv('Sykt_t_and_soil.csv', encoding='cp1251')
db = db.set_index(pd.DatetimeIndex(db['date']))
print(db.head(0))

b_date = '01.06.2018'
e_date = '10.06.2018'
begin_date = pd.to_datetime(b_date, format='%d.%m.%Y')
end_date = pd.to_datetime(e_date, format='%d.%m.%Y')

db_select = db[['Intraday_mean', 'Soil_mean', '20cm','Precipitation']].loc[((db.index.month > begin_date.month) & (db.index.month < end_date.month)) | ((begin_date.month < end_date.month) & (((db.index.month == begin_date.month) & (db.index.day >= begin_date.day)) | ((db.index.month == end_date.month) & (db.index.day <= end_date.day)))) | ((begin_date.month == end_date.month) & (db.index.month == end_date.month) & (db.index.day >= begin_date.day) & (db.index.day <= end_date.day))]
db2 = db_select.loc[db_select['Intraday_mean'] >= 10]

db1 = db2[['Intraday_mean']].groupby(db2.index.year).agg(['mean'])
db3 = db2[['Precipitation']].groupby(db2.index.year).agg(['sum'])
db1['Precipitation'] = db3[['Precipitation']]
var = db1['Intraday_mean']
print('mean:', var.mean())
print('max:', var.max())
print('min:', var.min())
var.hist(bins='auto', density=1, alpha=0.6, color='r',edgecolor="b")
#var.plot()
plt.show()
var = db1['Precipitation']
print('mean:', var.mean())
print('max:', var.max())
print('min:', var.min())
