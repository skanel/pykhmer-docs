# -*- coding: utf-8 -*-
"""
Created on Sun May  5 21:44:28 2019

@author: Kanel.Soeng
"""

from player import Player 
 
 
player1 = Player("Tom", 20)
 
player2 = Player("Jerry", 20)
 
print ("player1.name = ", player1.name)
print ("player1.age = ", player1.age)
 
 
print ("player2.name = ", player2.name)
print ("player2.age = ", player2.age)
 
print (" ------------ ")
 
print ("Assign new value to player1.age = 21 ")
 
# Gán giá trị mới cho thuộc tính (attribute) age của player1.
player1.age = 21
 
print ("player1.name = ", player1.name)
print ("player1.age = ", player1.age)
 
print ("player2.name = ", player2.name)
print ("player2.age = ", player2.age)