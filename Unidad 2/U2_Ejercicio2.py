from tkinter import *
root = Tk()
e = Entry(root)
e.pack()
e.focus_set()
###############################################################
frutas = ["limon", "frutilla"]                                                  #lista de 2 objetos
oracion = "Me gusta el " + frutas[0] + " y la " + frutas[1]                     #concatenacion de strings y objetos de la lista
###############################################################
var = IntVar()
e.config(textvariable=var)
var.set(oracion)
mainloop()