import csv
import sys

filename = sys.argv[1]

f = open(filename)
for row in csv.reader(f):
    print(row)
f.close()