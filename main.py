import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    dt = 0
    clock = pygame.time.Clock()
    
    while True:
        # Check if the user exit the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0, 0, 0))
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