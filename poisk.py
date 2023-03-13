from tkinter import *
from tkinter import ttk

import matplotlib.pyplot as plt
import numpy as np

global entry_phi, entry_dist, entry_alfa, entryp, entryd, entrya, entry_signal, entry_target, signal_type, target_type
global signal_select, target_select
global fd, fs, ti, Tc, d, signal_left, signal_right

entry_phi = 0
entry_dist = 0
target_type = 'ПЛ'

root = Tk()

#Функция ввода параметров
def Entry_param():
    global entrya, entryd, entryp, entry_signal, signal_select, target_select
    #Ввод угла фи
    entryp = Entry()
    entryp.insert(0, '45')
    entryp.place(x = 550, y = 50)
    lblp = Label(text = 'Введите пеленг', bg = '#FFF', font = ('Times New Roman', 15))
    lblp.place(x = 550, y = 80)
    #Ввод дистанции
    entryd = Entry()
    entryd.insert(0, '300')
    entryd.place(x = 550, y = 110)
    lbld = Label(text = 'Введите дистанцию до цели', bg = '#FFF', font = ('Times New Roman', 15))
    lbld.place(x = 550, y = 140)
    #Ввод угла альфа
    entrya = Entry()
    entrya.insert(0, '0')
    entrya.place(x = 550, y = 170)
    lbla = Label(text = 'Введите угол движения цели', bg = '#FFF', font = ('Times New Roman', 15))
    lbla.place(x = 550, y = 200)

    #Выбор типа сигнала и цели
    signal_select = ttk.Combobox(root, values = ('Непрерывный', 'Импульсный'), state = 'readonly')
    signal_select.insert(0, 'Непрерывный')
    signal_select.place(x = 550, y = 230)
    target_select = ttk.Combobox(root, values = ('ПЛ', 'Имитатор', 'Облако обломков'), state = 'readonly')
    target_select.place(x = 550, y = 260)

    #Кнопка старт для записи переменных, кнопка Draw для отображения результата в окне вывода
    Button(text = 'Enter', bg = '#FFF', font = ('Times New Roman', 15), command = Enter).place(x = 550, y = 310,
                                                                                               width = 115, height = 30)
    Button(text = 'Draw', bg = '#FFF', font = ('Times New Roman', 15), command = Draw).place(x = 550, y = 340,
                                                                                               width = 115, height = 30)
    Button(text = 'Start', bg = '#FFF', font = ('Times New Roman', 15), command = Water).place(x = 550, y = 370,
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
    global signal_type
    time = np.arange(0, Tc, 1/fd)
    if signal_type == 'Непрерывный':
        signal_left = np.random.randn(time.size)/10
        signal_right = np.random.randn(time.size)/10
        delay = entry_dist/1500
        dt = d/1500 * np.sin(entry_phi)
        for i in range(time.size):
            if time[i] > delay and time[i] < delay + ti:
                signal_left[i] += np.sin(2 * np.pi * fs * time[i])
                signal_right[i] += np.sin(2 * np.pi * fs * time[i] - dt)

        plt.plot(time, signal_left, time, signal_right)
        plt.show(block = False)

    else:
        print('None')


def Sonar():
    global fd, fs, ti, Tc, d
    fd = 80000
    fs = 21000
    ti = 0.1
    d = 0.02
    Tc = 1

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