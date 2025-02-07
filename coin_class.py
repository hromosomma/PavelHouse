import pygame
import random
from methods import load_image

class Coin(pygame.sprite.Sprite):
    def __init__(self, sprite_group, screen_width, screen_height):
        super().__init__(sprite_group)
        self.image = load_image("coin.png")
        self.image = pygame.transform.scale(self.image, (75, 75))
        self.rect = self.image.get_rect()

        coin_width, coin_height = self.image.get_size()
        self.rect.x = random.randint(coin_width + 5, screen_width - coin_width - 5)
        self.rect.y = random.randint(coin_height + 5, screen_height - coin_height - 5)
