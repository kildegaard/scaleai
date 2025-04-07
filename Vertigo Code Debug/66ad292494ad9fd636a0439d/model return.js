const fs = require('fs');
const csv = require('csv-parser');
const math = require('mathjs');

// Use mathjs for more concise calculations
const { mean, sum } = math;

// Asynchronously read and parse the CSV data
fs.createReadStream('data.csv')
    .pipe(csv())
    .on('data', (row) => {
        data.push([parseFloat(row.x), parseFloat(row.y)]);
    })
    .on('end', () => {
        calculateLinearRegression(data);
    });

// Store data in an array
const data = [];

// Main function to calculate and output linear regression results
function calculateLinearRegression(data) {
    // Extract x and y values using destructuring
    const x = data.map(([x]) => x);
    const y = data.map(([, y]) => y);

    const meanX = mean(x);
    const meanY = mean(y);

    const slope = calculateSlope(x, y, meanX, meanY);
    const intercept = calculateIntercept(meanX, meanY, slope);

    outputResult(slope, intercept);
}

// Calculate the slope of the regression line
function calculateSlope(x, y, meanX, meanY) {
    const numerator = sum(x.map((xi, i) => (xi - meanX) * (y[i] - meanY)));
    const denominator = sum(x.map(xi => (xi - meanX) ** 2));

    return numerator / denominator;
}

// Calculate the y-intercept of the regression line
function calculateIntercept(meanX, meanY, slope) {
    return meanY - slope * meanX;
}

// Output the calculated slope and intercept
function outputResult(slope, intercept) {
    console.log(`Slope: ${slope}`);
    console.log(`Intercept: ${intercept}`);
}
