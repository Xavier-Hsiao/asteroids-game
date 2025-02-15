import pygame

# Base class for game objects
# asteroids and users are all circle objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # Check if it needs to init with groups
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius
    
    def draw(self, screen):
        pass

    def update(self, dt):
        pass

    def collides_with(self, another_circleshape):
        distance = self.position.distance_to(another_circleshape.position)
        return distance <= self.radius + another_circleshape.radius
