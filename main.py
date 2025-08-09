import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *


def main():
    pygame.init()
    game_clock = pygame.time.Clock() 
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    game_loop = True
    score = 0


    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()
    while game_loop == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0), rect=None, special_flags=0)
        
        updatable.update(dt)

        for item in asteroids:
            if player.collision(item):
                pass
            else:
                print("Game over!")
                print(f"Score: {score} ")
                sys.exit(1)
        for a in asteroids:
            for s in shots:
                if s.collision(a):
                    pass
                else:
                    if a.radius <= ASTEROID_MIN_RADIUS:
                        score += 10
                    else:
                        score += 1
                    s.kill()
                    a.split()
                    
                    updatable.update(0)
        for item in drawable:
            item.draw(screen)
            
        pygame.display.flip()
        dt = game_clock.tick(60)/1000


if __name__ == "__main__":
    main()
