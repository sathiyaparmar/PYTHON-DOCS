def static_params(param1,param2):
	print(param1,param2)

def dynamic_params(*params):
	print(params)

x = ('1st','2nd')
print(x)
print(*x)
static_params(*x)
dynamic_params(*x)
