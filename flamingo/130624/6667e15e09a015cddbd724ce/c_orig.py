import pygame
import random

# Initialize pygame
# pygame.init()

# Set up display
# WIDTH, HEIGHT = 800, 600
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Deep Sea Exploration")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Player
player_image = pygame.Surface((50, 50))
player_image.fill(BLUE)
player_rect = player_image.get_rect(center=(WIDTH//2, HEIGHT//2))

# Marine life
marine_life_images = []  # Add various marine life images
marine_life_rects = []   # Corresponding rects for collision detection
for _ in range(10):
    image = pygame.Surface((30, 30))  # Placeholder
    image.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    rect = image.get_rect(center=(random.randint(0, WIDTH), random.randint(0, HEIGHT)))
    marine_life_images.append(image)
    marine_life_rects.append(rect)

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= 5
    if keys[pygame.K_RIGHT]:
        player_rect.x += 5
    if keys[pygame.K_UP]:
        player_rect.y -= 5
    if keys[pygame.K_DOWN]:
        player_rect.y += 5

    # Collision detection
    for rect in marine_life_rects:
        if player_rect.colliderect(rect):
            # Handle encounter
            pass

    # Draw everything
    # screen.fill(WHITE)
    # screen.blit(player_image, player_rect)
    # for rect, image in zip(marine_life_rects, marine_life_images):
    #     screen.blit(image, rect)
    # pygame.display.flip()

    # Frame rate
    # pygame.time.Clock().tick(60)

# Quit
# pygame.quit()