const fs = require('fs');
const express = require('express');
const app = express();
const server = require('http').createServer(app);
const io = require('socket.io')(server);

// Specify the log file to monitor
const logFile = './log.txt';

// Set up the server to listen on port 3000
server.listen(3000, () => {
  console.log('Server listening on port 3000');
});

// Use the `fs.watch` function to monitor the log file for changes
fs.watch(logFile, (event, filename) => {
  if (event === 'change') {
    // Read the log file contents when a change is detected
    fs.readFile(logFile, 'utf8', (err, data) => {
      if (err) {
        console.error(err);
      } else {
        // Emit the log data to connected clients
        io.emit('log update', data);
      }
    });
  }
});

// Set up the Socket.IO connection
io.on('connection', (socket) => {
  console.log('Client connected');

  // Send the initial log data to the client
  fs.readFile(logFile, 'utf8', (err, data) => {
    if (err) {
      console.error(err);
    } else {
      socket.emit('log update', data);
    }
  });

  // Handle client disconnection
  socket.on('disconnect', () => {
    console.log('Client disconnected');
  });
});