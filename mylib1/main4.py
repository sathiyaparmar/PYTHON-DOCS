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