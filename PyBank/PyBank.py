import os
import csv

csvpath = os.path.join("Resources/budget_data.csv")
txtpath = os.path.join("Analysis/budget_data.txt")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next (csvreader)
    print(header)
    
    total_months = 0
    total_amount = 0
    previous = 0
    change = 0
    change_list = []
    maxchange = 0
    maxdate = ""
    minchange = 99999999
    mindate = ""

#loop through to find total of months 
    for row in csvreader:
        total_months= total_months +1
        total_amount= total_amount + int(row[1])
        change=int(row[1])- previous  
        change_list.append(change)  
        previous = int(row[1])

        if change>maxchange:
            maxchange=change
            maxdate=row[0]

        if change<minchange:
            minchange=change
            mindate=row[0]

    average_change = sum (change_list[1:])/len (change_list[1:])

    print(f"Total Months: {total_months}")
    print(f"Total Amount: {total_amount}")   
    # print (change_list)
    print(f"Average Change: {average_change}")
    print(f"Greatest Increase {maxchange}{maxdate}")
    print(f"Greatest Decrease {minchange}{mindate}")

with open(txtpath,'w') as txtwriter:  
    txtwriter.write(f"Total Months: {total_months} \n")
    txtwriter.write(f"Total Amount: {total_amount} \n")
    txtwriter.write(f"Average Change: {average_change}\n")
    txtwriter.write(f"Greatest Increase {maxchange}{maxdate}\n")
    txtwriter.write(f"Greatest Decrease {minchange}{mindate}\n")