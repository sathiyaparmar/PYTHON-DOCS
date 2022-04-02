"""
make a function called switch
that takes status as argument
if status is true then return false and if false then return true
basically flips the value
"""

def switch(status:bool) -> bool:
	"""
	Switches the value of status\n
	"""
	return not status


isFanOn = True
print(switch(isFanOn))