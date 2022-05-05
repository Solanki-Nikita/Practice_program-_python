'''# Python program to find the size of a tuple 

# Creating a tuple in python 
myTuple = ('niki', 'python', 3, 2021)

# Finding size of tuple using len() method 
tupleLength = len(myTuple)

# Printing the tuple and Length
print("Tuple : ", str(myTuple))
print("Tuple Length : ", tupleLength)'''

# Python program to find the size (__sizeof__)of a tuple 

# Creating a tuple in python 
myTuple = ('includehelp', 'python', 3, 2021)

# Finding size of tuple
tupleSize = myTuple.__sizeof__()

# Printing the tuple and size
print("Tuple : ", str(myTuple))
print("Tuple Length : ", tupleSize)
