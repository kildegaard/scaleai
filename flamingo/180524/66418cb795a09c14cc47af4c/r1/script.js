let score = 0;
let time = 90;
let timer;

function createGrid() {
    const grid = document.getElementById('grid');
    grid.innerHTML = '';
    const squares = [];
    for (let i = 0; i < 36; i++) {
        const square = document.createElement('button');
        square.className = 'square';
        square.style.backgroundColor = 'rgb(120, 120, 120)';
        square.onclick = () => checkClick(i);
        grid.appendChild(square);
        squares.push(square);
    }
    const uniqueIndex = Math.floor(Math.random() * 36);
    squares[uniqueIndex].style.backgroundColor = 'rgb(255, 0, 0)';
}

function checkClick(index) {
    const squares = document.querySelectorAll('.square');
    if (squares[index].style.backgroundColor === 'rgb(255, 0, 0)') {
        score++;
        createGrid();
    }
}

function startGame() {
    createGrid();
    timer = setInterval(() => {
        time--;
        if (time <= 0) {
            clearInterval(timer);
            alert(`Game Over! Your score is ${score}`);
        }
    }, 1000);
}

startGame();