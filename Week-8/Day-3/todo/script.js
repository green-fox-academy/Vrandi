'use strict';

var url = 'https://mysterious-dusk-8248.herokuapp.com/todos';
var todoContainer = document.querySelector('.todo-container');

var listCallback = function(response) {
  var todoArray = JSON.parse(response);
  todoArray.forEach(function(todoItem) {
    var newItem = document.createElement('p');
    newItem.innerText = todoItem.text;
    todoContainer.appendChild(newItem);
  });
}

var refresh = function() {
  createRequest('GET', url, {}, listCallback);
}

refresh();

var newTodo = JSON.stringify({text: 'hali'});
var createTodoCallback = function(response) {
  refresh();
}

createRequest('POST', url, newTodo, createTodoCallback);
