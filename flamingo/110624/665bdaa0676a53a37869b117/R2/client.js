// Create a WebSocket connection to the server
const socket = new WebSocket('ws://localhost:8080');

// Function to handle incoming log data from the server
socket.onmessage = (event) => {
  const logContent = event.data;
  const logLines = logContent.split('\n');

  // Display the log lines in the browser console or a UI component
  logLines.forEach((logLine) => {
    console.log(logLine);
  });
};

// Handle WebSocket connection errors
socket.onerror = (event) => {
  console.error('Error occurred while connecting to the WebSocket server:', event);
};

// Handle WebSocket connection closure
socket.onclose = () => {
  console.log('Disconnected from the WebSocket server.');
};