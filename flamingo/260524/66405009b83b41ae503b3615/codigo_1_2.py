import pygame
import random

# Initialize Pygame
pygame.init()

# Set up some colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set up the screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set up the title of the window
pygame.display.set_caption("Alien Landscape")


# Define the base class for alien species
class AlienSpecies:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self):
        pass

    def draw(self):
        pass


# Define a plant species that grows over time
class AlienPlant(AlienSpecies):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.size = 10
        self.growth_rate = 0.1

    def update(self):
        self.size += self.growth_rate

    def draw(self):
        pygame.draw.circle(screen, GREEN, (int(self.x), int(self.y)), int(self.size))


# Define an animal species that moves around the screen
class AlienAnimal(AlienSpecies):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.speed = 2
        self.direction = random.choice([-1, 1])

    def update(self):
        self.x += self.speed * self.direction
        if self.x < 0 or self.x > SCREEN_WIDTH:
            self.direction *= -1

    def draw(self):
        pygame.draw.rect(screen, RED, (int(self.x), int(self.y), 10, 10))


# Create a list to hold all the alien species
alien_species = []

# Create some initial alien species
for _ in range(10):
    alien_species.append(
        AlienPlant(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT))
    )
    alien_species.append(
        AlienAnimal(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT))
    )

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update all the alien species
    for species in alien_species:
        species.update()

    # Draw everything
    screen.fill(WHITE)
    for species in alien_species:
        species.draw()
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.delay(1000 // 60)
