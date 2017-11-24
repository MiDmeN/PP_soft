#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Tkinter import *


class PP_soft:
    def __init__(self):
        self.root = Tk()
        self.root.title("Панель управления")
        self.frame = Frame(self.root)
        self.frame.grid()
        self.cp

    # Сформировать панель управления
    @property
    def cp(self):
        # Получаем размер экрана
        self.x, self.y = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        # Заголовок окна
        label = Label(self.frame, text="Поедим-Подумаем", font=('Arial', 20), fg="Red").grid(row=1, column=1,
                                                                                             columnspan=2,
                                                                                             sticky=W + E + N + S)
        # Установка времени таймера
        label1 = Label(self.frame, text="Time: ").grid(row=2, column=1, sticky=W)
        self.isec = Entry(self.frame)
        self.isec.grid(row=2, column=2, sticky=W)
        self.isec.insert(0, "60")

        # Блок кнопок
        w = 25
        h = 2
        self.op = Button(self.frame, text="Открыть окно", width=w, height=h)
        self.op.grid(row=3, column=1, columnspan=2)
        op_sp = Button(self.frame, text="Показать заставку", width=w, height=h)
        op_sp.grid(row=4, column=1, columnspan=2)
        op_t = Button(self.frame, text="Показать таймер", width=w, height=h)
        op_t.grid(row=5, column=1, columnspan=2)
        op_r5 = Button(self.frame, text="Результаты 5х5", width=w, height=h)
        op_r5.grid(row=6, column=1, columnspan=2)
        op_m1 = Button(self.frame, text="Результаты осн Ч1", width=w, height=h)
        op_m1.grid(row=7, column=1, columnspan=2)
        op_m2 = Button(self.frame, text="Результаты осн Ч2", width=w, height=h)
        op_m2.grid(row=8, column=1, columnspan=2)
        start_t = Button(self.frame, text="Старт", width=w, height=h)
        rs_t = Button(self.frame, text="Сброс", width=w, height=h)

        # Привязка кнопок
        self.op.bind("<Button-1>", self.op_win)
        op_t.bind("<Button-1>", self.c_timer)

    def minsec(self, sec):
        min = (sec // 60) % 60
        if min < 10:
            min = '0' + str(min)
        else:
            min = str(min)
        sec = sec % 60
        if sec < 10:
            sec = '0' + str(sec)
        else:
            sec = str(sec)
        return min, sec

    def init_timer(self):
        min, sec = self.minsec(self.s)
        second = self.canvas.create_text((self.ww / 2), (self.wh / 2), text=(min + ':' + sec), font=('Arial', 300), fill="White")
#        if self.s > 10:
#            print ("Many")
#        else:
#            print ("Low")

    # Открыть окно
    def op_win(self, event):
        self.win = Toplevel(self.root)
        self.win.overrideredirect(1)
        self.win.geometry('%dx%d%+d+%d' % ((self.x / 2), self.y, (self.x / 2), 0))
        self.op.config(text="Закрыть окно")
        self.op.bind("<Button-1>", self.cl_win)

    # Закрыть окно
    def cl_win(self, event):
        self.win.destroy()
        self.op.config(text="Открыть окно")
        self.op.bind("<Button-1>", self.op_win)

    # открыть таймер
    def c_timer(self, event):
        self.s = int(self.isec.get())
        print(self.s)
        self.canvas = Canvas(self.win, width=(self.x / 2), height=self.y, bg="Black")
        self.canvas.pack(fill=BOTH, expand=1)
        self.wh, self.ww = self.canvas.canvasx(self.win.winfo_height()), self.canvas.canvasy(self.win.winfo_width())
        self.init_timer()
#        start_t.grid(row=9, column=1, columnspan=2)
#        rs_t.grid(row=10, column=1, columnspan=2)

    @property
    def start(self):
        self.root.mainloop()


PP_soft().start
