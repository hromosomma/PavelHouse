import pygame

from button_class import Button
from first_level import load_image


def first_page():
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

    running = True

    start_button = Button(width // 2 - 150, height // 2 - 100, 300, 100, "Start",
                          "assets/buttons/button_1.png", "assets/buttons/button_1_hovered.png",
                          "assets/sounds/pushed_button.mp3")
    rules_button = Button(width // 2 - 150, height // 2 + 100, 300, 100, "Rules",
                          "assets/buttons/button_1.png", "assets/buttons/button_1_hovered.png",
                          "assets/sounds/pushed_button.mp3")

    font = pygame.font.Font("assets/fonts/Daydream.ttf", 40)
    title_surface = font.render("Pasha's House", True, (255, 255, 255))
    title_rect = title_surface.get_rect(center=(width // 2, 100))

    exit_flag = 1

    while running:
        screen.fill((0, 0, 0))
        screen.blit(bg_home_screen, (camera_x, camera_y))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_flag = 1
                running = False
            start_button.handle_event(event)
            rules_button.handle_event(event)

            if event.type == pygame.USEREVENT and event.button == start_button:
                start_button.sound.play()
                pygame.time.wait(500)
                exit_flag = 0
                running = False

            if event.type == pygame.USEREVENT and event.button == rules_button:
                rules_button.sound.play()
                pygame.time.wait(500)
                exit_flag = 3
                running = False

        start_button.draw(screen)
        start_button.check_hover(pygame.mouse.get_pos())

        rules_button.draw(screen)
        rules_button.check_hover(pygame.mouse.get_pos())

        screen.blit(title_surface, title_rect)

        pygame.display.flip()

    pygame.quit()
    return exit_flag
