import pygame

# Функція для малювання діалогового табло
def draw_dialog_box(display, font, text, options):
    # Малюємо прямокутник табло
    dialog_box = pygame.Rect(50, 400, 500, 150)
    pygame.draw.rect(display, (200, 200, 200), dialog_box)
    pygame.draw.rect(display, (0, 0, 0), dialog_box, 2)

    # Малюємо текст
    dialog_text = font.render(text, True, (0, 0, 0))
    display.blit(dialog_text, (dialog_box.x + 10, dialog_box.y + 10))

    # Малюємо кнопки
    for i, option in enumerate(options):
        button = pygame.Rect(dialog_box.x + 10, dialog_box.y + 50 + i * 40, 480, 30)
        pygame.draw.rect(display, (255, 255, 255), button)
        pygame.draw.rect(display, (0, 0, 0), button, 2)
        option_text = font.render(option, True, (0, 0, 0))
        display.blit(option_text, (button.x + 10, button.y + 5))