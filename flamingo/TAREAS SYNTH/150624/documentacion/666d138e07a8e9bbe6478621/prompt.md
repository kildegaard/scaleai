Can you help me write some documentation for this code? It writes different types of log messages to system.log using Node.js. The logs can be either events or errors. There are functions to log system events and errors. What do each function do and how does the logging work?

```javascript
const fs = require('fs');
const path = require('path');
const LOG_FILE = path.join(__dirname, 'system.log');

const logEvent = (type, message) => {
    const timestamp = new Date().toISOString();
    const logMessage = `${timestamp} - ${type.toUpperCase()}: ${message}\n`;
    
    fs.appendFile(LOG_FILE, logMessage, (err) => {
        if (err) {
            console.error('Error writing to log file:', err);
        }
    });
};

const logSystemEvent = (message) => {
    logEvent('event', message);
};

const logError = (message) => {
    logEvent('error', message);
};

// Example usage
logSystemEvent('System initialized');
logSystemEvent('User login successful');
logError('Failed to connect to database');
logSystemEvent('User logged out');
logSystemEvent('Backup completed successfully');
logError('Unexpected shutdown detected');

console.log('Logging completed. Check the system.log file for details.');
```