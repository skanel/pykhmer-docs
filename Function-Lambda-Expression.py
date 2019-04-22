#Python has many built-in 
#function like print(), range()
#min(), max()

#We can also create our own function in python
#These function are called as user-defined function

#it avoid repetition of the code and makes it re-usable

#A function is a block of code organized and reusable 
#code that perform a specific task.

#A function run only when we call a function

#A function can return data as a result when it is required.

def my_function():
    print("Hello")
    
    
my_function
my_function()

help(my_function)

def my_function():
	"""
	Create by: Kanel
	Input: No
	Output: Hello
	
	"""
	
	print("Hello")

my_function()
help(my_function)


def greeting():
	print("Good Morning")
	
greeting()

# How to give an argument in the function

def greeting(name):
	print("Good Evening " + name)
greeting("Sok")
greeting("Sao")


def greeting(name="Sao"):
	print("Good Evening" + name)
greeting()

my_vaiable = greeting("Sok")
my_vaiable
type(my_vaiable)


#store data into a variable with "return"

def greeting(name = "Makara"):
	return "Hello " + name

greeting()
a = greeting("Chan")
a
type(a)

# defined a function for additional of two numbers
def  add(n1, n2):
	return n1+n2

add(70,30)
b = add(70,30)
b

# Q: Print the even numbers from the given list

def even_number(l):
	"""
	It's a function to print even number's 
	input: A list with number 
	output: A list with even numbers
	"""
	enum = []
	for n in l:
		if n in l:
			if n% 2 == 0:
				enum.append(n)
	return(enum)
	
even_number([1,2,3,4,5,6,7,8,9]

## Function
# 1) How to defined a function?
# 2) How to add the doc string in a function
# 3) How to give an argument in the function?
# 4) Use of the keyword "return".

# 5) Function for addition of two numbers.s
# 6) Function to return even number from a given list.