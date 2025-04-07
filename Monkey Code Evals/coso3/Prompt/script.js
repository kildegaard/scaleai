const gridContainer = document.getElementById("grid-container");
// Create the grid with 15 boxes
for (let i = 0; i < 15; i++) {
    const gridBox = document.createElement("div");
    gridBox.classList.add("grid-box");
    gridContainer.appendChild(gridBox);
}

let currentBoxIndex = 0;
gridContainer.children[currentBoxIndex].classList.add("highlighted");


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