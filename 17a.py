"""
Make a calculator
add
sub
mul
div

enter number 1 (input)
enter number 2 (input)
what do you want to do (input)
"""

def my_add(num1,num2):
	return num1 + num2

def my_sub(num1,num2):
	return num1 - num2

def my_mul(num1,num2):
	return num1 * num2

def my_div(num1,num2):
	return num1 / num2

n1, n2 = 2, 5
a = 'sub'

actions = {
	'add':my_add,
	'sub':my_sub,
	'mul':my_mul,
	'div':my_div
}

print(actions[a](n1,n2))