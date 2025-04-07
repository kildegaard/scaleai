I’m working on a personal finance dashboard with real-time expense tracking. The javascript file to update real-time expenses on the dashboard isn’t working. Can you help me out? Here’s the HTML and JS.

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Finance Dashboard</title>
</head>

<body>
    <div id="expenses-container">
        <h2>Expenses</h2>
        <div id="expense-chart"></div>
    </div>
    <script src="expenses.js"></script>
</body>

</html>
```

```javascript
// expenses.js

// Get the expense chart element by its ID
const expenseChart = document.getElementById('expense-chart');

// Function to update the expense chart with new data
function updateExpenseChart(data) {
    expenseChart.innerHTML = `<p>Total Expenses: $${data.total}</p>`;
}

// Function to fetch expenses from the server
function fetchExpenses() {
    fetch('/api/expenses')
        .then(response => response.json())
        .then(data => {
            updateExpenseChart(data);
        })
        .catch(error => {
            console.error('Error fetching expenses:', error);
        });
}

// Fetch expenses every 5 seconds
setInterval(fetchExpenses, 5000);
```