import csv
import sys,os

curDir = os.path.dirname(
            os.path.abspath(__file__)
            )
csvFilePath = os.path.join(curDir,"names.csv")

with open(csvFilePath, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['first_name'], row['last_name'])




print(row)