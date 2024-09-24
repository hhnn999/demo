import tkinter as hoang

def btn_click(entry, value):
    current = entry.get()
    entry.delete(0, hoang.END)
    entry.insert(hoang.END, str(current) + str(value))

def btn_clear(entry):
    entry.delete(0, hoang.END)

def btn_equal(entry):
    try:
        current = entry.get()
        result = eval(current)
        entry.delete(0, hoang.END)
        entry.insert(hoang.END, str(result))
    except Exception as e:
        entry.delete(0, hoang.END)
        entry.insert(hoang.END, "Error")