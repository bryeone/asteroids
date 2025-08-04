import pygame
from constants import *
from player import *


def main():
    pygame.init()
    game_clock = pygame.time.Clock() 
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    game_loop = True

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    while game_loop == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0), rect=None, special_flags=0)
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()
        dt = game_clock.tick(60)/1000


if __name__ == "__main__":
    main()
