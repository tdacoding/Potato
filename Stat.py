import csv
import numpy as np
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt


db = pd.read_csv('Sykt_t_and_soil.csv', encoding='cp1251')
db = db.set_index(pd.DatetimeIndex(db['date']))
print(db.head(0))
# var = db['Soil_mean'].loc[(db.index.month == 1) | (db.index.month == 2) | (db.index.month == 12)]
# print(var.mean())
# var.hist(bins='auto', density=1, alpha=0.6, color='g',edgecolor="b")
var = db['Soil_mean'].loc[(db.index.month == 6) | (db.index.month == 7) | (db.index.month == 8)]
print('mean:', var.mean())
print('max:', var.max())
print('min:', var.min())
var.hist(bins='auto', density=1, alpha=0.6, color='g',edgecolor="b")
var = db['20cm'].loc[(db.index.month == 6) | (db.index.month == 7) | (db.index.month == 8)]
print('mean:', var.mean())
print('max:', var.max())
print('min:', var.min())
var.hist(bins='auto', density=1, alpha=0.6, color='r',edgecolor="b")
#var.plot()
plt.show()
var = db['Intraday_mean'].loc[(db.index.month == 6) | (db.index.month == 7) | (db.index.month == 8)]
print('mean:', var.mean())
print('max:', var.max())
print('min:', var.min())
