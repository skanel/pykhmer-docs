# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 07:04:00 2019

@author: Kanel.Soeng
"""

# 1) Range function (upper bound exlcuded)

for num in range(10):
    print(num)


for num in range(3,11):
    print(num)
    
for num in range(3,11, 2):
    print(num)

my_list = [1,2,3,4,5,6,7,8,9,10]
range(10)
list(range(10))
list(range(0,11))
list(range(1,11))

list1 = list(range(1,11)


#2) Enumurate

word ="Badman"
for item in word:
    print(item)

for item in enumerate(word):
    print(item)
    
for a, b in enumerate(word):
    print(a, b)

   
for a, b in enumerate(word):
    print(b)

for a, b in enumerate(word):
    print(a)
    print(b)
    print("\n")

#3) zip
    
list1 = [1,2,3,4,5]
list2 = ["a","b","c","d", "e"]

zip(list1, list2)

for item in zip(list1, list2):
    print(item)
    
for a, b in zip(list1, list2):
    print(a, b)

for a, b in zip(list1, list2):
    print(a)
    
for a, b in zip(list1, list2):
    print(b)
    
list1 = [1,2,3,4,5]
list2 = ["a","b","c","d", "e"]
lst3 = ["a", "b", "d"]

for item in zip(list1, list2. list3):
    print(item)
list1 = [1,2,3,4,5]
list2 = ["a","b","c","d", "e"]
lst3 = ["a", "b", "d"]

for a,b,c in zip(list1, list2. list3):
    print(a,b,c)

# 4) in
"a"in [2,3,4]
"a" in [2,3,4, "a"]

"s"in "school"

"s"in "School"

"k1" in {"k1":100 , "k2": 200, "k3":300}

d = {"k1":100 , "k2": 200, "k3":300}
100 in d.keys()
100 in d.values()

#5 List comprehensions in python

my_string = "Spartans"
for letter in my_string:
    print(letter)

my_list = []
for letter in my_string:
    my_list.append(letter)
    
my_list


my_list = [letter for letter in my_string]
#for letter in my_string:
   # my_list.append(letter
my_list

list1 = [asdf for asdf in range(10)]
list1


# commonly used Built-in function in python
# 1) Range function
# 2) Enumerate
# 3) zip
# 4) in

# list comprehensions in python