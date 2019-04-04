# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 07:03:54 2019

@author: Kanel.Soeng
"""

# Boolean's ##

True
true

False
false

type(True)
10 > 9
3 == 2

7 < 5

#example 1:
l = [1,2,3,4, -1,-3]
#control flow , if else => boolean to control the flow logic of the programs.
for i in l:
    if -3 >= 1 :
        print(i)
    else: print("none")
       


#example 2:
number = 23
guess = int(input('Enter an integer : '))

if guess == number: # is it true or false? 
    # New block starts here
    print('Congratulations, you guessed it.')
    print('(but you do not win any prizes!)')
    # New block ends here
elif guess < number:
    # Another block
    print('No, it is a little higher than that')
    # You can do whatever you want in a block ...
else:
    print('No, it is a little lower than that')
    # you must have guessed > number to reach here

print('Done')
# This last statement is always executed,
# after the if statement is executed.

#REMEMBER Write in  'True' not 'true'


