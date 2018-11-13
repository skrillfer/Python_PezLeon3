#!/usr/bin/env python
# -*- coding: utf-8 -*-
#from PyQt4 import QtGui    # or PySide
import codecs
from tkinter import *
from tkinter import ttk

import tkinter.font as FONTS
import modulo_funciones

import os
dir_path = os.getcwd()

class Aplicacion():
    def __init__(self):
        self.raiz = Tk()

        # Gets the requested values of the height and widht.
        windowWidth = self.raiz.winfo_reqwidth()
        windowHeight = self.raiz.winfo_reqheight()
        print("Width",windowWidth,"Height",windowHeight)

        # Gets both half the screen width/height and window width/height
        positionRight = int(self.raiz.winfo_screenwidth()/3 - windowWidth/2)
        positionDown = int(self.raiz.winfo_screenheight()/3 - windowHeight/2)

        # Positions the window in the center of the page.
        self.raiz.geometry("+{}+{}".format(positionRight, positionDown))

        modulo_funciones.informacion_por_defecto()

        background_image = PhotoImage(file = dir_path+"/imagenes/img1.png")
        background_label = ttk.Label(self.raiz, image=background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)


        # Define la dimensión de la ventana
        self.raiz.geometry("550x400")
        self.raiz.resizable(0,0)
        self.raiz.title("Peces Leon")

        self.btn_datos = Button(self.raiz,text='Datos del Pez Leon', padx=5, pady=5,command=self.opcion1)
        self.btn_datos.pack(padx=5, pady=5)
        self.btn_datos.config(bg='#5f7f7a', fg='white')
        self.btn_datos.config(font=('helvetica', 20, 'bold'))

        self.btn_ingresar = Button(self.raiz,text='Ingresar Datos', padx=5, pady=5,command=self.opcion2)
        self.btn_ingresar.pack(padx=5, pady=5)
        self.btn_ingresar.config(bg='#5f7f7a', fg='white')
        self.btn_ingresar.config(font=('helvetica', 20, 'bold'))


        self.btn_estadisticas = Button(self.raiz,text='Estadisticas', padx=5, pady=5,command=self.opcion3)
        self.btn_estadisticas.pack(padx=5, pady=5)
        self.btn_estadisticas.config(bg='#5f7f7a', fg='white')
        self.btn_estadisticas.config(font=('helvetica', 20, 'bold'))

        self.btn_prim_aux = Button(self.raiz,text='Primeros Auxilios', padx=5, pady=5,command=self.opcion4)
        self.btn_prim_aux.pack(padx=5, pady=5)
        self.btn_prim_aux.config(bg='#5f7f7a', fg='white')
        self.btn_prim_aux.config(font=('helvetica', 20, 'bold'))

        self.btn_dat_pez = Button(self.raiz,text='Informacion pez', padx=5, pady=5,command=self.opcion5)
        self.btn_dat_pez.pack(padx=5, pady=5)
        self.btn_dat_pez.config(bg='#5f7f7a', fg='white')
        self.btn_dat_pez.config(font=('helvetica', 20, 'bold'))

        '''
        self.btn_datos.place(x=10, y=10)
        self.btn_ingresar.place(x=10, y=75)
        self.btn_estadisticas.place(x=10, y=150)
        '''
        self.raiz.mainloop()

    def opcion1(self):
        modulo_funciones.datos_pez_leon()

    def opcion2(self):
        modulo_funciones.ingresar_datos()

    def opcion3(self):
        modulo_funciones.mostrar_estadisticas()

    def opcion4(self):
        mostrar_primeros_auxilios()

    def opcion5(self):
        mostrar_informacion_pez()

def mostrar_primeros_auxilios():
    window = Tk()
    window.title("Primeros Auxilios")
    window.geometry('950x450')
    contents = ''
    f = codecs.open(dir_path+"/imagenes/primeros_auxilios.txt", encoding='latin-1')
    for line in f:
        contents += line
    #f=open(dir_path+"/imagenes/primeros_auxilios.txt", "r")
    #contents = f.read()
    #contents = contents.decode('unicode_escape').encode('utf-8')
    lbl = Text(window,height=70, width=100)
    lbl.tag_configure('big', font=('Verdana', 20, 'bold'))
    lbl.tag_configure('color', foreground='blue',
						font=('sans-serif', 10, 'bold'),justify='center')
    lbl.insert(END,'\nPrimeros Auxilios en caso de Picadura del Pez león:\n', 'big')
    lbl.insert(END, contents,'color')
    lbl.pack(side=LEFT)
    window.mainloop()

def mostrar_informacion_pez():
    window = Tk()


    window.title("Primeros Auxilios")
    window.geometry('950x450')

    contents = ''
    f = codecs.open(dir_path+"/imagenes/datos_pez_leon.txt", encoding='latin-1')
    for line in f:
        contents += line
    #f=open(dir_path+"/imagenes/datos_pez_leon.txt", "r")
    #contents =f.read()
    lbl = Text(window,height=70, width=100)
    lbl.tag_configure('big', font=('Verdana', 20, 'bold'))
    lbl.tag_configure('color', foreground='blue',
						font=('sans-serif', 10, 'bold'),justify='center')
    lbl.insert(END,'\nDatos del Pez Leon\n', 'big')
    lbl.insert(END, contents,'color')
    lbl.pack(side=LEFT)

    window.mainloop()

def main():
    mi_app = Aplicacion()
    return 0

if __name__ == '__main__':
    main()
