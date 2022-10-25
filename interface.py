import tkinter as tk
import numpy as np
from tkinter import *
import lagrange as p

def valueLagrange():
    a = 0
    b = 2 * np.pi / 3
    x = var.get()*np.pi
    value = p.lagrange(5, x, a, b)
    lbl_result["text"] = value

root = tk.Tk()
root.title("Контрольная по численным методам 05-005")
root.geometry("500x200")

lbl_preview = tk.Label(text="Выберите значение x: ")
lbl_preview.pack()

def sel():
   selection = "Теперь нажмите кнопку, чтобы интерполировать"
   label.config(text = selection)

var = DoubleVar()
R1 = Radiobutton(root, text="0.095п", variable=var, value=0.095, command=sel)
R1.pack()
R2 = Radiobutton(root, text="0.18п", variable=var, value=0.18, command=sel)
R2.pack()
R3 = Radiobutton(root, text="0.42п", variable=var, value=0.42, command=sel)
R3.pack()


btn_convert = tk.Button(
    master=root,
    text="Интерполировать",
    command=valueLagrange
)
lbl_result = tk.Label(master=root, text="здесь появится результат")


label = Label(root)
lbl_result.pack()
btn_convert.pack()
label.pack()
root.mainloop()