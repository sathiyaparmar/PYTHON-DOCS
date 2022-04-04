import os

c = ['config1','config2','config3']

# config1.json
currentDirectoryPath = os.path.dirname(__file__)
print(currentDirectoryPath) 

for i in c:

	x = os.path.join(currentDirectoryPath,f"{i}.json")
	print(x)

	status = os.path.exists(x)
	print(status)