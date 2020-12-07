import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next (csvreader)
    print(header)
    
    total_months = 0
    total_amount = 0

    for row in csvreader:
        total_months= total_months +1
        total_amount= total_amount + int(row[1])

    print (total_amount)
    print (total_months)
