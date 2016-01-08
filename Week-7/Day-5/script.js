'use strict';

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


var currentPictureNumber = 0

var left = document.querySelector('.left');
var right = document.querySelector('.right');
var pictureChanger = document.querySelector('.picturechanger');
var thumbnails = document.querySelector('.thumbnails')
createThumbnails();

left.addEventListener('click', function() {
	leftEvent();
})

right.addEventListener('click', function() {
	rightEvent();
})

thumbnails.addEventListener('click', function(event) {
  if (event.target.src) {
    pictureChanger.setAttribute('src', event.target.src);
  }
});

function leftEvent() {
	if (currentPictureNumber === 0) {
		currentPictureNumber = pictures.length;
	}
	currentPictureNumber --;
	pictureChanger.setAttribute('src', pictures[currentPictureNumber]);
}

function rightEvent() {
	if (currentPictureNumber === pictures.length-1) {
		currentPictureNumber = 0;
	}
	currentPictureNumber ++;
	pictureChanger.setAttribute('src', pictures[currentPictureNumber]);
}

function createThumbnails() {
	for (var i = 0; i < pictures.length; i++) {
		var a = createReference();
		var image = createImage(a, i);
	}
}

function createReference() {
	var a = document.createElement('a');
	a.setAttribute('href', '#');
	thumbnails.appendChild(a);
	return a;
}

function createImage(referencetag, index) {
	var image = document.createElement('img');
	image.setAttribute('src', pictures[index]);
	referencetag.appendChild(image);
	return image;
}


