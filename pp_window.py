#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Tkinter import *
import timer

# Сформировать панель управления
# @property
def cp(self):
    print("OK")
    # Получаем размер экрана
    self.x, self.y = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
    print self.x, self.y
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
    self.ss_t = Button(self.frame, text="Старт", width=w, height=h)
    self.rs_t = Button(self.frame, text="Сброс", width=w, height=h)

    # Привязка кнопок
    self.op.bind("<Button-1>", self.op_win)
    op_t.bind("<Button-1>", self.c_timer)
    # self.ss_t.bind("<Button-1>", timer.w_timer)
    self.rs_t.bind("<Button-1>", timer.res_t(self))
