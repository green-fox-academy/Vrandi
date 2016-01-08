'use strict';

function Student() {
	this.grades = [];
	this.addGrade = function(grade) {
		this.grades.push(grade);
	};
	this.getAverage = function() {
		return this.grades.reduce((a, b) => a + b) / this.grades.length;
	};
}



var juci = new Student();
juci.addGrade(3);
juci.addGrade(4);
juci.addGrade(5);
juci.addGrade(5);
console.log(juci.getAverage());
