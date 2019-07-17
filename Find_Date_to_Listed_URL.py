import numpy as np
import pandas as pd
import os
os.chdir('C:\\Users\\zacth\\Desktop')
f = open("URL Output Data 3.txt")
l = open("All Listed URLs.txt", encoding='utf16')
d = open("Final URLs 3.txt", "w")

def goto(linenum):
    global line
    line = linenum

for line1 in l:
    #print(line1)
    f.seek(0)
    for line2 in f:
        #print(line1)
        #print(line2)
        if line1 == line2:
            d.write(line1)
            d.write(f.readline())
            line2 += "DONE"
            line1 = l.readline()
        else:
            continue


d.close()
l.close()
f.close()
            

