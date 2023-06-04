import tkinter as tk
from tkinter import ttk, scrolledtext

ventana = tk.Tk()

textoCaja = tk.StringVar(value='valor por defecto')

alto = 800
ancho = 600

ventana.geometry(f'{alto}x{ancho}')
ventana.title("Varios, scroll / combo")

ventana.iconbitmap("img/party_mexico_dead_donkey_mexican_pinata_icon_252385.ico")

text = 'El número de núcleos de su procesador es uno de los componentes que determinan el rendimiento de tu CPU y, por ende, de tu ordenador. En el pasado, cada procesador tenía solo un núcleo. En cambio, las CPU modernas tienen de cuatro a dieciocho, de media (y llegan incluso a 128)'
scroll = scrolledtext.ScrolledText(ventana, width = 30, height=5, wrap=tk.WORD)
scroll.insert(tk.INSERT, text)
scroll.grid(row=1,column=1)

datos = [x*3 for x in range(20)]
combobox = ttk.Combobox(ventana, width=15, values=datos)
combobox.grid(row=5,column=1,padx=15, pady=15)
combobox.current(3)
print(f'Mostando el valor del combo al iniciar ventana {combobox.get()}')

imagen = tk.PhotoImage(file='img/images.png')
boton = ttk.Button(ventana, image=imagen)
boton.grid(row=6, column=1)

ventana.mainloop()