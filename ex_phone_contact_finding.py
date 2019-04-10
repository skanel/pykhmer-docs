# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 18:43:34 2019

@author: Kanel.Soeng
"""


#Solution 1
file = open("E:\\DOCUMENT\\Lecture\\pykhmer-docs\\phonebook.txt")
d = {}
with file as f:
    list_of_lines = f.readlines() # return as a list  [a,b,c,d]

    if(len(list_of_lines) > 0):
        for line in list_of_lines:
            contact = line.split(": ") #['Mr.Q','081555317']
            d[contact[0]] = contact[1]
    else:
        print("file is empty")
        
#print(d["Mr.Z"])

for (key, value) in d.items():
    print(f"{key} {value}")
    
#Solution 2    
d = {}
for line in open("E:\\DOCUMENT\\Lecture\\pykhmer-docs\\phonebook.txt"):
    contact = line.split(": ") #['Mr.Q','081555317']
    d[contact[0]] = contact[1]

    