const fs = require('fs')
const csv = require('csv-parser')

let data = []

// load the CSV data and process it
fs.createReadStream('data.csv')
    .pipe(csv())
    .on('data', (row) => {
        data.push([parseFloat(row.x), parseFloat(row.y)])
    })
    .on('end', () => {
        processData(data)
    });

/**
 * process the data for linear regression model calculation
 * @param {Array} data array of data points
 */
function processData(data) {
    const x = data.map(d => d[0])
    const y = data.map(d => d[1])

    const { slope, intercept } = linearRegression(x, y)
    displayResults(slope, intercept)
}

/**
 * calculates the linear regression model
 * @param {Array} x array of x values
 * @param {Array} y array of y values
 * @returns {Object} slope and intercept of the regression
 */
function linearRegression(x, y) {
    const meanX = mean(x)
    const meanY = mean(y)

    const { numerator, denominator } = calculateSlopeComponents(x, y, meanX, meanY)
    const slope = numerator / denominator
    const intercept = meanY - slope * meanX

    return {
        slope: parseFloat(slope.toFixed(3)),
        intercept: parseFloat(intercept.toFixed(3))
    };
}

/**
 * calculates the mean of an array
 * @param {Array} arr array of numbers
 * @returns {number} mean of the array
 */
function mean(arr) {
    const sum = arr.reduce((acc, val) => acc + val, 0)
    return sum / arr.length
}

/**
 * components needed to determine the slope
 * @param {Array} x array of x values
 * @param {Array} y array of y values
 * @param {number} meanX mean of the x values
 * @param {number} meanY mean of the y values
 * @returns {Object} numerator and denominator for the slope
 */
function calculateSlopeComponents(x, y, meanX, meanY) {
    let numerator = 0
    let denominator = 0

    for (let i = 0; i < x.length; i++) {
        const diffX = x[i] - meanX
        const diffY = y[i] - meanY
        numerator += diffX * diffY
        denominator += diffX * diffX
    }

    return { numerator, denominator }
}

/**
 * displays the results of the linear regression calculation
 * @param {number} slope slope of the regression line
 * @param {number} intercept intercept of the regression line
 */
function displayResults(slope, intercept) {
    console.log(`Slope: ${slope}`)
    console.log(`Intercept: ${intercept}`)
}
