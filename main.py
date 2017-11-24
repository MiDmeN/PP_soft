#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
import window
from Tkinter import *


class PP_soft:
    def __init__(self):
        self.root = Tk()
        self.root.title("Панель управления")
        self.frame = Frame(self.root)
        self.frame.grid()
        window.cp(self)

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
        print(self.s)
        min, sec = self.minsec(self.s)
        self.second = self.canvas.create_text((self.ww / 2), (self.wh / 2), text=(min + ':' + sec), font=('Arial', 300))

        if self.s > 10:
            print ("Many")
            self.canvas.itemconfig(self.second, fill="White")
        elif 10 >= self.s > 0:
            print ("Middle")
            self.canvas.itemconfig(self.second, fill="Red")
        else:
            print ("Low")
            self.canvas.itemconfig(self.second, fill="Yellow")

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
        self.canvas = Canvas(self.win, width=(self.x / 2), height=self.y, bg="Black")
        self.canvas.pack(fill=BOTH, expand=1)
        self.wh, self.ww = self.canvas.canvasx(self.win.winfo_height()), self.canvas.canvasy(self.win.winfo_width())
        self.init_timer()
        self.ss_t.grid(row=9, column=1, columnspan=2)
        self.rs_t.grid(row=10, column=1, columnspan=2)

    #Таймер обратного отсчета
    def timer(self, event):
        self.st = 0
        self.ss_t.config(text="Стоп")
        self.ss_t.bind("<Button-1>", self.st_t)
        while self.s >= 1:
            if self.st == 1:
                break

            time.sleep(1)
            self.root.update()
            self.canvas.delete(self.second)
            self.s -= 1
            self.init_timer()
        else:
            time.sleep(1)
            self.root.update()
            self.canvas.delete(self.second)
            self.init_timer()


    #Остановка таймера
    def st_t(self, event):
        self.st=1
        self.s=1

    # Сбросить счетчик таймер
    def res_t(self, event):
        self.s = int(self.isec.get())
        self.root.update()
        self.canvas.delete(self.second)
        self.init_timer()
        self.ss_t.config(text="Старт")
        self.ss_t.bind("<Button-1>", self.timer)

    @property
    def start(self):
        self.root.mainloop()


PP_soft().start
