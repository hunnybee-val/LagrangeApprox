import tkinter as tk
import numpy as np
from tkinter import *
import lagrange as p

def valueLagrange():
    x = var.get()
    value = p.lagrange(5, x, 0, 2 * np.pi / 3)
    lbl_result["text"] = value

root = tk.Tk()
root.title("Контрольная по численным методам 05-005")
root.geometry("500x200")

lbl_preview = tk.Label(text="Выберите значение x: ")
lbl_preview.pack()

def sel():
   selection = "Теперь нажмите кнопку, чтобы интерполировать"
   label.config(text = selection)

var = IntVar()
R1 = Radiobutton(root, text="0.095п", variable=var, value=0.095*np.pi, command=sel)
R1.pack()
R2 = Radiobutton(root, text="0.18п", variable=var, value=0.18*np.pi, command=sel)
R2.pack()
R3 = Radiobutton(root, text="0.42п", variable=var, value=0.42*np.pi, command=sel)
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