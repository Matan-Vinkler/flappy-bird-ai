import pygame

from models.bird import Bird
from models.pipe import Pipe
from models.base import Base

from globals.constants.sys import *

def draw_window(win: pygame.surface.Surface, birds: list[Bird], pipes: list[Pipe], base: Base, score, gen):
    win.blit(BG_IMG, (0, 0))

    text = STAT_FONT.render(SCORE_MSG + str(score), True, STAT_FONT_COLOR)
    win.blit(text, (WIN_WIDTH - text.get_width() - STAT_WIDTH_NORM, STAT_HEIGHT))

    text = STAT_FONT.render(GEN_MSG + str(gen), True, STAT_FONT_COLOR)
    win.blit(text, (GEN_MSG_X, GEN_MSG_Y))

    for pipe in pipes:
        pipe.draw(win)

    for bird in birds:
        bird.draw(win)

    base.draw(win)

    pygame.display.update()