"""
Find how many burger, pizza, sandwithc

Algo
- First we make one item
- then we remove those quantity in currentstock
- the redo step 1 until it breaks
"""

import json

with open('17d.json') as f:
	bakery = json.load(f)
	f.close()

# TODO Code here
# print(bakery)

def does_have_minimum_stock(rI,cS):
	"""
	"""
	haveAllIngradients = True
	for i in rI:
		for name, q in i.items():
			for stock in cS:
				if (stock['name'] == name): 
					if (stock['quantity'] >= q):
						print(name,'hai')
						break
					else:
						haveAllIngradients = False

	return haveAllIngradients


def remove_items_from_current_stock(rI,cS):
	for i in rI:
		for name,q in i.items():
			for stock in cS:
				if stock['name'] == name:
					stock['quantity'] -= q


# For burger
currentFood = 'sandwitch'
currentStock = bakery['inventory'].copy()
# print(currentStock)
noOfBurgers = 0
requiredIngradients = bakery['recipe'][currentFood]['ingradients'] # This is a list
while does_have_minimum_stock(requiredIngradients,currentStock):
	noOfBurgers += 1
	remove_items_from_current_stock(requiredIngradients,currentStock)

print("Max burgers:",noOfBurgers)