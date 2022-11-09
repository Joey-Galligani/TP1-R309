from tkinter import *
from tkinter import ttk

# Exercice 1

number = 0

window = Tk()
window.title("ex1")

label = Label(window, text=number)
label.grid(column=0,row=0)

def plus():
    global number
    number += 1
    label.config(text=number)

def moins():
    global number
    number -= 1
    label.config(text=number)

button = Button(window, text="+", command=plus)
button2 = Button(window, text="-", command=moins)

button.grid(column=1, row=2)
button2.grid(column=2, row=2)


window.mainloop()