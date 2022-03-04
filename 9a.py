country = 'UK'
noOfPeople = 73
# Every odd number is male, and even is female

# print in sequence member code
# UK:1_M
# UK:2_F

t = []
for i in range(1,noOfPeople+1,2):
	t.append(f"{country}:{i}_M")
	t.append(f"{country}:{i+1}_F")
print(t)