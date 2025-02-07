import pygame

from methods import load_image
from coin_class import Coin
from cactus_class import Cactus

def second_level():
    pygame.init()
    size = width, height = 900, 900
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Дом Паши')

    COINS_TIMER = pygame.USEREVENT + 1
    CACTUS_TIMER = pygame.USEREVENT + 2

    bg_1 = load_image("backgrounds/bg_4.jpeg")
    bg_1 = pygame.transform.scale(bg_1, (1600, 1600))

    camera_x = 0
    camera_y = 0

    hero_velocity = 1

    heroes_sprites = pygame.sprite.Group()
    coins_sprites = pygame.sprite.Group()
    cactuses_sprites = pygame.sprite.Group()

    hero_sprite = pygame.sprite.Sprite(heroes_sprites)
    hero_sprite.image = load_image('main_character/stickman.png')
    hero_sprite.image = pygame.transform.scale(hero_sprite.image, (150, 150))
    hero_sprite.rect = hero_sprite.image.get_rect()

    coins_time_span = 3
    coins_for_one_time = 1 # сколько монеток отрисуется за раз
    pygame.time.set_timer(COINS_TIMER, coins_time_span * 1000)# время до появления монетки
    coins_counter = 0 # счетчик для снижения скорости появлениия монетки через каждые три операции
    coins_flag = False

    cactuses_time_span = 3
    pygame.time.set_timer(CACTUS_TIMER, cactuses_time_span * 1000)
    cactuses_counter = 0 # счетчик для снижения скорости появления кактуса через каждые две операции

    left_border_x = hero_sprite.rect.x # границы экрана, после которых вместе с героем начинает двигаться фон
    right_border_x = width - hero_sprite.rect.x
    up_border_y = hero_sprite.rect.y
    down_border_y = height - hero_sprite.rect.y

    icon_image = load_image("icon.jpg")
    pygame.display.set_icon(icon_image)

    exit_flag = 1

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(bg_1, (camera_x, camera_y))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_flag = 1
                running = False
            if event.type == COINS_TIMER:
                for i in range(coins_for_one_time):
                    coin = Coin(coins_sprites, width, height)
                    coins_counter += 1
                if coins_counter % 3 == 0:
                    coins_time_span -= 1 #увеличение скорости появления монеток
                    coins_for_one_time += 1
                    if coins_time_span == 0:
                        coins_flag = True
                pygame.time.set_timer(COINS_TIMER, coins_time_span * 1000)

            if event.type == CACTUS_TIMER:
                cactus = Cactus(cactuses_sprites, width, height)
                cactuses_counter += 1
                if cactuses_counter % 2 == 0:
                    cactuses_time_span -= 1
                pygame.time.set_timer(CACTUS_TIMER, cactuses_time_span * 1000)

        keys = pygame.key.get_pressed()

        if not any(keys):
            hero_flag = True
        else:
            hero_flag = False
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

        coins_sprites.draw(screen)
        cactuses_sprites.draw(screen)
        heroes_sprites.draw(screen)

        pygame.sprite.spritecollide(hero_sprite, coins_sprites, True)

        collided_cactuses = pygame.sprite.spritecollide(hero_sprite, cactuses_sprites, False)
        if collided_cactuses:
            for cactus in collided_cactuses: # Если столкновение произошло, изменить изображение спрайта кактуса
                cactus.change_image()
                exit_flag = 2
                pygame.time.wait(500)
                running = False

        if len(coins_sprites) == 0 and coins_flag is True:
                exit_flag = 4
                running = False

        pygame.display.flip()

    pygame.quit()
    return exit_flag
