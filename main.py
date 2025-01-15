import pygame
import os
import time

pygame.init()

clock = pygame.time.Clock()

display = pygame.display.set_mode((600, 600))

geroy = pygame.Rect(65, 65, 29, 22)

go_right = go_left = go_up = go_down = False

dir_path = os.path.dirname(__file__)

TILE_SIZE = 40  # Розмір текстур: 40x40

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
    14: pygame.image.load(dir_path + "/all_textures/flover.png"),
    15: pygame.image.load(dir_path + "/all_textures/stone.png")
}


hero = pygame.image.load(dir_path + "/all_textures/wicked_cat_right.png")

#-------------ігрове поле нашої гри

initial_textures = [
    [4,6,6,6,6,6,6,6,6,6,6,6,6,6,10],
    [3,2,2,2,2,2,2,2,2,2,2,2,2,2,9],
    [3,2,2,2,2,2,2,2,2,14,2,2,2,2,9],
    [3,2,2,2,2,2,2,2,2,2,2,2,12,2,9],
    [3,2,2,2,2,2,2,2,2,2,2,2,2,2,9],
    [3,2,2,12,2,2,2,2,2,2,2,2,2,2,9],
    [3,2,2,2,2,2,2,2,2,2,2,8,2,2,9],
    [3,2,2,2,2,2,2,2,2,2,2,2,2,2,9],
    [3,2,2,2,2,12,2,2,2,2,2,2,2,2,9],
    [3,2,2,2,2,2,2,2,2,2,2,2,2,2,9],
    [3,2,2,2,2,2,2,2,2,2,2,2,2,2,9],
    [3,2,2,2,2,2,2,2,2,12,2,2,2,2,9],
    [3,2,2,2,2,14,2,2,2,2,2,2,2,2,9],
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
    [15,15,15,15,15,15,15,15,15,15,15,15,15,15,15],
    ]

# Змінна для збереження мапи
textures = initial_textures  # Початкова мапа

# Позиція телепорту
teleport_back = pygame.Rect(400, 300, TILE_SIZE, TILE_SIZE)

# Блок телепорту назад в кафе
teleport_back = pygame.image.load(dir_path + "/all_textures/portal.png")

# Функція для зміни мапи на кафе
def switch_to_cafe():
    global textures
    textures = cafe_textures

# Функція для повернення на початкову мапу
def switch_to_initial():
    global textures
    textures = initial_textures

# Функція для телепортування в кафе
def teleport_to_cafe():
    global geroy
    geroy.x = 65  # Початкова позиція
    geroy.y = 65  # Початкова позиція

bad = []
good = []

# Генеруємо квадрати
for y, row in enumerate(textures):
    for x, tile in enumerate(row):
        rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
        if tile in [3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15]:
            bad.append(rect)
        elif tile == 8:
            good.append(rect)


#-------------безкінечний цикл гри

# Функція для повернення на початкову локацію
def teleport_to_initial_position():
    global geroy
    geroy.x = 65  # Початкова позиція
    geroy.y = 65  # Початкова позиція

# Завантажуємо зображення для телепорту назад
teleport_back_image = pygame.image.load(dir_path + "/all_textures/portal.png")
teleport_back_rect = pygame.Rect(400, 300, TILE_SIZE, TILE_SIZE)  # Координати блоку телепорту


game = True
while game:
    display.fill((194, 178, 128))

    # Малюємо мапу
    for y, row in enumerate(textures):
        for x, tile in enumerate(row):
            texture = pygame.transform.scale(textures_images[tile], (TILE_SIZE, TILE_SIZE))
            display.blit(texture, (x * TILE_SIZE, y * TILE_SIZE))

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
        geroy.x += 5
        for ba in bad:
            if geroy.colliderect(ba):  # Якщо є зіткнення
                geroy.x -= 5  # Припинити рух в право
                break

    if go_left:
        geroy.x -= 5
        for ba in bad:
            if geroy.colliderect(ba):  # Якщо є зіткнення
                geroy.x += 5  # Припинити рух в ліво
                break

    if go_up:
        geroy.y -= 5
        for ba in bad:
            if geroy.colliderect(ba):  # Якщо є зіткнення
                geroy.y += 5  # Припинити рух вгору
                break

    if go_down:
        geroy.y += 5
        for ba in bad:
            if geroy.colliderect(ba):  # Якщо є зіткнення
                geroy.y -= 5  # Припинити рух вниз
                break

    # Перевірка на хороші місця
    for goo in good:
        if geroy.colliderect(goo):
            switch_to_cafe()  # Переходимо на новий рівень
            
        # Перевірка телепорту назад
    if geroy.colliderect(teleport_back_rect) and textures == cafe_textures:
        teleport_to_initial_position()  # Повертаємо героя на початкову позицію
        switch_to_initial()  # Повертаємо початкову мапу

        def switch_to_cafe():
            # Очищаємо екран від попереднього рівня
            global textures
            global geroy
            textures = cafe_textures  # Змінюємо текстури на кафе

            # Встановлюємо нового героя в точку на кафе (можна змінити координати)
            geroy.x = 200
            geroy.y = 200

        # Якщо ми в кафе, перевіряємо блок телепорту
        if textures == cafe_textures:  # Якщо ми в кафе
            pygame.image.load(dir_path + "/all_textures/portal.png")

        # Перевірка на попадання в кафе
        for goo in good:
            if geroy.colliderect(goo):
                switch_to_cafe()  # Якщо доторкнулись до кафе, змінюємо мапу на кафе

    pygame.display.flip()
    clock.tick(60)