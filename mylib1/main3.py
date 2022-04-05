import os



x = os.path.dirname(__file__)
print(x)

x1 = os.path.join(x,"mydir1","mydir2")
print(x1)

# os.mkdir(x1)