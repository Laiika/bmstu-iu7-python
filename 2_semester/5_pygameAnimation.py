# Завойских Евгения, ИУ7-23Б
# Реальзация двух одновременных движений: поступательного и вращательного

import pygame

WIDTH = 500  # Ширина игрового окна
HEIGHT = 500  # Высота игрового окна
FPS = 30  # Частота кадров в секунду
FIGURE_W = 70  # Ширина изображения
FIGURE_H = 70  # Высота изображения

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Функция, осуществляющая поступательное движение
def translational(image, rect):
    rect.x += 5
    # Если дошли до левого края, переходим в правый
    if rect.left > WIDTH:
        rect.right = 0
    # Рисуем перемещенное изображение
    screen.blit(image, rect)

# Функция, осуществляющая вращение вокруг центра
def rotational(image, angle):
    w, h = image.get_size()  # Размеры изображения
    # Поворот векторов точек ограничительной рамки изображения на заданный угол
    box = [pygame.math.Vector2(p) for p in [(0, 0), (w, 0), (w, -h), (0, -h)]]
    box_rotate = [p.rotate(angle) for p in box]
    # Ищем минимальную и максимальную повернутые точки
    min_box = (min([p[0] for p in box_rotate]), min([p[1] for p in box_rotate]))
    max_box = (max([p[0] for p in box_rotate]), max([p[1] for p in box_rotate]))
    # Ищем положение левой верхней точки изображения относительно центра
    place = (WIDTH / 2 + min_box[0], HEIGHT / 2 - max_box[1])
    # Поворачиваем исходное изображение на заданный угол
    rotated_image = pygame.transform.rotate(image, angle)
    # Рисуем новое изображение
    screen.blit(rotated_image, place)


# Создаем игру и окно
pygame.init()  # Запуск pygame
pygame.mixer.init()  # Для звука
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Окно программы
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

# Задаем первое изображение
first = pygame.image.load('astr.jpg')
first.set_colorkey(WHITE)  # Делаем прозрачный фон
first = pygame.transform.scale(first, (FIGURE_W, FIGURE_H))  # Меняем размеры
# Определяем его местоположение
rect1 = first.get_rect()
rect1.center = (WIDTH / 2, HEIGHT / 4)

# Задаем второе изображение
second = pygame.image.load('raketa.jpg')
second.set_colorkey(WHITE)  # Делаем прозрачный фон
second = pygame.transform.scale(second, (FIGURE_W, FIGURE_H))  # Меняем размеры
# Определяем его местоположение
rect2 = second.get_rect()
rect2.center = (WIDTH / 2, HEIGHT / 2)
# Определяем его угол поворота
angle = 0

# Цикл игры
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)

    # Ввод процесса (события)
    for event in pygame.event.get():
        # Проверка закрытия окна
        if event.type == pygame.QUIT:
            running = False

    # Прорисовка
    screen.fill(BLACK)
    # Поступательное движение первого изображения
    translational(first, rect1)
    # Вращательное движение второго изображения
    rotational(second, angle)
    angle += 5

    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()