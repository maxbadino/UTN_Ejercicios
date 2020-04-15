import random
from tkinter import *

root = Tk()
e = Entry(root)
e.pack()
e.focus_set()
#####################################################################
a = 5                               #Entero
b = "2"                             #String
c = a + int(b)                      #Convierte el string 2 a entero y suma las variabless a y b
d = c * random.randint(0, 10)       #Multplica "c" por un numero random entre (0 y 10)
#####################################################################
var = IntVar()
e.config(textvariable=var)
var.set(d)                          #Modifique "c" por "d" para obtener el resultado de "d"
mainloop()
