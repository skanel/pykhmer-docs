# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 07:25:17 2019

@author: Kanel.Soeng
"""

## File Handling

# Read file from a default folder
my_file = open("E:\\DOCUMENT\\Lecture\\pykhmer-docs\\sample_file.txt")

my_file.read()

my_file.read()

my_file.seek(2) # set cursor to position 2
my_file.read() # read by start from position2
my_file.seek(0) # set cursor to position 0

# To Read a line
my_file.readline()
my_file.seek(0)

# store a file data into a variable

new_file = my_file.read()
new_file

# To Find the current directory
pwd


# after read / write REMEMBER TO Close the file

my_file.close()


## What we have learn

# 1) Read file from the a default folder
# 2) Store file data into a variable
# 3) Find the current directory
# 4) Read a file from anywhere in the computer
# 5) Close the file

# READ ALL LINES IN THE FILE, is to loop over it line by line
with open('E:\\DOCUMENT\\Lecture\\pykhmer-docs\\sample_file.txt') as f:
    lines = f.readlines(1) #= f.readline() no 's'
    
    print(lines)
    