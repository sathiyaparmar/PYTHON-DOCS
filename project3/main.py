

class Player:

	currentHealth = 100
	isDead = False

	def __init__(self,username) -> None:
		self.username = username

	def get_damage(self,howMuchDamage:float):
		self.currentHealth -= howMuchDamage
		
		if self.currentHealth <= 0:
			self.isDead = True
			print(self.username,'is dead')

	def get_current_health(self) -> float:
		return self.currentHealth


JOINED_PLAYERS = [
	Player('dummy1'),
	Player('dummy2')
]

JOINED_PLAYERS[0].get_damage(20)
JOINED_PLAYERS[0].get_damage(20)
JOINED_PLAYERS[0].get_damage(20)
JOINED_PLAYERS[0].get_damage(50)
print(JOINED_PLAYERS[0].get_current_health())
print(JOINED_PLAYERS[1].get_current_health())