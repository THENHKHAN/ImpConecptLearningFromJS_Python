/*
--> Destructuring is a programming concept used in several languages, including JavaScript, Python, and
     more, to extract values from objects, arrays, or other iterable data structures. 
     It allows you to unpack data into distinct variables or properties, 
     making it easier to work with the individual components of complex data structures.

Here's a brief overview of destructuring in a few popular programming languages:

JavaScript: JavaScript introduced destructuring in ECMAScript 6 (ES6).
 It allows you to extract values from arrays and objects into variables easily. For example:

 IMP=> The typeof operator returns "object" for objects, arrays, and null,Arrray because in JavaScript arrays are objects.

==>REST=>  when ... three dot prifix used in the paramter of function definition then called REST Operator/parameter. It rcv argumrnt as array.

==>SPREAD=>  when ... three dot prifix used like below means unpacking or destrucuring called spread operator.
they do the same thing they have different name bcz of where they are getting used.
NOTE: they can call interchangebly

spread operator , you can think of combining two array. 
EX:
const a1 = [1,2,3] 
const a2 = [4,5]

a3 = [...a1,...a2 ] // [1,2,3,4] 
// but if we used without rest operator
a4 =[a1,a2] //  [ [1,2,3] ,[4,5]]
console.log(a3);
console.log(a4);
OUTPUT:
[ 1, 2, 3, 4, 5 ]
[ [ 1, 2, 3 ], [ 4, 5 ] ]

Here are the main differences:

The spread operator (...) unpacks the elements of an iterable object.
The rest parameter (...) packs the elements into an array.
 */ 

const arr = [1,2,4,6,8,9]

console.log(arr)
console.log(typeof(arr))
console.log("***** Destructuring of array    ********");

const [one , two , , six] = arr;

console.log(`ONE ->  ${one}`);
console.log(`TWO ->  ${two}`);
console.log(`six ->  ${six}`);

console.log("***** Destructuring of array  with SPread operator   ********");
// Spread an array into individual elements. Imp: only once ... will be used i.e. at the time of assigning and rest time only variable name
const numbers = [1, 2, 3 ,7 , 6 , 10 ,78 , 100];
const [...rest] = numbers
console.log("NUMBER:  " , numbers); // Output: 1 2 3 : means unpacked and not  [1 2 3] 
console.log("spredOp:  " , rest);
console.log("type of numbers" , typeof(numbers)) // object since array
console.log("type of spredOp" , typeof(spredOp)) // object since array



const [ , n2 , , , n6 , ...restNumber] = numbers // we left blankfor 1 , 3, 5 and except 2,6 we stored the value in  ...restNumber.
console.log(`number2 : ${n2}` );
console.log(`number6 : ${n6}` );
console.log("RestValue after 6 : " ,restNumber); // [ 10, 78, 100 ]

// example:
function sum(...args) {  // argd = [1,2,3]
     let total = 0;
     for (const a of args) {
         total += a;
     }
     return total;
 }
 
 sum(1, 2, 3); // 6

