""" Scoreboard is shown at the end of a game containing scores and strikes of different players"""
import pygame
import util.config as cfg


class ScoreBoard(pygame.sprite.Sprite):
    """ Sprite class implemening scoreboard"""
    W, H = cfg.SCOREBOARD_SIZE

    def __init__(self, scores, total_strikes):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(cfg.SCOREBOARD_SIZE)
        self.image.fill(cfg.COLORS['SCOREBOARD_BG'])
        self.rect = self.image.get_rect()
        self.rect.center = cfg.SCOREBOARD_POS
        self.place_ptr = (0, 0)
        self.print_titles()

        srt = ScoreBoard.make_sorted_idx(scores)
        for i in srt:
            self.print_player(cfg.BALL_COLORS[i], scores[i], total_strikes[i])


    def print_titles(self):
        """ Prints 'SCOREBOARD' title and 'SCORE STRIKES' subtitle onto scoreboard """
        title = cfg.scoreboard_font1.render('SCOREBOARD', False, cfg.COLORS['BLACK'])
        title_rect = title.get_rect()
        twh = title_rect.center[0]
        title_rect.topleft = (ScoreBoard.W // 2 - twh, (ScoreBoard.H) // 8)
        self.image.blit(title, title_rect)

        subr, subs = ScoreBoard.wide_surface(40)
        vcent = subr.center[1]
        subr.topleft = subr.topleft[0], title_rect.bottomleft[1]
        score_txt = cfg.scoreboard_font2.render('SCORE', False, cfg.COLORS['BLACK'])
        strikes_txt = cfg.scoreboard_font2.render('STRIKES', False, cfg.COLORS['BLACK'])
        cent_txt = score_txt.get_rect().h // 2
        subs.blit(score_txt, (ScoreBoard.H // 2, vcent - cent_txt))
        subs.blit(strikes_txt, (3 * ScoreBoard.H // 4, vcent - cent_txt))
        self.image.blit(subs, subr.topleft)
        self.place_ptr = subr.bottomleft

    def print_player(self, color, score, strikes):
        """ Prints players colored ball, score and strikes onto scoreboard """
        rect, surf = self.wide_surface()
        pygame.draw.rect(surf, cfg.COLORS['SCOREBOARD_BLACK'], ScoreBoard.accent_rect())
        vcent = rect.center[1]
        rect.topleft = self.place_ptr
        self.place_ptr = rect.bottomleft[0], rect.bottomleft[1] + cfg.SCOREBOARD_GAP

        pygame.draw.circle(surf, color, (ScoreBoard.W // 4, vcent - cfg.BALL_RAD), cfg.BALL_RAD)
        score_txt = cfg.scoreboard_font3.render(str(score), False, cfg.COLORS['BLACK'])
        strikes_txt = cfg.scoreboard_font3.render(str(strikes), False, cfg.COLORS['BLACK'])
        cent_txt = score_txt.get_rect().h // 2
        surf.blit(score_txt, (ScoreBoard.H // 2, vcent - cent_txt))
        surf.blit(strikes_txt, (3 * ScoreBoard.H // 4, vcent - cent_txt))

        self.image.blit(surf, rect)

    @staticmethod
    def make_sorted_idx(scores : list[int]) -> list[int]:
        """ Returns sorting permutaion from given scores """
        score_idx = [* enumerate(scores)]
        score_idx = sorted(score_idx, key = lambda tpl: tpl[1], reverse = True)
        return [idx for idx, _ in score_idx]

    @staticmethod
    def accent_rect():
        """ Returns rectangle that can be used to give accent to an area on scoreboard """
        return pygame.Rect(cfg.SCOREBOARD_ACCENT_RECT_POS, cfg.SCOREBOARD_ACCENT_RECT_SIZE)

    @staticmethod
    def wide_surface(height = 50) ->  tuple[pygame.Rect, pygame.Surface]:
        """ Helper function for getting 'line' surface for scoreboard """
        surf = pygame.Surface([ScoreBoard.W, height], pygame.SRCALPHA)
        return surf.get_rect(), surf
