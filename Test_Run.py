import pandas as pd
import os
import safebrowsing
import numpy
import numbers

URLList = []

os.chdir('C:\\Users\\zacth\\Desktop')
f = open("PythonOutput.txt", "a+")

os.chdir('E:\Documents\School\Thesis\Json Data\Data')

file = "xab.json"
x = 0
print(file)
data = pd.read_json(file, lines=True)
data.shape
df = pd.DataFrame.from_dict(data, orient='columns')
source_list = df['source'].tolist()
final_list = source_list
y = 0
while y < len(source_list):
    if source_list[y] == '':
        y += 1
    elif type(source_list[y]) == float:
        y += 1
    elif type(source_list[y]) == str:
        final_list[y] = source_list[y].replace('href="', '').replace('"', '').split()
        final_list[y] = source_list[y][1]
        y += 1

z = 0

        
x = 0
apikey = '$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$'
sb = safebrowsing.LookupAPI(apikey)
print ("Starting Google API")
x = 9829 #19828
while x < 9830: #len(final_list):
        resp = sb.threat_matches_find(final_list[x])
        print(resp, x)
        if (len(resp) > 0):
                if (isinstance(final_list[x], float)):
                        print("")
                else:
                        f.write('{0} {1} {2}\n'.format(x, final_list[x], resp))
                        URLList.append(final_list[x])
        x = x + 1

