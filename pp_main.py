#!/usr/bin/python
# -*- coding: UTF-8 -*-
# from tkinter import *

# import pp_timer
import pp_window


class PP_soft:
    def __init__(self):
        win = pp_window.PP_window()
        win.pp_start()

        # self.root = Tk()
        # self.root.title("Панель управления")
        # self.frame = Frame(self.root)
        # self.frame.grid()
        # pp_window.cp(self)

    # # Открыть окно
    # def op_win(self, event):
    #     self.win = Toplevel(self.root)
    #     self.win.overrideredirect(1)
    #     self.win.geometry('%dx%d%+d+%d' % ((self.x / 2), self.y, (self.x / 2), 0))
    #     self.op.config(text="Закрыть окно")
    #     self.op.bind("<Button-1>", self.cl_win)
    #
    # # Закрыть окно
    # def cl_win(self, event):
    #     self.win.destroy()
    #     self.op.config(text="Открыть окно")
    #     self.op.bind("<Button-1>", self.op_win)
    #
    #
    # @property
    # def start(self):
    #     self.root.mainloop()
    #
    #


PP_soft()
