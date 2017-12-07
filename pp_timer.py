#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
import pp_window
from tkinter import *


# открыть таймер
def c_timer(event):
    # s = int(pp_window.isec.get())
    canvas = Canvas(win, width=(pp_window.x / 2), height=pp_window.y, bg="Black")
    canvas.pack(fill=BOTH, expand=1)
    wh, ww = canvas.canvasx(self.win.winfo_height()), canvas.canvasy(self.win.winfo_width())
    pp_timer.init_timer(self)
    self.ss_t.grid(row=9, column=1, columnspan=2)
    self.rs_t.grid(row=10, column=1, columnspan=2)


# разделение секунд на минуты и секунды
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


#отображение таймер и его цвета
def init_timer(self):
    print(self.s)
    min, sec = minsec(self, self.s)
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


# Таймер обратного отсчета
def w_timer(event):
    st = 0
    pp_window.change_ss_but(1)
    while self.s >= 1:
        if st == 1:
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


# Остановка таймера
def st_t(self, event):
    st = 1
    self.s = 1


# Сбросить счетчик таймер
def res_t(event):
    s = int()
    root.update()
    canvas.delete(self.second)
    self.init_timer()
    pp_window.change_ss_but(0)
