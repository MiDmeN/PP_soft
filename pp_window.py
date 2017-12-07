#!/usr/bin/python
# -*- coding: UTF-8 -*-

from tkinter import *


class PP_window:
    def pp_start(self):
        self.root = Tk()
        self.root.title("Панель управления")  # Заголовок окна
        self.frame = Frame(self.root)
        self.frame.grid()
        self.cp()
        self.pp_cp_bind()
        self.root.mainloop()

    # Получить размеры экрана
    def pp_co(self):
        x, y = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        return x, y

    # Открыть окно
    def pp_op_win(self, event):
        self.pp_win()
        self.pp_cp_bind('open')

    # Закрыть в окно
    def pp_cl_win(self, event):
        self.pp_win('close')
        self.pp_cp_bind('close')

    # Управление окном
    def pp_win(self, state='open'):
        if state == 'open':
            x, y = self.pp_co()
            self.win = Toplevel(self.root)
            self.win.overrideredirect(1)
            self.win.geometry('%dx%d%+d+%d' % ((x / 2), y, (x / 2), 0))
        elif state == 'close':
            self.win.destroy()
        else:
            pass

    # Сформировать панель управления
    def cp(self):
        # Заголовок окна
        pp_top_label = Label(self.frame, text="Поедим-Подумаем", font=('Arial', 20), fg="Red").grid(row=1, column=1,
                                                                                                    columnspan=2,
                                                                                                    sticky=W + E + N + S)
        # Установка времени таймера
        pp_time_label = Label(self.frame, text="Time: ").grid(row=2, column=1, sticky=W)
        isec = Entry(self.frame)
        isec.grid(row=2, column=2, sticky=W)
        isec.insert(0, "60")

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
        ss_t = Button(self.frame, text="Старт", width=w, height=h)
        rs_t = Button(self.frame, text="Сброс", width=w, height=h)

    # Привязка функций к кнопкам
    def pp_cp_bind(self, state='none'):
        if state == 'none':
            self.op.bind("<Button-1>", self.pp_op_win)

        elif state == 'open':
            self.op.config(text="Закрыть окно")
            self.op.bind("<Button-1>", self.pp_cl_win)

        elif state == 'close':
            self.op.config(text="Открыть окно")
            self.op.bind("<Button-1>", self.pp_op_win)

        else:
            pass
