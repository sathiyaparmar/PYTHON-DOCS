"""
make a class name Validator, where in constructor pass a string
make an instance variable isValid
if all chars of string are lower then set isValid to true else false
"""

class Player:

	isDead = False
	currentHealth = 100
	maxHealth = 100

	def __init__(self, username:str):
		pass

p1 = Player('dummy1')
p1.isDead = True

print(p1.isDead)		# True
print(Player.isDead)	# False