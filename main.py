# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    pygame.init()
    
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Set up the main game screen
    game_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Set up the game clock
    game_clock = pygame.time.Clock()

    dt = 0

    while True:
        # Allow user to close game on close button on title bar
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # redraw screen    
        game_screen.fill((80, 80, 80))

        # Flip the display to render the updated screen
        pygame.display.flip()

        # Delta adjust to 60fps
        dt = game_clock.tick(60) / 1000
        print(dt)

if __name__ == "__main__":
    main()