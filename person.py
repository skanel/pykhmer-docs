# -*- coding: utf-8 -*-
"""
Created on Sun May  5 21:39:42 2019

@author: Kanel.Soeng
"""

class Person :
   
    # Tham số age và gender có giá trị mặc định.
    def __init__ (self, name, age = 1, gender = "Male" ):
         
        self.name = name
        self.age = age 
        self.gender= gender
         
     
    def showInfo(self):
         
        print ("Name: ", self.name)
        print ("Age: ", self.age)
        print ("Gender: ", self.gender)
    
p1 = Person("kanel", 12)
p1.showInfo()