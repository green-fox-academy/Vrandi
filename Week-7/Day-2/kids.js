'use strict';

var kids = [
	{name: 'Tibor', candies: 2},
	{name: 'Jozsi', candies: 3},
	{name: 'Agoston', candies: 0},
	{name: 'Aurel', candies: 7},
	{name: 'Zakarias', candies: 4}
];


function getTheRichestKidsName(kids) {
	return kids.reduce((x, y) => x.candies > y.candies ? x : y ).name;
}

console.log(getTheRichestKidsName(kids)); 