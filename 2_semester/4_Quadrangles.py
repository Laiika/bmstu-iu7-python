# Завойских Евгения, ИУ7-23Б
# На плоскости задано множество точек.
# Определить количество выпуклых четырехугольников, которые можно построить на этих точках.
# Дать графическое изображение результатов.

from tkinter import *
from tkinter import messagebox as mb
from math import sqrt


# Функция, проверяющая, что строка содержит число
def is_number(st):
    if st.isdigit() or (st[0] == '-' and st[1:].isdigit()):  # Строка содержит целое число
        return True
    else:
        try:
            float(st)  # Строка содержит вещественное число
            return True
        except ValueError:
            return False  # Не число

# Функция, добавляющая точку в списки и выводящая её координаты
def add_point():
    # Проверки на ввод данных
    if (not is_number(x.get()) or not is_number(y.get())):
        mb.showerror("Ошибка", "Должны быть введены числа")
    else:  # Всё введено корректно
        x2 = float(x.get())
        y2 = float(y.get())

        if [x2, y2] in points:  # Такая точка уже есть в списке
            mb.showerror("Ошибка", "Такая точка уже есть")
        else:
            points.append([x2, y2])
            # Вывод координат точки
            label = Label(text=('(' + str(x2) + ', ' + str(y2) + ')'), font='1')
            label.grid(row=len(points) + 2, column=0, columnspan=2)

            labels.append(label)

# Функция, проверяющая, образуют ли треугольник переданные точки
def is_triangle(a, b, c):
    ab = sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)  # Вычисление длины стороны AB
    ac = sqrt((a[0] - c[0]) ** 2 + (a[1] - c[1]) ** 2)  # Вычисление длины стороны AC
    bc = sqrt((b[0] - c[0]) ** 2 + (b[1] - c[1]) ** 2)  # Вычисление длины стороны BC
    eps = 1e-10  # Погрешность вычислений

    if (abs(ab - ac - bc) < eps) or (abs(ac - ab - bc) < eps) or (abs(bc - ac - ab) < eps):  # Все три точки лежат на одной прямой
        return False
    else:
        return True

# Функция, проверяющая, находится ли точка внутри треугольника
def in_triangle(p, a, b, c):
    pr1 = (a[0] - p[0]) * (b[1] - a[1]) - (b[0] - a[0]) * (a[1] - p[1])  # Вычисление векторного произведения AB и PA
    pr2 = (b[0] - p[0]) * (c[1] - b[1]) - (c[0] - b[0]) * (b[1] - p[1])  # Вычисление векторного произведения BC и PB
    pr3 = (c[0] - p[0]) * (a[1] - c[1]) - (a[0] - c[0]) * (c[1] - p[1])  # Вычисление векторного произведения CA и PA
    eps = 1e-10  # Погрешность вычислений

    if (pr1 < 0 and pr2 < 0 and pr3 < 0) or (pr1 > 0 and pr2 > 0 and pr3 > 0):  # Точка находится внутри треугольника
        return True
    elif abs(pr1) < eps or abs(pr2) < eps or abs(pr3) < eps:  # Точка лежит на одной из сторон
        return True

    return False

# Функция, проверяющая, образуют ли точки выпуклый четырехугольник
def is_convex(p1, p2, p3, p4):
    # Три точки на одной прямой или четырехугольник не выпуклый
    if not(is_triangle(p1, p2, p3) and not in_triangle(p4, p1, p2, p3)):
        return False

    # Три точки на одной прямой или четырехугольник не выпуклый
    if not(is_triangle(p1, p2, p4) and not in_triangle(p3, p1, p2, p4)):
        return False

    # Три точки на одной прямой или четырехугольник не выпуклый
    if not(is_triangle(p1, p3, p4) and not in_triangle(p2, p1, p3, p4)):
        return False

    # Три точки на одной прямой или четырехугольник не выпуклый
    if not(is_triangle(p2, p3, p4) and not in_triangle(p1, p2, p3, p4)):
        return False

    return True

# Функция, проверяющая, что отрезки p1p2 и p3p4 пересекаются
def is_cross(p1, p2, p3, p4):
    v1 = (p4[0] - p3[0]) * (p1[1] - p3[1]) - (p4[1] - p3[1]) * (p1[0] - p3[0])
    v2 = (p4[0] - p3[0]) * (p2[1] - p3[1]) - (p4[1] - p3[1]) * (p2[0] - p3[0])
    v3 = (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])
    v4 = (p2[0] - p1[0]) * (p4[1] - p1[1]) - (p2[1] - p1[1]) * (p4[0] - p1[0])

    if v1 * v2 < 0 and v3 * v4 < 0:  # Отрезки пересекаются
        return True

    return False

# Функция, выводящая выпуклый четырехугольник
def display_figure(p1, p2, p3, p4):
    if is_cross(p1, p2, p3, p4):  # p1p2 и p3p4 - диагонали
        x = [p1[0], p3[0], p2[0], p4[0]]
        y = [p1[1], p3[1], p2[1], p4[1]]
    elif is_cross(p2, p3, p1, p4):  # p2p3 и p1p4 - диагонали
        x = [p1[0], p2[0], p4[0], p3[0]]
        y = [p1[1], p2[1], p4[1], p3[1]]
    else:
        x = [p1[0], p2[0], p3[0], p4[0]]
        y = [p1[1], p2[1], p3[1], p4[1]]

    # Создание окна для вывода четырехугольника
    newwindow = Toplevel()
    newwindow.geometry('600x600')
    canvas = Canvas(newwindow, width=600, height=600)
    # Перемещение точки (0, 0)
    canvas.xview_scroll(600, "units")
    canvas.yview_scroll(600, "units")
    canvas.pack()

    # Масштабирование координат по оси x
    xmax = max([abs(i) for i in x])
    for i in range(len(x)):
        x[i] = x[i] * 150 / xmax

    # Масштабирование координат по оси y
    ymax = max([abs(i) for i in y])
    for i in range(len(y)):
        y[i] = -y[i] * 150 / ymax

    # Вывод четырехугольника
    canvas.create_polygon(x[0], y[0], x[1], y[1], x[2], y[2], x[3], y[3])

# Функция, вычисляющая количество выпуклых четырехугольников и выводящая их
def calc_quads():
    count = 0  # Количество выпуклых четырехугольников

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            for k in range(j + 1, len(points)):
                for l in range(k + 1, len(points)):
                    # Точки образуют выпуклый четырехугольник
                    if is_convex(points[i], points[j], points[k], points[l]):
                        count += 1
                        # Вывод фигуры
                        display_figure(points[i], points[j], points[k], points[l])

    countlabel.configure(text=str(count))  # Вывод количества

# Функция, удаляющая все точки и все с ними связанное
def delete_points():
    # Удаление строк
    for l in labels:
        l.destroy()
    labels.clear()

    points.clear()  # Удаление точек

    countlabel.configure(text='-----')  # Удаление количества четырехугольников

# Создание окна с указанными размерами и заголовком
window = Tk()
window.geometry('1200x700')
window.title('Нахождение выпуклых четырехугольников')

x = StringVar()  # Строка с координатой точки по оси x
y = StringVar()  # Строка с координатой точки по оси y

points = []  # Список точек
labels = []  # Список строк с координатами точек

# Создание поясняющего текста для ввода
xlabel = Label(text='Координата точки x', font='1')
xlabel.grid(row=0, column=0, columnspan=2)
# Создание поля для ввода координаты
xentry = Entry(textvariable=x, font='1')
xentry.grid(row=0, column=2, columnspan=2)

# Создание поясняющего текста для ввода
ylabel = Label(text='Координата точки y', font='1')
ylabel.grid(row=0, column=4, columnspan=2)
# Создание поля для ввода координаты
yentry = Entry(textvariable=y, font='1')
yentry.grid(row=0, column=6, columnspan=2)

# Создание кнопки для добавления точки в список
button1 = Button(text='Добавить точку', font='1', command=add_point)
button1.grid(row=0, column=8, columnspan=2)

# Создание кнопки для подсчета количества выпуклых четырехугольников
button2 = Button(text='Подсчитать количество выпуклых четырехугольников', font='1', command=calc_quads)
button2.grid(row=1, column=0, columnspan=4)

# Создание кнопки для удаления всех точек
button3 = Button(text='Начать заново', font='1', command=delete_points)
button3.grid(row=1, column=4, columnspan=3)

# Вывод поясняющего текста о количестве выпуклых четырехугольников
aboutcountlabel = Label(text='Количество выпуклых четырехугольников', font='1')
aboutcountlabel.grid(row=2, column=0, columnspan=4)

# Вывод количества выпуклых четырехугольников
countlabel = Label(text='-----', font='1')
countlabel.grid(row=2, column=4, columnspan=2)

window.mainloop()
