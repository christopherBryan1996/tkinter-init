import tkinter as tk
from tkinter import ttk



def click():
    print(entradaTextos.get())
    boton.config(text=entradaTextos.get())
    entradaTextos.delete(0,tk.END)#borrar desde la poscicion 0 hasta el final
    entradaTextos01.focus()

ventana = tk.Tk()

textoCaja = tk.StringVar(value='valor por defecto')

alto = 800
ancho = 600

ventana.geometry(f'{alto}x{ancho}')
ventana.title("Caja de textos")
ventana.iconbitmap("img/party_mexico_dead_donkey_mexican_pinata_icon_252385.ico")

#entrada de textos 
entradaTextos = ttk.Entry(ventana,width=40, justify=tk.LEFT)
entradaTextos.grid(row=1, column=4, padx=20, pady=20)
# primer parametro es la posiscion donde quieres poner el texto y el segundo que vas a poner 
entradaTextos.insert(0,'cadena de texto por defecto')
#entradaTextos.insert(7,'cadena')
entradaTextos.insert(tk.END, "///")

#Otras propiedades
entradaTextos01 = ttk.Entry(ventana, width=40, justify=tk.RIGHT, show='*')
entradaTextos01.grid(row=3, column=4, ipadx=20, ipady=20)
#poniendo este estado ya no nose deja modificar el texto
#entradaTextos01.config(state='readonly')

entradaTextos03 = ttk.Entry(ventana, width=40, justify=tk.LEFT)
entradaTextos03.grid(row=4, column=4, ipadx=20, ipady=20)


boton = ttk.Button(ventana, text="click", command=click)
boton.grid(row=5, column=4)

ventana.mainloop()