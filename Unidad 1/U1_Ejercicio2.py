from tkinter import *

root = Tk()
e = Entry(root)
e.pack()
e.focus_set()
#####################################################################
a = 5               #Entero
b = "2"             #String
c = str(a) + b      #Convierte 5 entero a String
#####################################################################
var = IntVar()
e.config(textvariable=var)
var.set(c)
mainloop()
