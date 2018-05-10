import numpy as np
import pandas as pd
from io import StringIO


with open('Sykt_Soil_2017_09.dat') as archive:
    db = {'time': [], '20cm': [], '40cm': [], '80cm': [], '160cm': [], '320cm': []}
    archive.__next__()
    for line in archive:
        db['time'].append(str(int(line[6:10].strip())) + ':' + str(int(line[11:13].strip())) + ':' + str(int(line[14:16].strip())))
        db['20cm'].append(int(line[45:49].strip()))
        db['40cm'].append(int(line[52:56].strip()))
        db['80cm'].append(int(line[66:70].strip()))
        db['160cm'].append(int(line[80:84].strip()))
        db['320cm'].append(int(line[94:98].strip()))

d = pd.DataFrame.from_dict(db)

d = d[['time', '20cm', '40cm', '80cm', '160cm', '320cm']]
#print(d)
#d.to_csv('Sykt_t_data.csv', encoding='cp1251')
d['time'] = pd.to_datetime(d['time'], format='%Y:%m:%d', errors='coerce')
d = d[d['time'].notnull()]
d = d.replace({9999: np.nan})
d[d.select_dtypes(include=['number']).columns] /= 10

d = d.set_index(pd.DatetimeIndex(d['time']))
d = d.loc[:'2017-09-30']
d.to_csv('Sykt_Soil_t_data_exel.csv', encoding='cp1251', sep=";", decimal=",")
#d.to_csv('Sykt_Soil_t_data.csv', encoding='cp1251')

