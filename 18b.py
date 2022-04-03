"""
make a function with name crop

input will be wh as a tuple with 2 values width and height ie.(1920,1080)
there will be a keyword argument aspectRatio with default value is (1,1) == 1:1

converts the height and width to 1:1

100x200 => 1:1 ==> 100x100
200x100 => 1:1 ==> 100x100
100x500 => 1:2 ==> 100x200
500x200 => 4:5 ==> (500*5/4=625)x200

find if landscape or portrait

"""

def get_image_type(wh:tuple) -> str:
	"""
	Returns landscape or portrait
	"""
	if wh[0] > wh[1]:
		return 'landscape'
	elif wh[0] < wh[1]:
		return 'portrait'
	else:
		return 'square'

def crop(wh:tuple,aspectRatio:tuple=(1,1)) -> tuple[int,int]:
	"""
	Crops image with aspect ratio\n
	"""
	# 100x200 = portrait => 100x100
	# 200x100 = landscape => 100x100
	imageType = get_image_type(wh)

	# If square crop karna hai
	if aspectRatio == (1,1):
		if imageType == 'square':
			return wh
		elif imageType == 'portrait':
			return wh[0],wh[0]
		elif imageType == 'landscape':
			return wh[1],wh[1]

	# If square crop nahi karna
	else:
		if imageType == 'square':
			return wh

		# Cropping portrait pics
		# This means height of pic > width of pic
		elif imageType == 'portrait':
			aW, aH = aspectRatio
			if aW > aH:
				return int(wh[1]*aH/aW), wh[1]
			elif aW < aH:
				return int(wh[1]*aW/aH), wh[1]

		elif imageType == 'landscape':
			pass

myImage = (500,600) # 300,600

print(crop(myImage,(1,1)))
# print(crop(myImage,(5,4)))
# print(get_image_type(myImage))
