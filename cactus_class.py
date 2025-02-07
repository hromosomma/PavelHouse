import pygame
import random

from methods import load_image


class Cactus(pygame.sprite.Sprite):
    def __init__(self, sprite_group, screen_width, screen_height):
        super().__init__(sprite_group)
        self.image = load_image("cactuses/cactus.png")
        self.image = pygame.transform.scale(self.image, (65, 65))

        self.rect = pygame.Rect(0, 0, 50, 50)

        cactus_width, cactus_height = self.image.get_size()
        self.rect.x = random.randint(0, screen_width - self.rect.width)
        self.rect.y = random.randint(0, screen_height - self.rect.height)

    def change_image(self):
        self.image = load_image("cactuses/cactus_exploding.png")
        self.image = pygame.transform.scale(self.image, (65, 65))
        self.rect = self.image.get_rect()
