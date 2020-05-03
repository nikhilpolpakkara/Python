import csv

def read_csv_file2(filename):
    """Reads a CSV file and prints each row without list brackets. """
    f = open(filename)
    for row in csv.reader(f):
        print()
        for i in range(0,len(row)):
            print(row[i],end=" ")
    f.close()