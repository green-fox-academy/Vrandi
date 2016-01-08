'use strict';

//reduce a listabol csinal valami mast pl. egy tombot leredukal egy szamra

var numbers = [5, 6, 3, 9];

var sum = numbers.reduce(function(acc, num) { return acc + num }, 0);
console.log(sum);