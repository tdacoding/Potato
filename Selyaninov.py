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

begin_date = pd.to_datetime('10.07.2016', format='%d.%m.%Y')
end_date = pd.to_datetime('26.07.2016', format='%d.%m.%Y')
db_select = db[['Intraday_mean', 'Precipitation']].loc[(db.index >= begin_date) & (db.index <= end_date) & (db['Intraday_mean'] >= 10)]

temp_sum = db_select['Intraday_mean'].sum()
print('Сумма среднесуточных температур выше 10 градусов за период:', temp_sum)
precip_sum = db_select['Precipitation'].sum()
print('Сумма осадков при температуре выше 10 градусов за период:', precip_sum)
K_sel = precip_sum*10/temp_sum
print('Коэффицент Селянинова за период:', K_sel)

db_select = db[['Intraday_mean', 'Soil_mean', '20cm']].loc[(db.index >= begin_date) & (db.index <= end_date)]
print('Средняя температура за период:', db_select['Intraday_mean'].mean())
print('Средняя температура поверхности почвы за период:', db_select['Soil_mean'].mean())
print('Средняя температура почвы на глубине 20см за период:', db_select['20cm'].mean())

# db_select = db[['Intraday_mean', 'Soil_mean', '20cm','Precipitation']].loc[((db.index.month > begin_date.month) & (db.index.month < end_date.month)) | (db.index.month == begin_date.month) & (db.index.day >= begin_date.day) | (db.index.month == end_date.month) & (db.index.day <= end_date.day)]

# db_select_KS = db_select[['Intraday_mean', 'Precipitation']].loc[db['Intraday_mean'] >= 10]
# temp_sum_hist = db_select_KS['Intraday_mean'].sum()
# print('Сумма среднесуточных температур выше 10 градусов за период за историю:', temp_sum_hist)
# precip_sum_hist = db_select_KS['Precipitation'].sum()
# print('Сумма осадков при температуре выше 10 градусов за период за историю:', precip_sum_hist)
# K_sel = precip_sum_hist*10/temp_sum_hist
# print('Коэффицент Селянинова за период:', K_sel)

# var1 = db_select['Intraday_mean']
# var2 = db_select['Precipitation']
# print(var1.mean())
# var1.hist(bins='auto', density=1, alpha=0.6, color='g',edgecolor="b")
# print(var2.mean())
# var2.hist(bins='auto', density=1, alpha=0.6, color='g',edgecolor="b")
# plt.show()
