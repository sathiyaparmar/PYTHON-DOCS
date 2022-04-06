import os, json


def login(username: str, password: str) -> bool:
	"""
	Log in\n
	"""
	return (username == 'dummy1' and password == 'dummypass')
	
# Login successful
# username or password incorrect

# with open(os.path.join(os.path.dirname(__file__),'credentials.json')) as f:
# 	creds = json.load(f)
# 	f.close()

# if login(creds['username'],creds['password']):
# 	print("login successful")
# else:
# 	print("invalid credentials")


## write or create a file
# newFilePath = os.path.join(os.path.dirname(__file__),'dummy.json')

# data = {f"key_{k}":k for k in range(500)}
# print(data)

# with open(newFilePath,'w') as f:
# 	json.dump(data,f,indent=4)