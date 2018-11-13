#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tkinter import *
import tkinter as tk
from tkinter import ttk


#Muestra una treeview para visualizar de forma jerarquiza los datos de la lista de paises
class Application(ttk.Frame):

    def __init__(self, main_window,lista):
        super().__init__(main_window)
        main_window.title("Informacion")

        self.treeview = ttk.Treeview(self)

        self.menubar = tk.Menu(self)
        self.winfo_toplevel().configure(menu=self.menubar)


        self.yscrollbar = ttk.Scrollbar(self, orient='vertical', command=self.treeview.yview)
        self.treeview.configure(yscrollcommand=self.yscrollbar.set)
        self.yscrollbar.pack(side="right", fill="y")

        self.treeview.pack(side="left", fill="both", expand=True)
        agregar(self,lista)
        for w in (self, main_window):
            w.rowconfigure(0, weight=1)
            w.columnconfigure(0, weight=1)
        self.pack()

#Se insertar pais por pais de la lista y por cada pais se inserta un puerto y su Informacion
def agregar(self,lista):
    padre1 = self.treeview.insert("", tk.END, text="Paises",open=True)
    for pais in lista:
        padre2 = self.treeview.insert(padre1, tk.END, text=pais.nombre,open=True)
        for puerto in pais.Puertos:
            padre3 = self.treeview.insert(padre2, tk.END, text=puerto.nombre,open=True)
            self.treeview.insert(padre3, tk.END, text='Vistos:'+str(puerto.pecesVistos))
            self.treeview.insert(padre3, tk.END, text='Pescados:'+str(puerto.pecesPescados))

#Crea una nueva Application
def crear(lista):
    main_window = tk.Tk()
    app = Application(main_window,lista)
    app.mainloop()
