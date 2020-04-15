from tkinter import *
from random import choice
from tkinter import messagebox
from tkinter import ttk
import sqlite3

class Programita:

    db_ID = 'database.db'

    def __init__(self,window):

        #VENTANA
        self.root = window
        self.root.geometry("700x500")
        self.root.title("Tarea POO")

        self.formulario = Label(self.root, text="Ingrese sus datos", bg="purple1", fg="white", width=80)
        self.formulario.grid(row=0,columnspan=4,sticky=W + E)

        # Titulo Input
        Label(root, text='Titulo: ').grid(row=1, column=0)
        self.titulo = Entry(root)
        self.titulo.focus()
        self.titulo.grid(row=1, column=1)

        # Descripcion Input
        Label(root, text='Descripcion: ').grid(row=2, column=0)
        self.descripcion = Entry(root)
        self.descripcion.grid(row=2, column=1)

        #Table
        self.table = ttk.Treeview(height=10,columns=1)
        self.table["columns"] = ("one","three")
        self.table.grid(row=5,column=0,columnspan=4)
        self.table.heading('#0',text='ID',anchor=CENTER)
        self.table.heading('#1',text='Título',anchor=CENTER)
        self.table.heading('#2',text='Descripción',anchor=CENTER)

        # Button Add Product
        self.button_mostrar_registros = Button(self.root, text="Mostrar registros existentes", width=80).grid(row=4,column=0,columnspan=4,sticky=W + E)
        self.button_alta = Button(self.root, text='Alta', command=self.add_product).grid(row=6, column=1, sticky=W + E)
        self.button_delete = Button(self.root, text='Borrar', command=self.delete_product).grid(row=6, column=2, sticky=W + E)
        # Output Messages
        self.message = Label(text='', fg='red')
        self.message.grid(row=3, column=0, columnspan=2, sticky=W + E)

        self.get_products()

    def run_query(self,query,parameters = ()):
        with sqlite3.connect(self.db_ID) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query,parameters)
            conn.commit()
        return result

    def get_products(self):
        #LIMPIANDO LA TABLA
        records = self.table.get_children()
        for element in records:
            self.table.delete(element)
        #QUERING DATOS
        query = 'SELECT * FROM product ORDER BY ID DESC'
        db_rows = self.run_query(query)
        # RELLENANDO DATOS
        for row in db_rows:
            self.table.insert("",0, text=row[0], values=row[1:])

    def validation(self):
        return len(self.titulo.get()) != 0 and len(self.descripcion.get()) != 0

    def add_product(self):
        if self.validation():
            query = 'INSERT INTO product VALUES(NULL, ?, ?)'
            parameters = (self.titulo.get(), self.descripcion.get())
            self.run_query(query, parameters)
            self.message['text'] = 'Titulo: {}, agregado'.format(self.titulo.get())
            self.titulo.delete(0, END)
            self.descripcion.delete(0, END)
        else:
            self.message['text'] = 'Titulo y descripción requerido'
        self.get_products()

    def delete_product(self):
        self.message['text'] = ''
        try:
            self.table.item(self.table.selection())['text'][0]
        except IndexError as e:
            self.message['text'] = 'Por favor selecciona un ID'
            return
        self.message['text'] = ''
        titulo = self.table.item(self.table.selection())['text']
        query = 'DELETE FROM product WHERE titulo = ?'
        self.run_query(query, (titulo,))
        self.message['text'] = 'Record {} deleted Successfully'.format(titulo)
        self.get_products()

if __name__ == '__main__':
    root = Tk ()
    programa = Programita(root)
    root.mainloop()

