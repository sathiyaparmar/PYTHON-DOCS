

class Vehicle:

	_speed = None

	def horn(self):
		print("Vehicle horn")

class Car(Vehicle):

	_noOfTyres = 4

	def horn(self):
		print("car horn")
		super().horn() # py3
		print("new things")

class Scooter(Vehicle):

	_noOfTyres = 2

	def apply_breaks(self):
		self._speed = 0

car1 = Car()
scooter1 = Scooter()

# print(car1._speed)
car1.horn()
#scooter1.horn()
scooter1.apply_breaks()
print(scooter1._speed)