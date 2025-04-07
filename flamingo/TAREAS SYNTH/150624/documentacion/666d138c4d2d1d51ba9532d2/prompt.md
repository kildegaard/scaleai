I’m adding a bank transaction API to my personal finance dashboard. Can you document the JavaScript code for fetching, displaying and updating bank transactions? Here’s the code:


```javascript
// bank-transactions.js
document.addEventListener('DOMContentLoaded', fetchBankTransactions);

const transactionsContainer = document.getElementById('transactions-container');

function fetchBankTransactions() {
    fetch('/api/bank-transactions')
        .then(response => response.json())
        .then(data => {
            displayTransactions(data);
        })
        .catch(error => {
            console.error('Error fetching transactions:', error);
        });
}

function displayTransactions(transactions) {
    transactionsContainer.innerHTML = transactions
        .map(transaction => `<div><p>${transaction.date}: ${transaction.amount} (${transaction.description})</p></div>`)
        .join('');
}
```