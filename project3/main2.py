"""
Make a class name Jug
Jug will have jugCapacity as argument as constructor input

make a method name pour_in with amount to pour in
if amount is greater than the capacity than print overflowed
"""

class Jug:

	def __init__(self, jugCapacity:float):
		self._jugCapacity = jugCapacity


if __name__ == '__main__':

	jug1 = Jug(100)
	jug2 = Jug(50)

	print(f"Jug1 capacity is {jug1._jugCapacity}")
	print(f"Jug2 capacity is {jug2._jugCapacity}")