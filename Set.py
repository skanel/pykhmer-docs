# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 06:59:06 2019

@author: Kanel.Soeng
"""
#set: Unorderd collection of unique and immutable objects
#in sets if we enter same object multiple times then it will take only one.
my_set = set()
my_set

my_set.add("Hello")
my_set
my_set.add(24)
my_set
my_set.add("Hello")
my_set

my_list = [1,1,1,2,3,4, "Apple", "Apple"]
my_list
set(my_list)
s = {1,2}

# UNION 2 SETS
setx = set(["apple", "mango"])
sety = set(["mango", "orange"])
setz = setx & sety
print(setz)

#INTERSECTION 2 SETS (to find a Set difference)
setb = setx - setz
print(setb)


# Other way to create set
my_set  = { 1,3,4,5}

#Remember to create a set you need to have a collection, example : list or tuple then you use set([2,3,1])





