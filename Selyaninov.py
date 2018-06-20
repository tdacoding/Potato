import csv
import numpy as np
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt


db = pd.read_csv('Sykt_t_and_soil.csv', encoding='cp1251')
db = db.set_index(pd.DatetimeIndex(db['date']))
print(db.head(0))

# var = db['Soil_mean'].loc[(db.index.month == 6) | (db.index.month == 7) | (db.index.month == 8)]
# print('mean:', var.mean())
# print('max:', var.max())
# print('min:', var.min())

#var.hist(bins='auto', density=1, alpha=0.6, color='g',edgecolor="b")

# var.plot()
# plt.show()
begin_date = '2016-7-10'
end_date = '2016-8-26'
db_select = db[['Intraday_mean', 'Precipitation']].loc[(db.index >= begin_date) & (db.index <= end_date) & (db['Intraday_mean'] >= 10)]

temp_sum = db_select['Intraday_mean'].sum()
print('Сумма среднесуточных температур выше 10 градусов за период:', temp_sum)
precip_sum = db_select['Precipitation'].sum()
print('Сумма осадков при температуре выше 10 градусов за период:', precip_sum)
K_sel = precip_sum*10/temp_sum
print('Коэффицент Селянинова за период:', K_sel)

db_select = db[['Intraday_mean', 'Soil_mean', '20cm']].loc[(db.index >= begin_date) & (db.index <= end_date)]
print(db_select)

