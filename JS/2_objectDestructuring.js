/*

Object destructuring is a feature available in several programming languages, including JavaScript and Python. It allows you to extract specific properties or elements from objects and assign them to variables in a more concise and readable way.
-->Remark: In python , dictionary will be called object.
JavaScript Example:
 
 */



// Object destructuring in JavaScript
const person = { firstName: 'John', lastName: 'Doe', age: 30 };

// Extract specific properties into variables
const { firstName, lastName } = person; // firstName , lastName must be same as key of the object.
// now firstName is equavlent to person.firstName which gives john as value
console.log(firstName); // Output: 'John'
console.log(lastName);  // Output: 'Doe'
