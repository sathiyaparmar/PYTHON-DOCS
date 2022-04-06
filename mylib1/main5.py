"""
Task manager

user will propted with enter tasks
if tasks is empty then exit the code
if there is a task then append to a list
"""

taskList = []

def add_task(task):
	taskList.append(task)

def save_tasks():
	pass

while True:

	taskToAdd = input("Enter your task: ")
	if taskToAdd:
		add_task(taskToAdd)
	else:
		break

print(taskList)
# tasklist = ['task1','task2']
save_tasks()