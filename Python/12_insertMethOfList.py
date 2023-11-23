
# Def: The insert() method inserts the specified value at the specified position or INDEX.
'''
list.insert(index, elmnt)
index	---->  Required. A number specifying in which index (index = position-1) to insert the value
elmnt---->  	Required. An element of any type (string, number, object etc.)
'''


# Python List insert() Method 

'''EX: Insert the value "orange" as the second element(or 2nd position OR means at 1st index ) of the fruit list:'''
def addOneEle (lst) :
       ele = "orange" 
       lst.insert(1,ele)
       print(f"Updated List : {lst}") #  ['apple', 'orange', 'banana', 'cherry']


fruits = ['apple', 'banana', 'cherry'] # existinglist. It could be empty as well
addOneEle(fruits)


# IMP INFO:
'''
1--->
Return Value from insert() ::::::::
The insert() method doesn't return anything; returns None. It only updates the current list.
It also supoort negative index.
If the index value is greater than or equal to the length of the list, the new element will be added to the end of the list. 


2 ---> 
        List Insert(): Definition and Use :::::::
        List Insert() function in Python is very useful to insert an element in a list. What makes it different from append() is that the list insert() function can add the value at any position in a list, whereas the append function is limited to adding values at the end.

        It is used in editing lists with huge amount of data, as inserting any missed value in that list is made very easy with this Python function.

3---> USEFUL links for HOW it python handle when we insert element which index is out of range. It act like a append method:

        https://stackoverflow.com/questions/25840177/list-insert-at-index-that-is-well-out-of-range-behaves-like-append
        https://code.activestate.com/lists/python-dev/132588

        a.insert(len(a), x) is equivalent to a.append(x). OR more precisely --> if index >=len(list) then it behave as list.append(ele)
        SOurce : https://docs.python.org/2/tutorial/datastructures.html

        other Ref : https://www.prepbytes.com/blog/python/insert-function-in-python/


'''
