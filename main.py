import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    pygame.time.Clock
    
    dt = 0
    
    while True:
        pygame.Surface.fill(screen, (0,0,0))
        for event in pygame.event.get():
            pygame.tick(60) = delta
            dt = delta/1000
            
            if event.type == pygame.QUIT:
                return
        pygame.display.flip()


    print("Starting Asteroids!")
    print("Screen width: 1280")
    print("Screen height: 720")

if __name__ == "__main__":
    main()