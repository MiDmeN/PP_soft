#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Tkinter import *
import time


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

    # Таймер обратного отсчета
    def w_timer(self, event):
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

    # Остановка таймера
    def st_t(self, event):
        self.st = 1
        self.s = 1

    # Сбросить счетчик таймер
    def res_t(self, event):
        self.s = int(self.isec.get())
        self.root.update()
        self.canvas.delete(self.second)
        self.init_timer()
        self.ss_t.config(text="Старт")
        self.ss_t.bind("<Button-1>", self.timer)
