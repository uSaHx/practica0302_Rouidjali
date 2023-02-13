import pygame
class Ladrillo:
    def __init__(self, x, y):
        self.image = pygame.image.load()
        self.rect = self.image.get_rect ( x = x, y = y)