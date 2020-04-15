from tkinter import *
root = Tk()
e = Entry(root)
e.pack()
e.focus_set()
###############################################################
frutas = ["limon", "frutilla","sandia","banana","naranja","uva","pera"]         #Lista de 7 objetos (strings)
###############################################################
var = IntVar()
e.config(textvariable=var)
var.set(frutas[2])                                                              #Muestra el tercer objeto de la lista frutas
mainloop()