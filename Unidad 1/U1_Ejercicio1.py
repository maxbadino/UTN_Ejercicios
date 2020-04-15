from tkinter import *

root = Tk()
e = Entry(root)
e.pack()
e.focus_set()
#####################################################################
a = 5                #Entero
b = "2"              #String
c = a + int(b)       #Convierte el string 2 a entero
#####################################################################
var = IntVar()
e.config(textvariable=var)
var.set(c)
mainloop()
