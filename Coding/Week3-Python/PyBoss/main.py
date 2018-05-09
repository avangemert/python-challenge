# PyBoss Challenge

import os
import csv
import datetime

# Create function to import all csv files.

def PyBoss (PyBosscsvpath):

    converted_employee_data = []

    # Read data into dictionary

    with open(PyBosscsvpath) as csvfile:
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

            # Reference US state abbreviations dictionary.
            us_state_abbrev = {
                'Alabama': 'AL',
                'Alaska': 'AK',
                'Arizona': 'AZ',
                'Arkansas': 'AR',
                'California': 'CA',
                'Colorado': 'CO',
                'Connecticut': 'CT',
                'Delaware': 'DE',
                'Florida': 'FL',
                'Georgia': 'GA',
                'Hawaii': 'HI',
                'Idaho': 'ID',
                'Illinois': 'IL',
                'Indiana': 'IN',
                'Iowa': 'IA',
                'Kansas': 'KS',
                'Kentucky': 'KY',
                'Louisiana': 'LA',
                'Maine': 'ME',
                'Maryland': 'MD',
                'Massachusetts': 'MA',
                'Michigan': 'MI',
                'Minnesota': 'MN',
                'Mississippi': 'MS',
                'Missouri': 'MO',
                'Montana': 'MT',
                'Nebraska': 'NE',
                'Nevada': 'NV',
                'New Hampshire': 'NH',
                'New Jersey': 'NJ',
                'New Mexico': 'NM',
                'New York': 'NY',
                'North Carolina': 'NC',
                'North Dakota': 'ND',
                'Ohio': 'OH',
                'Oklahoma': 'OK',
                'Oregon': 'OR',
                'Pennsylvania': 'PA',
                'Rhode Island': 'RI',
                'South Carolina': 'SC',
                'South Dakota': 'SD',
                'Tennessee': 'TN',
                'Texas': 'TX',
                'Utah': 'UT',
                'Vermont': 'VT',
                'Virginia': 'VA',
                'Washington': 'WA',
                'West Virginia': 'WV',
                'Wisconsin': 'WI',
                'Wyoming': 'WY',
            }    

            # The state data should be rewritten as a two-letter abbreviation.
            state_abbrev = [us_state_abbrev[state]]

            # Append data to converted_employee_data field
            converted_employee_data.append(
                    {
                        "emp_id": emp_id,
                        "first_name": first_name,
                        "last_name" : last_name,
                        "dob_mdy": dob_mdy,
                        "ssn_mask": ssn_mask,
                        "us_state_abbrev": state_abbrev   
                    }
            )


            # Grab the filename from the original path
            _, filename = os.path.split(PyBosscsvpath)  

            # Write updated data to csv file
            csvpath = os.path.join("output", filename)
            with open(csvpath, "w") as csvfile:
                fieldnames = ["emp_id", "first_name", "last_name", "dob_mdy", "ssn_mask", "us_state_abbrev"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(converted_employee_data)

#find and join the path (choose one of the data sets)
PyBosscsvpath = os.path.join("employee_data1.csv")
PyBosscsvpath2 = os.path.join("employee_data2.csv")

PyBoss(PyBosscsvpath)
PyBoss(PyBosscsvpath2)
                
            
            
