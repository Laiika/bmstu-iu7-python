# Завойских Евгения, ИУ7-23Б
# Реализовать метод шейкер-сортировки, составить таблицу замеров времени сортировки для различных списков

from tkinter import *
from tkinter import messagebox as mb
import time
import random

# Функция, сортирующая список
def shakersort(a):
    l = 0  # Левая граница неотсортированной части списка
    r = len(a) - 1  # Правая граница неотсортированной части списка
    while l < r:
        r2 = l  # Новая правая граница
        for i in range(l, r):
            # Два элемента расположены неправильно
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                r2 = i
        r = r2

        l2 = r  # Новая левая граница
        for i in range(r - 1, l - 1, -1):
            # Два элемента расположены неправильно
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                l2 = i
        l = l2
    return a

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

# Функция, выводящая отсортированный введенный список
def display_answer1():
    nums = list(map(str, testnums.get().split()))  # Введенный список
    for num in nums:
        if not is_number(num):  # Проверка, что введено число
            mb.showerror("Ошибка", "Должен быть введен список чисел")
            return

    nums = list(map(float, nums))
    nums = shakersort(nums)
    reslabel.configure(text=' '.join(list(map(str, nums))))  # Вывод ответа

# Функция, возвращающая время сортировки упорядоченного списка
def ordered_sort_time(n):
    a = []  # Список
    for i in range(n):
        a.append(i)

    start = time.time()  # Начало замера
    shakersort(a)
    return time.time() - start

# Функция, возвращающая время сортировки случайного списка
def random_sort_time(n):
    a = []  # Список
    for i in range(n):
        a.append(random.randint(0, 100))

    start = time.time()  # Начало замера
    shakersort(a)
    return time.time() - start

# Функция, возвращающая время сортировки обратно упорядоченного списка
def reverse_sort_time(n):
    a = []  # Список
    for i in range(n - 1, -1, -1):
        a.append(i)

    start = time.time()  # Начало замера
    shakersort(a)
    return time.time() - start

# Функция, выводящая результаты замеров времени сортировки для списков
def display_answer2():
    nums = [n1.get(), n2.get(), n3.get()]  # Введенные размеры списков
    for num in nums:
        if not num.isdigit():  # Проверка, что введено неотрицательное число
            mb.showerror("Ошибка", "Должно быть введено 3 положительных числа")
            return

    # Вывод замеров времени сортировки для упорядоченных списков
    orderlabel1.configure(text=ordered_sort_time(int(nums[0])))
    orderlabel2.configure(text=ordered_sort_time(int(nums[1])))
    orderlabel3.configure(text=ordered_sort_time(int(nums[2])))

    # Вывод замеров времени сортировки для случайных списков
    randomlabel1.configure(text=random_sort_time(int(nums[0])))
    randomlabel2.configure(text=random_sort_time(int(nums[1])))
    randomlabel3.configure(text=random_sort_time(int(nums[2])))

    # Вывод замеров времени сортировки для обратно упорядоченных списков
    reverselabel1.configure(text=reverse_sort_time(int(nums[0])))
    reverselabel2.configure(text=reverse_sort_time(int(nums[0])))
    reverselabel3.configure(text=reverse_sort_time(int(nums[0])))


# Создание окна с указанными размерами и заголовком
window = Tk()
window.geometry('1100x250')
window.title('Перевод чисел')


testnums = StringVar()  # Строка с тестовой последовательностью

# Создание поясняющего текста для ввода
testlabel = Label(text='Тестовая сортировка', font='1')
testlabel.grid(row=0, column=0, columnspan=3)

# Создание поля для ввода чисел
testentry = Entry(textvariable=testnums, font='1')
testentry.grid(row=0, column=3, columnspan=2)

# Создание кнопки для сортировки чисел
testbutton = Button(text='Отсортировать', font='1', command=display_answer1)
testbutton.grid(row=0, column=5, columnspan=2)

# Создание надписи с ответом
reslabel = Label(text='-----', font='1')
reslabel.grid(row=0, column=7, columnspan=3)


n1 = StringVar()  # Строка с вводимым первым размером
n2 = StringVar()  # Строка с вводимым вторым размером
n3 = StringVar()  # Строка с вводимым третьим размером

# Создание поясняющего текста для ввода
tablelabel = Label(text='Размерности массивов ', font='1')
tablelabel.grid(row=1, column=0, columnspan=3)

# Создание поля для ввода первого числа
entry1 = Entry(textvariable=n1, font='1')
entry1.grid(row=1, column=3, columnspan=2)

# Создание поля для ввода второго числа
entry2 = Entry(textvariable=n2, font='1')
entry2.grid(row=1, column=5, columnspan=2)

# Создание поля для ввода третьего числа
entry3 = Entry(textvariable=n3, font='1')
entry3.grid(row=1, column=7, columnspan=2)

# Создание поясняющего текста для вывода
orderlabel = Label(text='Упорядоченный массив ', font='1')
orderlabel.grid(row=2, column=0, columnspan=3)

# Создание текста вывода для первого списка
orderlabel1 = Label(text='----', font='1')
orderlabel1.grid(row=2, column=3, columnspan=2)

# Создание текста вывода для второго списка
orderlabel2 = Label(text='----', font='1')
orderlabel2.grid(row=2, column=5, columnspan=2)

# Создание текста вывода для третьего списка
orderlabel3 = Label(text='----', font='1')
orderlabel3.grid(row=2, column=7, columnspan=2)

# Создание поясняющего текста для вывода
randomlabel = Label(text='Случайный массив ', font='1')
randomlabel.grid(row=3, column=0, columnspan=3)

# Создание текста вывода для первого списка
randomlabel1 = Label(text='----', font='1')
randomlabel1.grid(row=3, column=3, columnspan=2)

# Создание текста вывода для второго списка
randomlabel2 = Label(text='----', font='1')
randomlabel2.grid(row=3, column=5, columnspan=2)

# Создание текста вывода для третьего списка
randomlabel3 = Label(text='----', font='1')
randomlabel3.grid(row=3, column=7, columnspan=2)

# Создание поясняющего текста для вывода
reverselabel = Label(text='Обратно упорядоченный массив ', font='1')
reverselabel.grid(row=4, column=0, columnspan=3)

# Создание текста вывода для первого списка
reverselabel1 = Label(text='----', font='1')
reverselabel1.grid(row=4, column=3, columnspan=2)

# Создание текста вывода для второго списка
reverselabel2 = Label(text='----', font='1')
reverselabel2.grid(row=4, column=5, columnspan=2)

# Создание текста вывода для третьего списка
reverselabel3 = Label(text='----', font='1')
reverselabel3.grid(row=4, column=7, columnspan=2)

# Создание кнопки для сортировка списков заданных размеров
tablebutton = Button(text='Отсортировать', font='1', command=display_answer2)
tablebutton.grid(row=5, column=0, columnspan=3)

window.mainloop()

