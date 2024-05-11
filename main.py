import pygame
import config
from game_manager import GameManager, GameState

pygame.init()
screen = pygame.display.set_mode(config.SCREEN_SIZE)
clocck = pygame.time.Clock()
gmanager = GameManager()
def quitend():
    pygame.display.quit()
    pygame.quit()
    exit(0)

if __name__ == '__main__':
    while gmanager.state == GameState.INITIAL_STATE:
        screen.fill(config.COLORS["BLACK"])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitend()
            if event.type == pygame.MOUSEBUTTONDOWN:
                gmanager.state = GameState.CHOOSING_PLAYER
        gmanager.blit_init(screen)
        pygame.display.flip()

    while True:
        gmanager.add_player_choosing_btns()
        while gmanager.state == GameState.CHOOSING_PLAYER:
            screen.fill(config.COLORS["WARM_YELLOW"])
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitend()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    gmanager.player_choose()
            gmanager.blit_choose_player(screen)
            pygame.display.flip()

        print(gmanager.players)


quitend()
