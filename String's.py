# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 21:56:22 2019

@author: Kanel.Soeng
"""


## String's ##

# 1) concatenate of the string's 
greeting = "Hello"
name = "Kanel"
print(greeting + name)
print(greeting + " "+ name)

# 2) input function
greeting = "Hello"
name = input("What is your sweet name ?")
print(greeting + " "+ name)

# 3) Split of the strings
split_string = "Hello everyone, welcome to the world of python !!!"
print(split_string)

split_string = "Hello everyone, \nwelcome to the world of python !!!"
print(split_string)

tab_string = "1\t2\t3\t4"
print(tab_string)





# 4) Indexing

color = "Oragne"  #0, r, a
len(color)
print(color[3])
print(color[0])
print(color[-1])# [-1]

print(color[0:3]) # upper bound excluded
print(color[0:4])# [star_index:end_index]

print(color[-3:-1]) #upper bound exclude
# [-3:-2]

print(color[ :4])
print(color[:4])# [:end_index]
print(color[2:]) # [star_index:end_index]
print(color[0:])
print(color)
print(color[-6:])

# 5) String Formating

age = 27 #change to str(27)
print("I am " + age + " Year's old")

age = 27 #change to str(27)
print("I am " + str(age) + " Year's old")

print("The colors are {} {} {} ".format("Red","Green","Blue"))

print("The colors are {0} {1} {2} ".format("Red","Green","Blue"))

print("The colors are {0} {0} {0} ".format("Red","Green","Blue"))


print("The colors are {2} {2} {2} ".format("Red","Green","Blue"))


print("The colors are {r} {g} {b} ".format(r="Red",g="Green",b="Blue"))
print("The colors are {r} {r} {r} ".format(r="Red",g="Green",b="Blue"))

pie = 3.14
print(pie)
print("The value of pie is {} ".format(pie))
print('>_< ' * 8)
# WHAT WE HAVE LEARN
# 1) concatenate of the string
# 2) Input function
# 3) Spliting of the string's (more advance)
# 4) Indexing [head:tail]
# 5) String formating


