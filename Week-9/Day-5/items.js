'use strict';

var mysql = require('mysql');
var connection = mysql.createConnection({
  host: 'localhost',
  user: 'test2',
  password: 'mackocska',
  database: 'todo'
});

connection.connect();

function addTodo(text, cb) {
  connection.query('INSERT INTO todo SET text= ?', text, function(err, result) {
    if (err) throw err;
    cb(result);
  })
}

function getAllItem(cb) {
  connection.query('SELECT * FROM todo', function(err, result) {
    if (err) throw err;
    cb(result);
  })
}

function updateItem(id, cb) {
  connection.query('UPDATE todo SET completed=\'true\' WHERE todo_id= ?', id, function(err, result) {
    if (err) throw err;
    cb(result);
  })
}

function deleteItem(id, cb) {
  connection.query('DELETE FROM todo WHERE todo_id= ?', id, function(err, result) {
    if (err) throw err;
    cb(result);
  })
}

module.exports = {
  add: addTodo,
  get: getAllItem,
  update: updateItem,
  del: deleteItem
}