const fs = require('fs');
const { Parser } = require('json2csv');

const numRows = 100;
let data = [];

for (let i = 0; i < numRows; i++) {
    let x = Math.random() * 100;
    let y = 2 * x + 10 + (Math.random() * 20 - 10); // y = 2x + 10 with some noise
    data.push({ x, y });
}

const json2csvParser = new Parser({ fields: ['x', 'y'] });
const csv = json2csvParser.parse(data);

fs.writeFile('mocked_data.csv', csv, function (err) {
    if (err) {
        return console.log(err);
    }
    console.log('Mocked data saved to mocked_data.csv');
});
