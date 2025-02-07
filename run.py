from first_page import first_page
from first_level import first_level
from final_screen import final_screen
from second_level import second_level
from rules import rules

if __name__ == "__main__":
    run_further = -2

    while run_further != -1:
        # Переход от первой страницы к первой странице или правилам
        run_further = first_page()
        if run_further == 0:
            run_further = first_level()  # Переход к первому уровню
        elif run_further == 3:
            run_further = rules()  # Переход к правилам
            if run_further == 0:
                continue  # Возврат к первой странице

        # Переход от первого уровня к финальному экрану
        if run_further != 1:
            run_further = first_level()
            if run_further == 0:
                run_further = final_screen(1)  # Переход к финальному экрану

        # Переход от финального экрана к второму уровню
        if run_further == 0:
            run_further = second_level()  # Переход ко второму уровню

        # Логика для второго уровня
        while run_further == 2:
            run_further = final_screen(3)  # Переход к финальному экрану 3
            if run_further == 0:
                run_further = second_level()  # Возврат ко второму уровню

        # Переход от второго уровня к финальному экрану 2
        if run_further == 4:
            run_further = final_screen(2)  # Переход к финальному экрану 2
            if run_further == 5:
                continue  # Перезапуск игры

        # Если run_further равно 1, игра завершена
        if run_further == 1:
            break  # Выход из цикла
