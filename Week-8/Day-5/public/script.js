'use strict';

function TodoApp() {
  var _this = this;
  this.addItemButton = document.querySelector('.add-item-button');
  this.input = document.querySelector('.input');
  this.todoItems = document.querySelector('.todo-elements');
  this.url = 'http://localhost:3000/todos';


  this.addItemButton.addEventListener('click', function() {
    _this.addItem();
    _this.input.value = '';
  });

  this.refresh = function() {
    this.todoItems.innerText = '';
    createRequest('GET', _this.url, null, _this.listCallback);
  };

  this.listCallback = function(response) {
    var todoArray = JSON.parse(response);
    todoArray.forEach(function(todoItem) {
      var newItem = document.createElement('div');
      newItem.innerText = todoItem.text;
      newItem.setAttribute('class', todoItem['completed']);
      newItem.setAttribute('id', todoItem.id);
      newItem.addEventListener('click', _this.addButtons);
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
    var parent = event.target.parentNode;
    var id = parent.id;
    var text = parent.innerText.substring(0, (parent.innerText).length-5);
    var url = _this.url + '/' + id;
    var update = JSON.stringify({ "completed": "true" , "text": text});
    createRequest('PUT', url, update, _this.createTodoCallback);
  };

  this.deleteItem = function() {
    var id = event.target.parentNode.id;
    var url = _this.url + '/' + id;
    createRequest('DELETE', url, null, _this.createTodoCallback);
  };

}

var todoapp = new TodoApp();
todoapp.refresh();
