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