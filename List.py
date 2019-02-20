# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 22:49:16 2019

@author: Kanel.Soeng
"""

# List can contain all data types string, int,float
# 1) concatenation 
# 2) Define empty list
# 3) Indexing in list
# 4) Editing the list's
# 5) Remove from the list
# 6) Add list into list
# 7) Python in-build functions with the list's 

my_list = ["Hello", 100, 23.47]
print(my_list)

second_list = ["one","two","three"]
print(second_list)

print(my_list, second_list)


# 1) concatenation 
new_list = my_list + second_list
print(new_list)

# 2) Define empty list
empty_list =[] 
print(empty_list)


# 3) Indexing in list or sclicings
#           [0,          1,       2,         3]
students = ["Thon","Veasna", "sokkhun","kanel"]
#          [-4,     -3,       -2,           -1]
print(students)
students[0]
students[2:1]
students[-3:-2]
students[0:3] # exlcude upper bone

# 4) Editing the list's
students[0] = "sereyvong"
students

# 5) Add list into list
students.append("thira")
students

# 5) Remove value
students.remove("veasna")
students

list1 = ["one", "two", "three", "four", "five"]
list1
list1.pop()

list1.pop(0)
list1

color = ["Red","Green", "Blue", "Violet"]
color
age = [21,32,34,45]

color.extend(age)
color

# 7) Python in-build functions with the list's

even = [2, 4, 6, 8]
odd = [1, 3, 5 , 7, 9,2]

numbers = even + odd
numbers

print(sorted(numbers))
sorted_number = sorted(numbers)

len(numbers) #number of items in the list

max(numbers) #maximum number in the list
min(numbers) 

# WHAT WE HAVE LEARN
# 1) concatenation 
# 2) Define empty list
# 3) Indexing in list
# 4) Editing the list's
# 5) Remove from the list
# 6) Add list into list
# 7) Python in-build functions with the list's 


#EXERCISE write the following python script in pycharm and explain the output
# 1. ex_list_01.py
Rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
print(Rainbow[0])
Rainbow[0] = 'red'
print('Print the rainbow')
for i in range(len(Rainbow)):
    print(Rainbow[i])

# 2.ex_list_02.py
a = [] # start an empty list
n = int(input("Please input n: ")) # read number of element in the list
for i in range(n): 
    new_element = int(input("Please put new element: ")) # read next element
    a.append(new_element) # add it to the list
    # the last two lines could be replaced by one:
    # a.append(int(input()))
print(a)

# 3. ex_list_03.py
a = []
for i in range(int(input())):
    a.append(int(input()))
print(a)