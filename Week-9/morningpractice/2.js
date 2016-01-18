'use strict';

var kids = [
  {name: 'Julika', age: 8, sex: 'female'},
  {name: 'Tiborka', age: 7, sex: 'male'},
  {name: 'Zsolti', age: 6, sex: 'male'},
  {name: 'Gerda', age: 9, sex: 'female'},
  {name: 'Zsomborka', age: 8, sex: 'male'}
];

function countByAge(kids, age) {
  return kids.reduce((acc, kid) => kid.age === age ? acc + 1 : acc + 0, 0);
}

console.log(countByAge(kids, 8));

function getAges(kids) {
  return kids.map(function(kid) { return kid.age; });
}

console.log(getAges(kids));

function getTheLongestNameAge(kids) {
  return kids.reduce((kid1, kid) => kid1.name.length > kid.name.length ? kid1 : kid).age;
}

console.log(getTheLongestNameAge(kids));