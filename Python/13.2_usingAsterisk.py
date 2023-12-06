# Using Asterisk*

# If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

print("\n ********  1st   *************\n ")
(green, yellow, *red) = fruits # Assign the rest of the values as a list called "red":

print(green)
print(yellow)
print(red)

# If the asterisk is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left.
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
print("\n ********  2nd   *************\n ")
(green, *tropic, red) = fruits # Add a list of values the "tropic" variable:

print(green)
print(tropic)
print(red)

# I/O:
'''
********  1st   *************
apple
banana
['cherry', 'strawberry', 'raspberry']
********  2nd   *************
apple
['mango', 'papaya', 'pineapple']
cherry
'''