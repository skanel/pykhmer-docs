# -*- coding: utf-8 -*-
"""
Created on Sun May  5 21:39:59 2019

@author: Kanel.Soeng
"""

from person import Person
 
# Tạo một đối tượng Person.
aimee = Person("Aimee", 21, "Female")
 
 
aimee.showInfo()
 
print (" --------------- ")
 
# age, gender mặc định.
alice = Person( "Alice" )
 
alice.showInfo()
 
print (" --------------- ")
 
# gender mặc định.
tran = Person("Tran", 37)
 
tran.showInfo()