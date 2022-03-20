"""
wordgame
for right ans +10
for '' game over
'fox' 

"""

player1 = {
	'name':'player1',
	'score':0
}

player2 = {
	'name':'player2',
	'score':0
}

FIRST_WORD = 'apple'

while True:

	for i, player in enumerate([player1,player2]):
		ans = input(f"player {i+1}: ")

		# TODO CODE HERE