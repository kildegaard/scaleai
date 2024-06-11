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
        self.fitness = 0

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
        self.growth_rate = random.uniform(0.1, 0.5)

    def update(self):
        self.size += self.growth_rate
        self.fitness = self.size

    def draw(self):
        pygame.draw.circle(
            screen, self.color, (int(self.x), int(self.y)), int(self.size)
        )


class Tree(Flora):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.color = (128, 64, 0)
        self.growth_rate = random.uniform(0.1, 0.5)

    def update(self):
        self.size += self.growth_rate
        self.fitness = self.size

    def draw(self):
        pygame.draw.rect(
            screen,
            self.color,
            (int(self.x), int(self.y), int(self.size), int(self.size)),
        )


class Fauna(Entity):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.speed = random.uniform(0.1, 1.0)
        self.intelligence = random.uniform(0.1, 1.0)

    def update(self):
        self.x += random.uniform(-self.speed, self.speed)
        self.y += random.uniform(-self.speed, self.speed)
        self.fitness = self.speed + self.intelligence


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


def genetic_algorithm(entities):
    # Selection
    entities.sort(key=lambda x: x.fitness, reverse=True)
    selected_entities = entities[: len(entities) // 2]

    # Crossover
    offspring = []
    for i in range(len(selected_entities)):
        parent1 = random.choice(selected_entities)
        parent2 = random.choice(selected_entities)
        child = type(parent1)(parent1.x, parent1.y)
        child.growth_rate = (parent1.growth_rate + parent2.growth_rate) / 2
        child.speed = (parent1.speed + parent2.speed) / 2
        child.intelligence = (parent1.intelligence + parent2.intelligence) / 2
        offspring.append(child)

    # Mutation
    for entity in offspring:
        if random.random() < 0.1:
            entity.growth_rate += random.uniform(-0.1, 0.1)
            entity.speed += random.uniform(-0.1, 0.1)
            entity.intelligence += random.uniform(-0.1, 0.1)

    return selected_entities + offspring


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

        entities = genetic_algorithm(entities)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
