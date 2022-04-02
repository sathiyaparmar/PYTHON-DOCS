"""
make a function with name crop

input will be wh as a tuple with 2 values width and height ie.(1920,1080)
there will be a keyword argument aspectRatio with default value is (1,1) == 1:1

converts the height and width to 1:1

100x200 => 1:1 ==> 100x100
200x100 => 1:1 ==> 100x100
100x500 => 1:2 ==> 100x200
500x200 => 4:5 ==> (500*5/4=625)x200

"""

def crop(wh:tuple,aspectRatio:tuple=(1,1)) -> tuple[int,int]:
	"""
	Crops image with aspect ratio\n
	"""
	return (0,0)

myImage = (500,400)
print(crop(myImage))