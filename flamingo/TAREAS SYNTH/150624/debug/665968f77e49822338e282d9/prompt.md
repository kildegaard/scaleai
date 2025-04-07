Help me document the code for creating, updating and visualizing financial goals in my personal finance dashboard. Here’s the code:

```javascript
// goal-management-ui.js

document.addEventListener('DOMContentLoaded', initializeGoalManagement);

const goalForm = document.getElementById('goal-form');
const goalNameInput = document.getElementById('goal-name');
const goalTargetInput = document.getElementById('goal-target');
const createGoalButton = document.getElementById('create-goal');
const goalsList = document.getElementById('goals-list');

function initializeGoalManagement() {
    createGoalButton.addEventListener('click', createGoal);
}

function createGoal(event) {
    event.preventDefault();
    const name = goalNameInput.value;
    const target = parseFloat(goalTargetInput.value);
    if (!name || isNaN(target) || target <= 0) return;
    fetch('/api/goals', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name, target })
    })
    .then(response => response.json())
    .then(data => {
        loadGoals();
    })
    .catch(error => {
        console.error('Error creating goal:', error);
    });
}

function loadGoals() {
    fetch('/api/goals')
        .then(response => response.json())
        .then(data => {
            displayGoals(data);
        })
        .catch(error => {
            console.error('Error fetching goals:', error);
        });
}

function displayGoals(goals) {
    goalsList.innerHTML = goals.map(goal => 
        `<div><p>Goal: ${goal.name} - Target: $${goal.target}</p></div>`
    ).join('');
}
```