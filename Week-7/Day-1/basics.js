'use strict'; // igy nem enged meg annyi mindent-- ezt mingig tegyuk

/*
var a = 123;
a *= 2;
a++; // ahol csinaljuk ott meg nem novelodik meg, csak egz sorral kesobb a += 1 meg azonnal megnoveli
a--;

console.log(a);

var myArray = [1, 2, 3, 4];
console.log(myArray[3]);
console.log(myArray[7]); //nem sir ha nincs ilyen hosszusag hanem undefined
console.log(myArray.length);

*/

/*

var a = 1;
if (a % 2 === 0) {
  console.log('paros');
} else {
  console.log('paratlan');
}

*/
/*

//switch

var a = 2;

switch (a) {
  case 0:
    console.log('nulla');
    break
  case 1:
    console.log('egy');
    break
  default:
    console.log('sok')
}
*/

/*
var i = 0
while (i <= 10) {
  console.log(i++);
  if (i === 4) {
  	break;
  }
}
*/

for (var i = 0; i < 5; i++) {
  console.log(i);
};

var array = ['kecske', 'dinnye', 'valami'];

for (var i = 0; i < array.length; i++) {
  console.log(array[i]);
}

var student = {
	kor: 6, 
	nev: 'tibi', 
	labmeret: 45
};

for (var key in student) {
  console.log(key);
  console.log(student[key]);
}