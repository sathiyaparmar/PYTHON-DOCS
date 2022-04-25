
"""

"""

class Player:

	currentHealth = 100

	def __init__(self, username:str):
		self.username = username

	def take_damage(self, damageBy, damageAmount:float):
		pass

if __name__ == '__main__':

	p1 = Player('dummy1')
	p2 = Player('dummy2')
	p3 = Player('dummy3')

	p1.take_damage(p2,20)
	p1.take_damage(p3,13.5)
	p2.take_damage(p1,57)
	p3.take_damage(p2,20)
	p2.take_damage(p2,70)
	p1.take_damage(p2,20)