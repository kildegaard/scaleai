const fs = require('fs');
const csv = require('csv-parser');
const math = require('mathjs');

var data = [];

fs.createReadStream('data.csv')
    .pipe(csv())
    .on('data', (row) => {
        data.push([parseFloat(row.x), parseFloat(row.y)]);
    })
    .on('end', () => {
        mainFunction(data);
    });

function mainFunction(data) {
    var x = data.map(d => d[0]);
    var y = data.map(d => d[1]);

    var meanX = mean(x);
    var meanY = mean(y);

    var slope = calcSlope(x, y, meanX, meanY);
    var intercept = calcIntercept(meanX, meanY, slope);

    outputResult(slope, intercept);
}

function mean(arr) {
    var sum = 0;
    for (var i = 0; i < arr.length; i++) sum += arr[i];
    return sum / arr.length;
}

function calcSlope(x, y, meanX, meanY) {
    var numerator = 0;
    var denominator = 0;

    for (var i = 0; i < x.length; i++) {
        var diffX = x[i] - meanX;
        var diffY = y[i] - meanY;
        numerator += diffX * diffY;
        denominator += diffX * diffX;
    }

    return numerator / denominator;
}

function calcIntercept(meanX, meanY, slope) {
    return meanY - slope * meanX;
}

function outputResult(slope, intercept) {
    console.log('Slope:', slope)
    console.log('Intercept:', intercept)
}

function calcSlope(x, y, meanX, meanY) {
    var numerator = 0;
    var denominator = 0;

    for (var i = 0; i < x.length; i++) {
        var diffX = x[i] - meanX;
        var diffY = y[i] - meanY;
        numerator += diffX * diffY;
        denominator += diffX * diffX;
    }

    return numerator / denominator;
}

function mainFunction(data) {
    var x = data.map(d => d[0]);
    var y = data.map(d => d[1]);

    var meanX = mean(x);
    var meanY = mean(y);

    var slope = calcSlope(x, y, meanX, meanY);
    var intercept = calcIntercept(meanX, meanY, slope);

    outputResult(slope, intercept);
}

function outputResult(slope, intercept) {
    console.log('Slope:', slope)
    console.log('Intercept:', intercept)
}

function calcIntercept(meanX, meanY, slope) {
    return meanY - slope * meanX;
}
