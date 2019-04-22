# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 21:27:45 2019

@author: Kanel.Soeng
"""

if 3 > 2:
    print("Right)
    
if 4 > 7:
    print("Right)
else:
    print("Wrong")

a = 3
b = 5
if a > b:
    print("Yes, It is right!!")
else:
    print("Try again")

drink = "beer"

if drink == "Coffee":
    print("We need some coffee")
else:
    print("We need to drink beer")

drink = "Coke"

if drink == "Coffee":
    print("We need some coffee")
elif drink == "Water":
    print("We need to drink water")
elif drink == "Coke":
    print("We need to dink coke")
else: 
    print("We need to drink")