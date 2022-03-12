"""
User have 10000 rs in his bank account
- Menu will ask to do
1. Deposite
2. Withdraw
3. See balance

- In deposite, ATM will ask how much money to deposite
- In withdraw, ATM will ask how much money to withdraw, if user has enough money to withdraw
- Show balance
"""

BALANCE = 10000

print("MENU")
print("1: Deposite")
print("2: Withdraw")
print("3: Check balance")
print("4: Exit")

while True:
	userInput = input("Your input: ")

	# Do deposite
	if userInput == '1':
		amountToDeposite = float(input("Enter amount: "))
		BALANCE += amountToDeposite

	# DO withdraw
	if userInput == '2':
		amountToWithdraw = float(input("Enter amount: "))

		if (BALANCE >= amountToWithdraw):
			BALANCE -= amountToWithdraw
		else:
			print("You are poor")

	# Check balance
	elif userInput == '3':
		print("Your current balance is",BALANCE)

	# Exit code
	elif userInput == '4':
		break

	else:
		print("Invalid input")
