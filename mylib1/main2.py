import os


currentDirectoryPath = os.path.dirname(__file__)
print(currentDirectoryPath) 

# Find difference between these two
# os.makedirs(x)
# os.mkdir()

# 
students = {
	"1":{
		"marks":None,
		"report":None
	},
	"2":{
		"marks":None,
		"report":None
	},
}

sd = os.path.join(currentDirectoryPath,'student')
print(sd)

os.mkdir(sd)

# os
# json
# time
# datetime
# pickle (serialization, deserialization)
# pandas