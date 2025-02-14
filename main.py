import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    dt = 0
    clock = pygame.time.Clock()

    # create groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    # add all instance of Player to groups
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        # Check if the user exit the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)
        screen.fill((0, 0, 0))
        for item in drawable:
            item.draw(screen)
        
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