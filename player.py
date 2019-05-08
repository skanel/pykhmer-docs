# -*- coding: utf-8 -*-
"""
Created on Sun May  5 21:43:26 2019

@author: Kanel.Soeng
"""

class Player:
     
    # Biến của lớp. 
    minAge  = 18
     
    maxAge = 50
     
     
    def __init__(self, name, age):
         
        self.name = name
        self.age = age