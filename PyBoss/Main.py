# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 17:52:16 2018

@author: 33017
"""

import os
import csv
import datetime
us_state_abbrev = {
    'Alabama': 'AL','Alaska': 'AK','Arizona': 'AZ','Arkansas': 'AR','California': 'CA','Colorado': 'CO',
    'Connecticut': 'CT','Delaware': 'DE','Florida': 'FL','Georgia': 'GA','Hawaii': 'HI','Idaho': 'ID',
    'Illinois': 'IL','Indiana': 'IN','Iowa': 'IA','Kansas': 'KS','Kentucky': 'KY',
    'Louisiana': 'LA','Maine': 'ME','Maryland': 'MD','Massachusetts': 'MA','Michigan': 'MI',
    'Minnesota': 'MN','Mississippi': 'MS','Missouri': 'MO','Montana': 'MT','Nebraska': 'NE',
    'Nevada': 'NV','New Hampshire': 'NH','New Jersey': 'NJ','New Mexico': 'NM','New York': 'NY',
    'North Carolina': 'NC','North Dakota': 'ND','Ohio': 'OH','Oklahoma': 'OK','Oregon': 'OR',
    'Pennsylvania': 'PA','Rhode Island': 'RI','South Carolina': 'SC','South Dakota': 'SD',
    'Tennessee': 'TN','Texas': 'TX','Utah': 'UT','Vermont': 'VT','Virginia': 'VA','Washington': 'WA',
    'West Virginia': 'WV','Wisconsin': 'WI','Wyoming': 'WY'}
csvpath = os.path.join(r'C:\Users\33017\Documents\DABootCamp\Day9\03-Python\Homework\Instructions\PyBoss\raw_data','employee_data1.csv')
newEmployeeCSV = os.path.join(r'C:\Users\33017\Documents\DABootCamp\Week3-HW\python-challenge\PyBoss', 'newemployee.csv')
with open(csvpath,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    
    Emp_ID = []
    first_name = []
    last_name = []
    DOB = []
    SSN =[]
    State = []

    for row in csvreader:
         Emp_ID.append(row[0])
         first, last = row[1].split(' ')
         first_name.append(first)
         last_name.append(last)
         new_date = datetime.datetime.strptime(row[2], '%Y-%m-%d').strftime('%m/%d/%y')
         DOB.append(new_date)
         first_ssn, mid_ssn, last_ssn = row[3].split('-')
         new_ssn = '***-**-' + last_ssn
         SSN.append(new_ssn)
         for key, value in us_state_abbrev.items():
             if row[4] == key:
                 State.append(value)
               
cleanCSV = zip(Emp_ID, first_name, last_name, DOB, SSN, State)
with open(newEmployeeCSV, 'w', newline="") as csvFile:

        csvWriter = csv.writer(csvFile, delimiter=',')
        csvWriter.writerow(["Emp ID","First Name","Last Name","DOB","SSN", "State"])
        csvWriter.writerows(cleanCSV)      
         
         
    