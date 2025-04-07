const gridContainer = document.getElementById("grid-container");
// Create the grid with 15 boxes
for (let i = 0; i < 15; i++) {
    const gridBox = document.createElement("div");
    gridBox.classList.add("grid-box");
    gridContainer.appendChild(gridBox);
}

let currentBoxIndex = 0;
gridContainer.children[currentBoxIndex].classList.add("highlighted");

const lineElement = document.querySelector('.line');
let linePosition = "top"; // Keep track of line position

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
    if (key === "ARROWDOWN") {
        lineElement.style.top = "42px"; // Move below (adjust '42px' if needed)
    } else if (key === "ARROWUP") {
        lineElement.style.top = "0";
        linePosition = "top";
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
