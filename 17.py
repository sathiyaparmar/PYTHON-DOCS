"""
Functions
"""

"""
make a function that takes 2 numbers as arguments and returns sum of them
"""

# What are positional arguments?

# in function arguments, in different languages
	# pass by value (does not exist in python)
	# pass by reference

myList = []

def some_func(someList):
	someList.append(1)


some_func(myList)
some_func(myList)

print(myList)