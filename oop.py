# -*- coding: utf-8 -*-
"""
Created on Sun May  5 20:26:25 2019

@author: Kanel.Soeng
"""

class simple():
    pass

my_class = simple() #object

type(my_class)

## 2) Create a class with attribute !!

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
P1 = Person("Chan", 38)
type(P1)

P1.name
P1.age

## 3) Create a class with attribute !!

class Person():
    
    eyes = "Blue" #class  Attribute
    
     # Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
P1 = Person("Chan", 38)
P1.eyes


##METHOD##

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def my_function(self, number):
        print("I am {} and ID is {}".format(self.name, number))
        
#create object now
        
P1 = Person("Maria", 28)
P1.age
P1.name

P1.my_function(99)


class Circle():
    pi = 3.14
    
    def __init__(self, radius):
        self.radius = radius
        self.area = self.pi* radius * radius
        
    def Circum(self):
        return 2 * self.pi * self.radius
    
    
C1 = Circle(10)
C1.area
C1.pi
C1.radius
C1.Circum()

### INHERITANCE ###

# this is a base class 
class Sports():
    def __init__(self):
        print("Enjoy the game")
    def health(self):
        print("I am healthy")    
    def excitement(self):
        print("I am exciting")
    
my_sport = Sports()

my_sport.excitement()
my_sport.health()

#Derivedclass
class Football(Sports):
    def __init__(self):
        Sports.__init__(self)
        print("I am football")
    # Re-write / Override a method in derived class
    def health(self):
        print("Playing footbal is good for health") 
    #create new method in the derived class
    def world_cup(self):
        print("Every four years")

my_football = Football()
my_football.excitement()
my_football.health()
my_football.world_cup()

# Base class
# Derived Class
# Inherite method from base class or parent class in the derived class
# Re-Write a method in the derived class
# Create new method in derived class