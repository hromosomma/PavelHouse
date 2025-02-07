import pygame

from methods import load_image
from button_class import Button


def final_screen(n):
    pygame.init()
    size = width, height = 900, 900
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Дом Паши')

    bg_final = load_image("backgrounds/bg_3.jpeg")
    bg_final = pygame.transform.scale(bg_final, (1600, 1600))
    bg_final_size = final_width, final_height = bg_final.get_size()

    continue_button = Button(width // 2 - 150, height // 2, 300, 100,"Continue!",
                          "assets/buttons/button_2.png", "assets/buttons/button_2_hovered.png",
                           "assets/sounds/pushed_button.mp3")

    replay_button = Button(width // 2 - 150, height // 2, 300, 100, "Play again",
                             "assets/buttons/button_2.png", "assets/buttons/button_2_hovered.png",
                             "assets/sounds/pushed_button.mp3")

    again_button = Button(width // 2 - 150, height // 2, 300, 100, "Play again",
                           "assets/buttons/button_2.png", "assets/buttons/button_2_hovered.png",
                           "assets/sounds/pushed_button.mp3")

    font = pygame.font.Font("assets/fonts/Daydream.ttf", 20)
    text_1_surface = font.render("Congrats! You passed the WHOOOLE level!", True, (255, 255, 255))
    text_1_rect = text_1_surface.get_rect(center=(width // 2 + 30, 100))
    text_2_surface = font.render("Hooray, you've done it! Game over!", True, (255, 255, 255))
    text_2_rect = text_2_surface.get_rect(center=(width // 2 + 30, 100))
    text_3_surface = font.render("Exploded cactus killed you. Wanna play again?", True, (255, 255, 255))
    text_3_rect = text_3_surface.get_rect(center=(width // 2 + 30, 100))

    running_1 = False
    running_2 = False
    dead_running = False
    if n == 1:
        running_1 = True
    if n == 2:
        running_2 = True
    if n == 3:
        dead_running = True

    exit_flag = 1

    while running_1: # финальный экран после первого уровня
        screen.fill((0, 0, 0))
        screen.blit(bg_final, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_flag = 1
                running_1 = False
            if event.type == pygame.USEREVENT and event.button == continue_button:
                continue_button.sound.play()
                pygame.time.wait(500)
                exit_flag = 0
                running_1 = False
            continue_button.handle_event(event)

        continue_button.draw(screen)
        continue_button.check_hover(pygame.mouse.get_pos())

        screen.blit(text_1_surface, text_1_rect)

        pygame.display.flip()

    while running_2: # финальный экран после второго уровня
        screen.fill((0, 0, 0))
        screen.blit(bg_final, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_flag = 1
                running_2 = False
            if event.type == pygame.USEREVENT and event.button == again_button:
                again_button.sound.play()
                exit_flag = 5
                pygame.time.wait(500)
                running_2 = False
            again_button.handle_event(event)

        again_button.draw(screen)
        again_button.check_hover(pygame.mouse.get_pos())

        screen.blit(text_2_surface, text_2_rect)

        pygame.display.flip()

    while dead_running:
        screen.fill((0, 0, 0))
        screen.blit(bg_final, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_flag = 1
                dead_running = False
            if event.type == pygame.USEREVENT and event.button == replay_button:
                replay_button.sound.play()
                pygame.time.wait(500)
                exit_flag = 0
                dead_running = False
            replay_button.handle_event(event)

        replay_button.draw(screen)
        replay_button.check_hover(pygame.mouse.get_pos())

        screen.blit(text_3_surface, text_3_rect)

        pygame.display.flip()

    pygame.quit()
    return exit_flag
