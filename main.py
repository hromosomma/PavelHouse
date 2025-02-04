import os
import random
import pygame

def load_image(name, colorkey=None):
    fullname = os.path.join('assets', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением {fullname} не найден")
        return None  # Изменено на None
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Coin(pygame.sprite.Sprite):
    def __init__(self, sprite_group, screen_width, screen_height):
        super().__init__(sprite_group)
        self.image = load_image("coin.png")
        self.image = pygame.transform.scale(self.image, (75, 75))
        self.rect = self.image.get_rect()

        coin_width, coin_height = self.image.get_size()
        self.rect.x = random.randint(coin_width + 5, screen_width - coin_width - 5)
        self.rect.y = random.randint(coin_height + 5, screen_height - coin_height - 5)


if __name__ == "__main__":
    pygame.init()
    size = width, height = 900, 900
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Дом Паши')

    COINS_TIMER = pygame.USEREVENT + 1

    bg_1 = load_image("backgrounds/bg_1.jpeg")
    bg_1 = pygame.transform.scale(bg_1, (3200, 6400))
    bg_width, bg_height = bg_1.get_size()

    camera_x = 0
    camera_y = 0

    hero_velocity = 1

    heroes_sprites = pygame.sprite.Group()
    coins_sprites = pygame.sprite.Group()

    hero_sprite = pygame.sprite.Sprite(heroes_sprites)
    hero_sprite.image = load_image('pigeon_main_character/pigeon.png')
    hero_sprite.image = pygame.transform.scale(hero_sprite.image, (150, 150))
    hero_sprite.rect = hero_sprite.image.get_rect()

    clock = pygame.time.Clock
    coins_time_span = 10 # время до появления монетки

    if hero_sprite.image:  # Проверка на существование изображения
        hero_width, hero_height = hero_sprite.image.get_size()
        hero_sprite.rect.x = width // 2 - (hero_width // 2)
        hero_sprite.rect.y = height // 2 - (hero_height // 2)

    left_border_x = hero_sprite.rect.x # границы экрана, после которых вместе с героем начинает двигаться фон
    right_border_x = width - hero_sprite.rect.x
    up_border_y = hero_sprite.rect.y
    down_border_y = height - hero_sprite.rect.y

    icon_image = load_image("icon.jpg")
    pygame.display.set_icon(icon_image)

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(bg_1, (camera_x, camera_y))

        coins_sprites.draw(screen)
        heroes_sprites.draw(screen)

        pygame.time.set_timer(COINS_TIMER, coins_time_span)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == COINS_TIMER:
                coin = Coin(coins_sprites, width, height)
                coins_time_span -= 1 #увеличение скорости появления монеток
                pygame.time.set_timer(COINS_TIMER, coins_time_span)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if hero_sprite.rect.x < width - hero_sprite.rect.width:  # Проверка правой границы
                hero_sprite.rect.x += hero_velocity

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if hero_sprite.rect.x > 0:  # Проверка левой границы
                hero_sprite.rect.x -= hero_velocity

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            if hero_sprite.rect.y > 0:  # Проверка верхней границы
                hero_sprite.rect.y -= hero_velocity

        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            if hero_sprite.rect.y < height - hero_sprite.rect.height:  # Проверка нижней границы
                hero_sprite.rect.y += hero_velocity

        camera_x = -hero_sprite.rect.x + width // 2  # Обновляем положение камеры
        camera_y = -hero_sprite.rect.y + height // 2

        if camera_x < -2280:
            camera_x = -2280
        if camera_x > 0:
            camera_x = 0
        if camera_y > -35:
            camera_y = -35
        if camera_y < -5550:
            camera_y = -5550

        pygame.sprite.spritecollide(hero_sprite, coins_sprites, True)

        pygame.display.flip()

    pygame.quit()
