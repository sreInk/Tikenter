import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
screen_width = 600
screen_height = 400

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Color Changing Sprites")

# Colors
def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Sprite Class
class Sprite(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.color = color
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.change_x = random.choice([-2, 2])
        self.change_y = random.choice([-2, 2])

    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y

        # Bounce off the walls
        if self.rect.left <= 0 or self.rect.right >= screen_width:
            self.change_x *= -1
            self.change_color()
        if self.rect.top <= 0 or self.rect.bottom >= screen_height:
            self.change_y *= -1
            self.change_color()

    def change_color(self):
        self.color = random_color()
        self.image.fill(self.color)

# Initialize two sprites
sprite1 = Sprite(100, 100, 50, 50, random_color())
sprite2 = Sprite(300, 200, 50, 50, random_color())

# Group for sprites
all_sprites = pygame.sprite.Group()
all_sprites.add(sprite1, sprite2)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the sprites
    all_sprites.update()

    # Detect collision and change color
    if pygame.sprite.collide_rect(sprite1, sprite2):
        sprite1.change_color()
        sprite2.change_color()

    # Draw everything
    screen.fill((0, 0, 0))  # Black background
    all_sprites.draw(screen)

    # Refresh the screen
    pygame.display.flip()
    clock.tick(60)

# Quit pygame
pygame.quit()
