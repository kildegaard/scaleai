// Get the canvas element
const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');

// Set the canvas dimensions
canvas.width = 800;
canvas.height = 600;

// Define the cell size
const cellSize = 10;

// Define the grid dimensions
const gridWidth = Math.floor(canvas.width / cellSize);
const gridHeight = Math.floor(canvas.height / cellSize);

// Create a 2D array to represent the grid
const grid = new Array(gridHeight).fill(0).map(() => new Array(gridWidth).fill(0));

// Define the color intensity decay rate
const decayRate = 0.9;

// Define the wave propagation speed
const speed = 1;

// Define the wave color
const waveColor = 'rgb(0, 0, 255)';

// Function to draw the grid
function drawGrid() {
    for (let i = 0; i < gridHeight; i++) {
        for (let j = 0; j < gridWidth; j++) {
            const intensity = grid[i][j];
            if (intensity > 0) {
                ctx.fillStyle = `rgba(0, 0, 255, ${intensity})`;
                ctx.fillRect(j * cellSize, i * cellSize, cellSize, cellSize);
            } else {
                ctx.fillStyle = 'rgba(0, 0, 0, 0)';
                ctx.fillRect(j * cellSize, i * cellSize, cellSize, cellSize);
            }
        }
    }
}

// Function to update the grid
function updateGrid() {
    const newGrid = new Array(gridHeight).fill(0).map(() => new Array(gridWidth).fill(0));
    for (let i = 0; i < gridHeight; i++) {
        for (let j = 0; j < gridWidth; j++) {
            const intensity = grid[i][j];
            if (intensity > 0) {
                // Update the current cell
                newGrid[i][j] = intensity * decayRate;

                // Propagate the wave to adjacent cells
                if (i > 0) newGrid[i - 1][j] = Math.max(newGrid[i - 1][j], intensity * decayRate);
                if (i < gridHeight - 1) newGrid[i + 1][j] = Math.max(newGrid[i + 1][j], intensity * decayRate);
                if (j > 0) newGrid[i][j - 1] = Math.max(newGrid[i][j - 1], intensity * decayRate);
                if (j < gridWidth - 1) newGrid[i][j + 1] = Math.max(newGrid[i][j + 1], intensity * decayRate);

                // Propagate the wave to diagonal cells
                if (i > 0 && j > 0) newGrid[i - 1][j - 1] = Math.max(newGrid[i - 1][j - 1], intensity * decayRate * 0.7);
                if (i > 0 && j < gridWidth - 1) newGrid[i - 1][j + 1] = Math.max(newGrid[i - 1][j + 1], intensity * decayRate * 0.7);
                if (i < gridHeight - 1 && j > 0) newGrid[i + 1][j - 1] = Math.max(newGrid[i + 1][j - 1], intensity * decayRate * 0.7);
                if (i < gridHeight - 1 && j < gridWidth - 1) newGrid[i + 1][j + 1] = Math.max(newGrid[i + 1][j + 1], intensity * decayRate * 0.7);
            }
        }
    }
    return newGrid;
}

// Function to handle mouse clicks
function handleClick(event) {
    const x = event.clientX - canvas.offsetLeft;
    const y = event.clientY - canvas.offsetTop;
    const i = Math.floor(y / cellSize);
    const j = Math.floor(x / cellSize);
    grid[i][j] = 1;
}

// Main loop
function loop() {
    drawGrid();
    grid = updateGrid();
    requestAnimationFrame(loop);
}

// Initialize the grid and start the main loop
canvas.addEventListener('click', handleClick);
loop();