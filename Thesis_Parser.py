import pandas as pd
import os
import safebrowsing
import numpy
import numbers

URLList = []

os.chdir('C:\\Users\\zacth\\Desktop')
f = open("PythonOutput.txt", "a+")

os.chdir('E:\Documents\School\Thesis\Json Data\Data')

for root, dirs, files in os.walk('E:\Documents\School\Thesis\Json Data\Data'):
        x = 0
        for name in files:
                x = 0
                print(name)
                data = pd.read_json(name, lines=True)
                data.shape
                df = pd.DataFrame.from_dict(data, orient='columns')
                source_list = df['source'].tolist()
                final_list = source_list
                y = 0
                while y < len(source_list):
                        if type(source_list[y]) == float:
                                y += 1
                        if type(source_list[y]) == str:
                                final_list[y] = source_list[y].replace('href="', '').replace('"', '').split()
                                final_list[y] = source_list[y][1]
                                y += 1
        
                del df
                x = 0
                apikey = '$$$$$$$$$$$$$$$$$$$$$$$$$'
                sb = safebrowsing.LookupAPI(apikey)
                print ("Starting Google API")
                while x < 1: #len(final_list):
                        resp = sb.threat_matches_find(final_list[x])
                        print (resp)
                        if (len(resp) > 0):
                                if (isinstance(final_list[x], float)):
                                        print("")
                                else:
                                        f.write('{0} {1} {2}\n'.format(x, final_list[x], resp))
                                        URLList.append(final_list[x])
                        x = x + 1

                #Not working. ValueError: Could not reserve memory block
                #Not enough memory, need to dump between runs
                source_list.clear()

