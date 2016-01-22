'use strict';

function TodoApp() {
  var _this = this;
  this.addItemButton = document.querySelector('.add-item-button');
  this.input = document.querySelector('.input');
  this.todoItems = document.querySelector('.todo-elements');
  this.url = 'http://localhost:3000/todos';


  this.addItemButton.addEventListener('click', function() {
    if (_this.input.value != '') {
      _this.addItem();
    }
    _this.input.value = '';
  });

  this.refresh = function() {
    this.todoItems.innerText = '';
    createRequest('GET', _this.url, null, _this.listCallback);
  };

  this.listCallback = function(response) {
    var todoArray = JSON.parse(response);
    todoArray.forEach(function(todoItem) { _this.createItem(todoItem); });
  };

  this.createItem = function(todoItem) {
    var newItem = document.createElement('div');
    newItem.innerText = todoItem.text;
    newItem.setAttribute('class', todoItem['completed']);
    newItem.setAttribute('id', todoItem.todo_id);
    newItem.addEventListener('click', _this.addButtons);
    _this.todoItems.appendChild(newItem);
  };

  this.addItem = function() {
    var newTodo = JSON.stringify({text: _this.input.value});
    createRequest('POST', _this.url, newTodo, _this.createTodoCallback);
  };

  this.createTodoCallback = function(response) {
    _this.refresh();
  };

  this.addButtons = function() {
    _this.existButton();
    var status = event.target.className;
    if (status === 'true') {
      _this.addDeleteButton();
    } else {
      _this.addCompleteButton();
      _this.addDeleteButton();
    }
  };

  this.existButton = function() {
    if (document.querySelector('.delete-button')) {
      document.querySelector('.delete-button').remove();

    }
    if (document.querySelector('.complete-button')) {
      document.querySelector('.complete-button').remove();
    }
  };

  this.addDeleteButton = function() {
    var deleteButton = document.createElement('button');
    deleteButton.innerText = 'x';
    deleteButton.setAttribute('class', 'delete-button');
    event.target.appendChild(deleteButton);
    deleteButton.addEventListener('click', _this.deleteItem);
  };

  this.addCompleteButton = function() {
    var completeButton = document.createElement('button');
    completeButton.innerText = 'done';
    completeButton.setAttribute('class', 'complete-button');
    event.target.appendChild(completeButton);
    completeButton.addEventListener('click', _this.changeStatusToComplete);
  };

  this.changeStatusToComplete = function() {
    var url = _this.url + '/' + event.target.parentNode.id;
    createRequest('PUT', url, null, _this.createTodoCallback);
  };

  this.deleteItem = function() {
    var url = _this.url + '/' + event.target.parentNode.id;
    createRequest('DELETE', url, null, _this.createTodoCallback);
  };

}

var todoapp = new TodoApp();
todoapp.refresh();
