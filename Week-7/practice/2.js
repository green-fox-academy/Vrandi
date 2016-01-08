'use strict';

function range(start, end) {
	var array = [];
	for (var i = start; i < end; i++) {
		array.push(i);
	}
	return array;
}

var array = range(3, 7);
console.log(array);