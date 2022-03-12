"""
This app will ask user to choose between 1 and 2
- if user selects 1 then ask user what task to add
- user will input task, task will added

if user selects 2 then remove the task

- take user input
- check input
- if 1 then ask what to add, add task
- if 2 then ask what to remove, remove task
- repeat
"""

TASK_LIST = []

userInput = True
while userInput:
	print("MENU")
	print("1: ADD")
	print("2: REMOVE")

	userInput = input("Enter what to do : ")

	# Adding a task
	if userInput == '1':
		print("Task: ")
		taskToAdd = input()
		TASK_LIST.append(taskToAdd)

	# Removing a task
	if userInput == '2':
		# Showing current tasks
		for i, task in enumerate(TASK_LIST):
			print(i, task)

		taskToRemoveIndex = int(input())
		TASK_LIST.pop(taskToRemoveIndex)

	# Printing all tasks
	print('MY TASKS:')
	for task in TASK_LIST:
		print(task)
