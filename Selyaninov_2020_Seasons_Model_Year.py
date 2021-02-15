import csv
import numpy as np
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt

db = pd.read_csv('Sykt_t_data_day_mean_2021WithRp5.csv', encoding='cp1251')
db = db.set_index(pd.DatetimeIndex(db['date']))
# print(db.head(0))

temp1 = 5
temp2 = 15

b_date = '01.01.2016'
e_date = '31.12.2016'
begin_date = pd.to_datetime(b_date, format='%d.%m.%Y')
end_date = pd.to_datetime(e_date, format='%d.%m.%Y')
db2 = db[['Intraday_mean', 'Precipitation']].loc[(db.index >= begin_date) & (db.index <= end_date)]
i = db2.loc[(db2.index.month == 2) & (db2.index.day == 29)].index
if not i.empty:
    db2.drop(i, inplace=True)

b_date = '01.01.2017'
e_date = '31.12.2017'
begin_date = pd.to_datetime(b_date, format='%d.%m.%Y')
end_date = pd.to_datetime(e_date, format='%d.%m.%Y')
db3 = db[['Intraday_mean', 'Precipitation']].loc[(db.index >= begin_date) & (db.index <= end_date)]
i = db3.loc[(db3.index.month == 2) & (db3.index.day == 29)].index
if not i.empty:
    db3.drop(i, inplace=True)

b_date = '01.01.2018'
e_date = '31.12.2018'
begin_date = pd.to_datetime(b_date, format='%d.%m.%Y')
end_date = pd.to_datetime(e_date, format='%d.%m.%Y')
db4 = db[['Intraday_mean', 'Precipitation']].loc[(db.index >= begin_date) & (db.index <= end_date)]
i = db4.loc[(db4.index.month == 2) & (db4.index.day == 29)].index
if not i.empty:
    db4.drop(i, inplace=True)

b_date = '01.01.2019'
e_date = '31.12.2019'
begin_date = pd.to_datetime(b_date, format='%d.%m.%Y')
end_date = pd.to_datetime(e_date, format='%d.%m.%Y')
db5 = db[['Intraday_mean', 'Precipitation']].loc[(db.index >= begin_date) & (db.index <= end_date)]
i = db5.loc[(db5.index.month == 2) & (db5.index.day == 29)].index
if not i.empty:
    db5.drop(i, inplace=True)

b_date = '01.01.2020'
e_date = '31.12.2020'
begin_date = pd.to_datetime(b_date, format='%d.%m.%Y')
end_date = pd.to_datetime(e_date, format='%d.%m.%Y')
db6 = db[['Intraday_mean', 'Precipitation']].loc[(db.index >= begin_date) & (db.index <= end_date)]
i = db6.loc[(db6.index.month == 2) & (db6.index.day == 29)].index
if not i.empty:
    db6.drop(i, inplace=True)

db_select = db[['Intraday_mean', 'Precipitation']]
db1 = db_select.groupby(db_select.index.strftime("%m.%d")).agg(['mean'])
i = db1.loc[(db1.index == '02.29')].index
db1.drop(i, inplace=True)
db1['days'] = db1.index

db1['days'] = pd.to_datetime(db1['days'].values + '.2000', format='%m.%d.%Y')
db1['days'] = db1['days'].apply(lambda x: x.strftime('%d.%m'))

db1_select = db1.loc[db1['Intraday_mean'].values >= temp1]
print(db1_select)

# print(db1_select.loc[db1_select.index == db1_select.index.min()])
# print(db1_select.index.min())
spring_begin = db1_select['days'].loc[db1_select.index.min()]
# print(db1_select.loc[db1_select.index == db1_select.index.max()])
autumn_end = db1_select['days'].loc[db1_select.index.max()]
# print(db1_select.index.max())
db1_select = db1.loc[db1['Intraday_mean'].values >= temp2]
spring_end = db1_select['days'].loc[db1_select.index.min()]
autumn_begin = db1_select['days'].loc[db1_select.index.max()]
print('Весна', spring_begin, '-', spring_end)
print('Осень', autumn_begin, '-', autumn_end)




plt.plot(db1['days'].values, db1['Intraday_mean'].values, label='норма')
locs, labels = plt.xticks()

labels = np.array(['01.01', '01.02', '01.03', '01.04', '01.05', '01.06', '01.07', '01.08', '01.09', '01.10', '01.11', '01.12', '31.12'])
locs = np.append(labels, np.array([spring_begin, spring_end, autumn_begin, autumn_end]))
labels = np.append(labels, np.array(['\n' + spring_begin, '\n' + spring_end, '\n' + autumn_begin, '\n' + autumn_end]))
plt.xticks(locs, labels, fontsize=10)
# plt.plot(db2['Intraday_mean'].values, label='2016')
# plt.plot(db3['Intraday_mean'].values, label='2017')
# plt.plot(db4['Intraday_mean'].values, label='2018')
# plt.plot(db5['Intraday_mean'].values, label='2019')
plt.plot(db6['Intraday_mean'].values, label='2020')
plt.axvline(linewidth=1.0, x=spring_begin, color='gray')
plt.axvline(linewidth=1.0, x=spring_end, color='gray')
plt.axvline(linewidth=1.0, x=autumn_begin, color='gray')
plt.axvline(linewidth=1.0, x=autumn_end, color='gray')

plt.legend()
plt.show()

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


