import zipfile
import numpy as np
import pandas as pd
from io import StringIO

flen = []
fields_name = []
db = {}
archive = zipfile.ZipFile('wr3288a4.zip', 'r')
fields = archive.read('fld3288a4.txt').decode('cp1251').split('\r\n')
fields.remove('')
for line in fields:
     flen.append([int(line[10:13].strip()[0]), line[15:].strip()])
     db[line[15:].strip()] = []
     fields_name.append(line[15:].strip())

print(fields_name)
print(db)

data = archive.read('wr3288a4.txt').decode('cp1251').split('\r\n')
data.remove('')
for line in data:
    p = 0
    for i in range(len(db)):
        db[flen[i][1]].append(line[p:p+flen[i][0]].strip())
        p += flen[i][0] + 1
#print(flen[1][1])

#print(db[flen[25][1]][-10:150969])
d = pd.DataFrame.from_dict(db)
d = d[fields_name]
d.to_csv('example.csv', encoding='cp1251')
