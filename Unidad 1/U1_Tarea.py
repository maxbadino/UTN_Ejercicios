from tkinter import *

root = Tk()
e = Entry(root)
e.pack()
e.focus_set()
#####################################################################
a = 5                                 #Entero
b = random.randrange(100)             #Asigna a "b" un numero aleatorio del 0 al 100
c = a + b                             #suma las dos variables
#####################################################################
var = IntVar()
e.config(textvariable=var)
var.set(c)
mainloop()
"""
el siguiente metodo random.randrange(100), da un numero aleatorio dentro de un rango que se asigne entre parentesis 
en este caso, da un numero aleatorio entre 0 y 100.
"""
