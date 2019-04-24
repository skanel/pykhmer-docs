# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 18:34:37 2019

@author: Kanel.Soeng
"""
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
type = showNumbers(limit)
print(type)

