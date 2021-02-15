import csv
import numpy as np
import pandas as pd
import datetime as dt


db = pd.read_csv('MeteoAndRp5_15_02_2021Merged.csv', encoding='cp1251')
db = db.set_index(pd.DatetimeIndex(db['date']))
db = db.loc['1967-01-01':]
grouped = db.groupby(db.index.date)
db1 = pd.DataFrame({'Intraday_mean': grouped[u'Температура воздуха по сухому терм-ру'].agg(np.mean),
                    'Intraday_min': grouped[u'Мин.температура воздуха между сроками'].agg(np.min),
                    'Intraday_max': grouped[u'Макс. темперура воздуха между сроками'].agg(np.max),
                    'Precipitation': grouped[u'Сумма осадков'].agg(np.sum),
                    'Humidity': grouped[u'Относительная влажность воздуха'].agg(np.mean),
                    'Soil_min': grouped[u'Мин. температура пов-сти почвы между сроками'].agg(np.min),
                    'Soil_mean': grouped[u'Температура поверхности почвы'].agg(np.mean),
                    'Soil_max': grouped[u'Макс. температура пов-сти почвы между сроками'].agg(np.max),})
db1['date'] = pd.to_datetime(db1.index, format='%Y-%m-%d')
db1 = db1.set_index(pd.DatetimeIndex(db1['date']))
db1 = db1.round(2)
db1 = db1[['date', 'Intraday_min', 'Intraday_max', 'Intraday_mean', 'Soil_min', 'Soil_max', 'Soil_mean', 'Precipitation', 'Humidity']]

db2 = pd.DataFrame({'date': pd.date_range('1981-11-01', '1981-11-30', freq='d'), 'Intraday_mean': np.nan, 'Intraday_max': np.nan, 'Intraday_mean': np.nan, 'Soil_min': np.nan, 'Soil_max': np.nan, 'Soil_mean': np.nan, 'Precipitation': np.nan, 'Humidity': np.nan})
db2 = db2.set_index(pd.DatetimeIndex(db2['date']))


db1 = db1.append(db2)
del db1['date']
db1 = db1.sort_values('date')

db1.to_csv('Sykt_t_data_day_mean_2021WithRp5.csv', encoding='cp1251')
# db1.to_csv('Sykt_t_data_day_mean_exel.csv', encoding='cp1251', sep=";", decimal=",")