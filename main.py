import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0
    clock = pygame.time.Clock()
    
    while True:
        # Check if the user exit the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        player.update(dt)
        screen.fill((0, 0, 0))
        player.draw(screen)
        
        # Update the full display Surface to the screen
        pygame.display.flip()

        # Pause the game loop until 1/60th of a sec passed
        # Return the delta time 
        dt = clock.tick(60) / 1000

    # print("Starting asteroids!")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")



# Ensure that main.py is called directly
if __name__ == "__main__":
    main()