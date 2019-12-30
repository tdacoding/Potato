
import csv
import numpy as np
import pandas as pd
import datetime as dt

with open('Sykt_t_data_2019.csv', encoding='cp1251') as csvfile:
    spamreader = csv.reader(csvfile)
    fields_name = spamreader.__next__()[1:]

fields = [*fields_name[1:5],*fields_name[10:11],*fields_name[28:30],*fields_name[31:33],*fields_name[34:35],*fields_name[37:39],*fields_name[41:42],*fields_name[43:44]]
print(repr(fields))

db = pd.read_csv('Sykt_t_data_2019.csv', encoding='cp1251')
db = db[fields]
print(db.loc[0])
db['date'] = db.apply(lambda row: str(int(row[fields[0]])) + ':' + str(int(row[fields[1]]))+ ':' + str(int(row[fields[2]])) + ':' + str(int(row[fields[3]])) + ":00:00", axis=1) #+'-'+db[fields_name[6]].str
db['date'] = pd.to_datetime(db['date'], format='%Y:%m:%d:%H:%M:%S')
#db['date'] = db['date'] + dt.timedelta(hours=3)
db['date'] = db['date'] + dt.timedelta(hours=3)

db = db.set_index(pd.DatetimeIndex(db['date']))
db = db[['Сумма осадков', 'Температура поверхности почвы', 'Мин. температура пов-сти почвы между сроками', 'Макс. температура пов-сти почвы между сроками', 'Температура воздуха по сухому терм-ру', 'Мин.температура воздуха между сроками', 'Макс. темперура воздуха между сроками', 'Относительная влажность воздуха']]
# print(db.loc['2018-09-02 15:00:00']['Температура воздуха по сухому терм-ру'])
# print(db.loc['2018-09-02 18:00:00']['Температура воздуха по сухому терм-ру'])
# print(db.loc['2018-09-02 21:00:00']['Температура воздуха по сухому терм-ру'])
db.to_csv('Sykt_t_data_cleaned_2019.csv', encoding='cp1251')

