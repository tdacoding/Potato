
import csv
import numpy as np
import pandas as pd
import datetime as dt

####
#!!!!csv файл с сайта rp5.ru надо пересохрагить в excel!!!!
####
db = pd.read_csv('rp5_24_09_2019!.csv', encoding='utf8')
db['date'] = pd.to_datetime(db['date'], format='%d.%m.%Y %H:%M')
db = db.set_index(pd.DatetimeIndex(db['date']))
db = db.sort_values('date', ascending=True)
#db['New']=db['RRR'].apply(lambda x: x if type(x) == float else '0')
db['RRR'] = db['RRR'].apply(pd.to_numeric, errors='coerce')
db['RRR'].fillna(0, inplace=True)
db = db[['T', 'U', 'RRR']]
db1 = pd.DataFrame(columns = ['Сумма осадков', 'Температура поверхности почвы', 'Мин. температура пов-сти почвы между сроками', 'Макс. температура пов-сти почвы между сроками', 'Температура воздуха по сухому терм-ру', 'Мин.температура воздуха между сроками', 'Макс. темперура воздуха между сроками', 'Относительная влажность воздуха'])
db1['Сумма осадков'] = db['RRR']
db1['Температура воздуха по сухому терм-ру'] = db['T']
db1['Относительная влажность воздуха'] = db['U']
db1 = db1.loc['2018-12-31 21:00:00':]
db1.to_csv('rp5_24_09_2019!toMerge.csv', encoding='cp1251')

db = pd.read_csv('Sykt_t_data_cleaned_2019.csv', encoding='cp1251')
db1 = pd.read_csv('rp5_24_09_2019!toMerge.csv', encoding='cp1251')
# db = db.set_index(pd.DatetimeIndex(db['date']))
# print(db)
db = pd.concat([db,db1])
db.set_index('date', inplace=True)
db.sort_index(inplace=True)
db.to_csv('MeteoAndRp5_24_09_2019Merged.csv', encoding='cp1251')

