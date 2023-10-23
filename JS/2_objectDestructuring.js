/*
REF : https://www.javascripttutorial.net/es6/javascript-object-destructuring/

Object destructuring is a feature available in several programming languages, including JavaScript and Python. It allows you to extract specific properties or elements from objects and assign them to variables in a more concise and readable way.
-->Remark: In python , dictionary will be called object.
JavaScript Example:
 
 */



// Object destructuring in JavaScript
const person = { firstName: 'John', lastName: 'Doe', age: 30 };

// Extract specific properties into variables
const { firstName, lastName } = person; // firstName , lastName must be same as key of the object.
// but if you want to give different name thne use : let { firstName: fname, lastName: lname } = person; now you can access with fname and lname.
// In this example, the firstName and lastName properties are assigned to the fName and lName variables respectively.

// generalize: let { property1: variable1, property2: variable2 } = object;
//  The identifier before the colon (:) is the property of the object and the identifier after the colon is the variable.
// REMARK : 1st way is prefereable i.e. same varibale as the object property.Bcz it more concise

// now firstName is equavlent to person.firstName which gives john as value
console.log(firstName); // Output: 'John'
console.log(lastName);  // Output: 'Doe'



/**
 
Summary
Object destructuring assigns the properties of an object to variables with the same names by default.

for more info read :::::::::::::
https://www.javascripttutorial.net/es6/javascript-object-destructuring/

   */