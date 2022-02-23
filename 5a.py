# Question 
users = ['Alice','Bob','Carmalia','Doug']
balance = [1000,2000,5000,80]
debt = [500,800,3600,0]

# Alice has debt of x%

s1 = f"{users[0]} has debt of {round((debt[0])/balance[0]*100,3)}"
s2 = f"{users[1]} has debt of {round((debt[1])/balance[1]*100,3)}"
s3 = f"{users[2]} has debt of {round((debt[2])/balance[2]*100,3)}"
s4 = f"{users[3]} has debt of {round((debt[3])/balance[3]*100,3)}"
print(s1)
print(s2)
print(s3)
print(s4)