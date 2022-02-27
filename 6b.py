totalBalance = 10000
myTransactions = [800,1200,6000,140,36.35,689]

# How much amount left in my purse
# How much percent did i spent
# percent spend save in a list

# 1st
# amountSpent = myTransactions[0] + myTransactions[1] + myTransactions[2] + myTransactions[3] + myTransactions[4] + myTransactions[5]
amountSpent = sum(myTransactions)
amountLeft = round(totalBalance - amountSpent, 3)
print('Amount left:',amountLeft)

# 2nd & 3rd
current = totalBalance
percentSpent = []

index = 0
p = myTransactions[index]/current*100
current -= myTransactions[index] 
percentSpent.append(p)
print(p)

index = 1
p = myTransactions[index]/current*100
current -= myTransactions[index] 
print(p)
percentSpent.append(p)

index = 2
p = myTransactions[index]/current*100
current -= myTransactions[index] 
print(p)
percentSpent.append(p)

index = 3
p = myTransactions[index]/current*100
current -= myTransactions[index] 
print(p)
percentSpent.append(p)

index = 4
p = myTransactions[index]/current*100
current -= myTransactions[index] 
print(p)
percentSpent.append(p)

index = 5
p = myTransactions[index]/current*100
current -= myTransactions[index] 
print(p)
percentSpent.append(p)

print(percentSpent)