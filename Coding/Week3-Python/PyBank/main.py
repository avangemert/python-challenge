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
    f = open("Financial Analysis.txt", "w")
    print >>f,("Financial Analysis")  
    print >>f,( "----------------------------")      
    print >>f,("Total Months: " + str(totalMonths))      
    print >>f,("Total Revenue: " + str(sum_rev))
    print >>f,("Average Revenue Change: " + str(avg_rev))    
    print >>f,("Greatest Increase in Revenue: " + str(max_rev))
    print >>f,("Greatest Decrease in Revenue: " + str(min_rev))

    f.close()

    
