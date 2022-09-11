import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

pygame.init()
screen = pygame.display.set_mode((300, 300))

degree = 0
done = False
clock = pygame.time.Clock()

while not done:
    clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(WHITE)

    surf = pygame.Surface((100, 100))
    surf.fill(WHITE)
    surf.set_colorkey((255, 0, 0))

    bigger = pygame.Rect(0, 0, 100, 100)

    pygame.draw.rect(surf, BLACK, bigger, 4)

    w, h = surf.get_size()  # Размеры изображения


    # Поворот векторов точек ограничительной рамки изображения на заданный угол
    box = [pygame.math.Vector2(p) for p in [(0, 0), (w, 0), (w, -h), (0, -h)]]
    box_rotate = [p.rotate(degree) for p in box]
    # Ищем минимальную и максимальную повернутые точки
    min_box = (min([p[0] for p in box_rotate]), min([p[1] for p in box_rotate]))
    max_box = (max([p[0] for p in box_rotate]), max([p[1] for p in box_rotate]))
    # Ищем положение левой верхней точки изображения относительно центра
    place = (300 / 2 + min_box[0], 300 / 2 - max_box[1])
    # Поворачиваем исходное изображение на заданный угол
    rotated_image = pygame.transform.rotate(surf, degree + 5)
    # Рисуем новое изображение
    screen.blit(rotated_image, place)
    degree += 20

    pygame.display.flip()

pygame.quit()