
var express = require('express');
var app = express();
var server = require('http').createServer(app);
var allowedOrigins = "*:*";

var io = require('socket.io').listen(server, {origins:allowedOrigins});
var fs = require('fs');

server.listen(process.env.PORT || 5000);

/*function handler (req, res) {
  fs.readFile(__dirname + '/index.html',
  function (err, data) {
    if (err) {
      res.writeHead(500);
      return res.end('Error loading index.html');
    }

    res.writeHead(200);
    res.end(data);
  });
}*/

io.on('connection', function (socket) {
  console.log("Client connected");
  console.log(Object.keys(io.engine.clients))
  socket.on('disconnect', function(){
    console.log("disconnected client!");
  });
  socket.on('lighton', function (data) {
    console.log("send data to other clients");
    io.emit('led');
  });

});
