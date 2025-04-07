I’m adding security alerts to a smart home system and need to document the JS code for detecting breaches and sending alerts. Can you walk me through how it monitors sensors, processes alerts and talks to the UI?

```javascript
function initializeSecuritySystem() {
    const securitySystem = new SecuritySystem();
    securitySystem.on('breachDetected', (alert) => {
        processAlert(alert);
    });
    securitySystem.on('sensorStatusUpdated', (status) => {
        updateSensorStatus(status);
    });
    securitySystem.startMonitoring();
}

function processAlert(alert) {
    console.log('Processing security alert:', alert);
    // Implementation for processing security alerts
}

function updateSensorStatus(status) {
    console.log('Updating sensor status:', status);
    // Implementation for updating sensor status on UI
}

class SecuritySystem {
    constructor() {
        this.listeners = {};
        this.sensors = [
            { id: 'doorSensor', status: 'secure' },
            { id: 'windowSensor', status: 'secure' },
            { id: 'motionSensor', status: 'inactive' }
        ];
    }

    on(event, listener) {
        this.listeners[event] = listener;
    }

    startMonitoring() {
        console.log('Starting security monitoring...');
        // Simulate security monitoring
        setInterval(() => {
            const alert = this.detectBreach();
            if (alert && this.listeners['breachDetected']) {
                this.listeners['breachDetected'](alert);
            }
        }, 3000);
    }

    detectBreach() {
        const breachDetected = Math.random() < 0.1;
        if (breachDetected) {
            return {
                sensor: 'doorSensor',
                type: 'door opened',
                timestamp: new Date()
            };
        }
        return null;
    }

    updateSensor(sensorId, status) {
        const sensor = this.sensors.find(s => s.id === sensorId);
        if (sensor) {
            sensor.status = status;
            if (this.listeners['sensorStatusUpdated']) {
                this.listeners['sensorStatusUpdated'](sensor);
            }
        }
    }
}

document.querySelector('#arm-system-button').addEventListener('click', () => {
    console.log('Arming security system...');
    // Implementation to arm the system
});

document.querySelector('#disarm-system-button').addEventListener('click', () => {
    console.log('Disarming security system...');
    // Implementation to disarm the system
});

// Function to simulate sensor update
function simulateSensorUpdate() {
    securitySystem.updateSensor('windowSensor', 'breached');
}

document.querySelector('#simulate-sensor-button').addEventListener('click', simulateSensorUpdate);

const securitySystem = new SecuritySystem();
```