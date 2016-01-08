'use strict';

function Car(color, type, km) { // construktort mindig nagy betuvel
	this.color = color;
	this.type = type;
	this.km = km;
	this.ride = function(km) {
		this.km += km;
	}
}

var golf = new Car('kopott piros', '1es Golf', 1e10); // nem szabad lefelejteni a newt

golf.ride(400);
console.log(golf.km);

// Tojas vallasa (nincs benne this-- kisebb a hibaforras)

function createCar(color, type, km) {
	return {
		color: color,
		type: type,
		km: km,
		ride: function(km) {
			this.km += km;
		}
	}
}

var volvo = createCar('zold', 'Volvo', 500);

volvo.ride(50);
console.log(volvo.km);