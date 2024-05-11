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

        gmanager.add_mode_choosing_btns()
        while gmanager.state == GameState.CHOOSING_MODE:
            screen.fill(config.COLORS["WARM_YELLOW"])
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitend()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    gmanager.mode_choose()
            gmanager.blit_choose_mode(screen)
            pygame.display.flip()
        print(gmanager.current_level)

        while gmanager.state == GameState.PLAYING:
            screen.fill(gmanager.get_curr_lvl().supp_clr)

            if gmanager.current_level >= config.NUM_LEVELS:
                gmanager.state = GameState.FINAL_STATE

quitend()
