import pygame
from constants import *

def main():
    pygame.init()
    window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        window.fill('#000000')
        pygame.display.flip()


if __name__ == "__main__":
    main()