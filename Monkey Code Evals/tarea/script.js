const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');


const shipWidth = 50;
const shipHeight = 30;
let shipX = (canvas.width - shipWidth) / 2;

const bulletWidth = 5;
const bulletHeight = 10;
let bullets = [];

const enemyWidth = 50;
const enemyHeight = 30;
let enemies = [];
const enemyRows = 3;
const enemyColumns = 8;
const enemyPadding = 10;
const enemyOffsetTop = 30;
const enemyOffsetLeft = 30;

let rightPressed = false;
let leftPressed = false;
let spacePressed = false;
let enemySpeed = 0.5;

document.addEventListener('keydown', keyDownHandler, false);
document.addEventListener('keyup', keyUpHandler, false);

function keyDownHandler(e) {
    if (e.key === 'd' || e.key === 'D') {
        rightPressed = true;
    } else if (e.key === 'a' || e.key === 'A') {
        leftPressed = true;
    } else if (e.key === ' ') {
        spacePressed = true;
    }
}

function keyUpHandler(e) {
    if (e.key === 'd' || e.key === 'D') {
        rightPressed = false;
    } else if (e.key === 'a' || e.key === 'A') {
        leftPressed = false;
    } else if (e.key === ' ') {
        spacePressed = false;
        fireBullet();
    }
}

function drawShip() {
    ctx.beginPath();
    ctx.rect(shipX, canvas.height - shipHeight, shipWidth, shipHeight);
    ctx.fillStyle = '#00f';
    ctx.fill();
    ctx.closePath();
}

function drawBullet(bullet) {
    ctx.beginPath();
    ctx.rect(bullet.x, bullet.y, bulletWidth, bulletHeight);
    ctx.fillStyle = '#f00';
    ctx.fill();
    ctx.closePath();
}

function drawEnemies() {
    for (let c = 0; c < enemyColumns; c++) {
        for (let r = 0; r < enemyRows; r++) {
            if (enemies[c][r].status === 1) {
                let enemyX = c * (enemyWidth + enemyPadding) + enemyOffsetLeft;
                let enemyY = enemies[c][r].y;
                enemies[c][r].x = enemyX;
                ctx.beginPath();
                ctx.rect(enemyX, enemyY, enemyWidth, enemyHeight);
                ctx.fillStyle = '#0f0';
                ctx.fill();
                ctx.closePath();
            }
        }
    }
}

function fireBullet() {
    bullets.push({ x: shipX + shipWidth / 2 - bulletWidth / 2, y: canvas.height - shipHeight });
}

function collisionDetection() {
    for (let c = 0; c < enemyColumns; c++) {
        for (let r = 0; r < enemyRows; r++) {
            let enemy = enemies[c][r];
            if (enemy.status === 1) {
                for (let i = 0; i < bullets.length; i++) {
                    let bullet = bullets[i];
                    if (bullet.x > enemy.x && bullet.x < enemy.x + enemyWidth && bullet.y > enemy.y && bullet.y < enemy.y + enemyHeight) {
                        enemy.status = 0;
                        bullets.splice(i, 1);
                        break;
                    }
                }
                if (enemy.y + enemyHeight > canvas.height - shipHeight) {
                    alert('¡Game Over!');
                    document.location.reload();
                }
            }
        }
    }
}

function moveEnemies() {
    for (let c = 0; c < enemyColumns; c++) {
        for (let r = 0; r < enemyRows; r++) {
            let enemy = enemies[c][r];
            if (enemy.status === 1) {
                enemy.y += enemySpeed;
            }
        }
    }
}

function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    drawShip();
    bullets.forEach(drawBullet);
    drawEnemies();
    collisionDetection();
    moveEnemies();

    if (rightPressed && shipX < canvas.width - shipWidth) {
        shipX += 7;
    } else if (leftPressed && shipX > 0) {
        shipX -= 7;
    }

    bullets.forEach((bullet, index) => {
        bullet.y -= 7;
        if (bullet.y < 0) {
            bullets.splice(index, 1);
        }
    });

    requestAnimationFrame(draw);
}

function initEnemies() {
    for (let c = 0; c < enemyColumns; c++) {
        enemies[c] = [];
        for (let r = 0; r < enemyRows; r++) {
            let enemyX = c * (enemyWidth + enemyPadding) + enemyOffsetLeft;
            let enemyY = r * (enemyHeight + enemyPadding) + enemyOffsetTop;
            enemies[c][r] = { x: enemyX, y: enemyY, status: 1 };
        }
    }
}

initEnemies();
draw();