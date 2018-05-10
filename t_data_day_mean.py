import csv
import numpy as np
import pandas as pd
import datetime as dt


db = pd.read_csv('Sykt_t_data_cleaned.csv', encoding='cp1251')
db = db.set_index(pd.DatetimeIndex(db['time']))
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
db1 = db1.round(2)
db1 = db1[['Intraday_min', 'Intraday_max', 'Intraday_mean', 'Soil_min', 'Soil_max', 'Soil_mean', 'Precipitation', 'Humidity']]

#db1.to_csv('Sykt_t_data_day_mean_exel.csv', encoding='cp1251', sep=";", decimal=",")

db1.to_csv('Sykt_t_data_day_mean.csv', encoding='cp1251')
