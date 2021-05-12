#   .csv - данные разделенные запятыми, табличне данные) сырые данные
import csv
with open ("test.csv", 'r' ) as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
    for row in reader:
        print(row)