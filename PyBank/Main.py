import os
csvpath=os.path.join(r'C:\Users\33017\Documents\DABootCamp\Day9\03-Python\Homework\Instructions\PyBank\raw_data','budget_data_1.csv')
import csv

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #Skip the header of CSV file
    next(csvreader)
    revenue_dic = {}    
    budget_data_dic = {}
    for row in csvreader:
        budget_data_dic[row[0]] = int(row[1])
        month, day = row[0].split('-')
        if month not in revenue_dic.keys():
            revenue_dic[month] = int(row[1])
        else:
            revenue_dic[month] = revenue_dic[month] + int(row[1])


revenues = []
for value in revenue_dic.values():
    revenues.append(value)


revenue_change = []
for i in range(len(revenues)):
    if i < len(revenues) - 1:
         revenue_change.append(revenues[i+1] - revenues[i])
average_change = sum(revenue_change)/(len(revenues)-1) 

max_revenue = max(budget_data_dic.values())
min_revenue = min(budget_data_dic.values())
for key, revenue in budget_data_dic.items():
    if revenue == max_revenue:
        max_date = key
    if revenue == min_revenue:
        min_date = key
    
fid = open('results.txt', 'w')    
fid.write("Financial Analysis\n")
fid.write("------------------------------------------------------\n")
fid.write("Total Months: " + str(len(revenue_dic.keys())) + '\n')
fid.write("Total Revenue: $" + str(sum(revenue_dic.values())) + '\n')
fid.write("Greatest increase in revenue: " + max_date + ' ($' + str(max_revenue) + ')' + '\n')
fid.write("Greatest decrease in revenue: " + min_date + ' ($' + str(min_revenue) + ')' + '\n')
fid.close()
          
print ("Financial Analysis")
print("------------------------------------------------------")
print("Total Months: " + str(len(revenue_dic.keys())))
print("Total Revenue: $" + str(sum(revenue_dic.values())))
print("Greatest increase in revenue: " + max_date + ' ($' + str(max_revenue) + ')')
print("Greatest decrease in revenue: " + min_date + ' ($' + str(min_revenue) + ')')



