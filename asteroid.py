import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        spawn_one_angle = self.velocity.rotate(angle)
        spawn_two_angle = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_one = Asteroid(self.position[0], self.position[1], new_radius)
        asteroid_one.velocity = spawn_one_angle * 1.2
        asteroid_two = Asteroid(self.position[0], self.position[1], new_radius)
        asteroid_two.velocity = spawn_two_angle * 1.2