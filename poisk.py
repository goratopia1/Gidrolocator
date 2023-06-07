import random
from tkinter import *
from tkinter import ttk

import matplotlib.pyplot as plt
import numpy as np

global entry_phi, entry_dist, entry_alfa, entryp, entryd, entrya, entry_signal, entry_target, signal_type, target_type, c
global signal_select, target_select
global fd, fs, ti, Tc, d, signal_left, signal_right

entry_phi = 0
entry_dist = 0
c = 1500
target_type = 'ПЛ'

root = Tk()

#Функция ввода параметров
def Entry_param():
    global entrya, entryd, entryp, entry_signal, signal_select, target_select
    #Ввод угла фи
    entryp = Entry()
    entryp.insert(0, '45')
    entryp.place(x = 550, y = 50)
    lblp = Label(text = 'Введите пеленг', bg = '#FFF', font = ('Times New Roman', 15)).place(x = 550, y = 80)
    #Ввод дистанции
    entryd = Entry()
    entryd.insert(0, '300')
    entryd.place(x = 550, y = 110)
    lbld = Label(text = 'Введите дистанцию до цели', bg = '#FFF', font = ('Times New Roman', 15)).place(x = 550, y = 140)
    #Ввод угла альфа
    entrya = Entry()
    entrya.insert(0, '0')
    entrya.place(x = 550, y = 170)
    lbla = Label(text = 'Введите угол движения цели', bg = '#FFF', font = ('Times New Roman', 15)).place(x = 550, y = 200)

    #Выбор типа сигнала и цели
    signal_select = ttk.Combobox(root, values = ('Активный'), state = 'readonly')
    signal_select.place(x = 550, y = 230)
    lbls = Label(text = 'Выберите тип обнаружения', bg = '#FFF', font = ('Times New Roman', 15)).place(x = 550,
                                                                                                       y = 260)
    target_select = ttk.Combobox(root, values = ('ПЛ', 'Облако обломков', 'Имитатор'), state = 'readonly')
    target_select.place(x = 550, y = 290)
    lblt = Label(text = 'Выберите тип цели', bg = '#FFF', font = ('Times New Roman', 15)).place(x = 550, y = 320)

    #Кнопка старт для записи переменных, кнопка Draw для отображения результата в окне вывода
    Button(text = 'Запись', bg = '#FFF', font = ('Times New Roman', 15), command = Enter).place(x = 550, y = 350,
                                                                                               width = 115, height = 30)
    Button(text = 'Рисование', bg = '#FFF', font = ('Times New Roman', 15), command = Draw).place(x = 550, y = 380,
                                                                                               width = 115, height = 30)
    Button(text = 'Старт', bg = '#FFF', font = ('Times New Roman', 15), command = Water).place(x = 550, y = 410,
                                                                                               width = 115, height = 30)


#Функция записи переменных
def Enter():
    global entry_phi, entry_dist, entry_alfa, entry_target, entry_signal, signal_type, target_type
    entry_phi = float(entryp.get())
    entry_phi = np.radians(entry_phi)
    entry_dist = float(entryd.get())
    entry_alfa = float(entrya.get())

    signal_type = signal_select.get()
    target_type = target_select.get()

def Water():
    global signal_type, target_type, entry_dist, dist
    Target()
    time = np.arange(0, Tc, 1/fd)
    signal_left = np.random.randn(time.size) / 10
    signal_right = np.random.randn(time.size) / 10
    delay = entry_dist / 1500
    dt = d / 1500 * np.sin(entry_phi)
    if signal_type == 'Активный':
        for i in range(time.size):
            if time[i] > 2*delay and time[i] < 2*delay + ti:
                    signal_left[i] += 0.8*np.sin(2 * np.pi * fs * time[i])
                    signal_right[i] += 0.8*np.sin(2 * np.pi * fs * time[i] + dt)

    plt.plot(time, signal_left, time, signal_right)
    plt.show(block = False)
    #Определение расстояния до цели
    for t in time:
        if np.abs(t-2*delay+ti)<1/fd:
            m_left = np.argmax(signal_left)
            m_right = np.argmax(signal_right)
            dist_left = (m_left/fd*1500)/2
            dist_right = (m_right/fd*1500)/2
            if dist_left < dist_right:
                dist = dist_left
            else:
                dist = dist_right
    dist = round(dist, 3)
    if len(dist_x) < 9 and len(dist_y) < 9:
        target_type = 'ПЛ'
    elif len(dist_x) < 20 and len(dist_y) < 20:
        target_type = 'Имитатор'
    else:
        target_type = 'Облако обломков'
    label_d = Label(text = 'Дистанция до цели:', bg = '#FFF', font = ('Times New Roman', 15)).place(x = 30, y = 580)
    label_dist = Label(text = str(dist), bg = '#FFF', font = ('Times New Roman', 15)).place(x = 30, y = 610)
    label_t = Label(text = 'Тип цели:', bg = '#FFF', font = ('Times New Roman', 15)).place(x = 30, y = 520)
    label_target = Label(text = '                                 ',
                         bg = '#FFF', font = ('Times New Roman', 15)).place(x = 30, y = 550)
    label_target = Label(text = str(target_type), bg = '#FFF', font = ('Times New Roman', 15)).place(x = 30, y = 550)

#Формирование бликов цели
def Target():
    global dist_x, dist_y
    dist_x = []
    dist_x.append(0)
    dist_y = []
    dist_y.append(0)
    if  target_type == 'ПЛ':
        for i in range(1, 7):
            dist_x.append(dist_x[i-1] + random.randrange(5, 20))
            dist_y.append(dist_y[i-1] + random.randrange(-5, 5))
    elif target_type == 'Имитатор':
        for i in range(1, 10):
            dist_x.append(dist_x[i - 1] + random.randrange(5, 30))
            dist_y.append(dist_y[i - 1] + random.randrange(0, 1))
    elif target_type == 'Облако обломков':
        for i in range(1, 27):
            dist_x.append(dist_x[i - 1] + random.randrange(1, 40))
            dist_y.append(dist_y[i - 1] + random.randrange(-10, 10))

def Sonar():
    global fd, fs, ti, Tc, d
    fd = 40
    fs = 10
    ti = 0.1
    d = 0.02
    Tc = 3


#Функция рисования окна вывода
def Draw():
    global target_type
    canvas  = Canvas(root, width = 500, height = 500, bg = 'gray')
    canvas.place(x = 10, y = 10)
    #Координаты гидролокатора
    x1_gidr = 240
    x2_gidr = 260
    y1_gidr = 240
    y2_gidr = 260
    canvas.create_oval([x1_gidr, y1_gidr], [x2_gidr, y2_gidr], fill = 'blue')
    #Координаты цели
    x_tar_gidr = np.sin(entry_phi)*entry_dist
    y_tar_gidr = np.cos(entry_phi)*entry_dist
    x1_tar = x1_gidr + x_tar_gidr
    y1_tar = y1_gidr - y_tar_gidr
    x2_tar = x2_gidr + x_tar_gidr
    y2_tar = y2_gidr - y_tar_gidr

    if target_type == 'ПЛ':
        canvas.create_rectangle(x1_tar, y1_tar, x2_tar, y2_tar, fill = 'blue')
    elif target_type == 'Имитатор':
        canvas.create_oval(x1_tar, y1_tar, x2_tar, y2_tar, fill = 'green')
    elif target_type == 'Облако обломков':
        canvas.create_oval(x1_tar, y1_tar, x2_tar, y2_tar, fill = 'white')
    canvas.create_line(x1_gidr, y1_gidr, x1_tar, y1_tar, width = 2, fill = 'yellow')

root.geometry('750x700')
root.resizable(False, False)
root.title('Расчет')
Sonar()
Entry_param()
Draw()
root.mainloop()