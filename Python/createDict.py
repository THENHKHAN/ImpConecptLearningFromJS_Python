
print("*************    Creating an Empty Dictionary:     ***************")
# You can create an empty dictionary by calling dict() with no arguments.
my_dict = dict()
print(my_dict)  # {}

print("*************  Creating a Dictionary from a List of Key-Value Pairs:     ***************")
# This creates a dictionary with the specified key-value pairs.

key_value_pairs = [("name", "John"), ("age", 30), ("city", "New York")]
my_dict = dict(key_value_pairs)
print(my_dict) # {'name': 'John', 'age': 30, 'city': 'New York'}

print("*************  Creating a Dictionary from Keyword Arguments:     ***************")
# You can create a dictionary by passing keyword arguments to the dict() function.
my_dict = dict(name="John", age=30, city="New York")
print(my_dict) # {'name': 'John', 'age': 30, 'city': 'New York'}

