# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 19:03:48 2019

@author: Kanel.Soeng
"""

from math import sqrt

print("ស្រាយ​សមីការដឹក្រេទី 2: ax^2 + bx + c = 0")
a = float(input("បញ្ចូល a: "))
b = float(input("បញ្ចូល b: "))
c = float(input("បញ្ចូល c: "))

if a == 0:
    if b == 0:
        if c == 0:
            print("​សមីការមាន​ឬសច្រើន​រាប់​មិនអស់!")
        else:
            print("​សមីការគ្មានឬស!")
    else:
        if c == 0:
            print("​សមីការមាន​ឬស x = 0")
        else:
            print("​សមីការមាន​ឬស មួយ x = ", -c / b)
else:
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print("សមីការគ្មានឬស!")
    elif delta == 0:
        print("សមីការមាន​ឬស មួយ x = ", -b / (2 * a))
    else:
        print("សមីការមាន​ឬស មួយ ពីរ​ផ្សេងគ្នា")
        print("x1 = ", float((-b - sqrt(delta)) / (2 * a)))
print("x2 = ", float((-b + sqrt(delta)) / (2 * a)))