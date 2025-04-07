const Papa = require('papaparse');

// Mock CSV data
const csvData = `
Name,Age,Occupation
Alice,30,Engineer
Bob,25,Designer
Charlie,35,Teacher
`;

Papa.parse(csvData, {
    header: true,
    skipEmptyLines: true,
    complete: function (results) {
        console.log(results.data);
    }
});
