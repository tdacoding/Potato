
import csv
import numpy as np
import pandas as pd
import datetime as dt

with open('Sykt_temp_data.csv', encoding='cp1251') as csvfile:
    spamreader = csv.reader(csvfile)
    fields_name = spamreader.__next__()[1:]
fields = [*fields_name[5:10],*fields_name[15:17],*fields_name[18:20],fields_name[21],*fields_name[24:26],*fields_name[27:29]]
print(repr(fields))
#     for row in spamreader:
#         print(row)
db = pd.read_csv('Sykt_temp_data.csv', encoding='cp1251')
db = db[fields]
print(db.loc[0])
db['time'] = db.apply(lambda row: str(int(row[fields[0]])) + ':' + str(int(row[fields[1]]))+ ':' + str(int(row[fields[2]])) + ':' + str(int(row[fields[3]])) + ":00:00", axis=1) #+'-'+db[fields_name[6]].str
db['time'] = pd.to_datetime(db['time'], format='%Y:%m:%d:%H:%M:%S')

db = db.set_index(pd.DatetimeIndex(db['time']))
print(db.loc['1966-01-02 03:00:00'])

#db.to_csv('Sykt_temp_data_cleaned.csv', encoding='cp1251')

