# PyBoss Challenge

import os
import csv
import datetime

# Import the employee_data1.csv and employee_data2.csv

filepath = os.path.join("/Users/avangemert/Downloads/employee_data1.csv")

converted_employee_data = []

# Read data into dictionary

with open(filepath) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        emp_id = row["Emp ID"]
        name = row["Name"]
        dob = row["DOB"]
        ssn = row["SSN"]
        state = row["State"]
       
       # The Name column should be split into separate First Name and Last Name columns.
        first_name = name.split()[0]
        last_name = name.split()[1]
       
       # The DOB should be reformatted as MM/DD/YYYY
        dob_mdy = datetime.datetime.strptime(dob, '%Y-%m-%d').strftime('%m/%d/%y')

        # The SSN should only show the last four digits.
        ssn_mask = ssn[-4:].rjust(len(ssn), "*")
        

        
             
        
        
