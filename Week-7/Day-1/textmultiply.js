'use strict';

function textMultiply(text, num) {
  var result = '';
  for (var i = 0; i < num; i++) {
	result += text;
  }
  return result;
}

console.log(textMultiply('alma', 3));

function textmultiply2(text, num) {
  if (num === 1) {
  	return text;
  } else {
    return text + textmultiply2(text, num-1);
  }
}

console.log(textmultiply2('alma', 3));

function textMultiply3(text, num) {
	return num ? text + textMultiply3(text, num-1) : '';
}

console.log(textMultiply3('alma', 3));
