import pygame
from player import *
from constants import *
from asteroid import *
from asteroidfield import *
from circleshape import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()

    asteroid = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shot = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Shot.containers = (updatable, drawable, shot)
    Asteroid.containers = (asteroid, updatable, drawable)
    AsteroidField.containers = (updatable)

    asteroidfield = AsteroidField()

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)

    dt = 0

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    running = True
    while running:
        tick_rate = clock.tick(60)
        dt = tick_rate/1000

        pygame.Surface.fill(screen, (0,0,0))

        updatable.update(dt)

        for asteroids in asteroid:
            if player.collision_check(asteroids) == True:
                print("Game over!")
                pygame.quit()
                exit()

        for asteroids in asteroid:
            for bullet in shot:
                if bullet.collision_check(asteroids):
                    bullet.kill()
                    asteroids.split()    

        for object in drawable:
            object.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.display.flip()



if __name__ == "__main__":
    main()