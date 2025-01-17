import pygame
import os
import dialog  # Assuming dialog.py contains your custom dialog handling code

pygame.init()

# Параметри екрана
WIDTH, HEIGHT = 600, 600
display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Гра з діалогами")

# Шрифт
FONT = pygame.font.Font(None, 30)

clock = pygame.time.Clock()

geroy = pygame.Rect(65, 65, 29, 22)
portal_rect = pygame.Rect(400, 400, 40, 40)
mage = pygame.Rect(370, 170, 40, 40)

go_right = go_left = go_up = go_down = False

dir_path = os.path.dirname(__file__)

TILE_SIZE = 40  # Розмір текстур: 40x40

wizard = pygame.image.load(dir_path + "/all_textures/cafe/wizard.png")
mage = pygame.Rect(370, 170, 40, 40)

textures_images = {
    2: pygame.image.load(dir_path + "/all_textures/nothing.png"),
    3: pygame.image.load(dir_path + "/all_textures/textures_left/wall_left.png"),
    4: pygame.image.load(dir_path + "/all_textures/textures_left/wall_up_left.png"),
    5: pygame.image.load(dir_path + "/all_textures/textures_left/wall_down_left.png"),
    6: pygame.image.load(dir_path + "/all_textures/textures_up/wall_up.png"),
    7: pygame.image.load(dir_path + "/all_textures/textures_down/wall_down.png"),
    8: pygame.image.load(dir_path + "/all_textures/cafe/cafe.png"),
    9: pygame.image.load(dir_path + "/all_textures/textures_right/wall_right.png"),
    10: pygame.image.load(dir_path + "/all_textures/textures_right/wall_up_right.png"),
    11: pygame.image.load(dir_path + "/all_textures/textures_right/wall_down_right.png"),
    12: pygame.image.load(dir_path + "/all_textures/one_wall.png"),
    13: pygame.image.load(dir_path + "/all_textures/cafe/cafe_floor.png"),
    14: pygame.image.load(dir_path + "/all_textures/decorations/flover.png"),
    15: pygame.image.load(dir_path + "/all_textures/stone.png"),
    16: pygame.image.load(dir_path + "/all_textures/decorations/rock.png")
}

portal_texture = pygame.image.load(dir_path + "/all_textures/portal.png")
teleport_back_image = pygame.image.load(dir_path + "/all_textures/portal.png")  # Додаємо сюди

hero = pygame.image.load(dir_path + "/all_textures/wicked_cat_right.png")

#-------------ігрове поле нашої гри

initial_textures = [
    [4,6,6,6,6,6,6,6,6,6,6,6,6,6,10],
    [3,2,2,2,2,2,2,2,2,2,2,2,2,2,9],
    [3,2,2,2,2,2,2,2,2,14,2,2,2,2,9],
    [3,2,2,2,2,2,2,2,2,2,2,2,12,2,9],
    [3,2,2,2,2,2,2,2,2,2,2,2,2,2,9],
    [3,2,2,12,2,2,2,2,2,2,2,2,2,2,9],
    [3,2,16,2,2,2,2,2,2,2,2,8,2,2,9],
    [3,2,2,2,2,2,2,2,2,2,2,2,2,2,9],
    [3,2,2,2,2,12,2,2,2,2,2,2,2,2,9],
    [3,2,2,2,2,2,2,2,2,2,2,2,2,2,9],
    [3,2,2,16,2,2,2,2,2,2,2,2,2,2,9],
    [3,2,2,2,2,2,2,2,2,12,2,2,2,2,9],
    [3,2,2,2,2,14,2,2,2,2,2,16,2,2,9],
    [3,2,2,2,2,2,2,2,2,2,2,2,2,2,9],
    [5,7,7,7,7,7,7,7,7,7,7,7,7,7,11],
]

cafe_textures = [
    [15,15,15,15,15,15,15,15,15,15,15,15,15,15,15],
    [15,13,13,13,13,13,13,13,13,13,13,13,13,13,15],
    [15,13,13,13,13,13,13,13,13,13,13,13,13,13,15],
    [15,13,13,13,13,13,13,13,13,13,13,13,13,13,15],
    [15,13,13,13,13,13,13,13,13,13,13,13,13,13,15],
    [15,13,13,13,13,13,13,13,13,13,13,13,13,13,15],
    [15,13,13,13,13,13,13,13,13,13,13,13,13,13,15],
    [15,13,13,13,13,13,13,13,13,13,13,13,13,13,15],
    [15,13,13,13,13,13,13,13,13,13,13,13,13,13,15],
    [15,13,13,13,13,13,13,13,13,13,13,13,13,13,15],
    [15,13,13,13,13,13,13,13,13,13,13,13,13,13,15],
    [15,13,13,13,13,13,13,13,13,13,13,13,13,13,15],
    [15,13,13,13,13,13,13,13,13,13,13,13,13,13,15],
    [15,13,13,13,13,13,13,13,13,13,13,13,13,13,15],
    [15,15,15,15,15,15,15,15,15,15,15,15,15,15,15]
]

# Функція для очищення списків колізій
def clear_collisions():
    bad.clear()
    good.clear()
    decoration.clear()

# Функція для перемикання на кафе
def switch_to_cafe():
    global textures
    clear_collisions()  # Очищаємо всі колізії
    textures = cafe_textures

# Функція для повернення на початкову мапу
def switch_to_initial():
    global textures
    clear_collisions()  # Очищаємо всі колізії
    textures = initial_textures

bad = []
good = []
decoration = []

textures = initial_textures

for y, row in enumerate(textures):
    for x, tile in enumerate(row):
        rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
        if tile in [3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 15]:
            bad.append(rect)
        elif tile == 8:
            good.append(rect)
        elif tile == 14:
            decoration.append(rect)

#-------------безкінечний цикл гри

# Функція для повернення на початкову локацію
def teleport_to_initial_position():
    global geroy
    geroy.x = 65  # Початкова позиція
    geroy.y = 65  # Початкова позиція


# Стан діалогу
dialog_active = False
current_dialog = 0
dialog_options = [
    {"text": "Привіт! Хто ти?", "responses": ["Я маг.", "Не твоє діло."]},
    {"text": "Що ти тут робиш?", "responses": ["Охороняю цей ліс.", "Чекаю на тебе."]},
    {"text": "До побачення!", "responses": ["Щасти!", "Прощавай."]},
]

# Функція для перевірки, чи герой біля мага
def check_if_near_mage():
    return geroy.colliderect(mage)


game = True
while game:
    display.fill((194, 178, 128))

    # Малюємо мапу
    for y, row in enumerate(textures):
        for x, tile in enumerate(row):
            texture = pygame.transform.scale(textures_images[tile], (TILE_SIZE, TILE_SIZE))
            display.blit(texture, (x * TILE_SIZE, y * TILE_SIZE))

    if textures == cafe_textures:
        display.blit(portal_texture, (portal_rect.x, portal_rect.y))

    if textures == cafe_textures:
        display.blit(wizard, (mage.x, mage.y))


    # Малюємо героя
    display.blit(hero, geroy)

    # Обробка подій
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                go_right = True
                hero = pygame.image.load(dir_path + "/all_textures/wicked_cat_right.png")
            if event.key == pygame.K_a:
                go_left = True
                hero = pygame.image.load(dir_path + "/all_textures/wicked_cat_left.png")
            if event.key == pygame.K_w:
                go_up = True
            if event.key == pygame.K_s:
                go_down = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                go_right = False
            if event.key == pygame.K_a:
                go_left = False
            if event.key == pygame.K_w:
                go_up = False
            if event.key == pygame.K_s:
                go_down = False

    # Рух героя
    if go_right:
        geroy.x += 2
        for ba in bad:
            if geroy.colliderect(ba):  # Якщо є зіткнення
                geroy.x -= 2  # Припинити рух в право
                break

    if go_left:
        geroy.x -= 2
        for ba in bad:
            if geroy.colliderect(ba):  # Якщо є зіткнення
                geroy.x += 2  # Припинити рух в ліво
                break

    if go_up:
        geroy.y -= 2
        for ba in bad:
            if geroy.colliderect(ba):  # Якщо є зіткнення
                geroy.y += 2  # Припинити рух вгору
                break

    if go_down:
        geroy.y += 2
        for ba in bad:
            if geroy.colliderect(ba):  # Якщо є зіткнення
                geroy.y -= 2  # Припинити рух вниз
                break

    # Перевірка на хороші місця
    # Перевірка на хороші місця (телепортер працює тільки на початковій мапі)
    if textures == initial_textures:
        for goo in good:
            if geroy.colliderect(goo):
                switch_to_cafe()  # Переходимо в кафе
                geroy.x, geroy.y = 100, 100  # Початкова позиція героя в кафе

    for dec in decoration:
        if geroy.colliderect(dec):
            pass
            
        # Перевірка телепорту назад
    if geroy.colliderect(portal_rect) and textures == cafe_textures:
        teleport_to_initial_position()  # Повертаємо героя на початкову позицію
        switch_to_initial()  # Повертаємо початкову мапу

    # Перевірка діалогу
    if event.type == pygame.KEYDOWN and not dialog_active:
        if hero.colliderect(wizard) and event.key == pygame.K_e:  # Натискаємо "E" біля мага
            dialog_active = True
            current_dialog = 0

    # Перевірка на маг
    if check_if_near_mage():
        # Якщо герой біля мага і натискає "E", активуємо діалог
        if event.type == pygame.KEYDOWN and event.key == pygame.K_e and not dialog_active:
            dialog_active = True
            current_dialog = 0

    # Вибір відповіді
    if event.type == pygame.MOUSEBUTTONDOWN and dialog_active:
        mouse_pos = pygame.mouse.get_pos()
        dialog_box = pygame.Rect(50, 400, 500, 150)
        for i, option in enumerate(dialog_options[current_dialog]["responses"]):
            button = pygame.Rect(dialog_box.x + 10, dialog_box.y + 50 + i * 40, 480, 30)
            if button.collidepoint(mouse_pos):
                print(f"Вибрано: {option}")
                current_dialog += 1
                if current_dialog >= len(dialog_options):
                    dialog_active = False

    # Відображення діалогового табло
    if dialog_active:
        dialog_data = dialog_options[current_dialog]
        dialog.draw_dialog_box(display, FONT, dialog_data["text"], dialog_data["responses"])

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            game = False

        # Початок діалогу
        if event.type == pygame.KEYDOWN and not dialog_active:
            if hero.colliderect(mage) and event.key == pygame.K_e:  # Натискаємо "E" біля мага
                dialog_active = True
                current_dialog = 0

        # Вибір відповіді
        if event.type == pygame.MOUSEBUTTONDOWN and dialog_active:
            mouse_pos = pygame.mouse.get_pos()
            dialog_box = pygame.Rect(50, 400, 500, 150)
            for i, option in enumerate(dialog_options[current_dialog]["responses"]):
                button = pygame.Rect(dialog_box.x + 10, dialog_box.y + 50 + i * 40, 480, 30)
                if button.collidepoint(mouse_pos):
                    print(f"Вибрано: {option}")
                    current_dialog += 1
                    if current_dialog >= len(dialog_options):
                        dialog_active = False
        # Відображення діалогового табло
    if dialog_active:
        dialog_data = dialog_options[current_dialog]
        dialog.draw_dialog_box(display, FONT, dialog_data["text"], dialog_data["responses"])

    # Повернення на початкову локацію
    if geroy.colliderect(portal_rect) and textures == cafe_textures:
        teleport_to_initial_position()  # Повертаємо героя на початкову позицію
        switch_to_initial()  # Повертаємо початкову мапу

    pygame.display.flip()
    clock.tick(60)
pygame.quit()