'use strict';

var numbers = [7, 8, -1, 4, 3, 12]
var min = numbers.reduce(function(x, y) { return x < y ? x : y })
var max = numbers.reduce(function(x, y) { return x > y ? x : y })
console.log(min)
console.log(max)