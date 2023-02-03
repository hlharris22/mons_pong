import pygame
import random


class Ball(pygame.sprite.Sprite):
    def __init__(self, image, x_start_pos, y_start_pos, x_speed, y_speed):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center=(x_start_pos, y_start_pos))
        self.speed = 20
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.bounce = False

    def update(self):
        self.move()

    def move(self):
        self.rect.centerx += self.x_speed
        self.rect.centery += self.y_speed
        self.bounce_direction()

    def bounce(self):
        self.bounce = True

    def bounce_direction(self):
        if self.rect.bottom >= 800:
            if self.x_speed < 0 and not self.bounce:
                self.y_speed *= -1.5
            else:
                self.y_speed *= -1
        elif self.rect.top <= 0:
            if self.x_speed < 0 and not self.bounce:
                self.y_speed *= -1.5
            else:
                self.y_speed *= -1

    def constraint(self):
        pass

