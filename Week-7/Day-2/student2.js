'use strict';

function Student() {
	this.grades = {};
	this.addGrade = function(subject, grade) {
		if (!(subject in this.grades)) {
			this.grades[subject] = [];
		} 
		this.grades[subject].push(grade);
	};

	this.getCount = function() {
		var countGrades = {};
		for (var key in this.grades) {
			countGrades[key] = this.grades[key].length;
		}
		return countGrades;
	};

	this.getAverage = function() {
		var grades = this.getAllGrades();
		return grades.reduce((a, b) => a + b) / grades.length;
	};

	this.getAverageBySubject = function() {
		var averageGrades = {};
		for (var key in this.grades) {
			var sum = this.grades[key].reduce((a, b) => a + b);
			var len = this.grades[key].length;
			averageGrades[key] = sum / len;
		}
		return averageGrades;
	};

	this.getAllGrades = function() {
		var allGrades = [];
		for (var key in this.grades) {
			this.grades[key].forEach(function(e) { allGrades.push(e); });
		}
		return allGrades;
	}
}


var laca = new Student();
laca.addGrade('matek', 5);
laca.addGrade('matek', 4);
laca.addGrade('matek', 4);
laca.addGrade('rajz', 1);
laca.addGrade('rajz', 3);
console.log(laca.getCount()); // {'rajz': 2, 'matek': 3}
console.log(laca.getAverage()); // 3.4

//szorgalmi
console.log(laca.getAverageBySubject());