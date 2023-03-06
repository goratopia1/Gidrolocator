from tkinter import *
from tkinter import ttk
import math


global entry_phi, entry_dist, entry_alfa, entryp, entryd, entrya, entry_signal, entry_target, signal_type, target_type
global signal_select, target_select
global fd, fs, ti, Tc, d
entry_phi = 0
entry_dist = 0
root = Tk()

#Функция ввода параметров
def Entry_param():
    global entrya, entryd, entryp, entry_signal, signal_select, target_select
    #Ввод угла фи
    entryp = Entry()
    entryp.place(x = 550, y = 50)
    lblp = Label(text = 'Введите угол фи', bg = '#FFF', font = ('Times New Roman', 15))
    lblp.place(x = 550, y = 80)
    #Ввод дистанции
    entryd = Entry()
    entryd.place(x = 550, y = 110)
    lbld = Label(text = 'Введите дистанцию до цели', bg = '#FFF', font = ('Times New Roman', 15))
    lbld.place(x = 550, y = 140)
    #Ввод угла альфа
    entrya = Entry()
    entrya.place(x = 550, y = 170)
    lbla = Label(text = 'Введите угол движения цели', bg = '#FFF', font = ('Times New Roman', 15))
    lbla.place(x = 550, y = 200)

    #Выбор типа сигнала и цели
    #signal_value = ['Непрерывный', 'Импульсный']
    signal_select = ttk.Combobox(root, values = ('Непрерывный', 'Импульсный'), state = 'readonly')
    signal_select.place(x = 550, y = 230)
    #target_value = ['ПЛ', 'Имитатор', 'Облако обломков']
    target_select = ttk.Combobox(root, values = ('ПЛ', 'Имитатор', 'Облако обломков'), state = 'readonly')
    target_select.place(x = 550, y = 260)

    #Кнопка старт для записи переменных, кнопка Draw для отображения результата в окне вывода
    Button(text = 'Start', bg = '#FFF', font = ('Times New Roman', 15), command = Start).place(x = 550, y = 310,
                                                                                               width = 115, height = 30)
    Button(text = 'Draw', bg = '#FFF', font = ('Times New Roman', 15), command = Draw).place(x = 550, y = 340,
                                                                                               width = 115, height = 30)


#Функция записи переменных и их счет
def Start():
    global entry_phi, entry_dist, entry_alfa, entry_target, entry_signal
    entry_phi = float(entryp.get())
    entry_phi = math.radians(entry_phi)
    entry_dist = float(entryd.get())
    entry_alfa = float(entrya.get())

    signal_type = signal_select.get()
    target_type = target_select.get()


#Функция рисования окна вывода
def Draw():
    canvas  = Canvas(root, width = 500, height = 500, bg = 'gray')
    canvas.place(x = 10, y = 10)
    #Координаты гидролокатора
    x1_gidr = 240
    x2_gidr = 260
    y1_gidr = 240
    y2_gidr = 260
    canvas.create_oval([x1_gidr, y1_gidr], [x2_gidr, y2_gidr], fill = 'blue')
    #Координаты цели
    x_tar_gidr = math.sin(entry_phi)*entry_dist
    y_tar_gidr = math.cos(entry_phi)*entry_dist
    x1_tar = x1_gidr + x_tar_gidr
    y1_tar = y1_gidr - y_tar_gidr
    x2_tar = x2_gidr + x_tar_gidr
    y2_tar = y2_gidr - y_tar_gidr
    canvas.create_rectangle(x1_tar, y1_tar, x2_tar, y2_tar, fill = 'blue')
    canvas.create_line(x1_gidr, y1_gidr, x1_tar, y1_tar, width = 2, fill = 'yellow')

root.geometry('750x700')
root.resizable(False, False)
root.title('Расчет')
Entry_param()
Draw()
root.mainloop()