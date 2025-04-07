Could you help draft documentation for this Express.js code? It's a server handling POST requests to a contact form, with validation for name, email, and message fields. It returns errors for invalid input and saves valid submissions. Documentation should include a brief overview, setup instructions, and details on endpoints and expected responses.

```javascript
const express = require('express');
const app = express();
const PORT = 3000;

app.use(express.json());

let submissions = [];

app.post('/contact', (req, res) => {
    const { name, email, message } = req.body;

    if (!name || typeof name !== 'string' || name.trim() === '') {
        return res.status(400).json({ error: 'Name is required and must be a non-empty string.' });
    }

    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!email || !emailRegex.test(email)) {
        return res.status(400).json({ error: 'Valid email is required.' });
    }

    if (!message || typeof message !== 'string' || message.length < 10) {
        return res.status(400).json({ error: 'Message must be at least 10 characters long.' });
    }

    const submission = { id: submissions.length + 1, name, email, message };
    submissions.push(submission);

    res.status(200).json({ message: 'Contact form submitted successfully.', submission });
});

app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
```