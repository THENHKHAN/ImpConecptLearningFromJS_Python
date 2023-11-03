

# Python map() Function
'''
The map() function executes a specified function for each item in an iterable. The item is sent to the function as a parameter.

Python map() function is used to apply a function on all the elements of specified iterable and return map object. Python map object is an iterator, so we can 
iterate over its elements. We can also convert map object to sequence objects such as list, tuple etc. using their factory functions.
'''
# Syntax:
            # map(function, iterables)
        
'''
function-> Required. The function to execute for each item
iterable-> Required. A sequence, collection or an iterator object. You can send as many iterables as you like, just make sure the function has one parameter for each iterable.

'''
def toUpperCase (inputStr):
    return inputStr.upper()

def doubleItem(item):
    return item*2


def printIterator(itr) : # this is another way to print the return iterable object without type casting
    for ele in itr :
        print(ele , end=" ")



# 1 

print("\n\n ******************  1   **********************\n")

lst1 = [1,2,3,4,5]
print(f" Origin list : {lst1}")
# i want to double each item 
map_iterator =map(doubleItem,lst1)
doubleItems =  list(map_iterator) # type casted bcz map , reduce ,filter all are return iterator
print(f" DoubledItem list : {doubleItems}")


#2 
print("\n\n ******************  2   map() with string **********************\n")
strLower = "abc"
print(f" Origin String : {strLower}")
myUpperStr = list(map(toUpperCase , strLower))# str(map(toUpperCase , strLower)) does not affect bcz it work differentlyt when casting in string.
print(f" my list of String : {myUpperStr}")
actualMyStr="".join(myUpperStr)
print(f" my Upper String : {actualMyStr}")
# behaviovour:
'''
he issue you're encountering is due to the behavior of Python's map function. In Python 3, the map 
function returns a map object, which is an iterator. It doesn't immediately compute the results and convert them into a list or string.

To convert the map object to a string, you need to iterate through it and build the string manually
or convert it to a list and then to a string. Here's how you can do it:
'''


#3 
print("\n\n ******************  3  map() with tuple **********************\n")
myOrgTuple =  ( 'a', 'xyz')
print(f" Origin Tuple : {myOrgTuple}")
map_iterator = map(toUpperCase , myOrgTuple)
print(f" my Upper TUPLE : " , end=" ")
printIterator(map_iterator)
# print(f" my Upper String : {tuple(map_iterator)}") # my Upper String : ('A', 'XYZ')

#4 
print("\n\n ******************  4  map() with LIST **********************\n")
myOrgList =  ['e', 'x', 'abc']
print(f" Origin LIST : {myOrgList}")
map_iterator = map(toUpperCase, myOrgList)
myUpperListItems =  list(map_iterator)
print(f" my Upper LstItems : {myUpperListItems}")



#5 
print("\n\n ******************  5  Converting map() to list, tuple, set **********************\n")

myOrgList =   ['a', 'b', 'c']
print(f" Origin LIST : {myOrgList}")
map_iterator = map( toUpperCase , myOrgList)
myList = list(map_iterator)
print(f"\t\t\t my Upper LstItems : {myList}")

# we can't just cast map_iterator to list , tuple and set one by one bcz iterator moved to next pointer hence remaing will get empty

map_iterator = map( toUpperCase , myOrgList)
myTuple = tuple(map_iterator)
print(f"\t\t\t my Upper TupleItems : {myTuple}")

map_iterator = map( toUpperCase , myOrgList)
mySet = set(map_iterator)
print(f"\t\t\t my Upper SetItems : {mySet}")


#6 
print("\n\n ******************  6  map() with Lambda function **********************\n")
# We can use lambda functions with map() if we don’t want to reuse it. This is useful when our function is small and we don’t want to define a new function.
list_numbers = [1, 2, 3, 4]
print(f" Origin LIST of Number : {list_numbers}")
map_iterator = map(lambda item : item * 2 , list_numbers)
print(f"my Double List of number : {list(map_iterator)}")


#7
print("\n\n ******************  7  map() with multiple Args **********************\n")

lst1 = [1,2,3]
lst2 = [10,11,12]
print(f" Origin LIST1 : {lst1}  and LIST2 : {lst2}")
map_iterator = map(lambda n1 , n2 : n1*n2 , lst1 , lst2) # so n1 from lst1 and n2 from lst2
print(f"Multiplication of above two  List to generate new list: {list(map_iterator)}")





# INPUT/OUTPUT

'''


 ******************  1   **********************

 Origin list : [1, 2, 3, 4, 5]
 DoubledItem list : [2, 4, 6, 8, 10]


 ******************  2   map() with string **********************

 Origin String : abc
 my list of String : ['A', 'B', 'C']
 my Upper String : ABC


 ******************  3  map() with tuple **********************

 Origin Tuple : ('a', 'xyz')
 my Upper TUPLE :  A XYZ

 ******************  4  map() with LIST **********************

 Origin LIST : ['e', 'x', 'abc']
 my Upper LstItems : ['E', 'X', 'ABC']


 ******************  5  Converting map to list, tuple, set **********************

 Origin LIST : ['a', 'b', 'c']
                         my Upper LstItems : ['A', 'B', 'C']
                         my Upper TupleItems : ('A', 'B', 'C')
                         my Upper SetItems : {'C', 'A', 'B'}


 ******************  6  map with Lambda function **********************

 Origin LIST of Number : [1, 2, 3, 4]
my Double List of number : [2, 4, 6, 8]

E:\NHKHAN_studySelf\#GitUsedForPersonalGitAccount_UploadFileFromGitHub\ImpConecptLearningFromJS_Python\Python>python -u "e:\NHKHAN_studySelf\#GitUsedForPersonalGitAccount_UploadFileFromGitHub\ImpConecptLearningFromJS_Python\Python\7_mapFunction.py"


 ******************  1   **********************

 Origin list : [1, 2, 3, 4, 5]
 DoubledItem list : [2, 4, 6, 8, 10]


 ******************  2   map() with string **********************

 Origin String : abc
 my list of String : ['A', 'B', 'C']
 my Upper String : ABC


 ******************  3  map() with tuple **********************

 Origin Tuple : ('a', 'xyz')
 my Upper TUPLE :  A XYZ

 ******************  4  map() with LIST **********************

 Origin LIST : ['e', 'x', 'abc']
 my Upper LstItems : ['E', 'X', 'ABC']


 ******************  5  Converting map() to list, tuple, set **********************

 Origin LIST : ['a', 'b', 'c']
                         my Upper LstItems : ['A', 'B', 'C']
                         my Upper TupleItems : ('A', 'B', 'C')
                         my Upper SetItems : {'B', 'A', 'C'}


 ******************  6  map() with Lambda function **********************

 Origin LIST of Number : [1, 2, 3, 4]
my Double List of number : [2, 4, 6, 8]


 ******************  7  map() with multiple Args **********************

Multiplication of above two  List to generate new list: [10, 22, 36]

E:\NHKHAN_studySelf\#GitUsedForPersonalGitAccount_UploadFileFromGitHub\ImpConecptLearningFromJS_Python\Python>python -u "e:\NHKHAN_studySelf\#GitUsedForPersonalGitAccount_UploadFileFromGitHub\ImpConecptLearningFromJS_Python\Python\7_mapFunction.py"


 ******************  1   **********************

 Origin list : [1, 2, 3, 4, 5]
 DoubledItem list : [2, 4, 6, 8, 10]


 ******************  2   map() with string **********************

 Origin String : abc
 my list of String : ['A', 'B', 'C']
 my Upper String : ABC


 ******************  3  map() with tuple **********************

 Origin Tuple : ('a', 'xyz')
 my Upper TUPLE :  A XYZ

 ******************  4  map() with LIST **********************

 Origin LIST : ['e', 'x', 'abc']
 my Upper LstItems : ['E', 'X', 'ABC']


 ******************  5  Converting map() to list, tuple, set **********************

 Origin LIST : ['a', 'b', 'c']
                         my Upper LstItems : ['A', 'B', 'C']
                         my Upper TupleItems : ('A', 'B', 'C')
                         my Upper SetItems : {'B', 'A', 'C'}


 ******************  6  map() with Lambda function **********************

 Origin LIST of Number : [1, 2, 3, 4]
my Double List of number : [2, 4, 6, 8]


 ******************  7  map() with multiple Args **********************

 Origin LIST1 : [1, 2, 3]  and LIST2: [10, 11, 12]
Multiplication of above two  List to generate new list: [10, 22, 36]

E:\NHKHAN_studySelf\#GitUsedForPersonalGitAccount_UploadFileFromGitHub\ImpConecptLearningFromJS_Python\Python>python -u "e:\NHKHAN_studySelf\#GitUsedForPersonalGitAccount_UploadFileFromGitHub\ImpConecptLearningFromJS_Python\Python\7_mapFunction.py"


 ******************  1   **********************

 Origin list : [1, 2, 3, 4, 5]
 DoubledItem list : [2, 4, 6, 8, 10]


 ******************  2   map() with string **********************

 Origin String : abc
 my list of String : ['A', 'B', 'C']
 my Upper String : ABC


 ******************  3  map() with tuple **********************

 Origin Tuple : ('a', 'xyz')
 my Upper TUPLE :  A XYZ

 ******************  4  map() with LIST **********************

 Origin LIST : ['e', 'x', 'abc']
 my Upper LstItems : ['E', 'X', 'ABC']


 ******************  5  Converting map() to list, tuple, set **********************

 Origin LIST : ['a', 'b', 'c']
                         my Upper LstItems : ['A', 'B', 'C']
                         my Upper TupleItems : ('A', 'B', 'C')
                         my Upper SetItems : {'A', 'B', 'C'}


 ******************  6  map() with Lambda function **********************

 Origin LIST of Number : [1, 2, 3, 4]
my Double List of number : [2, 4, 6, 8]


 ******************  7  map() with multiple Args **********************

 Origin LIST1 : [1, 2, 3]  and LIST2 : [10, 11, 12]
Multiplication of above two  List to generate new list: [10, 22, 36]


'''