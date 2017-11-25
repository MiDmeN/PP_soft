#!/usr/bin/python
# -*- coding: UTF-8 -*-
import window
import timer
from Tkinter import *


class PP_soft:
    def __init__(self):
        self.root = Tk()
        self.root.title("Панель управления")
        self.frame = Frame(self.root)
        self.frame.grid()
        window.cp(self)


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
        timer.init_timer(self)
        self.ss_t.grid(row=9, column=1, columnspan=2)
        self.rs_t.grid(row=10, column=1, columnspan=2)


    @property
    def start(self):
        self.root.mainloop()


PP_soft().start
