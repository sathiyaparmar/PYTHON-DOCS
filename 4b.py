member = "Jason"
height = 190
weight = 80

# 
# x = BMI (Body Mass Index)
# BMI = kg/m^2

bmi = weight/pow((height/100),2)

s = f"{member} has BMI of {round(bmi,3)}"
print(s)