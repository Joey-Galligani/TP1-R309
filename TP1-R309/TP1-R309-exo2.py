from re import A
from tkinter import *
from tkinter import ttk

# Exercice 2

window = Tk()
window.title("ex1")
window.geometry("250x100")

label = Label(window, text="Veuillez entrer votre Email :")
label.grid(column=0,row=0)

varmail=StringVar()
mail=Entry(textvariable=varmail)
mail.focus_set()
mail.grid(column=0, row=3)

a=NORMAL

def verif():
    varmail=""
    if varmail.find(" ") != -1 :
        a=DISABLED
    if varmail.find("@") == -1 :
        a=DISABLED
    if varmail.find(".") == -1 :
        a=DISABLED
    return a

    

button = Button(window, text="Vérifier", command=verif, state=a)

button.grid(column=10, row=5)



window.mainloop()