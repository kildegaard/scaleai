// Initialize Phaser
var config = {
    type: Phaser.AUTO,
    width: 800,
    height: 600,
    backgroundColor: '#00ff00',
    physics: {
      default: 'arcade',
      arcade: {
        gravity: { y: 300 },
        debug: true // Enable physics debugging
      }
    },
    scene: {
      preload: preload,
      create: create,
      update: update
    }
  };
  
  var game = new Phaser.Game(config);
  
  // Define game variables
  var player;
  var platforms;
  var enemies;
  var movingObjects;
  var bullets;
  var healthBar;
  var healthBlocks = 5;
  var isGameOver = false;
  var timer;
  var enemiesKilled = 0;
  
  // Preload assets
  function preload() {
    this.load.image('player', 'player.png'); // Load player sprite (5x5 px blue triangle)
    this.load.image('platform', 'platform.png'); // Load platform sprite
    this.load.image('enemy', 'enemy.png'); // Load enemy sprite (5x5 px red pentagon)
    this.load.image('movingObject', 'movingObject.png'); // Load moving object sprite (10x20 px grey rectangle)
    this.load.image('bullet', 'bullet.png'); // Load bullet sprite
  }
  
  // Create game objects
  function create() {
    // Create platforms
    platforms = this.physics.add.staticGroup();
    platforms.create(400, 568, 'platform').setScale(2).refreshBody();
    platforms.create(600, 400, 'platform');
    platforms.create(50, 250, 'platform');
  
    // Create player
    player = this.physics.add.sprite(100, 450, 'player');
    player.setBounce(0.2);
    player.setCollideWorldBounds(true);
  
    // Create enemies
    enemies = this.physics.add.group();
    for (var i = 0; i < 10; i++) {
      var enemy = enemies.create(Phaser.Math.Between(0, 800), Phaser.Math.Between(0, 600), 'enemy');
      enemy.setVelocityX(Phaser.Math.Between(-100, 100));
    }
  
    // Create moving objects
    movingObjects = this.physics.add.group();
    movingObjects.create(300, 300, 'movingObject').setVelocityX(100);
  
    // Create bullets
    bullets = this.physics.add.group();
  
    // Create health bar
    healthBar = this.add.group();
    for (var i = 0; i < healthBlocks; i++) {
      var healthBlock = this.add.rectangle(20 + i * 30, 20, 20, 20, 0xff0000);
      healthBar.add(healthBlock);
    }
  
    // Add colliders
    this.physics.add.collider(player, platforms);
    this.physics.add.collider(enemies, platforms);
    this.physics.add.collider(movingObjects, platforms);
    this.physics.add.collider(bullets, platforms, destroyBullet, null, this);
    this.physics.add.collider(bullets, enemies, hitEnemy, null, this);
    this.physics.add.collider(player, enemies, hitPlayer, null, this);
    this.physics.add.collider(player, movingObjects, hitPlayer, null, this);
  
    // Start countdown timer
    timer = this.time.addEvent({ delay: 60000, callback: onCountdownEnd, callbackScope: this });
  }
  
  // Update game state
  function update() {
    if (isGameOver) return;
  
    // Move player
    if (this.input.keyboard.addKey(Phaser.Input.Keyboard.KeyCodes.LEFT).isDown || this.input.keyboard.addKey(Phaser.Input.Keyboard.KeyCodes.A).isDown) {
      player.setVelocityX(-160);
    } else if (this.input.keyboard.addKey(Phaser.Input.Keyboard.KeyCodes.RIGHT).isDown || this.input.keyboard.addKey(Phaser.Input.Keyboard.KeyCodes.D).isDown) {
      player.setVelocityX(160);
    } else {
      player.setVelocityX(0);
    }
  
    // Jump
    if ((this.input.keyboard.addKey(Phaser.Input.Keyboard.KeyCodes.UP).isDown || this.input.keyboard.addKey(Phaser.Input.Keyboard.KeyCodes.W).isDown) && player.body.touching.down) {
      player.setVelocityY(-330);
    }
  
    // Shoot
    if (this.input.keyboard.addKey(Phaser.Input.Keyboard.KeyCodes.SPACE).isDown) {
      var bullet = bullets.create(player.x, player.y, 'bullet');
      bullet.setVelocityX(400);
    }
  
    // Move enemies
    enemies.children.each(function(enemy) {
      if (enemy.body.touching.down) {
        enemy.setVelocityX(Phaser.Math.Between(-100, 100));
      }
    });
  
    // Check game over
    if (healthBlocks <= 0) {
      isGameOver = true;
      this.add.text(400, 300, 'Game Over', { fontSize: '32px', fill: '#000' });
    }
  }
  
  // Destroy bullet
  function destroyBullet(bullet, platform) {
    bullet.destroy();
  }
  
  // Hit enemy
  function hitEnemy(bullet, enemy) {
    bullet.destroy();
    enemy.destroy();
    enemiesKilled++;
    if (enemiesKilled >= 10) {
      isGameOver = true;
      this.add.text(400, 300, 'You Win!', { fontSize: '32px', fill: '#000' });
    }
  }
  
  // Hit player
  function hitPlayer(player, enemy) {
    healthBlocks--;
    healthBar.children.each(function(healthBlock) {
      healthBlock.destroy();
    });
    for (var i = 0; i < healthBlocks; i++) {
      var healthBlock = this.add.rectangle(20 + i * 30, 20, 20, 20, 0xff0000);
      healthBar.add(healthBlock);
    }
  }
  
  // Countdown end
  function onCountdownEnd() {
    if (enemiesKilled < 10) {
      isGameOver = true;
      this.add.text(400, 300, 'Time\'s Up! Game Over', { fontSize: '32px', fill: '#000' });
    }
  }