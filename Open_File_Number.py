
import os
import glob

os.chdir('C:\\Users\\zacth\\Desktop')
file = open("Line_Count.txt", "r+")
count = int(file.read(),)
os.chdir('C:\\Users\\zacth\\Desktop\\Data')

to = count+2

for f in glob.glob('*.txt')[count:to]:
    print(f)
    with open(f) as inputfile:
        print(f)


        
file.seek(0)
file.write(str(to))
file.close()
