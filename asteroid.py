from curses import COLOR_WHITE
import random
import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y , radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            rand_angle = random.uniform(20, 50)
            new_direction_1 = self.velocity.rotate(rand_angle)
            new_direction_2 = self.velocity.rotate(-rand_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            split_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            split_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
            
            split_asteroid_1.velocity = new_direction_1 * 1.2
            split_asteroid_2.velocity = new_direction_2