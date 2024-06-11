import pygame
import random

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))


class Entity:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self):
        pass

    def draw(self):
        pass


class Flora(Entity):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.size = 1

    def update(self):
        self.size += 0.1


class Plant(Flora):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.color = (0, 255, 0)

    def draw(self):
        pygame.draw.circle(
            screen, self.color, (int(self.x), int(self.y)), int(self.size)
        )


class Tree(Flora):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.color = (128, 64, 0)

    def draw(self):
        pygame.draw.rect(
            screen,
            self.color,
            (int(self.x), int(self.y), int(self.size), int(self.size)),
        )


class Fauna(Entity):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.speed = 1

    def update(self):
        self.x += random.uniform(-self.speed, self.speed)
        self.y += random.uniform(-self.speed, self.speed)


class Herbivore(Fauna):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.color = (0, 0, 255)

    def draw(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), 5)


class Carnivore(Fauna):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.color = (255, 0, 0)

    def draw(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), 5)


def main():
    clock = pygame.time.Clock()

    entities = [
        Plant(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(50)
    ]
    entities += [
        Tree(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(20)
    ]
    entities += [
        Herbivore(random.randint(0, WIDTH), random.randint(0, HEIGHT))
        for _ in range(10)
    ]
    entities += [
        Carnivore(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(5)
    ]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(WHITE)

        for entity in entities:
            entity.update()
            entity.draw()

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
