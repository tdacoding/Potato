import csv
import numpy as np
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt


db = pd.read_csv('Sykt_t_data_day_mean_2020WithRp5.csv', encoding='cp1251')
db = db.set_index(pd.DatetimeIndex(db['date']))
print(db.head(0))


# b_date = '01.01.2016'
# e_date = '31.12.2016'
b_date = '30.04.2016'
e_date = '11.10.2016'
inter_year = 2016
temperature = 10
veg_b = '30.04.2016'
veg_e = '23.09.2016'
veg_b = pd.to_datetime(veg_b, format='%d.%m.%Y')
veg_e = pd.to_datetime(veg_e, format='%d.%m.%Y')

begin_date = pd.to_datetime(b_date, format='%d.%m.%Y')
end_date = pd.to_datetime(e_date, format='%d.%m.%Y')

db_select = db[['Intraday_mean', 'Precipitation']].loc[(db.index >= begin_date) & (db.index <= end_date)]
#print(db_select['Intraday_mean'].loc[db_select['Intraday_mean'] > 20])
db1_select = db_select.loc[(db_select['Intraday_mean'] > temperature)]# & (db_select['Precipitation'] > 0)]
#print(db1_select)
#print(db1_select.loc[db1_select.index == db1_select.index.min()])
print(db1_select.index.min())
begin_date1 = db1_select.index.min()
begin_date1 =begin_date
#print(db1_select.loc[db1_select.index == db1_select.index.max()])
end_date1 = db1_select.index.max()
end_date1 = end_date
print(db1_select.index.max())
#

step = dt.timedelta(days=3)
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

date = pd.date_range(begin_date1, end_date1, freq='3D')

#date = date.append(pd.DatetimeIndex([date[-1]+step]))
#print(date)

yearData = pd.DataFrame(date, index=date, columns=['date'])


yearData['GTK'] = yearData.apply(lambda row: db['Precipitation'].loc[(db.index >= row['date']) & (db.index < row['date'] + step) & (db['Intraday_mean'] >= temperature)].sum()*10/db['Intraday_mean'].loc[(db.index >= row['date']) & (db.index < row['date'] + step) & (db['Intraday_mean'] >= temperature)].sum(), axis=1)
yearData['GTK'] = yearData['GTK'].fillna(0)
#print(yearData)
var1 = yearData['GTK']




# counts, bins, patches  = plt.hist(var1, bins=var1.size, density=0, alpha=0.6, color='gray', edgecolor="black")
# title = "Гистограмма распределения гидротермического коэффициента Селянинова с 1967 по 2020 гг. " + r"за период %s - %s," % (begin_date1.strftime("%d.%m"), end_date1.strftime("%d.%m")) + "\n" + r"показатель ГТК за %s" % (inter_year)
# #plt.text(0.4, 0, r'$\mathrm{S}^2_U=\overline{U^2}-{\overline{U}}^2$', fontsize=20)
#
# plt.grid(axis = 'y', color='black', linewidth=0)
# bins1 = bins
# print(bins)
# bins2 = bins.round(2)
# #plt.xticks(bins1, bins2, fontsize=12)
# #plt.yticks(np.array([0, 2, 4, 6, 8, 10, 12, 14, 16, 18]), np.array([0, 2, 4, 6, 8, 10, 12, 14, 16, 18]), fontsize=12)
# # for i in range(counts.size):
# #     plt.text((bins[i + 1] + bins[i])/2, counts[i] + 0.2, str(int(counts[i])), fontsize=12)
# # plt.ylim((0, 20))
# width = bins[counts.size] - bins[0];
# plt.xlim((bins[0] - width/30,  bins[counts.size] + width/30))
# plt.title(title, fontsize=12)



print(var1.size)
yearData['numer'] = np.arange(0, var1.size)
print(yearData)

bars = yearData['date'].loc[(yearData['numer'] % 5 == 0)].apply(lambda x: x.strftime('%d.%m'))
print(bars)
bars = bars.append(pd.Series([(yearData['date'].max()+step).strftime('%d.%m')], index=[yearData['date'].max()+step]))
print(bars)
title = "Диаграмма изменчивости трехдневного гидротермического коэффициента Селянинова\n" + r"%s год" % (begin_date1.strftime("%Y")) + "\n" + r"вегетационный период с %s по %s" % (veg_b.strftime("%d.%m"), veg_e.strftime("%d.%m"))
plt.title(title, fontsize=12)

y_pos = np.arange(0, var1.size) + 0.5
#print(bars)

plt.bar(y_pos, var1, width=1, color='gray', edgecolor="black", linewidth=0.5)
xtick_pos = np.arange(0, var1.size+1,5)
#xtick_pos = pd.Series([0,4,8,12,16,20,24])
#print(xtick_pos)
#bars = pd.Series(['30.04', '28.05', '25.06', '23.07', '20.08', '17.09', '15.10'])
plt.xticks(xtick_pos, bars, fontsize=12, rotation='vertical')
plt.ylim(0, 24)
plt.xlim(-0.5, var1.size+0.5)
plt.axvline(linewidth=0.75, x=0, color='b')
plt.axvline(linewidth=0.75, x=48+2/3, color='b')
plt.show()


# plt.plot(var1)
#plt.show()

# x = np.arange(9)
# title = "Подекадные медианные значения гидротермического коэффициента Селянинова с 1967 по 2019 гг."
# #plt.bar(x,[1.45, 1.75, 1.30, 1.35, 1.08, 1.40, 1.39, 1.64, 1.83])#средние значения
# plt.bar(x,[1.09, 1.19, 0.82, 1.06, 0.92, 1.20, 1.09, 1.21, 1.68])#медианные значения
# plt.xticks(x, ('I.06', 'II.06', 'III.06', 'I.07', 'II.07', 'III.07', 'I.08', 'II.08', 'III.08'))
# plt.title(title)
#plt.show()
# title = "График изменчивости понедельного гидротермического коэффициента Селянинова\n" + r"%s год" % (begin_date1.strftime("%Y")) + "\n" + r"отображен период с %s по %s" % (yearData['date'].min().strftime("%d.%m"), (yearData['date'].max()+step).strftime("%d.%m"))
# plt.title(title, fontsize=12)
# var1.plot()
# plt.show()