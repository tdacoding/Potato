import csv
import numpy as np
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt

db = pd.read_csv('Sykt_t_data_day_mean_2020WithRp5.csv', encoding='cp1251')
db = db.set_index(pd.DatetimeIndex(db['date']))
print(db.head(0))

b_date = '01.01.1987'
e_date = '31.12.1987'

temp1 = 5
temp2 = 15

begin_date = pd.to_datetime(b_date, format='%d.%m.%Y')
end_date = pd.to_datetime(e_date, format='%d.%m.%Y')
inter_year = begin_date.strftime("%Y")

db_select = db[['Intraday_mean', 'Precipitation']].loc[(db.index >= begin_date) & (db.index <= end_date)]

db1_select = db_select.loc[db_select['Intraday_mean'] >= temp1]
# print(db1_select)
# print(db1_select.loc[db1_select.index == db1_select.index.min()])
# print(db1_select.index.min())
spring_begin = db1_select.index.min()
# print(db1_select.loc[db1_select.index == db1_select.index.max()])
autumn_end = db1_select.index.max()
# print(db1_select.index.max())
db1_select = db_select.loc[db_select['Intraday_mean'] >= temp2]
spring_end = db1_select.index.min()
autumn_begin = db1_select.index.max()
print('Весна', spring_begin, '-', spring_end)
print('Осень', autumn_begin, '-', autumn_end)
#
# db_select = db[['Intraday_mean', 'Precipitation']].loc[
#     ((db.index.month > begin_date.month) & (db.index.month < end_date.month)) | (
#                 (begin_date.month < end_date.month) & (
#                     ((db.index.month == begin_date.month) & (db.index.day >= begin_date.day)) | (
#                         (db.index.month == end_date.month) & (db.index.day <= end_date.day)))) | (
#                 (begin_date.month == end_date.month) & (db.index.month == end_date.month) & (
#                     db.index.day >= begin_date.day) & (db.index.day <= end_date.day))]
# db['date1'] = db.index
db2 = db[['Intraday_mean', 'Precipitation', 'date']].loc[db['Intraday_mean'] >= temp1]
db1 = db2.groupby(db2.index.year).agg(['min'])['date']['min']
db1['spr_b'] = db2.groupby(db2.index.year).agg(['min'])['date']['min']
db1['aut_e'] = db2.groupby(db2.index.year).agg(['max'])['date']['max']

db2 = db[['Intraday_mean', 'Precipitation', 'date']].loc[db['Intraday_mean'] >= temp2]

db1['spr_e'] = db2.groupby(db2.index.year).agg(['min'])['date']['min']
db1['aut_b'] = db2.groupby(db2.index.year).agg(['max'])['date']['max']
db3 = db1[['spr_b', 'spr_e', 'aut_b', 'aut_e']]
db3['spr_long'] = (pd.to_datetime(db3['spr_e'])-pd.to_datetime(db3['spr_b'])).dt.days
db3['aut_long'] = (pd.to_datetime(db3['aut_e'])-pd.to_datetime(db3['aut_b'])).dt.days
db3['ratio'] = db3['spr_long']/db3['aut_long']
# print(db3['ratio'])
db3['ratio1'] = db3['ratio'].apply(lambda x: x-1 if x >= 1 else -(1/x-1))
# print(db3['ratio1'])
plt.bar(db3['ratio1'].index, db3['ratio1'])
locs, labels = plt.yticks()
title = "Отношение продолжительности вегетационной весны к вегетационной осени"
# plt.axhline(linewidth=1.5, y=db3['spr_long'].quantile(.25), color='b')
# plt.axhline(linewidth=1.5, y=db3['spr_long'].mean(), color='b')
# plt.axhline(linewidth=1.5, y=db3['spr_long'].quantile(.75), color='b')

locs1 = np.append(locs, np.array([db3['ratio'].quantile(.25), db3['ratio'].mean(), db3['ratio'].quantile(.75)]))
labels = np.append(locs.round(0), np.array([r'$q_1$=' + '{:.2f}'.format(db3['ratio'].quantile(.25)), r'$\overline{x}$=' + '{:.2f}'.format(db3['ratio'].mean()), r'$q_3$=' + '{:.2f}'.format(db3['ratio'].quantile(.75))]))

# plt.yticks(locs1, labels, fontsize=10)
plt.title(title, fontsize=12)
plt.show()

