# PyBank Challenge

import os
import csv

# Import the budget data files
filepath = os.path.join("budget_data_1.csv")

# Open data files
with open(filepath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    total = 0
    next(csvreader)

    revenues = [float(row[1]) for row in csvreader]
    dates = [float(row[0]) for row in csvreader]

    # Calculate total # of months
    totalMonths = len(revenues)

    # Calculate total revenue
    sum_rev = sum(revenues)

    # Find average change in revenue
    avg_rev = sum_rev / totalMonths

    # Find greatest increase in revenue
    max_rev = max(revenues)
    
    # Get the max revenue index
    max_rev_index = revenues.index(max_rev)

    # Apply the max revenue index to the Dates column.
    # Note from Allison: I haven't figured this out yet.    
    
    # Get the greatest decrease in revenue
    min_rev = min(revenues) 

    # Get the min revenue index
    min_rev_index = revenues.index(min_rev)

    print("Financial Analysis")  
    print( "----------------------------")      
    print("Total Months: " + str(totalMonths))      
    print("Total Revenue: " + str(sum_rev))
    print("Average Revenue Change: " + str(avg_rev))    
    print("Greatest Increase in Revenue: " + str(max_rev))
    print("Greatest Decrease in Revenue: " + str(min_rev))    

    # Write results to txt file

    csvpath = os.path.join("Financial Analysis")
    with open(csvpath, "w") as txtfile:
        txtfile.write("Financial Analysis\n")
        txtfile.write("----------------------------\n")
        txtfile.write("Total Months: " + str(totalMonths)+"\n")
        txtfile.write("Total Revenue: " + str(sum_rev)+"\n")
        txtfile.write("Average Revenue Change: " + str(avg_rev)+"\n")
        txtfile.write("Greatest Increase in Revenue: " + str(max_rev)+"\n")
        txtfile.write("Greatest Decrease in Revenue: " + str(min_rev)+"\n")
    
