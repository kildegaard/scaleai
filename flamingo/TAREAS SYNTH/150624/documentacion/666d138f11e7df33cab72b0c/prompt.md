Could you provide documentation for the following Node.js code? The script uses `readline` to create a customer feedback form that collects a user's name, email, and feedback. It validates the email format and saves the feedback to a file. Include explanations for the key functions and modules used.

```javascript
const fs = require('fs');
const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const askQuestion = (question) => {
    return new Promise((resolve) => rl.question(question, resolve));
};

const getFeedback = async () => {
    const name = await askQuestion('Enter your name: ');
    const email = await askQuestion('Enter your email: ');
    const feedback = await askQuestion('Enter your feedback: ');

    if (!name || !email || !feedback) {
        console.log('All fields are required.');
        rl.close();
        return;
    }

    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
        console.log('Invalid email format.');
        rl.close();
        return;
    }

    const feedbackEntry = `Name: ${name}\nEmail: ${email}\nFeedback: ${feedback}\n---\n`;

    fs.appendFile('feedback.txt', feedbackEntry, (err) => {
        if (err) {
            console.log('Error writing to file:', err);
        } else {
            console.log('Feedback saved successfully.');
        }
        rl.close();
    });
};

console.log('Customer Feedback Form');
getFeedback();
```