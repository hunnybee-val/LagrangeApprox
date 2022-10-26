import tkinter as tk
from tkinter import *

import numpy as np

import lagrange as p


def valueLagrange():
    a = 0
    b = 2 * np.pi / 3
    x = var.get()*np.pi
    value1 = p.lagrange(5, x, a, b, 1)
    value2 = p.lagrange(5, x, a, b, 0)

    lbl_result["text"] = f"\nL_5({var.get()}pi) = {value1} (первый способ задания узлов)\n" \
                         f"L_5({var.get()}pi) = {value2} (второй способ задания узлов)"
    lbl_calc_res["text"] = f"Результат прямого вычисления: {p.funct(var.get()*np.pi)}\n" \
                           f"Оценка приближения для первого случая: {np.abs(p.funct(var.get()*np.pi)-value1)}\n" \
                           f"Оценка приближения для второго случая: {np.abs(p.funct(var.get()*np.pi)-value2)}\n"

def valueNewton():
    a = 0
    b = 2 * np.pi / 3
    x = var.get() * np.pi
    value_newton = p.newton_poly(x, 5, a, b)
    lbl_result["text"] = f"\nN_5({var.get()}pi) = {value_newton} \n"
    lbl_calc_res["text"] = f"Результат прямого вычисления: {p.funct(var.get() * np.pi)}\n" \
                           f"Оценка приближения: {np.abs(p.funct(var.get() * np.pi) - value_newton)}\n"

def valueHermite():
    x = var.get() * np.pi
    value_hermite = p.hermite(x,5)
    lbl_result["text"] = f"\nH_5({var.get()}pi) = {value_hermite} \n"
    lbl_calc_res["text"] = f"Результат прямого вычисления: {p.funct(var.get() * np.pi)}\n" \
                           f"Оценка приближения: {np.abs(p.funct(var.get() * np.pi) - value_hermite)}\n"

root = tk.Tk()
root.title("Контрольная по численным методам 05-005")
root.geometry("500x400")

lbl1 = tk.Label(text="Выберите значение x: ")
lbl1.pack()

# def sel():
#    selection = "Теперь нажмите кнопку, чтобы интерполировать"
#    label.config(text = selection)

var = DoubleVar()
R1 = Radiobutton(root, text="0.095п", variable=var, value=0.095 )
R1.pack()
R2 = Radiobutton(root, text="0.18п", variable=var, value=0.18)
R2.pack()
R3 = Radiobutton(root, text="0.42п", variable=var, value=0.42)
R3.pack()
R4 = Radiobutton(root, text="п/6 (проверка первого способа задания узлов)", variable=var, value=1/6)
R4.pack()
R5 = Radiobutton(root, text="п/3 (проверка второго способа задания узлов)", variable=var, value=1/3)
R5.pack()

lbl2 = tk.Label(text="Форма построения полинома: ")
lbl2.pack()


btn_convert1 = tk.Button(
    master=root,
    text="Лагранж",
    command=valueLagrange
)
btn_convert2 = tk.Button(
    master=root,
    text="Ньютон",
    command=valueNewton
)
btn_convert3 = tk.Button(
    master=root,
    text="Эрмит-Фейер",
    command=valueHermite
)

lbl_calc_res = tk.Label(master=root)
lbl_result = tk.Label(master=root)


label = Label(root)
btn_convert1.pack()
btn_convert2.pack()
btn_convert3.pack()
lbl_result.pack()
lbl_calc_res.pack()
label.pack()
root.mainloop()