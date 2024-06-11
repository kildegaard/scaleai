import pygame
import random

# Window size
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Square size
SQUARE_SIZE = 50

# Circle size
CIRCLE_SIZE = 20

# Colors
RED = (255, 0, 0)
BLUE = (0, 0, 255)


class Circle:
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), CIRCLE_SIZE)

    def move(self, target_x, target_y):
        if self.x < target_x:
            self.x += 1
        elif self.x > target_x:
            self.x -= 1
        if self.y < target_y:
            self.y += 1
        elif self.y > target_y:
            self.y -= 1


def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()

    # Start button
    start_button = pygame.Rect(WINDOW_WIDTH // 2 - 50, WINDOW_HEIGHT // 2 - 25, 100, 50)
    game_started = False

    # Squares
    red_square = pygame.Rect(
        50, WINDOW_HEIGHT - SQUARE_SIZE - 50, SQUARE_SIZE, SQUARE_SIZE
    )
    blue_square = pygame.Rect(
        WINDOW_WIDTH - SQUARE_SIZE - 50,
        WINDOW_HEIGHT - SQUARE_SIZE - 50,
        SQUARE_SIZE,
        SQUARE_SIZE,
    )

    # Circles
    circles = [
        Circle(RED, random.randint(0, WINDOW_WIDTH), random.randint(0, WINDOW_HEIGHT))
        for _ in range(10)
    ]
    circles += [
        Circle(BLUE, random.randint(0, WINDOW_WIDTH), random.randint(0, WINDOW_HEIGHT))
        for _ in range(10)
    ]

    target_x = None
    target_y = None
    color = None

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if not game_started:
                    if start_button.collidepoint(event.pos):
                        game_started = True
                elif red_square.collidepoint(event.pos):
                    target_x = red_square.centerx
                    target_y = red_square.centery
                    color = RED
                elif blue_square.collidepoint(event.pos):
                    target_x = blue_square.centerx
                    target_y = blue_square.centery
                    color = BLUE

        screen.fill((0, 0, 0))

        if game_started:
            pygame.draw.rect(screen, RED, red_square)
            pygame.draw.rect(screen, BLUE, blue_square)
            for circle in circles:
                circle.draw(screen)
                if circle.color == color:
                    circle.move(target_x, target_y)
        else:
            pygame.draw.rect(screen, (0, 255, 0), start_button)
            font = pygame.font.Font(None, 36)
            text = font.render("Start", True, (255, 255, 255))
            screen.blit(
                text,
                (
                    start_button.centerx - text.get_width() // 2,
                    start_button.centery - text.get_height() // 2,
                ),
            )

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
