import os

tasklist = ['task1','task2']

def save_data():
	someData = '\n'.join(tasklist)

	with open(os.path.join(os.path.dirname(__file__),'somedata.txt'),'w') as f:
		f.write(someData)
		f.close()