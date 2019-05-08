# -*- coding: utf-8 -*-
"""
Created on Sun May  5 20:26:25 2019

@author: Kanel.Soeng
"""
"""
OOP
    -Class A
        -Property or Attribute
            example: skin_color
        -Method or Action
            +def walk(self, )
            +def sleep(self, )
            +def stand(self, )
            +def sit(self, )
        
    -Object O 
        Chenthon  = A()
            skin: black
            +walk()
            +sleep()
            +stand()
            +sit()
"""    

#blueprint
class simple():
    pass
# Instance or Object
my_class = simple() #object

type(my_class)

## 2) Create/define a class with attribute !!

class Person():
    #constructor , we call it method = function
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
#create instance object        
P1 = Person("Chenthon", 38)
P2 = Person("Kanel", 18)
P3 = Person("Veasna", 40)

#print its type as object type.
type(P1)

# Access to object properties or attribute.
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


##METHOD##

class Person():
    # Special function call it as initializer
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
        #self.area = self.pi* radius * radius
        
    def area(self):
        return pi* self.radius * self.radius
    
    
C1 = Circle(10)
C1.area


### INHERITANCE ###

# this is a base class 
class Sports():
    def __init__(self):
        print("Enjoy the game")
        
    def health(self):
        print("I am healthy")    
    def excitement(self):
        print("I am exciting")

#create an instance of class.    
my_sport = Sports()

my_sport.excitement()
my_sport.health()

#Derived or sub-class
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
my_football.excitement #from parent
my_football.health() # from parent but overidden by child
my_football.world_cup()

#INHERITANCE
    # Base class
    # Derived Class
    # Inherite method from base class or parent class in the derived class
    # Re-Write a method in the derived class
    # Create new method in derived class
    
   
#
 """ 
    class
    object
    property or attribute
    method 
    inheritance 
        base class
        sub-class or derived.
        override ~pol
        new method
        contructor or initialize.
"""