# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 20:29:15 2018

@author: 33017
"""

#import re
textpath = r'C:\Users\33017\Documents\DABootCamp\Day9\03-Python\Homework\Instructions\PyParagraph\raw_data\paragraph_1.txt'
paragraph = open(textpath, 'r')
#re.split("(?&lt;=[.!?]) +", paragraph)
for line in paragraph:
    sentence = line.split('. ')
for w in sentence:
    word = line.split(' ')
print("Approximate Word Count: " + str(len(word)))
print("Approximate Sentence Count: " + str(len(sentence)))  
letter_length = []  
for letter in word:
    letter_length.append(len(letter))
print("Average Letter Count: " + str(sum(letter_length)/len(letter_length))) 
print("Average Sentence Length: " + str (len(word)/len(sentence)))
