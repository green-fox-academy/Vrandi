'use strict';

var mysql = require('mysql');
var connection = mysql.createConnection({
  host: 'localhost',
  user: 'test2',
  password: 'mackocska',
  database: 'todo'
});

connection.connect();

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
  databaseReq : dataBaseCommand
}