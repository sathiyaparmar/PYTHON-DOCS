# List

"""
List vs Array

- in list elements type can be very
- in array elements are of same type

- in list reversal index can be accessed
- in array reversal index can not be accessed

- you can delete index in list
- you can not delete index in array

- list elements are scattered in RAM
- array elements are in sequence

- in execution list are slow
- in execution arrays are fast
"""
# del myList[1]
# print(myList)

"""
1000-1003	=> 0
10004-1007	=> 1
1008-1011	=> 2
1012-1015	=> 3
"""

myList = ['A',1,1.36,sum,ImportError] # list
# ['A',1,1.36,sum,ImportError]
# [['A',1,1.36,sum,ImportError]]
print(list(myList))
print([myList])