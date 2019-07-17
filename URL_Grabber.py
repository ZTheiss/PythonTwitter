import pandas as pd
import os
import safebrowsing
import numpy
import numbers
import sys
import glob

os.chdir('C:\\Users\\zacth\\Desktop')
file = open("Line_Count.txt", "r+")
count = int(file.read(),)

t = open("All URLs 3.txt", "a+")
f = open("New URLs 10.txt", "a+")
d = open("URL Output with Date Data 3.txt", "a+")

os.chdir('C:\\Users\\zacth\\Desktop\\Data')

to = count+1

#name = input("Current File: ")
#x = 0
for name in glob.glob('*.txt')[count:to]:
    with open(name) as inputfile:
        print(name)
        data = pd.read_json(name, lines=True)
        data.shape
        df = pd.DataFrame.from_dict(data, orient='columns')
        source_list = df['source'].tolist()
        created_list = df['created_at'].tolist()

        final_list = source_list
        create_final_list = created_list

        y = 0
        while y < len(source_list):
            try:
                if not final_list[y]:
                    y += 1
                elif type(source_list[y]) == float:
                    y += 1
                elif type(source_list[y]) == str:
                    final_list[y] = source_list[y].replace('href="', '').replace('"', '').split()
                    final_list[y] = source_list[y][1]
                    f.write('{0}\n'.format(final_list[y]))
                    t.write('{0}\n'.format(final_list[y]))
                    d.write('{0}\n'.format(final_list[y]))
                    d.write('{0}\n'.format(create_final_list[y]))
                    y += 1
            except:
                y += 1
                continue
print("Wrote")
file.seek(0)
file.write(str(to))
file.close()
sys.exit()
