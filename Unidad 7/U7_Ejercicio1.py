from tkinter import *
from random import choice
from tkinter import messagebox

class Programita:
    def __init__(self,window):

        #VENTANA
        self.root = window
        self.root.geometry("450x150")
        self.root.title("Tarea POO")

        #FUNCION 1
        def imprimir():
            if titulo.get() == "" and ruta.get() == "" and descripcion.get() == "":
                messagebox.showinfo("ERROR", "No cargaste ningun dato")
            else:
                print(titulo.get())
                print(ruta.get())
                print(descripcion.get())
                titulo.set("")
                ruta.set("")
                descripcion.set("")
        #FUNCION 2
        def colorear():
            root.configure(bg=choice(colores))

        colores = ['snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white', 'old lace',
                'linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff',
                'navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender',
                'lavender blush', 'misty rose', 'dark slate gray', 'dim gray', 'slate gray',
                'light slate gray', 'gray', 'light grey', 'midnight blue', 'navy', 'cornflower blue', 'dark slate blue',
                'slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue',  'blue',
                'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue',
                'light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise',
                'cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green',
                'dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'spring green',
                'lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green',
                'forest green', 'olive drab', 'dark khaki', 'khaki', 'pale goldenrod', 'light goldenrod yellow',
                'light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod', 'dark goldenrod', 'rosy brown',
                'indian red', 'saddle brown', 'sandy brown',
                'dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange',
                'coral', 'light coral', 'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pink', 'light pink',
                'pale violet red', 'maroon', 'medium violet red', 'violet red',
                'medium orchid', 'dark orchid', 'dark violet', 'blue violet', 'purple', 'medium purple',
                'thistle', 'snow2', 'snow3',
                'snow4', 'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1', 'AntiqueWhite2',
                'AntiqueWhite3', 'AntiqueWhite4', 'bisque2', 'bisque3', 'bisque4', 'PeachPuff2',
                'PeachPuff3', 'PeachPuff4', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4',
                'LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'cornsilk2', 'cornsilk3',
                'PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'maroon1', 'maroon2',
                'maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4',
                'magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'plum1',
                'plum2', 'plum3', 'plum4', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3',
                'MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4',
                'purple1', 'purple2', 'purple3', 'purple4', 'MediumPurple1', 'MediumPurple2',
                'MediumPurple3', 'MediumPurple4', 'thistle1', 'thistle2', 'thistle3', 'thistle4',
                'gray1']

        #VARIABLES
        titulo = StringVar()
        ruta = StringVar()
        descripcion = StringVar()

        #LABELS
        formulario = Label(self.root,text="Ingrese sus datos",bg="purple1")
        formulario.pack(fill="x")
        formulario.config(fg="white")
        self.label_titulo = Label(self.root,text="Título").place(x=10,y=30)
        self.label_ruta = Label(self.root,text="Ruta").place(x=10,y=50)
        self.label_descripcion = Label(self.root,text="Descripción").place(x=10,y=70)

        #ENTRYS
        self.entry_titulo = Entry(self.root,textvariable=titulo).place(x=150,y=30)
        self.entry_ruta = Entry(self.root,textvariable=ruta).place(x=150,y=50)
        self.entry_descripcion= Entry(self.root,textvariable=descripcion).place(x=150,y=70)

        #BUTTONS
        self.button_alta = Button(self.root,text="Alta",command=imprimir).place(x=200,y=100)
        self.button_sorpresa = Button(self.root,text="Sorpresa",command=colorear).place(x=320,y=100)

if __name__ == '__main__':
    root = Tk ()
    programa = Programita(root)
    root.mainloop()

