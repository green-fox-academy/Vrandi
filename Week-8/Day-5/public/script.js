'use strict';

function TodoApp() {
  var _this = this;
  this.addItemButton = document.querySelector('.add-item-button');
  this.input = document.querySelector('.input');
  this.todoItems = document.querySelector('.todo-elements');
  this.url = 'http://localhost:3000/todos';


  this.addItemButton.addEventListener('click', function() {
    _this.addItem();
  });

  this.refresh = function() {
    createRequest('GET', _this.url, {}, _this.listCallback);
  };

  this.listCallback = function(response) {
    var todoArray = JSON.parse(response);
    todoArray.forEach(function(todoItem) {
      var newItem = document.createElement('div');
      newItem.innerText = todoItem.text;
      _this.todoItems.appendChild(newItem);
    });
  };

  this.addItem = function() {
    var textareaInput = this.input.value;
    var newTodo = JSON.stringify({text: textareaInput});
    createRequest('POST', _this.url, newTodo, _this.createTodoCallback);
  };

  this.createTodoCallback = function(response) {
    _this.refresh();
  }

}

var todoapp = new TodoApp();
todoapp.refresh();

/*
var newTodo = JSON.stringify({text: 'hali'});


createRequest('POST', url, newTodo, createTodoCallback);

var update = JSON.stringify({ "completed": "true" })
createRequest('PUT', urlupdate, update, createTodoCallback);


createRequest('DELETE', urldelete, {}, createTodoCallback);
*/