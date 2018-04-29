# PyBoss Challenge

import os
import csv

# Import the employee_data1.csv and employee_data2.csv

filepath = os.path.join("PyBoss", "employee_data1.csv")

# Read data into dictionary

with open(filepath) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        emp_id = row["Emp ID"]
        name = row["Name"]
        dob = row["DOB"]
        ssn = row["SSN"]
        state = row["State"]