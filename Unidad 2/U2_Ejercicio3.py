from tkinter import *
root = Tk()
e = Entry(root)
e.pack()
e.focus_set()
###############################################################

f = {"identificador": "3", "nombre":"Diego", "apellido":"Suarez", "telefono":"47293655"}      # Creacion de diccionario (3 claves y 3 valores)
c = len(f)                                                                                    # longuitud de claves del diccionario
d = list(f.keys())                                                                            # Crea una lista que contiene las claves
oracion = "Los elementos son: " , c , "las claves son: " , d                                  # Crea oracion concatenando string y variables

###############################################################
var = IntVar()
e.config(textvariable=var)
var.set(oracion)                                                                              # Imprime en pantalla la variable oracion
mainloop()