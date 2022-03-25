player1 = {
	'name':'player1',
	'score':0
}

player2 = {
	'name':'player2',
	'score':0
}

guessedWords = []
isGameOver = False

while True:

	for i, player in enumerate([player1,player2]):
		if guessedWords:
			print(f"word should start with",guessedWords[-1][-1])
		ans = input(f"player {i+1}: ")

		# TODO - if player gave up
		if not ans:
			isGameOver = True
			break

		# TODO - check if the answer is unique
		if ans in guessedWords:
			isGameOver = True
			break

		else:
			if not guessedWords:
				player['score'] += 10
				guessedWords.append(ans)

			elif ans[0] == guessedWords[-1][-1]:
				player['score'] += 10
				guessedWords.append(ans)

			else:
				isGameOver = True
				break

	# Check if game is over
	if isGameOver:
		print(player1)
		print(player2)
		break