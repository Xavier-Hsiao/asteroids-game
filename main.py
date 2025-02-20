import sys
import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    dt = 0
    clock = pygame.time.Clock()

    # create groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    # add all relevant instance to its groups
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        # Check if the user exit the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)
        screen.fill((0, 0, 0))
        
        # Detect collision between player and asteroids
        for ast in asteroids:
            if ast.collides_with(player):
                print("Game over!")
                sys.exit()

            # Detect collision between asteroids and bullets
            for bullet in shots:
                if bullet.collides_with(ast):
                    ast.split()
                    bullet.kill()
        
        for item in drawable:
            item.draw(screen)
        
        # Update the full display Surface to the screen
        pygame.display.flip()

        # Pause the game loop until 1/60th of a sec passed
        # Return the delta time 
        dt = clock.tick(60) / 1000

# Ensure that main.py is called directly
if __name__ == "__main__":
    main()