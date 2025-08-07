from constants import * 
from circleshape import *
import pygame


class Shot(CircleShape):
    def __init__(self, x, y, rotation):
        super().__init__(x, y, SHOT_RADIUS)
        self.rotation = rotation
        self.velocity = pygame.Vector2(0,1).rotate(rotation) * PLAYER_SHOOT_SPEED

        

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)

    
    def update(self, dt):
        self.position += (self.velocity * dt)