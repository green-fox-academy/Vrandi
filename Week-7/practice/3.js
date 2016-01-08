'use strict';

function range(start, end, step) {
	var array = [];
	if (start < end) {
		for (var i = start; i < end; i += step) {
			array.push(i);
		}
	} else {
		for (var i = start; i > end; i += step) {
			array.push(i);
		}
	}
	return array;
}

var array = range(3, 7, 2);
var array2 = range(8, 4, -1);
console.log(array);
console.log(array2);