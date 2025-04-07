I’m working on a deck builder for my collectible card game site. The JavaScript for validating decks and handling errors during deck creation isn’t working right and I’m getting validation failures or bad error handling. Can you help me out? Here’s the HTML and JavaScript.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Deck Builder</title>
</head>
<body>
    <div id="deck-builder">
        <h2>Create Your Deck</h2>
        <input type="text" id="deck-name" placeholder="Deck Name">
        <textarea id="deck-cards" placeholder="Enter card IDs, separated by commas"></textarea>
        <button id="validate-deck">Validate Deck</button>
        <div id="validation-results"></div>
    </div>
    <script src="deck-builder.js"></script>
</body>
</html>
```

```javascript
const deckNameInput = document.getElementById('deck-name');
const deckCardsInput = document.getElementById('deck-cards');
const validateDeckButton = document.getElementById('validate-deck');
const validationResults = document.getElementById('validation-results');

validateDeckButton.addEventListener('click', validateDeck);

function validateDeck() {
    const deckName = deckNameInput.value;
    const cardIds = deckCardsInput.value.split(',').map(id => id.trim());
    
    if (!deckName || cardIds.length < 5) {
        validationResults.textContent = 'Deck must have a name and at least 5 cards.';
        return;
    }

    fetch('/api/validate-deck', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ deckName, cardIds })
    })
    .then(response => response.json())
    .then(data => {
        displayValidationResults(data);
    })
    .catch(error => {
        console.error('Error validating deck:', error);
    });
}

function displayValidationResults(data) {
    validationResults.innerHTML = `<p>${data.message}</p>`;
}
```