'use strict';

var express = require("express");
var bodyParser = require("body-parser");
var items = require("./items.js");

var app = express();


app.use(logRequest);
app.use(express.static("public"));
app.use(bodyParser.json());

// GET /todos => list all todo items
app.get("/todos", function (req, res) {
  items.databaseReq(['SELECT * FROM todo'], function(result) {
    res.json(result);
  });
});

// POST /todos => create a new todo item
app.post("/todos", function (req, res) {
  items.databaseReq(['INSERT INTO todo SET text= ?', req.body.text], function(result){
    res.json(result);
  });
});

// PUT /todos/1 => edit a todo item
app.put("/todos/:id", function (req, res) {
  items.databaseReq(['UPDATE todo SET completed=\'true\' WHERE todo_id= ?', req.params.id], function(result) {
    res.json(result);
  });
});


// DELETE /todos/1 => remove a todo item
app.delete("/todos/:id", function (req, res) {
  items.databaseReq(['DELETE FROM todo WHERE todo_id= ?', req.params.id], function (item) {
    res.json(item);
  });
});


app.listen(3000, function () {
  console.log("Listening on port 3000...")
});


function logRequest(req, res, next) {
  var parts = [
    new Date(),
    req.method,
    req.originalUrl,
  ];
  console.log(parts.join(" "));

  next();
}


