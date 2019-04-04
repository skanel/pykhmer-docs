# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 19:35:23 2019

@author: Kanel.Soeng
"""

# Python program to print Even Numbers in a List 
  
# list of numbers 
list1 = [10, 21, 4, 45, 66, 93] 
  
# iterating each number in list 
for num in list1: 
      
    # checking condition 
    if num % 2 == 0: 
       print(num, end = " ") 
       
# Python program to print Even Numbers in a List 
  
# list of numbers 
list1 = [10, 21, 4, 45, 66, 93] 
num = 0
  
# using while loop         
while(num < len(list1)): 
      
    # checking condition 
    if num % 2 == 0: 
       print(list1[num], end = " ") 
      
    # increment num   
    num += 1

# Python program to print even Numbers in a List 
  
# list of numbers 
list1 = [10, 21, 4, 45, 66, 93] 
  
# using list comprehension 
even_nos = [num for num in list1 if num % 2 == 0] 
  
print("Even numbers in the list: ", even_nos) 

# Python program to print Even Numbers in a List 
  
# list of numbers  
list1 = [10, 21, 4, 45, 66, 93, 11]  
  
  
# we can also print even no's using lambda exp.  
even_nos = list(filter(lambda x: (x % 2 == 0), list1)) 
  
print("Even numbers in the list: ", even_nos)  