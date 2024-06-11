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

    def update(self, environment):
        pass

    def draw(self):
        pass


class Flora(Entity):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.size = random.uniform(1, 5)

    def update(self, environment):
        self.size += 0.1

        if environment["temperature"] > 25:
            self.fitness -= 1
        elif environment["temperature"] < 15:
            self.fitness -= 1
        else:
            self.fitness += 1

        if environment["humidity"] > 60:
            self.fitness += 1
        elif environment["humidity"] < 40:
            self.fitness -= 1


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
        self.speed = random.uniform(1, 5)

    def update(self, environment):
        self.x += random.uniform(-self.speed, self.speed)
        self.y += random.uniform(-self.speed, self.speed)

        if self.x < 0 or self.x > WIDTH or self.y < 0 or self.y > HEIGHT:
            self.fitness -= 1
        else:
            self.fitness += 1

        if environment["terrain"] == "desert":
            self.fitness -= 1
        elif environment["terrain"] == "forest":
            self.fitness += 1


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


def mutate(entity):
    if isinstance(entity, Flora):
        entity.size += random.uniform(-1, 1)
    elif isinstance(entity, Fauna):
        entity.speed += random.uniform(-1, 1)


def evolve(entities):
    entities.sort(key=lambda x: x.fitness, reverse=True)
    entities = entities[: len(entities) // 2]

    for _ in range(len(entities)):
        entity = random.choice(entities)
        new_entity = type(entity)(entity.x, entity.y)
        mutate(new_entity)
        entities.append(new_entity)

    return entities


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

    environment = {"temperature": 20, "humidity": 50, "terrain": "plains"}

    generation = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(WHITE)

        for entity in entities:
            entity.update(environment)
            entity.draw()

        pygame.display.flip()
        clock.tick(60)

        generation += 1
        if generation % 100 == 0:
            entities = evolve(entities)

            environment["temperature"] += random.uniform(-5, 5)
            environment["humidity"] += random.uniform(-10, 10)

            if random.random() < 0.1:
                environment["terrain"] = random.choice(["desert", "forest", "plains"])

    pygame.quit()


if __name__ == "__main__":
    main()
