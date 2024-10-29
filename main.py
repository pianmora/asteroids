# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame # type: ignore
from constants import *
from player import Player

def main():
    pygame.init()
    
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Set up the main game screen
    game_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Set up the game clock
    game_clock = pygame.time.Clock()

    # delta time
    dt = 0

    while True:
        # Allow user to close game on close button on title bar
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # redraw screen    
        game_screen.fill((20, 20, 20))

        # Draw player
        game_player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
        game_player.draw(game_screen)
        game_player.update(dt)

        # Flip the display to render the updated screen
        pygame.display.flip()

        # Delta adjust to 60fps
        dt = game_clock.tick(60) / 1000

if __name__ == "__main__":
    main()