from tkinter import *
from random import randrange

def damier():
	"Trace le damier"
	y = 0
	while y < 8:
		if y % 2 == 0: # Décale une fois sur deux 
			x = 1      # la position du premier carré noir
		else:
			x = 0
		carre_noir(x*taille_carre, y*taille_carre)
		y += 1

def carre_noir(x, y):
	"Trace les carrés noirs"
	i = 1
	while i < 5:
		can.create_rectangle(x, y, x+taille_carre, y+taille_carre, fill = "black")
		i += 1
		x += taille_carre * 2

taille_carre = 40 # permet de définir une taille de damier modifiable
fen = Tk()
can = Canvas(fen, width = taille_carre * 8, height = taille_carre * 8, bg = "white")
can.pack(side = TOP, padx = 5, pady = 5)
b1 = Button(fen, text = "damier", command = damier)
b1.pack(side = LEFT, padx = 5, pady = 5) 
fen.mainloop()