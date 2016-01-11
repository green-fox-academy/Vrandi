'use strict';

function Gallery(pictureArray) {
	var _this = this;
	this.pictures = pictureArray;
	this.currentPictureNumber = 0;
	this.leftButton = document.querySelector('.left');
	this.rightButton = document.querySelector('.right');
	this.changingPicture = document.querySelector('.picturechanger');
	this.thumbnails = document.querySelector('.thumbnails');
	

	this.leftButton.addEventListener('click', function() {
		_this.leftEvent();
	});

	this.rightButton.addEventListener('click', function() {
		_this.rightEvent();
	});

	this.thumbnails.addEventListener('click', function(event) {
  	if (event.target.src) {
    	_this.changingPicture.setAttribute('src', event.target.src);
  	}
	});

	this.leftEvent = function() {
		if (this.currentPictureNumber === 0) {
			this.currentPictureNumber = this.pictures.length;
		}
		this.currentPictureNumber --;
		this.changingPicture.setAttribute('src', this.pictures[this.currentPictureNumber]);
	};

	this.rightEvent = function() {
		if (this.currentPictureNumber === this.pictures.length-1) {
			this.currentPictureNumber = 0;
		}
		this.currentPictureNumber ++;
		this.changingPicture.setAttribute('src', this.pictures[this.currentPictureNumber]);
	};

	this.createThumbnails = function() {
		for (var i = 0; i < this.pictures.length; i++) {
			var a = this.createReference();
			var image = this.createImage(a, i);
		}
	};

	this.createReference = function() {
		var a = document.createElement('a');
		a.setAttribute('href', '#');
		this.thumbnails.appendChild(a);
		return a;
	};

	this.createImage = function(referencetag, index) {
		var image = document.createElement('img');
		image.setAttribute('src', this.pictures[index]);
		referencetag.appendChild(image);
		return image;
	};

	this.createThumbnails();
}

var pictures = [
	'images/1.jpg',
	'images/2.jpg',
	'images/3.jpg',
	'images/4.jpg',
	'images/5.jpg',
	'images/6.jpg',
	'images/7.jpg',
	'images/8.jpg',
	'images/9.jpg'
];

var gallery = new Gallery(pictures);
