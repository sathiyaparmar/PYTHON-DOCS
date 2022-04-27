import math 

class Vector:

	def __init__(self, p1,p2,p3):
		self.i = p1
		self.j = p2
		self.k = p3

	def __repr__(self):
		return repr((self.i,self.j,self.k))

	def __add__(self,other):
		p1 = self.i + other.i
		p2 = self.j + other.j
		p3 = self.k + other.k
		return Vector(p1,p2,p3)

	def __sub__(self, other):
		p1 = self.i - other.i
		p2 = self.j - other.j
		p3 = self.k - other.k
		return Vector(p1,p2,p3)

	def get_magnitude(self):
		return round(math.sqrt((self.i*self.i) + (self.j*self.j) + (self.k*self.k)),3)

if __name__ == "__main__":
	v1 = Vector(0,1,0)
	print(v1)

	# v2 = Vector(1,1,1)
	# print(v2)

	# print(v1 - v2)

	v3 = Vector(3,4,5)
	print(v3.get_magnitude())