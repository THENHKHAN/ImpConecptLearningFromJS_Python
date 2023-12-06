#  use the * operator for the tuples and the ** operator for the dictionary in the function call. 
# can check you docs: https://docs.google.com/document/d/1Q1iJ4X65I77xN3h3D-LxvHnwjXYKHU2In2imWk4w480/edit


'''
Packing and unpacking in Python generally refer to the concept of bundling multiple values into a single variable (packing) or 
extracting values from a single variable into separate variables (unpacking). This is often used with tuples, lists, and dictionaries. '''
# Code #1:
'''
unpacking
# Program to understand about 
# packing in Python
'''
# Code #5: * THrough FUNCTION ::::::::  UNnnnnnnnnnnPacking arguments in FUNCITN
def sum1(a,b,c):
    return (a+b+c)
a = [1, 999, 1] # it could be tuple as well things will work same.
print("The sum of the list is: ",sum1(*a)) # The sum of the list is:  1001

# Code #2: Packing
# Packing values into a tuple
my_tuple = 1, 2, 3 # or it could be (1,2,3) or [1,2,3]  -- In this example, we first pack the values 1, 2, and 3 into a tuple my_tuple. 

# Printing the tuple
print("Packed Tuple:", my_tuple) # Packed Tuple: (1, 2, 3)

# Code #3: Unpacking:
# Unpacking values from a tuple
a, b, c = my_tuple             # Then, we unpack the values from the tuple into variables a, b, and c.  

# Printing the unpacked values
print("Unpacked Values:", a, b, c) # Unpacked Values: 1 2 3  


# Code #4: Unpacking: DICTIONARY
# Unpacking key-value pairs from a dictionary
d = {'x': 10, 'y': 20, 'z': 30}

a, b, c = d.values()

# Printing the unpacked values
print("Unpacked Values:", a, b, c) # Unpacked Values: 10 20 30

# Code #5: * THrough FUNCTION ::::::::  Pacccccccccccccccccccccccccccking arguments IN FUNCITON
# Packing arguments into a tuple using *args
def pack_arguments(*args):
    print("Packed Arguments:", args) # Packed Arguments: (1, 2, 3, 'a', 'b')

# Calling the function with multiple arguments
pack_arguments(1, 2, 3, 'a', 'b') 

# Code #6: * AND some varibale : THrough FUNCTION ::::::::  Pacccccccccccccccccccccccccccking arguments IN FUNCITON
# Unpacking arguments from a tuple using *args
def unpack_arguments(a, b, c, *args):
    print("Unpacked Values:", a, b, c, args) # Unpacked Values: 1 2 3 ('a', 'b', 'c')

# Calling the function with multiple arguments
unpack_arguments(1, 2, 3, 'a', 'b', 'c')



# Code #7:    WIHT DICTTTTTTTTTTTTTTTTT 
# Packing keyword arguments into a dictionary using **kwargssss  with DICTTTTTTTTTTTTT
def pack_keyword_arguments(**kwargs):
    print("Packed Keyword Arguments:", kwargs) # packed Keyword Arguments: {'a': 1, 'b': 2, 'c': 'hello'}

# Calling the function with multiple keyword arguments
pack_keyword_arguments(a=1, b=2, c='hello')


# Code #8:    WIHT DICTTTTTTTTTTTTTTTTT 
# Unpacking keyword arguments from a dictionary using **kwargs
def unpack_keyword_arguments(a, b, c='default', **kwargs):     # kwargs work as a dict
    print("Unpacked Values:", a, b, c, kwargs) # Unpacked Values: 1  2 hello {'d': 4, 'e': 'world'}
    print("Unpacked Values:", a, b, c, kwargs["d"]) # Unpacked Values: 1 2 hello 4

# Calling the function with multiple keyword arguments 
unpack_keyword_arguments(a=1, b=2, c='hello', d=4, e='world') 
