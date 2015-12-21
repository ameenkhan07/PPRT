
import pandas as pd
import random
import csv
fi = open("graph3.csv","r")
rd = csv.reader(fi)

date=[]
freq=[]

for row in rd:
    date.append(row[0])
    freq.append(row[1])    
    

idx = pd.DatetimeIndex(date)
AO = pd.Series(freq,index=idx)
per = AO.resample('D', how='sum')
per.plot(kind='area')
