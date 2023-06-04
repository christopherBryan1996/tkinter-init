import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()

ventana.title("Posicionar componentes")

ancho = 600
alto = 500

ventana.iconbitmap("img/household_furniture_library_bookcase_book_bookshelf_icon_252382.ico")

ventana.geometry(f'{ancho}x{alto}')

ventana.rowconfigure(0, weight=2)
ventana.rowconfigure(1,weight=4)

boton01 = ttk.Button(ventana,text="Boton1")
boton01.grid(row=1,column=0, sticky="S")

boton02 = ttk.Button(ventana,text="Boton2")
boton02.grid(row=1,column=1, sticky="N")

boton03 = ttk.Button(ventana,text="Boton2")
boton03.grid(row=2,column=1, sticky="W")

boton04 = ttk.Button(ventana,text="Boton2")
boton04.grid(row=1,column=3, sticky="E")

ventana.mainloop()