google.charts.load('current', { 'packages': ['corechart'] });

document.getElementById('jsonFile').addEventListener('change', handleFile);

function handleFile(event) {
    const file = event.target.files[0];
    const reader = new FileReader();

    reader.onload = function (e) {
        const data = JSON.parse(e.target.result);
        generateReport(data);
        generateChart(data);
    };

    reader.readAsText(file);
}

function getOptimalPowerRange(isMax, unit) {
    if (unit === 'dBmV') {
        return isMax ? { min: 10, max: 15 } : { min: 0, max: 10 };
    } else if (unit === 'dBµV') {
        return isMax ? { min: 68, max: 73 } : { min: 58, max: 68 };
    }
}

function generateReport(data) {
    const reportDiv = document.getElementById('report');
    reportDiv.innerHTML = '<h2>Frequency Report</h2>';

    const table = document.createElement('table');
    table.innerHTML = `
        <tr>
            <th>Frequency</th>
            <th>Max Power (dBmV)</th>
            <th>Max Power (dBµV)</th>
            <th>Min Power (dBmV)</th>
            <th>Min Power (dBµV)</th>
            <th>AV Ratio</th>
        </tr>
    `;

    data.forEach(freq => {
        const row = table.insertRow();
        row.insertCell().textContent = freq.frequency;

        ['max_power_dbmv', 'max_power_dbuv', 'min_power_dbmv', 'min_power_dbuv'].forEach(field => {
            const cell = row.insertCell();
            cell.textContent = freq[field];
            stylePowerCell(cell, field, freq[field]);
        });

        const avRatioCell = row.insertCell();
        avRatioCell.textContent = freq.AV_Ratio;
        styleAVRatioCell(avRatioCell, freq.AV_Ratio);
    });

    reportDiv.appendChild(table);
}

function stylePowerCell(cell, field, value) {
    const isMax = field.startsWith('max');
    const unit = field.endsWith('dbmv') ? 'dBmV' : 'dBµV';
    const optimalRange = getOptimalPowerRange(isMax, unit);

    if (value < optimalRange.min) {
        cell.classList.add('warning');
    } else if (value > optimalRange.max) {
        cell.classList.add('warning');
    }
}

function styleAVRatioCell(cell, value) {
    if (value < 3 || value > 5) {
        cell.classList.add('warning');
        cell.innerHTML += ' <span class="warning">(Out of Range)</span>';
    } else {
        cell.classList.add('success');
        cell.innerHTML += ' <span class="success">(In Range)</span>';
    }
}

// ... (rest of the script.js code for generateChart and helper functions)