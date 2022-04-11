"""
read data from input.json and write it in input.txt
"""

import os

p = os.path.join(os.path.dirname(__file__),'somefile.txt')


def read_txt_file(filePath: str) -> str:
	"""
	Reads a txt file\n
	"""
	with open(filePath) as f:
		data = f.read()
		f.close()
	return data

# print(read_txt_file(p))

with open(p,'a') as f:
	f.write("\nSome new data")
	f.close()
