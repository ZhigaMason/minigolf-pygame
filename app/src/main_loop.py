import pygame
import util.config as cfg
from src.game.manager import GameManager, GameState

def quitend():
    pygame.display.quit()
    pygame.quit()
    exit(0)

def start():
    pygame.init()
    screen = pygame.display.set_mode(cfg.SCREEN_SIZE)
    clock = pygame.time.Clock()
    gmanager = GameManager()

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

        gmanager.add_start_level_choosing_btns()
        while gmanager.state == GameState.CHOOSING_MODE:
            screen.fill(cfg.COLORS["WARM_YELLOW"])
            gmanager.blit_choose_mode(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitend()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    gmanager.mode_choose()
            pygame.display.flip()

        draw_arrow = False
        gmanager.preplay_util()
        while gmanager.state == GameState.PLAYING:
            dt = clock.tick(cfg.FPS) / 100
            gmanager.blit_current_level(screen)
            gmanager.update_physics()
            gmanager.update_visuals(dt)
            gmanager.update_logic()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitend()
                if all((event.type == pygame.MOUSEBUTTONDOWN, gmanager.pos_in_current_ball(pygame.mouse.get_pos()), not gmanager.any_movement())):
                    gmanager.draw_arrow()
                    draw_arrow = True
                if event.type == pygame.MOUSEBUTTONUP and draw_arrow:
                    gmanager.leave_arrow()
                    draw_arrow = False
            if gmanager.movement_stopped():
                gmanager.next_plr()
            pygame.display.flip()

        gmanager.add_score_board()
        gmanager.add_final_buttons()
        while gmanager.state == GameState.FINAL_STATE:
            screen.fill(cfg.COLORS["GREEN"])
            gmanager.blit_score_board(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitend()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    gmanager.restart_choose()
            pygame.display.flip()
        
        if gmanager.state == GameState.EXIT:
            break
        gmanager.reset()
    quitend()

