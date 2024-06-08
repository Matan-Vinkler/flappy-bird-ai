import pygame, neat

from models.bird import Bird
from models.pipe import Pipe
from models.base import Base

from globals.utils.draw_window import draw_window

from globals.constants.sys import *
from globals.constants.ml import *

gen_num = 0

def genome_function(gnomes, config):
    global gen_num
    gen_num += 1

    nets = []
    ge = []
    birds: list[Bird] = []

    for _, g in gnomes:
        net = neat.nn.FeedForwardNetwork.create(g, config)
        nets.append(net)
        birds.append(Bird(BIRD_DEFAULT_X, BIRD_DEFAULT_Y))
        g.fitness = 0
        ge.append(g)

    base = Base(BASE_DEFAULT_Y)
    pipes = [Pipe(PIPE_DEFAULT_X)]

    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    clock = pygame.time.Clock()

    score = 0
    still_run = True

    while still_run:
        clock.tick(CLOCK_DEFAULT_TICK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                still_run = False
                pygame.quit()
                quit()

        pipe_ind = 0
        if len(birds) > 0:
            if len(pipes) > 1 and birds[0].x > pipes[0].x + pipes[0].PIPE_TOP.get_width():
                pipe_ind = 1
        else:
            still_run = False
            break

        for x, bird in enumerate(birds):
            bird.move()
            ge[x].fitness += FITNESS_SLIGHT_GAIN

            outputs = nets[x].activate((bird.y, abs(bird.y - pipes[pipe_ind].height), abs(bird.y - pipes[pipe_ind].bottom)))
            if(outputs[0] > OUTPUT_JUMP_THRESHOLD):
                bird.jump()

        rem = []
        add_pipe = False

        for pipe in pipes:
            for x, bird in enumerate(birds):
                if pipe.collide(bird):
                    ge[x].fitness -= FITNESS_AMOUNT_LOSE
                    birds.pop(x)
                    nets.pop(x)
                    ge.pop(x)

                if not pipe.passed and pipe.x < bird.x:
                    pipe.passed = True
                    add_pipe = True

            if pipe.x + pipe.PIPE_TOP.get_width() < 0:
                rem.append(pipe)

            pipe.move()

        if add_pipe:
            score += 1
            for g in ge:
                g.fitness += FITNESS_AMOUNT_GAIN
            pipes.append(Pipe(PIPE_DEFAULT_X))

        for r in rem:
            pipes.remove(r)

        for x, bird in enumerate(birds):
            if bird.y + bird.img.get_height() >= BIRD_BASE_COLLIDE_HEIGHT or bird.y < 0:
                birds.pop(x)
                nets.pop(x)
                ge.pop(x)

        base.move()

        draw_window(win, birds, pipes, base, score, gen_num)