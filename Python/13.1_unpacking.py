# Python - Unpack Tuples

###################### Example 1: Using list, tuple & string

x, y, z = 10, 20, 30
print("x = {0}, y = {1}, z = {2}".format(x, y, z)) # x = 10, y = 20, z = 30

# list example
x, y, z = [40, 50, 60]
print("x = {0}, y = {1}, z = {2}".format(x, y, z)) # x = 40, y = 50, z = 60

# tuple example
x, y, z = (70, 80, 90)
print("x = {0}, y = {1}, z = {2}".format(x, y, z)) # x = 70, y = 80, z = 90

# string example
w, x, y, z = 'Data'
print("w = {0}, x = {1}, y = {2}, z = {3}".format(w, x, y, z)) # w = D, x = a, y = t, z = a

##################### Example 2: Using sets and dictionaries

# dictionary example
x, y, z = {'k1': 101, 'k2':102, 'k3': 103}
print("x = {0}, y = {1}, z = {2}".format(x, y, z)) # x = k1, y = k2, z = k3

# set example
x, y, z = {104, 105, 106}
print("x = {0}, y = {1}, z = {2}".format(x, y, z)) # x = 104, y = 105, z = 106

'''
Tips: Since sets & dictionaries are an unordered collection of elements, it is not 
recommended to use them for unpacking as there is no guarantee on the order of the results.'''

fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
# green, yellow, red = fruits both are same means can be used the varibale

print(green)
print(yellow)
print(red)

# Note**: The number of variables must match the number of values in the tuple, if not, you must use an asterisk to collect the remaining values as a list.





# When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
# we are also allowed to extract the values back into variables. This is called "unpacking":


'''
x = 10, y = 20, z = 30
x = 40, y = 50, z = 60
x = 70, y = 80, z = 90
w = D, x = a, y = t, z = a
x = k1, y = k2, z = k3
x = 104, y = 105, z = 106
apple
banana
cherry
'''