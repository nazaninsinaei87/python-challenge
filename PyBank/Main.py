import os
from dateutil.parser import parse
csvpath = os.path.join(r'C:\Users\33017\Desktop\LearnPython\03-Python\Homework\Instructions\PyBank\raw_data\budget_data_1.csv')
import csv

# Dictionary for lookup month
month_dic = {    1: 'Jan',
                 2: 'Feb',
                 3: 'Mar',
                 4: 'Apr',
                 5: 'May',
                 6: 'Jun',
                 7: 'Jul',
                 8: 'Aug',
                 9: 'Sep',
                 10: 'Oct',
                 11: 'Nov',
                 12: 'Dec'
                 }
# Read the csv file
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #Skip the header of CSV file
    next(csvreader)
# Dictionary to hold the date which is a combination of month and year and its total revenue  
    date_revenue_dic = {}
# Loop through each row in csv file to parse the date and get the year and month    
    for row in csvreader:
        date = parse(row[0])
        yy = date.year
        mm = date.month
        
# Looking for combination of year and month in the dictionary. 
#if it does not find the combination, it will add that combination to key and the value would be the revenue. 
#if it finds the combination, just add the value of the new row to previous values of that combination
                
        if (yy, mm) not in date_revenue_dic:
            date_revenue_dic[yy, mm] = int(row[1])
        else:
            date_revenue_dic[yy, mm] = date_revenue_dic[yy, mm] + int(row[1])
# Create a revenue list to hold all revenues    
    revenues = []
    for value in date_revenue_dic.values():
        revenues.append(value)

# Create a revenue change list which contain the revenue changes between months
    revenue_change = []
    for i in range(len(revenues)-1):
             revenue_change.append(revenues[i+1] - revenues[i])
             
# Create another dictionary to hold the month-year combination and corresponding revenue change value 
    diff_revenue_dic = {}    
    
    for index, (key, value) in enumerate(date_revenue_dic.items()):
        if index > 0:
            diff_revenue_dic[key] = revenue_change[index - 1]
    
# Finding the greatest increase and decrease by looking at max and min of values in recent dictionary
    greatest_increase = max(diff_revenue_dic.values())
    greatest_decrease = min(diff_revenue_dic.values())
    for key, value in diff_revenue_dic.items():
#Finding date corresponds to greatest increase and decrese        
        if value == greatest_increase:
            greatest_increase_date = key
            greatest_increase_date_formated = month_dic[greatest_increase_date[1]] + '-' + str(greatest_increase_date[0])
                
        if value == greatest_decrease:
            greatest_decrease_date = key
            greatest_decrease_date_formated = month_dic[greatest_decrease_date[1]] + '-' + str(greatest_decrease_date[0])
        
# Write the results to a text file  
fid = open('results_budget_data1.txt', 'w')    
fid.write("Financial Analysis\n")
fid.write("------------------------------------------------------\n")
fid.write("Total Months: " + str(len(date_revenue_dic.keys())) + '\n')
fid.write("Total Revenue: $" + str(sum(date_revenue_dic.values())) + '\n')
fid.write("Average Change: $" + str(round(sum(revenue_change)/len(revenue_change), 2)) + '\n')
fid.write("Greatest increase in revenue: " + greatest_increase_date_formated + ' ($' + str(greatest_increase) + ')' + '\n')
fid.write("Greatest decrease in revenue: " + greatest_decrease_date_formated + ' ($' + str(greatest_decrease) + ')' + '\n')
fid.close()

# Print the results          
print ("Financial Analysis")
print("------------------------------------------------------")
print("Total Months: " + str(len(date_revenue_dic.keys())))
print("Total Revenue: $" + str(sum(date_revenue_dic.values())))
print("Average Change: $" + str(round(sum(revenue_change)/len(revenue_change), 2)))
print("Greatest increase in revenue: " + greatest_increase_date_formated + ' ($' + str(greatest_increase) + ')')
print("Greatest decrease in revenue: " + greatest_decrease_date_formated + ' ($' + str(greatest_decrease) + ')')


