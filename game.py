import pygame

# Инициализация Pygame
pygame.init()

# Определение размеров карты
map_width = 1000
map_height = 600

canvas = pygame.Surface((map_width, map_height))
# canvas.set

#
cam_1 = pygame.Surface((map_width - (map_width // 3), map_height))
cam_2 = pygame.Surface((map_width - cam_1.get_width(), map_height))

cam_1.fill((0, 255, 0))

cam_2.fill((0, 0, 0))
# Создание окна для отрисовки
window = pygame.display.set_mode((map_width, map_height))

bg_img = pygame.image.load('img/map1.PNG')
bg_img = pygame.transform.scale(bg_img, (cam_1.get_width(), cam_1.get_height()))
bg_img_copy = bg_img.copy()

pygame.display.set_caption("Управление БПЛА")
font = pygame.font.SysFont("Arial", 24)




def show_info(x, y):
    text = font.render(f"Положение БПЛА: ({x}, {y})", True, (255, 0, 0))
    window.blit(text, (cam_1.get_width() + 20, 20), )


# Загрузка изображения БПЛА
UAV_image = pygame.image.load('img/uav.png')

# Получение размеров самолета
UAV_width = UAV_image.get_width()
UAV_height = UAV_image.get_height()

# Изначальное положение самолета на карте
airplane_x = int((map_width - UAV_width) / 2)
airplane_y = int((map_height - UAV_height) / 2)

s = pygame.Surface((UAV_width, UAV_height))
s.set_alpha(70)
s.fill((102, 255, 51))
bg_img.blit(s, (airplane_x - UAV_width // 2, airplane_y - UAV_height // 2))

piece_rect = pygame.Rect(0, 0, 200, 200)
piece_image = pygame.Surface(piece_rect.size)


def show_cam(x, y):
    piece_rect.x = x
    piece_rect.y = y
    cam_2.blit(bg_img_copy, (cam_2.get_width() // 1 / 4, 100), piece_rect)


def show_track(x, y):
    pygame.draw.circle(bg_img, (255, 0, 0), (x, y), 3)


# Функция для отрисовки самолета на карте
def draw_airplane(x, y):
    window.blit(UAV_image, (x - UAV_image.get_width() // 2, y - UAV_image.get_height() // 2), )


# Основной цикл программы
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Получение текущего состояния клавиш
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and airplane_x > 0:
        airplane_x -= 5
    if keys[pygame.K_RIGHT] and airplane_x < cam_1.get_width() - UAV_width:
        airplane_x += 5
    if keys[pygame.K_UP] and airplane_y > 0:
        airplane_y -= 5
    if keys[pygame.K_DOWN] and airplane_y < cam_1.get_height() - UAV_height:
        airplane_y += 5

    # Очистка экрана

    window.blit(canvas, (0, 0))
    # window.blit(cam_1, (0, 0))
    window.blit(cam_2, (cam_1.get_width(), 0))
    window.blit(bg_img, (0, 0))

    # Отрисовка самолета
    draw_airplane(airplane_x, airplane_y)
    show_cam(airplane_x, airplane_y)

    show_info(airplane_x, airplane_y)
    show_track(airplane_x, airplane_y)

    # Обновление окна
    pygame.display.update()

# Завершение работы Pygame
pygame.quit()
