import pygame
from config import SCREEN_SIZE
from game_manager import GameManager, GameState

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
clocck = pygame.time.Clock()
gmanager = GameManager()

def quitend():
    pygame.display.quit()
    pygame.quit()
    exit(0)

if __name__ == '__main__':
    while gmanager.state == GameState.INITIAL_STATE:
        screen.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("asdasda")
                quitend()
            if event.type == pygame.MOUSEBUTTONDOWN:
                gmanager.state = GameState.CHOOSING_PLAYER
        gmanager.blit_init(screen)
        pygame.display.flip()


quitend()
