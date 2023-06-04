import tkinter as tk
from tkinter import ttk, messagebox


def click():
    print(entradaTextos.get())
    boton.config(text=entradaTextos.get())
    entradaTextos.delete(0,tk.END)#borrar desde la poscicion 0 hasta el final

def mensaje():
    messagebox.showinfo("me mostre","hola")

ventana = tk.Tk()

textoCaja = tk.StringVar(value='valor por defecto')

alto = 800
ancho = 600

ventana.geometry(f'{alto}x{ancho}')
ventana.title("Etiqueta / mensaje")
ventana.iconbitmap("img/party_mexico_dead_donkey_mexican_pinata_icon_252385.ico")

#etiqueta
lblNombre = ttk.Label(ventana, text="Nombre")
lblNombre.grid(row=2,column=1)

#entrada de textos 
entradaTextos = ttk.Entry(ventana,width=40, justify=tk.LEFT)
entradaTextos.grid(row=2, column=2, padx=20, pady=20)

boton = ttk.Button(ventana, text="click", command=click)
boton.grid(row=5, column=2)

boton = ttk.Button(ventana, text="mensaje", command=mensaje)
boton.grid(row=5, column=4)

ventana.mainloop()