import pygame
import random

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
RED = (255, 0, 0)
BLUE = (0, 0, 255)
SQUARE_SIZE = 50
CIRCLE_SIZE = 20

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the squares
red_square = pygame.Rect(
    WIDTH / 2 - SQUARE_SIZE, HEIGHT - SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE
)
blue_square = pygame.Rect(WIDTH / 2, HEIGHT - SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)

# Set up the circles
circles = []

# Game loop
running = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not running:
                running = True
            else:
                mouse_pos = pygame.mouse.get_pos()
                if red_square.collidepoint(mouse_pos):
                    for circle in circles:
                        if circle[1] == RED:
                            circle[0].y += 5
                elif blue_square.collidepoint(mouse_pos):
                    for circle in circles:
                        if circle[1] == BLUE:
                            circle[0].y += 5

    if running:
        # Randomly create new circles
        if random.random() < 0.1:
            x = random.randint(0, WIDTH - CIRCLE_SIZE)
            y = 0
            color = RED if random.random() < 0.5 else BLUE
            circles.append([pygame.Rect(x, y, CIRCLE_SIZE, CIRCLE_SIZE), color])

        # Move circles
        for circle in circles:
            circle[0].y += 2

        # Remove circles that have moved off the screen
        circles = [circle for circle in circles if circle[0].y < HEIGHT]

    # Draw everything
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, RED, red_square)
    pygame.draw.rect(screen, BLUE, blue_square)
    for circle in circles:
        pygame.draw.ellipse(screen, circle[1], circle[0])

    # Update the display
    pygame.display.flip()
