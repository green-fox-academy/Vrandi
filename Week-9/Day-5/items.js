'use strict';

var mysql = require('mysql');
var connection = mysql.createConnection({
  host: 'localhost',
  user: 'test2',
  password: 'mackocska',
  database: 'todo'
});

connection.connect();

function addItem(text, cb) {
  dataBaseCommand(['INSERT INTO todo SET text= ?', text], cb);
}

function getItems(cb) {
  dataBaseCommand(['SELECT * FROM todo'], cb);
}

function update(id, cb) {
  dataBaseCommand(['UPDATE todo SET completed=\'true\' WHERE todo_id= ?', id], cb);
}

function deleteItem(id, cb) {
  dataBaseCommand(['DELETE FROM todo WHERE todo_id= ?', id], cb);
}


function dataBaseCommand(sqlcommand, cb) {
  if (sqlcommand.length > 1) {
    connection.query(sqlcommand[0], sqlcommand[1], function(err, result) {
      if (err) throw err;
      cb(result);
    });
  } else {
    connection.query(sqlcommand[0], function(err, result) {
      if (err) throw err;
      cb(result);
    });
  }
}

module.exports = {
  getItems: getItems,
  addItem: addItem,
  update: update,
  deleteItem: deleteItem
}