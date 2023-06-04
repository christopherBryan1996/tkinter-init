import tkinter as tk

#creamos objeto de la clase tk
ventana =tk.Tk()
ancho = 800
alto=600
tamaño =f'{ancho}x{alto}'
print(tamaño)
#tamaño
ventana.geometry(tamaño)
#titulo
ventana.title("Primera vetana")
#importante poner, para q se ejecute continuamente 
ventana.mainloop()