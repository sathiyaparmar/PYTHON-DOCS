username = 'change'
accountBalance = 1000
debt = 900


# s = username + " has debt of " + str(debt/accountBalance*100) + "%"
# print(s)

# fstring
x = debt/accountBalance*100
# s = f"{username} has debt of {x}%"
s = "{u} has debt of {}%{}".format(x,'jfjasfd',u=username)
# 90% has debt of change
# 90.0 has debt of change%
# change has debt of 90%
print(s)

# dummy has debt of x%
# x = net/inital *100
# x = 500/1000*100

# print(500/1000*100)

# 3.333333338489 # add precision