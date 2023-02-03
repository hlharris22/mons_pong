import pygame


class Paddle(pygame.sprite.Sprite):
    def __init__(self, image_path, x_pos, y_pos, mov_speed):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect(center=(x_pos, y_pos))
        self.mov_speed = mov_speed

    def update(self):
        # self.rect.center = self.rect.center
        self.screen_constraint()
        pass

    def move(self, direction):
        if direction:
            self.rect.centery += (self.mov_speed * direction)

    def screen_constraint(self):
        if 0 >= self.rect.top:
            self.rect.top = 0
        if 800 <= self.rect.bottom:
            self.rect.bottom = 800
