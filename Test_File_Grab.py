import pandas as pd
import os
import safebrowsing
import numpy
import numbers
import sys

os.chdir('C:\\Users\\zacth\\Desktop\\Data')

folder = 'C:\\Users\\zacth\\Desktop\\Data'

FileLst = []


for root, dirs, files in os.walk(folder):
    with open('files.txt', 'w') as f:
        for item in files:
            f.write("%s\n" % item)
