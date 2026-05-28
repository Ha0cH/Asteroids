from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS 
import pygame
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt: float) -> None:
        self.position += self.velocity * dt
    
    def split(self):
        self.kill() # remove the original asteroid

        if self.radius <= ASTEROID_MIN_RADIUS:
            return # too small to split, just remove it
        else:
            log_event("asteroid_split")
            random_angle = random.uniform(20, 50)
            first_velocity = self.velocity.rotate(random_angle)
            second_velocity = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            Asteroid(self.position.x, self.position.y, new_radius).velocity = first_velocity * 1.2
            Asteroid(self.position.x, self.position.y, new_radius).velocity = second_velocity * 1.2
            
            


