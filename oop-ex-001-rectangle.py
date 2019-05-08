# -*- coding: utf-8 -*-
"""
Created on Sun May  5 21:36:16 2019

@author: Kanel.Soeng
"""

# Một lớp mô phỏng một hình chữ nhật.
class Rectangle :
    'This is Rectangle class'
    
    # Một phương thức được sử dụng để tạo đối tượng (Contructor).
    def __init__(self, width, height):
         
        self.width= width
        self.height = height
    
     
     
    def getWidth(self):        
        return self.width
     
     
    def getHeight(self):        
        return self.height
 
    # Phương thức tính diện tích.
    def getArea(self):
         
        return self.width * self.height