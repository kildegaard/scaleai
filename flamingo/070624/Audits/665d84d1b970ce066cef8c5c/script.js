// Get the canvas element
const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');

// Set the canvas dimensions
canvas.width = 800;
canvas.height = 600;

// Set the game variables
let player1X = 50;
let player1Y = canvas.height / 2;
let player2X = canvas.width - 50;
let player2Y = canvas.height / 2;
let ballX = canvas.width / 2;
let ballY = canvas.height / 2;
let ballVelocityX = 2;
let ballVelocityY = 2;
let player1Score = 0;
let player2Score = 0;
let timer = 60;
let isPlayer1Frozen = false;
let isPlayer2Frozen = false;
let player1Speed = 5;
let player2Speed = 5;
let powerUps = [];

// Set the power-up variables
let powerUpSpawnTime = 5;
let powerUpSpawnTimer = 0;

// Set the game loop
setInterval(gameLoop, 1000 / 60);

// Function to draw the game
function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Draw the players
    ctx.beginPath();
    ctx.rect(player1X, player1Y, 10, 100);
    ctx.fillStyle = 'blue';
    ctx.fill();
    ctx.beginPath();
    ctx.rect(player2X, player2Y, 10, 100);
    ctx.fillStyle = 'red';
    ctx.fill();

    // Draw the ball
    ctx.beginPath();
    ctx.arc(ballX, ballY, 10, 0, 2 * Math.PI);
    ctx.fillStyle = 'black';
    ctx.fill();

    // Draw the power-ups
    for (let i = 0; i < powerUps.length; i++) {
        ctx.beginPath();
        ctx.rect(powerUps[i].x, powerUps[i].y, 10, 10);
        ctx.fillStyle = powerUps[i].color;
        ctx.fill();
    }

    // Draw the scores and timer
    ctx.font = '24px Arial';
    ctx.fillStyle = 'black';
    ctx.textAlign = 'left';
    ctx.textBaseline = 'top';
    ctx.fillText(`Player 1 Score: ${player1Score}`, 10, 10);
    ctx.fillText(`Player 2 Score: ${player2Score}`, 10, 30);
    ctx.textAlign = 'right';
    ctx.textBaseline = 'top';
    ctx.fillText(`Timer: ${timer}`, canvas.width - 10, 10);
}

// Function to update the game state
function update() {
    // Update the players
    if (!isPlayer1Frozen) {
        if (keys.w) player1Y -= player1Speed;
        if (keys.s) player1Y += player1Speed;
        if (keys.a) player1X -= player1Speed;
        if (keys.d) player1X += player1Speed;
    }
    if (!isPlayer2Frozen) {
        if (keys.up) player2Y -= player2Speed;
        if (keys.down) player2Y += player2Speed;
        if (keys.left) player2X -= player2Speed;
        if (keys.right) player2X += player2Speed;
    }

    // Update the ball
    ballX += ballVelocityX;
    ballY += ballVelocityY;
    if (ballX < 0 || ballX > canvas.width) {
        ballVelocityX = -ballVelocityX;
    }
    if (ballY < 0 || ballY > canvas.height) {
        ballVelocityY = -ballVelocityY;
    }

    // Check for collisions with the players
    if (ballX < player1X + 10 && ballX > player1X && ballY > player1Y && ballY < player1Y + 100) {
        ballVelocityX = -ballVelocityX;
    }
    if (ballX > player2X && ballX < player2X + 10 && ballY > player2Y && ballY < player2Y + 100) {
        ballVelocityX = -ballVelocityX;
    }

    // Check for goals
    if (ballX < 0) {
        player2Score++;
        resetBall();
    }
    if (ballX > canvas.width) {
        player1Score++;
        resetBall();
    }

    // Check for power-ups
    for (let i = 0; i < powerUps.length; i++) {
        if (powerUps[i].x < player1X + 10 && powerUps[i].x > player1X && powerUps[i].y > player1Y && powerUps[i].y < player1Y + 100) {
            if (powerUps[i].color === 'blue') {
                isPlayer2Frozen = true;
                setTimeout(() => {
                    isPlayer2Frozen = false;
                }, 5000);
            }
            if (powerUps[i].color === 'red') {
                player1Speed += 2;
                setTimeout(() => {
                    player1Speed -= 2;
                }, 5000);
            }
            powerUps.splice(i, 1);
        }
        if (powerUps[i].x > player2X && powerUps[i].x < player2X + 10 && powerUps[i].y > player2Y && powerUps[i].y < player2Y + 100) {
            if (powerUps[i].color === 'blue') {
                isPlayer1Frozen = true;
                setTimeout(() => {
                    isPlayer1Frozen = false;
                }, 5000);
            }
            if (powerUps[i].color === 'red') {
                player2Speed += 2;
                setTimeout(() => {
                    player2Speed -= 2;
                }, 5000);
            }
            powerUps.splice(i, 1);
        }
    }

    // Update the timer
    timer -= 1 / 60;
    if (timer <= 0) {
        timer = 0;
        endGame();
    }

    // Spawn power-ups
    powerUpSpawnTimer += 1 / 60;
    if (powerUpSpawnTimer >= powerUpSpawnTime) {
        powerUpSpawnTimer = 0;
        spawnPowerUp();
    }
}

// Function to handle key presses
let keys = {};
document.addEventListener('keydown', (e) => {
    keys[e.key] = true;
});
document.addEventListener('keyup', (e) => {
    keys[e.key] = false;
});

// Function to reset the ball
function resetBall() {
    ballX = canvas.width / 2;
    ballY = canvas.height / 2;
    ballVelocityX = 2;
    ballVelocityY = 2;
}

// Function to end the game
function endGame() {
    if (player1Score > player2Score) {
        alert('Player 1 wins!');
    } else if (player2Score > player1Score) {
        alert('Player 2 wins!');
    } else {
        alert('It\'s a tie!');
    }
    player1Score = 0;
    player2Score = 0;
    timer = 60;
}

// Function to spawn power-ups
function spawnPowerUp() {
    let powerUp = {
        x: Math.random() * (canvas.width - 20) + 10,
        y: Math.random() * (canvas.height - 20) + 10,
        color: Math.random() < 0.5 ? 'blue' : 'red'
    };
    powerUps.push(powerUp);
}

// Main game loop
function gameLoop() {
    update();
    draw();
}