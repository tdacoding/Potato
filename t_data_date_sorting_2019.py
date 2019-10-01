import csv
import numpy as np
import pandas as pd
import datetime as dt


db = pd.read_csv('Sykt_t_data_cleaned_2019.csv', encoding='cp1251')
db = db.set_index(pd.DatetimeIndex(db['date']))
db = db.loc['1967-01-01':]



db = db.sort_values('date', ascending=False)
del db['date']
db.to_csv('Sykt_t_data_date_sorted_2019.csv', encoding='cp1251')
# db1.to_csv('Sykt_t_data_day_mean_exel.csv', encoding='cp1251', sep=";", decimal=",")