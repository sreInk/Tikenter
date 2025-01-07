import pygame

# Initialize pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Initialize the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Game Screen with Elements")

# Fonts
font = pygame.font.Font(None, 50)  # Default font with size 50

# Text
text = font.render("Hello, Pygame!", True, BLUE)

# Rectangle properties
rect_x = 350
rect_y = 250
rect_width = 100
rect_height = 100
rect_color = RED

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with white background
    screen.fill(WHITE)

    # Draw rectangle
    pygame.draw.rect(screen, rect_color, (rect_x, rect_y, rect_width, rect_height))

    # Display text
    screen.blit(text, (300, 100))  # Draw text at position (300, 100)

    # Update the display
    pygame.display.flip()

    # Control frame rate
    clock.tick(60)

# Quit pygame
pygame.quit()
