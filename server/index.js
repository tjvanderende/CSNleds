
var express = require('express');
var app = express();
var server = require('http').createServer(app);
var allowedOrigins = "*:*";

var io = require('socket.io').listen(server, {origins:allowedOrigins});
var fs = require('fs');

server.listen(process.env.PORT || 5000); // luister op poort 5000 tenzij anders aangegeven via de opties in Heroku.

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

/**
 * Connectie gemaakt
 */
io.on('connection', function (socket) {
  console.log("Client connected"); 
  console.log(Object.keys(io.engine.clients)); // print connected clients (voor debug).
  socket.on('disconnect', function(){ // kijk of een connectie is verbroken
    console.log("Client disconnected");
  });
  /**
   * Ontvang data
   */
  socket.on('led_value', function (data) {
    console.log(data);
    // stuur dit aan alle clients door BEHALVE de client waar het pakketje led_value weg komt!
    socket.broadcast.emit('led_value', data); // { led: id van ledje, status: 1 == aan, 0 == uit }
  });

});
