import os
import sys

os.chdir('C:\\Users\\zacth\\Desktop')

d = open("URL Data.txt")
x = 0

num_lines = sum(1 for line in d)

print (num_lines/2)
