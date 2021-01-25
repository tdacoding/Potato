import csv
import numpy as np
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import math

db = pd.read_csv('Sykt_t_data_day_mean_2020WithRp5.csv', encoding='cp1251')
db = db.set_index(pd.DatetimeIndex(db['date']))
# print(db.head(0))


b_date = '01.01.2018'
e_date = '31.12.2018'
inter_year = 2018
temperature = 10

begin_date = pd.to_datetime(b_date, format='%d.%m.%Y')
end_date = pd.to_datetime(e_date, format='%d.%m.%Y')




# db_select = db[['Intraday_max','Intraday_min']].loc[(((db.index.month > begin_date.month) & (db.index.month < end_date.month)) | ((begin_date.month < end_date.month) & (((db.index.month == begin_date.month) & (db.index.day >= begin_date.day)) | ((db.index.month == end_date.month) & (db.index.day <= end_date.day)))) | ((begin_date.month == end_date.month) & (db.index.month == end_date.month) & (db.index.day >= begin_date.day) & (db.index.day <= end_date.day))) & (db.index.year < 2019)]
db_select = db[['Intraday_mean']].loc[(((db.index.month > begin_date.month) & (db.index.month < end_date.month)) | ((begin_date.month < end_date.month) & (((db.index.month == begin_date.month) & (db.index.day >= begin_date.day)) | ((db.index.month == end_date.month) & (db.index.day <= end_date.day)))) | ((begin_date.month == end_date.month) & (db.index.month == end_date.month) & (db.index.day >= begin_date.day) & (db.index.day <= end_date.day))) & (db.index.year < 2020) & (db['Intraday_mean'] >= 10)]
db_select = db_select.fillna(0)
db1 = db_select.groupby(db_select.index.year).agg(['sum'])
db2=db1['Intraday_mean']
#print(db_select)
# print(db1)
var1 = db2
print(var1)
print(var1.mean())
print(math.sqrt(var1.var()))
print(var1.min())
print(var1.min().index)
print(var1.max())
print(var1.max().index)
# print(pd.Series(db2['mean']))
# regressor = LinearRegression()
# x=var1.index.to_numpy().reshape(53, 1)
# y=np.reshape(db2.to_numpy(), (53, 1))
# # print(x)
# # print(y)
#
# #
# #
# regressor.fit(x, y) #actually produces the linear eqn for the data
# y_pred = regressor.predict(x)
#
# print(regressor.coef_)
# print(regressor.intercept_)
# plt.plot(x, y, color='blue')
# # # plt.plot(x, y_pred, color='grey')
# var1.plot()
# # # plt.legend().remove()
# plt.xlabel('Год')
# plt.ylabel('Средняя температура')
# # # # plt.legend(['Максимальная суточная','Минимальная суточная'])
# # # #plt.legend(['Влажность*температура'])
# plt.title('Среднее значение биологически активных температур', fontsize=12)
# plt.show()
