import numpy as np
import pandas as pd
import os
os.chdir('C:\\Users\\zacth\\Desktop')
f = open("URL Output Data.txt")

date_list = []
source_list = []


for line in f:
    #print(line)
    line = line.strip('\n')
    if '2018' in line:
        date_list.append(line)
    else:
        source_list.append(line)

df = pd.DataFrame({'date': date_list})
df['URL'] = source_list
#df.corr()
