'use strict';

function range(num) {
	var array = [];
	for (var i = 0; i < num; i++) {
		array.push(i);
	}
	return array;
}

var array = range(5);
console.log(array);