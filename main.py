import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
game_clock = pygame.time.Clock()
dt = 0
drawables = pygame.sprite.Group()
updatables = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
Player.containers = (drawables, updatables)
Asteroid.containers = (asteroids, drawables, updatables)
AsteroidField.containers = (updatables)

def game_loop(dt, player):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for d in drawables:
            d.draw(screen)
        for u in updatables:
            u.update(dt)
        for a in asteroids:
            if a.collision(player):
                print("Game over!")
                sys.exit()
        pygame.display.flip()
        dt = game_clock.tick(60) / 1000

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
    asteroid_field = AsteroidField()
    game_loop(dt, player)


if __name__ == "__main__":
    main()