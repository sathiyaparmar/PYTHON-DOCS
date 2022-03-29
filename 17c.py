"""
The gymMembers dict contains gym members base data
- Calculate BMI for each member and put the 'bmi' as key in gymData dict
	=> BMI (Body Mass Index) = kg/m^2

- Add a key 'diet' to gymMembers dict where
	- If BMI is < 17 that means the person is underweight and should follow underweight diet
	- If BMI is > 27 that means the person is overweight and should follow overweight diet
	- If person is between 17 and 27 then person should follow body maintain diet

- Use functions wisely

"""

import json

with open('17c.json') as f:
	gymMembers = json.load(f)
	f.close()

# TODO Code here
# print(gymMembers)

for member in gymMembers:
	member['somedata'] = 'some useful data'

for member in gymMembers:
	print(member)