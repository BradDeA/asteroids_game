import pygame
from constants import *

def main():
    pygame.init()
    window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    time = pygame.time.Clock()
    dt = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        window.fill('#000000')
        pygame.display.flip()
        miliseconds = time.tick(60)
        dt = miliseconds / 1000


if __name__ == "__main__":
    main()