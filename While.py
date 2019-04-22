# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 06:55:40 2019

@author: Kanel.Soeng
"""

i = 0
while i < 5:
    print(i)
    i =  i+1
    
i = 0
while i < 5:
    print(i)
    i =  i+1
else:
    print("i is not less than 5")

#Pass, Break and Continue
    
l = [1,2,3,4,5]

for item in l:
    #comment
    pass
print("I will work after !!!")


my_string = "Hello World"
for letter in my_string:
    if letter =="r":
        break #exit from loop
    print(letter)
    
my_string = "Hello World"
for letter in my_string:
    if letter == "e":
        continue
    print(letter)
    
i = 0
while i < 5:
    if i == 3:
        break;
    print(i)
    i  = i +1