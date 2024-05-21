import pygame
import pygame.gfxdraw
import config as cfg
from math import pi
from pygame.math import Vector2 as v2

class TextSprite(pygame.sprite.Sprite):
    def __init__(self, label, w, h, bg_color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([w, h], pygame.SRCALPHA)
        self.image.fill(bg_color)
        lrect = label.get_rect();
        self.image.blit(label, (w // 2 - lrect.w // 2, h // 2 - lrect.h // 2 ))
        self.rect = self.image.get_rect()

class SelectButton(TextSprite):

    def __init__(self, label, info, w = 240, h = 360, color = cfg.COLORS['WHITE']):
        TextSprite.__init__(self, label, w, h, color)
        self.info = info

    def inrect(self, x, y) -> bool:
        return self.rect.topleft[0] <= x and self.rect.topleft[1] <= y and x <= self.rect.bottomright[0] and y <= self.rect.bottomright[1]

    def is_clicked(self) -> bool:
        print(self.rect, pygame.mouse.get_pos())
        return pygame.mouse.get_pressed()[0] and self.inrect(*pygame.mouse.get_pos())

class RisingLabel(TextSprite):

    def __init__(self, label, w = 100, h = 50, bg_color = cfg.COLORS['NULL'], alt = 100, acc = 2):
        TextSprite.__init__(self, label, w, h, bg_color)
        self.alt = alt
        self.vel = 0
        self.acc = acc

    def update(self, dt, *args, **kwargs):
        self.vel += dt * self.acc
        s = dt * self.vel
        self.alt -= s
        self.rect.center = self.rect.center[0], self.rect.center[1] - s
        if self.alt <= 0:
            self.kill()

class TurnIndecator(pygame.sprite.Sprite):

    def __init__(self, pos, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(cfg.TURN_ID_SIZE, pygame.SRCALPHA)
        self.image.fill(cfg.COLORS['NULL'])
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.clr = color
        self.ang_offset = 0
        self.draw_self()

    def draw_self(self):
        self.image.fill(cfg.COLORS['NULL'])
        r = cfg.TURN_ID_RAD
        c = cfg.TURN_ID_CENTER
        ang_seg = int(120 / cfg.TURN_ID_STROKES)
        for i in range(cfg.TURN_ID_STROKES):
            a = 3*i*ang_seg + int(self.ang_offset)
            b = (3*i+1)*ang_seg + int(self.ang_offset)
            for w in range(cfg.TURN_ID_WIDTH):
                pygame.gfxdraw.arc(self.image, *c, r - w, a, b, self.clr)

    def update(self, dt, *args, **kwargs):
        self.ang_offset += cfg.TURN_ID_SPEED*dt
        self.draw_self()

class ScoreBoard(pygame.sprite.Sprite):
    W, H = cfg.SCOREBOARD_SIZE

    def __init__(self, scores, total_strikes):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(cfg.SCOREBOARD_SIZE)
        self.image.fill(cfg.COLORS['SCOREBOARD_BG'])
        self.rect = self.image.get_rect()
        self.rect.center = cfg.SCOREBOARD_POS
        self.place_ptr = (0, 0)
        self.print_title()

        srt = ScoreBoard.make_sorted_idx(scores)
        for i in srt:
            self.print_player(cfg.BALL_COLORS[i], scores[i], total_strikes[i])


    def print_title(self):
        title = cfg.scoreboard_font1.render('SCOREBOARD', False, cfg.COLORS['BLACK'])
        title_rect = title.get_rect()
        twh, thh = title_rect.center
        title_rect.topleft = (ScoreBoard.W // 2 - twh, (ScoreBoard.H + thh) // 5)
        self.image.blit(title, title_rect)

        subr, subs = self.wide_surface(40)
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
        score_idx = [* enumerate(scores)]
        score_idx = sorted(score_idx, key = lambda tpl: tpl[1], reverse = True)
        return [idx for idx, _ in score_idx]
        

    def wide_surface(self, height = 50) ->  tuple[pygame.Rect, pygame.Surface]:
        surf = pygame.Surface([ScoreBoard.W, height], pygame.SRCALPHA)
        return surf.get_rect(), surf
    
    @staticmethod
    def accent_rect():
        return pygame.Rect(ScoreBoard.H // 8, 0, 3 * ScoreBoard.H // 4, 50 )

