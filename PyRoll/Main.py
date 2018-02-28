# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 12:06:35 2018

@author: 33017
"""

import os
import csv
csvpath = os.path.join(r'C:\Users\33017\Documents\DABootCamp\Day9\03-Python\Homework\Instructions\PyPoll\raw_data','election_data_1.csv')

with open(csvpath, 'r', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    vote = {}    
    for row in csvreader:
        
        if row[2] not in vote.keys():
            vote[row[2]] = 1
        else:
            vote[row[2]] = vote[row[2]] + 1
total_vote = sum(vote.values())


print("Election Results")
fid = open('Vote_results.txt','w')
fid.write("Election Results\n")

print("----------------------------------------------")
fid.write("----------------------------------------------\n")
print("Total Votes: " + str(total_vote))
fid.write("Total Votes: " + str(total_vote) + '\n') 
print("----------------------------------------------")
fid.write("----------------------------------------------\n")
max_vote = max(vote.values())
for key, value in vote.items():
    percent_vote = round ((value/total_vote)*100,0)
    print(key + ": " + str(percent_vote) + "% " + "(" + str(value) + ")")
    fid.write(key + ": " + str(percent_vote) + "% " + "(" + str(value) + ")" + '\n') 
    if value == max_vote:
        winner = key
print("----------------------------------------------")
fid.write("----------------------------------------------\n")
print("Winner: " + winner)
fid.write("Winner: " + winner + '\n') 
fid.close