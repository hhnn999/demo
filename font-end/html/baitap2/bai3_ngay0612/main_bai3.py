import tkinter as tk
from calculator_functions import btn_click, btn_clear, btn_equal

def tao_nut(root, text, hang, cot, entry):
    nut = tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 16), command=lambda: nut_click(text, entry))
    nut.grid(row=hang, column=cot)

def nut_click(gia_tri, entry):
    if gia_tri != '=':
        btn_click(entry, gia_tri)
    elif gia_tri == '=':
        btn_equal(entry)
    elif gia_tri == 'C':
        btn_clear(entry)

goc = tk.Tk()
goc.title("Máy Tính Casio")

entry = tk.Entry(goc, width=16, font=("Arial", 16))
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 1), ('C', 4, 0), ('=', 4, 2), ('+', 4, 3)
]

for (text, hang, cot) in buttons:
    tao_nut(goc, text, hang, cot, entry)

goc.mainloop()
