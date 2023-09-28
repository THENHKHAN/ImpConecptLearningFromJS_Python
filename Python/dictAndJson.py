# https://www.w3schools.com/python/python_json.asp


import json

print("*************** 0  Dictionary *****************************")
data = {"a" : 2 , "b" : 4 , "c" : 8}
print(f" dict  :  {data}")
print(f" type(data)  :  {type(data)}")
# OUTPUT
'''
 dict  :  {'a': 2, 'b': 4, 'c': 8}
 type(data)  :  <class 'dict'>

'''
print("*************** 1  string *****************************")

String = '{"x": 2 , "b" : 4 , "c": "new york"}'
print(f" jsonString  :  {String}") #  {1 : 2 , 'b : 4 , c : False}: Since  False is False: this means  it is a string 
print(f" jsonString  :  {type(String)}")  

#  see the value False value.
print("*************** 2 - json -> Dict *****************************")
# some JSON:
JsonString =  '{"name":"John", "age":30, "city":"LKO"}'
Dict = json.loads(JsonString) # jsonObj  : is a json object but if you print type then it will show str since its format is string  
print(f" Dict  :  {Dict}")
print("specific value base on key : " , Dict["city"])
print(f" type(data)  :  {type(Dict)}") # Since  False is false: 


print("*************** 3 - Dict -> json *****************************")

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": True
}

# convert into JSON:
JsonString = json.dumps(x) 
                      
# the result is a JSON string:   {"name": "John", "age": 30, "city": true}
print(JsonString) # see the True will get true