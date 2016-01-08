'use strict';

//1

function Multiply(num) {
	var output = '';
	for (var i = 1; i <= 10; i++) {
		output += num+ ' * '+ i + ' = ' + num * i + '\n';
	}
	return output;
}


function MultiplicationTable() {
	for (var i = 1; i <= 10; i ++) {
		console.log(Multiply(i));
	}
}

//MultiplicationTable();

//2

function recSzorozo(number, i) {
	if (i < 10) {
		return '';
	}
	return number + ' * ' + i + ' = ' + number * i + '\n' + recSzorozo(number, i + 1);
}

//console.log(recSzorozo(4, 1));

// 3 map

var szamok = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

var szorzotabla = '';

var sorok = szamok.map(function(e) { return e + '*' + 4 + '=' + e * 4; });

szorzotabla = sorok.join('\n');
console.log(szorzotabla)