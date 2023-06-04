import tkinter as tk

ventana = tk.Tk()

textoCaja = tk.StringVar(value='valor por defecto')

alto = 800
ancho = 600

ventana.geometry(f'{alto}x{ancho}')
ventana.title("Plantilla")

ventana.iconbitmap("img/party_mexico_dead_donkey_mexican_pinata_icon_252385.ico")

ventana.mainloop()