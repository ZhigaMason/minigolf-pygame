import pygame
import config as cfg
from game_manager import GameManager, GameState

pygame.init()
screen = pygame.display.set_mode(cfg.SCREEN_SIZE)
clock = pygame.time.Clock()
gmanager = GameManager()
def quitend():
    pygame.display.quit()
    pygame.quit()
    exit(0)

if __name__ == '__main__':
    while gmanager.state == GameState.INITIAL_STATE:
        screen.fill(cfg.COLORS["BLACK"])
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
            screen.fill(cfg.COLORS["WARM_YELLOW"])
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
            screen.fill(cfg.COLORS["WARM_YELLOW"])
            gmanager.blit_choose_mode(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitend()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    gmanager.mode_choose()
            pygame.display.flip()
        print(gmanager.current_level)

        draw_arrow = False
        gmanager.preplay_util()
        while gmanager.state == GameState.PLAYING:
            dt = clock.tick(cfg.FPS) / 100
            gmanager.update_physics()
            gmanager.update_visuals()
            gmanager.update_logic()
            gmanager.blit_current_level(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitend()
                if event.type == pygame.MOUSEBUTTONDOWN and gmanager.pos_in_current_ball(pygame.mouse.get_pos()):
                    gmanager.draw_arrow()
                    draw_arrow = True
                if event.type == pygame.MOUSEBUTTONUP and draw_arrow:
                    gmanager.leave_arrow()
                    draw_arrow = False
            pygame.display.flip()
            

        quitend()

quitend()
