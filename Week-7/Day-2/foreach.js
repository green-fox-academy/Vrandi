'use strict';

var dogs = [
	'Morzsi',
	'Zsemle',
	'Tappancs',
	'Lady'
];

//masodik parameter ay index, a harmadik az egesz tomb

dogs.forEach(function(e, i, arr) {
	console.log(e, i, arr);
});