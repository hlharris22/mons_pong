import pygame


class Transformer:

    @staticmethod
    def clip(surface, x, y, x_size, y_size):
        handle_surface = surface.copy()
        clip_rect = pygame.Rect(x, y, x_size, y_size)
        handle_surface.set_clip(clip_rect)
        image = surface.subsurface(handle_surface.get_clip())
        return image.copy()
