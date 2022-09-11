# Завойских Евгения, ИУ7-23Б
# Написать программу, переводящую вещественное число из 10-й с.с. в 8-ю и обратно

from tkinter import *
from tkinter import Menu
from tkinter import messagebox


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

# Функция, проверяющая, что в строке нет цифр 8 и 9
def is_8th_sys(st):
    if st.find('8') != -1 or st.find('9') != -1:
        return False
    return True

# Функция, переводящая число из 10-й с.с. в 8-ю
def from_10th_to_8th(num):
    num = str(float(num))
    sign = ''  # Знак числа
    if num[0] == '-':
        sign = '-'
        num = num[1:]

    intpart, frpart = num.split('.')  # Целая и дробная части числа

    intpart = int(intpart)
    intres = []  # Целая часть результата
    # Перевод целой части
    if intpart == 0:
        intres.append('0')
    else:
        while intpart != 0:
            intres.append(str(intpart % 8))
            intpart = intpart // 8

    frpart = int(frpart) / (10 ** len(frpart))  # Дробная часть числа
    eps = 10e-5
    i = 1
    frres = 0  # Дробная часть результата
    # Перевод дробной части
    while frpart > eps and i < 5:
        frpart *= 8
        frres += int(frpart) / (10 ** i)
        frpart = frpart - int(frpart)
        i += 1

    res = int(''.join(intres[::-1])) + frres  # Результат перевода

    return sign + str(res)

# Функция, переводящая число из 8-й с.с. в 10-ю
def from_8th_to_10th(num):
    num = str(float(num))
    sign = ''  # Знак числа
    if num[0] == '-':
        sign = '-'
        num = num[1:]

    intpart, frpart = num.split('.')  # Целая и дробная части числа

    res = 0  # Результат перевода
    i = len(intpart) - 1
    # Перевод целой части
    for s in intpart:
        res += int(s) * (8 ** i)
        i -= 1

    # Перевод дробной части
    for s in frpart:
        res += int(s) * (8 ** i)
        i -= 1

    return sign + '{:.4f}'.format(res)

# Функция, выводящая переведенное из 10-й с.с. число
def display_answer1():
    if not is_number(num.get()):  # Проверка, что введено число
        res = 'Введёная строка - не число'
    else:
        res = from_10th_to_8th(num.get())  # Перевод числа из 10-й с.с.
    reslabel.configure(text=res)  # Вывод ответа

# Функция, выводящая переведенное из 8-й с.с. число
def display_answer2():
    if not is_number(num.get()):  # Проверка, что введено число
        res = 'Введёная строка - не число'
    elif not is_8th_sys(num.get()):  # Проверка, что число в 8-ой с.с.
        res = 'Введите число в 8-ой с.с.'
    else:
        res = from_8th_to_10th(num.get())  # Перевод числа из 8-й с.с.
    reslabel.configure(text=res)  # Вывод ответа

# Функция, устанавливающая перевод из 10-й с.с.
def set_10th_sys():
    inlabel.configure(text='Введите число в 10ой с.с. ')  # Изменение поясняющего текста ввода
    outlabel.configure(text='Число в 8ой с.с. ')  # Изменение поясняющего текста вывода
    button.configure(text='Перевести из 10-й с.с.', command=display_answer1)  # Изменение кнопки перевода

# Функция, устанавливающая перевод из 8-й с.с.
def set_8th_sys():
    inlabel.configure(text='Введите число в 8ой с.с. ')  # Изменение поясняющего текста ввода
    outlabel.configure(text='Число в 10ой с.с. ')  # Изменение поясняющего текста вывода
    button.configure(text='Перевести из 8-й с.с.', command=display_answer2)  # Изменение кнопки перевода

# Функция, очищающая поле
def clear_field():
    entry.delete(0, END)
    reslabel.configure(text='-----')

# Функция, выводящая информацию о программе и авторе
def get_ref():
    prog = 'О программе: программа переводит числа из 10-й системы счисления в 8-ю и обратно'
    author = 'Автор: Завойских Е.В., группа ИУ7-23Б'
    messagebox.showinfo('Информация о программе и авторе', prog + '\n' + author)

# Функция, завершающая программу
def exit_prog():
    window.destroy()

# Функции, выводящие в поле выбранные символы
def print_1():
  entry.insert(END, '1')

def print_2():
  entry.insert(END, '2')

def print_3():
  entry.insert(END, '3')

def print_4():
  entry.insert(END, '4')

def print_5():
  entry.insert(END, '5')

def print_6():
  entry.insert(END, '6')

def print_7():
  entry.insert(END, '7')

def print_8():
  entry.insert(END, '8')

def print_9():
    entry.insert(END, '9')

def print_0():
  entry.insert(END, '0')

def print_point():
  entry.insert(END, '.')

def print_minus():
  entry.insert(END, '-')


# Создание окна с указанными размерами и заголовком
window = Tk()
window.geometry('800x250')
window.title('Перевод чисел')

# Создание главного меню
mainmenu = Menu(window)
window.config(menu=mainmenu)

# Создание подменю по заданным действиям
actmenu = Menu(mainmenu, tearoff=0)
actmenu.add_command(label='Перевод из 10-й с.с в 8-ю', command=set_10th_sys)
actmenu.add_command(label='Перевод из 8-й с.с в 10-ю', command=set_8th_sys)

# Добавление подменю и других пунктов в главное меню
mainmenu.add_cascade(label='Заданные действия', menu=actmenu)
mainmenu.add_command(label='Очистка поля', command=clear_field)
mainmenu.add_command(label='О программе', command=get_ref)
mainmenu.add_command(label='Выход', command=exit_prog)


num = StringVar()  # Строка с вводимым числом

# Создание поясняющего текста для ввода
inlabel = Label(text='Введите число в 10ой с.с. ', font='1')
# Расположение текста
inlabel.grid(row=0, column=0, columnspan=3)

# Создание поля для ввода числа
entry = Entry(textvariable=num, font='1')
# Расположение поля
entry.grid(row=0, column=3, columnspan=3)

# Создание кнопки для перевода числа
button = Button(text='Перевести из 10-й с.с.', font='1', command=display_answer1)
# Расположение кнопки
button.grid(row=0, column=7, columnspan=3)

# Создание поясняющего текста для вывода
outlabel = Label(text='Число в 8ой с.с. ', font='1')
# Расположение текста
outlabel.grid(row=1, column=0, columnspan=3)

# Создание надписи с ответом
reslabel = Label(text='-----', font='1')
# Расположение текста
reslabel.grid(row=1, column=3, columnspan=3)

# Создание кнопок для ввода символов в поле
button1 = Button(text='1', font='1', width=2, height=1, command=print_1)
button2 = Button(text='2', font='1', width=2, height=1, command=print_2)
button3 = Button(text='3', font='1', width=2, height=1, command=print_3)
button4 = Button(text='4', font='1', width=2, height=1, command=print_4)
button5 = Button(text='5', font='1', width=2, height=1, command=print_5)
button6 = Button(text='6', font='1', width=2, height=1, command=print_6)
button7 = Button(text='7', font='1', width=2, height=1, command=print_7)
button8 = Button(text='8', font='1', width=2, height=1, command=print_8)
button9 = Button(text='9', font='1', width=2, height=1, command=print_9)
button0 = Button(text='0', font='1', width=2, height=1, command=print_0)
buttonpoint = Button(text='.', font='1', width=2, height=1, command=print_point)
buttonminus = Button(text='-', font='1', width=2, height=1, command=print_minus)

# Расположение кнопок
button1.grid(row=2, column=3)
button2.grid(row=2, column=4)
button3.grid(row=2, column=5)
button4.grid(row=3, column=3)
button5.grid(row=3, column=4)
button6.grid(row=3, column=5)
button7.grid(row=4, column=3)
button8.grid(row=4, column=4)
button9.grid(row=4, column=5)
button0.grid(row=5, column=3)
buttonpoint.grid(row=5, column=4)
buttonminus.grid(row=5, column=5)

window.mainloop()