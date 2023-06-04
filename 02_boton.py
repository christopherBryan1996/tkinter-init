import tkinter as tk 
from tkinter import ttk

ventana = tk.Tk()

ventana.title("Botón")

ancho = 800
alto = 600

tamaño = f"{ancho}x{alto}"

ventana.geometry(tamaño)

#poner icon personalizado 
ventana.iconbitmap("img/fantasma.ico")

#poner boton
boton=ttk.Button(ventana,text="Click")
#para mostrar boton
boton.pack()

ventana.mainloop()