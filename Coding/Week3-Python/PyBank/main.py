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

    revenues = [int(row[1]) for row in csvreader]
    dates = [int(row[0]) for row in csvreader]

    # Calculate total # of months
    totalMonths = len(revenues)

    # Calculate total revenue
    sum_rev = sum(revenues)
    
    # Determine change from month to month
    rev_change = []
    
    for i in range(len(revenues)-1):
        rev_change.append(revenues[i+1] - revenues[i]) 
        
    # Determine Average Revenue Change
    tot_rev_change = sum(rev_change) 
    avg_rev_change = tot_rev_change / (totalMonths - 1)
    
    # Determine greatest revenue increase
    max_rev_change = max(rev_change)

    # Determine month of greatest revenue increase
    index_max_month = rev_change.index(max_rev_change)
   
    # Below, I apply the logic of apply the index of 39 to the dates. Unfortunately, I got an IndexError.
    # max_month = dates[index_max_month]


    # Determine greatest revenue decrease
    min_rev_change = min(rev_change)

    # Determine month of greatest revenue decrease
    index_min_month = rev_change.index(min_rev_change)
    
    # min_month = dates[index_min_month]
    
    print("Financial Analysis")  
    print( "----------------------------")      
    print("Total Months: " + str(totalMonths))      
    print("Total Revenue: $" + str(sum_rev))   
    print("Average Revenue Change: $" + str(avg_rev_change))    
    print("Greatest Increase in Revenue: $" + str(max_rev_change))
    print("Greatest Decrease in Revenue: $" + str(min_rev_change))    

    # Write results to txt file
    f = open("Financial Analysis.txt", "w")
    print >>f,("Financial Analysis")  
    print >>f,( "----------------------------")      
    print >>f,("Total Months: " + str(totalMonths))      
    print >>f,("Total Revenue: " + str(sum_rev))
    print >>f,("Average Revenue Change: " + str(avg_rev_change))    
    print >>f,("Greatest Increase in Revenue: " + str(max_rev_change))
    print >>f,("Greatest Decrease in Revenue: " + str(min_rev_change))

    f.close()

    
