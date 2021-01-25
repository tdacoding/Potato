import csv
import numpy as np
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib.axis import Axis
from matplotlib.dates import DayLocator, HourLocator, DateFormatter, drange

db = pd.read_csv('Sykt_t_data_day_mean_2020WithRp5.csv', encoding='cp1251')
db = db.set_index(pd.DatetimeIndex(db['date']))
print(db.head(0))


b_date = '01.01.2020'
e_date = '31.12.2020'

inter_year = 2020
temperature = 10


begin_date = pd.to_datetime(b_date, format='%d.%m.%Y')
end_date = pd.to_datetime(e_date, format='%d.%m.%Y')

db_select = db[['Intraday_mean', 'Precipitation']].loc[(db.index >= begin_date) & (db.index <= end_date)]

db1_select = db_select.loc[(db_select['Intraday_mean'] >= temperature)]# & (db_select['Precipitation'] > 0)]

print(db1_select.index.min())
begin_date1 = db1_select.index.min()

end_date1 = db1_select.index.max()

print(db1_select.index.max())


step = dt.timedelta(days=1)

date = pd.date_range(begin_date1, end_date1, freq='1D')

print(date)

yearData = pd.DataFrame(date, index=date, columns=['date'])


yearData['GTK'] = yearData.apply(lambda row: db['Precipitation'].loc[(db.index >= row['date']) & (db.index < row['date'] + step) & (db['Intraday_mean'] >= temperature)].sum()*10/db['Intraday_mean'].loc[(db.index >= row['date']) & (db.index < row['date'] + step) & (db['Intraday_mean'] >= temperature)].sum(), axis=1)
yearData['GTK'] = yearData['GTK'].fillna(0)
print(yearData)
var1 = yearData['GTK']






#
# step = dt.timedelta(days=7)
#
# date = pd.date_range(begin_date1, end_date1, freq='7D')
#
# print(date)
# barData = pd.DataFrame(date, index=date, columns=['date'])
# bars = barData['date'].apply(lambda x: x.strftime('%d.%m'))
#
# bars = bars.append(pd.Series([(barData['date'].max()+step).strftime('%d.%m')], index=[barData['date'].max()+step]))

# title = "Диаграмма изменчивости суточного гидротермического коэффициента Селянинова\n" + r"%s год" % (begin_date1.strftime("%Y")) + "\n" + r"вегетационный период с %s по %s" % (begin_date1.strftime("%d.%m"), end_date1.strftime("%d.%m"))
# plt.title(title, fontsize=12)

# y_pos = np.arange(0, var1.size)

#
# # plt.Axes.bar(y_pos, var1)#, edgecolor="black", linewidth=0.5)
#
# date = pd.date_range(begin_date1, end_date1, freq='7D')-dt.timedelta(days=7)
# Date = pd.DataFrame(date, index=date, columns=['date'])
# bars = Date['date'].apply(lambda x: x.strftime('%d.%m'))
# bars = bars.append(pd.Series([(yearData['date'].max()+dt.timedelta(days=7)).strftime('%d.%m')], index=[yearData['date'].max()+dt.timedelta(days=7)]))
# print(bars)
# xtick_pos = np.arange(0, bars+1)
# # print(bars)
# fig, ax = plt.subplots()

# print(var1.size)
delta = dt.timedelta(days=1)
dates = pd.date_range(begin_date1, end_date1, freq='1D')
print(dates)

fig, ax = plt.subplots()
ax.bar(dates, var1)

ax.set_xlim(dates[0], dates[-1]+delta)

ax.xaxis.set_major_locator(DayLocator(interval=7))
Axis.set_minor_locator(ax.xaxis, DayLocator())
ax.xaxis.set_major_formatter(DateFormatter('%d.%m'))

ax.fmt_xdata = DateFormatter('%Y-%m-%d %H:%M:%S')
fig.autofmt_xdate()

fig.suptitle("Диаграмма изменчивости суточного гидротермического коэффициента Селянинова\n" + r"%s год" % (begin_date1.strftime("%Y")) + "\n" + r"вегетационный период с %s по %s" % (begin_date1.strftime("%d.%m"), end_date1.strftime("%d.%m")), fontsize=12, fontweight='bold')

plt.show()











# ax.xaxis.set_major_locator(xtick_pos)
# ax.xaxis.set_minor_locator(MultipleLocator(1))
# plt.xticks(MultipleLocator(7), bars, fontsize=12, rotation='vertical')
# ax.xaxis.set_major_formatter(FormatStrFormatter('%d'))
# xtick_pos = np.arange(0, var1.size+1)
# # xtick_pos = pd.Series([0,4,8,12,16,20,24])
# print(xtick_pos)
# # bars = pd.Series(['30.04', '28.05', '25.06', '23.07', '20.08', '17.09', '15.10'])
# bars=[]
# plt.xticks(xtick_pos, bars, fontsize=12, rotation='vertical')
# # plt.tick_params(axis='x', width=2.5, color='black')
# # plt.ylim(0, 8)
# plt.xlim(-0.5, var1.size+0.5)
# # plt.axvline(linewidth=0.75, x=0, color='b')
# plt.axvline(linewidth=0.75, x=14+6/10, color='b')
# plt.show()

