import pygame
from methods import load_image
from button_class import Button

def rules():
    pygame.init()
    size = width, height = 900, 900
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Дом Паши')

    icon_image = load_image("icon.jpg")
    pygame.display.set_icon(icon_image)

    bg_home_screen = load_image("backgrounds/bg_2.jpeg")
    if bg_home_screen is None:  # Проверка загрузки изображения
        print("Не удалось загрузить фоновое изображение.")
        pygame.quit()
        exit()
    bg_home_screen = pygame.transform.scale(bg_home_screen, (1000, 1000))
    bg_width, bg_height = bg_home_screen.get_size()

    camera_x = 0
    camera_y = 0

    exit_button = Button(100, 100, 250, 100, "Main Menu",
                          "assets/buttons/button_1.png", "assets/buttons/button_1_hovered.png",
                          "assets/sounds/pushed_button.mp3")

    running = True

    exit_flag = 1

    font = pygame.font.Font("assets/fonts/Daydream.ttf", 25)
    rule_1_surface = font.render("Use W, A, S, D or arrow keys to move", True, (255, 255, 255))
    rule_1_rect = rule_1_surface.get_rect(center=(width // 2, 400))

    rule_2_surface = font.render("Don't come closer to cactuses!", True, (255, 255, 255))
    rule_2_rect = rule_1_surface.get_rect(center=(width // 2, 500))

    rule_3_surface = font.render("Don't tell anyone about fight club", True, (255, 255, 255))
    rule_3_rect = rule_3_surface.get_rect(center=(width // 2, 600))

    while running:
        screen.fill((0, 0, 0))
        screen.blit(bg_home_screen, (camera_x, camera_y))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_flag = 1
                running = False
            exit_button.handle_event(event)

            if event.type == pygame.USEREVENT and event.button == exit_button:
                exit_button.sound.play()
                pygame.time.wait(500)
                exit_flag = 0
                running = False

        exit_button.draw(screen)
        exit_button.check_hover(pygame.mouse.get_pos())

        exit_button.draw(screen)
        exit_button.check_hover(pygame.mouse.get_pos())

        screen.blit(rule_1_surface, rule_1_rect)
        screen.blit(rule_2_surface, rule_2_rect)
        screen.blit(rule_3_surface, rule_3_rect)

        pygame.display.flip()

    pygame.quit()
    return exit_flag