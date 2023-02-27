from tkinter import *

global entry_phi, entry_dist, entry_alfa, entryp, entryd, entrya
entry_phi = 0
entry_dist = 0
root = Tk()

#Функция ввода параметров
def Entry_param():
    global entrya, entryd, entryp
    #Ввод угла фи
    entryp = Entry()
    entryp.place(x = 550, y = 50)
    lblp = Label(text = 'Entry phi', bg = '#FFF', font = ('Times New Roman', 15))
    lblp.place(x = 550, y = 80)
    #Ввод дистанции
    entryd = Entry()
    entryd.place(x = 550, y = 110)
    lbld = Label(text = 'Entry dist', bg = '#FFF', font = ('Times New Roman', 15))
    lbld.place(x = 550, y = 140)
    #Ввод угла альфа
    entrya = Entry()
    entrya.place(x = 550, y = 170)
    lbla = Label(text = 'Entry alfa', bg = '#FFF', font = ('Times New Roman', 15))
    lbla.place(x = 550, y = 200)

    Button(text = 'Start', bg = '#FFF', font = ('Times New Roman', 15), command = start).place(x = 550, y = 250,
                                                                                               width = 115, height = 30)
    Button(text = 'Draw', bg = '#FFF', font = ('Times New Roman', 15), command = Draw).place(x = 550, y = 280,
                                                                                               width = 115, height = 30)


#Функция записи переменных и их счет
def start():
    global entry_phi, entry_dist, entry_alfa
    entry_phi = int(entryp.get())
    entry_dist = int(entryd.get())
    entry_alfa = int(entrya.get())
    #Result = entry_dist+entry_alfa+entry_phi
    #lbl = Label(text = Result, bg = '#FFF', font = ('Times New Roman', 15))
    #lbl.place(x = 150, y = 600)

#Функция рисования окна вывода
def Draw():
    canvas  = Canvas(root, width = 500, height = 500, bg = 'gray')
    canvas.place(x = 10, y = 10)
    #Координаты гидролокатора
    x1_gidr = 240
    x2_gidr = 260
    y1_gidr = 480
    y2_gidr = 500
    canvas.create_oval([x1_gidr, y1_gidr], [x2_gidr, y2_gidr], fill = 'blue')
    #Координаты цели
    x1_cel = 400
    y1_cel = 100
    x2_cel = 410
    y2_cel = 110
    canvas.create_rectangle(x1_cel, y1_cel, x2_cel, y2_cel, fill = 'blue')
    canvas.create_line(x1_gidr, y1_gidr, x1_cel, y1_cel, width = 2, fill = 'yellow')
    #print(x1_cel, y1_cel, x2_cel, y2_cel)

root.geometry('750x700')
root.resizable(False, False)
root.title('Расчет')
Entry_param()
Draw()
root.mainloop()