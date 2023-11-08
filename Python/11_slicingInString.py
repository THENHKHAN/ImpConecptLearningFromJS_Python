# String Slicing in Python: Usage and Examples
'''
One of the key features of string slicing in Python is that it doesn’t alter the original string. Instead, 
it generates a new string with the sliced characters.
This ensures your original data stays unmodified, allowing you to use it for other operations without concern.
'''

s = "Python Programming"
print("String is: ", s) #Python Programming
print(f"String {s} length:  {len(s)}") # 18

# Negative indexing  
print("The last character of the string is: ", s[-1])  # g
print("The second last character of the string is: ", s[-2]) # n 
print("The last five characters of the string are: ", s[-5:]) # mming
print("Characters from index -1 to -5 are: ", s[-1:-6:-1]) # gnimm
# comment:
'''
In this code, s[-1] will print the last character, s[-2] will print the 
second last character, s[-5:] will print the last 5 characters and s[-1:-6:-1] will 
show the characters from -1 index to -5 index.
'''

print("\n\n *****   Stride in String Slicing         *******\n\n ")

# Stride in String Slicing OR puting the 3rd argument called stride
'''
Stride, on the other hand, gives you the ability to skip characters in a slice.

It's the third argument you can pass in the slicing syntax (start:stop:stride). By default, the stride is 1,means move forward in sequence
which means no characters are skipped. However, if you set the stride to 2, 
for instance, every other character will be skipped, providing a more controlled slice.
'''

s = "Hello, World!"

# stride 1, no characters are skipped
print("Original string: ", s)  # Hello, World!
strided_s_1 = s[::1]
print("Strided string with stride 1: ", strided_s_1) # Hello, World!

# stride 2, every other character is skipped
strided_s_2 = s[::2]
print("Strided string with stride 2: ", strided_s_2) #   Hlo ol!

# stride -1, it will reverse the string -- printing from last to 1st character means moving backward since -1.
strided_s_reverse = s[ : :-1]
print("Strided string with stride -1 (Reverse string): ", strided_s_reverse) # !dlroW ,olleH
# COMMENTS:
'''
In the above code, s[::1] prints the original string without skipping any character, s[::2] prints every other character 
by skipping one character, and s[::-1] reverses the original string.
'''
 
print("\n\n *****  More Examples of Python String Slicing         *******\n\n ")

#  More Examples of Python String Slicing

s = 'Hello, World!'

# Removing the first character

print(s[1:]) # prints 'ello, World!'

# Removing the last character

print(s[:-1]) # prints 'Hello, World'

# Removing every other character

print(s[::2]) # prints 'Hlo ol!'

# Setting all three arguments

print(s[0:5:2]) # prints 'Hlo'
