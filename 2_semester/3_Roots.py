# Завойских Евгения, ИУ7-23Б
# Используя метод Брента, найти корни на заданном отрезке, вывести таблицу и график

from tkinter import *
from tkinter import messagebox as mb
import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt
from math import sin, cos


# Функция, вычисляющая значение функции
def f(x):
    return sin(x) + 0.5

# Функция, вычисляющая значение производной
def first_der_f(x):
    return cos(x)

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

# Функция, проверяющая корректность ввода
def check_input(start, end, step, ep):
    if end < start:  # Конец отрезка меньше начала
        return False

    if (end - start) < step:  # Длина отрезка меньше шага
        return False

    if (ep > 1) or (ep < 0):  # Точность меньше 0 или больше 1
        return False

    return True  # Всё нормально

# Функция, возвращающая список корней для разбиения отрезка с шагом h
def get_roots(func, start, end, step, ep):
    roots = []  # Корни
    i = start  # Начало отрезка

    # Проходим все отрезки с заданным шагом
    while (i < end):
        miniend = i + step  # Конец отрезка
        if miniend > end:  # Вышли за конец
            miniend = end

        if (func(i) * func(miniend) > 0):  # Корня на отрезке нет
            roots.append(None)
        else:
            # Вычисление корня функции на отрезке с заданной точностью
            root, res = optimize.brentq(func, i, miniend, xtol=ep, maxiter=100, full_output=True)
            roots.append(res)
        i += step  # Переход к следующему отрезку

    return roots

# Функция, выводящая таблицу корней
def display_table(rs, start, end, step):
    # Названия столбцов таблицы
    cols = ["Номер корня", "[xi; x(i+1)]", "Корень", "Значение функции в точке корня",
            "Количество итераций", "Код ошибки"]

    # Вывод названий столбцов
    j = 0
    for i in cols:
        label = Label(text=i, font='1')
        label.grid(row=3, column=j, columnspan=2)
        j += 2

    i = start  # Начало отрезка
    num = 0  # Индекс элемента списка корней
    r = 4  # Номер строки
    cnt = 1  # Количество корней

    # Проходим все отрезки с заданным шагом
    while (i < end):
        miniend = i + step  # Конец отрезка
        if miniend > end:  # Вышли за конец
            miniend = end

        # Список значений в строке
        vals = [str(cnt), '[' + '{:.3n}'.format(i) + '; ' + '{:.3n}'.format(miniend) + ']']

        if (rs[num] == None):  # Корня на отрезке нет
            vals[0] = '---'
            vals.append('---')
            vals.append('---')
            vals.append('---')
            vals.append('2')
        else:
            cnt += 1
            # Добавление корня функции, значения фукнции в точке корня, количества итераций
            vals.append(('{:.6n}'.format(rs[num].root)))
            vals.append(('{:.4e}'.format(f(rs[num].root))))
            vals.append(str(rs[num].iterations))

            if rs[num].iterations > 100:  # Превышено количество итераций
                vals.append('1')
            else:  # Всё нормально
                vals.append('0')

        j = 0
        # Вывод строки таблицы
        for x in vals:
            label = Label(text=x, font='1')
            label.grid(row=r, column=j, columnspan=2)
            labels.append(label)
            j += 2

        i += step  # Переход к следующему отрезку
        r += 1  # Переход к следующей строке
        num += 1  # Переход к следующему элементу списка корней

# Функция, выводящая график функции
def display_graph(start, stop, step, roots, extrs):
    # Значения x и y точек графика на отрезке с заданным шагом, корней и экстремумов
    x = np.sort(np.concatenate([np.arange(start, stop + step, step), np.array(roots + extrs)]))
    y = [f(i) for i in x]

    # Значения x и y точек корней и экстремумов
    x2 = roots + extrs
    y2 = [f(i) for i in x2]

    # Вывод графика с выделенными точками корней и экстремумов
    plt.title("y = x ^ 2 - 1")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid()
    plt.plot(x, y, color='b')
    plt.scatter(x2, y2, color='orange', s=40, marker='o')
    plt.show()

# Функция, выводящая таблицу с корнями и график
def display_table_graph():
    # Проверки на ввод данных
    if (not is_number(a.get())) or (not is_number(b.get())) or (not is_number(h.get())) or (not is_number(eps.get())):
        mb.showerror("Ошибка", "Должны быть введены числа")
    elif not check_input(float(a.get()), float(b.get()), float(h.get()), float(eps.get())):
        mb.showerror("Ошибка", "начало < конца, шаг < длины отрезка, точность от 0 до 1")
    else:  # Всё введено корректно
        a2 = float(a.get())
        b2 = float(b.get())
        h2 = float(h.get())
        eps2 = float(eps.get())

        # Удаление строк прежней таблицы
        for l in labels:
            l.destroy()
        labels.clear()

        f_roots = get_roots(f, a2, b2, h2, eps2)  # Корни функции
        display_table(f_roots, a2, b2, h2)  # Вывод таблицы корней

        # Выделяем отдельно значения корней функции
        rs1 = []
        for x in f_roots:
            if x != None:
                rs1.append(x.root)

        first_der_roots = get_roots(first_der_f, a2, b2, h2, eps2)  # Точки экстремума
        # Выделяем отдельно значения точек экстремума
        rs2 = []
        for x in first_der_roots:
            if x != None:
                rs2.append(x.root)

        display_graph(a2, b2, h2, rs1, rs2)  # Вывод графика функции


# Создание окна с указанными размерами и заголовком
window = Tk()
window.geometry('1200x250')
window.title('Вычисление корней функции')

a = StringVar()  # Строка с началом отрезка
b = StringVar()  # Строка с концом отрезка
h = StringVar()  # Строка с шагом
eps = StringVar()  # Строка с точностью

labels = []  # Список строк таблицы корней

# Создание поясняющего текста для ввода
alabel = Label(text='Начало отрезка', font='1')
alabel.grid(row=0, column=0, columnspan=2)
# Создание поля для ввода начала отрезка
aentry = Entry(textvariable=a, font='1')
aentry.grid(row=0, column=2, columnspan=2)

# Создание поясняющего текста для ввода
blabel = Label(text='Конец отрезка', font='1')
blabel.grid(row=0, column=4, columnspan=2)
# Создание поля для ввода конца отрезка
bentry = Entry(textvariable=b, font='1')
bentry.grid(row=0, column=6, columnspan=2)

# Создание поясняющего текста для ввода
hlabel = Label(text='Шаг', font='1')
hlabel.grid(row=1, column=0, columnspan=2)
# Создание поля для ввода шага
hentry = Entry(textvariable=h, font='1')
hentry.grid(row=1, column=2, columnspan=2)

# Создание поясняющего текста для ввода
epslabel = Label(text='Точность', font='1')
epslabel.grid(row=1, column=4, columnspan=2)
# Создание поля для ввода точности
epsentry = Entry(textvariable=eps, font='1')
epsentry.grid(row=1, column=6, columnspan=2)

# Создание кнопки для вывода таблицы корней
button = Button(text='Корни', font='1', command=display_table_graph)
button.grid(row=2, column=0, columnspan=3)

# Создание меню по кодам ошибок
mainmenu = Menu(window)
window.config(menu=mainmenu)

errmenu = Menu(mainmenu, tearoff=0)
errmenu.add_command(label='0 - нет ошибок')
errmenu.add_command(label='1 - превышено количество итераций при вычислении корня')
errmenu.add_command(label='2 - нет корня')

mainmenu.add_cascade(label='Коды ошибок', menu=errmenu)

window.mainloop()





