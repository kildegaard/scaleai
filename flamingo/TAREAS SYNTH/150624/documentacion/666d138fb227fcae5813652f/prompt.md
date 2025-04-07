Can you help me with some documentation for this code? It’s an Express.js server that serves and allows users to download files from a directory. Please, I need a brief description of what it does, how to run it, and any important details or dependencies.

```javascript
const express = require('express');
const fs = require('fs');
const path = require('path');
const app = express();
const PORT = 3000;
const DIRECTORY = path.join(__dirname, 'files');

app.use(express.static(DIRECTORY));

app.get('/', (req, res) => {
    fs.readdir(DIRECTORY, (err, files) => {
        if (err) {
            return res.status(500).send('Unable to scan directory');
        }
        res.send(`
            <h1>Design Studio File Server</h1>
            <ul>
                ${files.map(file => `<li><a href=""/${file}"" download>${file}</a></li>`).join('')}
            </ul>
        `);
    });
});

app.get('/download/:filename', (req, res) => {
    const file = path.join(DIRECTORY, req.params.filename);
    res.download(file, (err) => {
        if (err) {
            res.status(500).send('File not found or unable to download');
        }
    });
});

app.listen(PORT, () => {
    console.log(`Server is running at http://localhost:${PORT}`);
});
```