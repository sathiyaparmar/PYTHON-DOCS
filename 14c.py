"""
dictionary
"""

myData = [{'x':4,'y':0},{'x':-10,'y':10}]

# find x and y projections

# print('x-axis-projection',4,'=>',10)
# print('y-axis-projection',0,'=>',10)

allX = [i['x'] for i in myData]
allY = [i['y'] for i in myData]

print(min(allX),'=>',max(allX))
print(min(allY),'=>',max(allY))