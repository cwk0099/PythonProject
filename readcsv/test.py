from read_csv import ReadCsv

re = ReadCsv('csvtest.csv')
res = re.readline()
title = re.readtitle()
row = re.onerow('username')
print(title)
print(row)
print(res)
re.closecsv()