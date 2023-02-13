import pygame
class Brick:
    def __init__(self, x, y, imagen):
        self.image = pygame.image.load(imagen)
        self.image = pygame.transform.scale(self.image, (150, 200))
        self.rect = self.image.get_rect(x=x,y=y)