const gridContainer = document.getElementById("grid-container");
// Create the grid with 15 boxes
for (let i = 0; i < 15; i++) {
    const gridBox = document.createElement("div");
    gridBox.classList.add("grid-box");
    gridContainer.appendChild(gridBox);
}

let currentBoxIndex = 0;
gridContainer.children[currentBoxIndex].classList.add("highlighted");

const line = document.querySelector('.line'); // Get the line element
let linePosition = 'above'; // Initial line position

document.addEventListener("keydown", function (event) {
    const key = event.key.toUpperCase();
    const gridBox = gridContainer.children[currentBoxIndex];

    // Check for letter input (A-Z)
    if (/^[A-Z]$/.test(key)) {
        gridBox.textContent = key;
        moveHighlight(1);
    } else if (key === "BACKSPACE") {
        // Backspace handling
        if (currentBoxIndex > 0) {
            gridContainer.children[currentBoxIndex - 1].textContent = "";
            moveHighlight(-1);
        }
    } else if (key === "ARROWLEFT") {
        // Left arrow handling
        moveHighlight(-1);
    } else if (key === "ARROWRIGHT") {
        // Right arrow handling
        moveHighlight(1);
    } else if (key === "DELETE") {
        // Delete handling
        gridBox.textContent = "";
    }
    if (event.key === "ARROWDOWN") {
        line.classList.remove('above');
        line.classList.add('below');
        linePosition = 'below';
    } else if (event.key === "ARROWUP") {
        line.classList.remove('below');
        line.classList.add('above');
        linePosition = 'above';
    }
});

function moveHighlight(direction) {
    const gridBox = gridContainer.children[currentBoxIndex];
    gridBox.classList.remove("highlighted");

    currentBoxIndex += direction;

    // Handle going out of bounds
    if (currentBoxIndex < 0) {
        currentBoxIndex = 0;
    } else if (currentBoxIndex >= gridContainer.children.length) {
        currentBoxIndex = gridContainer.children.length - 1;
    }

    gridContainer.children[currentBoxIndex].classList.add("highlighted");
}