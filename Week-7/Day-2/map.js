'use strict';

var benaSzavak = [
	'kuty',
	'macsk',
	'alm',
	'kacs'
];

var faszaSzavak = [];

benaSzavak.forEach(function(szo) { faszaSzavak.push(szo + 'a'); });

console.log(faszaSzavak);

var faszaSzavak2 = benaSzavak.map(function(szo) { return szo + 'a' }); // vegig megy a tomb elemein es megcsinalja a muveletet a tomb egyes elemein
console.log(faszaSzavak2);
console.log(benaSzavak);

