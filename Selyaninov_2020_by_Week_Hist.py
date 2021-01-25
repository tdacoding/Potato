import csv
import numpy as np
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt


db = pd.read_csv('Sykt_t_data_day_mean_2020WithRp5.csv', encoding='cp1251')
db = db.set_index(pd.DatetimeIndex(db['date']))
print(db.head(0))


b_date = '01.01.2016'
e_date = '31.12.2016'
#b_date = '05.05.2016'
#e_date = '22.09.2016'
inter_year = 2016
temperature = 10

begin_date = pd.to_datetime(b_date, format='%d.%m.%Y')
end_date = pd.to_datetime(e_date, format='%d.%m.%Y')

db_select = db[['Intraday_mean', 'Precipitation']].loc[(db.index >= begin_date) & (db.index <= end_date)]
#print(db_select['Intraday_mean'].loc[db_select['Intraday_mean'] > 20])
db1_select = db_select.loc[(db_select['Intraday_mean'] > temperature) & (db_select['Precipitation'] > 0)]
#print(db1_select)
#print(db1_select.loc[db1_select.index == db1_select.index.min()])
print(db1_select.index.min())
begin_date1 = db1_select.index.min()
# begin_date1 =begin_date
#print(db1_select.loc[db1_select.index == db1_select.index.max()])
end_date1 = db1_select.index.max()
# end_date1 = end_date
print(db1_select.index.max())
#

step = dt.timedelta(days=7)
# d1 = begin_date1
# d2 = end_date1
# while True:
#     d2 = d1 + step
#     print(d1.strftime('%d.%m.%Y') + '-' + d2.strftime('%d.%m.%Y'))
#     db_select = db[['Intraday_mean', 'Precipitation']].loc[
#         (db.index >= d1) & (db.index < d2) & (db['Intraday_mean'] >= temperature)]
#     temp_sum = db_select['Intraday_mean'].sum()
#     temp_mean = db_select['Intraday_mean'].mean()
#     print('Сумма среднесуточных температур выше', temperature, 'градусов за период:', temp_sum)
#     print('Седнее среднесуточных температур выше', temperature, 'градусов за период:', temp_mean)
#
#     precip_sum = db_select['Precipitation'].sum()
#     print('Сумма осадков при температуре выше 10 градусов за период:', precip_sum)
#     if not db_select.empty:
#         K_sel = precip_sum * 10 / temp_sum
#     else:
#         K_sel = 0
#     print('Коэффицент Селянинова за период:', K_sel)
#     if d2 >= end_date1:
#         break
#     d1 = d2

date = pd.date_range(begin_date1, end_date1, freq='W-' + pd.to_datetime(begin_date1).strftime('%a'))

yearData = pd.DataFrame(date, index=date, columns=['date'])


yearData['GTK'] = yearData.apply(lambda row: db['Precipitation'].loc[(db.index >= row['date']) & (db.index < row['date'] + step) & (db['Intraday_mean'] >= temperature)].sum()*10/db['Intraday_mean'].loc[(db.index >= row['date']) & (db.index < row['date'] + step) & (db['Intraday_mean'] >= temperature)].sum(), axis=1)
yearData['GTK'] = yearData['GTK'].fillna(0)
#print(yearData)
var1 = yearData['GTK']


counts, bins, patches  = plt.hist(var1, bins='auto', density=0, alpha=0.6, color='gray', edgecolor="black")
title = "Гистограмма распределения понедельного гидротермического коэффициента Селянинова " + r"за %s год" % (begin_date1.strftime("%Y"))
#plt.text(0.4, 0, r'$\mathrm{S}^2_U=\overline{U^2}-{\overline{U}}^2$', fontsize=20)
# plt.axvline(linewidth=2.5, x=var1.quantile(.25), color='r')
# plt.axvline(linewidth=2.5, x=var1.quantile(.75), color='r')
plt.grid(axis = 'y', color='black', linewidth=0)
bins1 = bins#, np.array([var1.quantile(.25), var1.quantile(.75)]))
bins2 = bins.round(2)#, np.array(['\n\n' + r'$q_1$=' + '{:.2f}'.format(var1.quantile(.25)), '\n\n' + r'$q_3$=' + '{:.2f}'.format(var1.quantile(.75))]))
plt.xticks(bins1, bins2, fontsize=12)
plt.yticks(np.array([0, 2, 4, 6, 8, 10, 12, 14, 16, 18]), np.array([0, 2, 4, 6, 8, 10, 12, 14, 16, 18]), fontsize=12)
for i in range(counts.size):
    plt.text((bins[i + 1] + bins[i])/2, counts[i] + 0.2, str(int(counts[i])), fontsize=12)
plt.ylim((0, 14))
width = bins[counts.size] - bins[0];
plt.xlim((bins[0] - width/30,  bins[counts.size] + width/30))
plt.title(title, fontsize=12)
plt.show()