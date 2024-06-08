import pygame

from globals.constants.bird import *

class Bird:
    IMGS = BIRD_IMGS
    MAX_ROTATION = BIRD_MAX_ROTATION
    ROT_VEL = BIRD_ROTATION_VELOCITY

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.tilt = 0
        self.tick_count = 0
        self.vel = 0
        self.height = y
        self.img_count = 0
        self.img = self.IMGS[0]

    def jump(self) -> None:
        self.vel = BIRD_JUMP_VELOCITY
        self.tick_count = 0
        self.height = self.y

    def move(self) -> None:
        self.tick_count += 1

        d = self.vel * self.tick_count + BIRD_MOVE_ACCELERATION * self.tick_count ** BIRD_ACC_BASE
        
        if d >= BIRD_MAX_DISTANCE:
            d = BIRD_MAX_DISTANCE
        if d < 0:
            d -= BIRD_NORM_DISTANCE

        self.y = self.y + d

        if d < 0 or self.y < self.height + BIRD_MAX_HEIGHT_FOT_ROTATION:
            if self.tilt < self.MAX_ROTATION:
                self.tilt = self.MAX_ROTATION
        else:
            if self.tilt > BIRD_THRESHOLD_TILT_1:
                self.tilt -= self.ROT_VEL

    def draw(self, win: pygame.surface.Surface):
        self.img_count += 1

        if self.img_count < BIRD_ANIMATION_TIME_1:
            self.img = self.IMGS[0]
        elif self.img_count < BIRD_ANIMATION_TIME_2:
            self.img = self.IMGS[1]
        elif self.img_count < BIRD_ANIMATION_TIME_3:
            self.img = self.IMGS[2]
        elif self.img_count < BIRD_ANIMATION_TIME_4:
            self.img = self.IMGS[1]
        elif self.img_count == BIRD_ANIMATION_TIME_2 + 1:
            self.img = self.IMGS[0]
            self.img_count = 0

        if self.tilt <= BIRD_THRESHOLD_TILT_2:
            self.img = self.IMGS[1]
            self.img_count = BIRD_ANIMATION_TIME_2

        rotated_image = pygame.transform.rotate(self.img, self.tilt)
        new_rect = rotated_image.get_rect(center=self.img.get_rect(topleft = (self.x, self.y)).center)
        win.blit(rotated_image, new_rect.topleft)

    def get_mask(self):
        return pygame.mask.from_surface(self.img)
