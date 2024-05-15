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
        gmanager.blit_init(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitend()
            if event.type == pygame.MOUSEBUTTONDOWN:
                gmanager.state = GameState.CHOOSING_PLAYER
        pygame.display.flip()

    while True:
        gmanager.add_player_choosing_btns()
        while gmanager.state == GameState.CHOOSING_PLAYER:
            screen.fill(config.COLORS["WARM_YELLOW"])
            gmanager.blit_choose_player(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitend()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    gmanager.player_choose()
            pygame.display.flip()
        print(gmanager.players)

        gmanager.add_mode_choosing_btns()
        while gmanager.state == GameState.CHOOSING_MODE:
            screen.fill(config.COLORS["WARM_YELLOW"])
            gmanager.blit_choose_mode(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitend()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    gmanager.mode_choose()
            pygame.display.flip()
        print(gmanager.current_level)

        gmanager.preplay_util()
        while gmanager.state == GameState.PLAYING:
            gmanager.blit_current_level(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitend()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    gmanager.next_level()
            pygame.display.flip()
            

        quitend()

quitend()
