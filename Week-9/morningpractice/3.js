'use strict';

var kids = [
  {name: 'Julika', age: 8, sex: 'female'},
  {name: 'Tiborka', age: 7, sex: 'male'},
  {name: 'Zsolti', age: 6, sex: 'male'},
  {name: 'Gerda', age: 9, sex: 'female'},
  {name: 'Zsomborka', age: 8, sex: 'male'}
];


function filterNamesBySex(kids, gender) {
  return kids.
  filter(function(kid) {
   return kid.sex === gender;
  }).
  map(function(kid) {
    return kid.name;
  });
}

console.log(filterNamesBySex(kids, 'female'));