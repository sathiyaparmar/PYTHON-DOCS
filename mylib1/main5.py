"""
Task manager

user will propted with enter tasks
if tasks is empty then exit the code
if there is a task then append to a list
"""

import os 

taskList = []

SAVE_PATH = os.path.join(os.path.dirname(__file__),'mytasks.txt')

def add_task(task):
	taskList.append(task)

def save_tasks():
	print("Ab jitne bhi tasks record hue hai utne txt me save karenge")

	# dataToSave = ""
	# for task in taskList:
	# 	dataToSave += task
	# 	dataToSave += '\n'

	dataToSave = '\n'.join(taskList)

	with open(SAVE_PATH,'w') as f:
		f.write(dataToSave)
		f.close()

while True:

	taskToAdd = input("Enter your task: ")
	if taskToAdd:
		add_task(taskToAdd)
	else:
		break

print(taskList)
# tasklist = ['task1','task2']
save_tasks()