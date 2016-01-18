'use strict';

var kids = [
  {name: 'Julika', age: 8, sex: 'female'},
  {name: 'Tiborka', age: 7, sex: 'male'},
  {name: 'Zsolti', age: 6, sex: 'male'},
  {name: 'Gerda', age: 9, sex: 'female'},
  {name: 'Zsomborka', age: 8, sex: 'male'}
];


function getAgeByName(kids, name) {
  return kids.reduce((a, b) => a.name === name ? a : b).age;
}

console.log(getAgeByName(kids, 'Gerda'));