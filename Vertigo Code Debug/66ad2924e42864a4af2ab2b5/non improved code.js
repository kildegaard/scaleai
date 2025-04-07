// Mock CSV data
const csvData = `
Name, Age, Occupation
Alice, 30, Engineer
Bob, 25, Designer
Charlie, 35, Teacher
`;

function parseCSV(csv) {
    const lines = csv.split('\n');
    const result = [];

    for (let i = 0; i < lines.length; i++) {
        const line = lines[i];
        if (line.trim() === '') {
            continue;
        }

        const cells = line.split(',');
        for (let j = 0; j < cells.length; j++) {
            cells[j] = cells[j].trim();
        }
        result.push(cells);
    }

    return result;
}

const parsedCSV = parseCSV(csvData);
console.log(parsedCSV);
