import os
from dateutil.parser import parse
csvpath = os.path.join(r'C:\Users\33017\Desktop\LearnPython\03-Python\Homework\Instructions\PyBank\raw_data\budget_data_2.csv')
import csv

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

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #Skip the header of CSV file
    next(csvreader)
    
    date_revenue_dic = {}
    
    for row in csvreader:
        date = parse(row[0])
        yy = date.year
        mm = date.month
                
        if (yy, mm) not in date_revenue_dic:
            date_revenue_dic[yy, mm] = int(row[1])
        else:
            date_revenue_dic[yy, mm] = date_revenue_dic[yy, mm] + int(row[1])
    
    revenues = []
    for value in date_revenue_dic.values():
        revenues.append(value)


    revenue_change = []
    for i in range(len(revenues)-1):
             revenue_change.append(revenues[i+1] - revenues[i])
 
    diff_revenue_dic = {}    
    
    for index, (key, value) in enumerate(date_revenue_dic.items()):
        if index > 0:
            diff_revenue_dic[key] = revenue_change[index - 1]
    

    greatest_increase  = min(diff_revenue_dic.values())
    greatest_decrease = max(diff_revenue_dic.values())
    for key, value in diff_revenue_dic.items():
        
        if value > greatest_increase:
            greatest_increase = value
            greatest_increase_date = key
            greatest_increase_date_formated = month_dic[greatest_increase_date[1]] + '-' + str(greatest_increase_date[0])
                
        if value < greatest_decrease:
            greatest_decrease = value
            greatest_decrease_date = key
            greatest_decrease_date_formated = month_dic[greatest_decrease_date[1]] + '-' + str(greatest_decrease_date[0])
        



    
fid = open('results_budget_data1.txt', 'w')    
fid.write("Financial Analysis\n")
fid.write("------------------------------------------------------\n")
fid.write("Total Months: " + str(len(date_revenue_dic.keys())) + '\n')
fid.write("Total Revenue: $" + str(sum(date_revenue_dic.values())) + '\n')
fid.write("Average Change: $" + str(round(sum(revenue_change)/len(revenue_change), 2)) + '\n')
fid.write("Greatest increase in revenue: " + greatest_increase_date_formated + ' ($' + str(greatest_increase) + ')' + '\n')
fid.write("Greatest decrease in revenue: " + greatest_decrease_date_formated + ' ($' + str(greatest_decrease) + ')' + '\n')
fid.close()
          
print ("Financial Analysis")
print("------------------------------------------------------")
print("Total Months: " + str(len(date_revenue_dic.keys())))
print("Total Revenue: $" + str(sum(date_revenue_dic.values())))
print("Average Change: $" + str(round(sum(revenue_change)/len(revenue_change), 2)))
print("Greatest increase in revenue: " + greatest_increase_date_formated + ' ($' + str(greatest_increase) + ')')
print("Greatest decrease in revenue: " + greatest_decrease_date_formated + ' ($' + str(greatest_decrease) + ')')


