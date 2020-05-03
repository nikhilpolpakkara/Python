def problem3_7(csv_pricefile, flower):
    import csv
    
    file = open(csv_pricefile)
    for row in csv.reader(file):
          if row[0] == flower:
            print(row[1])
            
    file.close()