I’m adding an expert Q&A API to my pet blog. I need documentation for the JavaScript code that does API requests and responses for user questions and expert answers. Can you document this? Here’s the code.

```javascript
// expert-qa.js

document.addEventListener('DOMContentLoaded', setupQnA);

const questionForm = document.getElementById('question-form');
const questionInput = document.getElementById('question-input');
const submitQuestionButton = document.getElementById('submit-question');
const answersContainer = document.getElementById('answers-container');

function setupQnA() {
    submitQuestionButton.addEventListener('click', submitQuestion);
}

function submitQuestion(event) {
    event.preventDefault();
    const question = questionInput.value;
    if (!question) return;
    fetch('/api/questions', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ question })
    })
    .then(response => response.json())
    .then(() => {
        fetchAnswers();
    })
    .catch(error => {
        console.error('Error submitting question:', error);
    });
}

function fetchAnswers() {
    fetch('/api/answers')
        .then(response => response.json())
        .then(data => {
            displayAnswers(data);
        })
        .catch(error => {
            console.error('Error fetching answers:', error);
        });
}

function displayAnswers(answers) {
    answersContainer.innerHTML = answers.map(answer => 
        `<div><h3>${answer.question}</h3><p>${answer.answer}</p></div>`
    ).join('');
}
```