'use strict';

var myArray = [1, 2, 3, 4, 5];

function printElem(e) {
	console.log(e);
}

myArray.forEach(printElem);
myArray.forEach(function(e) { console.log(e*10); })