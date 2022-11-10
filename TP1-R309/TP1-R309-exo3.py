from tkinter import *

def figure_1():
    "dessiner le damier"
    global x,y,damier
    x=0
    y=0
    can.delete(ALL)
    
    damier=[]
    while y<200:
        damier.append(remplir(y))
        y=y+20
    a=0
    while a<8:
        
        al=damier[a]
        b=0
        while b<8:
            al1=al[b]
            can.create_rectangle(al1[0],al1[+1],al1[2],al1[3],fill='white')
            b=b+2   
        a=a+2
    a=1
    while a<8:
        
        al=damier[a]
        b=1
        while b<8:
            al1=al[b]
            can.create_rectangle(al1[0],al1[+1],al1[2],al1[3],fill='white')
            b=b+2   
        a=a+2
        
def remplir(y):
    x=0
    liste=[]
    while x<200:
        liste.append([x,y,x+20,y+20])
        x=x+20
    return liste  
        
global damier
fen = Tk()
can = Canvas(fen, width =158, height =158, bg ='black')
can.pack(side =TOP, padx =5, pady =5)
b1 = Button(fen, text ='damier', command =figure_1)
b1.pack(side =LEFT, padx =3, pady =3)
fen.mainloop()