# How to take space-separated input in one line in Python? 

# Program take space-separated input in one line in Python
x, y, z = input("Enter two value space separated : ").split()
print(f"X: {x} , Y:{y} , Z: {z}") # X: 5 , Y:6 , Z: 3
# Enter two value space separated : 5 6 3     if split()
# X: 5 , Y:6 , Z: 3
# Enter two value space separated : 6-4-2 if  split("-")
# X: 6 , Y:4 , Z: 2
'''
Note that we don’t have to explicitly specify split(" ") because split() uses any whitespace characters as a delimiter as default.
One thing to note in the above Python code is, both x and y would be of string. We can convert them to int using another line. by type casting.
'''