from tkinter import *
import datetime
root = Tk()
root.config(bd=3)
root.config(relief="solid")

hoy = StringVar()
hoy.set(datetime.datetime.now().strftime("%d/%m/%Y"))

formulario=Label(root,text="Formulario de datos",bg="green",bd=1, relief="solid").grid(row=0,columnspan=5,sticky="we")
label_id=Label(root,text="id",bg="green",bd=1, relief="solid").grid(row=1,column=1,sticky="we")
label_fecha=Label(root,text="fecha",bg="green",bd=1, relief="solid").grid(row=1,column=2,sticky="we")
label_nombre=Label(root,text="nombre",bg="green",bd=1, relief="solid").grid(row=1,column=3,sticky="we")
label_apellido=Label(root,text="apellido",bg="green",bd=1, relief="solid").grid(row=1,column=4,sticky="we")

a1 = Entry(root,bg="Yellow")
a2 = Entry(root,bg="Yellow",textvariable=hoy,justify="center")
a3 = Entry(root,bg="Yellow")
a4 = Entry(root,bg="Yellow")                       #FILAS Y COLUMNAS DEL a1 a a4 .. PRIMERA FILA
b1 = Entry(root,bg="Yellow")
b2 = Entry(root,bg="Yellow",textvariable=hoy,justify="center")
b3 = Entry(root,bg="Yellow")
b4 = Entry(root,bg="Yellow")                       #FILAS Y COLUMNAS DEL b1 a b4 .. SEGUNDA FILA
c1 = Entry(root,bg="Yellow")
c2 = Entry(root,bg="Yellow",textvariable=hoy,justify="center")
c3 = Entry(root,bg="Yellow")
c4 = Entry(root,bg="Yellow")                       #FILAS Y COLUMNAS DEL c1 a c4 .. TERCER FILA
d1 = Entry(root,bg="Yellow")
d2 = Entry(root,bg="Yellow",textvariable=hoy,justify="center")
d3 = Entry(root,bg="Yellow")
d4 = Entry(root,bg="Yellow")                       #FILAS Y COLUMNAS DEL d1 a d4 .. CUARTA FILA
e1 = Entry(root,bg="Yellow")
e2 = Entry(root,bg="Yellow",textvariable=hoy,justify="center")
e3 = Entry(root,bg="Yellow")
e4 = Entry(root,bg="Yellow")                       #FILAS Y COLUMNAS DEL e1 a e4 .. QUINTA FILA

a1.grid(row=2, column=1)
a2.grid(row=2, column=2)
a3.grid(row=2, column=3)
a4.grid(row=2, column=4)
b1.grid(row=3, column=1)
b2.grid(row=3, column=2)
b3.grid(row=3, column=3)
b4.grid(row=3, column=4)
c1.grid(row=4, column=1)
c2.grid(row=4, column=2)
c3.grid(row=4, column=3)
c4.grid(row=4, column=4)
d1.grid(row=5, column=1)
d2.grid(row=5, column=2)
d3.grid(row=5, column=3)
d4.grid(row=5, column=4)
e1.grid(row=6, column=1)
e2.grid(row=6, column=2)
e3.grid(row=6, column=3)
e4.grid(row=6, column=4)

mainloop()