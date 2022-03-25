carGear = [1,2,3,4,5] # n
carSpeedRange = [10,30,50,70] # m
carSetting3 = [9,2,3] # l
# (1,10),(1,30),(1,50),(1,70),(2,10)...(5,70)

# n*m * l * l2
for i in carGear:
	for j in carSpeedRange:
		for k in carSetting3:
			print((i,j,k))
