import csv
import numpy as np
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt

db = pd.read_csv('Sykt_t_data_day_mean_2020WithRp5.csv', encoding='cp1251')
db = db.set_index(pd.DatetimeIndex(db['date']))
print(db.head(0))

b_date = '01.01.1991'
m_date = '15.07.1991'
e_date = '31.12.1991'

temp1 = 5
temp2 = 15

begin_date = pd.to_datetime(b_date, format='%d.%m.%Y')
mid_date = pd.to_datetime(m_date, format='%d.%m.%Y')
end_date = pd.to_datetime(e_date, format='%d.%m.%Y')
inter_year = begin_date.strftime("%Y")

db_select = db[['Intraday_mean', 'Precipitation']].loc[(db.index >= begin_date) & (db.index <= mid_date)]

db1_select = db_select.loc[db_select['Intraday_mean'] < temp1]
# print(db1_select)
# print(db1_select.index.max()+dt.timedelta(days=1))
# print(db1_select.loc[db1_select.index == db1_select.index.min()])
# print(db1_select.index.min())
spring_begin = db1_select.index.max()+dt.timedelta(days=1)

db1_select = db_select.loc[db_select['Intraday_mean'] < temp2]

spring_end = db1_select.index.max()
db_select = db[['Intraday_mean', 'Precipitation']].loc[(db.index >= mid_date) & (db.index <= end_date)]
db1_select = db_select.loc[db_select['Intraday_mean'] < temp2]

autumn_begin = db1_select.index.min()
db1_select = db_select.loc[db_select['Intraday_mean'] < temp1]
autumn_end = db1_select.index.min()-dt.timedelta(days=1)

print(db1_select)
print('Весна', spring_begin, '-', spring_end)
print('Осень', autumn_begin, '-', autumn_end)


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

db3['ratio1'] = db3['ratio'].apply(lambda x: x-1 if x >= 1 else -(1/x-1))

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
var1 = db3['aut_long']

counts, bins, patches  = plt.hist(var1, bins='auto', density=0, alpha=0.6, color='gray', edgecolor="black")
title = "Гистограмма распределения продолжительности вегетационной осени с 1967 по 2020 гг. "
plt.axvline(linewidth=2.5, x=var1.quantile(.25), color='r')
plt.axvline(linewidth=2.5, x=var1.quantile(.75), color='r')
plt.axvline(linewidth=2.5, x=var1.mean(), color='blue')
plt.grid(axis = 'y', color='black', linewidth=0)
bins1 = np.append(bins, np.array([var1.quantile(.25), var1.mean(), var1.quantile(.75)]))
bins2 = np.append(bins.round(2), np.array(['\n\n\n' + r'$q_1$=' + '{:.2f}'.format(var1.quantile(.25)), '\n' + '{:.2f}'.format(var1.mean()) + '\n среднее ', '\n\n\n' + r'$q_3$=' + '{:.2f}'.format(var1.quantile(.75))]))
plt.xticks(bins1, bins2, fontsize=12)
plt.yticks(np.array([0, 2, 4, 6, 8, 10, 12, 14, 16, 18]), np.array([0, 2, 4, 6, 8, 10, 12, 14, 16, 18]), fontsize=12)
for i in range(counts.size):
    plt.text((bins[i + 1] + bins[i])/2, counts[i] + 0.2, str(int(counts[i])), fontsize=12)
# plt.ylim((0, 20))
width = bins[counts.size] - bins[0];
plt.xlim((bins[0] - width/30,  bins[counts.size] + width/30))
plt.title(title, fontsize=12)
plt.show()



db_select = db[['Intraday_mean']].loc[(db.index >= pd.to_datetime('01.04.1991', format='%d.%m.%Y')) & (db.index <= pd.to_datetime('31.08.1991', format='%d.%m.%Y'))]
plt.plot(db_select)
plt.show()