import csv
import numpy as np
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt


db = pd.read_csv('Sykt_t_and_soil_2018.csv', encoding='cp1251')
db = db.set_index(pd.DatetimeIndex(db['date']))
print(db.head(0))

# var = db['Soil_mean'].loc[(db.index.month == 6) | (db.index.month == 7) | (db.index.month == 8)]
# print('mean:', var.mean())
# print('max:', var.max())
# print('min:', var.min())

#var.hist(bins='auto', density=1, alpha=0.6, color='g',edgecolor="b")

# var.plot()
# plt.show()
b_date = '31.07.2018'
e_date = '30.08.2018'
temperature = 10
begin_date = pd.to_datetime(b_date, format='%d.%m.%Y')
end_date = pd.to_datetime(e_date, format='%d.%m.%Y')
db_select = db[['Intraday_mean', 'Precipitation']].loc[(db.index >= begin_date) & (db.index <= end_date) & (db['Intraday_mean'] >= temperature)]
#
temp_sum = db_select['Intraday_mean'].sum()
temp_mean = db_select['Intraday_mean'].mean()
print('Сумма среднесуточных температур выше', temperature, 'градусов за период:', temp_sum)
print('Седнее среднесуточных температур выше', temperature, 'градусов за период:', temp_mean)
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
db2 = db_select.loc[db_select['Intraday_mean'] >= temperature]

db1 = db2.groupby(db2.index.year).agg(['sum'])


db3 = db1[['Intraday_mean','Precipitation']]
ad = db3['Precipitation']*10/db3['Intraday_mean']

db3['sel'] = ad['sum']
#print(db3)
# db3['sel'] = db3.apply(lambda row: row.Precipitation*10/row.Intraday_mean, axis=1)


# db_select_KS = db_select[['Intraday_mean', 'Precipitation']].loc[db['Intraday_mean'] >= 10]
# temp_sum_hist = db_select_KS['Intraday_mean'].sum()
# print('Сумма среднесуточных температур выше 10 градусов за период за историю:', temp_sum_hist)
# precip_sum_hist = db_select_KS['Precipitation'].sum()
# print('Сумма осадков при температуре выше 10 градусов за период за историю:', precip_sum_hist)
# K_sel = precip_sum_hist*10/temp_sum_hist
# print('Коэффицент Селянинова за период:', K_sel)

## для расчета по декадам
# mean_temp_sum = db3['Intraday_mean']/11
# precipitation = db3['Precipitation']
# print('средняя температура в декаде', begin_date.strftime('%d.%m.%Y'), '-', end_date.strftime('%d.%m.%Y'), ':', round(mean_temp_sum['sum'][begin_date.year], 1))
# print('сумма осадков', begin_date.strftime('%d.%m.%Y'), '-', end_date.strftime('%d.%m.%Y'), ':', round(precipitation['sum'][begin_date.year], 1), '\n')
# print('средняя температура 1967-2018', round(mean_temp_sum['sum'].mean(), 1))
# print('средняя сумма осадков 1967-2018', round(precipitation['sum'].mean(), 1), '\n')

var1 = db3['sel']
#print(var1)
# var2 = db_select['Precipitation']
print('ГКС', begin_date.strftime('%d.%m.%Y'), '-', end_date.strftime('%d.%m.%Y'), ':', var1[begin_date.year])
print('Среднее', var1.mean())
print('Квантиль 0,25', var1.quantile(.25))
print('Квантиль 0,75', var1.quantile(.75))
print('Медиана', var1.median())


counts, bins, patches  = plt.hist(var1, bins='auto', density=0, alpha=0.6, color='gray', edgecolor="black")
title = "Гистограмма распределения гидротермического коэффициента Селянинова с 1967 по 2018 гг.\n" + r"период %s - %s (фаза формирования урожая сортообразца 1603-7 в %s г.)" % (begin_date.strftime("%d.%m"), end_date.strftime("%d.%m"), begin_date.year)
#plt.text(0.4, 0, r'$\mathrm{S}^2_U=\overline{U^2}-{\overline{U}}^2$', fontsize=20)
plt.axvline(linewidth=2.0, x=var1.quantile(.25), color='r')
plt.axvline(linewidth=2.0, x=var1.quantile(.75), color='r')
plt.axvline(linewidth=2.0, x=var1[begin_date.year], color='black')
plt.grid(axis = 'y', color='black', linewidth=0)
bins1 = np.append(bins, np.array([var1.quantile(.25), var1[begin_date.year], var1.quantile(.75)]))
bins2 = np.append(bins.round(2), np.array(['\n\n\n' + r'$q_1$=' + '{:.2f}'.format(var1.quantile(.25)), '\n' + '{:.2f}'.format(var1[begin_date.year]) + '\n ГТК за '+'{:.0f}'.format(begin_date.year) + ' г.', '\n\n\n' + r'$q_3$=' + '{:.2f}'.format(var1.quantile(.75))]))
plt.xticks(bins1, bins2, fontsize=12)
plt.yticks(np.array([0, 2, 4, 6, 8, 10, 12, 14, 16, 18]), np.array([0, 2, 4, 6, 8, 10, 12, 14, 16, 18]), fontsize=12)
for i in range(counts.size):
    plt.text((bins[i + 1] + bins[i])/2, counts[i] + 0.2, str(int(counts[i])), fontsize=12)
plt.ylim((0, 20))
plt.xlim((0, 4.25))
plt.title(title, fontsize=12)
plt.show()
plt.plot(var1)
#plt.show()

x = np.arange(9)
title = "Подекадные медианные значения гидротермического коэффициента Селянинова с 1967 по 2018 гг."
#plt.bar(x,[1.45, 1.75, 1.30, 1.35, 1.08, 1.40, 1.39, 1.64, 1.83])#средние значения
plt.bar(x,[1.09, 1.19, 0.82, 1.06, 0.92, 1.20, 1.09, 1.21, 1.68])#медианные значения
plt.xticks(x, ('I.06', 'II.06', 'III.06', 'I.07', 'II.07', 'III.07', 'I.08', 'II.08', 'III.08'))
plt.title(title)
#plt.show()