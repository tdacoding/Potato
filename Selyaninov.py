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
b_date = '24.06.2015'
e_date = '27.06.2015'
begin_date = pd.to_datetime(b_date, format='%d.%m.%Y')
end_date = pd.to_datetime(e_date, format='%d.%m.%Y')
db_select = db[['Intraday_mean', 'Precipitation']].loc[(db.index >= begin_date) & (db.index <= end_date) & (db['Intraday_mean'] >= 10)]
#
temp_sum = db_select['Intraday_mean'].sum()
print('Сумма среднесуточных температур выше 10 градусов за период:', temp_sum)
precip_sum = db_select['Precipitation'].sum()
print('Сумма осадков при температуре выше 10 градусов за период:', precip_sum)
K_sel = precip_sum*10/temp_sum
print('Коэффицент Селянинова за период:', K_sel)
#
# db_select = db[['Intraday_mean', 'Soil_mean', '20cm']].loc[(db.index >= begin_date) & (db.index <= end_date)]
# print('Средняя температура за период:', db_select['Intraday_mean'].mean())
# print('Средняя температура поверхности почвы за период:', db_select['Soil_mean'].mean())
# print('Средняя температура почвы на глубине 20см за период:', db_select['20cm'].mean())

db_select = db[['Intraday_mean', 'Soil_mean', '20cm','Precipitation']].loc[((db.index.month > begin_date.month) & (db.index.month < end_date.month)) | ((begin_date.month < end_date.month) & (((db.index.month == begin_date.month) & (db.index.day >= begin_date.day)) | ((db.index.month == end_date.month) & (db.index.day <= end_date.day)))) | ((begin_date.month == end_date.month) & (db.index.month == end_date.month) & (db.index.day >= begin_date.day) & (db.index.day <= end_date.day))]
db2 = db_select.loc[db_select['Intraday_mean'] >= 10]

db1 = db2.groupby(db2.index.year).agg(['sum'])


db3 = db1[['Intraday_mean','Precipitation']]
ad = db3['Precipitation']*10/db3['Intraday_mean']

db3['sel'] = ad['sum']
# db3['sel'] = db3.apply(lambda row: row.Precipitation*10/row.Intraday_mean, axis=1)


# db_select_KS = db_select[['Intraday_mean', 'Precipitation']].loc[db['Intraday_mean'] >= 10]
# temp_sum_hist = db_select_KS['Intraday_mean'].sum()
# print('Сумма среднесуточных температур выше 10 градусов за период за историю:', temp_sum_hist)
# precip_sum_hist = db_select_KS['Precipitation'].sum()
# print('Сумма осадков при температуре выше 10 градусов за период за историю:', precip_sum_hist)
# K_sel = precip_sum_hist*10/temp_sum_hist
# print('Коэффицент Селянинова за период:', K_sel)

var1 = db3['sel']
# var2 = db_select['Precipitation']
print('ГКС 2016',var1[2015])
print('Среднее',var1.mean())
print('Квантиль 0,25',var1.quantile(.25))
print('Квантиль 0,75',var1.quantile(.75))
print('Медиана',var1.median())
var1.hist(bins='auto', density=1, alpha=0.6, color='g',edgecolor="b")

title = "Гистограмма распределения гидротермического коэффициента Селянинова с 1967 по 2017 гг.\n" + r"период %s - %s (фаза 1 сортообразца 1523-15)" % (begin_date.strftime("%d.%m"), end_date.strftime("%d.%m"))
plt.text(0.11,35,r'$\mathrm{S}^2_U=\overline{U^2}-{\overline{U}}^2$', fontsize=20)
plt.axvline(x=var1.quantile(.25),color='r')
plt.axvline(x=var1.quantile(.75),color='r')
plt.axvline(x=var1[2015],color='darkblue')
plt.xticks([var1.quantile(.25),var1[2015],var1.quantile(.75),round(var1.max())],['\n' + '{:.2f}'.format(var1.quantile(.25)) + '\n 25%','{:.2f}'.format(var1[2015]), '\n' + '{:.2f}'.format(var1.quantile(.75)) + '\n 75%',round(var1.max())])


plt.title(title)
plt.show()
