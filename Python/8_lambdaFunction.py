
# Python Lambda Functions
'''
Will study anonymous, commonly called lambda functions in Python. A lambda function can take n number of arguments at a time.
But it returns only one argument(result) at a time. We will understand what they are, how to execute them, 
and their syntax.
--> This function accepts any count of inputs but only evaluates and returns one expression. That means it takes many inputs but returns only one output.
'''

print("\n\n ******************  1st Way - giving name **********************\n")

lmdWith2Args = lambda n1 , n2 : n1+n2 

add6 = lambda n1 : n1+6  # here add6 will work as a function 


def reciprocal( num ):  
    return 1 / num  
   
lambda_reciprocal = lambda num: 1 / num  
   


inpNum = int(input("Enter any number i will return a new by adding 6: "))
res = add6(inpNum)
print(f"Modified {inpNum} Number to new : {res} \n")

print("\n\n ******************  1st Way but two args- giving name **********************\n")

inpNum2 = int(input("Enter one more numer i will add modified and new number both: "))
res2 = lmdWith2Args(res , inpNum2)
print(f"Added two modifed {res} and new one {inpNum2} : {res2} \n")



print("\n\n ******************  2nd Way-  difference between def() and lambda(). **********************\n")

# using the function defined by def keyword  
print( "Def keyword: ", reciprocal(6) )  
   
# using the function defined by lambda keyword  
print( "Lambda keyword: ", lambda_reciprocal(6) )  

print("\n\n ******************  Some useCases As EXAMPLES. **********************\n\n")

print("\t\t  Lambda Function with filter() - filter the Odd numbers only \n")
# This code used to filter the odd numbers from the given list  
ListOfNumbers = [1,2,5,76,35, 12, 69, 55, 75, 14, 73]  
print(f" Origin LIST of Number : {ListOfNumbers}")
oddNumList= list(filter(lambda num: num % 2 != 0 , ListOfNumbers))
print( "filtered odd Number Of above list: ", oddNumList )  
   

# Code to use lambda function with if-else    
Minimum = lambda x, y : x if (x < y) else y       
print('The greater number is:', Minimum( 35, 74 ))  


# about filter() function

'''
The filter() method accepts two arguments in Python: a function and an iterable such as a list.

The function is called for every item of the list, and a new iterable or list is 
returned that holds just ** those elements that returned True ** when supplied to the function.
'''