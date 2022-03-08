"""
List 
Dict
Tuple
Set
"""

"""
Use of list?
- to store more than one element
- It basically wraps the data
- If I want add data or remove
- Values can be updated

Use of Tuple?
- For constants
- For security 

- It can be empty
- Once made, elements can not be updated
	- No of elements in a tuple can not be changed
	- Type of each elements at the beginning can not be changed
	- Insider objects can be updated
"""

x = [i+1 for i in range(10)]
print(tuple(x))