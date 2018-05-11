import csv
import numpy as np
import pandas as pd
import datetime as dt


db1 = pd.read_csv('Sykt_t_data_day_mean.csv', encoding='cp1251')
#db1 = db1.set_index(pd.DatetimeIndex(db1['date']))
db2 = pd.read_csv('Sykt_Soil_t_data.csv', encoding='cp1251')
#db2 = db2.set_index(pd.DatetimeIndex(db2['date']))
#print(db2[(~db2.index.isin(db1.index))])
print(db1.head(0))
print(db2.head(0))
db1 = db1.join(db2[['20cm', '40cm', '80cm', '160cm', '320cm']])
db1 = db1.set_index(pd.DatetimeIndex(db1['date']))
del db1['date']
db1.to_csv('Sykt_t_and_soil_exel.csv', encoding='cp1251', sep=";", decimal=",")
# db1.to_csv('Sykt_t_and_soil.csv', encoding='cp1251')

