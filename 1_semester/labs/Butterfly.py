# Завойских Евгения, ИУ7-13Б
# Проверка, находится ли заданная точка внутри графика бабочки

eps = 1e-10  # Погрешность вычислений
s = 1  # Условие работы цикла

while s != 0:  # Проверка, продолжать ли работу
    x, y = map(float, input('Введите координаты x, y одной точки: ').split())  # Ввод координат точки
    x = abs(x)  # Получание модуля координаты x
    f = False  # Пока не известно, лежит ли точка внутри графика

    if 1 <= x <= 9:  # Проверка на верхние крылья
        f = (y <= ((-1 / 8) * (x - 9) ** 2 + 8))  # Верхние грани крыла
        if 8 <= x <= 9:
            f = f and (y >= (7 * (x - 8) ** 2 + 1))  # Крайние нижние части крыльев
        elif 1 <= x <= 8:
            f = f and (y >= ((1 / 49) * (x - 1) ** 2))  # Основные нижние части крыльев

    if 1 <= x <= 8 and not f:  # Точка не в верхних крыльях, проверка на нижние крылья
        f = (y <= ((-4 / 49) * (x - 1) ** 2))  # Верхние грани крыльев
        if 2 <= x <= 8:
            f = f and (y >= ((1 / 3) * (x - 5) ** 2 - 7))  # Большие нижние части крыльев
        elif 1 <= x <= 2:
            f = f and (y >= (-2 * (x - 1) ** 2 - 2))  # Меньшие нижние части крыльев

    if x <= 1 and not f:  # Точка не в крыльях, проверка на туловище
        f = (y <= (-4 * x * x + 2))  # Верхняя грань туловища
        f = f and (y >= (4 * x * x - 6))  # Нижняя грань туловища

    if x <= 2 and not f:  # Точка не в крыльях или туловище, проверка на усики
        f = abs(y - (1.5 * x + 2)) < eps  # Точка может лежать на усиках с некоторой погрешностью

    if f:  # Точка лежит внутри графика
        print('Точка находится внутри графика')
    else:  # Точка лежит вне графика
        print('Точка находится вне графика')

    s = int(input('Введите 0, если хотите закончить работу, иначе 1: '))  # Запрос на продолжение работы