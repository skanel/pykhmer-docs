# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 18:34:37 2019

@author: Kanel.Soeng

"""

#function not return a value

def say_hi():
    print("Say hi 2")
    print("Say hi 3")
say_hi()

def return_val():
    return 100
n = return_val()
print(n)

#f(X)  = x2+2x+1
def fn(x):
    return x**2 + 2*x +1 
result = fn(10)
print(result)


def add2numbers(a, b):
        b = 100*2 
        #More code here
        
        return a+b

#call a function
result = add2numbers(100, 200)
print(result)


"""
Exercise

Write a function called showNumbers that takes a parameter called limit.
 It should print all the numbers between 0 and limit with a label to identify the even and odd numbers.
 For example, if the limit is 3, it should print:
0 EVEN
1 ODD
2 EVEN
3 ODD
"""
#Declare a function
def showNumbers(limit):
    coll_1 = {}
    for item in range(limit+1):
        if int(item) % 2 == 0:
            num = item
            type = "EVEN"
            coll_1.update({num: type})
        # num = "EVEN"
        else:
            num = item
            type = "ODD"
            coll_1.update({num:type})
    return coll_1


limit = int(input("input your limit number: "))
#Call this function
type = showNumbers(limit)
print(type)

"""
Write a function that returns the sum of multiples of 3 and 5 between 0 and limit (parameter).
 For example, if limit is 20, it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18, 20.
"""

def sum_multiples(limit=20):
    l = []
    limit+=1
    for i in range(limit):
        if(i%3 == 0 or i%5 == 0):
            l.append(i)
    print(l)

sum_multiples()



#Example: How to sort the list of tuple

from operator import itemgetter
inventory = [('apple', 5), ('apple', 3), ('banana', 2), ('pear', 5), ('orange', 1), ('apple', 1)]
sorted(inventory, key= itemgetter(0,1) )




"""
Question:
You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string, age and height are numbers. The tuples are input by console. The sort criteria is:
    1: Sort based on name;
    2: Then sort based on age;
    3: Then sort by score.
The priority is that name > age > score.

If the following tuples are given as input to the program:
INPUT:
    Tom,19,80
    John,20,90
    Jony,17,91
    Jony,18,93
    Json,21,85

Then, the output of the program should be:
[
 ('John', '20', '90'),
 ('Jony', '17', '91'),
 ('Jony', '18', '93'), 
 ('Json', '21', '85'), 
 ('Tom', '19', '80')
 ]
"""


#SOLUTION

#import the third-party library
from operator import itemgetter

#Create empty list
persons = []

#Loop forever, till user input nothing.
while True:
	line = input("input the tuple: ")
	if not line:
		break #Exit from loop if user nothing input
	persons.append(tuple(line.split(','))) #split string kanel,23,60 into (kanel,23,60)

persons = sorted(persons, key=itemgetter(0, 1, 2)) #sort the list of tuple by name>age,score

print(persons)
#loop over and printer the result
for person in persons:
    print (','.join(person))
