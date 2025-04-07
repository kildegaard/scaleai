// Import required modules
const fs = require('fs');
const WebSocket = require('ws');
const wss = new WebSocket.Server({ port: 8080 });

// Initialize the log file path and the last modified timestamp
const logFilePath = 'cosa.log';
let lastModified = null;

// Function to check for log file changes
function checkForChanges() {
  // Get the current modified timestamp of the log file
  const stats = fs.statSync(logFilePath);
  const currentModified = stats.mtimeMs;

  // If this is the first check or the log file has been modified
  if (lastModified === null || currentModified > lastModified) {
    // Update the last modified timestamp
    lastModified = currentModified;

    // Read the log file and send the new content to all connected clients
    const logContent = fs.readFileSync(logFilePath, 'utf8');
    wss.clients.forEach((client) => {
      if (client.readyState === WebSocket.OPEN) {
        client.send(logContent);
      }
    });
  }
}

// Check for log file changes every second
setInterval(checkForChanges, 1000);