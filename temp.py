
import csv
import numpy as np
import pandas as pd

with open('example.csv') as csvfile:
    spamreader = csv.reader(csvfile)
    fields_name = spamreader.__next__()[1:]
fields = [fields_name[0]]+fields_name[5:10]+fields_name[15:17]+fields_name[18:20]+[fields_name[21]]+fields_name[24:26]+fields_name[27:29]
print(fields)
#     for row in spamreader:
#         print(row)
db = pd.read_csv('example.csv', encoding='cp1251')

db = db[fields]
print(db)
