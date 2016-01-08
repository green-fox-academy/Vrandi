'use strict';

var numbers = [1, 2, 3, 4, 5, 6];
var sum = numbers.reduce(function(x, y) { return x + y });
console.log(sum);