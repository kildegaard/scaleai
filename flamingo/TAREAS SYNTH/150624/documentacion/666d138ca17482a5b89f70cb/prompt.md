I’m building an energy management system that gives recommendations based on usage. Can you help me with the JavaScript code that crunches the usage data, makes the recommendations and shows them to the user?

```javascript
function initializeEnergyManagement() {
    const energyManager = new EnergyManager();
    energyManager.on('recommendationGenerated', (recommendation) => {
        displayRecommendation(recommendation);
    });
    energyManager.on('usageDataUpdated', (usage) => {
        updateUsageData(usage);
    });
    energyManager.startAnalysis();
}

function displayRecommendation(recommendation) {
    console.log('Energy Saving Recommendation:', recommendation);
    // Implementation for displaying recommendations to user
}

function updateUsageData(usage) {
    console.log('Updating usage data:', usage);
    // Implementation for updating usage data on UI
}

class EnergyManager {
    constructor() {
        this.listeners = {};
        this.usageData = [];
        this.recommendations = [];
    }

    on(event, listener) {
        this.listeners[event] = listener;
    }

    startAnalysis() {
        console.log('Starting energy usage analysis...');
        // Simulate energy usage analysis
        setInterval(() => {
            const usage = this.generateUsageData();
            this.usageData.push(usage);
            if (this.listeners['usageDataUpdated']) {
                this.listeners['usageDataUpdated'](usage);
            }
            this.generateRecommendation(usage);
        }, 10000);
    }

    generateUsageData() {
        return {
            appliance: 'HVAC',
            usage: Math.floor(Math.random() * 1000),
            timestamp: new Date()
        };
    }

    generateRecommendation(usage) {
        const recommendation = {
            message: `Reduce usage of ${usage.appliance} to save energy`,
            timestamp: new Date()
        };
        this.recommendations.push(recommendation);
        if (this.listeners['recommendationGenerated']) {
            this.listeners['recommendationGenerated'](recommendation);
        }
    }
}

document.querySelector('#start-analysis-button').addEventListener('click', () => {
    initializeEnergyManagement();
});

document.querySelector('#stop-analysis-button').addEventListener('click', () => {
    console.log('Stopping energy usage analysis...');
    // Implementation for stopping analysis
});

// Function to manually add usage data
function addUsageData() {
    const usage = {
        appliance: 'Washing Machine',
        usage: 300,
        timestamp: new Date()
    };
    energyManager.usageData.push(usage);
    updateUsageData(usage);
}

document.querySelector('#add-usage-button').addEventListener('click', addUsageData);

const energyManager = new EnergyManager();
```