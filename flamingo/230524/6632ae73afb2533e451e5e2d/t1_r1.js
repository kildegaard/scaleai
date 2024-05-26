// Function to load data from a JSON file or string
function loadData(data) {
    if (typeof data === 'string') {
        return JSON.parse(data);
    } else {
        return data;
    }
}

// Function to calculate daily price change and other metrics
function analyzeData(data) {
    let highestClose = data[0];
    let lowestClose = data[0];
    let totalVolume = 0;
    let dailyChanges = [];

    data.forEach((day) => {
        // Calculate daily price change
        day.priceChange = day.close - day.open;
        dailyChanges.push(day.priceChange);

        // Update highest and lowest closing prices
        if (day.close > highestClose.close) {
            highestClose = day;
        }
        if (day.close < lowestClose.close) {
            lowestClose = day;
        }

        // Update total trading volume
        totalVolume += day.volume;
    });

    // Calculate average daily trading volume
    let averageVolume = totalVolume / data.length;

    // Identify periods of significant price volatility
    let volatilityThreshold = 2; // Adjust this value to set the threshold for significant volatility
    let volatilePeriods = [];
    for (let i = 0; i < dailyChanges.length; i++) {
        if (Math.abs(dailyChanges[i]) > volatilityThreshold) {
            volatilePeriods.push(data[i].date);
        }
    }

    return {
        highestClose: highestClose,
        lowestClose: lowestClose,
        averageVolume: averageVolume,
        volatilePeriods: volatilePeriods,
    };
}

// Example usage:
let jsonData = `[
    {"date": "2022-01-01", "open": 100.0, "high": 110.0, "low": 90.0, "close": 105.0, "volume": 1000},
    {"date": "2022-01-02", "open": 105.0, "high": 115.0, "low": 100.0, "close": 110.0, "volume": 1500},
    {"date": "2022-01-03", "open": 110.0, "high": 120.0, "low": 105.0, "close": 115.0, "volume": 2000}
]`;

let data = loadData(jsonData);
let results = analyzeData(data);

console.log("Highest closing price:", results.highestClose);
console.log("Lowest closing price:", results.lowestClose);
console.log("Average daily trading volume:", results.averageVolume);
console.log("Periods of significant price volatility:", results.volatilePeriods);